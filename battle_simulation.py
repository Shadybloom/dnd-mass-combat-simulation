#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import math
import random
import timeit
import time
import traceback
import collections
# Парсер аргументов командной строки:
import argparse

import dices
from data import maps
from data import squads
from data import database
from squad_generation import *
from battlescape import *

#-------------------------------------------------------------------------
# Аргументы командной строки:

def create_parser():
    """Список доступных параметров скрипта."""
    parser = argparse.ArgumentParser()
    parser.add_argument('squads',
                        nargs='*',
                        help='Например: zone_1 legionary zone_5 hoplites'
                        )
    parser.add_argument('-r', '--rounds',
                        action='store', dest='rounds', type=int, default=10,
                        help='Например: 10 -- раундов боя'
                        )
    parser.add_argument('-m', '--map',
                        action='store', dest='map', type=str,
                        help='Например: battle_map_city'
                        )
    parser.add_argument('-c', '--commands',
                        action='store_true', dest='commands', default=False,
                        help='Позволяет команды отрядам: dodge, fearless, retreat, т.д. (-command -- отмена, auto -- автопилот)'
                        )
    parser.add_argument('-v', '--visual',
                        action='store_true', dest='visual', default=False,
                        help='Показывает ходы каждого бойца.'
                        )
    parser.add_argument('-s', '--save',
                        action='store_true', dest='save', default=False,
                        help='Сохранить отряды после боя.'
                        )
    parser.add_argument('-R', '--reinforce',
                        action='store_true', dest='reinforce', default=False,
                        help='Подкрепления во время боя.'
                        )
    parser.add_argument('-I', '--injured',
                        action='store_true', dest='injured', default=False,
                        help='Павшие с 0 hp тоже попадают на поле боя.'
                        )
    parser.add_argument('--rest',
                        action='store_true', dest='short_rest', default=False,
                        help='Короткий отдых перед боем, лечение всех.'
                        )
    return parser

#-------------------------------------------------------------------------
# Классы:

class battle_simulation(battlescape):
    """Описание класса.
    
    """
    # Боец переходит в оборону, если враг в пределах 3x3 клеток сильнее друзей:
    engage_danger = 0
    # Размер тайла -- 5 футов (1.5 метра):
    tile_size = 5
    namedtuple_squad = namedtuple('squad',['zone','type','initiative'])
    namedtuple_commander = namedtuple('commander',['place','danger','uuid'])
    # Слоу-поиск пути, AStarFinder (100 бойцов на отряд):
    slow_path_max = 100
    # Подключаемся к базе данных солдат:
    database = database.database()
    ally_zones = ['zone_0','zone_1','zone_2','zone_3','zone_4']
    enemy_zones = ['zone_5','zone_6','zone_7','zone_8','zone_9']
    # Опыт от показателя опасности:
    challenge_rating_experience_dict = {
            '0':10,
            '1/8':25,
            '1/4':50,
            '1/2':100,
            '1':200,
            '2':450,
            '3':700,
            '4':1100,
            '5':1800,
            '6':2300,
            '7':2900,
            '8':3900,
            '9':5000,
            '10':5900,
            '11':7200,
            '12':8400,
            '13':10000,
            '14':11500,
            '15':13000,
            '16':15000,
            '17':18000,
            '18':20000,
            '19':22000,
            '20':25000,
            '21':33000,
            '22':41000,
            '23':50000,
            '24':62000,
            '25':75000,
            '26':90000,
            '27':105000,
            '28':120000,
            '29':135000,
            '30':155000,
            }

    def prepare_battlefield(self, battle_map, zones_squads_dict):
        """Подготовка поля боя.
        
        - Создание поля боя.
        - Генерация отрядов.
        - Размещение солдат.
        """
        self.create_battlespace(battle_map)
        self.squads = self.create_squads(zones_squads_dict)
        self.metadict_soldiers = self.create_metadict_soldiers(self.squads)
        self.place_soldiers()
        for key,squad in self.squads.items():
            self.set_squad_battle_order(squad, key.zone)
            #[print(el) for el in squad.battle_order.items()]
            for soldier in squad.metadict_soldiers.values():
                soldier.set_actions_base(squad)
                soldier.set_actions(squad)
        # Подготовка к бою (бонусные хиты, заклинания, отдых и лечение):
        for key,squad in self.squads.items():
            self.set_squad_heal(squad)
            self.set_squad_bonus_hitpoints(squad)
            self.set_squad_bardic_inspiration(squad)
            self.set_squad_spell_bless(squad)
            # Короткий отдых:
            if namespace.short_rest:
                self.set_squad_short_rest(squad)
        # Вывод карты до начала боя:
        #print_ascii_map(battle.gen_battlemap())

    def create_squads(self, zones_squads_dict):
        """Создаём отряды.
        
        Солдаты в отрядах узнают своих и врагов.
        Командиры бросают кости инициативы, определяя порядок ходов.
        В вывод словарь отрядов, отсортированный в порядке командирской инициативы.
        """
        squads_list_types = list(sorted(squads.metadict_squads.keys()))
        squads_list_DB = self.database.print_squads()
        ready_squads = {}
        for zone, squad_type in zones_squads_dict.items():
            squad = squad_generation()
            if squad_type in squads_list_types:
                squad.create_squad(squad_type)
            elif squad_type in squads_list_DB:
                squad.load_squad_from_DB(squad_type, namespace.injured)
            if zone in self.ally_zones:
                squad.set_ally_side(self.ally_side)
                squad.set_enemy_side(self.enemy_side)
            elif zone in self.enemy_zones:
                squad.set_ally_side(self.enemy_side)
                squad.set_enemy_side(self.ally_side)
            squad.set_hitpoints()
            squad.set_initiative()
            squad.initiative = squad.throw_squad_initiative()
            squad_tuple = self.namedtuple_squad(zone, squad_type, squad.initiative)
            ready_squads[squad_tuple] = squad
        # Отряды сортированы в порядке командирских бросков инициативы:
        ready_squads = OrderedDict(reversed(sorted(ready_squads.items(),key=lambda x: x[0].initiative)))
        return ready_squads

    def create_metadict_soldiers(self, squads):
        """Общий словарь всех бойцов на поле боя."""
        metadict_soldiers = {}
        for squad in squads.values():
            metadict_soldiers.update(squad.metadict_soldiers)
        return metadict_soldiers

    def place_soldiers(self):
        """Размещаем метки бойцов на карте.
        
        Каждая метка, это кортеж со стороной юнита, его типом и uuid.
        """
        # Перемешиваем пункты спавна, чтобы получился разомкнутый строй:
        spawn_list = list(self.spawn_list)
        random.shuffle(spawn_list)
        # Размещаем солдат (если точка не занята):
        for key, squad in self.squads.items():
            for spawn_point in spawn_list:
                if spawn_point.zone == key.zone:
                    for n,uuid in enumerate(squad.soldiers_list):
                        if squad.metadict_soldiers[uuid].behavior == spawn_point.type:
                            if not tuple in [type(el) for el in self.dict_battlespace[spawn_point.place]]:
                                # Извлекаем ключ по номеру:
                                uuid = squad.soldiers_list.pop(n)
                                # Вытаскиваем данные по ключу:
                                soldier = squad.metadict_soldiers[uuid]
                                # Размещаем лошадей, если таковые есть:
                                if hasattr(soldier, 'mount_uuid')\
                                        and soldier.mount_combat == True\
                                        and soldier.mount_uuid in squad.metadict_soldiers:
                                    mount = squad.metadict_soldiers[soldier.mount_uuid]
                                    mount_tuple = (squad.ally_side, mount.behavior, mount.uuid)
                                    # Лошади крупные создания, занимают 2x2 тайла:
                                    mount_place_field = self.point_to_field_2x2(spawn_point.place)
                                    for point in mount_place_field:
                                        if point in self.dict_battlespace:
                                            self.dict_battlespace[point].append(mount_tuple)
                                    # А ещё лошадки высокие, что позволяет смотреть далеко:
                                    self.dict_battlespace[spawn_point.place].append('mount_height')
                                    squad.metadict_soldiers[mount.uuid].set_coordinates(spawn_point.place)
                                # TODO: Сделай нормальный поиск по namedtuple.
                                # ------------------------------------------------------------
                                # Сейчас бойцы на карте ищутся перебором type(tuple), это неэффективно.
                                # Проблема в том, что namedtuple не определяется как обычный кортеж
                                # ------------------------------------------------------------
                                #soldier_tuple = self.namedtuple_soldier(side,behavior,uuid)
                                soldier_tuple = (squad.ally_side, soldier.behavior, soldier.uuid)
                                # Дополняем словарь поля боя и вырубаем цикл, так как спавн занят:
                                if soldier.size == 'medium' or soldier.size == 'small':
                                    self.dict_battlespace[spawn_point.place].append(squad.ally_side)
                                    self.dict_battlespace[spawn_point.place].append(soldier_tuple)
                                # Большие существа занимают 2x2 тайла:
                                elif soldier.size == 'large':
                                    soldier_place_field = self.point_to_field_2x2(spawn_point.place)
                                    for point in soldier_place_field:
                                        if point in self.dict_battlespace:
                                            self.dict_battlespace[point].append(soldier_tuple)
                                            self.dict_battlespace[point].append(squad.ally_side)
                                            self.dict_battlespace[point].append('mount_height')
                                # Даём бойцу его координаты:
                                squad.metadict_soldiers[uuid].set_coordinates(spawn_point.place)
                                break

    def set_squad_battle_order(self, squad, squad_zone):
        """Солдаты запоминают своё положение в строю относительно командира.
        
        battle_order, это не сами координаты, а смещение по осям координат.
        """
        # Точка отсчёта -- позиция командира отряда:
        guiding_point = None
        for soldier in squad.metadict_soldiers.values():
            if hasattr(soldier, 'place') and soldier.place and soldier.behavior == 'commander':
                guiding_point = soldier.place
                break
            #elif hasattr(soldier, 'place') and soldier.place:
            #    guiding_point = soldier.place
            #    break
        # Создаём боевой порядок на основе точек спавна:
        squad.battle_order = {}
        for point, descript in self.dict_battlespace.items():
            if squad_zone in descript and 'spawn' in descript:
                for spawn_type in self.spawn_types:
                    if spawn_type in descript:
                        x_relativ = point[0] - guiding_point[0]
                        y_relativ = point[1] - guiding_point[1]
                        place_in_order = (x_relativ, y_relativ)
                        squad.battle_order[place_in_order] = (spawn_type, None)
        # Отмечаем присутствующих солдат в боевом порядке:
        for soldier in squad.metadict_soldiers.values():
            if hasattr(soldier, 'place') and soldier.place and guiding_point:
                x_relativ = soldier.place[0] - guiding_point[0]
                y_relativ = soldier.place[1] - guiding_point[1]
                place_in_order = (x_relativ, y_relativ)
                # Запоминаем положение всех бойцов на начало боя:
                squad.battle_order[place_in_order] = (soldier.behavior, soldier.uuid)
                # Солдат узнаёт своё место в строю (это ключевое):
                soldier.set_place_in_order(place_in_order)
                #print(soldier.behavior,soldier.place, soldier.place_in_order)

    def set_squad_heal(self, squad):
        """Лекари поднимают на ноги павших бойцов (ключ -I при запуске)

        Feat_Healer:
        - стабилизация раненого возвращает ему 1 hp.
        - перевязка на 1d6+4 + максимум_кости_хитов
        - только одна перевязка перед коротким/продолжительным отдыхом.
        """
        bless_list = []
        bless_type = 'treated'
        for soldier in squad.metadict_soldiers.values():
            if soldier.class_features.get('Feat_Healer'):
                bless_list.append(dices.dice_throw_advantage("1d6") + 4)
        soldiers_list_elite = self.select_soldiers_for_bless(
                len(self.metadict_soldiers), squad.ally_side, bless_type)
        # Лечим раненых:
        for soldier in soldiers_list_elite:
            if not soldier.disabled and not soldier.death:
                if bless_list and soldier.hitpoints <= soldier.hitpoints_max / 2:
                    max_hit_dice = int(soldier.hit_dice.split('d')[1])
                    heal = bless_list.pop() + max_hit_dice
                    soldier.set_hitpoints(heal = heal)
                    soldier.treated = True
                    soldier.fall = False
                    print('{side} Feat_Healer, {p} {b} {n} heal: {hit}/{hit_max} ({heal})'.format(
                        side = soldier.ally_side,
                        p = soldier.place,
                        b = soldier.behavior,
                        n = soldier.name,
                        hit = soldier.hitpoints,
                        hit_max = soldier.hitpoints_max,
                        heal = heal,
                        ))

    def set_squad_bonus_hitpoints(self, squad):
        """Бонусные хиты от способности командира.
        
        Feat_Inspiring_Leader (бонус уровня и харизмы во временные хиты):
        - 4 офицера = 24 бойца = плюс 6-7 хитов каждому (150-170 хитов на роту)
        Бонусные хиты раздаются сразу всей союзной армии, сначала элите, потом рядовым.
        """
        # TODO: отключение способности через soldier.inspiring_leader некрасиво сделано.
        # inspiring_leader должен восстанавливаться после короткого отдыха.
        # А также требует 10 минут выступления.
        bless_list = []
        bless_type = 'bonus_hitpoints'
        for soldier in squad.metadict_soldiers.values():
            if hasattr(soldier, 'inspiring_leader') and soldier.inspiring_leader:
                for n in range(0, 6):
                    bonus_hitpoints = soldier.mods['charisma'] + soldier.level
                    bless_list.append(bonus_hitpoints)
                soldier.inspiring_leader = False
        soldiers_list_elite = self.select_soldiers_for_bless(
                len(bless_list), squad.ally_side, bless_type)
        # Наконец, раздаём бонусные хиты:
        for soldier in soldiers_list_elite:
            if bless_list:
                soldier.set_hitpoints(bonus_hitpoints = bless_list.pop())
                #print('{side} Feat_Inspiring_Leader, {p} {b} {n} bonus_hitpoints: {hitpoints}/{hitpoints_max} ({hitpoints_bonus})'.format(
                #    side = soldier.ally_side,
                #    p = soldier.place,
                #    b = soldier.behavior,
                #    n = soldier.name,
                #    hitpoints = soldier.hitpoints + soldier.bonus_hitpoints,
                #    hitpoints_max = soldier.hitpoints_max,
                #    hitpoints_bonus = soldier.bonus_hitpoints,
                #    ))

    def set_squad_bardic_inspiration(self, squad):
        """Барды дают бонус к атаке или спасброску вдохновлённых бойцов.
        
        Один бард может раздать вдохновение нескольким союзникам.
        """
        bless_list = []
        bless_type = 'bardic_inspiration'
        for soldier in squad.metadict_soldiers.values():
            if hasattr(soldier, 'inspiring_bard_number') and soldier.inspiring_bard_number:
                for n in range(0, soldier.inspiring_bard_number):
                    bless_list.append(dices.dice_throw_advantage(soldier.inspiring_bard_dice))
                soldier.inspiring_bard_number = 0
        soldiers_list_elite = self.select_soldiers_for_bless(
                len(bless_list), squad.ally_side, bless_type)
        for soldier in soldiers_list_elite:
            if bless_list:
                soldier.bardic_inspiration = bless_list.pop()
                #print(soldier.rank, soldier.bardic_inspiration)

    def set_squad_spell_bless(self, squad):
        """Заклинание "Благословение" (Bless)"""
        bless_list = []
        bless_type = 'bless'
        for soldier in squad.metadict_soldiers.values():
            if hasattr(soldier, 'spells') and soldier.spells_generator.find_spell('Bless'):
                spell_dict = soldier.set_bless()
                for n in range(0, spell_dict['attacks_number']):
                    bless_list.append(dices.dice_throw_advantage(spell_dict['damage_dice']))
        soldiers_list_elite = self.select_soldiers_for_bless(
                len(bless_list), squad.ally_side, bless_type)
        for soldier in soldiers_list_elite:
            if bless_list:
                soldier.bless = bless_list.pop()
                soldier.bless_timer = spell_dict['effect_timer']

    def select_soldiers_for_bless(self, number, ally_side, bless_type):
        """Выбираем солдат для Bless, Inspiring_Leader, Bardic_Inspiration и т.д.
        
        Сначала офицеры, затем ветераны, после обычные бойцы.
        Ездовых животных не выбираем.
        """
        soldiers_list = [ ] 
        max_level = max([soldier.level for soldier in self.metadict_soldiers.values()])
        for level in reversed(range(0, max_level +1)):
            for soldier in self.metadict_soldiers.values():
                if not number <= 0\
                        and not soldier.behavior == 'mount'\
                        and not soldier.__dict__.get(bless_type)\
                        and soldier.ally_side == ally_side\
                        and soldier.level == level:
                    soldiers_list.append(soldier)
                    number -= 1
        return soldiers_list

    def set_squad_short_rest(self, squad):
        """Короткий отдых (1 час).

        """
        # TODO: Короткий отдых восстанавливает способности:
        # - способности бойца
        # - заклинания колдуна
        # - перевязку можно повторить
        bless_type = 'short_rest'
        soldiers_list_elite = self.select_soldiers_for_bless(
                len(squad.metadict_soldiers), squad.ally_side, bless_type)
        for soldier in soldiers_list_elite:
            soldier.set_short_rest_heal()
            soldier.set_short_rest_restoration()

    def set_squad_battle_stat(self, attack_result, squad, attack_choice = None):
        """Подсчёт попадания, промахов и урона под каждый вид оружия."""
        if not hasattr(squad, 'battle_stat'):
            squad.battle_stat = {}
        if not attack_choice:
            attack_choice = attack_result['attack_choice']
        attack_key_hit = tuple(list(attack_choice) + ['hit'])
        attack_key_fatal = tuple(list(attack_choice) + ['fatal'])
        attack_key_miss = tuple(list(attack_choice) + ['miss'])
        attack_key_damage = tuple(list(attack_choice) + ['damage'])
        attack_key_shield_impact = tuple(list(attack_choice) + ['shield_impact'])
        attack_key_hit_friendly = tuple(list(attack_choice) + ['damage_friend'])
        if attack_result.get('hit')\
                and not attack_result.get('victim_side') == squad.ally_side:
            if not attack_key_damage in squad.battle_stat and attack_result['damage'] > 0:
                squad.battle_stat[attack_key_damage] = attack_result['damage']
            elif attack_key_damage in squad.battle_stat and attack_result['damage'] > 0:
                squad.battle_stat[attack_key_damage] += attack_result['damage']
            if not attack_key_hit in squad.battle_stat:
                squad.battle_stat[attack_key_hit] = 1
            else:
                squad.battle_stat[attack_key_hit] += 1
        # Учитывем дружественный огонь:
        elif attack_result.get('hit')\
                and attack_result.get('victim_side') == squad.ally_side:
            if not attack_key_hit_friendly in squad.battle_stat and attack_result['damage'] > 0:
                squad.battle_stat[attack_key_hit_friendly] = attack_result['damage']
            elif attack_key_damage in squad.battle_stat and attack_result['damage'] > 0:
                squad.battle_stat[attack_key_hit_friendly] += attack_result['damage']
            if not attack_key_hit in squad.battle_stat:
                squad.battle_stat[attack_key_hit] = 1
            else:
                squad.battle_stat[attack_key_hit] += 1
        else:
            if not attack_key_miss in squad.battle_stat:
                squad.battle_stat[attack_key_miss] = 1
            else:
                squad.battle_stat[attack_key_miss] += 1
        # Пилумы ломают щиты (-1 AC с каждым попаданием):
        if attack_result.get('shield_impact') and attack_result.get('shield_breaker'):
            if not attack_key_shield_impact in squad.battle_stat:
                squad.battle_stat[attack_key_shield_impact] = 1
            else:
                squad.battle_stat[attack_key_shield_impact] += 1
        if attack_result.get('fatal_hit'):
            if not attack_key_fatal in squad.battle_stat:
                squad.battle_stat[attack_key_fatal] = 1
            else:
                squad.battle_stat[attack_key_fatal] += 1
        #print(squad.battle_stat)
        # Красивый вывод данных:
        if attack_result.get('fatal_hit'):
            attack_choice = attack_result['attack_choice']
            soldier = self.metadict_soldiers[attack_result['sender_uuid']]
            enemy_soldier = self.metadict_soldiers[attack_result['victim_uuid']]
            print('{side}, {c1} {s} {w} >> {c2} {e}, hit {h}, fall {f}'.format(
                side = enemy_soldier.enemy_side,
                s = soldier.behavior,
                e = enemy_soldier.behavior,
                c1 = soldier.place,
                c2 = enemy_soldier.place,
                w = attack_choice,
                h = attack_result['hit'],
                f = attack_result['fatal_hit'],
                ))
            if namespace.visual:
                time.sleep(0.2)

    def start (self, max_rounds = 10, commands = False):
        """Начинаем бой."""
        for battle_round in range(1, max_rounds +1):
            # Измеряем время раунда:
            start = timeit.default_timer()
            # Чистим карту от павших в прошлом раунде:
            self.clear_battlemap()
            for squad in self.squads.values():
                # Тяжелораненые могут погибнуть:
                self.fall_to_death(squad)
                # Отряд делает ход:
                self.round_run_squad(squad, commands)
                # Выводим карту после хода каждого отряда:
                print_ascii_map(self.gen_battlemap())
                time.sleep(0.2)
            stop = timeit.default_timer()
            print('round end:', battle_round, 'time:', round(stop - start, 3))
            # Подкрепления в конце хода (кому не хватило точек спавна):
            if namespace.reinforce:
                self.place_soldiers()
        # Уточняем потери по результатам боя:
        for squad in self.squads.values():
            self.fall_to_death(squad)
            squad.casualty = self.calculate_casualty(squad)

    def round_run_squad(self, squad, commands = False):
        """Ход отряда."""
        # Список команд на текущий ход:
        self.set_squad_command_and_control(squad)
        squad.commands = self.squad_AI(squad, squad.commander, commands)
        # Боец действует, только если он находится на карте и боеспособен:
        for uuid, soldier in squad.metadict_soldiers.items():
            if soldier.get_coordinates() and soldier.hitpoints > 0\
                    and not soldier.sleep and not soldier.defeat:
                self.round_run_soldier(soldier, squad)

    def set_squad_command_and_control(self, squad):
        """Работает командование отряда:
        
        - Командиры отмечают видимых врагов.
        - По зонам вокруг видимых врагов размечается линия фронта.
        - Данные по врагу обобщаются (дистанция, число, вооружение).
        - Отмечаются зоны концентрации врага для града стрел.
        """
        # Ограничиваем поиск пути:
        squad.slow_path_uses = 0
        squad.slow_path_max = self.slow_path_max
        # Список командиров, их координат и уровней опасности:
        squad.commanders_list = self.commanders_to_list(squad)
        squad.casualty = self.calculate_casualty(squad)
        squad.enemies = None
        squad.frontline = None
        squad.commander = None
        squad.moral = 0
        if squad.commanders_list:
            # Командир -- первый из списка офицеров:
            squad.commander = squad.metadict_soldiers[squad.commanders_list[0].uuid]
            # Командиры ищут видимых врагов и чертят по ним линию фронта:
            squad.allies = self.commanders_seek_allies(squad)
            squad.enemies = self.commanders_seek_enemies(squad)
            squad.frontline = self.draw_frontline(squad.enemies)
            if squad.enemies:
                # Разведка противника, обобщение данных:
                squad.enemy_recon = self.recon_enemy_side(squad.enemies, squad.allies)
                # Зоны концентрации врага с точки зрения командира:
                squad.danger_points = battle.find_danger_zones(
                        squad.enemy_side, zone_length = 2,
                        soldier_coordinates = squad.commanders_list[0].place)
            else:
                squad.enemy_recon = None
                # Зоны концентрации врага с точки зрения мимо пролетавшей сороки:
                squad.danger_points = battle.find_danger_zones(squad.enemy_side, zone_length = 5)
            # Командиры отряда поддерживают его мораль:
            squad.moral = squad.throw_squad_moral(squad.enemy_recon, squad.commanders_list)

    def commanders_to_list(self, squad):
        """Командиры возвращают свои координаты и уровень опасности рядом."""
        #commanders_list = [soldier for soldier in squad.metadict_soldiers.values()\
        #        if soldier.behavior == 'commander']
        commanders_list = []
        for uuid, soldier in squad.metadict_soldiers.items():
            if hasattr(soldier, 'place')\
                    and soldier.hitpoints > 0\
                    and soldier.behavior == 'commander'\
                    and soldier.escape != True:
                commander_tuple = self.namedtuple_commander(soldier.place,soldier.danger,soldier.uuid)
                commanders_list.append(commander_tuple)
        return commanders_list

    def commanders_seek_enemies(self, squad):
        """Командиры отряда находят видимых врагов."""
        dict_enemies = {}
        for commander_tuple in squad.commanders_list:
            commander = squad.metadict_soldiers[commander_tuple.uuid]
            dict_enemies.update(self.find_visible_soldiers(
                    commander.place, commander.enemy_side,
                    max_number = 30, max_try = 60))
        dict_enemies = OrderedDict(sorted(dict_enemies.items(),key=lambda x: x[1].distance))
        return dict_enemies

    def commanders_seek_allies(self, squad):
        """Командиры отряда находят видимых союзников."""
        dict_allies = {}
        for commander_tuple in squad.commanders_list:
            commander = squad.metadict_soldiers[commander_tuple.uuid]
            dict_allies.update(self.find_visible_soldiers(
                    commander.place, commander.ally_side,
                    max_number = 30, max_try = 60))
        dict_allies = OrderedDict(sorted(dict_allies.items(),key=lambda x: x[1].distance))
        return dict_allies

    def draw_frontline(self, dict_enemies):
        """Командиры отряда отмечают точки линии фронта.
        
        Линия фронта, это незанятые точки рядом с видимыми бойцами врага.
        """
        frontline = []
        target_points = []
        for target in dict_enemies.values():
            target_points.append(target.place)
            frontline.extend(self.point_to_field(target.place))
            frontline = list(set(frontline))
        frontline = list(set(frontline) - set(target_points))
        return frontline

    def calculate_casualty(self, squad):
        """Статистика отряда, убитые и раненые:"""
        dict_casualty = {
                'dead':0,
                'disabled':0,
                'captured':0,
                'fall':0,
                'injured':0,
                'light_injured':0,
                'escape':0,
                'lucky_one':0,
                }
        for soldier in squad.metadict_soldiers.values():
            if soldier.hitpoints <= 0:
                dict_casualty['fall'] += 1
                if hasattr(soldier, 'death') and soldier.death == True:
                    dict_casualty['dead'] += 1
                elif hasattr(soldier, 'disabled') and soldier.disabled == True:
                    dict_casualty['disabled'] += 1
                elif hasattr(soldier, 'captured') and soldier.captured == True:
                    dict_casualty['captured'] += 1
            elif soldier.escape:
                dict_casualty['escape'] += 1
            elif soldier.hitpoints <= round(soldier.hitpoints_max / 2):
                dict_casualty['injured'] += 1
            elif soldier.hitpoints < soldier.hitpoints_max:
                dict_casualty['light_injured'] += 1
            else:
                dict_casualty['lucky_one'] += 1
        soldiers_number = len(squad.metadict_soldiers)
        dict_casualty['fall_percent'] = round(dict_casualty['fall'] / soldiers_number * 100)
        dict_casualty['dead_percent'] = round(dict_casualty['dead'] / soldiers_number * 100)
        dict_casualty['disabled_percent'] = round(dict_casualty['disabled'] / soldiers_number * 100)
        dict_casualty['captured_percent'] = round(dict_casualty['captured'] / soldiers_number * 100)
        dict_casualty['injured_percent'] = round(dict_casualty['injured'] / soldiers_number * 100)
        dict_casualty['light_injured_percent'] = round(dict_casualty['light_injured'] / soldiers_number * 100)
        dict_casualty['escape_percent'] = round(dict_casualty['escape'] / soldiers_number * 100)
        dict_casualty['lucky_one_percent'] = round(dict_casualty['lucky_one'] / soldiers_number * 100)
        # Потери отряда, это павшие в бою и бежавшие с поля боя (это учитывается в soldier.set_danger):
        dict_casualty['casualty_percent'] = dict_casualty['fall_percent'] + dict_casualty['escape_percent']
        return dict_casualty

    def recon_enemy_side(self, enemies_dict, allies_dict):
        """Изучаем видимых противников, делаем выводы.
        
        Ключевое:
        - средняя скорость врага.
        - средняя дистанция до врага.
        - тип и класс самых многочисленных бойцов.
        - распространённые атаки (ranged, throw, reach)
        """
        enemy_recon = {}
        speed_list = []
        types_list = []
        clases_list = []
        distance_list = []
        attacks_list = []
        danger_list = []
        ally_strenght_list = []
        attacks_sense_limit = 0.25
        for uuid, enemy_tuple in enemies_dict.items():
            enemy_soldier = self.metadict_soldiers[uuid]
            # Смотрим, не на коне ли враг:
            if hasattr(enemy_soldier, 'mount_uuid')\
                    and enemy_soldier.mount_combat == True\
                    and self.metadict_soldiers.get(enemy_soldier.mount_uuid)\
                    and self.metadict_soldiers[enemy_soldier.mount_uuid].place == enemy_soldier.place:
                speed_list.append(self.metadict_soldiers[enemy_soldier.mount_uuid].base_speed)
            else:
                speed_list.append(enemy_soldier.base_speed)
            distance_list.append(enemy_tuple.distance)
            types_list.append(enemy_soldier.behavior)
            clases_list.append(enemy_soldier.char_class)
            danger_list.append(self.dict_danger[enemy_soldier.behavior])
            attacks_types = set([key[0] for key in enemy_soldier.attacks.keys()])
            attacks_list.extend(attacks_types)
        for uuid, ally_tuple in allies_dict.items():
            ally_soldier = self.metadict_soldiers[uuid]
            ally_strenght_list.append(self.dict_danger[ally_soldier.behavior])
        # Словари. Число вражеских бойцов по типам и классам персонажей, их атаки:
        enemy_types_dict = collections.Counter(types_list)
        enemy_classes_dict = collections.Counter(clases_list)
        enemy_attacks_dict = collections.Counter(attacks_list)
        # Знание о собственном отряде и соседях:
        enemy_recon['ally_number'] = len(allies_dict)
        enemy_recon['ally_strenght'] = sum(ally_strenght_list)
        # Типы вражеских атак (редкие не учитываем):
        enemy_recon['enemy_number'] = len(enemies_dict)
        enemy_recon['enemy_strenght'] = sum(danger_list)
        enemy_recon['attacks'] = [key for key in enemy_attacks_dict.keys()\
                if enemy_attacks_dict[key] >= len(enemies_dict) * attacks_sense_limit]
        # Выбор наиболее частого типа и класса бойцов:
        enemy_recon['type'] = max(enemy_types_dict, key=lambda key: enemy_types_dict[key])
        enemy_recon['class'] = max(enemy_classes_dict, key=lambda key: enemy_classes_dict[key])
        # Средняя скорость и длина хода врага:
        medial_speed = sum(speed_list) / len(enemies_dict)
        enemy_recon['move'] = round(medial_speed / self.tile_size)
        # Средняя дистанция до врага:
        enemy_recon['distance_medial'] = round(sum(distance_list) / len(enemies_dict))
        enemy_recon['distance'] = min(distance_list)
        return enemy_recon

    def squad_AI(self, squad, commander, commands):
        """Создаёт список команд на ход."""
        commands_list = []
        if squad.commander and squad.enemies:
            save_distance = squad.enemy_recon['move']
            if squad.enemy_recon['distance'] > save_distance:
                commands_list = ['lead','follow']
                commands_list.append('attack')
                commands_list.append('spellcast')
            elif squad.enemy_recon['distance'] <= save_distance:
                commands_list = ['lead','follow','engage']
                commands_list.append('attack')
                commands_list.append('spellcast')
        elif squad.commander and not squad.enemies:
            commands_list = ['lead','follow']
        elif not squad.commander:
            # TODO: вот здесь-то и нужен рассчёт потерь в отряде:
            # И выбор 'retreat', если всё совсем плохо.
            #commands_list = ['seek','engage','attack']
            # TODO: disengage использует squad.enemy_recon.
            # А разведка противника не обновляется без командира.
            commands_list = ['disengage','dodge','attack']
            #commands_list = ['retreat']
        if squad.commander:
            # Бесстрашные создания бесстрашны, зато трусоватые спасают своих:
            if squad.commander.__dict__.get('fearless'):
                commands_list.append('fearless')
            else:
                commands_list.append('rescue')
            # Лучники и метатели дротиков должны чуть что отступать:
            if squad.behavior == 'archer':
                #commands_list.append('seek')
                commands_list.append('volley')
                commands_list.append('spellcast')
                commands_list.append('fireball')
                if 'engage' in commands_list:
                    commands_list.remove('engage')
                    commands_list.append('disengage')
                if squad.enemies and squad.enemy_recon['distance'] <= save_distance * 2:
                    commands_list.remove('lead')
                    commands_list.append('dodge')
            # Бойцы у нас кавалерия:
            #if commander.char_class == 'Fighter' or commander.char_class == 'Barbarian':
            #    commands_list.append('fearless')
        if commands:
            # Ручной ввод команд отряду, если симуляция запущена с ключом --commands
            if not hasattr(squad, 'commands_manual') or not 'auto' in squad.commands_manual:
                print(squad.ally_side, squad.squad_type, commands_list)
                commands_input = list(input('---Команды отряду ("auto" -- выход): ').split())
                if commands_input:
                    squad.commands_manual = commands_input
            if hasattr(squad, 'commands_manual') and squad.commands_manual:
                for command in squad.commands_manual:
                    if command[0] == '-':
                        command = command[1:]
                        if command in commands_list:
                            commands_list.remove(command)
                    elif command not in commands_list:
                        commands_list.append(command)
            print(squad.ally_side, squad.squad_type, commands_list)
        return commands_list

    def round_run_soldier(self, soldier, squad):
        """Ход отдельного бойца."""
        # Разрешаем battle_action, move_action и т.д.
        soldier.set_actions(squad)
        # Запоминаем все точки вокруг, не занятые непроходимой местностью или границами зон:
        # Находим противников и союзников в области 5 футов, 3x3 клетки:
        # Крупные создания осматривают большую зону вокруг себя.
        if soldier.size == 'large':
            soldier_tuple = (squad.ally_side, soldier.behavior, soldier.uuid)
            soldier_place_field = self.point_to_field_2x2(soldier.place)
            recon_near = {}
            near_zone = []
            for point in soldier_place_field:
                if point in self.dict_battlespace and\
                        soldier_tuple in self.dict_battlespace[point]:
                    recon_near.update(self.recon(point, distance = 1))
                    near_zone.extend(self.find_points_in_zone(point, distance = 1))
            near_zone = list(set(near_zone))
        else:
            near_zone = self.find_points_in_zone(soldier.place, distance = 1)
            recon_near = self.recon(soldier.place, distance = 1)
        soldier.near_zone = near_zone
        soldier.set_near_allies(recon_near)
        soldier.set_near_enemies(recon_near)
        enemy = self.find_enemy(soldier, squad)
        # Работает страхочуйка и мораль бойца:
        soldier.set_danger(self.recon_action_danger(soldier, recon_near), squad)
        #if soldier.danger > 0:
        #    print('{0} {1} {2} hp {3}/{4} danger {5}'.format(
        #    soldier.ally_side, soldier.place, soldier.rank,
        #    soldier.hitpoints, soldier.hitpoints_max, soldier.danger))
        # Бойцы отступают и лечатся зельями, если это необходимо:
        if soldier.hitpoints <= soldier.hitpoints_max / 2:
            destination = self.find_spawn(soldier.place, soldier.ally_side)
            destination = random.choice(self.point_to_field(destination))
            self.move_action(soldier, squad, destination, allow_replace = True)
            if soldier.second_wind:
                soldier.set_second_wind()
            elif soldier.lay_on_hands:
                soldier.set_lay_of_hands()
            elif soldier.equipment_weapon.get('Infusion of Healing'):
                soldier.use_potion_of_healing()
        # Солдат отступает, если опасность слишком велика:
        if soldier.danger > self.engage_danger or 'retreat' in squad.commands:
            destination = self.find_spawn(soldier.place, soldier.ally_side)
            destination = random.choice(self.point_to_field(destination))
            self.move_action(soldier, squad, destination, allow_replace = False)
            # Испуганный боец может сбежать (но у храброго преимущество):
            if "brave" in squad.commands:
                soldier.escape = soldier.morality_check_escape(soldier.danger, advantage = True)
            else:
                soldier.escape = soldier.morality_check_escape(soldier.danger)
            # Командир может отступить в глубину строя:
            if soldier.behavior == 'commander' or 'retreat' in squad.commands:
                self.move_action(soldier, squad, destination, allow_replace = True)
            if soldier.escape or 'retreat' in squad.commands:
                soldier.escape = True
                self.move_action(soldier, squad, destination, allow_replace = True)
                if 'spawn' in self.dict_battlespace[soldier.place]:
                    self.clear_battlemap()
        # Отряд может ускориться с dash_action, если таков приказ (и врагов нет рядом):
        if 'dash' in squad.commands:
            if not enemy or enemy.distance >= soldier.move_pool / 2:
                self.dash_action(soldier)
        # Командир отряда может вести бойцов в ручном режиме:
        if 'move' in squad.commands and not 'auto' in squad.commands\
                and soldier.uuid == squad.commander.uuid:
            destination = list(input('---Куда идти? ("10 10", это x=10, y=10): ').split())
            destination = tuple([int(el) for el in destination])
            if destination and len(destination) > 1:
                squad.destination = destination
                self.move_action(soldier, squad, destination, allow_replace = True)
        # Командир ведёт бойцов автоматически, но не вырывается впереди строя:
        if 'lead' in squad.commands and soldier.behavior == 'commander':
            if len(soldier.near_allies) >= 2 or 'fearless' in squad.commands:
                if hasattr(squad, 'destination') and squad.destination\
                        and not 'auto' in squad.commands:
                    self.move_action(soldier, squad, squad.destination, allow_replace = True)
                elif enemy and 'dodge' in squad.commands:
                    self.move_action(soldier, squad, enemy.place, allow_replace = False)
                elif enemy:
                    self.move_action(soldier, squad, enemy.place, allow_replace = True)
                else:
                    destination = self.find_spawn(soldier.place, soldier.enemy_side)
                    self.move_action(soldier, squad, destination, allow_replace = True)
        # Оборонительная тактика, если таков приказ (вторые ряды всё же атакуют):
        if 'dodge' in squad.commands and soldier.near_enemies\
                or soldier.danger > self.engage_danger:
            self.dodge_action(soldier)
        # Простые солдаты следуют за командиром, зная своё место в строю:
        if 'follow' in squad.commands and squad.commander and not soldier.near_enemies:
            self.follow_action(soldier, squad, squad.commander)
        # Боец наступает, если союзники рядом сильнее противника в точке назначения:
        if 'engage' in squad.commands and enemy and not soldier.near_enemies:
            self.engage_action(soldier, squad, enemy, recon_near)
        # Кастеры работают магией, сначала по группам, а потом целевой:
        if 'spellcast' in squad.commands and enemy:
            recon_near = self.recon(soldier.place, distance = 1)
            soldier.set_near_enemies(recon_near)
            soldier.set_danger(self.recon_action_danger(soldier, recon_near), squad)
            if soldier.danger <= 0 or 'fearless' in squad.commands:
                self.fireball_action(soldier, squad)
                self.spellcast_action(soldier, squad, enemy)
        # Атака следует за 'engage', поэтому осматриваемся снова:
        if 'attack' in squad.commands and enemy:
            recon_near = self.recon(soldier.place, distance = 1)
            soldier.set_near_enemies(recon_near)
            soldier.set_danger(self.recon_action_danger(soldier, recon_near), squad)
            if soldier.danger <= 0 or 'fearless' in squad.commands:
                self.attack_action(soldier, squad, enemy)
                if 'engage' in squad.commands\
                        and not 'dodge' in squad.commands\
                        and not 'disengage' in squad.commands:
                    self.engage_action(soldier, squad, enemy, recon_near)
            # Удвоенный ход бойца:
            if soldier.action_surge and len(soldier.near_enemies) >= 2:
                if soldier.set_action_surge():
                    self.round_run_soldier(soldier, squad)
        # Не видя врага, лучники стреляют навесом:
        if 'volley' in squad.commands and not enemy and soldier.behavior == 'archer':
            self.volley_action(soldier, squad)
        # Лучники отступают, если враг близко:
        if 'disengage' in squad.commands and enemy and enemy.distance <= squad.enemy_recon['move'] * 2:
            destination = self.find_spawn(soldier.place, soldier.ally_side)
            self.move_action(soldier, squad, destination, allow_replace = True)
        # Если действия таки не использовались -- защищаемся:
        if soldier.battle_action or soldier.bonus_action:
            self.dodge_action(soldier)

    def recon_action_danger(self, soldier, recon_near = None):
        """Оценка опасности ближней зоны"""
        if not recon_near:
            recon_near = self.recon(soldier.place, distance = 2)
        danger = self.danger_sense(recon_near, soldier.enemy_side)
        # TODO: Кучи павших своих, это объективный показатель угрозы:
        # Но лучше подсчитывать это в soldier.set_danger
        # На самом деле редкое явление, тяжелораненых вытаскивают.
        for point in soldier.near_zone:
            if soldier.ally_side in self.dict_battlespace[point]:
                for descript in self.dict_battlespace[point]:
                    if descript == 'fall_place':
                        danger +=1
        return danger

    def follow_action(self, soldier, squad, commander):
        """Солдат следует за командиром, стараясь держать строй.
        
        Как это работает:
        - Боец знает своё место в строю относительно командира.
        - Если у него нет места, он выбирает свободное из доступных.
        - Точность построения в пределах 3x3 точек (чтобы не толкались за места)
        """
        # Боец следует к своему месту в строю:
        if hasattr(soldier, 'place_in_order') and soldier.place_in_order:
            destination = [c1 + c2 for c1, c2 in zip(commander.place, soldier.place_in_order)]
            destination = tuple(destination)
        # Если в строю есть свободное место, боец занимает его:
        else:
            for place_in_order, unit in squad.battle_order.items():
                if None in unit:
                    squad.battle_order[place_in_order] = (soldier.behavior, soldier.uuid)
                    soldier.set_place_in_order(place_in_order)
                    destination = [c1 + c2 for c1, c2 in zip(commander.place, soldier.place_in_order)]
                    break
            else:
                destination = random.choice(commander.near_zone)
        # Абсолютная точность не нужна, боец не двигается, если его местов пределах 3x3 тайлов:
        if not destination in self.point_to_field(soldier.place, 1):
            try:
                self.move_action(soldier, squad, destination)
            except KeyError:
                #traceback.print_exc()
                destination = random.choice(commander.near_zone)
                self.move_action(soldier, squad, destination)

    def engage_action(self, soldier, squad, enemy, recon_near):
        """Солдат сближается с противником, готовясь атаковать.
        
        Как это работает:
        - Боец оценивает силу союзников рядом (в зоне 3x3 клетки)
        - Он сравнивает эту силу с силой врага в точке назначения.
        - Затем он направляется к ближайшей свободной точке линии фронта.
        - И только после этого бросается к ближайшему врагу.
        Эта тактика защищает от окружения и провоцированных атак.
        """
        ally_strenght = self.danger_sense(recon_near, soldier.ally_side)
        recon_enemy = self.recon(enemy.place, 1, soldier.place)
        enemy_strenght = self.danger_sense(recon_enemy, soldier.enemy_side)
        if squad.frontline:
            frontline_distances = []
            for point in squad.frontline:
                distance = round(distance_measure(soldier.place, point))
                frontline_distances.append((point,distance))
            frontline_distances = sorted(frontline_distances,key=lambda x: x[1])
            destination = frontline_distances[0][0]
        else:
            destination = enemy.place
        # Простые солдаты нападают вблизи только при двухкратном превосходстве союзников:
        if not soldier.near_enemies and ally_strenght >= enemy_strenght * 2\
                or soldier.hero == True and not soldier.near_enemies and ally_strenght >= enemy_strenght\
                or 'fearless' in squad.commands:
            self.move_action(soldier, squad, destination)
            recon_near = self.recon(soldier.place, distance = 1)
            soldier.set_near_enemies(recon_near)
            if not soldier.near_enemies or 'fearless' in squad.commands:
                self.move_action(soldier, squad, enemy.place, save_path = False)
                if soldier.hero == True or soldier.behavior == 'commander':
                    self.move_action(soldier, squad, enemy.place, allow_replace = True)

    def dodge_action(self, soldier):
        """Боец защищается.
        
        https://www.dandwiki.com/wiki/5e_SRD:Dodge_Action
        """
        # TODO: перенести в класс soldier_fight
        if soldier.bonus_action and soldier.class_features.get('Cunning_Action'):
            soldier.set_cunning_action_defence()
        elif soldier.battle_action:
            soldier.battle_action = False
            soldier.dodge_action = True
        elif soldier.class_features.get('Patient_Defense'):
            soldier.set_patient_defence()

    def dash_action(self, soldier):
        """Боец ускоряется.
        
        https://www.dandwiki.com/wiki/5e_SRD:Dash_Action
        """
        # TODO: перенести в класс soldier_fight
        if soldier.bonus_action and soldier.class_features.get('Cunning_Action'):
            soldier.set_cunning_action_dash()
        elif soldier.battle_action:
            soldier.battle_action = False
            soldier.dash_action = True

    def pathfinder(self, soldier, squad, destination):
        """Пытаемся найти путь к цели.

        Как работает поиск пути:
        - Пытаемся найти путь по линии взгляда.
        - Если не получается используем AStarFinder.
        - Для оптимизации оба алгоритма игнорируют солдат.

        Число срабатываний слоупочного AStarFinder ограничено.
        - Если путь сложный, сначала пойдут первые 40 солдат.
        - Когда они увидят точку назначения, выступят следующие 40.
        Это важно для подземелий, где командира легко потерять из виду.
        """
        path = self.find_path_fast(soldier.place, destination)
        # Слоу-поиск пути, это самое тормозное, поэтому ограничиваем сверху:
        if path == None and squad.slow_path_uses <= squad.slow_path_max:
            try:
                path = self.find_path_slow(soldier.place, destination)
                squad.slow_path_uses +=1
            except IndexError:
                #traceback.print_exc()
                path = None
        return path

    def path_to_savepath(self, path, frontline):
        """Правим путь, чтобы конечная точка не была за линией фронта.
        
        Чтобы бойцы не бегали между врагами. Это защита от провоцированных атак.
        """
        # Работает, но лучше сделать поиск пути до ближайшей точки на линии фронта.
        save_path = []
        for point in path:
            if point not in frontline:
                save_path.append(point)
            else:
                break
        return save_path

    def move_action(self, soldier, squad, destination,
            free_path = False, allow_replace = False,
            save_path = True, allow_manoeuvre = True):
        """Боец следует к цели.
        
        Как работает следование маршруту:
        - Боец проверяет, не занята ли точка на пути.
        - Если точка занята, он проверяет ближайшие точки.
        - И занимает одну из них при двух ключевых условиях.
        - Точка свободна и с неё можно вернуться на путь.
        
        Подробнее о манёврах в пределах пути:
        Если точка назначения занята, делаем срез списков (111):
        ..1..
        .we..
        ..1..
        И считаем следующую точку пути любой подходящей из среза.
        """
        path = self.pathfinder(soldier, squad, destination)
        if save_path and path and squad.frontline != None:
            # Безопасный путь, это остановка перед линией фронта:
            path = self.path_to_savepath(path, squad.frontline)
        if path:
            while path and soldier.move_pool > 0:
                # Если ближайшая точка пути свободна, переходим на неё:
                place = self.check_place(path[0])
                if place.free or free_path:
                    # TODO: пусть боец запоминает направление движения.
                    # -------------------------------------------------
                    # Сделай это функцией soldier. Всего 8 направлений.
                    # Это можно будет использовать как область зрения.
                    # А также для команд вроде 'move_backward', 'move_forvard'
                    # -------------------------------------------------
                    next_place = path.pop(0)
                    prev_place = soldier.place
                    soldier.move(self.tile_size, place.rough)
                    self.change_place(prev_place, next_place, soldier.uuid)
                # Если точка занята ездовым животным бойца, то можно двигаться:
                elif not place.free and place.unit\
                        and hasattr(soldier, 'mount_uuid')\
                        and place.unit[1] == 'mount'\
                        and place.unit[-1] == soldier.mount_uuid:
                    next_place = path.pop(0)
                    prev_place = soldier.place
                    soldier.move(self.tile_size, place.rough)
                    self.change_place(prev_place, next_place, soldier.uuid)
                # Если точка занята союзником, можно поменяться с ним местами:
                elif not place.free and allow_replace and place.unit\
                        and place.unit[0] == soldier.ally_side:
                    unit_uuid = place.unit[-1]
                    next_place = path.pop(0)
                    prev_place = soldier.place
                    soldier.move(self.tile_size, place.rough)
                    self.change_place(prev_place, next_place, soldier.uuid)
                    # Многотайловых лошадей не трогаем, мимо протискиваемся:
                    if place.unit[1] != 'mount':
                        self.change_place(next_place, prev_place, unit_uuid)
                # Если точка занята кем-то, можно шагнуть по диагонали и вернуться на путь:
                elif not place.free and allow_manoeuvre:
                    if len(path) > 1:
                        next_place = path[1]
                    elif len(path) == 1:
                        next_place = path[0]
                    # Боец проверяет точки в пределах манёвра и выбирает свободную:
                    # Он идёт на неё в следующий проход цикла.
                    prev_place = soldier.place
                    coordinates_field = self.point_to_field(prev_place, 1)
                    destination_field = self.point_to_field(next_place, 1)
                    destination_slice = list(set(destination_field) & set(coordinates_field))
                    for destination in destination_slice:
                        near_place = self.check_place(destination)
                        if near_place.free:
                            path[0] = destination
                            break
                    else:
                        path = None
                else:
                    break

    def change_place(self, coordinates, destination, uuid):
        """Перемещаем бойца на точку назначения.
        
        Вызывается по одной клетке в move_action.
        """
        for el in self.dict_battlespace[coordinates]:
            if type(el) == tuple and el[-1] == uuid:
                soldier_tuple = el
                soldier_uuid = el[-1]
                soldier = self.metadict_soldiers[soldier_uuid]
                if hasattr(soldier, 'mount_uuid') and soldier.mount_uuid:
                    self.change_place_mount(coordinates, destination, soldier)
                if soldier.size == 'medium' or soldier.size == 'small':
                    self.dict_battlespace[coordinates].remove(el)
                    self.dict_battlespace[destination].append(soldier_tuple)
                    soldier.set_coordinates(destination)
                elif soldier.size == 'large':
                    soldier_place_field = self.point_to_field(coordinates, 3)
                    for point in soldier_place_field:
                        if point in self.dict_battlespace\
                                and soldier_tuple in self.dict_battlespace[point]:
                            self.dict_battlespace[point].remove(el)
                    #self.dict_battlespace[destination].append(soldier_tuple)
                    destination_field = self.point_to_field_2x2(destination)
                    for point in destination_field:
                        if point in self.dict_battlespace and point != coordinates:
                            self.dict_battlespace[point].append(soldier_tuple)
                            self.dict_battlespace[point].append('mount_height')
                    soldier.set_coordinates(destination)
        # Показывает ходы бойца:
        if namespace.visual:
            print_ascii_map(self.gen_battlemap())
            time.sleep(0.02)

    def change_place_mount(self, coordinates, destination, soldier):
        """Перемещаем мультитайловое ездовое животное вместе с наездником."""
        mount_tuple = None
        mount_place_field = self.point_to_field(coordinates, 3)
        # Проверяем, есть ли рядом с бойцом его ездовое животное:
        for point in mount_place_field:
            for el in self.dict_battlespace[point]:
                if type(el) == tuple\
                        and el[1] == 'mount'\
                        and el[-1] == soldier.mount_uuid:
                    mount_tuple = el
                    mount_uuid = el[-1]
                    mount = self.metadict_soldiers[mount_uuid]
                    break
        # Если есть, перемещаем его в зону назначения:
        if mount_tuple:
            for point in mount_place_field:
                if point in self.dict_battlespace:
                    if mount_tuple in self.dict_battlespace[point]:
                        self.dict_battlespace[point].remove(mount_tuple)
            destination_field = self.point_to_field_2x2(destination)
            for point in destination_field:
                if point in self.dict_battlespace:
                    self.dict_battlespace[point].append(mount_tuple)
            # Пытаемся передвинуть точку обзора вместе с лошадкой:
            self.dict_battlespace[destination].append('mount_height')
            try:
                self.dict_battlespace[coordinates].remove('mount_height')
            except:
                #traceback.print_exc()
                #print(self.dict_battlespace[coordinates])
                pass
            mount.set_coordinates(destination)

    def volley_action(self, soldier, squad):
        """Лучник обстреливает зону градом стрел."""
        # Выбираем подходящее оружие:
        attack_choice = None
        for target in squad.danger_points:
            distance = round(distance_measure(soldier.place, target))
            if distance >= 2 and 'volley' in [attack[0] for attack in soldier.attacks]:
                volley_attack = [attack for attack in soldier.attacks if attack[0] == 'volley'\
                        and attack[1] == soldier.attacks[attack]['weapon_of_choice']][0]
                volley_range = round(soldier.attacks[volley_attack]['attack_range_max'] / self.tile_size)
                if volley_range >= distance:
                    attack_choice = volley_attack
                    break
        # Рассчитываем зону обстрела (зависит от положения бойца в строю и рассеивания стрел):
        if attack_choice:
            if hasattr(soldier, 'place_in_order'):
                target = [c1 + c2 for c1, c2 in zip(target, soldier.place_in_order)]
            else:
                target = random.choice(self.point_to_field(target, round(distance / 10)))
            target = tuple(target)
            # Смотрим, есть ли кто в точке попадания:
            if target in self.dict_battlespace.keys():
                if not 'volley' in self.dict_battlespace[target]:
                    self.dict_battlespace[target].append('volley')
                for value in self.dict_battlespace[target]:
                    if type(value) == tuple:
                        uuid = value[-1]
                        cover = self.calculate_enemy_cover(target, target).cover
                        distance = round(distance_measure(soldier.place, target))
                        enemy = self.namedtuple_target(value[0],value[1],target,distance,cover,uuid)
                        self.attack_action(soldier, squad, enemy, attack_choice = attack_choice)
                        break
                else:
                    # Стрелы расходуются, если летят совсем не туда:
                    soldier.attacks[attack_choice]['ammo'] -= 1
                    self.set_squad_battle_stat(soldier.attacks.get(attack_choice), squad, attack_choice)

    def attack_action(self, soldier, squad, enemy, attack_choice = None):
        """Боец выбирает противника и атакует."""
        enemy_soldier = self.metadict_soldiers[enemy.uuid]
        if soldier.battle_action:
            # Смотрим, возможно ли атаковать:
            if not attack_choice:
                attack_choice = soldier.select_attack(squad, enemy, self.tile_size)
                if attack_choice == None:
                    return False
            # Готовим цепь атак:
            attacks_number = soldier.attacks_number
            attacks_chain = [attack_choice] * attacks_number
            soldier.battle_action = False
            # Оцениваем угрозу контратаки, прежде чем нападать:
            danger_offence = self.check_danger_offence(soldier, enemy)
            # TODO: бонусы классов в отдельную функцию:
            attacks_chain_bonus = []
            # Боец может использовать парное оружие (в том числе метательное), если нет щита:
            if soldier.class_features.get('Fighting_Style_Two_Weapon_Fighting'):
                if attack_choice[0] == 'close' or attack_choice[0] == 'throw':
                    attacks_chain_bonus = soldier.set_two_weapon_fighting(attack_choice)
            if soldier.char_class == 'Barbarian':
                if attack_choice[0] == 'close':
                    soldier.set_rage()
                if attack_choice[0] == 'close' and danger_offence:
                    attacks_chain_bonus = soldier.set_frenzy(attack_choice)
            elif soldier.char_class == 'Monk':
                if attack_choice[0] == 'close':
                    attacks_chain_bonus = soldier.set_martial_arts()
            # Роги умело выбивают командиров:
            # TODO: для этого теперь есть команда "kill".
            elif soldier.char_class == 'Rogue':
                if attack_choice[0] == 'ranged' and squad.enemies:
                    visible_enemies = self.find_visible_soldiers(
                            soldier.place, soldier.enemy_side, squad.enemies,
                            max_number = 30, max_try = 60)
                    enemy_commander = self.select_enemy(visible_enemies, select_strongest = True)
                    if enemy_commander:
                        enemy = enemy_commander
                        enemy_soldier = self.metadict_soldiers[enemy_commander.uuid]
            # Рейнджеры выбирают групповые цели:
            elif soldier.char_class == 'Ranger':
                if attack_choice[0] == 'ranged':
                    if hasattr(soldier, 'spells')\
                            and enemy_soldier.near_allies and len(enemy_soldier.near_allies) > 2:
                        soldier.set_thorns()
                    if soldier.class_features.get('Hunter_Horde_Breaker')\
                            and enemy_soldier.near_allies:
                        attacks_chain_bonus = [attack_choice]
            attacks_chain.extend(attacks_chain_bonus)
            # Начинаем цепь атак:
            while attacks_chain:
                # Иногда заканчиваются боеприпасы:
                if not soldier.attacks.get(attacks_chain[0]):
                    break
                # Боец подготавливает атаку:
                attack_choice = attacks_chain.pop(0)
                advantage, disadvantage = self.test_enemy_defence(soldier, enemy, attack_choice)
                if not advantage:
                    advantage = self.break_enemy_defence(soldier, squad, enemy, attack_choice)
                # Вместо атаки можно перейти в рукопашный бой (сбивание с ног, захваты, разоружение):
                if attack_choice[0] == 'close':
                    if len(soldier.near_allies) > 2\
                            and len(soldier.near_enemies) == 1\
                            and not enemy_soldier.size == 'large'\
                            or enemy_soldier.sleep\
                            or soldier.char_class == 'Monk'\
                            or soldier.class_features.get('Grappler_AI'):
                        wrestling_action = self.wrestling_action(soldier, squad,
                                enemy_soldier, advantage, disadvantage)
                        if wrestling_action != None:
                            continue
                # Боец реализует атаку:
                attack_dict = soldier.attack(soldier.attacks[attack_choice], attack_choice,
                        enemy, self.metadict_soldiers,
                        advantage = advantage, disadvantage = disadvantage)
                # Противник получает атаку:
                attack_result = enemy_soldier.take_attack(
                        attack_choice, attack_dict, self.metadict_soldiers)
                # Монашьи боласы могут сбить с ног:
                if attack_result['hit'] and 'prone' in attack_result['weapon_type']\
                        and not enemy_soldier.prone:
                    prone = enemy_soldier.set_fall_prone(soldier, advantage, disadvantage)
                # Атаку рейнджера дополняет шрапнель от Hail_of_Thorns:
                if attack_result['hit'] and soldier.thorns\
                        and enemy_soldier.near_allies and len(enemy_soldier.near_allies) > 2:
                    self.fireball_action(soldier, squad, soldier.thorns, enemy.place)
                    soldier.thorns_timer = 0
                    soldier.thorns = None
                # Паладин добивает врага с помощью Divine_Smite:
                if attack_result['hit'] and not attack_result['fatal_hit']\
                        and hasattr(soldier, 'spells') and soldier.spells\
                        and soldier.spells_generator.find_spell('Divine_Smite'):
                    spell_choice = soldier.spells_generator.find_spell('Divine_Smite')
                    self.spellcast_action(soldier, squad, enemy,
                            spell_choice, subspell = True, use_spell = True)
                # Волшебный меч Sword of the Past:
                if attack_result['hit'] and 'sword_burst' in attack_result['weapon_type']:
                    spell_choice = 'subspell', 'Sword_Burst'
                    spell_dict = soldier.spells[spell_choice]
                    spell_dict['spell_choice'] = spell_choice
                    self.fireball_action(soldier, squad, spell_dict, soldier.place, safe = True)
                # Мастер тяжёлого оружия получает бонусную атаку, если убивает врага:
                # 20 варварам 2 lvl это добавляет 25% атак. От 10 до 30 атак за минуту боя.
                if attack_result['crit'] or attack_result['fatal_hit']:
                    if attack_dict.get('weapon_skills_use')\
                            and 'Feat_Great_Weapon_Master' in attack_dict['weapon_skills_use']\
                            and soldier.bonus_action:
                        attacks_chain.append(attack_choice)
                        soldier.bonus_action = False
                # Добавляем опыт отряду:
                if attack_result['fatal_hit']:
                    self.set_squad_experience(squad, enemy_soldier)
                    soldier.victories += 1
                    enemy_soldier.defeats += 1
                    enemy_soldier.prone = True
                    if attack_result['crit']:
                        enemy_soldier.disabled = True
                    # Колдун с Dark_One\'s_Blessing получает бонусные хиты:
                    if soldier.class_features.get('Dark_One\'s_Blessing'):
                        bonus_hitpoints_bless = soldier.mods['charisma'] + soldier.level
                        if bonus_hitpoints_bless > soldier.bonus_hitpoints:
                            #print('{0} {1} temp_hp {2}'.format(
                            #    soldier.ally_side, soldier.rank, bonus_hitpoints_bless))
                            soldier.set_hitpoints(bonus_hitpoints = bonus_hitpoints_bless)
                # Убираем противника из списка целей и с карты:
                if attack_result['fatal_hit']:
                    self.clear_battlemap()
                    fall_place = enemy_soldier.place
                    self.dict_battlespace[fall_place].append('fall_place')
                    self.dict_battlespace[fall_place].append(enemy_soldier.ally_side)
                    # Осматриваемся, убираем жертву из списка целей бойца.
                    recon_near = self.recon(soldier.place, distance = 1)
                    soldier.set_near_enemies(recon_near)
                    danger = self.danger_sense(recon_near, soldier.enemy_side)
                    if squad.enemies and enemy.uuid in squad.enemies:
                        squad.enemies.pop(enemy.uuid)
                    # Выбираем новую цель:
                    if soldier.near_enemies:
                        enemy = random.choice(soldier.near_enemies)
                        enemy_soldier = self.metadict_soldiers[enemy.uuid]
                # Обобщаем статистику атак (расход боеприпасов и прочее):
                self.set_squad_battle_stat(attack_result, squad)

    def wrestling_action(self, soldier, squad, enemy_soldier, advantage = False, disadvantage = False):
        """Рукопашный бой вместо обычных атак.
        
        1) Пытаемся сбить врага с ног.
        2) Сбитого с ног врага хватаем, чтобы не встал.
        3) Схваченного врага пытаемся разоружить.
        """
        # TODO: бонусные атаки нельзя заменить захватами:
        # ------------------------------------------------------------
        # Пусть возвращает True, если рукопашный бой уместен, и тогда continue
        # You cannot replace bonus action attacks with grapples.
        # (e.g. from the Monk or a Barbarian's Frenzy)
        # ------------------------------------------------------------
        # кроме того обычные advantage и disadvantage не должны работать.
        # ------------------------------------------------------------
        # Сбитого с ног врага пытаемся схватить:
        if not enemy_soldier.grappled:
            grappled = enemy_soldier.set_grappled(soldier, advantage, disadvantage)
            # Боец становится на место схваченного врага, а борцуха-монах выдирает его из строя:
            if grappled and not enemy_soldier.behavior == 'mount':
                if soldier.char_class == 'Monk':
                    destination = self.find_spawn(soldier.place, soldier.ally_side)
                    self.move_action(soldier, squad, destination, allow_replace = True)
                    self.change_place(enemy_soldier.place, soldier.place, enemy_soldier.uuid)
                else:
                    self.change_place(soldier.place, enemy_soldier.place, soldier.uuid)
            return grappled
        # Пытаемся сбить врага с ног:
        elif not enemy_soldier.prone:
            prone = enemy_soldier.set_fall_prone(soldier, advantage, disadvantage)
            return prone
        # У схваченного врага пытаемся вырвать щит:
        elif enemy_soldier.armor['shield_use'] and not enemy_soldier.class_features.get('Weapon_Bond'):
            disarmed = enemy_soldier.set_disarm_shield(soldier, advantage, disadvantage)
            return disarmed
        # TODO: проверка по числу атак -- плохая идея. У нас будут минотавры с рогами.
        # И наконец, отбираем у схваченного врага оружие и тащим его к нашим:
        elif len(enemy_soldier.attacks) > 1 and not enemy_soldier.class_features.get('Weapon_Bond'):
            disarmed = enemy_soldier.set_disarm_weapon(soldier, advantage, disadvantage)
            if disarmed and len(soldier.near_allies) >= 1:
                destination = self.find_spawn(soldier.place, soldier.ally_side)
                self.move_action(soldier, squad, destination, allow_replace = True)
                self.change_place(enemy_soldier.place, soldier.place, enemy_soldier.uuid)
            return disarmed

    def spellcast_action(self, soldier, squad, enemy,
            spell_choice = None, subspell = False, use_spell = True):
        """Боец атакует заклинанием."""
        enemy_soldier = self.metadict_soldiers[enemy.uuid]
        if hasattr(soldier, 'spells') and soldier.spells and soldier.battle_action\
                or spell_choice and subspell:
            # Смотрим, возможно ли атаковать:
            if not spell_choice:
                spell_choice = soldier.select_spell(squad, enemy, self.tile_size)
                if spell_choice == None:
                    return False
            if use_spell:
                spell_dict = soldier.spells_generator.use_spell(spell_choice)
            else:
                spell_dict = soldier.spells[spell_choice]
            attacks_number = spell_dict['attacks_number']
            spell_chain = [spell_choice] * attacks_number
            soldier.battle_action = False
            while spell_chain:
                spell_choice = spell_chain.pop(0)
                advantage, disadvantage = self.test_enemy_defence(soldier, enemy, spell_choice)
                # Заклинание Word_of_Radiance, избирательно бьющее по врагам вблизи.
                if spell_dict.get('effect') == 'burst':
                    if soldier.class_features.get('Channel_Radiance_of_the_Dawn')\
                            and soldier.near_enemies and len(soldier.near_enemies) > 1\
                            and soldier.channel_divinity > 0:
                        spell_choice = 'channel', 'Radiance_of_the_Dawn'
                        spell_dict = soldier.spells[spell_choice]
                        spell_dict['spell_choice'] = spell_choice
                        self.fireball_action(soldier, squad, spell_dict, soldier.place, safe = True)
                        soldier.channel_divinity -= 1
                        continue
                    else:
                        spell_dict['spell_choice'] = spell_choice
                        self.fireball_action(soldier, squad, spell_dict, soldier.place, safe = True)
                        continue
                # TODO: заклинания в отдельные функции.
                # Заклинание Cause_Fear:
                elif spell_dict.get('effect') == 'fear':
                    enemy_soldier = self.find_target_for_debuff(soldier, enemy, 'fear')
                    if not enemy_soldier:
                        break
                    else:
                        fear = enemy_soldier.set_fear(soldier, spell_dict['spell_save_DC'])
                        # TODO: нам нужна функция концентрации.
                        # Вот только целей у заклинания может быть несколько.
                        #if fear:
                        #    soldier.concentration = True
                    continue
                # Заклинание Entangle:
                elif spell_dict.get('effect') == 'entangle':
                    enemy_soldier = self.find_target_for_debuff(soldier, enemy, 'restained')
                    if not enemy_soldier:
                        break
                    else:
                        enemy_soldier.set_restained(spell_dict['spell_save_DC'])
                        fall_place = enemy_soldier.place
                        if not 'volley' in self.dict_battlespace[fall_place]:
                            self.dict_battlespace[fall_place].append('volley')
                        # TODO: проверь check_place. Что-то ломается. Бойцы начинают бегать через своих:
                        #if not 'bushes' in self.dict_battlespace[fall_place]:
                        #    self.dict_battlespace[fall_place].insert(0, 'bushes')
                        #    if not 'rough_terrain' in self.dict_battlespace[fall_place]:
                        #        self.dict_battlespace[fall_place].insert(1, 'rough_terrain')
                    continue
                # Заклинание Sleep:
                elif spell_dict.get('effect') == 'sleep':
                    sleep_pool = dices.dice_throw_advantage(spell_dict['damage_dice'])
                    # Перебираем цели, пока есть хоть кто-то с хитами меньшими, чем sleep_pool:
                    while sleep_pool > 0:
                        if enemy_soldier.sleep or enemy_soldier.hitpoints > sleep_pool:
                            enemy_soldier = self.find_target_for_debuff(soldier, enemy, 'sleep')
                            if not enemy_soldier:
                                break
                        sleep_pool -= enemy_soldier.hitpoints
                        enemy_soldier.set_sleep()
                        self.clear_battlemap()
                        fall_place = enemy_soldier.place
                        self.dict_battlespace[fall_place].append('fall_place')
                        self.dict_battlespace[fall_place].append(enemy_soldier.ally_side)
                    continue
                # Magic_Missile всегда попадает.
                elif spell_dict.get('direct_hit'):
                    attack_dict = soldier.spell_attack(spell_dict, enemy,
                            advantage = advantage, disadvantage = disadvantage)
                    attack_result = enemy_soldier.take_attack(
                            spell_choice, attack_dict, self.metadict_soldiers)
                    # Заклинание "Create_Bonfire" оставляет пожары:
                    if spell_dict.get('effect') == 'bonfire':
                        # TODO: поставь в начале хода атаку любого, кто оказался в зоне поражения.
                        # Для этого нужна отдельная, универсальная функция.
                        if soldier.concentration and soldier.concentration_spell.get('bonfire_place'):
                            try:
                                bonfire_place_old = soldier.concentration_spell['bonfire_place']
                                self.dict_battlespace[bonfire_place_old].remove('fire')
                                self.dict_battlespace[bonfire_place_old].remove('danger_terrain')
                                self.dict_battlespace[bonfire_place_old].remove('stop_terrain')
                            except ValueError:
                                #traceback.print_exc()
                                pass
                        bonfire_place = enemy_soldier.place
                        spell_dict['bonfire_place'] = bonfire_place
                        #self.dict_battlespace[bonfire_place].append('fire')
                        self.dict_battlespace[bonfire_place].insert(0, 'fire')
                        self.dict_battlespace[bonfire_place].append('danger_terrain')
                        self.dict_battlespace[bonfire_place].append('stop_terrain')
                        # Обновляем сетку, метка "fire" -- опасная зона.
                        self.matrix = self.map_to_matrix(self.battle_map, self.dict_battlespace)
                        soldier.concentration_spell = spell_dict
                        soldier.concentration = True
                # Заклинания с показателем атаки мало отличаются от стрел и мечей:
                elif spell_dict.get('attack_mod'):
                    attack_dict = soldier.attack(spell_dict, spell_choice,
                            enemy, self.metadict_soldiers,
                            advantage = advantage, disadvantage = disadvantage)
                    attack_result = enemy_soldier.take_attack(
                            spell_choice, attack_dict, self.metadict_soldiers)
                else:
                    print('NYA. Недопиленое заклинание', spell_choice, spell_dict)
                    continue
                # Добавляем опыт отряду:
                if attack_result['fatal_hit']:
                    self.set_squad_experience(squad, enemy_soldier)
                    soldier.victories += 1
                    enemy_soldier.defeats += 1
                    enemy_soldier.prone = True
                    if attack_result['crit']:
                        enemy_soldier.disabled = True
                    # Колдун с Dark_One\'s_Blessing получает бонусные хиты:
                    if soldier.class_features.get('Dark_One\'s_Blessing'):
                        bonus_hitpoints_bless = soldier.mods['charisma'] + soldier.level
                        if bonus_hitpoints_bless > soldier.bonus_hitpoints:
                            #print('{0} {1} temp_hp {2}'.format(
                            #    soldier.ally_side, soldier.rank, bonus_hitpoints_bless))
                            soldier.set_hitpoints(bonus_hitpoints = bonus_hitpoints_bless)
                # Убираем противника из списка целей и с карты:
                if attack_result['fatal_hit']:
                    self.clear_battlemap()
                    fall_place = enemy_soldier.place
                    self.dict_battlespace[fall_place].append('fall_place')
                    self.dict_battlespace[fall_place].append(enemy_soldier.ally_side)
                    if squad.enemies and enemy.uuid in squad.enemies:
                        squad.enemies.pop(enemy.uuid)
                # Обобщаем статистику атак (расход боеприпасов и прочее):
                self.set_squad_battle_stat(attack_result, squad)

    def find_target_for_debuff(self, soldier, enemy, debuff):
        """Ищет цели, на которые ещё не наложен выбранный эффект заклинания.
        
        Например, enemy.fear для Cause_Fear, или enemy.sleep для заклинания Sleep
        """
        recon_enemy = self.recon(enemy.place, 6, soldier.place)
        enemy_list = [unit for unit in recon_enemy.values() if unit.side == soldier.enemy_side]
        for enemy in enemy_list:
            enemy_soldier = self.metadict_soldiers[enemy.uuid]
            if getattr(enemy_soldier, debuff) != True:
                return enemy_soldier

    def fireball_action(self, soldier, squad, spell_dict = None, zone_center = None, safe = False):
        """Маг работает артиллерией."""
        if hasattr(soldier, 'spells') and soldier.battle_action\
                and self.select_zone_spell(soldier, squad)\
                or spell_dict and zone_center:
            if spell_dict and zone_center:
                spell_choice = spell_dict['spell_choice']
                auto_zone_target = False
            else:
                auto_zone_target = True
                spell_choice, zone_center = self.select_zone_spell(soldier, squad)
                # TODO: здесь должна быть проверка на soldier.concentration
                # ------------------------------------------------------------
                # И единая система, где в concentration указано заклинание.
                # Например soldier.concentration = spell_choice (или spell_dict)
                # А concentration_timer тогда берём из самого заклинания.
                # Сделай! Так будет гораздо удобнее.
                # ------------------------------------------------------------
                # Moonbeam можно перенацеливать, минута действия:
                if spell_choice[-1] == 'Moonbeam':
                    if soldier.__dict__.get('moonbeam_timer', 0) > 0:
                        spell_dict = soldier.moonbeam
                    else:
                        spell_dict = soldier.spells_generator.use_spell(spell_choice)
                        soldier.moonbeam = spell_dict
                        soldier.moonbeam_timer = 10
                # Call_Lightning -- убийственная версия Moonbeam
                elif spell_choice[-1] == 'Call_Lightning':
                    if soldier.__dict__.get('call_lightning_timer', 0) > 0:
                        spell_dict = soldier.call_lightning
                    else:
                        spell_dict = soldier.spells_generator.use_spell(spell_choice)
                        soldier.call_lightning = spell_dict
                        soldier.call_lightning_timer = 100
                else:
                    spell_dict = soldier.spells_generator.use_spell(spell_choice)
            zone_radius = round(spell_dict['radius'] / self.tile_size)
            recon_dict = self.recon(zone_center, zone_radius)
            # TODO: зона не всегда круглая, добавь формы в словари заклинаний:
            if zone_radius > 1:
                targets = [target for target in recon_dict.values()\
                        if inside_circle(target.place, zone_center, zone_radius)]
            elif spell_dict.get('zone_shape') == '2x2':
                zone_points_list = self.point_to_field_2x2(zone_center)
                targets = [target for target in recon_dict.values()\
                        if target.place in zone_points_list]
            elif spell_dict.get('zone_shape') == 'square':
                targets = [target for target in recon_dict.values()]
            else:
                targets = [target for target in recon_dict.values()]
            if targets:
                soldier.battle_action = False
                if spell_dict.get('zone_danger'):
                    danger_zone = self.point_to_field(zone_center)
                    for point in danger_zone:
                        if not 'volley' in self.dict_battlespace[point]:
                            self.dict_battlespace[point].append('volley')
            for enemy in targets:
                # Враг может защититься контрзаклинанием, если угроза достаточно велика:
                if spell_choice[0][0].isnumeric() and int(spell_choice[0][0]) >= 3:
                    counterspell_enemies = [enemy_soldier\
                            for enemy_soldier in self.metadict_soldiers.values()\
                            if enemy_soldier.ally_side == soldier.enemy_side\
                            and 'Counterspell' in [spell[-1] for spell in enemy_soldier.spells.keys()]]
                    if counterspell_enemies:
                        enemy_soldier = counterspell_enemies[0]
                        counterspell_choice = [spell for spell in enemy_soldier.spells.keys()
                                if 'Counterspell' in spell][0]
                        counterspell_dict = enemy_soldier.spells_generator.use_spell(counterspell_choice)
                        enemy_soldier.reaction = False
                        # TODO: здесь костыль. Сделай универсальное прерывание концентрации.
                        if soldier.call_lightning:
                            soldier.call_lightning_timer = 0
                        print('DISPELL', soldier.ally_side, soldier.place, spell_choice, '<<',
                                enemy_soldier.ally_side, counterspell_choice)
                        break
                if safe and enemy.side in soldier.ally_side:
                    continue
                # У заклинания Ice_Knife есть и шрапнель, и основной поражающий элемент:
                if spell_dict.get('effect') == 'ice_knife' and enemy.place == zone_center:
                    self.spellcast_action(soldier, squad, enemy,
                            spell_choice = spell_dict['subspell'], subspell = True, use_spell = False)
                enemy_soldier = self.metadict_soldiers[enemy.uuid]
                advantage, disadvantage = self.test_enemy_defence(soldier, enemy, spell_choice)
                attack_dict = soldier.spell_attack(spell_dict, enemy,
                        advantage = advantage, disadvantage = disadvantage)
                attack_result = enemy_soldier.take_attack(
                        spell_choice, attack_dict, self.metadict_soldiers)
                # Добавляем опыт отряду:
                if attack_result['fatal_hit']:
                    self.set_squad_experience(squad, enemy_soldier)
                    soldier.victories += 1
                    enemy_soldier.defeats += 1
                    enemy_soldier.prone = True
                    if attack_result['crit']:
                        enemy_soldier.disabled = True
                    # Колдун с Dark_One\'s_Blessing получает бонусные хиты:
                    if soldier.class_features.get('Dark_One\'s_Blessing'):
                        bonus_hitpoints_bless = soldier.mods['charisma'] + soldier.level
                        if bonus_hitpoints_bless > soldier.bonus_hitpoints:
                            #print('{0} {1} temp_hp {2}'.format(
                            #    soldier.ally_side, soldier.rank, bonus_hitpoints_bless))
                            soldier.set_hitpoints(bonus_hitpoints = bonus_hitpoints_bless)
                # Убираем противника из списка целей и с карты:
                if attack_result['fatal_hit']:
                    self.clear_battlemap()
                    fall_place = enemy_soldier.place
                    self.dict_battlespace[fall_place].append('fall_place')
                    self.dict_battlespace[fall_place].append(enemy_soldier.ally_side)
                    if squad.enemies and enemy.uuid in squad.enemies:
                        squad.enemies.pop(enemy.uuid)
                # Обобщаем статистику атак (расход боеприпасов и прочее):
                self.set_squad_battle_stat(attack_result, squad)
            # Переоцениваем опасные зоны на текущий ход:
            if auto_zone_target:
                squad.danger_points = battle.find_danger_zones(
                        squad.enemy_side, zone_length = 5,
                        soldier_coordinates = squad.commanders_list[0].place)

    def select_zone_spell(self, soldier, squad):
        """Выбор заклинания, бьющего по территории и точки атаки для него."""
        spell_choice_list = []
        for spell_slot in soldier.spellslots:
            if int(spell_slot[0]) <= 2 or 'fireball' in squad.commands:
                slot_spells_list = [attack for attack in soldier.spells if attack[0] == spell_slot
                        and soldier.spells[attack].get('zone')]
                spell_choice_list.extend(slot_spells_list)
        if spell_choice_list:
            # Сортируем. Сначала заклинания высших уровней:
            spell_choice_list = sorted(spell_choice_list, reverse = True)
            for spell_choice in spell_choice_list:
                for zone_center, danger in squad.danger_points.items():
                    distance = round(distance_measure(soldier.place, zone_center))
                    if distance <= round(soldier.spells[spell_choice]['attack_range'] / self.tile_size):
                        return spell_choice, zone_center

    def check_danger_offence(self, soldier, enemy):
        """Проверяем, опасно ли атаковать врага."""
        # TODO: это задача командира. Используем check_danger_offence только если ротной разведки нет.
        enemy_soldier = self.metadict_soldiers[enemy.uuid]
        enemy_attacks = [key[0] for key in enemy_soldier.attacks.keys()] 
        # Маги всех мастей просто чудовища:
        if hasattr(enemy_soldier, 'spells'):
            return True
        # Метатели дротиков и лучники крайне опасны в любых условиях боя:
        if 'throw' in enemy_attacks or 'ranged' in enemy_attacks:
            return True
        # Гоплиты с их длинными копьями -- угроза даже на дистанции хода:
        #elif enemy.distance <= round(enemy_soldier.base_speed / self.tile_size)\
        #        and 'reach' in enemy_attacks and len(enemy_soldier.near_allies) >= 3:
        #    return True
        # Трое врагов рядом, это в любом случае опасно:
        elif soldier.near_enemies and len(soldier.near_enemies) >= 3:
            return True

    def test_enemy_defence(self, soldier, enemy, attack_choice):
        """Проверяем, есть ли преимущества и помехи в атаке на врага.
       
        Возможные преимущества:
        - Упавшего противника легче атаковать (только вблизи).
        - Кавалерист с Feat_Mounted_Combatant легко бьёт пеших (только вблизи).

        Возможные помехи:
        - Противник может защищаться с Dodge_Action
        - Противника может прикрыть боец с щитом и Fighting_Style_Protection
        """
        advantage = False
        disadvantage = False
        enemy_soldier = self.metadict_soldiers[enemy.uuid]
        # Опутанный крайне уязвим:
        if enemy_soldier.restained == True:
            advantage = True
        # Упавшего легче поразить, но только вблизи:
        if enemy_soldier.prone == True:
            if attack_choice[0] == 'close' or attack_choice[0] == 'reach':
                advantage = True
            else:
                disadvantage = True
        # Безрассудного варвара легче поразить (но хрена с два это помогает):
        if enemy_soldier.reckless_attack == True:
            advantage = True
        # Верховой боец атакует с преимуществом, если цель не всадник:
        if attack_choice[0] == 'close' or attack_choice[0] == 'reach':
            if soldier.class_features.get('Feat_Mounted_Combatant') == True\
                    and soldier.mount_combat\
                    and hasattr(soldier, 'mount_uuid')\
                    and self.metadict_soldiers.get(soldier.mount_uuid)\
                    and self.metadict_soldiers[soldier.mount_uuid].place == soldier.place:
                if not hasattr(enemy_soldier, 'mount_uuid')\
                        or hasattr(enemy_soldier, 'mount_uuid')\
                        and hasattr(self.metadict_soldiers[enemy_soldier.mount_uuid], 'place')\
                        and not self.metadict_soldiers[enemy_soldier.mount_uuid].place == enemy_soldier.place:
                    advantage = True
        # Опутанный крайне уязвим:
        if soldier.restained == True:
            disadvantage = True
        # Наш боец может быть сбит с ног (и ему не удалось подняться в начале раунда):
        if soldier.prone == True:
            disadvantage = True
        # Учитываем, что противник может защищаться:
        if enemy_soldier.dodge_action == True:
            disadvantage = True
        # Заклинание 'Размытый образ' прикрывает от атак:
        elif enemy_soldier.blur == True:
            disadvantage = True
        # Противника может защитить товарищ с Fighting_Style_Protection:
        elif len(enemy_soldier.near_allies) > 1:
            for soldier_tuple in enemy_soldier.near_allies:
                enemy_ally = self.metadict_soldiers[soldier_tuple.uuid]
                if enemy_ally.class_features.get('Fighting_Style_Protection')\
                        and enemy_ally.reaction == True\
                        and enemy_ally.uuid != enemy_soldier.uuid\
                        and enemy_ally.armor['shield_use'] != None:
                    disadvantage = enemy_ally.set_protection(enemy_soldier)
                    #print('{0} {1} {2} attack {3} {4} {5} reaction protect from {6} {7} {8}'.format(
                    #    soldier.ally_side, soldier.place, soldier.behavior,
                    #    enemy_soldier.ally_side, enemy_soldier.place, enemy_soldier.behavior,
                    #    enemy_ally.ally_side, enemy_ally.place, enemy_ally.behavior))
                    break
        # Жрец домена света может поставить помеху на одиночную атаку (на дистанции до 30 футов):
        elif hasattr(enemy_soldier, 'warding_flare') and enemy_soldier.warding_flare > 0\
                and enemy_soldier.reaction\
                and (enemy.distance * self.tile_size) <= 30:
            enemy_soldier.warding_flare -= 1
            enemy_soldier.reaction = False
            disadvantage = True
        return advantage, disadvantage

    def break_enemy_defence(self, soldier, squad, enemy, attack_choice):
        """Проверяем, есть ли преимущества или помехи в атаке на врага."""
        advantage = False
        enemy_soldier = self.metadict_soldiers[enemy.uuid]
        # Безрассудная атака варвара, преимущество своим, преимущество врагу:
        if attack_choice[0] == 'close' or attack_choice[0] == 'reach'\
                and soldier.class_features.get('Reckless_Attack'):
            advantage = soldier.set_reckless_attack()
            return advantage
        # Финт за счёт help_action, боец просит помощи низкоуровнего союзника:
        elif attack_choice[0] == 'close' or attack_choice[0] == 'reach' or attack_choice[0] == 'throw':
            if len(enemy_soldier.near_enemies) > 1 and enemy_soldier.armor['armor_class']\
                    > soldier.attacks[attack_choice]['attack_mod'] + 10:
                for ally in enemy_soldier.near_enemies:
                    ally_soldier = self.metadict_soldiers[ally.uuid]
                    if ally_soldier.level < soldier.level or ally_soldier.level == 1:
                        if ally_soldier.uuid != soldier.uuid\
                                and ally_soldier.danger <= self.engage_danger\
                                and not 'dodge' in squad.commands\
                                and not ally_soldier.hero\
                                and not ally_soldier.class_features.get('Reckless_Attack')\
                                and not ally_soldier.help_action:
                            #print('help_action', ally_soldier.ally_side, ally_soldier.rank,
                            #        '-->', soldier.rank)
                            ally_soldier.help_action = True
                            advantage = True
                            return advantage

    def find_enemy(self, soldier, squad):
        """Ищем врага в радиусе атаки.

        Порядок разведки:
        - В ближнем радиусе (5 футов, 3x3 клетки)
        - В радиусе reach-атаки (10 футов, 5x5 клеток)
        - Из списка замеченных командиром (squad.enemies)
        - В раиусе дальних атак (лук, праща, дротики)
        """
        if soldier.near_enemies:
            if soldier.behavior == 'commander' or "kill" in squad.commands:
                return self.select_enemy(soldier.near_enemies, select_strongest = True)
            else:
                return self.select_enemy(soldier.near_enemies)
        if 'reach' in [attack[0] for attack in soldier.attacks]:
            near_enemies = self.find_enemies_near(soldier, distance = 2)
            if near_enemies:
                return self.select_enemy(near_enemies)
        if 'throw' in [attack[0] for attack in soldier.attacks]:
            near_enemies = self.find_enemies_near(soldier, distance = 2)
            if near_enemies:
                return self.select_enemy(near_enemies)
        # Командир выбирает целью вражеских командиров:
        if squad.enemies and soldier.behavior == 'commander'\
                or squad.enemies and "kill" in squad.commands:
            sorted_enemies = self.refind_soldiers_distance(soldier.place, squad.enemies)
            visible_enemies = self.find_visible_soldiers(
                    soldier.place, soldier.enemy_side, sorted_enemies,
                    max_number = 30, max_try = 60)
            return self.select_enemy(visible_enemies, select_strongest = True)
        # Сортируем цели по дистанции и берём по две, чтобы захватить всадника и коня:
        elif squad.enemies:
            sorted_enemies = self.refind_soldiers_distance(soldier.place, squad.enemies)
            visible_enemies = self.find_visible_soldiers(
                    soldier.place, soldier.enemy_side, sorted_enemies,
                    max_number = 2, max_try = 6)
            return self.select_enemy(visible_enemies)
        # Ищем цели в зоне видимости без указания командира:
        if 'seek' in squad.commands:
            visible_enemies = self.find_visible_soldiers(soldier.place, soldier.enemy_side,
                    max_number = 2, max_try = 6)
            return self.select_enemy(visible_enemies)

    def select_enemy(self, near_enemies, select_strongest = False, select_weaker = False):
        """Выбираем слабейшего/сильнейшего врага из списка целей.
        
        Лучшая тактика в текущих условиях боя -- выбивать слабейших.
        """
        # На входе может быть как список, так и словарь:
        if type(near_enemies) == dict:
            near_enemies = near_enemies.values()
        # Список типов противников, отсортированный по уровню угрозы:
        if select_strongest == True:
            danger_list = list(self.dict_danger.keys())
        elif select_weaker == True:
            danger_list = reversed(list(self.dict_danger.keys()))
        else:
            danger_list = (list(self.dict_danger.keys()))
            random.shuffle(danger_list)
        # Выбор первого врага, который сильнейший/слабейший из списка угроз:
        for enemy_type in danger_list:
            for target in near_enemies:
                if target.type == enemy_type:
                    return target

    def find_enemies_near(self, soldier, distance = 1):
        """Боец осматривается и ищет ближайшего врага.
        
        Сначала он смотрит в ближнем радиусе, затем дальше.
        """
        # TODO: оптимизация поиска
        # ------------------------------------------------------------
        # С каждым проходом recon боец снова и снова осматривает ближнюю зону
        # Нужно давать разницу координат ближней зоны и координат дальней
        # Так при distance = 3 мы получим не 7*7=49 клеток, а 7*7-5*5=24 клетки.
        # ------------------------------------------------------------
        # Лучше используй один из алгоритмов Field_of_Vision.
        # http://www.roguebasin.com/index.php?title=Field_of_Vision
        # http://www.roguebasin.com/index.php?title=FOV_using_recursive_shadowcasting
        # http://www.roguebasin.com/index.php?title=FOV_using_recursive_shadowcasting_-_improved
        # Здесь бы отлично смотрелся FoV на shadowcasting. Вот хороший пример:
        # http://www.roguebasin.com/index.php?title=Python_shadowcasting_implementation
        # https://github.com/elemel/python-fov
        # https://github.com/elemel/python-fov/blob/master/src/fov.py
        # ------------------------------------------------------------
        target_list = []
        distance_max = distance
        for distance in range(1, distance_max + 1):
            dict_recon = self.recon(soldier.place, distance)
            for target in dict_recon.values():
                if target.side == soldier.enemy_side:
                    target_list.append(target)
        return target_list

    def find_spawn(self, soldier_coordinates, side, random_range = 10):
        """Если боец не видит врага, то по крайней мере знает примерное направление.
        
        Он выбирает случайную точку спавна врага в диапазоне дистанций и следует к ней.
        """
        coord_dict = {}
        for el in self.spawn_list:
            if side in self.dict_battlespace[el.place]:
                distance = round(distance_measure(soldier_coordinates, el.place))
                coord_dict[el.place] = distance
        coord_dict = OrderedDict(sorted(coord_dict.items(),key=lambda x: x[1]))
        if len(coord_dict) < random_range:
            random_range = len(coord_dict)
        key_number = random.randrange(0, int(len(coord_dict) / random_range))
        for n, key in enumerate(coord_dict.keys()):
            if n == key_number:
                return key

    def set_squad_experience(self, squad, enemy_soldier):
        """Отряд получает опыт за победу над врагом.
        
        Уровень опасности обычных легионеров/гоплитов -- 1/8,
        Поскольку у них в среднем +3 к атаке, 15-17 AC и 8 hp.
        """
        if not hasattr(squad, 'experience'):
            squad.experience = 0
        if enemy_soldier.hitpoints <= 0 and not enemy_soldier.defeat:
            enemy_soldier.defeat = True
            # Опыт от показателя опасности:
            if hasattr(enemy_soldier, 'challenge_rating')\
                    and enemy_soldier.challenge_rating in self.challenge_rating_experience_dict:
                experience_new = self.challenge_rating_experience_dict[enemy_soldier.challenge_rating]
                squad.experience += round(experience_new)
            else:
                # Опыт за уровень врага:
                # 1 lvl: 25*2^(1-1) = 25 exp; 5 lvl: 25*2^(5-1) = 400 exp
                experience_new = 25 * 2 ** (enemy_soldier.level - 1)
                if hasattr(enemy_soldier, 'hero') and enemy_soldier.hero:
                    experience_new *= 2
                elif enemy_soldier.char_class == 'Commoner':
                    experience_new /= 2.5
                squad.experience += round(experience_new)

    def fall_to_death(self, squad):
        """Тяжелораненые делают спасброски от смерти в начале каждого хода.
        
        Death Saving Throws:
        https://www.dandwiki.com/wiki/5e_SRD:Dropping_to_0_Hit_Points
        """
        for soldier in squad.metadict_soldiers.values():
            # Спящего от заклинания Sleep разбудят (или сам проснётся)
            if soldier.sleep and not soldier.captured:
                self.rescue(soldier)
                soldier.sleep_timer -= 1
                if soldier.sleep_timer <= 0:
                    soldier.sleep = False
            # Тяжелораненые играют в рулетку с мрачным жнецом:
            if soldier.hitpoints <= 0 and not soldier.death and not soldier.stable:
                soldier.set_death()
            if soldier.hitpoints <= 0 and not soldier.death and not soldier.stable:
                if hasattr(squad, 'commands') and 'rescue' in squad.commands:
                    self.rescue(soldier)
                    if not soldier.stable and soldier.level > 1 and soldier.death_save_loss >= 1:
                        self.rescue_magic(soldier)

    def rescue(self, soldier):
        """Товарищи стабилизируют тяжелораненых и будят спящих.
        
        Как это работает:
        1) Тяжелораненые и спящие "просят" помощи у всех вокруг.
        2) Если кто-то способен помочь, он помогает с help_action.
        3) Товарищ оттаскивает раненого к себе и пытается перевязать.
        """
        # Раненого можно вытащить, если он не схвачен:
        if not soldier.grappled and not soldier.behavior == 'mount':
            recon_near = self.recon(soldier.place, distance = 1)
            soldier.set_near_allies(recon_near)
            for ally in soldier.near_allies:
                ally_soldier = self.metadict_soldiers[ally.uuid]
                if len(ally_soldier.near_enemies) <= 1\
                        and not ally_soldier.hitpoints <= 0\
                        and not ally_soldier.uuid == soldier.uuid\
                        and not ally_soldier.escape and not ally_soldier.sleep\
                        and not soldier.place == ally_soldier.place\
                        and 'fall_place' in self.dict_battlespace[soldier.place]\
                        and soldier.ally_side in self.dict_battlespace[soldier.place]:
                    self.dict_battlespace[soldier.place].remove('fall_place')
                    self.dict_battlespace[soldier.place].remove(soldier.ally_side)
                    self.change_place(soldier.place, ally_soldier.place, soldier.uuid)
                    soldier.captured = False
                    if soldier.sleep:
                        soldier.sleep_timer = 0
                        soldier.sleep = False
                        break
                    # Только одна попытка первой помощи за ход:
                    elif ally_soldier.first_aid(soldier):
                        soldier.stable = True
                        break
                    else:
                        self.dict_battlespace[soldier.place].append('fall_place')
                        self.dict_battlespace[soldier.place].append(soldier.ally_side)
                        break

    def rescue_magic(self, soldier):
        """Клирик спасает раненого, используя Healing_Word.
        
        Либо раненый спасает себя сам, используя зелье лечения.
        Только стабилизация, без лечения (потому что раненый, скорее всего, в толпе врагов).
        """
        # TODO: добавь проверки.
        # ------------------------------------------------------------
        # Во-первых у тебя даже мёртвый клирик может лечить.
        # Во-вторых нет ограничений по дистанции, а Healing_Word работает на 60 футов.
        # ------------------------------------------------------------
        if soldier.equipment_weapon.get('Infusion of Healing'):
            soldier.use_potion_of_healing()
            soldier.stable = True
        else:
            for healer in self.metadict_soldiers.values():
                if healer.ally_side == soldier.ally_side and hasattr(healer, 'spells'):
                    spell_choice = healer.spells_generator.find_spell('Healing_Word')
                    if spell_choice:
                        spell_dict = healer.spells_generator.use_spell(spell_choice)
                        soldier.stable = True
                        break

    def clear_battlemap(self):
        """Чистим карту от павших/беглецов.
        
        Убираем всех, у кого хитов меньше нуля. А также сбежавших с поля боя.
        """
        for place, content in self.dict_battlespace.items():
            for el in content:
                if type(el) == tuple:
                    uuid = el[-1]
                    soldier = self.metadict_soldiers[uuid]
                    if soldier.defeat:
                        content.remove(el)
                        #soldier.place = None
                        #if 'fall_place' in content and soldier.ally_side in content:
                        #    content.remove('fall_place')
                        #    content.remove(soldier.ally_side)
                    elif soldier.escape == True\
                            and 'spawn' in content\
                            and soldier.ally_side in content:
                        content.remove(el)
                        soldier.defeat = True
                        print('{0} {1} {2} hp {3}/{4} retreat {5}'.format(
                            soldier.ally_side, soldier.place, soldier.behavior,
                            soldier.hitpoints, soldier.hitpoints_max, soldier.escape))
                        # Проверяем, есть ли рядом с бойцом его ездовое животное:
                        if hasattr(soldier, 'mount_uuid') and soldier.mount_uuid\
                                and self.metadict_soldiers.get(soldier.mount_uuid):
                            mount_place_field = self.point_to_field(place, 3)
                            mount = self.metadict_soldiers[soldier.mount_uuid]
                            for point in mount_place_field:
                                for el in self.dict_battlespace[point]:
                                    if type(el) == tuple\
                                            and el[1] == 'mount'\
                                            and el[-1] == soldier.mount_uuid:
                                        self.dict_battlespace[point].remove(el)
                                        mount.escape = True
                                        mount.defeat = True
                # Чистим лошадиные высоты с карты, раз уж так криво сделано:
                if el == 'mount_height' and not tuple in [type(el) for el in content]:
                    try:
                        content.remove(el)
                    except ValueError:
                        #traceback.print_exc()
                        pass
                # Убираем метки "Града стрел":
                if el == 'volley':
                    try:
                        content.remove(el)
                    except ValueError:
                        #traceback.print_exc()
                        pass

    def print_battle_statistics(self):
        """Вывод статистики после боя. Убитые, раненые по отрядам."""
        for key, squad in self.squads.items():
            casualty = squad.casualty
            if not hasattr(squad, 'experience'):
                squad.experience = 0
            squad_hitpoints_max = sum([soldier.hitpoints_max for soldier\
                in squad.metadict_soldiers.values()])
            squad_hitpoints_new = sum([soldier.hitpoints for soldier\
                in squad.metadict_soldiers.values()\
                if not soldier.hitpoints <= 0])
            print('--------------------------------------------------------------------------------')
            print('{0} {1} {2} exp {3} hp {4}/{5} (dead {6}% disabled {7}% captured {8}%) fall {9}%, injured {10}%, light {11}%, escape {12}% lucky {13}%'.format(
                    squad.ally_side, key.zone, key.type, squad.experience,
                    squad_hitpoints_new, squad_hitpoints_max,
                    casualty['dead_percent'], casualty['disabled_percent'],
                    casualty['captured_percent'], casualty['fall_percent'],
                    casualty['injured_percent'], casualty['light_injured_percent'],
                    casualty['escape_percent'], casualty['lucky_one_percent']))
            dict_dead = {}
            dict_disabled = {}
            dict_capture = {}
            dict_fall = {}
            for soldier in squad.metadict_soldiers.values():
                if hasattr(soldier, 'death') and soldier.death == True:
                    if not soldier.rank in dict_dead:
                        dict_dead[soldier.rank] = 1
                    elif soldier.rank in dict_dead:
                        dict_dead[soldier.rank] += 1
                elif hasattr(soldier, 'disabled') and soldier.disabled == True:
                    if not soldier.rank in dict_disabled:
                        dict_disabled[soldier.rank] = 1
                    elif soldier.rank in dict_disabled:
                        dict_disabled[soldier.rank] += 1
                elif hasattr(soldier, 'captured') and soldier.captured == True:
                    if not soldier.rank in dict_capture:
                        dict_capture[soldier.rank] = 1
                    elif soldier.rank in dict_capture:
                        dict_capture[soldier.rank] += 1
                elif soldier.hitpoints <= 0:
                    if not soldier.rank in dict_fall:
                        dict_fall[soldier.rank] = 1
                    elif soldier.rank in dict_fall:
                        dict_fall[soldier.rank] += 1
            dict_dead = OrderedDict(reversed(sorted(dict_dead.items(),key=lambda x: x)))
            dict_disabled = OrderedDict(reversed(sorted(dict_disabled.items(),key=lambda x: x)))
            dict_capture = OrderedDict(reversed(sorted(dict_capture.items(),key=lambda x: x)))
            dict_fall = OrderedDict(reversed(sorted(dict_fall.items(),key=lambda x: x)))
            for key, el in dict_dead.items():
                print('dead', el, key)
            for key, el in dict_disabled.items():
                print('disabled', el, key)
            for key, el in dict_capture.items():
                print('captured', el, key)
            for key, el in dict_fall.items():
                print('fall', el, key)
            if hasattr(squad, 'battle_stat'):
                battle_stat = squad.battle_stat
                battle_stat = OrderedDict(sorted(battle_stat.items(),key=lambda x: x))
                for attack, stat in battle_stat.items():
                    print(attack, stat)

    def save_soldiers_to_database(self):
        """Сохраняем солдат в базу данных."""
        # TODO: добавь запрос на "y", прежде чем сохранять.
        squads_list_DB = self.database.print_squads()
        for squad in self.squads.values():
            if squad.name in squads_list_DB:
                print('Отряд будет сохранён в БД: ', squad.name, self.database.database_path)
                for soldier in squad.metadict_soldiers.values():
                    print('SAVE: {0} {1} {2} hp: {3}/{4} vic/def {5}/{6}'.format(
                        soldier.ally_side, soldier.rank, soldier.name,
                        soldier.hitpoints, soldier.hitpoints_max, soldier.victories, soldier.defeats,
                        ))
                    self.database.soldier_to_database(soldier)
                self.database.commit()

#-------------------------------------------------------------------------
# Интерфейс:

class interface(battlescape):
    """Описание класса.
    
    """
    # Шаблоны отрядов для интерфейса:
    metadict_squads = squads.metadict_squads
    #map_default = 'battle_map'
    # Подключаемся к базе данных солдат:
    database = database.database()

    def select_map(self, filter_string = None):
        """Выбор карты поля боя."""
        maps_list = [key for key in maps.__dict__.keys()\
                if not key.startswith('__') and not callable(key)]
        #print('------------------------------------------------------------')
        if filter_string and filter_string in maps_list:
            map_name = filter_string
            return getattr(maps, map_name)
        elif filter_string:
            maps_list = [key for key in maps_list\
                    if filter_string in key]
            if len(maps_list) == 1:
                map_name = maps_list[0]
                return getattr(maps, map_name)
            else:
                for number, map_name in enumerate(maps_list):
                    print(number, map_name)
                string_number = input('---Выбор карты (введите номер): ')
                if string_number:
                    map_name = maps_list[int(string_number)]
                    return getattr(maps, map_name)
                else:
                    return getattr(maps, maps_list[0])
        else:
            for number, map_name in enumerate(maps_list):
                print(number, map_name)
            string_number = input('---Выбор карты (введите номер): ')
            if string_number:
                map_name = maps_list[int(string_number)]
                return getattr(maps, map_name)
            else:
                return getattr(maps, maps_list[0])

    def select_squads(self, selected_map, zones_squads_list = None):
        """Выбор отрядов и зон расположения."""
        self.create_battlespace(selected_map)
        spawn_zones_dict = self.find_spawn_zones()
        spawn_zones_list = list(spawn_zones_dict.keys())
        squads_list = list(sorted(squads.metadict_squads.keys()))
        # Пополняем список отрядами из базы данных:
        print('Database :', self.database.print_squads())
        squads_list.extend(self.database.print_squads())
        #print('------------------------------------------------------------')
        zones_squads_dict = {}
        if zones_squads_list:
            for number, el in enumerate(zones_squads_list):
                if el in spawn_zones_list:
                    spawn_zone = el
                    spawn_zones_list.remove(spawn_zone)
                    squad_filter = zones_squads_list[number + 1]
                    squads_list_slice = [key for key in squads_list\
                            if squad_filter in key]
                    if len(squads_list_slice) == 1:
                        squad_name = squads_list_slice[0]
                        zones_squads_dict[spawn_zone] = squad_name
                    else:
                        if int(spawn_zone[-1]) < 5:
                            spawn_type = self.ally_side
                        elif int(spawn_zone[-1]) >= 5:
                            spawn_type = self.enemy_side
                        print('Spawn:', spawn_zone, spawn_type)
                        for number, squad_name in enumerate(squads_list_slice):
                            print(number, squad_name)
                        string_number = input('---{0} (номер отряда): '.format(spawn_zone))
                        if string_number:
                            squad_name = squads_list_slice[int(string_number)]
                            zones_squads_dict[spawn_zone] = squad_name
                        else:
                            squad_name = squads_list_slice[0]
                            zones_squads_dict[spawn_zone] = squad_name
        if len(zones_squads_dict) < 2:
            for spawn_zone in spawn_zones_list:
                for number, squad_name in enumerate(squads_list):
                    print(number, squad_name)
                string_number = input('---{0} (номер отряда): '.format(spawn_zone))
                if string_number:
                    squad_name = squads_list[int(string_number)]
                    zones_squads_dict[spawn_zone] = squad_name
        return zones_squads_dict

#-------------------------------------------------------------------------
# Тесты:

if __name__ == '__main__':
    # Обработка аргументов командной строки:
    console = interface()
    parser = create_parser()
    namespace = parser.parse_args()
    if namespace.map:
        selected_map = console.select_map(namespace.map)
    else:
        selected_map = console.select_map()
    if namespace.squads:
        zones_squads_dict = console.select_squads(selected_map, namespace.squads)
    else:
        zones_squads_dict = console.select_squads(selected_map)
    # Симуляция:
    battle = battle_simulation()
    battle.prepare_battlefield(selected_map, zones_squads_dict)
    try:
        battle.start(max_rounds = namespace.rounds, commands = namespace.commands)
        # Сохраняем отряды в БД:
        if namespace.save:
            battle.save_soldiers_to_database()
        # Смотрим сколько народу пострадало:
        battle.print_battle_statistics()
    except KeyboardInterrupt:
        #traceback.print_exc()
        battle.print_battle_statistics()
