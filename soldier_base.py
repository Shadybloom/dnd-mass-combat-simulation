#!/usr/bin/env python
# -*- coding: utf-8 -*-

import uuid
import math
import random
import copy

import dices
from data import chars
from data import animals
from data import races
from data import classes
from data import squads
from data import items
from data import spells
import config

#-------------------------------------------------------------------------
# Функции:

def translate_to_lang(*wordlist, dict_words):
    """Переводит строку/список английских слов в строку из словаря.
    
    Принимает простые строки, вроде 'first light and second light'.
    Если не может перевести, то слово так и остаётся на своём месте.
    """
    wordlist = ' '.join(wordlist).split()
    # Вот так-то, Шейд. Я тоже умею в крутые однострочники!
    wordlist = list(map(lambda word: dict_words.get(word,word), wordlist))
    return wordlist

def gen_name(dict_words, name_length = 2):
    """Имя из словаря.

    Словарь в формате:
    'слово_понятное':'слово_на_синдарине',
    Формат вывода: имя1, имя2, перевод1, перевод2
    """
    # Случайные ключи из словаря:
    rnd_words = [random.choice(list(dict_words.keys())) for x in range(name_length)]
    wordlist = list(map(lambda word: dict_words.get(word,word), rnd_words))
    # Первый символ имени делаем строчным:
    wordlist = [x.capitalize() for x in wordlist]
    #name = tuple(wordlist + rnd_words)
    return tuple(wordlist), tuple(rnd_words)

def gen_name_real():
    """Создаёт реалистичное имя.

    Словари настраиваются в config.py
    Словари в формате: 'имя':'значение',
    Формат вывода: (имя, фамилия), (значение_имени, значение_фамилии)
    """
    name = random.choice(list(config.NAMES_DICT.items()))
    surname = random.choice(list(config.SURNAMES_DICT.items()))
    if not surname[1]:
        surname = (surname[0], 'Unknown')
    name_and_surname = (name[0], surname[0])
    name_and_surname = tuple((x.capitalize() for x in name_and_surname))
    name_and_surname_translate = tuple((name[1], surname[1]))
    return name_and_surname, name_and_surname_translate

def gen_ability_throws(hero = True):
    """Характеристики героя по правилам D&D 3.5-5.0
    
    Вывод -- список с результатами бросков. Без распределения на силу, ловкость и т.д.
    Распределение зависит от класса персонажа. Сначала бросаем, потом распределяем.
    - Под каждый параметр бросаем 4 кости на d6
    - Получается список чисел (например 1,4,6,3)
    - Меньшее число из списка отбрасываем (получается 4,6,3)
    - Суммируем показатели, получаем число в диапазоне 3-18
    - Повторяем шесть раз.
    На выборке из 10 000 героев среднее арифметической от суммы параметров -- 73.5
    Из 10 000 простолюдинов среднее арифметическое от суммы параметров -- 63
    """
    abilityes = []
    while len(abilityes) < 6:
        if hero:
            # Четыре раза бросаем кость d6, сохраняем все значения:
            throws_list = [dices.throw_d6() for x in range(4)]
            # Удаляем меньшее значение
            throws_list.remove(min(throws_list))
            ability = sum(throws_list)
        else:
            # Три раза бросаем кость d6, сохраняем все значения:
            throws_list = [dices.throw_d6() for x in range(3)]
            ability = sum(throws_list)
        abilityes.append(ability)
    return abilityes

def calculate_equipment_weight(equipment_dict, metadict_items):
    """Рассчитываем вес предметов в инвентаре."""
    weight = 0
    for key, value in equipment_dict.items():
        try:
            weight += metadict_items[key]['weight (lb)'] * value
        except Exception as error_output:
            print('Исключение calculate_equipment_weight (вес предмета не указан)', key, error_output)
    return weight

def calculate_equipment_cost(equipment_dict, metadict_items,
        gold_coin_value = 1, silver_coin_value = 60, copper_coin_value = 3600):
    """Рассчитываем стоимость предметов в инвентаре.
    
    В D&D приняты золотые, серебряные и медные монеты. Все массой по 9 грамм.
    Их соотношение 1:10:100, хотя вернее было бы 1:15:750 (для Византии 6 века н.э.)
    «Weights, measures and antique currencies adapted to roleplaying games»
    http://www.guildcompanion.com/scrolls/2008/nov/assemblage.html

    Эфес (55 грамм золота) -- 60 gp в DnD.
    - Это год службы профессионального солдата.
    - Это стоимость чешуйчатых доспехов, комплекта вооружения, или обученного верхового коня.
    - Это 1/30 аттического таланта серебра, или 60 шекелей, 200 драхм, 1200 обелисков, 3600 фоллисов.
    - Это год скромной жизни (рыба, каша, оливковое масло) -- 1-2 фоллиса/день для семьи в 6 человек.
    
    1 золотой эфес = 60 грамм золота = 60 золотых монет из D&D
    1 золотой эфес = 60 серебряных шекелей = 3600 бронзовых Folles
    """
    cost_sum_gp = 0
    cost_sum_sp = 0
    cost_sum_cp = 0
    # TODO: допилить или переделать начисто
    # ------------------------------------------------------------
    # Да, это работает, но, боги, как же криво и косо смотрится.
    # Наверное, лучше перенести в методы и считать отдельно gp и эфесы
    # ------------------------------------------------------------
    # Цены указаны в разных монетах, поэтому перебираем все:
    for key, value in equipment_dict.items():
        try:
            cost_sum_gp += metadict_items[key]['cost (ephesi)'] * value
            #cost_sum_gp += metadict_items[key]['cost (gp)'] * value
        except:
            try:
                cost_sum_sp += metadict_items[key]['cost (grams_of_gold)'] * value
                #cost_sum_sp += metadict_items[key]['cost (sp)'] * value
            except:
                try:
                    cost_sum_cp += metadict_items[key]['cost (follis)'] * value
                    #cost_sum_cp += metadict_items[key]['cost (cp)'] * value
                except:
                    pass
    cost_sum = cost_sum_gp + cost_sum_sp / silver_coin_value + cost_sum_cp / copper_coin_value
    dict_equipment_cost = {
            'equipment_cost_sum (ephesi)':round(cost_sum, 2),
            'equipment_cost (ephesi)':cost_sum_gp,
            'equipment_cost (grams_of_gold)':cost_sum_sp,
            'equipment_cost (follis)':cost_sum_cp,
            }
    #return dict_equipment_cost
    return cost_sum

#-------------------------------------------------------------------------
# Классы:

class soldier():
    """Шаблонные солдаты с характеристиками в формате D&D 5.0.

    Что они имеют:
    - Снаряжение и способности из шаблона. Собственное имя, рост и вес.
    - Силу, телосложение и прочие характеристики. Модификатор и спасброски.
    - Класс защиты (солдат сам выбирает броню из инвентаря по своим способностям)
    - Словарь атак (солдат сам смотрит оружие и определяет модификаторы)
    - Оценка веса снаряжения и его стоимости. Ожидаемая плата.

    # Создаём солдата:
    newbie = soldier()
    newbie.create_soldier('Warrior 1 lvl (legionary infantry)')
    # Повышаем уровень:
    newbie.levelup('Warrior 5 lvl (legionary infantry-captain)')
    # Смотрим, что получилось:
    for key,value in newbie.__dict__.items():
        print(key,value)
    """
    # Словарь с расовыми чертами:
    race_base = 'Human-common'
    race_base_pet = 'Horse'
    dict_races = races.dict_races
    # Словарь шаблонов под персонажи и словарь вещей:
    metadict_chars = chars.metadict_chars
    metadict_items = chars.metadict_items
    metadict_animals = animals.metadict_animals
    metadict_chars.update(metadict_animals)
    # Словари главных параметров и спасбросков (например, у бойца это сила и телосложение):
    ability_names = ['strength','dexterity','constitution','intelligence','wisdom','charisma']
    dict_class_abilityes = classes.dict_class_abilityes
    dict_class_saves = classes.dict_class_saves
    # Словари особенностей класса. Бонус мастерства, Ки монаха, Скрытая атака вора:
    # Всё распределено в огромные таблицы, где каждому уровню соответствуют свои бонусы.
    metadict_class_proficiency = classes.metadict_class_proficiency
    metadict_class_spells = classes.metadict_class_spells
    # Ограниченеи ловкости в средних доспехов и базовый класс доспехов.
    allow_dexterity_mod = 2
    armor_class_base = 10
    dict_attack_unarmed = {
        'weapon':False,
        'weapon_type':['simple','finesse'],
        'damage_type':'bludgeoning',
        'damage_dice':'1d1',
        }
    # TODO: отделить монетную систему
    # ------------------------------------------------------------
    # Монетную систему перенеси в основной конфиг. Когда он будет готов.
    # ------------------------------------------------------------
    # Для расчётов стоимости:
    # Важная часть платы наёмника -- его снаряжение (1/4 полной стоимости/год)
    property_pay_share = 1/4
    # Относительные цены монет: 1:60:3600 (ценных металлов: 1:15:750)
    # 1 золотой эфес (55 грамм) = 60 золотых монет из D&D (по 9 грамм)
    # 1 золотой эфес (55 грамм) = 60 серебряных силикв (по 15 грамм)
    gold_coin_value = 1
    silver_coin_value = 60
    copper_coin_value = 3600
    # Меры длины и веса для перевода в привычные метры/килограммы:
    inch_to_meters = 0.0254
    feet_to_meters = inch_to_meters * 12
    pound_to_kilograms = 0.45

    def __init__(self):
        # TODO: убрать
        # ------------------------------------------------------------
        # Теперь не используется, можно убрать.
        # ------------------------------------------------------------
        pass

    def create_soldier(self, rank, sex = 'Male', hero = None):
        """Создаём бойца выбранного ранга.

        Шаблон берём из chars. Все индивидуальные параметры случайны.
        """
        self.rank = rank
        if config.__dict__.get('LANGUAGE_DICT_FANTASY'):
            self.name, self.name_translate = gen_name(config.LANGUAGE_DICT_FANTASY)
        else:
            self.name, self.name_translate = gen_name_real()
        # ЗАМЕТКА:
        # ------------------------------------------------------------
        # Помни, анон, только UUID v4 -- случайные числа,
        # Версии 1-2 генерируются из MAC-адреса.
        # ------------------------------------------------------------
        self.uuid = uuid.uuid4()
        self.sex = sex
        # Берём шаблон солдата:
        self.__dict__.update(copy.deepcopy(self.metadict_chars[rank]))
        # Проверяем, есть ли особенные черты:
        if not hasattr(self, 'class_features'):
            self.class_features = {}
        # Проверяем, есть ли в словаре раса шаблона:
        if not self.dict_races.get(self.race):
            print('ERROR: "{0}" not found in races.dict_races {1} use {2}'.format(
                self.race, self.dict_races.keys(), race_base))
            self.race = self.race_base
        # Проверяем, указано ли, что это герой:
        if hero == True or hero == False:
            self.hero = hero
        elif self.dict_races[self.race].get('hero'):
            self.hero = self.dict_races[self.race]['hero']
        else:
            self.hero = False
        # Характеристики можно указать в шаблоне, тогда у всех будут одинаковы:
        if not hasattr(self, 'abilityes'):
            self.abilityes = self.get_class_abilityes(gen_ability_throws(self.hero))
            self.abilityes = self.add_race_abilityes()
        self.body = self.gen_height_and_weight()
        self.size = self.body['size']
        self.proficiency = self.find_class_proficiency()
        self.proficiency_bonus = self.proficiency['proficiency_bonus']
        self.overload = self.calculate_overload()
        self.base_speed = self.overload['base_speed']
        self.mods = self.calculate_mods()
        self.saves = self.calculate_saves()
        self.hitpoints_max = self.calculate_hitpoints()
        self.hitpoints_max_backup = self.hitpoints_max
        self.hitpoints = self.hitpoints_max
        self.armor = self.takeoff_armor()
        self.armor.update(self.get_armor())
        self.attacks = self.takeoff_weapon()
        self.attacks.update(self.get_weapon())
        self.attacks.update(self.modify_attacks())
        self.attacks.update(self.modify_attacks_weapon_of_choice())
        self.spells_generator = spells.gen_spells(self)
        self.spellslots = self.spells_generator.spellslots
        self.spells = self.spells_generator.spells
        self.unit_cost = self.calculate_unit_cost()

    def create_pet(self, animal_type, sex = 'Male', hero = False):
        """Создаём питомца (верховое животное или чудовище).

        Шаблон берём из animals. Все индивидуальные параметры случайны.
        """
        # TODO: допилить, чтобы наравне с бойцами использовать.
        # А ещё лучше объединить.
        self.rank = animal_type
        if config.__dict__.get('LANGUAGE_DICT_FANTASY'):
            self.name, self.name_translate = gen_name(config.LANGUAGE_DICT_FANTASY, name_length = 1)
        else:
            self.name, self.name_translate = gen_name(config.LANGUAGE_DICT_REAL, name_length = 1)
        self.uuid = uuid.uuid4()
        self.sex = sex
        # Берём шаблон:
        self.__dict__.update(copy.deepcopy(self.metadict_animals[animal_type]))
        # Проверяем, есть ли особенные черты:
        if not hasattr(self, 'class_features'):
            self.class_features = {}
        ## Проверяем, есть ли в словаре раса шаблона:
        if not self.dict_races.get(self.race):
            print('ERROR: "{0}" not found in races.dict_races {1} use {2}'.format(
                self.race, self.dict_races.keys(), self.race_base_pet))
            self.race = self.race_base_pet
        # Проверяем, указано ли, что это герой (ага, лошади тоже могут):
        if hero == True or hero == False:
            self.hero = hero
        elif self.dict_races[self.race].get('hero'):
            self.hero = self.dict_races[self.race]['hero']
        else:
            self.hero = False
        # Характеристики можно указать в шаблоне, тогда у всех будут одинаковы:
        if not hasattr(self, 'abilityes'):
            self.abilityes = self.get_class_abilityes(gen_ability_throws(self.hero))
            self.abilityes = self.add_race_abilityes()
        self.body = self.gen_height_and_weight()
        self.size = self.body['size']
        self.proficiency = self.find_class_proficiency()
        self.proficiency_bonus = self.proficiency['proficiency_bonus']
        self.overload = self.calculate_overload()
        self.base_speed = self.overload['base_speed']
        self.mods = self.calculate_mods()
        self.saves = self.calculate_saves()
        if not hasattr(self, 'hitpoints_max'):
            self.hitpoints_max = self.calculate_hitpoints()
            self.hitpoints = self.hitpoints_max
        self.armor = self.takeoff_armor()
        self.armor.update(self.get_armor())
        if not hasattr(self, 'attacks'):
            self.attacks = self.takeoff_weapon()
            self.attacks.update(self.get_weapon())
            self.attacks.update(self.modify_attacks())
            self.attacks.update(self.modify_attacks_weapon_of_choice())
        self.spells_generator = spells.gen_spells(self)
        self.spellslots = self.spells_generator.spellslots
        self.spells = self.spells_generator.spells
        self.unit_cost = self.calculate_unit_cost()

    def levelup(self, rank, regen_spells = True):
        """Меняет ранг солдата на новый. Многое пересчитывается.
        
        Например: Warrior 1 lvl (legionary infantry) >>> Warrior 2 lvl (legionary infantry-corporal)
        - Имя, рост и вес, сила и ловкость -- базовые параметры остаются прежними.
        - Способности бойца меняются на новые. Снаряжение обновляется.
        - Хитпоинты пересчитываются заново (надо исправить).
        - Боец берёт новую броню и выбирает новые атаки.
        """
        # TODO: если поднять обычного бойца до героя, он не получит бонусов характеристик.
        # ------------------------------------------------------------
        # Давай им +2 ко всем характеристикам (61 > 73), и расовый бонус +1.
        # ------------------------------------------------------------
        self.rank = rank
        check_hero = self.hero
        # Смотрим, изменился ли класс:
        # ------------------------------------------------------------
        # Если класс персонажа изменился, перетасовываем характеристики под новый класс.
        # Так можно делать солдат офицерами, поднимая харизму за счёт телосложения. Стареют ведь.
        # ------------------------------------------------------------
        old_char_class = self.char_class
        new_char_class = self.metadict_chars[self.rank]['char_class']
        if not old_char_class == new_char_class:
            self.char_class = new_char_class
            ability_list = self.abilityes.values()
            self.abilityes = self.get_class_abilityes(ability_list)
            #print(ability_list, old_char_class, '>>>', self.char_class)
        # Обновляем шаблон:
        # TODO: маленькая проблема. Старые параметры в шаблоне сохраняются.
        # Если у нас в старом шаблоне mount_combat True, то это перейдёт и в новый шаблон.
        # Нельзя просто закомментировать #mount_combat у паладина 5 lvl. Нужно ставить False.
        self.__dict__.update(copy.deepcopy(self.metadict_chars[rank]))
        if not hasattr(self, 'class_features'):
            self.class_features = {}
        # Обычный боец может стать героем, и получить +2 к характеристикам:
        if self.dict_races[self.race].get('hero'):
            self.hero = self.dict_races[self.race]['hero']
            if not check_hero and self.hero:
                self.abilityes = self.add_race_abilityes()
                self.abilityes = self.add_hero_abilityes()
        self.body = self.gen_height_and_weight()
        self.size = self.body['size']
        self.set_improvement_abilityes()
        self.proficiency = self.find_class_proficiency()
        self.proficiency_bonus = self.proficiency['proficiency_bonus']
        self.overload = self.calculate_overload()
        self.base_speed = self.overload['base_speed']
        self.mods = self.calculate_mods()
        self.saves = self.calculate_saves()
        self.hitpoints_max = self.calculate_hitpoints()
        self.hitpoints = self.hitpoints_max
        self.armor = self.takeoff_armor()
        self.armor.update(self.get_armor())
        self.attacks = self.takeoff_weapon()
        self.attacks.update(self.get_weapon())
        self.attacks.update(self.modify_attacks())
        self.attacks.update(self.modify_attacks_weapon_of_choice())
        # TODO: пилим заклинания.
        # Класс должен создавать словарь spells и обрабатывать его.
        if regen_spells:
            self.spells_generator = spells.gen_spells(self)
            self.spellslots = self.spells_generator.spellslots
            self.spells = self.spells_generator.spells
            self.unit_cost = self.calculate_unit_cost()

    def gen_height_and_weight(self):
        """По правилам D&D 5 рост и вес персонажа зависят только от расы.

        Правила из "Книги игрока", глава 4 "Личность и предыстория":
        Рост человека, это базовые 4 фута 8 дюймов + 2d10 дюймов (мод_роста).
        Вес зависит от модификатора роста: 110 фунтов + мод_роста * 2d4 фунта.
        Диапазон роста для человека (футы и дюймы): 4'8'' - 7'2''
        Диапазон веса для человека (фунты): 114 - 274
        """
        race_traits = self.dict_races[self.race]
        height_base_inches = race_traits['height_base_inches']
        weight_base_lb = race_traits['weight_base_lb']
        random_for_height = dices.dice_throw(race_traits['height_mod_dice'])
        random_for_weight = dices.dice_throw(race_traits['weight_mod_dice'])
        # Рост в дюймах, вес в фунтах:
        height_inches = height_base_inches + random_for_height
        weight_lb = weight_base_lb + (random_for_height * random_for_weight)
        height_meters = round(height_inches * self.inch_to_meters, 2)
        weight_kilograms = round(weight_lb * self.pound_to_kilograms)
        dict_body = {
                'height_inches':height_inches,
                'weight_lb':weight_lb,
                'height_meters':height_meters,
                'weight_kilograms':weight_kilograms,
                'size':race_traits['size'],
                }
        return dict_body

    def get_class_abilityes(self, ability_throws):
        """Распределят параметры персонажа в зависимости от класса.
        
        Не названные параметры из списка получают названия:
        Например, у бойца максимальный параметр, это сила. Второй телосложение, и т.д.
        """
        # Список с числами параметров разворачиваем, чтобы наибольшие были в начале:
        ability_list = reversed(sorted(ability_throws))
        try:
            # Названия главных параметров в список:
            char_abilityes = self.dict_class_abilityes[self.char_class]
            if hasattr(self, 'abilityes_choice') and type(self.abilityes_choice) == list:
                char_abilityes = self.abilityes_choice
        except Exception as error_output:
            # Если класса не существует, то все параметры рандомно:
            print('Исключение get_class_abilityes (класс героя не указан)',error_output)
            char_abilityes = []
        # Названия второстепенных параметров в отдельный список:
        second_abilityes = [a for a in self.ability_names if a not in char_abilityes]
        dict_abilityes = {}
        for n, ability in enumerate(ability_list):
            if n < len(char_abilityes):
                ability_name = char_abilityes[n]
                dict_abilityes[ability_name] = ability
            else:
                # Второстепенные параметры распределяем рандомно,
                # с каждым проходом обрезая список названий:
                ability_name = second_abilityes.pop(random.randrange(len(second_abilityes)))
                dict_abilityes[ability_name] = ability
        return dict_abilityes

    def add_hero_abilityes(self):
        """К характеристикам добавляются геройские бонусы
        
        Средние характеристики героя -- 73
        Средние характеристики простолюдина -- 61
        Всего: 73 - 61 = 12 (+2 к каждой характеристике)
        """
        free_ability_points = 0
        dict_abilityes = self.abilityes
        # Не повышаем характеристики выше 18:
        for key in dict_abilityes:
            if dict_abilityes[key] < 16:
                dict_abilityes[key] += 2
            else:
                free_ability_points += 2
            # Распределяем свободные пункты характеристик:
            if dict_abilityes[key] < 18 and free_ability_points > 0:
                points_to_ability = 18 - dict_abilityes[key]
                if free_ability_points > points_to_ability:
                    free_ability_points -= points_to_ability
                    dict_abilityes[key] += points_to_ability
                else:
                    dict_abilityes[key] += free_ability_points
                    free_ability_points = 0
        return dict_abilityes

    def add_race_abilityes(self):
        """К характеристикам добавляются расовые бонусы
        
        У героев-людей это +1 для всего.
        """
        race = self.race
        race_traits = self.dict_races[self.race]
        dict_abilityes = self.abilityes
        # Добавляем к характеристикам расовые бонусы (если они есть)
        for key, value in dict_abilityes.items():
            if race_traits.get(key):
                dict_abilityes[key] += race_traits[key]
        self.abilityes = dict_abilityes
        return dict_abilityes

    def set_improvement_abilityes(self):
        """Характеристики можно повысить с уровнем."""
        # TODO: добавь проверку, иначе характеристики будут повышаться с каждым levelup.
        if self.class_features.get('Ability_Score_Improvement'):
            improvement_dict = self.class_features.get('Ability_Score_Improvement')
            for key, value in improvement_dict.items():
                self.abilityes[key] += value

    def find_class_proficiency(self):
        """Бонус мастерства зависит от уровня. Выбор по таблице.
        
        У всех классов бонус мастерства одинаковый.
        Кроме этого мы добавляем прочие показатели, зависящие от уровня в классе:
        sneak_attack_dice вора, ki_points_max монаха, sorcery_points чародея и т.д.
        https://www.dandwiki.com/wiki/5e_SRD:Proficiency_Bonus
        """
        level = self.level
        char_class = self.char_class
        dict_proficiency = copy.deepcopy(self.metadict_class_proficiency[('Any',level)])
        dict_proficiency.update(self.metadict_class_proficiency[(char_class,level)])
        dict_proficiency['spellslots'] = copy.deepcopy(self.metadict_class_spells[('Any',level)])
        if self.metadict_class_spells.get((char_class,level)):
            dict_proficiency['spellslots'].update(self.metadict_class_spells[(char_class,level)])
        # Feat_Magic_Initiate: добавляет заклинание 1 круга и слот для него:
        if self.class_features.get('Feat_Magic_Initiate'):
            if dict_proficiency['spellslots'].get('1_lvl'):
                dict_proficiency['spellslots']['1_lvl'] += 1
            else:
                dict_proficiency['spellslots']['1_lvl'] = 1
        # Feat_Martial_Adept: даёт два приёма мастера боевых искусств, и одну кость превосходства 1d6.
        if self.class_features.get('Feat_Martial_Adept'):
            if not dict_proficiency.get('superiority_dice'):
                dict_proficiency['superiority_dice'] = '1d6'
            if dict_proficiency.get('superiority_dices'):
                dict_proficiency['superiority_dices'] += 1
            else:
                dict_proficiency['superiority_dices'] = 1
        return dict_proficiency

    def calculate_mods(self):
        """Модификаторы характеристик.
        
        По правилам DnD модификаторы округляются вниз:
        Ловкость 15, это +2 модификатор ловкости, а не 2.5 или 3.
        """
        ability_dict = self.abilityes
        dict_mods = {}
        for ability, value in ability_dict.items():
            # По правилам D&D модификаторы округляются вниз:
            ability_mod_value = math.floor((value - 10) / 2)
            dict_mods[ability] = ability_mod_value
        return dict_mods

    def calculate_saves(self):
        """Спасброски характеристик. К последним прибавляется бонус мастерства.
        
        По правилам D&D спасброски округляются вниз:
        То есть Ловкость 15, это +2 спасброска ловкости, а не 2.5 или 3.
        """
        dict_saves = {}
        dict_class_saves = self.dict_class_saves
        proficiency_bonus = self.proficiency_bonus
        for ability, value in self.abilityes.items():
            # Бонус спасброска округляем вниз:
            ability_save_value = math.floor((value - 10) / 2)
            # Добавляем бонус мастерства к спасброскам, если доступен:
            if ability in dict_class_saves[self.char_class]:
                ability_save_value += proficiency_bonus
            # Добавляем бонус мастерства за черту:
            if self.class_features.get('Feat_Resilient')\
                    and ability == self.class_features['Feat_Resilient']:
                ability_save_value += proficiency_bonus
            dict_saves[ability] = ability_save_value
        return dict_saves

    def find_base_speed(self):
        """Берём базовую скорость. Отдельной функцией. Монахи, варвары, все дела."""
        base_speed = self.dict_races[self.race]['base_speed']
        # Добавляем бонус скорости монахов:
        if hasattr(self, 'proficiency') and self.proficiency.get('unarmored_movement'):
            base_speed += self.proficiency['unarmored_movement']
        return base_speed

    def calculate_overload(self):
        """Рассчитываем переносимый вес и скорость юнита.
     
        Вариант правил из "книги игрока" DnD 5:
        вес < сила x5 -- лёгкий вес (при 10 силы, это 50 футов, до 25 кг)
        вес < сила x10 -- нагрузка (-10 футов к скорости)
        вес < сила x15 -- перегрузка  (-10 футов к скорости, помеха к атаке и спасброскам)
        По стандартным правилам D&D 5 переносимый вес (в фунтах), это сила x15. Штрафов нет.
        """
        # Рассчитываем массу снаряжения, нагрузку:
        base_speed = self.find_base_speed()
        metadict_items = self.metadict_items
        equipment_weight = calculate_equipment_weight(self.equipment_weapon, metadict_items)
        backpack_weight = calculate_equipment_weight(self.equipment_backpack, metadict_items)
        supply_weight = calculate_equipment_weight(self.equipment_supply, metadict_items)
        mounted_weigh = 0
        # Если солдат может позволить себе лошадь, то снаряжение во вьюках.
        if hasattr(self, 'equipment_mount'):
            mounted_weigh = calculate_equipment_weight(self.equipment_mount, metadict_items)
            mounted_weigh += backpack_weight
            backpack_weight = 0
        light_load = self.abilityes['strength'] * 2.5
        normal_load = self.abilityes['strength'] * 5
        maximum_load = self.abilityes['strength'] * 10
        # Великаны переносят вчетверо больше средних существ:
        if self.size == 'huge':
            light_load *= 4
            normal_load *= 4
            maximum_load *= 4
        # Для крупных существ переносимый вес удваивается:
        elif self.size == 'large':
            light_load *= 2
            normal_load *= 2
            maximum_load *= 2
        # Для маленьких существ переносимый вес вдвое меньше:
        elif self.size == 'tiny':
            light_load = round(light_load / 2)
            normal_load = round(normal_load / 2)
            maximum_load = round(maximum_load / 2)
        # В бою боец носит только оружие и доспехи:
        battle_overload = False
        battle_lightload = False
        # Если нагрузка чрезмерна, убавляем скорости:
        if equipment_weight > normal_load:
            battle_overload = True
            base_speed += -10
        # Homebrew: Если нагрузка очень лёгкая, то добавляем скорости:
        # - Нормальный строевой шаг, 120 шагов/минуту при длине шага 0.75 метров (30 футов)
        # - Ускоренный строевой шаг, 135 шагов/минуту при длине шага 0.8 метров (35 футов)
        elif equipment_weight <= light_load:
            battle_lightload = True
            base_speed += 5
        # В походе пеший боец тащит ещё и рюкзак (спальник, вода, сухари, инструменты):
        travel_overload = False
        if equipment_weight + backpack_weight > maximum_load:
            travel_overload = True
        dict_overload = {
                'equipment_weight (lb)':equipment_weight,
                'backpack_weight (lb)':backpack_weight,
                'property_weight (lb)':backpack_weight + equipment_weight + mounted_weigh,
                'supply_weight (lb)':supply_weight,
                'normal_load (lb)':normal_load,
                'light_load (lb)':light_load,
                'maximum_load (lb)':maximum_load,
                'battle_lightload':battle_lightload,
                'battle_overload':battle_overload,
                'travel_overload':travel_overload,
                'base_speed':base_speed,
                }
        return dict_overload

    def calculate_unit_cost (self):
        """По снаряжению бойца и его уровню определяем стоимость "юнита".
        
        Минимальная плата равна 1/4 стоимости снаряжения и годовой стоимости пищи.
        Плата пешего наёмника -- 1 эфес/год. С каждым уровнем плата повышается вдвое.
        Это геометрическая прогрессия, например для центуриона 5 lvl: 1*2**(5-1) = 16 эфесов.
    
        Для сравнения, Римская республика/империя на рубеже нашей эры (времена Цезаря):
        Плата легионера -- 112.5-225 денариев в год (500-1000 грамм серебра, 0.5-1 эфеса)
        Плата центуриона -- 3750-15000 денариев в год (16.6-66.7 кг серебра, 20-80 эфесов)
        https://en.wikipedia.org/wiki/Denarius#Comparisons_and_silver_content
        
        Солдатам в Римской империи (300 года н.э.) платили 15 400 медных денариев/год (повторюсь, медных!)
        При этом 20% платы выдавали в виде пшеницы, 30 модиев/год (0.54 кг/день, 1350 килокаллорий).
        Платы легионера хватало, чтобы прокормить его самого и ещё двух-трёх членов семьи.
        http://ancientcoinsforeducation.org/content/view/79/98/

        Стоимость заклинаний:
        Жрецов | lvl    | круг | закл/год  | эфс/год | стоимость/закл  | возможности   
        ------ |------- | ---- | --------- | ------- | --------------- | -----------
        5000   | 1-2+   | 1    | 3 600 000 | 7.5     | 1 эфс/100 закл  | Cure Wounds
        1250   | 3-4+   | 2    | 900 000   | 30      | 4 эфс/100 закл  | Lesser Restoration
        312    | 5-6+   | 3    | 224 600   | 120     | 17 эфс/100 закл | Реанимация
        78     | 7-8+   | 4    | 28 000    | 480     | 1.3 эфеса/закл  | Предсказание
        20     | 9-10+  | 5    | 7 200     | 1920    | 5.3 эфесов      | Raise Dead
        4      | 11-12+ | 6    | 1 440     | 7680    | 21  эфесов      | Пир героев
        1      | 13-14+ | 7    | 360       | 30 720  | 84  эфесов      | Resurrection
        Доступность заклинаний -- 11.5 млн. жреческих заклинаний/год (на 50 млн. населения)
        Денежный оборот храмов -- 260 тыс. эфесов/год (только жрецы)
        """
        metadict_items = self.metadict_items
        property_pay_share = self.property_pay_share
        gp, sp, cp = self.gold_coin_value, self.silver_coin_value, self.copper_coin_value
        equipment_cost = calculate_equipment_cost(self.equipment_weapon, metadict_items, gp, sp, cp)
        backpack_cost = calculate_equipment_cost(self.equipment_backpack, metadict_items, gp, sp, cp)
        supply_cost = calculate_equipment_cost(self.equipment_supply, metadict_items, gp, sp, cp)
        if hasattr(self, 'equipment_mount'):
            mount_cost = calculate_equipment_cost(self.equipment_mount, metadict_items, gp, sp, cp)
        else:
            mount_cost = 0
        property_cost = equipment_cost + backpack_cost + mount_cost
        # Учитываем стоимость заклинаний:
        # Заклинание 1_lvl -- 1 gp, 2_lvl -- 4 gp, и т.д.
        spells_cost = 0
        if hasattr(self, 'spells'):
            for spellslot, spell_per_day in self.spellslots.items():
                if int(spellslot[0]) == 1:
                    spells_cost += 1
                elif int(spellslot[0]) > 1:
                    spells_cost += 1 * (4 ** int(spellslot[0]))
        # Годовая плата -- геометрическая прогрессия к уровню бойца:
        unit_pay_year = ((property_cost * property_pay_share) + supply_cost) * 2 ** (self.level - 1)\
                + spells_cost
        unit_cost_dict = {
                'equipment_cost':round(equipment_cost, 2),
                'property_cost':round(property_cost, 2),
                'supply_cost':round(supply_cost, 2),
                'spells_cost':round(spells_cost, 2),
                'unit_pay_year':round(unit_pay_year, 2),
                }
        return unit_cost_dict

    def calculate_hitpoints(self):
        """Рассчитывает количество хитпоинтов персонажа.
        
        Два варианта расчёта:
        - средний по кости хитов, как в Monsters_Manual.
        - и броски кости хитов, как для героев.
        """
        level = self.level
        hit_dice = self.hit_dice
        constitution_mod = self.mods['constitution']
        bonus_hitpoints_constitution = constitution_mod * level
        # Выбор среднего. У героев максимум хитов на 1 lvl, у монстров всё усредняется:
        if hasattr(self, 'hitpoints_medial') and self.hitpoints_medial:
            if self.hero:
                level_1_hitpoints = int(hit_dice.split('d')[1])
            else:
                level_1_hitpoints = (int(hit_dice.split('d')[1]) / 2 + 0.5)
            hitpoints_levels = sum([(int(hit_dice.split('d')[1]) / 2 + 0.5) for x in range(level - 1)])
            hitpoints_max = level_1_hitpoints + hitpoints_levels + bonus_hitpoints_constitution
        # Заданные хитпоинты, плюс бонус телосложения.
        elif hasattr(self, 'hitpoints_base') and self.hitpoints_base:
            hitpoints_levels = self.hitpoints_base
            hitpoints_max = hitpoints_levels + bonus_hitpoints_constitution
        else:
            # Броски костей хитов. На первом уровне максимум у всех:
            level_1_hitpoints = int(hit_dice.split('d')[1])
            bonus_hitpoints_levels = 0
            if level > 1:
                bonus_hitpoints_levels = sum([dices.dice_throw(hit_dice) for x in range(level - 1)])
            hitpoints_max = level_1_hitpoints + bonus_hitpoints_levels + bonus_hitpoints_constitution
        # "Крепкий" Feat_Tough получает +2 hp/уровень:
        if self.class_features.get('Feat_Tough'):
            hitpoints_max += level * 2
        # У симулякра только половина хитпоинтов оригинала:
        if hasattr(self, 'simulacrum') and self.simulacrum:
            hitpoints_max = hitpoints_max / 2
        return int(hitpoints_max)

    def takeoff_armor(self):
        """Солдат без брони и без щита.
        
        Возвращает диапазон Armor Class в таком порядке:
        1) Есть удар по броне.
        2) Есть удар по щиту.
        3) Уклонение. Пока что только уклонение.
        """
        dexterity_mod = self.mods['dexterity']
        if self.__dict__.get('armor_class_natural'):
            armor_class_base = self.__dict__.get('armor_class_natural')
        elif self.dict_races[self.race].get('armor_class_natural'):
            armor_class_base = self.dict_races[self.race].get('armor_class_natural')
        else:
            armor_class_base = self.armor_class_base
        # Базовые параметры
        armor_use = None
        shield_use = None
        armor_class_shield = 0
        Unarmored_Defense = False
        armor_stealth_disadvantage = False
        armor_class_dodge = armor_class_base + dexterity_mod
        # Монахи и варвары неплохо защищены и без брони:
        if self.class_features.get('Unarmored_Defense'):
            if self.char_class == 'Monk':
                armor_class_dodge += self.mods['wisdom']
                Unarmored_Defense = True
            elif self.char_class == 'Barbarian':
                armor_class_dodge += self.mods['constitution']
                Unarmored_Defense = True
            else:
                armor_class_dodge += self.mods['wisdom']
                Unarmored_Defense = True
        if not armor_use and Unarmored_Defense == True:
            armor_use = 'Unarmored_Defense'
        armor_class_armor = armor_class_dodge
        dict_armor_class = {
                'armor_class':armor_class_armor + armor_class_shield,
                'armor_class_armor_impact':armor_class_armor + armor_class_shield,
                'armor_class_shield_impact':armor_class_dodge + armor_class_shield,
                'armor_class_no_impact':armor_class_dodge,
                'armor_stealth_disadvantage':armor_stealth_disadvantage,
                'armor_class_shield':armor_class_shield,
                'armor_class_armor':armor_class_armor,
                'armor_use':armor_use,
                'shield_use':shield_use,
                }
        return dict_armor_class

    def select_armor(self, item):
        """Примеряем броню, учитывая бонусы ловкости и бонусы класса.
        
        Вывод -- словарь брони, изменённый с учётом способностей бойца.
        """
        dexterity_mod = self.mods['dexterity']
        armor_choice = {}
        armor_choice.update(self.metadict_items[item])
        item_armor_ac = armor_choice['armor_class_armor']
        allow_dexterity_mod = self.allow_dexterity_mod
        # TODO: классовые бонусы в отдельный метод
        # ------------------------------------------------------------
        # Нужно как-то перенести классовые бонусы в отдельную функцию.
        # Или забить на точность проверки брони, а просто добавить бонусы позже.
        # ------------------------------------------------------------
        if self.class_features.get('Medium_Armor_Master'):
            # Мастер средних доспехов может использовать мод ловкости +3:
            # А также не получает штрафов в проверках скрытности.
            armor_choice['armor_stealth_disadvantage'] = False
            allow_dexterity_mod += 1
        if self.class_features.get('Fighting_Style_Defence'):
            # Боевой стиль: оборона -- даёт +1 AC в броне:
            item_armor_ac += 1
        # Определяем тип брони и учитываем бонус ловкости:
        if armor_choice.get('armor_type') == 'medium':
            if dexterity_mod <= allow_dexterity_mod:
                armor_dexterity_mod = dexterity_mod
            else:
                armor_dexterity_mod = allow_dexterity_mod
        # Тяжёлая броня нивелирует как плюсы высокой, так и минусы низкой ловкости.
        elif armor_choice.get('armor_type') == 'heavy' or armor_choice.get('armor_type') == 'Barkskin':
            armor_dexterity_mod = 0
        else:
            armor_dexterity_mod = dexterity_mod
        # Наконец, суммируем и переносим в словарь:
        armor_choice['armor_class_armor'] = item_armor_ac + armor_dexterity_mod
        armor_choice['armor_dexterity_mod'] = armor_dexterity_mod
        return armor_choice

    def get_armor(self):
        """Выбираем броню. Солдат берёт лучшую, с учётом своих способностей.
        
        Использует select_armor(item) чтобы оценить параметры доспехов.
        Возвращает диапазон Armor Class в таком порядке:
        1) Есть удар по броне.
        2) Есть удар по щиту.
        3) Уклонение.
        """
        # Перебираем броню и выбираем, если она даёт защиту не хуже уклонения:
        metadict_items = self.metadict_items
        armor_class_base = self.armor_class_base
        armor_class_armor = self.armor['armor_class_armor']
        armor_class_shield = self.armor['armor_class_shield']
        armor_stealth_disadvantage = self.armor['armor_stealth_disadvantage']
        armor_class_dodge = self.armor['armor_class_no_impact']
        armor_use = self.armor['armor_use']
        shield_use = self.armor['shield_use']
        for item in self.equipment_weapon:
            if metadict_items[item].get('armor') == True:
                if metadict_items[item]['armor_type'] in self.armor_skill\
                        or metadict_items[item]['armor_type'] == 'Barkskin'\
                        or metadict_items[item]['armor_type'] == 'Mage_Armor':
                    # Боец примеряет броню и оценивает её по своим способностям:
                    armor_choice = self.select_armor(item)
                    item_armor_ac = armor_choice['armor_class_armor']
                    if item_armor_ac > armor_class_armor:
                        # Продолжаем перебирать броню,
                        # Но теперь сравниваем с выбранной:
                        armor_class_armor = item_armor_ac
                        dexterity_mod = armor_choice['armor_dexterity_mod']
                        armor_class_dodge = armor_class_base + dexterity_mod
                        armor_stealth_disadvantage = armor_choice.get(
                                'armor_stealth_disadvantage', False)
                        armor_use = item
            elif metadict_items[item].get('shield') == True:
                if 'shield' in self.armor_skill:
                    item_shield_ac = metadict_items[item].get('armor_class_shield', 0)
                    if item_shield_ac > armor_class_shield:
                        armor_class_shield = item_shield_ac
                        shield_use = item
        # Наручи защиты, даются +2 AC тем, кто не носит доспехи и щиты:
        if 'Bracers of Defence' in self.equipment_weapon:
            if not armor_use and not shield_use\
                    or armor_use == 'Unarmored_Defense' and not shield_use:
                armor_class_armor += 2
        # Вывод диапазона параметров: удар по броне, по щиту, уклонение:
        dict_armor_class = {
                'armor_class':armor_class_armor + armor_class_shield,
                'armor_class_armor_impact':armor_class_armor + armor_class_shield,
                'armor_class_shield_impact':armor_class_dodge + armor_class_shield,
                'armor_class_no_impact':armor_class_dodge,
                'armor_stealth_disadvantage':armor_stealth_disadvantage,
                'armor_class_shield':armor_class_shield,
                'armor_class_armor':armor_class_armor,
                'armor_use':armor_use,
                'shield_use':shield_use,
                }
        return dict_armor_class

    def select_attack_mod(self, dict_attack):
        """Выбираем модификаторы атаки и урона.
        
        Выбираем, ловкость или силу использовать для атаки/урона.
        Определяем, умеет ли боец пользоваться оружием (владение оружием).
        """
        strenght_mod = self.mods['strength']
        dexterity_mod = self.mods['dexterity']
        weapon_type_list = dict_attack['weapon_type']
        try:
            # Проверяем владение оружием.
            # Сравниваем два списка, в выводе совпадающие элементы:
            weapon_skill_check = list(set(self.weapon_skill) & set(weapon_type_list))
            weapon_skills_use = weapon_skill_check
            if weapon_skill_check:
                proficiency_bonus = self.proficiency_bonus
            else:
                proficiency_bonus = 0
        except Exception as error_output:
            print('Исключение select_attack_mod (солдат не владеет оружием):', self.rank, error_output)
            weapon_skills_use = []
            proficiency_bonus = 0
        # Распределяем модификаторы в зависимости от типа оружия:
        if dict_attack['attack_range'] >= 10 and 'ranged' in weapon_type_list:
            attack_mod_type = 'dexterity'
            attack_mod = dexterity_mod + proficiency_bonus
            damage_mod = dexterity_mod
        elif 'finesse' in weapon_type_list\
                and dexterity_mod >= strenght_mod:
            attack_mod_type = 'dexterity'
            attack_mod = dexterity_mod + proficiency_bonus
            damage_mod = dexterity_mod
        else:
            attack_mod_type = 'strength'
            attack_mod = strenght_mod + proficiency_bonus
            damage_mod = strenght_mod
        attack_mod_dict = {
                'weapon_skills_use':weapon_skills_use,
                'attack_mod_type':attack_mod_type,
                'attack_mod':attack_mod,
                'damage_mod':damage_mod,
                }
        return attack_mod_dict

    def takeoff_weapon(self):
        """Убираем оружие, используем только рукопашную атаку.
        
        Эта функция создаёт рукопашную атаку. У монахов должна быть.
        Если у существа уже есть природная атака, то новая не создаётся.
        """
        metadict_attacks = {}
        if self.metadict_chars[self.rank].get('attacks'):
            metadict_attacks.update(copy.deepcopy(self.metadict_chars[self.rank]['attacks']))
        else:
            dict_attack = {}
            dict_attack.update(self.dict_attack_unarmed)
            dict_attack['attack_range'] = 5
            dict_attack['attack_type'] = 'close'
            dict_attack.update(self.select_attack_mod(dict_attack))
            metadict_attacks['close','unarmed'] = {}
            metadict_attacks['close','unarmed'].update(dict_attack)
        return metadict_attacks

    def get_weapon(self):
        """Рассчитываем параметры атак для каждого экипированного оружия.
        
        У каждого предмета может быть несколько типов атак (ближняя, бросок, град стрел)
        """
        metadict_attacks = {}
        metadict_items = self.metadict_items
        for item in self.equipment_weapon:
            if metadict_items[item].get('weapon') == True:
                # Распределяем атаки по задачам/дистанции:
                # Добавляем модификаторы атаки/урона (пока что базовые).
                if 'close' in metadict_items[item].get('weapon_type'):
                    # TODO: избавиться от повторяющихся участков кода
                    # ------------------------------------------------------------
                    # Например, сделай это отдельной фукнцией.
                    # Рабочий словарь dict_attack, он обнуляется с каждым сработавшим if.
                    # Нельзя просто взять и сделать dict_attack = metadict_items[item]
                    # Это ломает атаки, потому что обновляется metadict_items[item]
                    # Есть же метод dict.copy() Используй его!
                    # Или ещё проще: dict_copy = dict(dict_old)
                    # Только помни, что это shallow copy
                    # Исправлено на deepcopy
                    # ------------------------------------------------------------
                    dict_attack = copy.deepcopy(metadict_items[item])
                    dict_attack['weapon_use'] = item
                    dict_attack['attack_range'] = 5
                    dict_attack['attack_type'] = 'close'
                    # Базовая атака создаётся в любом случае:
                    dict_attack.update(self.select_attack_mod(dict_attack))
                    metadict_attacks['close',item] = {}
                    metadict_attacks['close',item].update(dict_attack)
                    # Ниже опциональные атаки с ядами/составами на клинке:
                    # TODO: вычитай 10 порций яда из экипировки, чтобы не дублировать.
                    ammo_type = dict_attack.get('ammo_type')
                    if isinstance(ammo_type, str):
                        ammo = ammo_type
                        if self.equipment_weapon.get(ammo):
                            dict_attack['ammo'] = self.equipment_weapon[ammo]
                            dict_attack.update(self.modify_attack_ammo(dict_attack, ammo))
                            dict_attack.update(self.select_attack_mod(dict_attack))
                            name = '{0} ({1})'.format(item, ammo)
                            metadict_attacks['close',name] = {}
                            metadict_attacks['close',name].update(dict_attack)
                    # Если ядов несколько, то для каждого своя атака:
                    elif isinstance(ammo_type, list):
                        for ammo in ammo_type:
                            if self.equipment_weapon.get(ammo):
                                dict_attack['ammo'] = self.equipment_weapon[ammo]
                                dict_attack.update(self.modify_attack_ammo(dict_attack, ammo))
                                dict_attack.update(self.select_attack_mod(dict_attack))
                                name = '{0} ({1})'.format(item, ammo)
                                metadict_attacks['close',name] = {}
                                metadict_attacks['close',name].update(dict_attack)
                if 'reach' in metadict_items[item].get('weapon_type'):
                    dict_attack = copy.deepcopy(metadict_items[item])
                    dict_attack['weapon_use'] = item
                    dict_attack['attack_range'] = 10
                    dict_attack['attack_type'] = 'reach'
                    dict_attack.update(self.select_attack_mod(dict_attack))
                    metadict_attacks['reach',item] = {}
                    metadict_attacks['reach',item].update(dict_attack)
                    # Ниже опциональные атаки с ядами/составами на клинке:
                    ammo_type = dict_attack.get('ammo_type')
                    if isinstance(ammo_type, str):
                        ammo = ammo_type
                        if self.equipment_weapon.get(ammo):
                            dict_attack['ammo'] = self.equipment_weapon[ammo]
                            dict_attack.update(self.modify_attack_ammo(dict_attack, ammo))
                            dict_attack.update(self.select_attack_mod(dict_attack))
                            name = '{0} ({1})'.format(item, ammo)
                            metadict_attacks['reach',name] = {}
                            metadict_attacks['reach',name].update(dict_attack)
                    # Если ядов несколько, то для каждого своя атака:
                    elif isinstance(ammo_type, list):
                        for ammo in ammo_type:
                            if self.equipment_weapon.get(ammo):
                                dict_attack['ammo'] = self.equipment_weapon[ammo]
                                dict_attack.update(self.modify_attack_ammo(dict_attack, ammo))
                                dict_attack.update(self.select_attack_mod(dict_attack))
                                name = '{0} ({1})'.format(item, ammo)
                                metadict_attacks['reach',name] = {}
                                metadict_attacks['reach',name].update(dict_attack)
                if 'throw' in metadict_items[item].get('weapon_type'):
                    dict_attack = copy.deepcopy(metadict_items[item])
                    dict_attack['weapon_use'] = item
                    dict_attack['attack_type'] = 'throw'
                    dict_attack['attack_range'] = dict_attack['throw_range']
                    dict_attack['attack_range_max'] = dict_attack['throw_range_max']
                    # Боезапас метательного оружия, внезапно, само оружие:
                    dict_attack['ammo'] = self.equipment_weapon[item]
                    dict_attack.update(self.select_attack_mod(dict_attack))
                    metadict_attacks['throw',item] = {}
                    metadict_attacks['throw',item].update(dict_attack)
                    # Ниже опциональные атаки с ядами/составами на клинке:
                    ammo_type = dict_attack.get('ammo_type')
                    if isinstance(ammo_type, str):
                        ammo = ammo_type
                        if self.equipment_weapon.get(ammo):
                            # Боеприпас метательного оружия, это само оружие:
                            dict_attack['ammo_type'] = item
                            dict_attack['ammo'] = self.equipment_weapon[item]
                            dict_attack.update(self.modify_attack_ammo(dict_attack, ammo))
                            dict_attack.update(self.select_attack_mod(dict_attack))
                            name = '{0} ({1})'.format(item, ammo)
                            metadict_attacks['throw',name] = {}
                            metadict_attacks['throw',name].update(dict_attack)
                    # Если ядов несколько, то для каждого своя атака:
                    elif isinstance(ammo_type, list):
                        for ammo in ammo_type:
                            if self.equipment_weapon.get(ammo):
                                dict_attack['ammo_type'] = item
                                dict_attack['ammo'] = self.equipment_weapon[item]
                                dict_attack.update(self.modify_attack_ammo(dict_attack, ammo))
                                dict_attack.update(self.select_attack_mod(dict_attack))
                                name = '{0} ({1})'.format(item, ammo)
                                metadict_attacks['throw',name] = {}
                                metadict_attacks['throw',name].update(dict_attack)
                # Прицельная стрельба со всеми модификаторами к атаке:
                if 'ranged' in metadict_items[item].get('weapon_type'):
                    dict_attack = copy.deepcopy(metadict_items[item])
                    dict_attack['weapon_use'] = item
                    dict_attack['attack_type'] = 'ranged'
                    dict_attack['attack_range'] = dict_attack['shoot_range']
                    dict_attack['attack_range_max'] = dict_attack['shoot_range_max']
                    # Тип боеприпаса может быть один, или список:
                    ammo_type = dict_attack.get('ammo_type')
                    if isinstance(ammo_type, str):
                        ammo = ammo_type
                        if self.equipment_weapon.get(ammo):
                            # Указываем в атаке количество доступных стрел:
                            # Затем модифицируем словарь атаки боеприпасом.
                            dict_attack['ammo'] = self.equipment_weapon[ammo]
                            dict_attack.update(self.modify_attack_ammo(dict_attack, ammo))
                            dict_attack.update(self.select_attack_mod(dict_attack))
                            name = '{0} ({1})'.format(item, ammo)
                            metadict_attacks['ranged',name] = {}
                            metadict_attacks['ranged',name].update(dict_attack)
                    # Если боеприпасов несколько, то для каждого своя атака:
                    elif isinstance(ammo_type, list):
                        for ammo in ammo_type:
                            if self.equipment_weapon.get(ammo):
                                dict_attack['ammo'] = self.equipment_weapon[ammo]
                                dict_attack.update(self.modify_attack_ammo(dict_attack, ammo))
                                dict_attack.update(self.select_attack_mod(dict_attack))
                                name = '{0} ({1})'.format(item, ammo)
                                metadict_attacks['ranged',name] = {}
                                metadict_attacks['ranged',name].update(dict_attack)
                    # Если боеприпас в оружии не указан, считается бесконечным:
                    else:
                        dict_attack.update(self.select_attack_mod(dict_attack))
                        name = '{0} ({1})'.format(item, 'endless_ammo')
                        metadict_attacks['ranged',name] = {}
                        metadict_attacks['ranged',name].update(dict_attack)
                # Неприцельная стрельба, град стрел/дротиков без модификаторов к атаке:
                if 'volley' in metadict_items[item].get('weapon_type'):
                    dict_attack = copy.deepcopy(metadict_items[item])
                    dict_attack['weapon_use'] = item
                    dict_attack['attack_type'] = 'volley'
                    if dict_attack.get('shoot_range'):
                        dict_attack['attack_range'] = dict_attack['shoot_range']
                        dict_attack['attack_range_max'] = dict_attack['shoot_range_max']
                        # Огнестрельное оружие x4 неприцельной дальности:
                        if 'firearm' in dict_attack.get('weapon_type'):
                            dict_attack['attack_range_max'] = dict_attack['shoot_range_volley']
                    elif dict_attack.get('throw_range'):
                        dict_attack['attack_range'] = dict_attack['throw_range']
                        dict_attack['attack_range_max'] = dict_attack['throw_range_max']
                    # Тип боеприпаса может быть один, или список:
                    ammo_type = dict_attack.get('ammo_type')
                    if isinstance(ammo_type, str):
                        ammo = ammo_type
                        if self.equipment_weapon.get(ammo):
                            # Указываем в атаке количество доступных стрел:
                            # Затем модифицируем словарь атаки боеприпасом.
                            dict_attack['ammo'] = self.equipment_weapon[ammo]
                            dict_attack.update(self.modify_attack_ammo(dict_attack, ammo))
                            dict_attack.update(self.select_attack_mod(dict_attack))
                            # Это неприцельный огонь, положительные модификаторы отменяются:
                            dict_attack['weapon_skills_use'] = []
                            if dict_attack['damage_mod'] > 0:
                                dict_attack['damage_mod'] = 0
                            if dict_attack['attack_mod'] > 0:
                                dict_attack['attack_mod'] = 0
                            name = '{0} ({1})'.format(item, ammo)
                            metadict_attacks['volley',name] = {}
                            metadict_attacks['volley',name].update(dict_attack)
                    # Если боеприпасов несколько, то для каждого своя атака:
                    elif isinstance(ammo_type, list):
                        for ammo in ammo_type:
                            if self.equipment_weapon.get(ammo):
                                dict_attack['ammo'] = self.equipment_weapon[ammo]
                                dict_attack.update(self.modify_attack_ammo(dict_attack, ammo))
                                dict_attack.update(self.select_attack_mod(dict_attack))
                                # Это неприцельный огонь, положительные модификаторы отменяются:
                                dict_attack['weapon_skills_use'] = []
                                if dict_attack['damage_mod'] > 0:
                                    dict_attack['damage_mod'] = 0
                                if dict_attack['attack_mod'] > 0:
                                    dict_attack['attack_mod'] = 0
                                name = '{0} ({1})'.format(item, ammo)
                                metadict_attacks['volley',name] = {}
                                metadict_attacks['volley',name].update(dict_attack)
                    # Если оружие метательное, то боеприпас, это оно само:
                    # TODO: здесь криво сделано. Лучше бы подправить, или вовсе убрать.
                    # Яды не подключаются.
                    elif not ammo_type and 'throw' in dict_attack['weapon_type']:
                        dict_attack['ammo_type'] = item
                        dict_attack['ammo'] = self.equipment_weapon[item]
                        dict_attack.update(self.modify_attack_ammo(dict_attack, ammo))
                        dict_attack.update(self.select_attack_mod(dict_attack))
                        dict_attack['weapon_skills_use'] = []
                        if dict_attack['damage_mod'] > 0:
                            dict_attack['damage_mod'] = 0
                        if dict_attack['attack_mod'] > 0:
                            dict_attack['attack_mod'] = 0
                        metadict_attacks['volley',item] = {}
                        metadict_attacks['volley',item].update(dict_attack)
                    # Если боеприпас в оружии не указан, считается бесконечным:
                    else:
                        dict_attack.update(self.select_attack_mod(dict_attack))
                        # Это неприцельный огонь, положительные модификаторы отменяются:
                        dict_attack['weapon_skills_use'] = []
                        if dict_attack['damage_mod'] > 0:
                            dict_attack['damage_mod'] = 0
                        if dict_attack['attack_mod'] > 0:
                            dict_attack['attack_mod'] = 0
                        name = '{0} ({1})'.format(item, 'endless_ammo')
                        metadict_attacks['volley',name] = {}
                        metadict_attacks['volley',name].update(dict_attack)
        return metadict_attacks

    def modify_attack_ammo(self, dict_attack, ammo):
        """Каждый боеприпас влияет на оружие.
        
        Свойства боеприпаса и оружия объединяются в атаке:
        - Кость урона боеприпаса.
        - Магические свойства боеприпаса.
        - Стоимость единичного боеприпаса.
        """
        metadict_items = self.metadict_items
        dict_ammo = copy.deepcopy(metadict_items[ammo])
        # Боеприпас указываем точно:
        dict_attack['ammo_type'] = ammo
        # Кость урона и тип урона боеприпаса:
        if dict_ammo.get('damage_dice'):
            dict_attack['damage_dice'] = dict_ammo['damage_dice']
        if dict_ammo.get('damage_type'):
            dict_attack['damage_type'] = dict_ammo['damage_type']
        # Дополняеются свойства оружия (магический боеприпас)
        if dict_ammo.get('weapon_type'):
            dict_attack['weapon_type'].extend(dict_ammo['weapon_type'])
            dict_attack['weapon_type'] = list(set(dict_attack['weapon_type']))
        # Дальность выстрела не может быть больше указанной в свойствах боеприпаса:
        if dict_ammo.get('shoot_range')\
                and dict_attack.get('shoot_range')\
                and dict_attack['shoot_range'] > dict_ammo['shoot_range']:
            dict_attack['shoot_range'] = dict_ammo['shoot_range']
            dict_attack['attack_range'] = dict_attack['shoot_range']
        if dict_ammo.get('shoot_range_max')\
                and dict_attack.get('shoot_range_max')\
                and dict_attack['shoot_range_max'] > dict_ammo['shoot_range_max']:
            dict_attack['shoot_range_max'] = dict_ammo['shoot_range_max']
            dict_attack['attack_range_max'] = dict_attack['shoot_range_max']
        # К стоимости оружия прибавляется стоимость единичного боеприпаса:
        if dict_ammo.get('cost (grams_of_gold)'):
            dict_attack['cost_ammo (grams_of_gold)'] = dict_ammo['cost (grams_of_gold)']
        #if dict_ammo.get('cost (ephesi)')\
        #        and dict_attack.get('cost (ephesi)'):
        #    dict_attack['cost (ephesi)'] += dict_ammo['cost (ephesi)']
        #if dict_ammo.get('cost (follis)')\
        #        and dict_attack.get('cost (follis)'):
        #    dict_attack['cost (follis)'] += dict_ammo['cost (follis)']
        #if dict_ammo.get('cost (gp)')\
        #        and dict_attack.get('cost (gp)'):
        #    dict_attack['cost (gp)'] += dict_ammo['cost (gp)']
        # Наконец, оружию передаются прочие свойства боеприпаса (вроде встроенного заклинания):
        for key in dict_ammo:
            if key not in dict_attack:
                dict_attack[key] = dict_ammo[key]
        return(dict_attack)

    def modify_attacks(self):
        """Перебираем атаки и добавляем к ним модификаторы способностей."""
        class_features = self.class_features
        metadict_attacks = self.attacks
        for attack_name, dict_attack in metadict_attacks.items():
            dict_attack.update(self.attack_modify_features(dict_attack))
            dict_attack.update(self.attack_modify_magic(dict_attack))
            metadict_attacks[attack_name] = dict_attack
        return metadict_attacks

    def modify_attacks_weapon_of_choice(self):
        """Отмечаем лучшее оружие."""
        class_features = self.class_features
        metadict_attacks = self.attacks
        # Укзаываем оптимальное оружие только для атак оружием.
        # Выбор природных атак рандомный, либо указан в самих атаках.
        for attack_name, dict_attack in metadict_attacks.items():
            if dict_attack.get('weapon') == True:
                metadict_attacks[attack_name]['weapon_of_choice']\
                        = self.find_weapon_of_choice(attack_name[0])
            elif not 'weapon_of_choice' in dict_attack:
                metadict_attacks[attack_name]['weapon_of_choice'] = None
        return metadict_attacks

    def attack_modify_features(self, dict_attack):
        """Добавляем модификаторы способностей к атаке и урону.
        
        Функция модифицирует одну атаку. Группы с помощью modify_attacks.
        """
        class_features = self.class_features
        # Исправляем, если не указано:
        if not dict_attack.get('weapon_type'):
            dict_attack['weapon_type'] = []
        if not dict_attack.get('weapon_skills_use'):
            dict_attack['weapon_skills_use'] = []
        # Дополняем/изменяем модификаторы в зависимости от способностей:
        attack_mod = dict_attack.get('attack_mod', 0)
        attack_mod_type = dict_attack.get('attack_mod_type',0)
        damage_mod = dict_attack.get('damage_mod', 0)
        damage_dice = dict_attack.get('damage_dice', None)
        weapon_type_list = dict_attack['weapon_type']
        weapon_skills_use = dict_attack['weapon_skills_use']
        # Большие существа наносят x2 костей урона оружием
        if self.size == 'large'\
                and dict_attack.get('weapon')\
                and not 'large_size_x2_damage_dice' in weapon_skills_use:
            weapon_skills_use.append('large_size_x2_damage_dice')
            dice = int(damage_dice[0]) * 2
            damage_dice = str(dice) + damage_dice[1:]
        elif self.size == 'huge'\
                and dict_attack.get('weapon')\
                and not 'huge_size_x3_damage_dice' in weapon_skills_use:
            weapon_skills_use.append('huge_size_x3_damage_dice')
            dice = int(damage_dice[0]) * 3
            damage_dice = str(dice) + damage_dice[1:]
        # Оружие с тегом versatile можно использовать как двуручное, если нет щита:
        if not self.armor['shield_use'] and 'damage_dice_versatile' in dict_attack:
            damage_dice = dict_attack['damage_dice_versatile']
        # Монахи могут использовать ловкость для простого и не тяжёлого оружия:
        # Также Martial_Arts позволяет изменить damage_dice оружия:
        # https://www.dandwiki.com/wiki/5e_SRD:Monk#Table:_The_monk
        if class_features.get('Martial_Arts') and dict_attack['attack_type'] == 'close':
            if self.mods['dexterity'] >= self.mods['strength'] and 'heavy' not in weapon_type_list:
                attack_mod_type = 'dexterity'
                attack_mod = self.mods['dexterity'] + self.proficiency_bonus
                damage_mod = self.mods['dexterity']
                weapon_skills_use.append('Martial_Arts')
                martial_arts_dice = self.proficiency['martial_arts_dice']
                # Сравниваем кость атаки Martial_Arts и оружия, выбираем наибольший диапазон:
                if int(damage_dice.split('d')[1]) < int(martial_arts_dice.split('d')[1]):
                    damage_dice =  martial_arts_dice
        # Рукопашные атаки монаха 6+ lvl считаются магическими. Преодолевают сопротивление урону.
        if class_features.get('Ki_Empowered_Strikes') and dict_attack['attack_type'] == 'close'\
                and not dict_attack.get('weapon') and not 'magic' in dict_attack['weapon_type']:
            dict_attack['weapon_type'].append('magic')
        # Специализации:
        # Улучшенные критические попадания бойца-чемпиона:
        if class_features.get('Champion_Improved_Critical'):
            if dict_attack['attack_type'] == 'close' or dict_attack['attack_type'] == 'reach':
                weapon_skills_use.append('Champion_Improved_Critical')
        # Скрытая атака вора:
        # https://www.dandwiki.com/wiki/5e_SRD:Rogue#Sneak_Attack
        if class_features.get('Sneak_Attack'):
            if 'finesse' in weapon_type_list or 'ranged' in weapon_type_list:
                sneak_attack_dice = self.proficiency['sneak_attack_dice']
                weapon_skills_use.append('Sneak_Attack')
        # Боевые стили:
        # Dueling можно использовать вместе с щитом. С парным/двуручным оружием нельзя:
        if class_features.get('Fighting_Style_Dueling'):
            if dict_attack['attack_type'] == 'close' or dict_attack['attack_type'] == 'reach':
                if 'two_handed' not in weapon_type_list and dict_attack['weapon']:
                    weapon_skills_use.append('Fighting_Style_Dueling')
                    damage_mod += 2
        # Great_Weapon_Fighting даёт преимущество по урону (в среднем +2 для диапазона 2d6):
        if class_features.get('Fighting_Style_Great_Weapon_Fighting'):
            if dict_attack['attack_type'] == 'close' or dict_attack['attack_type'] == 'reach':
                if 'two_handed' in weapon_type_list and 'heavy' in weapon_type_list:
                    weapon_skills_use.append('Fighting_Style_Great_Weapon_Fighting')
        # Fighting_Style_Two_Weapon_Fighting -- атака вторым оружием за счёт бонусного действия:
        if class_features.get('Fighting_Style_Two_Weapon_Fighting'):
            if dict_attack['attack_type'] == 'close' or dict_attack['attack_type'] == 'throw':
                if 'light' in weapon_type_list or 'throw' in weapon_type_list:
                    weapon_skills_use.append('Fighting_Style_Two_Weapon_Fighting')
                elif not 'heavy' in weapon_type_list and class_features.get('Feat_Dual_Wielder'):
                    weapon_skills_use.append('Fighting_Style_Two_Weapon_Fighting')
        # Archery добавляет +2 к атаке оружию дальнего боя (но не метательному):
        if class_features.get('Fighting_Style_Archery') and dict_attack['attack_type'] == 'ranged':
            if 'ranged' in weapon_type_list:
                attack_mod += 2
                weapon_skills_use.append('Fighting_Style_Archery')
        # Features:
        # Feat_Mounted_Combatant даёт преимущество в атаке на пехоту:
        if class_features.get('Feat_Mounted_Combatant')\
                and hasattr(self, 'mount_combat') and self.mount_combat == True:
            if dict_attack['attack_type'] == 'reach' or dict_attack['attack_type'] == 'close':
                weapon_skills_use.append('Feat_Mounted_Combatant')
        # Feat_Defensive_Duelist даёт возможность парировать реакцией:
        if class_features.get('Feat_Defensive_Duelist'):
            if 'finesse' in weapon_type_list and dict_attack['attack_type'] == 'close':
                weapon_skills_use.append('Feat_Defensive_Duelist')
        # Feat_Great_Weapon_Master даёт бонусную атаку после убийства/крита:
        # Также можно получить +10 урона за счёт -5 атаки:
        if class_features.get('Feat_Great_Weapon_Master') and dict_attack['attack_type'] == 'close':
            if 'two_handed' in weapon_type_list and 'heavy' in weapon_type_list:
                weapon_skills_use.append('Feat_Great_Weapon_Master')
        # Feat_Sharpshooter позволяет стрелять без помехи на макс. дальность:
        # Игнорировать укрытие; а также стрелять на +10 урон за счёт -5 атаки:
        if class_features.get('Feat_Sharpshooter') and dict_attack['attack_type'] == 'ranged':
            if 'ranged' in weapon_type_list:
                dict_attack['ignore_cover'] = True
                weapon_skills_use.append('Sharpshooter')
        # Feat_Firearms_Expert позволяет стрелять в упор без помехи:
        if class_features.get('Feat_Firearms_Expert') and dict_attack['attack_type'] == 'ranged':
            if 'ranged' in weapon_type_list and 'firearm' in weapon_type_list:
                weapon_skills_use.append('Firearms_Expert')
        attack_mod_dict = {
                'weapon_skills_use':weapon_skills_use,
                'attack_mod_type':attack_mod_type,
                'attack_mod':attack_mod,
                'damage_mod':damage_mod,
                'damage_dice':damage_dice,
                }
        return attack_mod_dict

    def attack_modify_magic(self, dict_attack):
        """Добавляем модификаторы магического оружия.
        
        - Если несколько модификаторов (стрела +1 и лук +2), то берётся наибольший.
        """
        attack_mod = dict_attack['attack_mod']
        damage_mod = dict_attack['damage_mod']
        if '+5' in dict_attack['weapon_type']:
            attack_mod += 5
            damage_mod += 5
        elif '+4' in dict_attack['weapon_type']:
            attack_mod += 4
            damage_mod += 4
        elif '+3' in dict_attack['weapon_type']:
            attack_mod += 3
            damage_mod += 3
        elif '+2' in dict_attack['weapon_type']:
            attack_mod += 2
            damage_mod += 2
        elif '+1' in dict_attack['weapon_type']:
            attack_mod += 1
            damage_mod += 1
        attack_mod_dict = {
                'attack_mod':attack_mod,
                'damage_mod':damage_mod,
                }
        return attack_mod_dict

    def find_weapon_of_choice(self, attack_type):
        """Выбор предпочитаемого оружия.
        
        На самом деле огромная проблема.
        - Пытаюсь селектировать по атаке, по урону, по весу -- всё не то.
        - Пытаюсь выбрать по навыкам (Dueling, Defensive_Duelist и т.д.) -- выбирают пиллумы.
        - Оптимальным решением оказалось простейшее. Лучшее оружие -- самое дорогое оружие.
        """
        test_weapon_cost = 0
        test_weapon_skills = 0
        weapon_of_choice = None
        weapon_of_choice_skills = None
        test_ammo_cost_max = 0
        test_ammo_cost_min = 0
        # Стоимость единичного боеприпаса:
        for attack_name, attack_dict in self.attacks.items():
            if attack_dict.get('cost_ammo (grams_of_gold)',0) > test_ammo_cost_max:
                test_ammo_cost_max = attack_dict['cost_ammo (grams_of_gold)']
            if attack_dict.get('cost_ammo (grams_of_gold)')\
                    and attack_dict['cost_ammo (grams_of_gold)'] < test_ammo_cost_max:
                test_ammo_cost_min = attack_dict['cost_ammo (grams_of_gold)']
        # Выбираем лучшее оружие (обычно самое дорогое):
        for attack_name, attack_dict in self.attacks.items():
            if attack_type in attack_name:
                if attack_dict.get('cost (grams_of_gold)',0) > test_weapon_cost:
                    test_weapon_cost = attack_dict['cost (grams_of_gold)']
                    weapon_of_choice = attack_name[1]
                if not attack_type == 'volley' and attack_dict.get('ammo')\
                        and attack_dict.get('cost (grams_of_gold)',0) >= test_weapon_cost:
                    test_weapon_cost = attack_dict['cost (grams_of_gold)']
                    weapon_of_choice = attack_name[1]
                if attack_type == 'ranged'\
                        and attack_dict.get('cost_ammo (grams_of_gold)',0) >= test_ammo_cost_min:
                    weapon_of_choice = attack_name[1]
                if attack_type == 'volley'\
                        and attack_dict.get('cost_ammo (grams_of_gold)',0) <= test_ammo_cost_min:
                    weapon_of_choice = attack_name[1]
                if attack_type == 'volley'\
                        and attack_dict.get('spell_dict'):
                    weapon_of_choice = attack_name[1]
                if len(attack_dict['weapon_skills_use']) >= test_weapon_skills:
                    test_weapon_skills = len(attack_dict['weapon_skills_use'])
                    weapon_of_choice_skills = attack_name[1]
        # Если не находим оружие по стоимости, выбираем по навыкам:
        if not weapon_of_choice:
            weapon_of_choice = weapon_of_choice_skills
        return weapon_of_choice
