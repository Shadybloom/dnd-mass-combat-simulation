#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections
import operator
import dices
import argparse
from soldier_fight import *
from data import lang_sindar
from data import lang_human
from data import squads
from data import database
from data import spells
from collections import OrderedDict

#-------------------------------------------------------------------------
# Аргументы командной строки:

def create_parser():
    """Список доступных параметров скрипта."""
    parser = argparse.ArgumentParser()
    parser.add_argument('squad',
                        nargs='*',
                        help='Например: legionary'
                        )
    parser.add_argument('-s', '--save',
                        action='store_true', dest='save', default=False,
                        help='Сохранить отряд в базу данных.'
                        )
    return parser

#-------------------------------------------------------------------------
# Классы:

class squad_generation():
    """Создаём отряд, распределяем должности, обучаем, снаряжаем.
    
    - Генерируется число солдат, равное численности отряда.
    - Солдаты распределяются по должностям и уровням (лучшие -- командиры)
    """
    metadict_squads = squads.metadict_squads
    # Для названий отрядов:
    dict_words = {}
    dict_words.update(lang_sindar.dict_words)
    dict_words.update(lang_human.dict_words)
    # Подключаемся к базе данных солдат:
    database = database.database()

    def create_squad(self, squad_type):
        """Создаём отряд.
        
        Описание функции.
        """
        # TODO: Добавь "воссоздание" отрядов из базы данных.
        # В том случае, если вместо squad_type указано его имя.
        self.squad_type = squad_type
        self.dict_squad = self.metadict_squads[self.squad_type].copy()
        # У отряда тоже есть имя -- название:
        self.name, self.name_translate = gen_name(self.dict_words, name_length = 3)
        reinforce_number = sum(self.dict_squad.values())
        # Изначально все бойцы отряда 1 уровня:
        self.metadict_soldiers = self.gen_soldiers(reinforce_number)
        self.squad_number = len(self.metadict_soldiers)
        self.soldiers_list = list(self.metadict_soldiers.keys())
        # Здесь бойцы отряда получают levelup и распределяются по должностям:
        self.metadict_soldiers.update(self.set_ranks())
        #self.set_initiative()
        # Отряд получает верховых животных:
        self.pet_types = self.find_pets(self.metadict_soldiers)
        for pet_type, number in self.pet_types.items():
            self.metadict_soldiers.update(self.gen_pets(number, pet_type))
        # Лошади знакомятся с хозяевами (и хозяева снаряжают их бронёй):
        self.set_mounts()
        self.set_mounts_armor()
        # Кое-какая обобщённая статистика:
        self.behavior = self.find_base_behaviour()
        self.squad_overload = self.calculate_squad_overload()
        self.armor_class = self.calculate_squad_armor_class()
        self.hitpoints_medial = self.calculate_squad_hitpoints_medial()
        self.attack_mod = self.calculate_squad_attack_mod()
        self.squad_cost = self.calculate_squad_cost()
        #self.set_hitpoints()

    def load_squad_from_DB(self, squad_name, get_injured = False, get_all = False):
        """Воссоздаём отряд из базы данных.
        
        Там только список солдат.
        """
        # TODO: пили вывод данных из БД.
        # Придумай что-нибудь с типом отряда и переводом имени
        self.squad_type = squad_name
        self.name = squad_name
        self.name_translate = squad_name
        soldiers_uuid_list = self.database.print_squad_soldiers(squad_name)
        self.metadict_soldiers = self.load_soldiers_from_DB(soldiers_uuid_list, get_injured, get_all)
        self.squad_number = len(self.metadict_soldiers)
        self.soldiers_list = list(self.metadict_soldiers.keys())
        # Кое-какая обобщённая статистика:
        self.behavior = self.find_base_behaviour()
        self.squad_overload = self.calculate_squad_overload()
        self.armor_class = self.calculate_squad_armor_class()
        self.attack_mod = self.calculate_squad_attack_mod()
        self.squad_cost = self.calculate_squad_cost()

    def load_soldiers_from_DB(self, soldiers_uuid_list, get_injured = False, get_all = False):
        """Создаём солдат, загружая характеристики из базы данных."""
        metadict_soldiers = {}
        for uuid_string in soldiers_uuid_list:
            soldier_dict = self.database.soldier_from_database(uuid_string)
            if not soldier_dict.get('death')\
                    and not soldier_dict.get('disabled')\
                    and not soldier_dict.get('captured')\
                    or get_all:
                if not soldier_dict.get('fall') and soldier_dict.get('hitpoints') > 0\
                        or get_all or get_injured:
                    recruit = soldier_in_battle()
                    recruit.__dict__ = soldier_dict
                    # Восстанавливаем рекурсивную ссылку:
                    recruit.spells_generator.mage = recruit
                    metadict_soldiers[recruit.uuid] = recruit
        # Сортируем бойцов по уровню, чтобы на вершине были командиры.
        metadict_soldiers = OrderedDict(reversed(sorted(metadict_soldiers.items(),key=lambda x: x[1].level)))
        return metadict_soldiers

    def set_hitpoints(self):
        """Хитпоинты в начале боя."""
        for uuid,soldier in self.metadict_soldiers.items():
            soldier.set_hitpoints()

    def set_initiative(self):
        """Броски инициативы бойцам стороны."""
        for uuid,soldier in self.metadict_soldiers.items():
            soldier.set_initiative()

    def set_ally_side(self, ally_side):
        """Указываем своих."""
        self.ally_side = ally_side
        for uuid,soldier in self.metadict_soldiers.items():
            soldier.set_ally_side(ally_side)

    def set_enemy_side(self, enemy_side):
        """Указываем врага."""
        self.enemy_side = enemy_side
        for uuid,soldier in self.metadict_soldiers.items():
            soldier.set_enemy_side(enemy_side)

    def reinforce(self, reinforce_number, rank = None):
        """Пополняем отряд. Просто создаём новых солдат и пополняем словарь."""
        self.metadict_soldiers.update(self.gen_soldiers(reinforce_number))
        self.squad_number = len(self.metadict_soldiers)

    def reinforce_pets(self, reinforce_number, animal_type = None):
        """Пополняем отряд лошадками."""
        # TODO: так потерявшие коней всадники должны получить новых.
        self.metadict_soldiers.update(self.gen_pets(reinforce_number, animal_type))

    def find_pets(self, metadict_soldiers):
        """Возвращает словарь ездовых/боевых животных отряда.
        
        Питомцы должны быть указаны в шаблонах metadict_chars.
        """
        # Находим нуждающихся в лошадках бойцов:
        animals_list = []
        for soldier in metadict_soldiers.values():
            if hasattr(soldier, 'mount_type'):
                animals_list.append(soldier.mount_type)
        # Группируем одинаковых питомцев в словарь:
        animals_dict = {}
        for key in animals_list:
            if not key in animals_dict:
                animals_dict[key] = 1
            elif key in animals_dict:
                animals_dict[key] += 1
        return animals_dict

    def set_mounts(self):
        """Верховые животные получают хозяев, а хозяева верховых животных.
        
        Отныне они узнают друг друга по uuid.
        """
        for soldier in self.metadict_soldiers.values():
            if hasattr(soldier, 'mount_type') and not hasattr(soldier, 'mount_uuid'):
                for mount in self.metadict_soldiers.values():
                    if mount.rank == soldier.mount_type and not hasattr(mount, 'master_uuid'):
                        soldier.mount_uuid = mount.uuid
                        mount.master_uuid = soldier.uuid
                        break

    def set_mounts_armor(self):
        """Верховые животные получают броню от своих хозяев."""
        for soldier in self.metadict_soldiers.values():
            if hasattr(soldier, 'mount_uuid'):
                mount = self.metadict_soldiers[soldier.mount_uuid]
                mount.equipment_weapon = soldier.equipment_mount
                mount.armor = mount.takeoff_armor()
                mount.armor.update(mount.get_armor())

    def find_medial_abilities(self):
        """Средняя сумма характеристик по роте.
        
        Используется для вывода статистики, другого применения нет.
        """
        ability_sum_list = [ ]
        for soldier in self.metadict_soldiers.values():
            ability_sum = sum(soldier.abilityes.values())
            ability_sum_list.append(ability_sum)
        medial_ability_sum = sum(ability_sum_list) / len(ability_sum_list)
        return medial_ability_sum

    def find_best(self):
        """Находим лучшего в роте по сумме параметров.
        
        Используется для выбора офицеров. Крепкие получаются бычары:
        - В геройской роте средние параметры командира -- 95
        - В роте из простолюдинов среднее для командира -- 82
        """
        ability_sum_min = 0
        for soldier in self.metadict_soldiers.values():
            ability_sum = sum(soldier.abilityes.values())
            if ability_sum >= ability_sum_min:
                ability_sum_min = ability_sum
                best_soldier = soldier
        return best_soldier.uuid

    def find_base_behaviour(self):
        """Определяем тактику отряда по основному юниту (лучники, бойцы).
        
        Это использует squad_AI для выбора задачи боя.
        """
        types_list = [soldier.behavior for soldier in self.metadict_soldiers.values()\
                if soldier.behavior != 'mount']
        types_dict = collections.Counter(types_list)
        max_type = max(types_dict.items(), key=operator.itemgetter(1))
        return max_type[0]

    def calculate_squad_overload(self):
        """Суммарный вес снаряжения отряда и число перегруженных бойцов."""
        overload_soldiers = 0
        lightload_soldiers = 0
        squad_overload = {}
        for soldier in self.metadict_soldiers.values():
            for key, value in soldier.overload.items():
                if key == 'base_speed':
                    pass
                elif not key in squad_overload and not type(value) == bool:
                    squad_overload[key] = value
                elif key in squad_overload and type(value) != bool:
                    squad_overload[key] += value
                elif key == 'battle_overload' and value == True:
                    overload_soldiers += 1
                elif key == 'battle_lightload' and value == True:
                    lightload_soldiers += 1
        #squad_overload.pop('base_speed'),
        #squad_overload.pop('battle_lightload'),
        #squad_overload.pop('battle_overload'),
        #squad_overload.pop('travel_overload')
        squad_overload['overload_soldiers'] = overload_soldiers
        squad_overload['lightload_soldiers'] = lightload_soldiers
        return squad_overload

    def calculate_squad_armor_class(self):
        """Усреднённая защита отряда."""
        sum_armor_class = sum([soldier.armor['armor_class'] for soldier in self.metadict_soldiers.values()])
        squad_number = len(self.metadict_soldiers)
        return round(sum_armor_class / squad_number, 1)

    def calculate_squad_hitpoints_medial(self):
        """Усреднённые хиты по отряду."""
        sum_hitpoints = sum([soldier.hitpoints_max for soldier in self.metadict_soldiers.values()])
        squad_number = len(self.metadict_soldiers)
        return round(sum_hitpoints / squad_number, 1)

    def calculate_squad_attack_mod(self):
        """Средний по отряду (и по типам бойцов) модификатор атаки.
        
        В выводе кортеж:
        1) атака лучшего бойца.
        2) лучшая атака бойцов усреднённо.
        3) средняя атака бойцов по всем видам оружия.
        """
        attack_mod_best = 0
        attack_mods_dict_sum = {}
        attack_mods_dict_max = {}
        for soldier in self.metadict_soldiers.values():
            attacks_mods_list = [attack['attack_mod'] for key, attack in soldier.attacks.items()
                    if not 'volley' in key]
            if attacks_mods_list:
                attack_mod_max = max(attacks_mods_list)
                attack_mod_medial = sum(attacks_mods_list) / len(attacks_mods_list)
                if not soldier.rank in attack_mods_dict_sum:
                    attack_mods_dict_max[soldier.rank] = attack_mod_max
                    attack_mods_dict_sum[soldier.rank] = attack_mod_medial
                else:
                    attack_mods_dict_max[soldier.rank] += attack_mod_max
                    attack_mods_dict_sum[soldier.rank] += attack_mod_medial
                #if attack_mod_max > attack_mod_best:
                #    attack_mod_best = attack_mod_max
                # Дуэлятся с героями у нас только командиры 4+ lvl:
                if attack_mod_max > attack_mod_best\
                        and soldier.behavior == 'commander' and soldier.level >= 4:
                    attack_mod_best = attack_mod_max
        attack_mod_medial = round(sum(attack_mods_dict_sum.values()) / len(self.metadict_soldiers), 1)
        attack_mod_max = round(sum(attack_mods_dict_max.values()) / len(self.metadict_soldiers), 1)
        #attack_mods_dict = {}
        #for key, attack_mod_sum in attack_mods_dict_sum.items():
        #    rank_list = [soldier for soldier in self.metadict_soldiers.values()\
        #            if soldier.rank == key]
        #    rank_number = len(rank_list)
        #    attack_mods_dict[key] = round(attack_mod_sum / rank_number, 1)
        #return attack_mods_dict
        return attack_mod_best, attack_mod_max, attack_mod_medial
    
    def calculate_squad_cost(self):
        """Суммарная стоимость отряда."""
        squad_cost_dict = {}
        for soldier in self.metadict_soldiers.values():
            for key, value in soldier.unit_cost.items():
                if not key in squad_cost_dict:
                    squad_cost_dict[key] = value
                elif key in squad_cost_dict and type(value) != bool:
                    squad_cost_dict[key] += value
        for key, value in squad_cost_dict.items():
            squad_cost_dict[key] = round(value)
        return squad_cost_dict

    def gen_pets(self, number, animal_type):
        """Даём отряду верховых животных, питомцев."""
        metadict_pets = {}
        for n in range(number):
            pet = soldier_in_battle()
            pet.create_pet(animal_type)
            pet.squad_name = self.name
            pet.squad_name_translate = self.name_translate
            metadict_pets[pet.uuid] = pet
        return metadict_pets

    def select_soldiers(func):
        """Выкидываем слабейших из состава отряда.

        Для этого есть метка recruit_selection (которая должна быть у всех).
        """
        def wrapper(self, squad_number, rank = None):
            metadict_soldiers = func(self, squad_number, rank = None)
            if not rank and [soldier for soldier in metadict_soldiers.values()
                    if soldier.__dict__.get('recruit_selection')]:
                # Убираем рекрутов из шаблона отряда:
                dict_squad = self.dict_squad.copy()
                common_soldier = max(dict_squad, key=lambda k: dict_squad[k])
                dict_squad.pop(common_soldier)
                # Отбираем лучших по оставшемуся числу:
                number = (sum(dict_squad.values()))
                metadict_soldiers = self.select_best_soldiers(number, metadict_soldiers)
            return metadict_soldiers
        return wrapper

    def select_best_soldiers(self, number, metadict_soldiers):
        """Выбирает определённое число лучших солдат в отряде.
        
        Лучшими считаются бойцы с наибольшей суммой параметров.
        """
        # ЗАМЕТКА: Стоило бы учесть хитпоинты, но все бойцы пока что 1 lvl.
        # ------------------------------------------------------------
        # Если понадобится, прибавь к сумме ниже число хитов, делённое на уровень.
        # Тогда нам нужна независимая от constitution сумма хитов. Да просто вычти!
        # ------------------------------------------------------------
        abilityes_dict = {uuid:sum(soldier.abilityes.values())
                for uuid, soldier in metadict_soldiers.items()}
        abilityes_dict = OrderedDict(reversed(sorted(abilityes_dict.items(),key=lambda x: x[1])))
        best_soldiers_list = list(abilityes_dict.keys())[0:number]
        best_soldiers_dict = {uuid:soldier for uuid, soldier in metadict_soldiers.items()
                if uuid in best_soldiers_list}
        #print([sum(soldier.abilityes.values()) for soldier in best_soldiers_dict.values()])
        return best_soldiers_dict

    @select_soldiers
    def gen_soldiers(self, squad_number, rank = None):
        """Даём отряду столько-то бойцов определённого ранга.

        По умолчанию берётся самый многочисленный ранг (рядовые бойцы).
        """
        dict_squad = self.dict_squad.copy()
        if not rank:
            common_soldier = max(dict_squad, key=lambda k: dict_squad[k])
            rank = common_soldier
        # Создаём солдат:
        metadict_soldiers = {}
        for n in range(squad_number):
            recruit = soldier_in_battle()
            recruit.create_soldier(common_soldier)
            # TODO: допилить
            # ------------------------------------------------------------
            # Здесь даём рекруту название его отряда.
            # Лучше бы сделать для этого сеттер (метод soldier)
            # ------------------------------------------------------------
            recruit.squad_name = self.name
            recruit.squad_name_translate = self.name_translate
            metadict_soldiers[recruit.uuid] = recruit
        return metadict_soldiers

    def set_ranks(self):
        """Раздаём должности солдатам, даём levelup лучшим.
        
        Как это работает:
        - В шаблоне отряда ищется самый малочисленный класс солдат (командиры)
        - Последовательно выбираются лучшие из списка рекрутов и их звание повышается.
        - Так командиром роты становится лучший по сумме параметров, а худшие остаются рядовыми.
        - Все командиры/сержанты/капралы получают levelup, чтобы соответствовать своим должностям.
        - Если их класс изменился, характеристики перетасовываются под новый класс (в методе levelup).
        """
        dict_squad = self.dict_squad.copy()
        metadict_reqruits = self.metadict_soldiers
        metadict_soldiers = {}
        for n in range(self.squad_number):
            # TODO: исправить баг
            # ------------------------------------------------------------
            # Тут костыль. Цикл прерывается, если должности закончились, а рекруты остались.
            # Это случается, если вызвать set_ranks заново, после срабатываения create_squad.
            # Один худший рекрут всегда теряется. Да и хрен с ним.
            # ------------------------------------------------------------
            #print(n, self.squad_number, dict_squad)
            if not dict_squad:
                break
            # Находим самое малочисленное звание и лучшего бойца:
            rank = min(dict_squad, key=lambda k: dict_squad[k])
            uuid = self.find_best()
            # Даём лучшему бойцу levelup до нового звания:
            recruit = metadict_reqruits[uuid]
            recruit.levelup(rank)
            metadict_soldiers[uuid] = recruit
            #print(recruit.level, recruit.abilityes, sum(recruit.abilityes.values()))
            # Убираем обработанные параметры рекрута:
            metadict_reqruits.pop(uuid)
            # Убираем занятую должность:
            dict_squad[rank] -=1
            if dict_squad[rank] <= 0:
                dict_squad.pop(rank)
        metadict_soldiers = OrderedDict(reversed(sorted(metadict_soldiers.items(),key=lambda x: x[1].level)))
        return metadict_soldiers

    def throw_squad_initiative(self):
        """Инициатива отряда = инициативы командира.
        
        Ранее была сумма инициативы командиров, но так честнее.
        """
        squad_initiative = 0
        for uuid,soldier in self.metadict_soldiers.items():
            if soldier.behavior == 'commander':
                squad_initiative += soldier.initiative
                break
        return squad_initiative

    def throw_squad_moral(self, enemy_recon, commanders_list, advantage = False, disadvantage = False):
        """Каждый командир даёт от -1 до +2 к морали отряда, как повезёт.
        
        Бросок морали = 1d20 + мод_харизмы + бонус_мастерства
        Сложность проверки = число_врагов/число_союзников * 10
        Если врагов и союзников поровну, сложность проверки = 10
        Если врагов вдвое больше, сложность проверки = 20
        - крит_успех 20 -- +2 мораль.
        - результат >10 -- +1 мораль.
        - результат <10 -- +0 мораль.
        #- крит_провал 0 -- -1 мораль.

        Офицеры дают больший бонус, чем сержанты:
        - сержант 3 lvl -- мораль x1
        - лейтенант 4 lvl -- мораль x2
        - капитан 5 lvl -- мораль x3

        Единицы морали и единицы опасности в danger_sense, это одно и то же.
        """
        if enemy_recon:
            # Число врагов относительно числа наших:
            # Например: 200/100 * 10 = 20 (это сложность броска морали)
            if enemy_recon['ally_strenght'] <= 0:
                enemy_recon['ally_strenght'] = 1
            morale_throw_DC = round(enemy_recon['enemy_strenght'] / enemy_recon['ally_strenght'] * 10)
        else:
            morale_throw_DC = 0
        commanders_list_uuids = [commander.uuid for commander in commanders_list]
        squad_moral = 0
        for uuid in commanders_list_uuids:
            commander_moral = 0
            commander = self.metadict_soldiers[uuid]
            morale_throw = dices.dice_throw_advantage('1d20', advantage, disadvantage)
            # TODO: здесь должне быть навык дипломатии/запугивания/обмана:
            result = morale_throw + commander.mods['charisma'] + commander.proficiency_bonus
            if morale_throw == 20:
                commander_moral += 2
            #elif morale_throw == 1:
            #    commander_moral -= 1
            elif result >= morale_throw_DC:
                commander_moral += 1
            elif result < morale_throw_DC:
                commander_moral += 0
            if commander.level <= 3:
                squad_moral += commander_moral
            elif commander.level == 4:
                squad_moral += commander_moral * 2
            elif commander.level > 4:
                squad_moral += commander_moral * 3
        #print(self.ally_side, enemy_recon, morale_throw_DC, squad_moral)
        return squad_moral

    def gen_ability_stat(self, metadict_soldiers):
        """Показывает распределение параметров по отряду.
        
        Сколько бойцов с силой 10, сколько с силой 11 и т.д.
        """
        dict_ability_stat = {}
        for soldier in metadict_soldiers.values():
            if soldier.behavior != 'mount':
                for ability, value in soldier.abilityes.items():
                    key = (ability, value)
                    if not key in dict_ability_stat:
                        dict_ability_stat[key] = 1
                    elif key in dict_ability_stat:
                        dict_ability_stat[key] += 1
        dict_ability_stat = OrderedDict(reversed(sorted(dict_ability_stat.items(),key=lambda x: x)))
        metadict_ability_stat = {}
        for key, number in dict_ability_stat.items():
            ability, value = key
            if not ability in metadict_ability_stat:
                metadict_ability_stat[ability] = {value:number}
            elif ability in metadict_ability_stat:
                metadict_ability_stat[ability][value] = number
        return metadict_ability_stat

    def print_ability_stat(self, metadict_ability_stat):
        """Вывод статистики параметров в виде графика."""
        import matplotlib.pyplot as plt
        abilities = tuple(metadict_ability_stat.keys())
        for ability, value_dict  in metadict_ability_stat.items():
            x_list = []
            y_list = []
            for value, number in value_dict.items():
                x_list.append(value)
                y_list.append(number)
            plt.scatter(x_list,y_list)
            plt.plot(x_list,y_list)
        plt.legend(abilities, loc='upper left')
        plt.show()

#-------------------------------------------------------------------------
# Тесты:

if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()
    squad = squad_generation()
    # TODO: перенеси ввод данных в отдельную функцию:
    squads_list = list(sorted(squads.metadict_squads.keys()))
    if namespace.squad:
        squad_filter = ' '.join(namespace.squad)
        squads_list_slice = [key for key in squads_list\
                if squad_filter in key]
    else:
        squads_list_slice = squads_list
    for number, squad_name in enumerate(squads_list_slice):
        print(number, squad_name)
    string_number = input('---Выбор отряда (номер отряда):')
    if string_number:
        squad_name = squads_list_slice[int(string_number)]
    squad.create_squad(squad_name)
    for soldier in reversed(list(squad.metadict_soldiers.values())):
        pass
        #print(soldier.name, soldier.name_translate)
        #print(soldier.rank, soldier.attacks.keys())
        #print(soldier.rank, [attack['attack_mod'] for attack in soldier.attacks.values()])
        #print(soldier.rank, soldier.unit_cost)
        #if hasattr(soldier, 'spells'):
        #    print(soldier.spells, soldier.spells_generator.spellslots)
        print('{r} cost:{c} hp:{hp:>2} AC:{ac} load:{l}/{l_max}'.format(
            r = soldier.rank,
            c = soldier.unit_cost['equipment_cost'],
            hp = soldier.hitpoints_max,
            ac = soldier.armor['armor_class'],
            l = soldier.overload['equipment_weight (lb)'],
            l_max = soldier.overload['normal_load (lb)'],
            ))
        #print('{r} sum:{s} STR:{str} DEX:{dex} CON:{con} INT:{int} WIS:{wis} CHA:{cha}'.format(
        #    r = soldier.rank,
        #    s = sum(soldier.abilityes.values()),
        #    str = soldier.abilityes['strength'],
        #    dex = soldier.abilityes['dexterity'],
        #    con = soldier.abilityes['constitution'],
        #    int = soldier.abilityes['intelligence'],
        #    wis = soldier.abilityes['wisdom'],
        #    cha = soldier.abilityes['charisma'],
        #    ))
        #print(soldier.rank, soldier.abilityes['charisma'], sum(soldier.abilityes.values()))
        #print('---------------------')
        #for key, value in soldier.__dict__.items():
        #    print(key, value)
        # Запись бойцов в базу данных:
    if namespace.save:
        print('Отряд будет сохранён в БД: ', squad.database.database_path)
        name_string = input('---Введите название отряда (пропуск -- случайное): ')
        if name_string:
            squad.name = [name_string]
            squad.name_translate = squad.name
            for soldier in reversed(list(squad.metadict_soldiers.values())):
                soldier.squad_name = squad.name
        for soldier in reversed(list(squad.metadict_soldiers.values())):
            squad.database.soldier_to_database(soldier)
        squad.database.commit()
    print(squad.name, squad.name_translate)
    print('cost: {cost} number: {number} weight: {w}/{w_max} (free: {w_free}) overload: {over}'.format(
        over = squad.squad_overload['overload_soldiers'],
        w = squad.squad_overload['equipment_weight (lb)'],
        w_max = squad.squad_overload['normal_load (lb)'],
        w_free = round(squad.squad_overload['normal_load (lb)'] - squad.squad_overload['equipment_weight (lb)']),
        number = len(squad.metadict_soldiers),
        cost = squad.squad_cost['equipment_cost']))
    print('Medial attack_mod:', squad.attack_mod)
    print('Medial hp:', squad.hitpoints_medial,'Medial AC:', squad.armor_class)
    # TODO: перенеси эти расчёты куда-нибудь:
    # Быстрые расчёты атаки:
    target_AC = 20
    attack_test_dict = dices.dice_throw_number('1d20',
            advantage = True, disadvantage = True,
            number = 10000, mod = round(squad.attack_mod[1]))
    percent_sum = 0
    for key, el in attack_test_dict.items():
        if key >= target_AC:
            print('attack: {0} -- {1}%'.format(key, el))
            percent_sum += el
    print('chance: {0}%'.format(round(percent_sum, 1)))
    # Вывод графика:
    #squad.print_ability_stat(squad.gen_ability_stat(squad.metadict_soldiers))
