#!/usr/bin/env python
# -*- coding: utf-8 -*-

import inspect
import random
import copy
import uuid

import dices

class gen_spells():
    """Заклинания представлены как функции.
    
    Параметры меняются в зависимости от способностей мага.
    """

    def __init__(self, soldier):
        # TODO: Так мы передадим заклинаниям параметры мага.
        # ------------------------------------------------------------
        # Создаётся при генерации, в soldier_base.
        # Можно просто передать словарь soldier.__dict__ в self.__dict__.
        # ------------------------------------------------------------
        self.mage = soldier
        # Это лишнее, мы можем просто вызвать self.mage.level:
        #self.mage_level = soldier.level
        #self.mage_class = soldier.char_class
        #self.mods = soldier.mods
        #self.proficiency_bonus = soldier.proficiency_bonus
        self.know_spells = soldier.class_features.get('Spells',[])
        # Нужен список методов класса, можно с примесью опций:
        #self.usable_spells = inspect.getmembers(self, predicate=inspect.ismethod)
        self.usable_spells = ([ method for method in dir(self) if not method.startswith('__')])
        self.spellslots = {}
        # Слоты заклинаний:
        for spell_slot, number in soldier.proficiency.get('spellslots').items():
            if number > 0:
                self.spellslots[spell_slot] = number
        # TODO: В отдельную функцию.
        # ------------------------------------------------------------
        # Нам нужен выбор случайных заклинаний, если в know_spells стоит random.
        # ------------------------------------------------------------
        # Динамическая генерация заклинаний:
        self.spells = {}
        for spell in self.know_spells:
            spell_name = spell[-1]
            spell_level = spell[0]
            if spell_name in self.usable_spells:
                func = getattr(self, spell_name)
                spell_dict = func(spell_level, use_spell = False)
                spell_dict['spell_choice'] = spell
                self.spells[spell] = spell_dict
        # Пополняемый список скастованных заклинаний.
        soldier.spells_active = {}
        #print(self.spells)

#----
# Декораторы:

    def modify_spell(func):
        """Кастер меняет параметры заклинания.
        
        """
        def wrapper(self, spell_level, gen_spell = False, spell_choice = False, use_spell = True):
            soldier = self.mage
            spell_dict = func(self, spell_level, gen_spell)
            #print('NYA', gen_spell, spell_choice, spell_dict)
            if spell_dict and use_spell:
                # Указываем выбор заклинания (круг и тип) в его словаре:
                spell_dict['spell_choice'] = spell_choice
                # А также uuid создателя заклинания:
                if not spell_dict.get('caster_uuid'):
                    spell_dict['caster_uuid'] = soldier.uuid
                # Даём заклинанию уникальный номер:
                # ЗАМЕТКА:
                # ------------------------------------------------------------
                # Помни, анон, только UUID v4 -- случайные числа,
                # Версии 1-2 генерируются из MAC-адреса.
                # ------------------------------------------------------------
                if not spell_dict.get('spell_uuid'):
                    spell_dict['spell_uuid'] = uuid.uuid4()
                # Бафф/дебафф передаём цели заклинания:
                if spell_dict.get('target_uuid'):
                    target = self.mage.metadict_soldiers[spell_dict['target_uuid']]
                else:
                    target = soldier
                # Переносим заклинание в список баффов/дебаффов. Они учитываются оттуда.
                if spell_dict.get('buff'):
                    target.buffs[spell_dict['effect']] = spell_dict
                if spell_dict.get('debuff') and spell_dict.get('target_uuid'):
                    target.debuffs[spell_dict['effect']] = spell_dict
                # Создаём список скастованных в бою заклинаний:
                if spell_choice:
                    if not spell_dict['spell_uuid'] in soldier.spells_active:
                        soldier.spells_active[spell_dict['spell_uuid']] = spell_dict
                    #print(len(soldier.spells_active))
                    #print('NYA', spell_choice)
                # Заклинание с соматическим компонентом не удаётся, если кастер схвачен:
                if 'somatic' in spell_dict.get('components',[])\
                        and soldier.grappled:
                    return False
                # Стихийный адепт преодолевает сопротивляемость определённому урону:
                if soldier.class_features.get('Feat_Elemental_Adept')\
                        and spell_dict.get('damage_type'):
                    ignore_resistance = soldier.class_features['Feat_Elemental_Adept']
                    if spell_dict['damage_type'] == ignore_resistance:
                        spell_dict['ignore_resistance'] = ignore_resistance
                # Артиллерист добавляет 1d8 к урону заклинаний:
                if soldier.class_features.get('Arcane_Firearm')\
                        and spell_dict.get('damage_type')\
                        and not 'use_bombs' in spell_dict:
                    if 'damage_mod' in spell_dict: spell_dict['damage_mod']\
                            += dices.dice_throw(soldier.class_features['Arcane_Firearm'])
                # Учёный алхимик добавляет модификатор интеллекта к урону:
                if soldier.class_features.get('Alchemical_Savant'):
                    if spell_dict.get('damage_type') == 'heal'\
                            or spell_dict.get('damage_type') == 'fire'\
                            or spell_dict.get('damage_type') == 'acid'\
                            or spell_dict.get('damage_type') == 'necrotic'\
                            or spell_dict.get('damage_type') == 'necrotic_energy'\
                            or spell_dict.get('damage_type') == 'poison':
                        if 'damage_mod' in spell_dict: spell_dict['damage_mod']\
                                += self.mage.mods['intelligence']
                        if 'healing_mod' in spell_dict: spell_dict['healing_mod']\
                                += self.mage.mods['intelligence']
                # Магическая защита восстанавливается или создаётся:
                if soldier.class_features.get('Arcane_Ward')\
                        and spell_dict.get('school') == 'abjuration':
                    if soldier.arcane_ward and not soldier.bonus_hitpoints:
                        soldier.bonus_hitpoints = int(spell_dict['spell_level'][0]) * 2
                    elif not soldier.arcane_ward and not soldier.bonus_hitpoints:
                        soldier.bonus_hitpoints = soldier.level * 2 + soldier.mods['intelligence']
                        soldier.arcane_ward = True
                return spell_dict
            elif spell_dict and not use_spell:
                if soldier.class_features.get('Feat_Spellsniper')\
                        and not spell_dict.get('direct_hit')\
                        and spell_dict.get('damage_type'):
                    spell_dict['ignore_cover'] = True
                    spell_dict['attack_range'] *= 2
                return spell_dict
            else:
                # - Absorb_Elements не срабатывает, если урон не в absorb_damage_type.
                #raise Exception("Заклинание не сработало", func.__name__, spell_choice)
                pass
        return wrapper

    def update_spell_dict(func):
        """Передача параметров заклинанию.

        - Параметры должны быть словарём.
        - Словарь изменений можно передать в spell_dict или в gen_spell.
        """
        def wrapper(self, spell_level, gen_spell = False, spell_choice = False, spell_dict = False):
            # Получаем базовый словарь заклинания:
            spell_dict_raw = func(self, spell_level, gen_spell = False)
            if spell_dict_raw and spell_dict and type(spell_dict) == dict:
                # Обновляем словарь заклинания:
                # Исполняем функцию с обновлёнными параметрами:
                spell_dict_raw.update(spell_dict)
                spell_dict = func(self, spell_level, gen_spell, spell_dict_raw)
                return spell_dict
            elif spell_dict_raw and gen_spell and type(gen_spell) == dict:
                spell_dict_raw.update(gen_spell)
                spell_dict = func(self, spell_level, gen_spell, spell_dict_raw)
                return spell_dict
            elif spell_dict_raw:
                spell_dict = func(self, spell_level, gen_spell)
                return spell_dict
            else:
                #raise Exception("Заклинание не сработало", func.__name__, spell_choice)
                pass
        return wrapper

#----
# Методы:

    def find_spell_attack_mod(self, proficiency_bonus = True):
        """Модификатор атаки заклинания зависит от класса.
        
        У волшебников это интеллект, у чародеев харизма, у жрецов мудрость.
        """
        # TODO: перенеси это в список, в classes.py
        if self.mage.char_class == 'Wizard'\
                or self.mage.char_class == 'Artificier'\
                or self.mage.char_class == 'Arcane_Tricker'\
                or self.mage.char_class == 'Eldritch_Knight'\
                or self.mage.char_class == 'Rogue':
            attack_mod = self.mage.mods['intelligence']
        elif self.mage.char_class == 'Sorcerer'\
                or self.mage.char_class == 'Bard'\
                or self.mage.char_class == 'Warlock'\
                or self.mage.char_class == 'Barbarian'\
                or self.mage.char_class == 'Paladin':
            attack_mod = self.mage.mods['charisma']
        elif self.mage.char_class == 'Cleric'\
                or self.mage.char_class == 'Cleric-heavy'\
                or self.mage.char_class == 'Druid'\
                or self.mage.char_class == 'Ranger'\
                or self.mage.char_class == 'Monk':
            attack_mod = self.mage.mods['wisdom']
        elif self.mage.char_class == 'Empyrean':
            attack_mod = self.mage.mods['charisma']
        else:
            # Если класса нет в списке, выбираем маскимальную характеристику:
            mods = self.mage.mods
            mods_list = [mods['intelligence'], mods['wisdom'], mods['charisma']]
            attack_mod = max(mods_list)
        if proficiency_bonus:
            attack_mod += self.mage.proficiency_bonus
        return attack_mod

    def find_spell(self, spell_name, effect = False):
        """Поиск заклинания из доступных.
        
        Возможен по эффекту заклинания. Тогда spell_name это effect.
        Случайный выбор, если несколько одинаковых заклинаний на разных уровнях.
        """
        if effect:
            spell_list = [spell for spell in self.spells
                    if self.spells[spell].get('effect') == spell_name]
        else:
            spell_list = [spell for spell in self.spells if spell[-1] == spell_name]
        if spell_list:
            spell_choice = random.choice(spell_list)
            return spell_choice

    def get_spell_dict(self, spell_choice, gen_spell = False, spell_dict = False):
        """Берём словарь заклинания из функции."""
        # TODO: почему я здесь указал 1_lvl? Проверить!
        # Ясно почему, потому что иначе ломаются проверки на int в заклинаниях.
        # Исправляется это не здесь, а в функции try_spellcast и ей подобных.
        spell_level = '1_lvl'
        #spell_level = spell_choice[0]
        if type(spell_choice) == tuple:
            spell_name = spell_choice[-1]
        else:
            spell_name = spell_choice
        func = getattr(self, spell_name)
        spell_dict = func(spell_level, gen_spell, spell_choice, use_spell = False)
        return spell_dict

    def use_buff(self, spell_choice, gen_spell = True, use_spell = True):
        """Используем функцию заклинания.
        
        - Меняет параметры солдата. if gen_spell в заклинании.
        - При этом не должен запускаться декоратор modify_spell.
        """
        # Декоратор таки запускается. Используется use_spell = True
        spell_level = '1_lvl'
        #spell_level = spell_choice[0]
        spell_name = spell_choice[-1]
        func = getattr(self, spell_name)
        spell_dict = func(spell_level, gen_spell, spell_choice, use_spell)
        return spell_dict

    def use_spell(self, spell_choice, gen_spell = False, use_spell_slot = True):
        """Расходуется ячейка заклинания, очищается словарь self.spells."""
        spell_slot_use = spell_choice[0]
        # Заклинания 0 уровня бесконечные:
        if spell_slot_use == 'cantrip':
            spell_level = spell_slot_use
            spell_name = spell_choice[-1]
            func = getattr(self, spell_name)
            spell_dict = func(spell_level, gen_spell, spell_choice)
            return spell_dict
        # Вызываем заклинание как способность, например Bardic_Inspiration:
        if type(use_spell_slot) == str:
            spell_level = '1_lvl'
            spell_name = spell_choice[-1]
            func = getattr(self, spell_name)
            spell_dict = func(spell_level, gen_spell, spell_choice)
            return spell_dict
        # Вызываем заклинание без ячейки, заклинание любое из доступных:
        if not use_spell_slot:
            spell_level = '1_lvl'
            spell_name = spell_choice[-1]
            func = getattr(self, spell_name)
            spell_dict = func(spell_level, gen_spell, spell_choice)
            return spell_dict
        # Используем ячейку заклинания:
        for spell_slot in self.spellslots:
            if spell_slot == spell_slot_use:
                # Генерируем заклинание, в том числе и неизвестное магу:
                if self.spellslots[spell_slot] > 0 and gen_spell:
                    self.spellslots[spell_slot] -= 1
                    spell_level = spell_slot[0]
                    spell_name = spell_choice[-1]
                    func = getattr(self, spell_name)
                    spell_dict = func(spell_level, gen_spell, spell_choice)
                # Используем подготовленное заклинание из списка заклинаний:
                elif self.spellslots[spell_slot] > 0:
                    self.spellslots[spell_slot] -= 1
                    gen_spell = False
                    spell_level = spell_slot[0]
                    spell_name = spell_choice[-1]
                    func = getattr(self, spell_name)
                    spell_dict = func(spell_level, gen_spell, spell_choice)
                    #spell_dict = copy.deepcopy(self.spells[spell_choice])
                    #spell_dict['spell_choice'] = spell_choice
                if self.spellslots[spell_slot] <= 0:
                    # Убираем закончившиеся ячейки:
                    # Убираем заклинания этого уровня, если ячейки закончились:
                    self.spellslots.pop(spell_slot)
                    spells_to_remove = [spell for spell in self.spells if spell[0] == spell_slot_use]
                    for spell in spells_to_remove:
                        self.spells.pop(spell)
                return spell_dict

#------------------------------------------------------------
# Состояния

    @modify_spell
    @update_spell_dict
    def Blinded(self, spell_level, gen_spell = False, spell_dict = False):
        """Ослепление. Ослеплённый.
        
        - Преимущество на атаки врагов.
        - Автоматический провал всех проверок, связанных со зрением.

        # https://www.dandwiki.com/wiki/5e_SRD:Conditions#Blinded
        """
        # Используем тот же формат, что и для заклинаний.
        # Длительность эффектов указана базовая.
        if not spell_dict:
            spell_dict = {
                    'debuff':True,
                    'effect':'blinded',
                    'effect_timer':10,
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_ability':'constitution',
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    }
            # Делаем полную копию словаря, чтобы оригинал не изменялся.
            spell_dict = copy.deepcopy(spell_dict)
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Charmed(self, spell_level, gen_spell = False, spell_dict = False):
        """Очарование. Очарованный.
        
        - Цель не будет вредить кастеру.
        - Преимущество на социальные броски кастеру.

        # https://www.dandwiki.com/wiki/5e_SRD:Conditions#Charmed
        """
        if not spell_dict:
            spell_dict = {
                    'debuff':True,
                    'effect':'charmed',
                    'effect_timer':10,
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_ability':'wisdom',
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    }
            spell_dict = copy.deepcopy(spell_dict)
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Deafened(self, spell_level, gen_spell = False, spell_dict = False):
        """Потеря слуха. Оглохший.
        
        - Автоматический провал всех проверок, связанных со слухом.

        # https://www.dandwiki.com/wiki/5e_SRD:Conditions#Deafened
        """
        if not spell_dict:
            spell_dict = {
                    'debuff':True,
                    'effect':'deafened',
                    'effect_timer':10,
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_ability':'constitution',
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    }
            spell_dict = copy.deepcopy(spell_dict)
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Exhaustion(self, spell_level, gen_spell = False, spell_dict = False):
        """Истощение. Истощённый.
        
        Шесть уровней истощения:
        1. Помеха на проверки характеристик.
        2. Скорость уменьшается вдвое.
        3. Помеха на броски атаки и спасброски.
        4. Максимум хитов уменьшается вдвое.
        5. Скорость уменьшается до 0.
        6. Смерть.
        
        # https://www.dandwiki.com/wiki/5e_SRD:Conditions#Exhaustion
        """
        if not spell_dict:
            spell_dict = {
                    'debuff':True,
                    'effect':'exhaustion',
                    'effect_timer':4800,
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_ability':'constitution',
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    }
            spell_dict = copy.deepcopy(spell_dict)
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Frightened(self, spell_level, gen_spell = False, spell_dict = False):
        """Испуг. Испуганный.
        
        Если источник страха видим:
        - Помеха на броски атаки и проверки характеристик.
        - Цель не может добровольно приблизиться к источнику страха.
        
        # https://www.dandwiki.com/wiki/5e_SRD:Conditions#Frightened
        """
        if not spell_dict:
            spell_dict = {
                    'debuff':True,
                    'effect':'frightened',
                    'effect_timer':10,
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_ability':'wisdom',
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    }
            spell_dict = copy.deepcopy(spell_dict)
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Grappled(self, spell_level, gen_spell = False, spell_dict = False):
        """Захват. Схваченный.
        
        - Скорость = 0. Нет никаких бонусов к скорости.
        - Захват прекращается, если схвативший недееспособен.
        - Захват прекращается, если цель вне радиуса захвата.
        
        # https://www.dandwiki.com/wiki/5e_SRD:Conditions#Grappled
        """
        if not spell_dict:
            spell_dict = {
                    'debuff':True,
                    'effect':'grappled',
                    'effect_timer':100,
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_ability':'strength',
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    }
            spell_dict = copy.deepcopy(spell_dict)
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Incapacitated(self, spell_level, gen_spell = False, spell_dict = False):
        """Недееспособность. Недееспособный.

        - Недееспособный не может двигаться
        - Недееспособный не может совершать действия или реакции.
        
        # https://www.dandwiki.com/wiki/5e_SRD:Conditions#Incapacitated
        """
        if not spell_dict:
            spell_dict = {
                    'debuff':True,
                    'effect':'incapacitated',
                    'effect_timer':600,
                    'direct_hit':True,
                    #'savethrow':True,
                    #'savethrow_ability':'constitution',
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    }
            spell_dict = copy.deepcopy(spell_dict)
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Invisible(self, spell_level, gen_spell = False, spell_dict = False):
        """Невидимость. Невидимый.

        - Броски атаки по невидимке с помехой.
        - Броски атаки невидимого с преимуществом.
        - Существо считается сильно заслонённым с точки зрения скрытности.
        
        # https://www.dandwiki.com/wiki/5e_SRD:Conditions#Invisible
        """
        if not spell_dict:
            spell_dict = {
                    'buff':True,
                    'effect':'invisible',
                    'effect_timer':600,
                    'direct_hit':True,
                    #'savethrow':True,
                    #'savethrow_ability':'intelligence',
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    }
            spell_dict = copy.deepcopy(spell_dict)
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Paralyzed(self, spell_level, gen_spell = False, spell_dict = False):
        """Паралич. Парализованный.

        - Парализованный = недееспособный
        - Автоматический провал спасбросков Силы и Ловкости.
        - Преимущество на броски атаки врагу.
        - Каждая атака -- критическая, если враг в 5 футах от цели.
        
        # https://www.dandwiki.com/wiki/5e_SRD:Conditions#Paralyzed
        """
        if not spell_dict:
            spell_dict = {
                    'debuff':True,
                    'effect':'paralyzed',
                    'effect_timer':10,
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_ability':'constitution',
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    }
            spell_dict = copy.deepcopy(spell_dict)
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Petrified(self, spell_level, gen_spell = False, spell_dict = False):
        """Окаменение. Окаменевший.

        - Вес существа увеличивается вдесятеро. Плотность? Нет, не слышали.
        - Окаменевший = недееспособный
        - Преимущество на броски атаки врагу.
        - Автоматический провал спасбросков Силы и Ловкости.
        - Сопротивляемость любому урону
        - Иммунитет к ядам и болезням

        # https://www.dandwiki.com/wiki/5e_SRD:Conditions#Petrified
        """
        if not spell_dict:
            spell_dict = {
                    'debuff':True,
                    'effect':'petrified',
                    'effect_timer':4800,
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_ability':'constitution',
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    }
            spell_dict = copy.deepcopy(spell_dict)
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Poisoned(self, spell_level, gen_spell = False, spell_dict = False):
        """Отравление. Отравленный.

        - Помеха на броски атаки.
        - Помеха на проверки характеристик.

        # https://www.dandwiki.com/wiki/5e_SRD:Conditions#Poisoned
        """
        if not spell_dict:
            spell_dict = {
                    'debuff':True,
                    'effect':'poisoned',
                    'effect_timer':600,
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_ability':'constitution',
                    'savethrow_advantage':False,
                    'savethrow_disadvantage':False,
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if gen_spell:
            if not spell_dict.get('target_uuid'):
                soldier = self.mage
            else:
                soldier = self.mage.metadict_soldiers[spell_dict['target_uuid']]
            difficult = spell_dict['spell_save_DC']
            ability = spell_dict['savethrow_ability']
            advantage = spell_dict['savethrow_advantage']
            disadvantage = spell_dict['savethrow_disadvantage']
            # Спасбросок против отравления:
            if 'antidote' in soldier.buffs:
                advantage = True
            if soldier.get_savethrow(difficult, ability, advantage, disadvantage)\
                    or 'poisoned' in soldier.immunity:
                return False
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Prone(self, spell_level, gen_spell = False, spell_dict = False):
        """Сбитый с ног. Лежащий ничком.

        - Передвигается ползком.
        - Помеха на броски атаки.
        - Помеха на броски атаки врагу. Если он дальше 5 футов.
        - Преимущество на броски атаки врагу. Если он в пределах 5 футов.

        # https://www.dandwiki.com/wiki/5e_SRD:Conditions#Prone
        """
        if not spell_dict:
            spell_dict = {
                    'debuff':True,
                    'effect':'prone',
                    'effect_timer':10,
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_ability':'strength',
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    }
            spell_dict = copy.deepcopy(spell_dict)
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Restrained(self, spell_level, gen_spell = False, spell_dict = False):
        """Опутывание. Опутанный.

        - Скорость = 0. Нет никаких бонусов к скорости.
        - Помеха на броски атаки.
        - Преимущество на броски атаки врагу.
        - Помеха на спасброски Ловкости.

        # https://www.dandwiki.com/wiki/5e_SRD:Conditions#Restrained
        """
        if not spell_dict:
            spell_dict = {
                    'debuff':True,
                    'effect':'restrained',
                    'effect_timer':100,
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_ability':'strength',
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    }
            spell_dict = copy.deepcopy(spell_dict)
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Stunned(self, spell_level, gen_spell = False, spell_dict = False):
        """Ошеломление. Ошеломлённый. Оглушение.

        - Ошеломлённый = недееспособный
        - Автоматический провал спасбросков Силы и Ловкости.
        - Преимущество на броски атаки врагу.

        # https://www.dandwiki.com/wiki/5e_SRD:Conditions#Stunned
        """
        if not spell_dict:
            spell_dict = {
                    'debuff':True,
                    'effect':'stunned',
                    'effect_timer':1,
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_danger':True,
                    'savethrow_ability':'constitution',
                    'savethrow_advantage':False,
                    'savethrow_disadvantage':False,
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if gen_spell:
            if not spell_dict.get('target_uuid'):
                soldier = self.mage
            else:
                soldier = self.mage.metadict_soldiers[spell_dict['target_uuid']]
            difficult = spell_dict['spell_save_DC']
            ability = spell_dict['savethrow_ability']
            advantage = spell_dict['savethrow_advantage']
            disadvantage = spell_dict['savethrow_disadvantage']
            danger = spell_dict.get('savethrow_danger', False)
            # Спасбросок против ошеломления:
            if soldier.get_savethrow(difficult, ability, advantage, disadvantage, danger)\
                    or 'stunned' in soldier.immunity:
                return False
            else:
                # Лишаем действий:
                soldier.battle_action = False
                soldier.bonus_action = False
                soldier.reaction = False
                soldier.dodge_action = False
                soldier.stunned_difficult = spell_dict['spell_save_DC']
                soldier.stunned_timer = spell_dict.get('effect_timer', 1)
                soldier.stunned = True
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Unconscious(self, spell_level, gen_spell = False, spell_dict = False):
        """Без сознания. Бессознательный.

        - Бессознательный = недееспособный
        - Теряет предметы из рук и падает (Prone)
        - Автоматический провал спасбросков Силы и Ловкости.
        - Преимущество на броски атаки врагу.
        - Каждая атака -- критическая, если враг в 5 футах от цели.

        # https://www.dandwiki.com/wiki/5e_SRD:Conditions#Unconscious
        """
        if not spell_dict:
            spell_dict = {
                    'debuff':True,
                    'effect':'unconscious',
                    'effect_timer':600,
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_ability':'constitution',
                    'savethrow_advantage':False,
                    'savethrow_disadvantage':False,
                    'spell_level':spell_level,
                    # Обычно это потеря сознания от ран или заклинания "Sleep":
                    'spell_save_DC':100,
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if gen_spell:
            if not spell_dict.get('target_uuid'):
                soldier = self.mage
            else:
                soldier = self.mage.metadict_soldiers[spell_dict['target_uuid']]
            difficult = spell_dict['spell_save_DC']
            ability = spell_dict['savethrow_ability']
            advantage = spell_dict['savethrow_advantage']
            disadvantage = spell_dict['savethrow_disadvantage']
            # Спасбросок только от усыпления ядами:
            #if 'antidote' in soldier.buffs:
            #    advantage = True
            # Спасбросок против потери сознания (от яда):
            if soldier.get_savethrow(difficult, ability, advantage, disadvantage)\
                    or 'unconscious' in soldier.immunity:
                return False
            else:
                soldier.battle_action = False
                soldier.bonus_action = False
                soldier.reaction = False
                soldier.dodge_action = False
                soldier.prone = True
        return spell_dict

#------------------------------------------------------------
# Зелья

    @modify_spell
    @update_spell_dict
    def Antidote(self, spell_level, gen_spell = False, spell_dict = False):
        """Антидот. Противоядие.
        
        Даёт преимущество к спасброскам от ядов.
        """
        if not spell_dict:
            spell_dict = {
                    'buff':True,
                    'effect':'antidote',
                    'effect_timer':600,
                    'casting_time':'free_action',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if gen_spell:
            if not spell_dict.get('target_uuid'):
                soldier = self.mage
            else:
                soldier = self.mage.metadict_soldiers[spell_dict['target_uuid']]
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Rage(self, spell_level, gen_spell = False, spell_dict = False):
        """Ярость. 50% сопротивляемость обычному оружию.
        
        Что это даёт:
        - Сопротивляемость к урону обычного оружия.
        - Дополнительный урон, что зависит от уровня варвара, либо +1.
        """
        # TODO: Перенести сюда способность варвара из set_rage.
        # 1) Сделай отмену бонусов, когда таймер заканчивается.
        if not spell_dict:
            spell_dict = {
                    'buff':True,
                    'effect':'rage',
                    'effect_timer':10,
                    'casting_time':'free_action',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if gen_spell:
            if not spell_dict.get('target_uuid'):
                soldier = self.mage
            else:
                soldier = self.mage.metadict_soldiers[spell_dict['target_uuid']]
            soldier.rage = True
            soldier.resistance.append('slashing')
            soldier.resistance.append('piercing')
            soldier.resistance.append('bludgeoning')
        return spell_dict

#------------------------------------------------------------
# Способности

    @modify_spell
    @update_spell_dict
    def Bardic_Inspiration(self, spell_level, gen_spell = False, spell_dict = False):
        """Вдохновение барда.
        
        Даёт бонус к атаке/спасброску или проверке характеристики на выбор воодушевлённого.
        """
        if not spell_dict:
            spell_dict = {
                    'buff':True,
                    'class_feature':True,
                    'effect':'bardic_inspiration',
                    'effect_timer':100,
                    'direct_hit':True,
                    'inspiration_dice':self.mage.proficiency['bardic_inspiration'],
                    'attacks_number':self.find_spell_attack_mod(proficiency_bonus = False),
                    'attack_range':60,
                    'components':['verbal'],
                    'casting_time':'bonus_action',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if gen_spell:
            if not spell_dict.get('target_uuid'):
                soldier = self.mage
            else:
                soldier = self.mage.metadict_soldiers[spell_dict['target_uuid']]
            spell_dict['inspiration_mod'] = dices.dice_throw(spell_dict['inspiration_dice'])
            # Бард тратит свои вдохновения, передавая их бойцу:
            #print(soldier.rank, self.mage.rank, self.mage.inspiring_bard_number)
            self.mage.inspiring_bard_number -= 1
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Repair_Eldritch_Cannon(self, spell_level, gen_spell = False, spell_dict = False):
        """Изобретатель-артиллерист восстанавливает своё орудие."""
        if not spell_dict:
            spell_dict = {
                    'direct_hit':True,
                    'attacks_number':1,
                    'attack_range':0,
                    'damage_type':'heal',
                    'healing_dice':'0d0',
                    'healing_mod':0,
                    'components':['somatic'],
                    'casting_time':'action',
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Bane',
                    'school':'transmutation',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if gen_spell:
            if not spell_dict.get('target_uuid'):
                soldier = self.mage
            else:
                soldier = self.mage.metadict_soldiers[spell_dict['target_uuid']]
            cannon = soldier.squad.metadict_soldiers[soldier.mount_uuid]
            cannon.captured = False
            cannon.defeat = False
            cannon.death = False
            cannon.fall = False
            cannon.hitpoints = cannon.hitpoints_max
            soldier.battle.place_unit(cannon, soldier.place)
        return spell_dict


#------------------------------------------------------------
# Заклинания

#----
# Channel_Divinity

    @modify_spell
    @update_spell_dict
    def Radiance_of_the_Dawn(self, spell_level, gen_spell = False, spell_dict = False):
        """Сияние рассвета.
        
        """
        # Абсолютно убийственная способность. Сотни обожённых, сотни смертей.
        # Можно защититься баррикадами, которые и без того нередко используются в бою.
        # Как вариант, пусть работает только против волшебных созданий: нежити, демонов, духов и фей.
        # Пока что урон ослаблен 2d10 > 1d10. Зато на 5 lvl урон повышается.
        if not spell_dict:
            spell_dict = {
                    'effect':'channel',
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_ability':'constitution',
                    'attacks_number':1,
                    'radius':30,
                    'attack_range':5,
                    'damage_type':'radiant',
                    'damage_dice':'1d10',
                    'components':['somatic'],
                    'casting_time':'action',
                    'damage_mod':0,
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Sacred_Flame',
                    }
            # Делаем полную копию словаря, чтобы оригинал не изменялся.
            spell_dict = copy.deepcopy(spell_dict)
        if self.mage.level >= 5:
            spell_dict['damage_dice'] = '2d10'
        if self.mage.level >= 11:
            spell_dict['damage_dice'] = '3d10'
        if self.mage.level >= 17:
            spell_dict['damage_dice'] = '4d10'
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Divine_Smite(self, spell_level, gen_spell = False, spell_dict = False):
        """Божественная кара.
        
        """
        # TODO: эта атака усиливается критическим ударом.
        # Кроме того наносит дополнительные 1d8 урона нежити и исчадиям.
        if not spell_dict:
            spell_dict = {
                    'effect':'smite',
                    'direct_hit':True,
                    'attacks_number':1,
                    'attack_range':5,
                    'damage_type':'radiant',
                    'damage_dice':'2d8',
                    'components':[],
                    'casting_time':None,
                    'damage_mod':0,
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Sacred_Flame',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if int(spell_level[0]) > 1:
            dice = int(spell_dict['damage_dice'][0])
            dice += int(spell_level[0]) - 1
            spell_dict['damage_dice'] = str(dice) + spell_dict['damage_dice'][1:]
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Sacred_Weapon(self, spell_level, gen_spell = False, spell_dict = False):
        """Священное оружие.
        
        Oath_of_Devotion
        """
        if not spell_dict:
            spell_dict = {
                    'effect':'sacred_weapon',
                    'effect_timer':10,
                    #'subspell':'Light',
                    'components':[],
                    'casting_time':None,
                    'attack_mod':self.mage.mods['charisma'],
                    'damage_mod':0,
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Sacred_Flame',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Dreadful_Aspect(self, spell_level, gen_spell = False, spell_dict = False):
        """Пугающее присутствие антипаладина.

        Channel_Dreadful_Aspect
        """
        if not spell_dict:
            spell_dict = {
                    'effect':'fear',
                    'attacks_number':1,
                    'zone':True,
                    'radius':30,
                    'attack_range':5,
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_all':True,
                    'savethrow_ability':'wisdom',
                    'components':['verbal'],
                    'casting_time':'action',
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Dreadful_Aspect',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Wrath_of_the_Storm(self, spell_level, gen_spell = False, spell_dict = False):
        """Контратака жреца

        """
        if not spell_dict:
            spell_dict = {
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_ability':'dexterity',
                    'attacks_number':1,
                    'attack_range':5,
                    'damage_type':'lightning',
                    'damage_dice':'2d8',
                    'components':['verbal'],
                    'casting_time':'action',
                    'damage_mod':0,
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Wrath_of_the_Storm',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        return spell_dict

#----
# Cantrips

    @modify_spell
    @update_spell_dict
    def Eldritch_Blast(self, spell_level, gen_spell = False, spell_dict = False):
        """Мистический заряд.

        Level: Cantrip
        Casting time: 1 Action
        Range: 120 feet
        Components: V, S
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/eldritch-blast
        """
        if not spell_dict:
            spell_dict = {
                    'attacks_number':1,
                    'attack_range':120,
                    'damage_type':'force',
                    'damage_dice':'1d10',
                    'components':['verbal','somatic'],
                    'casting_time':'action',
                    'spell_level':spell_level,
                    'damage_mod':0,
                    'attack_mod':self.find_spell_attack_mod(),
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    # TODO: сделай выбор оптимального заклинания:
                    'spell_of_choice':'Eldritch_Blast',
                    'school':'evocation',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if self.mage.class_features.get('Invocation_Agonizing_Blast'):
            spell_dict['damage_mod'] = self.mage.mods['charisma']
        if self.mage.class_features.get('Invocation_Eldritch_Spear'):
            spell_dict['attack_range'] = 300
        if self.mage.level >= 5:
            spell_dict['attacks_number'] = 2
        if self.mage.level >= 11:
            spell_dict['attacks_number'] = 3
        if self.mage.level >= 17:
            spell_dict['attacks_number'] = 4
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Fire_Bolt(self, spell_level, gen_spell = False, spell_dict = False):
        """Огненный снаряд.

        Level: Cantrip
        Casting time: 1 Action
        Range: 120 feet
        Components: V, S
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/fire-bolt
        """
        if not spell_dict:
            spell_dict = {
                    'attacks_number':1,
                    'attack_range':120,
                    'damage_type':'fire',
                    'damage_dice':'1d10',
                    'components':['verbal','somatic'],
                    'casting_time':'action',
                    'spell_level':spell_level,
                    'damage_mod':0,
                    'attack_mod':self.find_spell_attack_mod(),
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Fire_Bolt',
                    'school':'evocation',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if self.mage.level >= 5:
            spell_dict['damage_dice'] = '2d10'
        if self.mage.level >= 11:
            spell_dict['damage_dice'] = '3d10'
        if self.mage.level >= 17:
            spell_dict['damage_dice'] = '4d10'
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Shocking_Grasp(self, spell_level, gen_spell = False, spell_dict = False):
        """Электрошок.

        Level: Cantrip
        Casting time: 1 Action
        Range: Touch
        Components: V, S
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/shocking-grasp
        """
        # Преимущество по бойцам в доспехах из металла в test_enemy_defence.
        if not spell_dict:
            spell_dict = {
                    'debuff':True,
                    'effect':'shocking_grasp',
                    'effect_timer':2,
                    'attacks_number':1,
                    'attack_range':5,
                    'damage_type':'lightning',
                    'damage_dice':'1d8',
                    'components':['verbal','somatic'],
                    'casting_time':'action',
                    'spell_level':spell_level,
                    'damage_mod':0,
                    'attack_mod':self.find_spell_attack_mod(),
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Shocking_Grasp',
                    'school':'evocation',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if self.mage.level >= 5:
            spell_dict['damage_dice'] = '2d8'
        if self.mage.level >= 11:
            spell_dict['damage_dice'] = '3d8'
        if self.mage.level >= 17:
            spell_dict['damage_dice'] = '4d8'
        if gen_spell:
            if not spell_dict.get('target_uuid'):
                soldier = self.mage
            else:
                soldier = self.mage.metadict_soldiers[spell_dict['target_uuid']]
                if soldier.reaction:
                    soldier.reaction = False
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Acid_Splash(self, spell_level, gen_spell = False, spell_dict = False):
        """Брызги кислоты.
        
        Поражает две цели, если не сумеют уклониться.

        Level: Cantrip
        Casting time: 1 Action
        Range: 60 feet
        Components: V, S
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/acid-splash
        """
        # TODO: две разные цели, обе должны быть рядом. Сделай через эффект.
        # Да не, фигня получается, лишнее переусложнение. Пусть будет пока так.
        if not spell_dict:
            spell_dict = {
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_all':True,
                    'savethrow_ability':'dexterity',
                    'attacks_number':2,
                    'attack_range':60,
                    'damage_type':'acid',
                    'damage_dice':'1d6',
                    'components':['verbal','somatic'],
                    'casting_time':'action',
                    'spell_level':spell_level,
                    'damage_mod':0,
                    'attack_mod':self.find_spell_attack_mod(),
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Acid_Splash',
                    'school':'conjuration',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if self.mage.level >= 5:
            spell_dict['damage_dice'] = '2d6'
        if self.mage.level >= 11:
            spell_dict['damage_dice'] = '3d6'
        if self.mage.level >= 17:
            spell_dict['damage_dice'] = '4d6'
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Vicious_Mockery(self, spell_level, gen_spell = False, spell_dict = False):
        """Злая насмешка

        Level: Cantrip
        Casting time: 1 Action
        Range: 60 feet
        Components: V
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/vicious-mockery
        """
        if not spell_dict:
            spell_dict = {
                    'debuff':True,
                    'effect':'mockery',
                    'effect_timer':2,
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_all':True,
                    'savethrow_ability':'wisdom',
                    'attacks_number':1,
                    'attack_range':60,
                    'damage_type':'psychic',
                    'damage_dice':'1d4',
                    'components':['verbal'],
                    'casting_time':'action',
                    'spell_level':spell_level,
                    'damage_mod':0,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Vicious_Mockery',
                    'school':'enchantment',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if self.mage.level >= 5:
            spell_dict['damage_dice'] = '2d4'
        if self.mage.level >= 11:
            spell_dict['damage_dice'] = '3d4'
        if self.mage.level >= 17:
            spell_dict['damage_dice'] = '4d4'
        if gen_spell:
            if not spell_dict.get('target_uuid'):
                soldier = self.mage
            else:
                soldier = self.mage.metadict_soldiers[spell_dict['target_uuid']]
            # Спасбросок против помехи на следующую атаку:
            difficult = spell_dict['spell_save_DC']
            ability = spell_dict['savethrow_ability']
            advantage = spell_dict.get('savethrow_advantage', False)
            disadvantage = spell_dict.get('savethrow_disadvantage', False)
            if soldier.get_savethrow(difficult, ability, advantage, disadvantage):
                return False
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Frostbite(self, spell_level, gen_spell = False, spell_dict = False):
        """Обморожение.

        Level: Cantrip
        Casting time: 1 Action
        Range: 60 feet
        Components: V, S
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/frostbite
        """
        if not spell_dict:
            spell_dict = {
                    'debuff':True,
                    'effect':'frostbite',
                    'effect_timer':2,
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_all':True,
                    'savethrow_ability':'constitution',
                    'attacks_number':1,
                    'attack_range':60,
                    'damage_type':'cold',
                    'damage_dice':'1d6',
                    'components':['verbal','somatic'],
                    'casting_time':'action',
                    'spell_level':spell_level,
                    'damage_mod':0,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Frostbite',
                    'school':'evocation',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if self.mage.level >= 5:
            spell_dict['damage_dice'] = '2d6'
        if self.mage.level >= 11:
            spell_dict['damage_dice'] = '3d6'
        if self.mage.level >= 17:
            spell_dict['damage_dice'] = '4d6'
        if gen_spell:
            if not spell_dict.get('target_uuid'):
                soldier = self.mage
            else:
                soldier = self.mage.metadict_soldiers[spell_dict['target_uuid']]
            # Спасбросок против помехи на следующую атаку:
            difficult = spell_dict['spell_save_DC']
            ability = spell_dict['savethrow_ability']
            advantage = spell_dict.get('savethrow_advantage', False)
            disadvantage = spell_dict.get('savethrow_disadvantage', False)
            if soldier.get_savethrow(difficult, ability, advantage, disadvantage):
                return False
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Sacred_Flame(self, spell_level, gen_spell = False, spell_dict = False):
        """Священное пламя.

        Level: Cantrip
        Casting time: 1 Action
        Range: 60 feet
        Components: V, S
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/sacred-flame
        """
        if not spell_dict:
            spell_dict = {
                    'direct_hit':True,
                    'ignore_cover':True,
                    'savethrow':True,
                    'savethrow_all':True,
                    'savethrow_ability':'dexterity',
                    'attacks_number':1,
                    'attack_range':60,
                    'damage_type':'radiant',
                    'damage_dice':'1d8',
                    'components':['verbal','somatic'],
                    'casting_time':'action',
                    'spell_level':spell_level,
                    'damage_mod':0,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Sacred_Flame',
                    'school':'evocation',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if self.mage.level >= 5:
            spell_dict['damage_dice'] = '2d8'
        if self.mage.level >= 11:
            spell_dict['damage_dice'] = '3d8'
        if self.mage.level >= 17:
            spell_dict['damage_dice'] = '4d8'
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Sword_Burst(self, spell_level, gen_spell = False, spell_dict = False):
        """Вспышка мечей.

        Level: Cantrip
        Casting time: 1 Action
        Range: 5 feet
        Components: V
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/sword-burst
        """
        if not spell_dict:
            spell_dict = {
                    'effect':'burst',
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_all':True,
                    'savethrow_ability':'dexterity',
                    'attacks_number':1,
                    'radius':5,
                    'attack_range':5,
                    'damage_type':'force',
                    'damage_dice':'1d6',
                    'components':['verbal'],
                    'casting_time':'action',
                    'damage_mod':0,
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Sword_Burst',
                    'school':'conjuration',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if self.mage.level >= 5:
            spell_dict['damage_dice'] = '2d6'
        if self.mage.level >= 11:
            spell_dict['damage_dice'] = '3d6'
        if self.mage.level >= 17:
            spell_dict['damage_dice'] = '4d6'
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Thunderclap(self, spell_level, gen_spell = False, spell_dict = False):
        """Громовая атака барда.

        Level: Cantrip
        Casting time: 1 Action
        Range: 5 feet
        Components: S
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/thunderclap
        """
        if not spell_dict:
            spell_dict = {
                    'effect':'burst',
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_all':True,
                    'savethrow_ability':'constitution',
                    'attacks_number':1,
                    'radius':5,
                    'attack_range':5,
                    'damage_type':'thunder',
                    'damage_dice':'1d6',
                    'components':['somatic'],
                    'casting_time':'action',
                    'damage_mod':0,
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Thunderclap',
                    'school':'evocation',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if self.mage.level >= 5:
            spell_dict['damage_dice'] = '2d6'
        if self.mage.level >= 11:
            spell_dict['damage_dice'] = '3d6'
        if self.mage.level >= 17:
            spell_dict['damage_dice'] = '4d6'
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Word_of_Radiance(self, spell_level, gen_spell = False, spell_dict = False):
        """Слово сияния.

        Level: Cantrip
        Casting time: 1 Action
        Range: 5 feet
        Components: V, M (a holy symbol)
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/word-of-radiance
        """
        if not spell_dict:
            spell_dict = {
                    'effect':'burst',
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_all':True,
                    'savethrow_ability':'constitution',
                    'attacks_number':1,
                    'radius':5,
                    'attack_range':5,
                    'damage_type':'radiant',
                    'damage_dice':'1d6',
                    'components':['verbal','material'],
                    'casting_time':'action',
                    'damage_mod':0,
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Word_of_Radiance',
                    'school':'evocation',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if self.mage.level >= 5:
            spell_dict['damage_dice'] = '2d6'
        if self.mage.level >= 11:
            spell_dict['damage_dice'] = '3d6'
        if self.mage.level >= 17:
            spell_dict['damage_dice'] = '4d6'
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Create_Bonfire(self, spell_level, gen_spell = False, spell_dict = False):
        """Сотворение костра.

        Level: Cantrip
        Casting time: 1 Action
        Range: 60 feet
        Components: V, S
        Duration: Concentration, up to 1 minute
        https://www.dnd-spells.com/spell/create-bonfire
        """
        if not spell_dict:
            spell_dict = {
                    'effect':'bonfire',
                    'effect_timer':10,
                    'concentration':True,
                    'zone_effect':True,
                    'zone_danger':True,
                    'radius':0,
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_all':True,
                    'savethrow_ability':'dexterity',
                    'attacks_number':1,
                    'attack_range':60,
                    'damage_type':'fire',
                    'damage_dice':'1d8',
                    'components':['verbal','somatic'],
                    'casting_time':'action',
                    'damage_mod':0,
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Create_Bonfire',
                    'school':'conjuration',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if self.mage.level >= 5:
            spell_dict['damage_dice'] = '2d8'
        if self.mage.level >= 11:
            spell_dict['damage_dice'] = '3d8'
        if self.mage.level >= 17:
            spell_dict['damage_dice'] = '4d8'
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Lightning_Lure(self, spell_level, gen_spell = False, spell_dict = False):
        """Лассо молний.

        Level: Cantrip
        Casting time: 1 Action
        Range: 15 feet
        Components: V
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/lightning-lure
        """
        if not spell_dict:
            spell_dict = {
                    'debuff':True,
                    'effect':'lightning_lure',
                    'attacks_number':1,
                    'attack_range':15,
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_all':True,
                    'savethrow_ability':'strength',
                    'damage_type':'lightning',
                    'damage_dice':'1d8',
                    'components':['verbal'],
                    'casting_time':'action',
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Lightning_Lure',
                    'school':'evocation',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if gen_spell:
            if not spell_dict.get('target_uuid'):
                soldier = self.mage
            else:
                soldier = self.mage.metadict_soldiers[spell_dict['target_uuid']]
            # Спасбросок силы против притягивания.
            difficult = spell_dict['spell_save_DC']
            ability = spell_dict['savethrow_ability']
            advantage = spell_dict.get('savethrow_advantage', False)
            disadvantage = spell_dict.get('savethrow_disadvantage', False)
            if soldier.get_savethrow(difficult, ability, advantage, disadvantage):
                return False
            else:
                # Врага притягивает на 10 футов
                if soldier.reaction:
                    caster = soldier.metadict_soldiers[spell_dict['caster_uuid']]
                    soldier.move_pool += 10
                    destination = caster.place
                    soldier.battle.move_action(soldier, soldier.squad, destination, free_path = True)
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Green_Flame_Blade(self, spell_level, gen_spell = False, spell_dict = False):
        """Клинок зелёного пламени.

        Level: Cantrip
        Casting time: 1 Action
        Range: 5 feet
        Components: V, M (a weapon)
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/green-flame-blade
        """
        if not spell_dict:
            spell_dict = {
                    'debuff':True,
                    'weapon_attack':True,
                    'effect':'green_flame_blade',
                    'attacks_number':1,
                    'attack_range':5,
                    'direct_hit':True,
                    'damage_type':'fire',
                    'damage_dice':'0d0',
                    'damage_mod':0,
                    'components':['verbal','material'],
                    'casting_time':'action',
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Green_Flame_Blade',
                    'school':'evocation',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if self.mage.level >= 5:
            spell_dict['damage_dice'] = '1d8'
        if self.mage.level >= 11:
            spell_dict['damage_dice'] = '2d8'
        if self.mage.level >= 17:
            spell_dict['damage_dice'] = '3d8'
        if gen_spell:
            if not spell_dict.get('target_uuid'):
                soldier = self.mage
            else:
                soldier = self.mage.metadict_soldiers[spell_dict['target_uuid']]
            soldier.battle.recon_action(soldier, soldier.squad)
            if soldier.near_allies:
                enemy = random.choice(soldier.near_allies)
                enemy_soldier = soldier.battle.metadict_soldiers[enemy.uuid]
                enemy = soldier.battle.get_enemy_tuple(soldier, enemy_soldier)
                mage = soldier.metadict_soldiers[spell_dict['caster_uuid']]
                spell_dict['debuff'] = False
                spell_dict['damage_mod'] = mage.spells_generator.find_spell_attack_mod(
                        proficiency_bonus = False)
                soldier.battle.fireball_action(mage, mage.squad,
                        spell_dict, enemy.place, single_target = enemy)
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Blade_Ward(self, spell_level, gen_spell = False, spell_dict = False):
        """Защита от оружия.

        Level: Cantrip
        Casting time: 1 Action
        Range: Self
        Components: V, S
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/blade-ward
        """
        # TODO: пока что каст бонусным действием.
        if not spell_dict:
            spell_dict = {
                    'buff':True,
                    'effect':'blade_ward',
                    'effect_timer':1,
                    'attack_range':0,
                    'absorb_damage_type':['bludgeoning','slashing','piercing'],
                    'components':['verbal','somatic'],
                    'casting_time':'bonus_action',
                    'spell_level':spell_level,
                    'spell_of_choice':'Blade_Ward',
                    'school':'abjuration',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if gen_spell:
            if not spell_dict.get('target_uuid'):
                soldier = self.mage
            else:
                soldier = self.mage.metadict_soldiers[spell_dict['target_uuid']]
            # Добавляем метку, чтобы убрать сопротивляемости в начале хода:
            # Лучше бы они убирались в самом заклинании, когда таймер отсчитает ход.
            soldier.blade_ward = True
            for el in spell_dict['absorb_damage_type']:
                if el not in soldier.resistance:
                    soldier.resistance.append(el)
        return spell_dict    

    @modify_spell
    @update_spell_dict
    def Mold_Earth(self, spell_level, gen_spell = False, spell_dict = False):
        """Лепка земли.

        Level: Cantrip
        Casting time: 1 Action
        Range: 30 feet
        Components: S
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/mold-earth
        """
        # Создаёт траншею и насыпь, укрытие на 3/4.
        if not spell_dict:
            spell_dict = {
                    'buff':True,
                    'effect':'mold_earth',
                    'attack_range':30,
                    'components':['somatic'],
                    'casting_time':'action',
                    'spell_level':spell_level,
                    'spell_of_choice':'Blade_Ward',
                    'school':'transmutation',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if gen_spell:
            if not spell_dict.get('target_uuid'):
                soldier = self.mage
            else:
                soldier = self.mage.metadict_soldiers[spell_dict['target_uuid']]
        if self.mage.class_features.get('Metamagic_Distant_Spell'):
            spell_dict['attack_range'] *= 2
        return spell_dict    

    @modify_spell
    @update_spell_dict
    def Magic_Stone(self, spell_level, gen_spell = False, spell_dict = False):
        """Волшебный камень.

        Level: Cantrip
        Casting time: 1 Bonus Action
        Range: touch
        Components: V, S
        Duration: 1 minute
        https://www.dnd-spells.com/spell/magic-stone
        """
        # Создаёт 3 волшебных камешка для пращи в инвентаре.
        if not spell_dict:
            spell_dict = {
                    'buff':True,
                    'attacks_number':3,
                    'effect':'magic_stone',
                    'components':['verbal','somatic'],
                    'casting_time':'bonus_action',
                    'spell_level':spell_level,
                    'spell_of_choice':'Mage_Hand',
                    'school':'transmutation',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if gen_spell:
            if not spell_dict.get('target_uuid'):
                soldier = self.mage
            else:
                soldier = self.mage.metadict_soldiers[spell_dict['target_uuid']]
            # Создаёт в инвентаре 3 волшебных камня:
            if 'Magic Stone' in soldier.equipment_weapon.keys():
                soldier.equipment_weapon['Magic Stone'] = spell_dict['attacks_number']
            elif 'Magic Boom-stone' in soldier.equipment_weapon.keys():
                soldier.equipment_weapon['Magic Boom-stone'] = spell_dict['attacks_number']
        return spell_dict    

    @modify_spell
    @update_spell_dict
    def Mage_Hand(self, spell_level, gen_spell = False, spell_dict = False):
        """Волшебная рука.

        Level: Cantrip
        Casting time: 1 Action
        Range: 30 feet
        Components: V, S
        Duration: 1 minute
        https://www.dnd-spells.com/spell/mage-hand

        - Поджигает 10-lb бомбы и доставляет их на 30 футов.
        - Боеприпас берётся из экипировки, подобно гранатам.
        - Данные spell_dict дополняются данными боеприпаса.
        """
        if not spell_dict:
            spell_dict = {
                    'zone':True,
                    'use_bombs':True,
                    'attacks_number':1,
                    'attack_range':30,
                    'components':['verbal','somatic'],
                    'casting_time':'action',
                    'max_weight':10,
                    'damage_mod':0,
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Sword_Burst',
                    'school':'conjuration',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        # Черта Телекинез делает руку невидимой, позволяет кастовать мысленно и удваивает радиус.
        if self.mage.class_features.get('Feat_Telekinetic'):
            spell_dict['attack_range'] = 60
            spell_dict['components'] = []
        if gen_spell:
            if not spell_dict.get('target_uuid'):
                soldier = self.mage
            else:
                soldier = self.mage.metadict_soldiers[spell_dict['target_uuid']]
            # Поиск боеприпасов в экипировке, бомбы массой менее 10 lb.
            metadict_ammo = {}
            for item, number in soldier.equipment_weapon.items():
                item_spell_dict = soldier.metadict_items[item].get('spell_dict')
                if item_spell_dict\
                        and 'zone' in item_spell_dict\
                        and 'damage_dice' in item_spell_dict\
                        and 'ammo' in soldier.metadict_items[item]\
                        and soldier.metadict_items[item].get('weight', 0) <= spell_dict['max_weight']:
                    metadict_ammo[item] = soldier.metadict_items[item]
            # Выбор боеприпаса и обновление словаря заклинания данными боеприпаса:
            if metadict_ammo:
                ammo, ammo_dict = random.choice(list(metadict_ammo.items()))
                spell_dict.update(ammo_dict['spell_dict'])
                attack_dict = copy.deepcopy(spell_dict)
                if soldier.equipment_weapon[ammo] > 0:
                    attack_dict['ammo_type'] = ammo
                    attack_dict['ammo'] = soldier.equipment_weapon[ammo]
                    soldier.use_ammo(attack_dict, soldier.squad.metadict_soldiers)
                    return spell_dict    
                else:
                    return False
            else:
                return False
        return spell_dict

#----
# Subspells

    @modify_spell
    @update_spell_dict
    def Ice_Knife_Piercing(self, spell_level, gen_spell = False, spell_dict = False):
        """Главный поражающий элемент заклинания Ice_Knife."""
        # Субзаклинание от Ice_Knife.
        if not spell_dict:
            spell_dict = {
                    'attacks_number':1,
                    'attack_range':60,
                    'damage_type':'piercing',
                    'damage_dice':'1d10',
                    'components':['somatic','material'],
                    'casting_time':'action',
                    'spell_level':spell_level,
                    'damage_mod':0,
                    'attack_mod':self.find_spell_attack_mod(),
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Ice_Knife_Piercing',
                    'school':'conjuration',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Ice_Storm_Cold(self, spell_level, gen_spell = False, spell_dict = False):
        """Град. Повреждения холодом отдельно.
        
        Для каждой отдельной цели.
        """
        if not spell_dict:
            spell_dict = {
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_ability':'dexterity',
                    'attacks_number':1,
                    'attack_range':0,
                    'damage_type':'cold',
                    'damage_dice':'4d6',
                    'components':[],
                    'casting_time':'free_action',
                    'damage_mod':0,
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Magic_Missile',
                    'school':'evocation',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Empyrean_Bolt(self, spell_level, gen_spell = False, spell_dict = False):
        """Дальная атака Эмпирея.

        Он может выбрать тип урона.
        """
        if not spell_dict:
            spell_dict = {
                    'attacks_number':1,
                    'attack_range':600,
                    'damage_type':'fire',
                    'damage_dice':'7d6',
                    'components':['somatic'],
                    'casting_time':'action',
                    'spell_level':spell_level,
                    'damage_mod':0,
                    'attack_mod':15,
                    'spell_save_DC':23,
                    'spell_of_choice':'Empyrean_Bolt',
                    'school':'evocation',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Protection_Field(self, spell_level, gen_spell = False, spell_dict = False):
        """Защитник изобретателя-артиллериста даёт бонусные хиты союзникам.
        
        Даёт 1d8+мод.инт хозяина бонусных хитов.
        """
        if not spell_dict:
            spell_dict = {
                    'buff':True,
                    'concentration':True,
                    'effect':'protection_field',
                    'effect_timer':1,
                    'zone_effect':True,
                    'zone_self':True,
                    'direct_hit':True,
                    'attack_range':0,
                    'radius':10,
                    'damage_type':'bonus_hitpoints',
                    'healing_dice':'1d8',
                    'healing_mod':5,
                    'components':[],
                    'casting_time':'action',
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Protection_Field',
                    'school':'transmutation',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if gen_spell:
            if not spell_dict.get('target_uuid'):
                soldier = self.mage
            else:
                soldier = self.mage.metadict_soldiers[spell_dict['target_uuid']]
            # Защитнки узнаёт модификатор интеллекта хозяина:
            if hasattr(soldier, 'master_uuid'):
                master = soldier.metadict_soldiers[soldier.master_uuid]
                spell_dict['healing_mod'] = master.mods['intelligence']
            # Защитник передаёт свои бонусные хиты союзникам и себе родимому:
            distance = round(spell_dict['radius'] / soldier.battle.tile_size)
            soldier.battle.recon_action(soldier, soldier.squad, distance)
            for ally in soldier.near_allies:
                bonus_hitpoints = dices.dice_throw_advantage(spell_dict['healing_dice'])\
                        + spell_dict['healing_mod']
                ally_soldier = soldier.metadict_soldiers[ally.uuid]
                if ally_soldier.bonus_hitpoints < bonus_hitpoints:
                    ally_soldier.set_hitpoints(bonus_hitpoints = bonus_hitpoints)
                    ally_soldier.buffs[spell_dict['effect']] = spell_dict
            if soldier.bonus_hitpoints <= 0:
                bonus_hitpoints = dices.dice_throw_advantage(spell_dict['healing_dice'])\
                        + spell_dict['healing_mod']
                soldier.set_hitpoints(bonus_hitpoints = bonus_hitpoints)
                soldier.buffs[spell_dict['effect']] = spell_dict
        return spell_dict

#----
# 1 lvl

    @modify_spell
    @update_spell_dict
    def Healing_Word(self, spell_level, gen_spell = False, spell_dict = False):
        """Лечащее слово.

        Level: 1
        Casting time: 1 Bonus Action
        Range: 60 feet
        Components: V
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/healing-word
        """
        # Дистанция заклинания увеличена до 120 футов.
        if not spell_dict:
            spell_dict = {
                    'direct_hit':True,
                    'attacks_number':1,
                    'attack_range':120,
                    'damage_type':'heal',
                    'healing_dice':'1d4',
                    'healing_mod':self.find_spell_attack_mod(proficiency_bonus = False),
                    'components':['verbal'],
                    'casting_time':'bonus_action',
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Bane',
                    'school':'evocation',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if int(spell_level[0]) > 1:
            dice = int(spell_dict['healing_dice'][0])
            dice += int(spell_level[0]) - 1
            spell_dict['healing_dice'] = str(dice) + spell_dict['healing_dice'][1:]
        if self.mage.class_features.get('Disciple_of_Life'):
            spell_dict['healing_mod'] += 2 + int(spell_level[0])
        if gen_spell:
            if not spell_dict.get('target_uuid'):
                soldier = self.mage
            else:
                soldier = self.mage.metadict_soldiers[spell_dict['target_uuid']]
            if soldier.hitpoints < soldier.hitpoints_max:
                heal = dices.dice_throw_advantage(spell_dict['healing_dice'])\
                        + spell_dict['healing_mod']
                soldier.set_hitpoints(heal = heal)
                soldier.stable = True
            else:
                return False
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Cure_Wounds(self, spell_level, gen_spell = False, spell_dict = False):
        """Лечение ран.

        Level: 1
        Casting time: 1 Action
        Range: Touch
        Components: V, S
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/cure-wounds
        """
        if not spell_dict:
            spell_dict = {
                    'direct_hit':True,
                    'attacks_number':1,
                    'attack_range':5,
                    'damage_type':'heal',
                    'healing_dice':'1d8',
                    'healing_mod':self.find_spell_attack_mod(proficiency_bonus = False),
                    'components':['verbal','somatic'],
                    'casting_time':'action',
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Bane',
                    'school':'evocation',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if int(spell_level[0]) > 1:
            dice = int(spell_dict['healing_dice'][0])
            dice += int(spell_level[0]) - 1
            spell_dict['healing_dice'] = str(dice) + spell_dict['healing_dice'][1:]
        if self.mage.class_features.get('Disciple_of_Life'):
            spell_dict['healing_mod'] += 2 + int(spell_level[0])
        if gen_spell:
            if not spell_dict.get('target_uuid'):
                soldier = self.mage
            else:
                soldier = self.mage.metadict_soldiers[spell_dict['target_uuid']]
            if soldier.hitpoints < soldier.hitpoints_max:
                heal = dices.dice_throw_advantage(spell_dict['healing_dice'])\
                        + spell_dict['healing_mod']
                soldier.set_hitpoints(heal = heal)
                soldier.stable = True
            else:
                return False
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Goodberry(self, spell_level, gen_spell = False, spell_dict = False):
        """Чудо-ягода, добряника.

        Level: 1
        Casting time: 1 Action
        Range: Touch
        Components: V, S, M (a sprig of mistletoe)
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/goodberry
        """
        # Этим заклинанием мы создаём 10 ягод добряники в инвентаре.
        # А передав use_goodberry (используя предмет Goodberry) съедаем одну из них.
        if not spell_dict:
            spell_dict = {
                    'direct_hit':True,
                    'use_goodberry':False,
                    'create_goodberry':True,
                    'attacks_number':10,
                    'damage_type':'heal',
                    'healing_mod':1,
                    'components':['verbal','somatic','material'],
                    'casting_time':'action',
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Bane',
                    'school':'transmutation',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        # В "Ответах мудреца" сказано, что Disciple_of_Life усиливает эффект добряники.
        if self.mage.class_features.get('Disciple_of_Life'):
            spell_dict['healing_mod'] += 2 + int(spell_level[0])
        if gen_spell:
            if not spell_dict.get('target_uuid'):
                soldier = self.mage
            else:
                soldier = self.mage.metadict_soldiers[spell_dict['target_uuid']]
            if spell_dict.get('create_goodberry'):
                if not 'Goodberry' in soldier.equipment_weapon:
                    soldier.equipment_weapon['Goodberry'] = spell_dict['attacks_number']
                else:
                    soldier.equipment_weapon['Goodberry'] += spell_dict['attacks_number']
            elif spell_dict.get('use_goodberry'):
                if soldier.hitpoints < soldier.hitpoints_max:
                    heal = spell_dict['healing_mod']
                    soldier.set_hitpoints(heal = heal)
                    soldier.stable = True
                else:
                    return False
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Bless(self, spell_level, gen_spell = False, spell_dict = False):
        """Благословление.

        Level: 1
        Casting time: 1 Action
        Range: 30 feet
        Components: V, S, M (a sprinkling of holy water)
        Duration: Concentration, up to 1 minute
        https://www.dnd-spells.com/spell/bless
        """
        if not spell_dict:
            spell_dict = {
                    'buff':True,
                    'concentration':True,
                    'effect':'bless',
                    'effect_timer':10,
                    'direct_hit':True,
                    'attacks_number':3,
                    'attack_range':30,
                    'damage_dice':'1d4',
                    'components':['verbal','somatic','material'],
                    'casting_time':'action',
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Bane',
                    'school':'enchantment',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if int(spell_level[0]) > 1:
            spell_dict['attacks_number'] += int(spell_level[0]) - 1
        if gen_spell:
            if not spell_dict.get('target_uuid'):
                soldier = self.mage
            else:
                soldier = self.mage.metadict_soldiers[spell_dict['target_uuid']]
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Shield_of_Faith(self, spell_level, gen_spell = False, spell_dict = False):
        """Щит веры.

        Level: 1
        Casting time: 1 Bonus Action
        Range: 60 feet
        Components: V, S, M (a small parchment with a bit of holy text written on it)
        Duration: Concentration, up to 10 minutes
        https://www.dnd-spells.com/spell/shield-of-faith
        """
        if not spell_dict:
            spell_dict = {
                    'buff':True,
                    'concentration':True,
                    'effect':'shield_of_faith',
                    'effect_timer':100,
                    'attacks_number':1,
                    'attack_range':60,
                    'damage_type':'shield',
                    'healing_mod':2,
                    'components':['verbal','somatic','material'],
                    'casting_time':'bonus_action',
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Bane',
                    'school':'abjuration',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if gen_spell:
            if not spell_dict.get('target_uuid'):
                soldier = self.mage
            else:
                soldier = self.mage.metadict_soldiers[spell_dict['target_uuid']]
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Longstrider(self, spell_level, gen_spell = False, spell_dict = False):
        """Скороход

        Level: 1
        Casting time: 1 Action
        Range: Touch
        Components: V, S, M (a pinch of dirt)
        Duration: 1 hour
        https://www.dnd-spells.com/spell/longstrider
        """
        if not spell_dict:
            spell_dict = {
                    'buff':True,
                    'effect':'longstrider',
                    'effect_timer':600,
                    'attacks_number':1,
                    'attack_range':5,
                    'components':['verbal','somatic','material'],
                    'casting_time':'action',
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Bane',
                    'school':'transmutation',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if int(spell_level[0]) > 1:
            spell_dict['attacks_number'] *= int(spell_level[0])
        if gen_spell:
            if not spell_dict.get('target_uuid'):
                soldier = self.mage
            else:
                soldier = self.mage.metadict_soldiers[spell_dict['target_uuid']]
            if not 'longstrider' in soldier.buffs:
                soldier.base_speed += 10
            else:
                return False
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Heroism(self, spell_level, gen_spell = False, spell_dict = False):
        """Героизм.


        Level: 1
        Casting time: 1 Action
        Range: Touch
        Components: V, S
        Duration: Concentration, up to 1 minute
        https://www.dnd-spells.com/spell/heroism
        """
        if not spell_dict:
            spell_dict = {
                    'buff':True,
                    'repeat':True,
                    'concentration':True,
                    'effect':'heroism',
                    'effect_timer':10,
                    'attacks_number':1,
                    'attack_range':5,
                    'damage_type':'bonus_hitpoints',
                    'damage_dice':'0d0',
                    'damage_mod':self.find_spell_attack_mod(proficiency_bonus = False),
                    'components':['verbal','somatic'],
                    'casting_time':'action',
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Bane',
                    'school':'enchantment',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if int(spell_level[0]) > 1:
            spell_dict['attacks_number'] *= int(spell_level[0])
        if gen_spell:
            if not spell_dict.get('target_uuid'):
                soldier = self.mage
            else:
                soldier = self.mage.metadict_soldiers[spell_dict['target_uuid']]
            if soldier.bonus_hitpoints < spell_dict['damage_mod']:
                soldier.set_hitpoints(bonus_hitpoints = spell_dict['damage_mod'])
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Fog_Cloud(self, spell_level, gen_spell = False, spell_dict = False):
        """Туманное облако.

        Level: 1
        Casting time: 1 Action
        Range: 120 feet
        Components: V, S
        Duration: Concentration, up to 1 hour
        https://www.dnd-spells.com/spell/fog-cloud
        """
        if not spell_dict:
            spell_dict = {
                    'concentration':True,
                    'effect':'fog',
                    'effect_timer':100,
                    'attacks_number':1,
                    'radius':20,
                    'attack_range':120,
                    'components':['verbal','somatic'],
                    'casting_time':'action',
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Cause_Fear',
                    'school':'conjuration',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        # Радиус облака растёт на 20 футов за каждый уровень выше первого:
        if int(spell_level[0]) > 1:
            spell_dict['radius'] += 20 * int(spell_level[0])
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Cause_Fear(self, spell_level, gen_spell = False, spell_dict = False):
        """Вызвать страх.

        Level: 1
        Casting time: 1 Action
        Range: 60 feet
        Components: V
        Duration: Concentration, up to 1 minute
        https://www.dnd-spells.com/spell/cause-fear
        """
        if not spell_dict:
            spell_dict = {
                    'concentration':True,
                    'attacks_number':1,
                    'attack_range':60,
                    'effect':'fear',
                    'effect_timer':10,
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_all':True,
                    'savethrow_ability':'wisdom',
                    'components':['verbal'],
                    'casting_time':'action',
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Cause_Fear',
                    'school':'necromancy',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if int(spell_level[0]) > 1:
            spell_dict['attacks_number'] = int(spell_level[0])
        if gen_spell:
            if not spell_dict.get('target_uuid'):
                soldier = self.mage
            else:
                soldier = self.mage.metadict_soldiers[spell_dict['target_uuid']]
            # Спасбросок мудрости против очарования:
            difficult = spell_dict['spell_save_DC']
            ability = spell_dict['savethrow_ability']
            advantage = spell_dict.get('savethrow_advantage', False)
            disadvantage = spell_dict.get('savethrow_disadvantage', False)
            if soldier.get_savethrow(difficult, ability, advantage, disadvantage):
                return False
            else:
                soldier.fear_difficult = difficult
                soldier.fear_source = self.mage
                soldier.fear = True
                #if soldier.reaction:
                #    # Солдат убегает за счёт реакции:
                #    soldier.reaction = False
                #    soldier.move_pool = soldier.base_speed
                #    destination = soldier.battle.find_spawn(soldier.place, soldier.ally_side)
                #    destination = random.choice(soldier.battle.point_to_field(destination))
                #    soldier.battle.move_action(soldier, soldier.squad, destination, allow_replace = True)
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Hex(self, spell_level, gen_spell = False, spell_dict = False):
        """Сглаз.

        Level: 1
        Casting time: 1 Bonus Action
        Range: 90 feet
        Components: V, S, M (the petrified eye of a newt)
        Duration: Concentration, up to 1 hour
        https://www.dnd-spells.com/spell/hex
        """
        if not spell_dict:
            spell_dict = {
                    'concentration':True,
                    'effect_timer':600,
                    'attacks_number':1,
                    'attack_range':90,
                    'effect':'hex',
                    'direct_hit':True,
                    'damage_type':'necrotic_energy',
                    'damage_dice':'1d6',
                    'components':['verbal','somatic','material'],
                    'casting_time':'bonus_action',
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Magic_Missile',
                    'school':'enchantment',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Sleep(self, spell_level, gen_spell = False, spell_dict = False):
        """Усыпление.

        Level: 1
        Casting time: 1 Action
        Range: 90 feet
        Components: V, S, M (a pinch of fine sand, rose petals, or a cricket)
        Duration: 1 minute
        https://www.dnd-spells.com/spell/sleep
        """
        if not spell_dict:
            spell_dict = {
                    'debuff':True,
                    'effect':'sleep',
                    'effect_timer':100,
                    'attacks_number':1,
                    'attack_range':90,
                    'radius':20,
                    'damage_type':'sleep',
                    'damage_dice':'5d8',
                    'components':['verbal','somatic','material'],
                    'casting_time':'action',
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Sleep',
                    'school':'enchantment',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        # Плюс одна кость усыпления за каждый уровень выше первого:
        if int(spell_level[0]) > 1:
            dice = int(spell_dict['damage_dice'][0])
            dice += int(spell_level[0]) - 1
            spell_dict['damage_dice'] = str(dice) + spell_dict['damage_dice'][1:]
        if self.mage.class_features.get('Metamagic_Distant_Spell'):
            spell_dict['attack_range'] *= 2
        if gen_spell:
            if not spell_dict.get('target_uuid'):
                soldier = self.mage
            else:
                soldier = self.mage.metadict_soldiers[spell_dict['target_uuid']]
            if not 'sleep' in soldier.debuffs:
                caster = soldier.metadict_soldiers[spell_dict['caster_uuid']]
                sleep_pool = dices.dice_throw_advantage(spell_dict['damage_dice'])
                # Перебираем цели, пока есть хоть кто-то с хитами меньшими, чем sleep_pool:
                while sleep_pool > 0:
                    if 'sleep' in soldier.debuffs or soldier.hitpoints > sleep_pool:
                        soldier = caster.battle.find_target_for_debuff(caster, soldier, 'sleep')
                        if not soldier:
                            break
                    sleep_pool -= soldier.hitpoints
                    if sleep_pool > 0:
                        soldier.debuffs[spell_dict['effect']] = spell_dict
                        fall_place = soldier.place
                        soldier.battle.dict_battlespace[fall_place].append('fall_place')
                        soldier.battle.dict_battlespace[fall_place].append(soldier.ally_side)
            else:
                return False
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Entangle(self, spell_level, gen_spell = False, spell_dict = False):
        """Опутывание.

        Level: 1
        Casting time: 1 Action
        Range: 90 feet
        Components: V, S
        Duration: Concentration, up to 1 minute
        https://www.dnd-spells.com/spell/entangle
        """
        # TODO: Чертовски неудобно использовать как зональное заклинание.
        # Пусть лучше будет 10 целей, эффект опутывания и растущие кусты.
        if not spell_dict:
            spell_dict = {
                    'concentration':True,
                    'effect':'entangle',
                    'effect_timer':10,
                    #'zone':True,
                    #'zone_shape':'square',
                    #'radius':10,
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_all':True,
                    'savethrow_ability':'strength',
                    'attacks_number':10,
                    'attack_range':90,
                    'components':['verbal','somatic'],
                    'casting_time':'action',
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Entangle',
                    'school':'conjuration',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Magic_Missile(self, spell_level, gen_spell = False, spell_dict = False):
        """Волшебная стрела.

        Level: 1
        Casting time: 1 Action
        Range: 120 feet
        Components: V,S
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/magic-missile
        """
        if not spell_dict:
            spell_dict = {
                    'direct_hit':True,
                    'attacks_number':3,
                    'attack_range':120,
                    'damage_type':'force',
                    'damage_dice':'1d4',
                    'components':['verbal','somatic'],
                    'casting_time':'action',
                    'spell_level':spell_level,
                    'damage_mod':+1,
                    'spell_of_choice':'Magic_Missile',
                    'school':'evocation',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        # За каждый уровень сверх первого один дополнительный дротик:
        if int(spell_level[0]) > 1:
            spell_dict['attacks_number'] += int(spell_level[0]) - 1
        if self.mage.class_features.get('Metamagic_Distant_Spell'):
            spell_dict['attack_range'] *= 2
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Guiding_Bolt(self, spell_level, gen_spell = False, spell_dict = False):
        """Направленный снаряд.

        Level: 1
        Casting time: 1 Action
        Range: 120 feet
        Components: V, S
        Duration: 1 round
        https://www.dnd-spells.com/spell/guiding-bolt
        """
        if not spell_dict:
            spell_dict = {
                    'debuff':True,
                    'effect':'guiding_bolt',
                    'effect_timer':2,
                    'attacks_number':1,
                    'attack_range':120,
                    'damage_type':'radiant',
                    'damage_dice':'4d6',
                    'components':['verbal','somatic'],
                    'casting_time':'action',
                    'spell_level':spell_level,
                    'damage_mod':0,
                    'attack_mod':self.find_spell_attack_mod(),
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Guiding_Bolt',
                    'school':'evocation',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if int(spell_level[0]) > 1:
            dice = int(spell_dict['damage_dice'][0])
            dice += int(spell_level[0]) - 1
            spell_dict['damage_dice'] = str(dice) + spell_dict['damage_dice'][1:]
        if self.mage.class_features.get('Metamagic_Distant_Spell'):
            spell_dict['attack_range'] *= 2
        if gen_spell:
            if not spell_dict.get('target_uuid'):
                soldier = self.mage
            else:
                soldier = self.mage.metadict_soldiers[spell_dict['target_uuid']]
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Burning_Hands(self, spell_level, gen_spell = False, spell_dict = False):
        """Огненные ладони.

        Level: 1
        Casting time: 1 Action
        Range: Self (15-foot cone)
        Components: V, S
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/burning-hands
        """
        if not spell_dict:
            spell_dict = {
                    'zone':True,
                    'zone_shape':'cone',
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_ability':'dexterity',
                    'attacks_number':1,
                    'attack_range':15,
                    'damage_type':'fire',
                    'damage_dice':'3d6',
                    'components':['verbal','somatic'],
                    'casting_time':'action',
                    'damage_mod':0,
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Magic_Missile',
                    'school':'evocation',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if int(spell_level[0]) > 1:
            dice = int(spell_dict['damage_dice'][0])
            dice += int(spell_level[0]) - 1
            spell_dict['damage_dice'] = str(dice) + spell_dict['damage_dice'][1:]
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Shield(self, spell_level, gen_spell = False, spell_dict = False):
        """Щит.

        Level: 1
        Casting time: Special
        Range: Self
        Components: V, S
        Duration: 1 round
        https://www.dnd-spells.com/spell/shield
        """
        if not spell_dict:
            spell_dict = {
                    'buff':True,
                    'effect':'shield',
                    'effect_timer':1,
                    'attack_range':0,
                    'damage_type':'shield',
                    'healing_mod':5,
                    'components':['verbal','somatic'],
                    'casting_time':'reaction',
                    'spell_level':spell_level,
                    'spell_of_choice':'Magic_Missile',
                    'school':'abjuration',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Absorb_Elements(self, spell_level, gen_spell = False, spell_dict = False):
        """Поглощение стихий.

        Level: 1
        Casting time: Special
        Range: Self
        Components: S
        Duration: 1 round
        https://www.dnd-spells.com/spell/absorb-elements
        """
        # 1d6 урона поглощённого типа можно направить атакой оружием в следующем раунде.
        # TODO: передавать в gen_spell словарь, где в damage_type указан урон. Затем spell_dict.update
        # Будет сделано через декоратор update_spell_dict
        if not spell_dict:
            spell_dict = {
                    'buff':True,
                    'effect':'absorb_elements',
                    'direct_hit':True,
                    'effect_timer':1,
                    'attack_range':0,
                    'absorb_damage_type':['acid','cold','fire','lightning','thunder'],
                    #'damage_type':'absorbed',
                    'damage_dice':'1d6',
                    'components':['somatic'],
                    'casting_time':'reaction',
                    'damage_mod':0,
                    'spell_level':spell_level,
                    'spell_of_choice':'Magic_Missile',
                    'school':'abjuration',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if int(spell_level[0]) > 1:
            dice = int(spell_dict['damage_dice'][0])
            dice += int(spell_level[0]) - 1
            spell_dict['damage_dice'] = str(dice) + spell_dict['damage_dice'][1:]
        if gen_spell:
            if not spell_dict.get('target_uuid'):
                soldier = self.mage
            else:
                soldier = self.mage.metadict_soldiers[spell_dict['target_uuid']]
            # Параметр 'damage_type' должен быть передан заклинанию с помощью update_spell_dict:
            if spell_dict['damage_type'] in spell_dict['absorb_damage_type']:
                soldier.resistance.append(spell_dict['damage_type'])
            else:
                return False
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Mage_Armor(self, spell_level, gen_spell = False, spell_dict = False):
        """Доспехи мага.

        Level: 1
        Casting time: 1 Action
        Range: Touch
        Components: V, S, M
        Duration: 8 hours
        https://www.dnd-spells.com/spell/mage-armor
        """
        # TODO: броня берётся из metadict_item.
        if not spell_dict:
            spell_dict = {
                    'buff':True,
                    'effect':'mage_armor',
                    'effect_timer':4800,
                    'attacks_number':1,
                    'armor':True,
                    'armor_type':'Mage_Armor',
                    'armor_class_armor':13,
                    'attack_range':0,
                    'components':['verbal','somatic','material'],
                    'casting_time':'action',
                    'spell_level':spell_level,
                    'spell_of_choice':'Magic_Missile',
                    'school':'abjuration',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if gen_spell:
            if not spell_dict.get('target_uuid'):
                soldier = self.mage
            else:
                soldier = self.mage.metadict_soldiers[spell_dict['target_uuid']]
            soldier.equipment_weapon['Mage_Armor'] = 1
            soldier.armor.update(soldier.get_armor())
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Armor_of_Agathys(self, spell_level, gen_spell = False, spell_dict = False):
        """Доспех Агатиса.


        Level: 1
        Casting time: 1 Action
        Range: Self
        Components: V, S, M (a cup of water)
        Duration: 1 hour
        https://www.dnd-spells.com/spell/armor-of-agathys
        """
        if not spell_dict:
            spell_dict = {
                    'buff':True,
                    'effect':'armor_of_agathys',
                    'effect_timer':600,
                    'direct_hit':True,
                    'attack_range':10,
                    'damage_type':'cold',
                    'damage_dice':'0d0',
                    'damage_mod':5,
                    'components':['verbal','somatic','material'],
                    'casting_time':'action',
                    'spell_level':spell_level,
                    'spell_of_choice':'Magic_Missile',
                    'school':'abjuration',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if int(spell_level[0]) > 1:
            spell_dict['damage_mod'] *= int(spell_level[0])
        if gen_spell:
            if not spell_dict.get('target_uuid'):
                soldier = self.mage
            else:
                soldier = self.mage.metadict_soldiers[spell_dict['target_uuid']]
            soldier.bonus_hitpoints = spell_dict['damage_mod']
        return spell_dict

    @modify_spell
    @update_spell_dict
    def False_Life(self, spell_level, gen_spell = False, spell_dict = False):
        """Псевдожизнь.

        Level: 1
        Casting time: 1 Action
        Range: Self
        Components: V, S, M (a small amount of alcohol or distilled spirits)
        Duration: 1 hour
        https://www.dnd-spells.com/spell/false-life
        """
        if not spell_dict:
            spell_dict = {
                    'buff':True,
                    'effect':'bonus_hitpoints',
                    'effect_timer':600,
                    'healing_dice':'1d4',
                    'healing_mod':4,
                    'components':['verbal','somatic','material'],
                    'casting_time':'action',
                    'spell_level':spell_level,
                    'spell_of_choice':'Magic_Missile',
                    'school':'necromancy',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if int(spell_level[0]) > 1:
            spell_dict['healing_mod'] = spell_dict['healing_mod'] * int(spell_level[0])
        if gen_spell:
            if not spell_dict.get('target_uuid'):
                soldier = self.mage
            else:
                soldier = self.mage.metadict_soldiers[spell_dict['target_uuid']]
            bonus_hitpoints = dices.dice_throw_advantage(spell_dict['healing_dice'])\
                    + spell_dict['healing_mod']
            soldier.set_hitpoints(bonus_hitpoints = bonus_hitpoints)
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Ice_Knife(self, spell_level, gen_spell = False, spell_dict = False):
        """Ледяной кинжал.

        Level: 1
        Casting time: 1 Action
        Range: 60 feet
        Components: S, M
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/ice-knife
        """
        if not spell_dict:
            spell_dict = {
                    'effect':'ice_knife',
                    'subspell':'Ice_Knife_Piercing',
                    'zone':True,
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_all':True,
                    'savethrow_ability':'dexterity',
                    'attacks_number':1,
                    'attack_range':60,
                    'radius':5,
                    'damage_type':'cold',
                    'damage_dice':'2d6',
                    'components':['somatic','material'],
                    'casting_time':'action',
                    'damage_mod':0,
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Magic_Missile',
                    'school':'conjuration',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if int(spell_level[0]) > 1:
            dice = int(spell_dict['damage_dice'][0])
            dice += int(spell_level[0]) - 1
            spell_dict['damage_dice'] = str(dice) + spell_dict['damage_dice'][1:]
        if self.mage.class_features.get('Metamagic_Distant_Spell'):
            spell_dict['attack_range'] *= 2
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Hail_of_Thorns(self, spell_level, gen_spell = False, spell_dict = False):
        """Град шипов.

        Level: 1
        Casting time: 1 Bonus Action
        Range: Self
        Components: V
        Duration: Concentration, up to 1 minute
        https://www.dnd-spells.com/spell/hail-of-thorns
        """
        if not spell_dict:
            spell_dict = {
                    'ammo':1,
                    'concentration':True,
                    'concentration_ready':True,
                    'effect':'thorns',
                    'effect_timer':10,
                    'zone':True,
                    'zone_shape':'square',
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_ability':'dexterity',
                    'attacks_number':1,
                    'attack_range':600,
                    'radius':5,
                    'damage_type':'piercing',
                    'damage_dice':'1d10',
                    'components':['verbal'],
                    'casting_time':'bonus_action',
                    'damage_mod':0,
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Magic_Missile',
                    'school':'conjuration',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if int(spell_level[0]) > 1:
            dice = int(spell_dict['damage_dice'][0])
            dice += int(spell_level[0]) - 1
            spell_dict['damage_dice'] = str(dice) + spell_dict['damage_dice'][1:]
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Arms_of_Hadar(self, spell_level, gen_spell = False, spell_dict = False):
        """Руки хадара.

        Level: 1
        Casting time: 1 Action
        Range: Self (10-foot radius)
        Components: V, S
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/arms-of-hadar
        """
        # TODO: сделай сбивание реакции.
        if not spell_dict:
            spell_dict = {
                    'effect':'burst',
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_ability':'strength',
                    'attacks_number':1,
                    'radius':10,
                    'attack_range':5,
                    'damage_type':'necrotic_energy',
                    'damage_dice':'2d6',
                    'components':['verbal', 'somatic'],
                    'casting_time':'action',
                    'damage_mod':0,
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Arms_of_Hadar',
                    'school':'conjuration',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if int(spell_level[0]) > 1:
            dice = int(spell_dict['damage_dice'][0])
            dice += int(spell_level[0]) - 1
            spell_dict['damage_dice'] = str(dice) + spell_dict['damage_dice'][1:]
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Thunderwave(self, spell_level, gen_spell = False, spell_dict = False):
        """Волна грома.

        Level: 1
        Casting time: 1 Action
        Range: Self (15-foot cube)
        Components: V, S
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/thunderwave
        """
        # TODO: сделай отталкивание
        if not spell_dict:
            spell_dict = {
                    'effect':'burst',
                    'direct_hit':True,
                    'savethrow':True,
                    'zone_shape':'square',
                    'savethrow_ability':'constitution',
                    'attacks_number':1,
                    'radius':5,
                    'attack_range':5,
                    'damage_type':'thunder',
                    'damage_dice':'2d8',
                    'components':['verbal', 'somatic'],
                    'casting_time':'action',
                    'damage_mod':0,
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Thunderwave',
                    'school':'evocation',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if int(spell_level[0]) > 1:
            dice = int(spell_dict['damage_dice'][0])
            dice += int(spell_level[0]) - 1
            spell_dict['damage_dice'] = str(dice) + spell_dict['damage_dice'][1:]
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Dissonant_Whispers(self, spell_level, gen_spell = False, spell_dict = False):
        """Диссонирующий щёпот.

        Level: 1
        Casting time: 1 Action
        Range: 60 feet
        Components: V
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/dissonant-whispers
        """
        if not spell_dict:
            spell_dict = {
                    'debuff':True,
                    'effect':'dissonant_whispers',
                    'attacks_number':1,
                    'attack_range':60,
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_all':True,
                    'savethrow_ability':'wisdom',
                    'damage_type':'psychic',
                    'damage_dice':'3d6',
                    'components':['verbal'],
                    'casting_time':'action',
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Dissonant_Whispers',
                    'school':'enchantment',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if gen_spell:
            if not spell_dict.get('target_uuid'):
                soldier = self.mage
            else:
                soldier = self.mage.metadict_soldiers[spell_dict['target_uuid']]
            # Спасбросок мудрости против очарования:
            difficult = spell_dict['spell_save_DC']
            ability = spell_dict['savethrow_ability']
            advantage = spell_dict.get('savethrow_advantage', False)
            disadvantage = spell_dict.get('savethrow_disadvantage', False)
            if soldier.get_savethrow(difficult, ability, advantage, disadvantage):
                return False
            else:
                if soldier.reaction:
                    # Солдат убегает за счёт реакции:
                    soldier.reaction = False
                    soldier.move_pool = soldier.base_speed
                    destination = soldier.battle.find_spawn(soldier.place, soldier.ally_side)
                    destination = random.choice(soldier.battle.point_to_field(destination))
                    soldier.battle.move_action(soldier, soldier.squad, destination, allow_replace = True)
        return spell_dict

#----
# 2 lvl

    @modify_spell
    @update_spell_dict
    def Flaming_Sphere(self, spell_level, gen_spell = False, spell_dict = False):
        """Пылающий шар.

        Level: 2
        Casting time: 1 Action
        Range: 60 feet
        Components: V, S, M (a bit of tallow, a pinch of brimstone, and a dusting of powdered iron)
        Duration: Concentration, up to 1 minute
        https://www.dnd-spells.com/spell/flaming-sphere
        """
        if not spell_dict:
            spell_dict = {
                    'concentration':True,
                    'effect':'flaming_sphere',
                    'effect_timer':10,
                    'zone':True,
                    'zone_target':True,
                    'zone_effect':True,
                    'zone_danger':True,
                    'zone_shape':'square',
                    'radius':5,
                    'attacks_number':1,
                    'attack_range':60,
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_ability':'dexterity',
                    'damage_type':'fire',
                    'damage_dice':'2d6',
                    'components':['verbal','somatic','material'],
                    'casting_time':'bonus_action',
                    'spell_level':spell_level,
                    'damage_mod':0,
                    'attack_mod':self.find_spell_attack_mod(),
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Scorching_Ray',
                    'school':'conjuration',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if int(spell_level[0]) > 2:
            dice = int(spell_dict['damage_dice'][0])
            dice += int(spell_level[0]) - 1
            spell_dict['damage_dice'] = str(dice) + spell_dict['damage_dice'][1:]
        if self.mage.class_features.get('Metamagic_Distant_Spell'):
            spell_dict['attack_range'] *= 2
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Scorching_Ray(self, spell_level, gen_spell = False, spell_dict = False):
        """Палящий луч.

        Level: 2
        Casting time: 1 Action
        Range: 120 feet
        Components: V, S
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/scorching-ray
        """
        if not spell_dict:
            spell_dict = {
                    #'direct_hit':True,
                    'attacks_number':3,
                    'attack_range':120,
                    'damage_type':'fire',
                    'damage_dice':'2d6',
                    'components':['verbal','somatic'],
                    'casting_time':'action',
                    'spell_level':spell_level,
                    'damage_mod':0,
                    'attack_mod':self.find_spell_attack_mod(),
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Scorching_Ray',
                    'school':'evocation',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        # За каждый уровень сверх первого один дополнительный луч:
        if int(spell_level[0]) > 1:
            spell_dict['attacks_number'] += int(spell_level[0]) - 1
        if self.mage.class_features.get('Metamagic_Distant_Spell'):
            spell_dict['attack_range'] *= 2
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Melfs_Acid_Arrow(self, spell_level, gen_spell = False, spell_dict = False):
        """Кислотная стрела Мельфа.

        Level: 2
        Casting time: 1 Action
        Range: 90 feet
        Components: V, S, M (powdered rhubarb leaf and an adder’s stomach)
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/melfs-acid-arrow
        """
        # TODO: 2d4 урона в следующий раунд.
        # TODO: сделай homebrew: коррозия неволшебных доспехов, щитов и оружия на -1
        if not spell_dict:
            spell_dict = {
                    'effect':'acid_arrow',
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_ability':'dexterity',
                    'attacks_number':1,
                    'attack_range':120,
                    'damage_type':'acid',
                    'damage_dice':'6d4',
                    'components':['verbal','somatic','material'],
                    'casting_time':'action',
                    'spell_level':spell_level,
                    'damage_mod':0,
                    'attack_mod':self.find_spell_attack_mod(),
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Melfs_Acid_Arrow',
                    'school':'evocation',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if int(spell_level[0]) > 2:
            dice = int(spell_dict['damage_dice'][0])
            dice += int(spell_level[0]) * 2 - 1
            spell_dict['damage_dice'] = str(dice) + spell_dict['damage_dice'][1:]
        if self.mage.class_features.get('Metamagic_Distant_Spell'):
            spell_dict['attack_range'] *= 2
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Moonbeam(self, spell_level, gen_spell = False, spell_dict = False):
        """Лунный луч.

        Level: 2
        Casting time: 1 Action
        Range: 120 feet
        Components: V, S, M (several seeds of any moonseed plant and a piece of opalescent feldspar)
        https://www.dnd-spells.com/spell/moonbeam
        """
        if not spell_dict:
            spell_dict = {
                    'concentration':True,
                    'effect':'moonbeam',
                    'effect_timer':10,
                    'zone':True,
                    'zone_shape':'2x2',
                    'zone_effect':True,
                    'zone_danger':True,
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_ability':'dexterity',
                    'attacks_number':1,
                    'attack_range':120,
                    'radius':5,
                    'damage_type':'radiant',
                    'damage_dice':'2d10',
                    'components':['verbal','somatic','material'],
                    'casting_time':'action',
                    'damage_mod':0,
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Magic_Missile',
                    'school':'evocation',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if int(spell_level[0]) > 2:
            dice = int(spell_dict['damage_dice'][0])
            dice += int(spell_level[0]) - 1
            spell_dict['damage_dice'] = str(dice) + spell_dict['damage_dice'][1:]
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Blur(self, spell_level, gen_spell = False, spell_dict = False):
        """Размытый образ.

        Level: 2
        Casting time: 1 Action
        Range: Self
        Components: V
        Duration: Concentration, up to 1 minute
        https://www.dnd-spells.com/spell/blur
        """
        if not spell_dict:
            spell_dict = {
                    'buff':True,
                    'concentration':True,
                    'effect':'blur',
                    'effect_timer':10,
                    'attack_range':0,
                    'components':['verbal'],
                    'casting_time':'action',
                    'spell_level':spell_level,
                    'spell_of_choice':'Magic_Missile',
                    'school':'illusion',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Mirror_Image(self, spell_level, gen_spell = False, spell_dict = False):
        """Отражения.

        Level: 2
        Casting time: 1 Action
        Range: Self
        Components: V, S
        Duration: 1 minute
        https://www.dnd-spells.com/spell/mirror-image
        """
        if not spell_dict:
            spell_dict = {
                    'buff':True,
                    'effect':'mirror_image',
                    'effect_timer':10,
                    'attack_range':0,
                    'components':['verbal','somatic'],
                    'casting_time':'action',
                    'spell_level':spell_level,
                    'spell_of_choice':'Magic_Missile',
                    'school':'illusion',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if gen_spell:
            if not spell_dict.get('target_uuid'):
                soldier = self.mage
            else:
                soldier = self.mage.metadict_soldiers[spell_dict['target_uuid']]
            # Создаются три иллюзорные копии:
            spell_dict['images'] = {}
            from soldier_fight import soldier_in_battle
            for n in range (0,3):
                image = soldier_in_battle()
                image.create_soldier('Mirror_Image (CR 0)')
                image.armor = copy.deepcopy(soldier.armor)
                image.set_actions_base(squad = None)
                image.set_ally_side(soldier.ally_side)
                image.set_enemy_side(soldier.enemy_side)
                image.set_coordinates(soldier.place)
                soldier.metadict_soldiers[image.uuid] = image
                spell_dict['images'][image.uuid] = image
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Shatter(self, spell_level, gen_spell = False, spell_dict = False):
        """Дребезги.

        Level: 2
        Casting time: 1 Action
        Range: 60 feet
        Components: V, S, M (a chip of mica)
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/shatter
        """
        if not spell_dict:
            spell_dict = {
                    'zone':True,
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_ability':'constitution',
                    'attacks_number':1,
                    'attack_range':60,
                    'radius':10,
                    'damage_type':'thunder',
                    'damage_dice':'3d8',
                    'components':['verbal','somatic','material'],
                    'casting_time':'action',
                    'damage_mod':0,
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Magic_Missile',
                    'school':'evocation',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if int(spell_level[0]) > 2:
            dice = int(spell_dict['damage_dice'][0])
            dice += int(spell_level[0]) - 1
            spell_dict['damage_dice'] = str(dice) + spell_dict['damage_dice'][1:]
        if self.mage.class_features.get('Metamagic_Distant_Spell'):
            spell_dict['attack_range'] *= 2
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Darkness(self, spell_level, gen_spell = False, spell_dict = False):
        """Темнота.
        
        Вокруг предмета, или вокруг точки.

        Level: 2
        Casting time: 1 Action
        Range: 60 feet
        Components: V, M (bat fur and a drop of pitch or piece of coal)
        Duration: Concentration, up to 10 minutes
        https://www.dnd-spells.com/spell/darkness
        """
        if not spell_dict:
            spell_dict = {
                    # Радиус 20 из-за круглой зоны. Получается 35 футов.
                    'concentration':True,
                    'effect':'darkness',
                    'effect_timer':100,
                    'zone_effect':True,
                    'zone_self':True,
                    'direct_hit':True,
                    'attacks_number':1,
                    'attack_range':60,
                    'radius':20,
                    'components':['verbal','material'],
                    'casting_time':'action',
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Darkness',
                    'school':'evocation',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if self.mage.class_features.get('Metamagic_Distant_Spell'):
            spell_dict['attack_range'] *= 2
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Aid(self, spell_level, gen_spell = False, spell_dict = False):
        """Подмога

        Level: 2
        Casting time: 1 Action
        Range: 30 feet
        Components: V, S, M (a tiny strip of white cloth)
        Duration: 8 hours
        https://www.dnd-spells.com/spell/aid
        """
        if not spell_dict:
            spell_dict = {
                    'buff':True,
                    'effect':'aid',
                    'effect_timer':4800,
                    'attack_range':30,
                    'attacks_number':3,
                    'damage_type':'heal',
                    'damage_dice':'0d0',
                    'damage_mod':5,
                    'components':['verbal','somatic','material'],
                    'casting_time':'action',
                    'spell_level':spell_level,
                    'spell_of_choice':'Magic_Missile',
                    'school':'abjuration',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if gen_spell:
            if not spell_dict.get('target_uuid'):
                soldier = self.mage
            else:
                soldier = self.mage.metadict_soldiers[spell_dict['target_uuid']]
            max_hitpoints = soldier.hitpoints_max + spell_dict['damage_mod']
            soldier.set_hitpoints(max_hitpoints = max_hitpoints)
            soldier.set_hitpoints(heal = max_hitpoints)
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Barkskin(self, spell_level, gen_spell = False, spell_dict = False):
        """Дубовая кора

        Level: 2
        Casting time: 1 Action
        Range: Touch
        Components: V, S, M (A handful of oak bark)
        Duration: Concentration, up to 1 hour
        https://www.dnd-spells.com/spell/barkskin
        """
        # TODO: броня берётся из metadict_item.
        if not spell_dict:
            spell_dict = {
                    'buff':True,
                    'concentration':True,
                    'effect':'barkskin',
                    'effect_timer':600,
                    'attacks_number':1,
                    'armor':True,
                    'armor_type':'Barkskin',
                    'armor_class_armor':16,
                    'attack_range':5,
                    'components':['verbal','somatic','material'],
                    'casting_time':'action',
                    'spell_level':spell_level,
                    'spell_of_choice':'Magic_Missile',
                    'school':'transmutation',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if gen_spell:
            if not spell_dict.get('target_uuid'):
                soldier = self.mage
            else:
                soldier = self.mage.metadict_soldiers[spell_dict['target_uuid']]
            soldier.equipment_weapon['Barkskin'] = 1
            soldier.armor.update(soldier.get_armor())
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Dragon_Breath(self, spell_level, gen_spell = False, spell_dict = False):
        """Дыхание дракона

        Level: 2
        Casting time: 1 Bonus Action
        Range: Touch
        Components: V, S, M (a hot pepper)
        Duration: Concentration, up to 1 minute
        https://www.dnd-spells.com/spell/dragons-breath
        """
        if not spell_dict:
            spell_dict = {
                    'ammo':1,
                    'buff':True,
                    'effect':'dragon_breath',
                    'effect_timer':10,
                    'zone':True,
                    'zone_shape':'cone',
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_ability':'dexterity',
                    'attacks_number':1,
                    'attack_range':15,
                    'damage_type':'fire',
                    'damage_type_choice':['acid','cold','fire','lightning','poison'],
                    'damage_dice':'3d6',
                    'components':['verbal','somatic','material'],
                    'casting_time':'bonus_action',
                    'damage_mod':0,
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Magic_Missile',
                    'school':'transmutation',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if gen_spell:
            if not spell_dict.get('target_uuid'):
                soldier = self.mage
            else:
                soldier = self.mage.metadict_soldiers[spell_dict['target_uuid']]
            # Даёт атаку драконьим дыханием, тип урона на выбор заклинателя:
            damage_type = random.choice(spell_dict['damage_type_choice'])
            spell_dict_copy = copy.deepcopy(spell_dict)
            spell_dict_copy['buff'] = False
            soldier.attacks[('zone', 'Dragon_Breath')] = spell_dict_copy
        return spell_dict

#----
# 3 lvl

    @modify_spell
    @update_spell_dict
    def Enemies_Abound(self, spell_level, gen_spell = False, spell_dict = False):
        """Изобилие врагов.

        Level: 3
        Casting time: 1 Action
        Range: 120 feet
        Components: V, S
        Duration: Concentration, up to 1 minute
        https://www.dnd-spells.com/spell/enemies-abound
        """
        if not spell_dict:
            spell_dict = {
                    'debuff':True,
                    'concentration':True,
                    'effect':'enemies_abound',
                    'effect_timer':10,
                    'attacks_number':1,
                    'attack_range':120,
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_all':True,
                    'savethrow_danger':True,
                    'savethrow_ability':'intelligence',
                    'components':['verbal','somatic'],
                    'casting_time':'action',
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Enemies_Abound',
                    'school':'enchantment',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if gen_spell:
            if not spell_dict.get('target_uuid'):
                soldier = self.mage
            else:
                soldier = self.mage.metadict_soldiers[spell_dict['target_uuid']]
            # Спасбросок интеллекта против очарования:
            # Бесстрашные неуязвимы к Enemies_Abound
            difficult = spell_dict['spell_save_DC']
            ability = spell_dict['savethrow_ability']
            advantage = spell_dict.get('savethrow_advantage', False)
            disadvantage = spell_dict.get('savethrow_disadvantage', False)
            danger = spell_dict.get('savethrow_danger', False)
            # Эффекты заклинания висят в round_run_soldier. Здесь только спасбросок.
            if soldier.get_savethrow(difficult, ability, advantage, disadvantage, danger)\
                    or 'fearless' in soldier.commands:
                return False
            else:
                soldier.ally_side, soldier.enemy_side, = soldier.enemy_side, soldier.ally_side
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Fear(self, spell_level, gen_spell = False, spell_dict = False):
        """Ужас.

        Level: 3
        Casting time: 1 Action
        Range: Self (30-foot cone)
        Components: V, S, M (a white feather or the heart of a hen)
        Duration: Concentration, up to 1 minute 
        https://www.dnd-spells.com/spell/fear
        """
        # TODO: Дальность расширена из-за проблем с наведением конуса. Ищи баг.
        if not spell_dict:
            spell_dict = {
                    'concentration':True,
                    'debuff':True,
                    'effect':'fear',
                    'effect_timer':10,
                    'safe':True,
                    'zone':True,
                    'zone_shape':'cone',
                    'attack_range':45,
                    #'attack_range':30,
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_all':True,
                    'savethrow_ability':'wisdom',
                    'components':['verbal'],
                    'casting_time':'action',
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Magic_Missile',
                    'school':'illusion',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Call_Lightning(self, spell_level, gen_spell = False, spell_dict = False):
        """Призыв молнии.

        Level: 3
        Casting time: 1 Action
        Range: 120 feet
        Components: V, S
        Duration: Concentration, up to 10 minutes
        https://www.dnd-spells.com/spell/call-lightning
        """
        # Зона поражения 2x2 клетки, а не 3x3.
        # Молния поражает цели в пределах 5 футов от точки.
        if not spell_dict:
            spell_dict = {
                    'concentration':True,
                    'effect':'call_lightning',
                    'effect_timer':100,
                    'zone':True,
                    'zone_shape':'2x2',
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_ability':'dexterity',
                    'attacks_number':1,
                    'attack_range':120,
                    'radius':5,
                    'damage_type':'lightning',
                    'damage_dice':'3d10',
                    'components':['verbal','somatic'],
                    'casting_time':'action',
                    'damage_mod':0,
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Magic_Missile',
                    'school':'conjuration',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if int(spell_level[0]) > 3:
            dice = int(spell_dict['damage_dice'][0])
            dice += int(spell_level[0]) - 1
            spell_dict['damage_dice'] = str(dice) + spell_dict['damage_dice'][1:]
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Fireball(self, spell_level, gen_spell = False, spell_dict = False):
        """Огненный шар.

        Level: 3
        Casting time: 1 Action
        Range: 150 feet
        Components: V,S,M
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/fireball
        """
        if not spell_dict:
            spell_dict = {
                    'zone':True,
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_ability':'dexterity',
                    'attacks_number':1,
                    'attack_range':150,
                    'radius':20,
                    'damage_type':'fire',
                    'damage_dice':'8d6',
                    'components':['verbal','somatic','material'],
                    'casting_time':'action',
                    'damage_mod':0,
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Magic_Missile',
                    'school':'evocation',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if int(spell_level[0]) > 3:
            dice = int(spell_dict['damage_dice'][0])
            dice += int(spell_level[0]) - 1
            spell_dict['damage_dice'] = str(dice) + spell_dict['damage_dice'][1:]
        if self.mage.class_features.get('Metamagic_Distant_Spell'):
            spell_dict['attack_range'] *= 2
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Lightning_Bolt(self, spell_level, gen_spell = False, spell_dict = False):
        """Удар молнии.

        Level: 3
        Casting time: 1 Action
        Range: Self (100-foot line)
        Components: V, S, M (a bit of fur and a rod of amber, crystal, or glass)
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/lightning-bolt
        """
        # TODO: добавь эффект no_cover. А то следующие цели получают +2, +5 к спасброскам ловкости.
        if not spell_dict:
            spell_dict = {
                    'zone':True,
                    'zone_shape':'ray',
                    #'ignore_cover':True,
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_ability':'dexterity',
                    'attacks_number':1,
                    'attack_range':100,
                    'damage_type':'lightning',
                    'damage_dice':'8d6',
                    'components':['verbal','somatic','material'],
                    'casting_time':'action',
                    'damage_mod':0,
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Magic_Missile',
                    'school':'evocation',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if int(spell_level[0]) > 3:
            dice = int(spell_dict['damage_dice'][0])
            dice += int(spell_level[0]) - 1
            spell_dict['damage_dice'] = str(dice) + spell_dict['damage_dice'][1:]
        if self.mage.class_features.get('Metamagic_Distant_Spell'):
            spell_dict['attack_range'] *= 2
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Melf_Minute_Meteors(self, spell_level, gen_spell = False, spell_dict = False):
        """Мельфовы маленькие метеоры.

        Level: 3
        Casting time: 1 Action
        Range: Self
        Components: V, S, M
        Duration: Concentration, up to 10 minutes
        https://www.dnd-spells.com/spell/melfs-minute-meteors
        """
        if not spell_dict:
            spell_dict = {
                    'ammo':6,
                    'concentration':True,
                    'concentration_ready':True,
                    'effect':'minute_meteors',
                    'effect_timer':100,
                    'zone':True,
                    'zone_shape':'square',
                    'radius':5,
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_ability':'dexterity',
                    'attacks_number':1,
                    'attack_range':120,
                    'damage_type':'fire',
                    'damage_dice':'2d6',
                    'components':['verbal'],
                    'casting_time':'bonus_action',
                    'damage_mod':0,
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Magic_Missile',
                    'school':'evocation',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if int(spell_level[0]) > 3:
            bonus_ammo = 2 * int(spell_level[0]) - 3 * 2
            spell_dict['ammo'] += bonus_ammo
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Counterspell(self, spell_level, gen_spell = False, spell_dict = False):
        """Контрзаклинание.

        Дальность 300 футов. Нужно видеть врага.

        Level: 3
        Casting time: Special
        Range: 60 feet
        Components: S
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/counterspell
        """
        if not spell_dict:
            spell_dict = {
                    'effect':'counterspell',
                    'attack_range':300,
                    'components':['somatic'],
                    'casting_time':'reaction',
                    'spell_level':spell_level,
                    'spell_of_choice':'Magic_Missile',
                    'school':'abjuration',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Dispel_Magic(self, spell_level, gen_spell = False, spell_dict = False):
        """Рассеивание магии.
        
        Можно использовать как импровизированный Counterspell
        В этом случае используется подготовленное действие.

        Level: 3
        Casting time: 1 Action
        Range: 120 feet
        Components: V, S
        Duration: Instantaneous
        """
        if not spell_dict:
            spell_dict = {
                    'effect':'counterspell',
                    'attack_range':120,
                    'components':['verbal','somatic'],
                    'casting_time':'action',
                    'spell_level':spell_level,
                    'spell_of_choice':'Magic_Missile',
                    'school':'abjuration',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Crusaders_Mantle(self, spell_level, gen_spell = False, spell_dict = False):
        """Мантия крестоносца.

        Level: 3
        Casting time: 1 Action
        Range: Self
        Components: V
        Duration: Concentration, up to 1 minute
        https://www.dnd-spells.com/spell/crusaders-mantle
        """
        if not spell_dict:
            spell_dict = {
                    'safe':True,
                    'concentration':True,
                    'effect':'crusaders_mantle',
                    'effect_timer':10,
                    'zone_effect':True,
                    'zone_self':True,
                    'direct_hit':True,
                    'attack_range':0,
                    'radius':30,
                    'components':['verbal'],
                    'damage_type':'radiant',
                    'damage_dice':'1d4',
                    'casting_time':'action',
                    'spell_level':spell_level,
                    'damage_mod':0,
                    'spell_of_choice':'Magic_Missile',
                    'school':'evocation',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        return spell_dict


    @modify_spell
    @update_spell_dict
    def Spirit_Guardians(self, spell_level, gen_spell = False, spell_dict = False):
        """Духовные стражи.

        Level: 3
        Casting time: 1 Action
        Range: Self (15-foot-radius)
        Components: V, S, M (a holy symbol)
        Duration: Concentration, up to 10 minutes
        https://www.dnd-spells.com/spell/spirit-guardians
        """
        if not spell_dict:
            spell_dict = {
                    # TODO:
                        # Это заклинание ужасающе сильное. Просто истребляет всех.
                        # нужно сократить радиус до 10 футов, либо длительность до 1 минуты.
                    'safe':True,
                    'concentration':True,
                    'effect':'spirit_guardians',
                    'effect_timer':100,
                    'zone_effect':True,
                    'zone_danger':True,
                    'zone_self':True,
                    'before_round':True,
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_ability':'wisdom',
                    'attacks_number':1,
                    'radius':15,
                    'attack_range':0,
                    'damage_type':'radiant',
                    'damage_dice':'3d8',
                    'components':['verbal','somatic','material'],
                    'casting_time':'action',
                    'damage_mod':0,
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Sacred_Flame',
                    'school':'conjuration',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if int(spell_level[0]) > 3:
            dice = int(spell_dict['damage_dice'][0])
            dice += int(spell_level[0]) - 1
            spell_dict['damage_dice'] = str(dice) + spell_dict['damage_dice'][1:]
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Blink(self, spell_level, gen_spell = False, spell_dict = False):
        """Мерцание.

        Level: 3
        Casting time: 1 Action
        Range: Self
        Components: V, S
        Duration: 1 minute
        https://www.dnd-spells.com/spell/blink
        """
        if not spell_dict:
            spell_dict = {
                    'buff':True,
                    'effect':'blink',
                    'effect_timer':10,
                    'attack_range':0,
                    'components':['verbal','somatic'],
                    'casting_time':'action',
                    'spell_level':spell_level,
                    'spell_of_choice':'Magic_Missile',
                    'school':'transmutation',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        return spell_dict

#----
# 4 lvl

    @modify_spell
    @update_spell_dict
    def Stoneskin(self, spell_level, gen_spell = False, spell_dict = False):
        """Каменная кожа.

        Level: 4
        Casting time: 1 Action
        Range: Touch
        Components: V, S, M (diamond dust worth 100 gp, which the spell consumes)
        Duration: Concentration, up to 1 hour
        https://www.dnd-spells.com/spell/stoneskin
        """
        if not spell_dict:
            # TODO: сделай homebrew, 17 AC брони в стиле Barkskin.
            spell_dict = {
                    'buff':True,
                    'repeat':True,
                    'concentration':True,
                    'effect':'stoneskin',
                    'effect_timer':600,
                    'attacks_number':1,
                    'attack_range':0,
                    'resistance':['slashing','piercing','bludgeoning'],
                    'components':['verbal','somatic','material'],
                    'casting_time':'action',
                    'spell_level':spell_level,
                    'spell_of_choice':'Magic_Missile',
                    'school':'abjuration',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if gen_spell:
            if not spell_dict.get('target_uuid'):
                soldier = self.mage
            else:
                soldier = self.mage.metadict_soldiers[spell_dict['target_uuid']]
            soldier.resistance.extend(spell_dict['resistance'])
            soldier.resistance = list(set(soldier.resistance))
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Ice_Storm(self, spell_level, gen_spell = False, spell_dict = False):
        """Град

        Level: 4
        Casting time: 1 Action
        Range: 300 feet
        Components: V, S, M (a pinch of dust and a few drops of water)
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/ice-storm
        """
        if not spell_dict:
            spell_dict = {
                    'zone':True,
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_ability':'dexterity',
                    'subspell':'Ice_Storm_Cold',
                    'attacks_number':1,
                    'attack_range':300,
                    'radius':20,
                    'damage_type':'bludgeoning',
                    'damage_dice':'2d8',
                    'components':['verbal','somatic','material'],
                    'casting_time':'action',
                    'damage_mod':0,
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Magic_Missile',
                    'school':'evocation',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if int(spell_level[0]) > 4:
            dice = int(spell_dict['damage_dice'][0])
            dice += int(spell_level[0]) - 1
            spell_dict['damage_dice'] = str(dice) + spell_dict['damage_dice'][1:]
        if self.mage.class_features.get('Metamagic_Distant_Spell'):
            spell_dict['attack_range'] *= 2
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Sickening_Radiance(self, spell_level, gen_spell = False, spell_dict = False):
        """Болезнное сияние.

        Level: 4
        Casting time: 1 Action
        Range: 120 feet
        Components: V, S
        Duration: Concentration, up to 10 minutes
        https://www.dnd-spells.com/spell/sickening-radiance
        """
        # TODO: уровень истощения после каждого неудачного спасброска.
        if not spell_dict:
            spell_dict = {
                    'concentration':True,
                    'effect':'sickening_radiance',
                    'effect_timer':100,
                    'zone':True,
                    'zone_effect':True,
                    'zone_danger':True,
                    'before_round':True,
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_all':True,
                    'savethrow_ability':'constitution',
                    'attacks_number':1,
                    'attack_range':120,
                    'radius':30,
                    'damage_type':'radiant',
                    'damage_dice':'4d10',
                    'components':['verbal','somatic'],
                    'casting_time':'action',
                    'damage_mod':0,
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Magic_Missile',
                    'school':'evocation',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Vitriolic_Sphere(self, spell_level, gen_spell = False, spell_dict = False):
        """Едкий шар.

        Level: 4
        Casting time: 1 Action
        Range: 150 feet
        Components: V, S, M (a drop of giant slug bile)
        Duration: Instantaneous 
        https://www.dnd-spells.com/spell/vitriolic-sphere
        """
        if not spell_dict:
            spell_dict = {
                    # TODO: атака во второй раунд на 5d4. Пока сделано 15d4.
                    'effect':'vitriolic_sphere',
                    'effect_timer':1,
                    'zone':True,
                    'zone_effect':True,
                    'zone_danger':True,
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_ability':'dexterity',
                    'attacks_number':1,
                    'attack_range':150,
                    'radius':20,
                    'damage_type':'acid',
                    #'damage_dice':'10d4',
                    'damage_dice':'15d4',
                    'components':['verbal','somatic','material'],
                    'casting_time':'action',
                    'damage_mod':0,
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Magic_Missile',
                    'school':'evocation',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        return spell_dict

#----
# 5 lvl

    @modify_spell
    @update_spell_dict
    def Cone_of_Cold(self, spell_level, gen_spell = False, spell_dict = False):
        """Конус холода.

        Level: 5
        Casting time: 1 Action
        Range: Self (60-foot cone)
        Components: V, S, M (a small crystal or glass cone)
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/cone-of-cold
        """
        # TODO: effect "icing" -- превращает погибших в ледяные статуи.
        if not spell_dict:
            spell_dict = {
                    'zone':True,
                    'zone_shape':'cone',
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_ability':'constitution',
                    'attacks_number':1,
                    'attack_range':60,
                    'damage_type':'cold',
                    'damage_dice':'8d8',
                    'components':['verbal','somatic','material'],
                    'casting_time':'action',
                    'damage_mod':0,
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Magic_Missile',
                    'school':'evocation',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if int(spell_level[0]) > 5:
            dice = int(spell_dict['damage_dice'][0])
            dice += int(spell_level[0]) - 1
            spell_dict['damage_dice'] = str(dice) + spell_dict['damage_dice'][1:]
        return spell_dict

    @modify_spell
    @update_spell_dict
    def Dawn(self, spell_level, gen_spell = False, spell_dict = False):
        """Рассвет.

        Level: 5
        Casting time: 1 Action
        Range: 60 feet
        Components: V, S, M (a sunburst pendant worth at least 100 gp)
        Duration: Concentration, up to 1 minute 
        https://www.dnd-spells.com/spell/dawn
        """
        # Первый удар заклинания неожиданный, дальше только смещение луча.
        if not spell_dict:
            spell_dict = {
                    'ammo':1,
                    'concentration':True,
                    'concentration_no_ammo':True,
                    'effect':'dawn',
                    'effect_timer':10,
                    'zone':True,
                    'zone_effect':True,
                    'zone_danger':True,
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_ability':'constitution',
                    'attacks_number':1,
                    'attack_range':60,
                    'radius':30,
                    'damage_type':'radiant',
                    'damage_dice':'4d10',
                    'components':['verbal','somatic','material'],
                    'casting_time':'action',
                    'damage_mod':0,
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Magic_Missile',
                    'school':'evocation',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        #if int(spell_level[0]) > 5:
        #    dice = int(spell_dict['damage_dice'][0])
        #    dice += int(spell_level[0]) - 1
        #    spell_dict['damage_dice'] = str(dice) + spell_dict['damage_dice'][1:]
        return spell_dict

#----
# 6 lvl

    @modify_spell
    @update_spell_dict
    def Circle_of_Death(self, spell_level, gen_spell = False, spell_dict = False):
        """Круг смерти.

        Level: 6
        Casting time: 1 Action
        Range: 150 feet
        Components: V, S, M (the powder of a crushed black pearl worth at least 500 gp)
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/circle-of-death
        """
        if not spell_dict:
            spell_dict = {
                    'zone':True,
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_ability':'constitution',
                    'attacks_number':1,
                    'attack_range':150,
                    'radius':60,
                    'damage_type':'necrotic_energy',
                    'damage_dice':'8d6',
                    'components':['verbal','somatic','material'],
                    'casting_time':'action',
                    'damage_mod':0,
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Magic_Missile',
                    'school':'necromancy',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        # Плюс 2d6 урона за каждый круг выше 6
        if int(spell_level[0]) > 6:
            dice = int(spell_dict['damage_dice'][0])
            dice += (int(spell_level[0]) - 6) * 2
            spell_dict['damage_dice'] = str(dice) + spell_dict['damage_dice'][1:]
        if self.mage.class_features.get('Metamagic_Distant_Spell'):
            spell_dict['attack_range'] *= 2
        return spell_dict

#----
# 7 lvl

    @modify_spell
    @update_spell_dict
    def Regeneration(self, spell_level, gen_spell = False, spell_dict = False):
        """Регенерация

        Level: 7
        Casting time: 1 Minute
        Range: Touch
        Components: V, S, M (a prayer wheel and holy water)
        Duration: 1 hour
        https://www.dnd-spells.com/spell/regenerate
        """
        if not spell_dict:
            spell_dict = {
                    'buff':True,
                    'repeat':True,
                    'effect':'regeneration',
                    'effect_timer':600,
                    'attacks_number':1,
                    'attack_range':5,
                    'damage_type':'heal',
                    'healing_dice':'4d8',
                    'healing_mod':15,
                    'components':['verbal','somatic','material'],
                    'casting_time':'action',
                    'spell_level':spell_level,
                    'spell_save_DC':8 + self.find_spell_attack_mod(),
                    'spell_of_choice':'Bane',
                    'school':'transmutation',
                    }
            spell_dict = copy.deepcopy(spell_dict)
        if gen_spell:
            if not spell_dict.get('target_uuid'):
                soldier = self.mage
            else:
                soldier = self.mage.metadict_soldiers[spell_dict['target_uuid']]
            # При первом использовании восстанавливает 4d8+15 хитов:
            if soldier.hitpoints < soldier.hitpoints_max and not 'regeneration' in soldier.buffs:
                heal = dices.dice_throw_advantage(spell_dict['healing_dice']) + spell_dict['healing_mod']
                soldier.set_hitpoints(heal = heal)
                soldier.stable = True
            # Далее 1 хит/раунд, лечит травмы:
            elif 'regeneration' in soldier.buffs:
                soldier.set_hitpoints(heal = 1)
                soldier.stable = True
                if soldier.disabled:
                    soldier.disabled = False
                if soldier.traumas_dict:
                    soldier.traumas_dict = {}
                #if len(soldier.traumas_dict) >= 1
                #    soldier.traumas_dict.pop(random.choice(list(soldier.traumas_dict.keys())))
            else:
                return False
        return spell_dict
