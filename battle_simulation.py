#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import math
import random
import timeit
import time
import traceback
import collections
from collections import Counter
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
                        help='Например: zone_1 legionary zone_5 hoplites zone_11 Squad\
                                (номера зон спавна пишутся на карте: 01 = zone_0, zone_1, zone_01)'
                        )
    parser.add_argument('-r', '--rounds',
                        action='store', dest='rounds', type=int, default=10,
                        help='Например: 10 -- раундов боя'
                        )
    parser.add_argument('-T', '--test',
                        action='store', dest='test', type=int, default=0,
                        help='Например: 10 -- тестовых боёв'
                        )
    parser.add_argument('-m', '--map',
                        action='store', dest='map', type=str,
                        help='Например: battle_map'
                        )
    parser.add_argument('-c', '--commands',
                        action='store_true', dest='commands', default=False,
                        help='Позволяет команды отрядам: dodge, fearless, retreat, move, т.д.\
                                (-command -- отмена, auto -- автопилот)'
                        )
    parser.add_argument('-w', '--weather',
                        action='store', dest='weather', type=str,
                        help='Доступно: night, wind, water, underwater'
                        )
    parser.add_argument('-v', '--visual',
                        action='store_true', dest='visual', default=False,
                        help='Показывает ходы каждого бойца.'
                        )
    parser.add_argument('-s', '--save',
                        action='store_true', dest='save', default=False,
                        help='Сохранить отряды после боя.'
                        )
    parser.add_argument('-S', '--stop',
                        action='store_true', dest='stop', default=False,
                        help='Останавливать бой, когда враги кончились.'
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
                        action='store_true', dest='rest', default=False,
                        help='Короткий отдых перед боем, лечение всех.'
                        )
    parser.add_argument('--rearm',
                        action='store_true', dest='rearm', default=False,
                        help='Пополнение боекомплекта, оружия, щитов.'
                        )
    return parser

#-------------------------------------------------------------------------
# Функции:

def first(s):
    '''Return the first element from an ordered collection
       or an arbitrary element from an unordered collection.
       Raise StopIteration if the collection is empty.
    '''
    return next(iter(s))

#-------------------------------------------------------------------------
# Классы:

class battle_simulation(battlescape):
    """Описание класса.
    
    """
    # Раунд боя:
    battle_round = 0
    winner = None
    # Боец переходит в оборону, если враг в пределах 3x3 клеток сильнее друзей:
    engage_danger = 0
    # Для магов. Если врагов пострадает вчетверо больше, чем наших, то бьём AoE-спеллом:
    danger_factor = 4
    # Для солдат. Если 10% отряда под ударом зонального заклинания, то отряд отступает.
    danger_percent = 0.1
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
    # Зоны 00-49 -- BLUEFOR, зоны 50-99 -- OPFOR:
    for number in range(0, 10):
        zone_name = 'zone_0{n}'.format(n = number)
        if not zone_name in ally_zones:
            ally_zones.append(zone_name)
    for number in range(10, 50):
        zone_name = 'zone_{n}'.format(n = number)
        if not zone_name in enemy_zones:
            ally_zones.append(zone_name)
    for number in range(50, 100):
        zone_name = 'zone_{n}'.format(n = number)
        enemy_zones.append(zone_name)

    def prepare_battlefield(self, battle_map, zones_squads_dict):
        """Подготовка поля боя.
        
        - Создание поля боя.
        - Генерация отрядов.
        - Размещение солдат.
        """
        self.create_battlespace(battle_map)
        self.squads = self.create_squads(zones_squads_dict)
        self.metadict_soldiers = self.create_metadict_soldiers(self.squads)
        # Размещаем солдат на поле боя в точках спавна:
        self.place_soldiers()
        for key,squad in self.squads.items():
            if 'commander' in [soldier.behavior for soldier in squad.metadict_soldiers.values()
                    if soldier.__dict__.get('place')]:
                self.set_squad_battle_order(squad, key.zone)
            #[print(el) for el in squad.battle_order.items()]
            for soldier in squad.metadict_soldiers.values():
                # ЗАМЕТКА: Даём каждому солдату ссылку на симуляцию и словарь остальных
                # ------------------------------------------------------------
                # Это понадобится для нацеливания заклинаний в их функциях.
                # При записи бойца в базу данных этот словарь будет обнуляться.
                # ------------------------------------------------------------
                soldier.squad = squad
                soldier.battle = battle
                soldier.metadict_soldiers = self.metadict_soldiers
                soldier.set_actions_base(squad)
                soldier.set_actions(squad)
            # Командование отряда начинает свою работу:
            self.set_squad_command_and_control(squad)
            squad.commands = self.squad_AI(squad, squad.commander, commands = False)
            for soldier in squad.metadict_soldiers.values():
                if squad.commands:
                    soldier.commands.extend(squad.commands)
        # Подготовка к бою (бонусные хиты, заклинания, отдых и лечение):
        for key,squad in self.squads.items():
            self.set_squad_buffs(squad)
            self.set_squad_spells_bless(squad)
            self.set_squad_spells_personal(squad)
            self.set_squad_heal(squad)
            # Пополнение боекомплекта:
            if namespace.rearm:
                self.set_squad_rearm(squad)
            # Короткий отдых (но сначала перевязка):
            if namespace.rest:
                for n in range (0,60):
                    self.set_squad_heal(squad, heal_all = True)
                self.set_squad_short_rest(squad)
            # Сумма бонусных хитов отряда:
            squad.bonus_hitpoints_max = sum([soldier.bonus_hitpoints for soldier\
                in squad.metadict_soldiers.values()])
        # Эффекты погоды:
        if namespace.weather:
            #weather_list = namespace.weather.split()
            if 'night' in namespace.weather:
                for point in self.dict_battlespace.keys():
                    if not 'obscure_terrain' in self.dict_battlespace[point]:
                        self.dict_battlespace[point].append('obscure_terrain')
            if 'wind' in namespace.weather:
                for point in self.dict_battlespace.keys():
                    if not 'warding_wind' in self.dict_battlespace[point]:
                        self.dict_battlespace[point].append('warding_wind')
            if 'water' in namespace.weather:
                for point in self.dict_battlespace.keys():
                    if not 'water' in self.dict_battlespace[point]:
                        self.dict_battlespace[point].append('water')
            if 'underwater' in namespace.weather:
                for point in self.dict_battlespace.keys():
                    if not 'underwater' in self.dict_battlespace[point]:
                        self.dict_battlespace[point].append('underwater')
                    if not 'height' in self.dict_battlespace[point]:
                        self.dict_battlespace[point].append('height')
        # Вывод карты до начала боя:
        if not namespace.test:
            print_ascii_map(battle.gen_battlemap())

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
            squad.zone = zone
            squad.type = squad_type
            squad.exit_points = self.find_zone_exit_points(squad.zone)
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
                                    self.place_unit(mount, spawn_point.place)
                                # Метка солдата, это кортеж/кортежи на поле боя:
                                self.place_unit(soldier, spawn_point.place)
                                break

    def place_unit(self, soldier, place):
        """Боец появляется на поле боя.
        
        Каждая метка, это кортеж со стороной юнита, его типом и uuid.
        """
        # TODO: Сделай нормальный поиск по namedtuple.
        # ------------------------------------------------------------
        # Сейчас бойцы на карте ищутся перебором type(tuple), это неэффективно.
        # Проблема в том, что namedtuple не определяется как обычный кортеж
        # ------------------------------------------------------------
        #soldier_tuple = self.namedtuple_soldier(side,behavior,uuid)
        soldier_tuple = (soldier.ally_side, soldier.behavior, soldier.level, soldier.uuid)
        # Дополняем словарь поля боя и вырубаем цикл, так как спавн занят:
        if soldier.size == 'medium'\
                or soldier.size == 'small'\
                or soldier.size == 'tiny':
            self.dict_battlespace[place].append(soldier.ally_side)
            self.dict_battlespace[place].append(soldier_tuple)
            # Даём бойцу его координаты:
            self.metadict_soldiers[soldier.uuid].set_coordinates(place)
            return True
        # Большие существа занимают 2x2 тайла:
        elif soldier.size == 'large':
            soldier_place_field = self.point_to_field_2x2(place)
            for point in soldier_place_field:
                if point in self.dict_battlespace:
                    self.dict_battlespace[point].append(soldier_tuple)
                    self.dict_battlespace[point].append(soldier.ally_side)
                    self.dict_battlespace[point].append('mount_height')
            # Даём бойцу его координаты:
            self.metadict_soldiers[soldier.uuid].set_coordinates(place)
            return True
        elif soldier.size == 'huge':
            soldier_place_field = self.point_to_field(place)
            for point in soldier_place_field:
                if point in self.dict_battlespace:
                    self.dict_battlespace[point].append(soldier_tuple)
                    self.dict_battlespace[point].append(soldier.ally_side)
                    self.dict_battlespace[point].append('mount_height')
            # Даём бойцу его координаты:
            self.metadict_soldiers[soldier.uuid].set_coordinates(place)
            return True

    def find_zone_exit_points(self, zone):
        """Точки выхода с карты для бегущих с поля боя.
        
        Это точки с меткой "exit" в зоне спавна отряда:
        - Метки "exit" ставятся по краям карты, если край не занят "stop_terrain" или "zone_border".
        - Если зона спавна отряда не встречается с краем карты, то он не сможет сбежать с поля боя.
        """
        exit_points = []
        for place, content in self.dict_battlespace.items():
            if 'exit' in content and zone in content:
                exit_points.append(place)
        return exit_points


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

    def set_squad_heal(self, squad, heal_all = False):
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
                if bless_list and soldier.hitpoints <= soldier.hitpoints_max / 2\
                        or bless_list and heal_all and soldier.hitpoints < soldier.hitpoints_max:
                    #print(bless_type, soldier.rank)
                    max_hit_dice = int(soldier.hit_dice.split('d')[1])
                    heal = bless_list.pop() + max_hit_dice
                    soldier.set_hitpoints(heal = heal)
                    soldier.treated = True
                    #soldier.fall = False
                    #print('{side} Feat_Healer, {p} {b} {n} heal: {hit}/{hit_max} ({heal})'.format(
                    #    side = soldier.ally_side,
                    #    p = soldier.place,
                    #    b = soldier.behavior,
                    #    n = soldier.name,
                    #    hit = soldier.hitpoints,
                    #    hit_max = soldier.hitpoints_max,
                    #    heal = heal,
                    #    ))

    def set_squad_buffs(self, squad):
        """Кастеры баффают солдат.
    
        Эта функция запускается до боя.
        """
        # TODO: перенести в функции способностей.
        # Bardic_Inspiration уже там.
        for soldier in squad.metadict_soldiers.values():
            # Воодушевляющий лидер:
            if soldier.class_features.get('Feat_Inspiring_Leader')\
                    and soldier.inspiring_leader:
                ally_number = 6
                bonus_hitpoints = soldier.mods['charisma'] + soldier.level
                soldier.inspiring_leader = False
                # Передаём бонусные хиты:
                soldiers_list = self.select_soldiers_for_bless(ally_number,
                        squad.ally_side, 'bonus_hitpoints')
                for ally_soldier in soldiers_list:
                    ally_soldier.set_hitpoints(bonus_hitpoints = bonus_hitpoints)
            # Вдохновение барда:
            if soldier.class_features.get('Bardic_Inspiration') and soldier.inspiring_bard_number:
                spell_dict = soldier.spells_generator.get_spell_dict('Bardic_Inspiration')
                soldiers_list = self.select_soldiers_for_bless(spell_dict['attacks_number'],
                        squad.ally_side, spell_dict['effect'])
                for ally_soldier in soldiers_list:
                    soldier.try_spellcast('Bardic_Inspiration',
                            gen_spell = {'target_uuid':ally_soldier.uuid},
                            use_action = False, use_spell_slot = 'feature')
                    #print(ally_soldier.rank, ally_soldier.buffs.keys())

    def set_squad_spells_bless(self, squad):
        """Жрецы и маги обкастовывают союзников, начиная с командиров.
    
        Эта функция запускается до боя.
        """
        for soldier in squad.metadict_soldiers.values():
            # Заклинания и концентрация на них:
            if 'spellcast' in soldier.commands and soldier.spells\
                    and not soldier.concentration:
                # TODO: bless_list создавать из soldier.spells.
                ## -------------------------------------------------
                # Сначала заклинания высших уровней, затем меньших.
                # В заклинаниях указывай buff = True.
                ## -------------------------------------------------
                bless_list = [
                        # Используя Mage_Armor на союзника маг тратит действие.
                        # И поэтому не может применить его на себя в set_squad_spells_personal
                        'Aid',
                        'Bless',
                        'Shield_of_Faith',
                        'Dragon_Breath',
                        'Stoneskin',
                        #'Longstrider',
                        #'Mage_Armor',
                        ]
                for bless in bless_list:
                    spell_dict = soldier.try_spellcast(bless, gen_spell = False, use_action = False)
                    if spell_dict:
                        soldiers_list = self.select_soldiers_for_bless(
                                spell_dict['attacks_number'], squad.ally_side, spell_dict['effect'])
                        for ally_soldier in soldiers_list:
                            ally_soldier.set_buff(spell_dict)
                            #print(ally_soldier.rank, ally_soldier.buffs.keys())

    def set_squad_spells_personal(self, squad):
        """Солдаты использует руны, заклинания, зелья.
    
        Эта функция запускается до боя.
        """
        for soldier in squad.metadict_soldiers.values():
            # Используем руны и заклинания в предметах:
            if 'runes' in soldier.commands:
                spells_list = [
                        'False_Life',
                        'Mage_Armor',
                        'Barkskin',
                        'Heroism',
                        'Longstrider',
                        'Stoneskin',
                        ]
                for spell in spells_list:
                    if not soldier.armor['armor_use'] and spell == 'Mage_Armor':
                        soldier.use_item('Mage_Armor', gen_spell = True, use_action = False)
                    if soldier.armor['armor_class'] < 16 and spell == 'Barkskin':
                        soldier.use_item('Barkskin', gen_spell = True, use_action = False)
                    if not soldier.bonus_hitpoints and spell == 'Heroism':
                        soldier.use_item('Heroism', gen_spell = True, use_action = False)
                    if not soldier.bonus_hitpoints and spell == 'False_Life':
                        soldier.use_item('False_Life', gen_spell = True, use_action = False)
                    if spell == 'Longstrider':
                        soldier.use_item('Longstrider', gen_spell = True, use_action = False)
                    if spell == 'Stoneskin':
                        soldier.use_item('Stoneskin', gen_spell = True, use_action = False)
            # Используем зелья:
            # TODO: Вообще, зелья дублируют руны по сути и содержимому.
            if 'potions' in soldier.commands:
                spells_list = [
                        'False_Life',
                        'Antidote',
                        ]
                for spell in spells_list:
                    if not soldier.bonus_hitpoints and spell == 'False_Life':
                        soldier.use_item('False_Life', gen_spell = True, use_action = False)
                    if not 'antidote' in soldier.buffs and spell == 'Antidote':
                        soldier.use_item('Antidote', gen_spell = True, use_action = False)
            # Тратим слоты заклинаний:
            if 'spellcast' in soldier.commands and soldier.spells:
                spells_list = [
                        'Armor_of_Agathys',
                        'False_Life',
                        'Mage_Armor',
                        'Barkskin',
                        'Blink',
                        'Mirror_Image',
                        ]
                # TODO: сделай функцию выбора в классе soldier_fight. Пусть возвращает True.
                for spell in spells_list:
                    if spell in [spell[-1] for spell in soldier.spells.keys()]:
                        if soldier.bonus_hitpoints <= 0 and spell == 'Armor_of_Agathys':
                            soldier.try_spellcast(spell, gen_spell = True, use_action = False)
                        if not soldier.armor['armor_use'] and spell == 'Mage_Armor':
                            soldier.try_spellcast(spell, gen_spell = True, use_action = False)
                        if soldier.armor['armor_class'] < 16 and spell == 'Barkskin'\
                                and not soldier.concentration:
                            soldier.try_spellcast(spell, gen_spell = True, use_action = False)
                        if not soldier.bonus_hitpoints and spell == 'False_Life':
                            soldier.try_spellcast(spell, gen_spell = True, use_action = False)
                        if spell == 'Blink':
                            soldier.try_spellcast(spell, gen_spell = True, use_action = False)
                            if 'blink' in soldier.buffs and dices.dice_throw('1d20') > 11:
                                self.clear_battlemap(uuid_for_clear = soldier.uuid)
                                soldier.blink = True
                        if spell == 'Mirror_Image':
                            soldier.try_spellcast(spell, gen_spell = True, use_action = False)
                        if spell == 'Stoneskin' and not soldier.concentration:
                            soldier.try_spellcast(spell, gen_spell = True, use_action = False)
                        #print(soldier.rank, soldier.buffs.keys())

    def select_soldiers_for_bless(self, number, ally_side, bless_type):
        """Выбираем солдат для Bless, Inspiring_Leader, Bardic_Inspiration и т.д.
        
        Сначала офицеры, затем ветераны, после обычные бойцы.
        Ездовых животных не выбираем.
        """
        # TODO: В список не должны включаться объекты с тегом mechanism
        # А вот лошадок можно и нужно лечить, добавь параметр get_all
        soldiers_list = [ ] 
        max_level = max([soldier.level for soldier in self.metadict_soldiers.values()])
        # Сначала выбираем героев, а затем командиров и простых бойцов:
        for level in reversed(range(0, max_level +1)):
            for soldier in self.metadict_soldiers.values():
                if not number <= 0\
                        and soldier.hero\
                        and not soldier.behavior == 'mount'\
                        and not soldier.__dict__.get(bless_type)\
                        and not bless_type in soldier.__dict__.get('buffs',{})\
                        and soldier.ally_side == ally_side\
                        and soldier.level == level:
                    soldiers_list.append(soldier)
                    number -= 1
        for level in reversed(range(0, max_level +1)):
            for soldier in self.metadict_soldiers.values():
                if not number <= 0\
                        and not soldier.hero\
                        and not soldier.behavior == 'mount'\
                        and not soldier.__dict__.get(bless_type)\
                        and not bless_type in soldier.__dict__.get('buffs',{})\
                        and soldier.ally_side == ally_side\
                        and soldier.level == level:
                    soldiers_list.append(soldier)
                    number -= 1
        return soldiers_list

    def set_squad_rearm(self, squad):
        """Пополнение боекомплекта."""
        bless_type = 'rearm'
        soldiers_list_elite = self.select_soldiers_for_bless(
                len(self.metadict_soldiers), squad.ally_side, bless_type)
        for soldier in soldiers_list_elite:
            soldier.set_short_rest_rearm()

    def set_squad_short_rest(self, squad):
        """Короткий отдых (1 час).

        """
        # TODO: Короткий отдых восстанавливает способности:
        # - способности бойца
        # - заклинания колдуна
        # - перевязку можно повторить
        bless_type = 'short_rest'
        soldiers_list_elite = self.select_soldiers_for_bless(
                len(self.metadict_soldiers), squad.ally_side, bless_type)
        for soldier in soldiers_list_elite:
            soldier.set_short_rest_rearm()
            soldier.set_short_rest_heal()
            soldier.set_short_rest_restoration()
            # Убираем бонусные хитпоинты (хотя они бывают разных типов):
            if soldier.bonus_hitpoints:
                soldier.set_hitpoints(bonus_hitpoints = 0)
            # Друид возвращает облик человека:
            if soldier.wild_shape:
                soldier.return_old_form(self.metadict_soldiers)

    def set_squad_battle_stat(self, attack_result, squad, attack_choice = None):
        """Подсчёт попадания, промахов и урона под каждый вид оружия."""
        if attack_result:
            if not hasattr(squad, 'battle_stat'):
                squad.battle_stat = {}
            if not attack_choice:
                attack_choice = attack_result.get('attack_choice',attack_result.get('spell_choice'))
            attack_key_hit = tuple(list(attack_choice) + ['hit'])
            attack_key_fatal = tuple(list(attack_choice) + ['fatal'])
            attack_key_miss = tuple(list(attack_choice) + ['miss'])
            attack_key_damage = tuple(list(attack_choice) + ['damage'])
            attack_key_damage_temp_hp = tuple(list(attack_choice) + ['damage_temp_hp'])
            attack_key_shield_impact = tuple(list(attack_choice) + ['shield_impact'])
            attack_key_hit_friendly = tuple(list(attack_choice) + ['damage_friend'])
            if attack_result.get('hit')\
                    and not attack_result.get('victim_side') == squad.ally_side:
                if not attack_key_damage in squad.battle_stat and attack_result.get('damage',0) > 0:
                    squad.battle_stat[attack_key_damage] = attack_result['damage']
                elif attack_key_damage in squad.battle_stat and attack_result.get('damage',0) > 0:
                    squad.battle_stat[attack_key_damage] += attack_result['damage']
                if not attack_key_damage_temp_hp in squad.battle_stat\
                        and attack_result.get('bonus_hitpoints_damage',0) > 0:
                    squad.battle_stat[attack_key_damage_temp_hp] = attack_result.get(
                            'bonus_hitpoints_damage',0)
                elif attack_key_damage_temp_hp in squad.battle_stat\
                        and attack_result.get('bonus_hitpoints_damage',0) > 0:
                    squad.battle_stat[attack_key_damage_temp_hp] += attack_result.get(
                            'bonus_hitpoints_damage',0)
                if not attack_key_hit in squad.battle_stat:
                    squad.battle_stat[attack_key_hit] = 1
                else:
                    squad.battle_stat[attack_key_hit] += 1
            # Учитывем дружественный огонь:
            elif attack_result.get('hit')\
                    and attack_result.get('victim_side') == squad.ally_side:
                if not attack_key_hit_friendly in squad.battle_stat and attack_result.get('damage',0) > 0:
                    squad.battle_stat[attack_key_hit_friendly] = attack_result['damage']
                elif attack_key_damage in squad.battle_stat and attack_result.get('damage',0) > 0:
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
            if not namespace.test:
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
            # Чистим списки закончившихся заклинаний, работает таймер:
            # Срабатывают повторяющиеся каждый раунд заклинания вроде Heroism:
            # TODO: последний раунд боя не учитывается
            self.all_clear_spells()
            self.all_get_buffs()
            for squad in self.squads.values():
                # Тяжелораненые могут погибнуть:
                self.fall_to_death(squad)
                # Отряд делает ход:
                self.round_run_squad(squad, commands)
                # Выводим карту после хода каждого отряда:
                if not namespace.test:
                    print_ascii_map(self.gen_battlemap())
                    time.sleep(0.2)
            stop = timeit.default_timer()
            self.battle_round = battle_round
            if not namespace.test:
                print('round end:', battle_round, 'time:', round(stop - start, 3))
            # Подкрепления в конце хода (кому не хватило точек спавна):
            if namespace.reinforce:
                self.place_soldiers()
            # Заканчиваем бой, если остались солдаты одной стороны:
            if namespace.stop and not namespace.rest and not namespace.rearm:
                sides_list = []
                for place, content in self.dict_battlespace.items():
                    for el in content:
                        if type(el) == tuple:
                            sides_list.append(el[0])
                sides_dict = Counter(sides_list)
                if len(sides_dict.keys()) == 1:
                    self.winner = list(sides_dict.keys())[0]
                    self.release_captures(self.winner)
                    break
                # Бывает, что с поля боя убегают все:
                elif not sides_dict:
                    self.release_captures('OPFOR')
                    self.release_captures('BLUEFOR')
                    self.winner = None
                    break
        # Уточняем потери по результатам боя:
        for squad in self.squads.values():
            self.fall_to_death(squad)
            squad.casualty = self.calculate_casualty(squad)

    def round_run_squad(self, squad, commands = False):
        """Ход отряда."""
        # Обновляем карту препятствий для поиска пути:
        self.matrix = self.map_to_matrix(self.battle_map, self.dict_battlespace)
        # Список команд на текущий ход:
        self.set_squad_command_and_control(squad)
        squad.commands = self.squad_AI(squad, squad.commander, commands)
        # Зоны контроля сбрасываются перед ходом отряда:
        squad.dict_control_zones = {}
        for key in self.dict_battlespace.keys():
            squad.dict_control_zones[key] = []
        # Боец действует, только если он находится на карте и боеспособен:
        for uuid, soldier in squad.metadict_soldiers.items():
            # Зональные эффекты до начала раунда бойца:
            # Зональные эффекты бьют в том числе и раненых:
            if soldier.get_coordinates():
                self.get_zone_effects(soldier, squad, before_round = True)
                # Маг под "Blink" возвращается с эфирного плана:
                if 'blink' in soldier.buffs and soldier.blink and not soldier.defeat:
                    self.place_unit(soldier, soldier.place)
                    soldier.blink = False
            if soldier.get_coordinates() and soldier.hitpoints > 0\
                    and not soldier.defeat\
                    and not 'sleep' in soldier.debuffs\
                    and not 'inactive' in squad.commands:
                # Начинаем раунд солдата
                self.round_run_soldier(soldier, squad)
                # Зона контроля для атак реакцией.
                self.set_control_zone(soldier, squad)
            # Зональные эффекты после раунда бойца. От таких можно сбежать:
            if soldier.get_coordinates():
                # Маг под "Blink" уходит в конце хода на эфирный план:
                if 'blink' in soldier.buffs and dices.dice_throw('1d20') > 11:
                    self.clear_battlemap(uuid_for_clear = soldier.uuid)
                    soldier.blink = True
                self.get_zone_effects(soldier, squad)
                # Ставим ауру, на случай, если боец применил заклинание, но не ходил:
                if soldier.concentration and soldier.concentration.get('zone_self'):
                    spell_dict = soldier.concentration
                    zone_radius = round(spell_dict['radius'] / self.tile_size)
                    self.change_place_effect(spell_dict['effect'],
                            soldier.place, soldier.place, zone_radius)
                    if spell_dict.get('zone_danger'):
                        self.change_place_effect('danger_terrain',
                                soldier.place, soldier.place, zone_radius)

    def set_control_zone(self, soldier, squad):
        """Зона контроля бойца. Для атак реакцией в ход врага.

        Зона контроля = досягаемость ближних атак:
        - Атака реакцией, если враг покидает зону контроля без Disengage_Action.
        # Зона 3x3 клетки (кинжалы, мечи, копья)
        # ..................................
        # ..^^^.............................
        # ..<C>.............................
        # ..^^^.............................
        # ..................................
        # # Зона 21 клетки (пики, глефы, алебарды)
        # ..................................
        # ..^^^.............................
        # .<^^^>............................
        # .<<C>>............................
        # .<^^^>............................
        # ..^^^.............................
        # ..................................
        """
        reach_ranges = [soldier.attacks[attack].get('attack_range', 0) for attack in soldier.attacks.keys()
                if attack[0] == 'close' or attack[0] == 'reach']
        if reach_ranges:
            zone_radius = round(max(reach_ranges) / self.tile_size)
            zone_list = self.point_to_field(soldier.place, zone_radius)
            if zone_radius > 1:
                zone_list = [point for point in zone_list\
                        if inside_circle(point, soldier.place, zone_radius)]
            soldier_tuple = (squad.ally_side, soldier.behavior, soldier.uuid)
            for point in zone_list:
                squad.dict_control_zones[point].append(soldier_tuple)

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
                squad.enemy_recon = self.recon_enemy_side(
                        squad.enemies, squad.allies, squad.commanders_list)
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
        """Командиры возвращают свои координаты и уровень опасности рядом.
        
        Если не осталось командиров в отряде, то командиром считается кто-то из бойцов.
        """
        commanders_list = []
        for uuid, soldier in squad.metadict_soldiers.items():
            if hasattr(soldier, 'place') and soldier.place\
                    and soldier.hitpoints > 0\
                    and soldier.behavior == 'commander'\
                    and soldier.escape != True\
                    and soldier.defeat != True:
                commander_tuple = self.namedtuple_commander(soldier.place,soldier.danger,soldier.uuid)
                commanders_list.append(commander_tuple)
        # Если командир выбыл, командование принимает обычный боец.
        if not commanders_list:
            for uuid, soldier in squad.metadict_soldiers.items():
                if hasattr(soldier, 'place') and soldier.place\
                        and soldier.hitpoints > 0\
                        and soldier.escape != True\
                        and soldier.defeat != True:
                    commander_tuple = self.namedtuple_commander(soldier.place,soldier.danger,soldier.uuid)
                    commanders_list.append(commander_tuple)
                    break
        return commanders_list

    def commanders_seek_enemies(self, squad):
        """Командиры отряда находят видимых врагов."""
        dict_enemies = {}
        for commander_tuple in squad.commanders_list:
            commander = squad.metadict_soldiers[commander_tuple.uuid]
            # На случай, если враг зачаровал командира:
            if commander.ally_side == squad.ally_side:
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
                if soldier.death:
                    dict_casualty['dead'] += 1
                elif soldier.disabled:
                    dict_casualty['disabled'] += 1
                elif soldier.captured:
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

    def recon_enemy_side(self, enemies_dict, allies_dict, commanders_list):
        """Изучаем видимых противников, делаем выводы.
        
        Ключевое:
        - средняя скорость врага.
        - средняя дистанция до врага.
        - тип и класс самых многочисленных бойцов.
        - распространённые атаки (ranged, throw, reach)
        - зональные заклинания, например: Spirit_Guardians
        """
        enemy_recon = {}
        speed_list = []
        types_list = []
        clases_list = []
        distance_list = []
        attacks_list = []
        danger_list = []
        ally_strenght_list = []
        danger_places = []
        enemy_recon['attack_range'] = 0
        # Обозначаем опасные зоны на поле боя
        # TODO: учитывай только видимые командирам опасные точки.
        for place, elements in self.dict_battlespace.items():
            for el in elements:
                if el == 'danger_terrain':
                    danger_places.append(place)
        # Интересны атаки, которые есть хотя бы у 25% бойцов отряда:
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
            attack_ranges = [value.get('attack_range',0)
                    for value in enemy_soldier.attacks.values()]
            attack_ranges.extend([value.get('attack_range_max',0)
                    for value in enemy_soldier.attacks.values()])
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
        if attack_ranges:
            enemy_recon['attack_range'] = round(max(attack_ranges) / self.tile_size)
        enemy_recon['distance_medial'] = round(sum(distance_list) / len(enemies_dict))
        enemy_recon['distance'] = min(distance_list)
        enemy_recon['danger_places'] = danger_places
        return enemy_recon

    def squad_AI(self, squad, commander, commands):
        """Создаёт список команд на ход."""
        commands_list = []
        if squad.commander and squad.enemies:
            save_distance = squad.enemy_recon['move']
            if squad.enemy_recon['distance'] > save_distance:
                commands_list = ['lead','follow']
                commands_list.append('carefull')
                commands_list.append('attack')
                commands_list.append('spellcast')
                commands_list.append('potions')
                commands_list.append('runes')
            elif squad.enemy_recon['distance'] <= save_distance:
                commands_list = ['lead','follow','engage']
                commands_list.append('carefull')
                commands_list.append('attack')
                commands_list.append('spellcast')
                commands_list.append('potions')
                commands_list.append('runes')
            # Оцениваем опасность зональных заклинаний. Например Spirit_Guardians:
            if squad.enemy_recon['danger_places']:
                danger_places = squad.enemy_recon['danger_places']
                enemy_mages_list = [enemy for enemy in self.metadict_soldiers.values()
                        if enemy.ally_side == commander.enemy_side
                        and enemy.concentration and enemy.concentration.get('zone_danger')]
                # Свои маги тоже небезопасны:
                ally_mages_list = [ally for ally in self.metadict_soldiers.values()
                        if ally.ally_side == commander.ally_side
                        and ally.concentration and ally.concentration.get('zone_danger')
                        and not ally.concentration.get('safe')]
                enemy_mages_list.extend(ally_mages_list)
                if enemy_mages_list:
                    commands_list.append('danger')
                    #print('NYA', enemy_mages_list[0].rank, danger_places)
                    zonal_spell_victims = [soldier for soldier in squad.metadict_soldiers.values()
                            if hasattr(soldier, 'place') and soldier.place in danger_places]
                    if zonal_spell_victims:
                        # Если больше 5% солдат под ударом, то отряд отступает:
                        if len(zonal_spell_victims) > len(squad.metadict_soldiers) * self.danger_percent:
                            if 'engage' in commands_list:
                                commands_list.remove('engage')
                            commands_list.append('disengage')
                            #print(len(zonal_spell_victims))
                        #else:
                        #    # TODO: это не работает, команды обнуляются в set_actions
                        #    for soldier in zonal_spell_victims:
                        #        soldier.commands.append('disengage')
        elif squad.commander and not squad.enemies:
            commands_list = ['lead','follow']
        elif not squad.commander:
            # TODO: disengage использует squad.enemy_recon.
            # А разведка противника не обновляется без командира.
            #commands_list = ['disengage','dodge','attack']
            commands_list = ['retreat', 'rescue']
        if squad.commander:
            # Командир уплотняет строй до 2 солдат на тайл:
            if squad.commander.__dict__.get('close_order_AI'):
                commands_list.append('close_order')
            # Осторожный командир позволяет раненым отступать:
            if squad.commander.__dict__.get('carefull_AI'):
                commands_list.append('very_carefull')
            # Скрытные командиры прячутся за "Fog_Cloud":
            if squad.commander.__dict__.get('sneak_AI'):
                commands_list.append('sneak')
            # Обычный боец -- негодный командир:
            if squad.commander.level < 3:
                commands_list = ['lead','follow']
                commands_list.append('dodge')
                commands_list.append('disengage')
                commands_list.append('carefull')
                commands_list.append('attack')
                commands_list.append('spellcast')
                commands_list.append('potions')
                commands_list.append('runes')
            # Оборонительная тактика:
            if squad.commander.__dict__.get('defender_AI'):
                commands_list = ['carefull','dodge']
                commands_list.append('very_carefull')
                commands_list.append('attack')
                commands_list.append('spellcast')
                commands_list.append('runes')
                commands_list.append('volley')
            # Поиск и атака всех:
            if squad.commander.__dict__.get('seeker_AI'):
                commands_list = ['engage','attack']
                commands_list.append('spellcast')
                commands_list.append('seek')
                #commands_list.append('carefull')
            # Захват пленных:
            if squad.commander.__dict__.get('enslave_AI'):
                commands_list.append('enslave')
                if squad.commander.__dict__.get('unarmed_AI'):
                    commands_list.append('unarmed')
            # Добавляем град стрел без лишних расчётов:
            if squad.commander.__dict__.get('volley_AI'):
                commands_list.append('volley')
                if squad.commander.__dict__.get('volley_AI_random'):
                    commands_list.append('volley_random')
            # Пополняем боекомплект из большого запаса:
            if squad.commander.__dict__.get('rearm_AI'):
                self.set_squad_rearm(squad)
            # Разрешаем заклинания 3 lvl и "божественный канал":
            if squad.commander.__dict__.get('fireball_AI'):
                commands_list.append('fireball')
                commands_list.append('channel')
            # Нацеливание зональных заклинаний, чтобы не задели своих:
            if squad.commander.__dict__.get('accurate_AI'):
                commands_list.append('accurate')
            # Плохие командиры плохо поддерживают строй:
            if squad.commander.level < 5:
                commands_list.append('crowd')
            # Обычный боец -- негодный командир:
            if squad.commander.level < 3:
                commands_list.append('coward')
            # Чучела, иллюзии и механизмы просто стоят:
            if squad.commander.__dict__.get('inactive_AI'):
                commands_list = []
                commands_list.append('inactive')
            # Стремительный командир гонит своих вперёд:
            if squad.commander.__dict__.get('Dash_AI'):
                commands_list.append('dash')
            # Бесстрашные создания бесстрашны, зато трусоватые спасают своих:
            if squad.commander.__dict__.get('brave_AI'):
                commands_list.append('brave')
            if squad.commander.__dict__.get('fearless_AI'):
                commands_list.append('fearless')
            else:
                commands_list.append('rescue')
            if squad.commander.__dict__.get('predator_AI'):
                commands_list.append('select_weaker')
            elif squad.commander.__dict__.get('hunter_AI'):
                commands_list.append('select_strongest')
            # Талант "Идеальное взаимодействие". Свита атакует вражеских командиров:
            elif squad.commander.__dict__.get('commando_AI'):
                commands_list.append('select_strongest')
            # Убийцы убивают схваченного врага. Снайпера стрелют с Feat_Sharpshooter:
            if squad.commander.__dict__.get('killer_AI'):
                commands_list.append('kill')
            if squad.commander.__dict__.get('grappler_AI'):
                commands_list.append('grapple')
            elif squad.commander.__dict__.get('no_grappler_AI'):
                commands_list.append('no_grapple')
            # Друиды превращаются в первом же раунде боя:
            if squad.commander.__dict__.get('changer_AI'):
                commands_list.append('change')
            # Плуты сближаются и отступают:
            if squad.commander.__dict__.get('disengage_AI'):
                commands_list.append('disengage')
            if squad.commander.__dict__.get('recharge_AI'):
                commands_list.append('recharge')
            # Лучники и метатели дротиков должны чуть что отступать:
            if squad.behavior == 'archer' or squad.commander.__dict__.get('archer_AI'):
                if commander.class_features.get('Feat_Sharpshooter'):
                    commands_list.append('volley')
                if 'engage' in commands_list:
                    commands_list.remove('engage')
                if 'carefull' in commands_list and squad.enemies\
                        and squad.enemy_recon['distance'] <= save_distance * 2\
                        or 'very_carefull' in commands_list and squad.enemies\
                        and squad.enemy_recon['distance'] <= save_distance * 4:
                    if 'lead' in commands_list:
                        commands_list.remove('lead')
                        commands_list.append('disengage')
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
        # Морские существа могут плавать:
        if soldier.__dict__.get('water_walk'):
            self.matrix = self.map_to_matrix(self.battle_map, self.dict_battlespace, water_walk = True)
        # Команды отряду считаются личными:
        if squad.commands:
            soldier.commands.extend(squad.commands)
            if soldier.__dict__.get('archer_AI') or soldier.behavior == 'archer':
                if 'engage' in soldier.commands:
                    soldier.commands.remove('engage')
            # Существа с перезарядкой атак не бросаются в бой, пока не готовы:
            if 'recharge' in soldier.commands and len(soldier.metadict_recharge) >= 1:
                if 'engage' in soldier.commands:
                    soldier.commands.remove('engage')
            # Солдат отступает из опасной зоны:
            if 'danger' in soldier.commands and 'danger_terrain' in self.dict_battlespace[soldier.place]:
                if 'engage' in soldier.commands:
                    soldier.commands.remove('engage')
                    soldier.commands.append('disengage')
                    soldier.commands.append('close_order')
            # Солдат сходит с ума от заклинания "Изобилие врагов":
            if 'enemies_abound' in soldier.debuffs and soldier.enemy_side == squad.ally_side:
                enemy_mage = self.metadict_soldiers[soldier.debuffs['enemies_abound']['caster_uuid']]
                enemy_squad = [enemy_squad for enemy_squad in self.squads.values()
                        if enemy_mage.uuid in enemy_squad.metadict_soldiers][0]
                self.clear_battlemap(uuid_for_clear = soldier.uuid)
                self.place_unit(soldier, soldier.place)
                soldier.commands.append('spellcast')
                soldier.commands.append('fearless')
                squad = enemy_squad
        # Осматриваем зону врагов, находим противника:
        self.recon_action(soldier, squad)
        enemy = self.find_enemy(soldier, squad)
        # Солдат отмечает местонахождение врага, если его ещё нет на линии фронта (для битв в темноте):
        if soldier.near_enemies and squad.frontline:
            for enemy in soldier.near_enemies:
                if enemy.place not in squad.frontline:
                    squad.frontline.append(enemy.place)
        # Солдат отступает, если ранен и таков приказ:
        if soldier.hitpoints <= soldier.hitpoints_max * 0.5\
                and 'carefull' in soldier.commands\
                and not 'fearless' in soldier.commands\
                or soldier.hitpoints <= soldier.hitpoints_max * 0.75\
                and'very_carefull' in soldier.commands\
                and not 'fearless' in soldier.commands:
            destination = self.find_spawn(soldier.place, soldier.ally_side)
            destination = random.choice(self.point_to_field(destination))
            self.move_action(soldier, squad, destination, close_order = True)
        # Солдат лечится способностями/зельями, если это необходимо:
        if soldier.hitpoints <= soldier.hitpoints_max * 0.5\
                and 'carefull' in soldier.commands\
                or soldier.hitpoints <= soldier.hitpoints_max * 0.75\
                and'very_carefull' in soldier.commands:
            soldier.use_heal()
        # Солдат отступает к точке спавна, если опасность слишком велика:
        if soldier.danger > self.engage_danger and not soldier.escape:
            destination = self.find_spawn(soldier.place, soldier.ally_side)
            destination = random.choice(self.point_to_field(destination))
            self.move_action(soldier, squad, destination, close_order = False)
            # Испуганный боец может сбежать (но у храброго преимущество):
            soldier.escape = soldier.morality_check_escape(soldier.danger)
            # Командир может отступить в глубину строя:
            if soldier.behavior == 'commander' or 'retreat' in soldier.commands:
                self.move_action(soldier, squad, destination, allow_replace = True)
        # Солдат бежит, если испуган, или таков приказ:
        elif soldier.escape or soldier.fear or 'retreat' in soldier.commands:
            if 'retreat' in soldier.commands:
                soldier.escape = True
            if not soldier.near_enemies:
                soldier.use_dash_action()
            # Бегство к выходу из карты, или к зоне спавна отряда:
            if len(squad.exit_points) > 0:
                destination = random.choice(squad.exit_points)
            else:
                destination = self.find_spawn(soldier.place, soldier.ally_side)
                destination = random.choice(self.point_to_field(destination))
            self.move_action(soldier, squad, destination, close_order = True)
            if 'exit' in self.dict_battlespace[soldier.place]:
                self.clear_battlemap()
        # Отряд может ускориться с dash_action, если таков приказ (и врагов нет рядом):
        if 'dash' in soldier.commands:
            if not enemy or enemy.distance >= round(soldier.move_pool / self.tile_size):
                soldier.use_dash_action()
        # Командир отряда может вести бойцов в ручном режиме:
        if 'move' in soldier.commands and not 'auto' in soldier.commands\
                and soldier.uuid == squad.commander.uuid:
            destination = list(input('---Куда идти? ("10 10", это x=10, y=10): ').split())
            destination = tuple([int(el) for el in destination])
            if destination and len(destination) > 1:
                squad.destination = destination
                self.move_action(soldier, squad, destination, allow_replace = True)
        # Командир ведёт бойцов автоматически, но не вырывается впереди строя:
        if 'lead' in soldier.commands\
                and squad.commanders_list\
                and soldier.uuid == squad.commander.uuid:
            if len(soldier.near_allies) >= 1\
                    or enemy and enemy.distance <= squad.enemy_recon['move'] * 2\
                    or 'fearless' in soldier.commands:
                # Командиры прорываются через зональные заклинания и атакуют магов:
                if 'danger' in soldier.commands and 'fearless' in soldier.commands\
                        or 'danger' in soldier.commands\
                        and squad.enemy_recon['ally_strenght'] > squad.enemy_recon['enemy_strenght']:
                    soldier.commands.remove('danger')
                if hasattr(squad, 'destination') and squad.destination\
                        and not 'auto' in soldier.commands:
                    self.move_action(soldier, squad, squad.destination, allow_replace = True)
                elif enemy and 'dodge' in soldier.commands:
                    self.move_action(soldier, squad, enemy.place, allow_replace = False)
                elif enemy:
                    self.move_action(soldier, squad, enemy.place, allow_replace = True)
                elif len(squad.danger_points) > 0:
                    destination = first(squad.danger_points)
                    self.move_action(soldier, squad, destination, allow_replace = True)
                else:
                    destination = self.find_spawn(soldier.place, soldier.enemy_side)
                    self.move_action(soldier, squad, destination, allow_replace = True)
        # Оборонительная тактика, если таков приказ (вторые ряды всё же атакуют):
        if 'dodge' in soldier.commands and soldier.near_enemies\
                or soldier.danger > self.engage_danger:
            soldier.use_dodge_action()
        # Простые солдаты следуют за командиром, зная своё место в строю:
        if 'follow' in soldier.commands and squad.commander and not soldier.near_enemies:
            if 'crowd' in soldier.commands:
                self.follow_action(soldier, squad, squad.commander, accuracy = 3)
            else:
                self.follow_action(soldier, squad, squad.commander, accuracy = 1)
        # Боец наступает, если союзники рядом сильнее противника в точке назначения:
        if 'engage' in soldier.commands and not soldier.near_enemies:
            if enemy:
                self.engage_action(soldier, squad, enemy.place)
            # Если не видно врага, ищем зону его конценрации:
            elif len(squad.danger_points) > 0:
                destination = random.choice(list(squad.danger_points.keys()))
                self.engage_action(soldier, squad, destination)
        # Кастеры работают магией, сначала по группам, а потом целевой:
        if 'spellcast' in soldier.commands and enemy:
            self.recon_action(soldier, squad)
            # Кастеры колдуют:
            if soldier.danger <= 0 or 'fearless' in soldier.commands:
                if 'channel' in soldier.commands:
                    self.channel_action(soldier, squad, enemy)
                self.prepare_spell_action(soldier, squad, enemy)
                self.fireball_action(soldier, squad)
                self.spellcast_action(soldier, squad, enemy)
            # Друиды меняют форму, если враг рядом:
            if soldier.class_features.get('Wild_Shape'):
                if soldier.near_enemies or 'change' in soldier.commands:
                    soldier.set_change_form(squad)
        # Осьминожки прячутся в чернильном облаке, остальные в "Fog_Cloud".
        # Но только в том случае, если у врага есть дальнобойное оружие.
        if 'sneak' in soldier.commands and enemy and squad.__dict__.get('enemy_recon'):
            if self.metadict_soldiers[enemy.uuid].hero\
                    or 'throw' in squad.enemy_recon['attacks']\
                    or 'ranged' in squad.enemy_recon['attacks']\
                    or squad.enemy_recon['enemy_strenght'] > squad.enemy_recon['ally_strenght']:
                self.sneak_action(soldier, squad, enemy)
        # Атака следует за 'engage', поэтому осматриваемся снова:
        if 'attack' in soldier.commands:
            self.recon_action(soldier, squad)
            enemy = self.find_enemy(soldier, squad)
            if enemy:
                if soldier.danger <= 0 or 'fearless' in soldier.commands:
                    self.attack_action(soldier, squad, enemy)
                    if 'engage' in soldier.commands\
                            and not 'dodge' in soldier.commands\
                            and not 'disengage' in soldier.commands:
                        self.engage_action(soldier, squad, enemy.place)
                # Удвоенный ход бойца:
                if len(soldier.near_enemies) >= 2\
                        or len(soldier.near_enemies) >= 1\
                        and max([enemy.level for enemy in soldier.near_enemies]) >= 5:
                    if soldier.set_action_surge():
                        self.round_run_soldier(soldier, squad)
        # Не видя врага, лучники стреляют навесом:
        if 'volley' in soldier.commands and not enemy:
            self.volley_action(soldier, squad)
        # Боец отступает, если таков приказ, или он в зоне опасного заклинания:
        if 'disengage' in soldier.commands and squad.__dict__.get('enemy_recon'):
            if enemy and 'carefull' in soldier.commands\
                    and enemy.distance <= squad.enemy_recon['move'] * 2\
                    and squad.enemy_recon['enemy_strenght'] > squad.enemy_recon['ally_strenght'] / 2\
                    or 'very_carefull' in soldier.commands and enemy\
                    and enemy.distance <= squad.enemy_recon['move'] * 4\
                    and squad.enemy_recon['enemy_strenght'] > squad.enemy_recon['ally_strenght'] / 4\
                    or 'danger' in soldier.commands\
                    and soldier.place in squad.enemy_recon.get('danger_places',[]):
                if not 'spawn' in self.dict_battlespace[soldier.place]:
                    destination = self.find_spawn(soldier.place, soldier.ally_side)
                elif 'spawn' in self.dict_battlespace[soldier.place]:
                    if len(squad.exit_points) > 0:
                        destination = random.choice(squad.exit_points)
                        soldier.use_dash_action(bonus_action = True)
                        soldier.escape = True
                    else:
                        destination = self.find_spawn(soldier.place, soldier.ally_side)
                self.move_action(soldier, squad, destination,
                        close_order = True, save_path = False, danger_path = True)
                if 'exit' in self.dict_battlespace[soldier.place]:
                    self.clear_battlemap()
        # Если не видно врагов, боец лечится добряникой:
        if not enemy and soldier.hitpoints < soldier.hitpoints_max:
            soldier.use_heal(use_minor_potion = True)
        # Если действия не использовались -- защищаемся:
        if soldier.battle_action or soldier.bonus_action:
            soldier.use_dodge_action()

    def sneak_action(self, soldier, squad, enemy):
        """Боец прячется с помощью "Туманного облака" или "Темноты"
        
        - осьминожки прячутся в "Чернильном облаке"
        """
        # Чернильное облако осьминожек:
        if 'spellcast' in soldier.commands:
            if soldier.spells_generator.find_spell('Fog_Cloud')\
                and not 'obscure_terrain' in self.dict_battlespace[soldier.place]:
                spell_choice = soldier.spells_generator.find_spell('Fog_Cloud')
                self.spellcast_action(soldier, squad, enemy, spell_choice)
            elif soldier.spells_generator.find_spell('Darkness')\
                and not 'obscure_terrain' in self.dict_battlespace[soldier.place]:
                spell_choice = soldier.spells_generator.find_spell('Darkness')
                self.spellcast_action(soldier, squad, enemy, spell_choice)
        if soldier.__dict__.get('ink_cloud') and soldier.near_enemies:
            zone_radius = round(soldier.ink_cloud_radius / self.tile_size)
            zone_list = self.point_to_field(soldier.place, zone_radius)
            zone_list_circle = [point for point in zone_list\
                    if inside_circle(point, enemy.place, zone_radius)]
            for point in zone_list_circle:
                if 'water' in self.dict_battlespace[point]\
                        and not 'obscure_terrain' in self.dict_battlespace[point]:
                    self.dict_battlespace[point].append('obscure_terrain')
            soldier.ink_cloud = False
            if soldier.bonus_action:
                soldier.use_dash_action(bonus_action = True)

    def recon_action(self, soldier, squad, distance = 1):
        """Боец осматривает зону вокруг себя.
        
        - soldier.near_zone -- срез поля боя
        - soldier.recon_near -- ближайшие существа
        - soldier.near_allies -- ближайшие союзники
        - soldier.near_enemies -- ближайшие враги
        - soldier.danger -- оценка угрозы
        """
        # Крупные создания осматривают большую зону вокруг себя.
        # Запоминаем все точки вокруг, не занятые непроходимой местностью или границами зон:
        # Находим противников и союзников в области 5 футов, 3x3 клетки:
        if soldier.size == 'large':
            soldier_tuple = (squad.ally_side, soldier.behavior, soldier.level, soldier.uuid)
            soldier_place_field = self.point_to_field_2x2(soldier.place)
            recon_near = {}
            near_zone = []
            for point in soldier_place_field:
                if point in self.dict_battlespace and\
                        soldier_tuple in self.dict_battlespace[point]:
                    recon_near.update(self.recon(point, distance))
                    near_zone.extend(self.find_points_in_zone(point, distance))
            near_zone = list(set(near_zone))
        elif soldier.size == 'huge':
            soldier_tuple = (squad.ally_side, soldier.behavior, soldier.level, soldier.uuid)
            soldier_place_field = self.point_to_field(soldier.place)
            recon_near = {}
            near_zone = []
            for point in soldier_place_field:
                if point in self.dict_battlespace and\
                        soldier_tuple in self.dict_battlespace[point]:
                    recon_near.update(self.recon(point, distance))
                    near_zone.extend(self.find_points_in_zone(point, distance))
            near_zone = list(set(near_zone))
        else:
            near_zone = self.find_points_in_zone(soldier.place, distance)
            recon_near = self.recon(soldier.place, distance)
        soldier.near_zone = near_zone
        soldier.recon_near = recon_near
        soldier.set_near_allies(recon_near)
        soldier.set_near_enemies(recon_near)
        # Работает страхочуйка и мораль бойца:
        soldier.set_danger(self.recon_action_danger(soldier, recon_near), squad)
        return near_zone, recon_near

    def recon_action_danger(self, soldier, recon_near = None, distance = 1):
        """Оценка опасности ближней зоны"""
        if not recon_near and soldier.recon_near:
            recon_near = soldier.recon_near
        elif not soldier.recon_near:
            recon_near = self.recon(soldier.place, distance)
        danger = self.danger_sense(recon_near, soldier.enemy_side)
        # TODO: Кучи павших своих, это объективный показатель угрозы:
        # -------------------------------------------------
        # Но лучше подсчитывать это в soldier.set_danger
        # На самом деле редкое явление, тяжелораненых вытаскивают.
        # -------------------------------------------------
        for point in soldier.near_zone:
            if soldier.ally_side in self.dict_battlespace[point]:
                for descript in self.dict_battlespace[point]:
                    if descript == 'fall_place':
                        danger +=1
        return danger

    def get_enemy_tuple(self, soldier, enemy_soldier):
        """Дистанция до врага, укрытие. Формат namedtuple_target."""
        enemy = self.namedtuple_target(
                enemy_soldier.ally_side,
                enemy_soldier.behavior,
                enemy_soldier.level,
                enemy_soldier.place,
                distance = round(distance_measure(soldier.place, enemy_soldier.place)),
                cover = self.calculate_enemy_cover(soldier.place, enemy_soldier.place).cover,
                uuid = enemy_soldier.uuid)
        return enemy

    def get_zone_effects(self, soldier, squad, before_round = False):
        """Эффекты зоны ранит солдата.

        Например: Spirit_Guardians, Create_Bonfire

        - Должен быть маг с концентрацией.
        - Эффект должен быть подписан в зоне.
        """
        if 'danger_terrain' in self.dict_battlespace[soldier.place]:
            enemy_mages_list = [enemy_soldier\
                    for enemy_soldier in self.metadict_soldiers.values()
                    if enemy_soldier.ally_side != soldier.ally_side
                    and enemy_soldier.concentration
                    and enemy_soldier.concentration.get('effect')
                    and enemy_soldier.concentration.get('zone_effect')
                    and enemy_soldier.concentration.get('zone_danger')]
            # Свои маги тоже небезопасны:
            ally_mages_list = [ally for ally in self.metadict_soldiers.values()
                    if ally.ally_side == soldier.ally_side
                    and ally.concentration
                    and ally.concentration.get('effect')
                    and ally.concentration.get('zone_effect')
                    and ally.concentration.get('zone_danger')
                    and not ally.concentration.get('safe')]
            enemy_mages_list.extend(ally_mages_list)
            # TODO: сначала перебор меток, потом перебор магов.
            # -------------------------------------------------
            # Несколько магов с Create_Bonfire не усилят единственный костёр.
            # Один вид эффекта наносит только один урон.
            # -------------------------------------------------
            if enemy_mages_list:
                for enemy_soldier in enemy_mages_list:
                    for descript in self.dict_battlespace[soldier.place]:
                        if enemy_soldier.concentration\
                                and enemy_soldier.concentration['effect'] == descript:
                            spell_dict = dict(enemy_soldier.concentration)
                            if not before_round and spell_dict.get('before_round'):
                                return False
                            else:
                                enemy_squad = [enemy_squad for enemy_squad in self.squads.values()
                                        if enemy_soldier.uuid in enemy_squad.metadict_soldiers][0]
                                # Для зачарованных жрецов:
                                if 'enemies_abound' in enemy_soldier.debuffs\
                                        and enemy_soldier.enemy_side == enemy_squad.ally_side:
                                    enemy_mage = self.metadict_soldiers[
                                            enemy_soldier.debuffs['enemies_abound']['caster_uuid']]
                                    enemy_squad = [enemy_squad for enemy_squad in self.squads.values()
                                            if enemy_mage.uuid in enemy_squad.metadict_soldiers][0]
                                self.fireball_action(enemy_soldier, enemy_squad,
                                        spell_dict, soldier.place,
                                        safe = spell_dict.get('safe', False),
                                        single_target = soldier
                                        )

    def follow_action(self, soldier, squad, commander, accuracy = 1):
        """Солдат следует за командиром, стараясь держать строй.
        
        Как это работает:
        - Боец знает своё место в строю относительно командира.
        - Если у него нет места, он выбирает свободное из доступных.
        - Точность построения в пределах 3x3 точек (чтобы не толкались за места)
        """
        destination = None
        # Боец следует к своему месту в строю:
        if hasattr(soldier, 'place_in_order') and soldier.place_in_order:
            destination = [c1 + c2 for c1, c2 in zip(commander.place, soldier.place_in_order)]
            destination = tuple(destination)
        # Если в строю есть свободное место, боец занимает его:
        elif squad.__dict__.get('battle_order'):
            for place_in_order, unit in squad.battle_order.items():
                if None in unit:
                    squad.battle_order[place_in_order] = (soldier.behavior, soldier.uuid)
                    soldier.set_place_in_order(place_in_order)
                    destination = [c1 + c2 for c1, c2 in zip(commander.place, soldier.place_in_order)]
                    break
        # Толпимся рядом с командиром, если боевого порядка нет:
        if not destination:
            # Идём к командиру, который в наибольшей опасности:
            commanders_danger_list = sorted(squad.commanders_list,key=lambda x: x.danger,
                    reverse = True)
            commander = self.metadict_soldiers[commanders_danger_list[0].uuid]
            if commander.near_zone:
                destination = random.choice(commander.near_zone)
            else:
                destination = commander.place
        # Абсолютная точность не нужна, боец не двигается, если его местов пределах 3x3 тайлов:
        if not destination in self.point_to_field(soldier.place, accuracy):
            try:
                self.move_action(soldier, squad, destination)
            except KeyError:
                #traceback.print_exc()
                # Идём к командиру, который в наибольшей опасности:
                commanders_danger_list = sorted(squad.commanders_list,key=lambda x: x.danger,
                        reverse = True)
                commander = self.metadict_soldiers[commanders_danger_list[0].uuid]
                if commander.near_zone:
                    destination = random.choice(commander.near_zone)
                else:
                    destination = commander.place
                self.move_action(soldier, squad, destination)

    def engage_action(self, soldier, squad, enemy_place, recon_near = None):
        """Солдат сближается с противником, готовясь атаковать.
        
        Как это работает:
        - Боец оценивает силу союзников рядом (в зоне 3x3 клетки)
        - Он сравнивает эту силу с силой врага в точке назначения.
        - Затем он направляется к ближайшей свободной точке линии фронта.
        - И только после этого бросается к ближайшему врагу.
        Эта тактика защищает от окружения и провоцированных атак.
        """
        if not recon_near:
            recon_near = soldier.recon_near
        ally_strenght = self.danger_sense(recon_near, soldier.ally_side)
        recon_enemy = self.recon(enemy_place, 1, soldier.place)
        enemy_strenght = self.danger_sense(recon_enemy, soldier.enemy_side)
        if squad.frontline:
            frontline_distances = []
            for point in squad.frontline:
                distance = round(distance_measure(soldier.place, point))
                frontline_distances.append((point,distance))
            frontline_distances = sorted(frontline_distances,key=lambda x: x[1])
            destination = frontline_distances[0][0]
        else:
            destination = enemy_place
        # Простые солдаты нападают вблизи только при двухкратном превосходстве союзников:
        if not soldier.near_enemies and ally_strenght >= enemy_strenght * 2\
                or soldier.hero == True and not soldier.near_enemies and ally_strenght >= enemy_strenght\
                or 'fearless' in soldier.commands:
            # После движение осматриваемся снова в поисках врагов:
            self.move_action(soldier, squad, destination)
            recon_near = self.recon(soldier.place, distance = 1)
            soldier.set_near_enemies(recon_near)
            if not soldier.near_enemies or 'fearless' in soldier.commands:
                self.move_action(soldier, squad, enemy_place, save_path = False)
                if soldier.hero == True or soldier.behavior == 'commander':
                    self.move_action(soldier, squad, enemy_place, save_path = False, allow_replace = True)

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

    def check_place_danger(self, soldier, next_place):
        """Солдат проверят точку пути на угрозы.
        
        - Выход из вражеской зоны контроля, это провоцированная атака реакцией.
        """
        prev_place = soldier.place
        dangers_dict = {
                'ready_attacks':[],
                'provoke_attacks':[],
                }
        for squad in self.squads.values():
            if squad.ally_side == soldier.enemy_side\
                    and squad.__dict__.get('dict_control_zones'):
                enemies_near = squad.dict_control_zones[soldier.place]
                enemies_next = squad.dict_control_zones[next_place]
                # Подготовленная атака на приближение врага:
                #ready_attacks_list = [enemy for enemy in enemies_next if enemy not in enemies_near]
                # Провоцированная атака на выход из зоны контроля:
                provoke_attacks_list = [enemy for enemy in enemies_near if enemy not in enemies_next]
                provoke_attacks_list = [enemy for enemy in provoke_attacks_list
                        if self.metadict_soldiers[enemy[-1]].reaction]
                if provoke_attacks_list:
                    dangers_dict['provoke_attacks'].extend(provoke_attacks_list)
                    #print(soldier.ally_side, soldier.place, next_place, provoke_attacks_list)
        #print(prev_place, next_place)
        if dangers_dict['provoke_attacks'] or dangers_dict['ready_attacks']:
            return dangers_dict
        else:
            return False

    def move_action(self, soldier, squad, destination,
            free_path = False, allow_replace = False,
            save_path = True, danger_path = False,
            allow_manoeuvre = True, close_order = False):
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
        # Удаляем последнюю точку, если там кто-то/что-то есть:
        if path and destination in path and not self.check_place(soldier, destination).free:
            enemy_point = path.pop(-1)
        if save_path and path and squad.frontline != None:
            # Безопасный путь, это остановка перед линией фронта:
            path = self.path_to_savepath(path, squad.frontline)
        if 'free_path' in soldier.commands or soldier.__dict__.get('air_walk'):
            free_path = True
        if 'close_order' in soldier.commands or soldier.__dict__.get('close_order'):
            close_order = True
        if path:
            while path and soldier.move_pool > 0:
                # Если ближайшая точка пути свободна, переходим на неё:
                move = False
                place = self.check_place(soldier, path[0])
                dangers_dict = self.check_place_danger(soldier, path[0])
                # Боец не идёт через зоны опасных заклинаний:
                if not danger_path and 'danger' in soldier.commands\
                        and place.place in squad.enemy_recon.get('danger_places',[]):
                            return False
                if dangers_dict and dangers_dict['provoke_attacks']:
                    self.provoke_attack_chain(soldier, squad, dangers_dict['provoke_attacks'])
                if place.free or free_path:
                    # TODO: пусть боец запоминает направление движения.
                    # -------------------------------------------------
                    # Сделай это функцией soldier. Всего 8 направлений.
                    # Это можно будет использовать как область зрения.
                    # А также для команд вроде 'move_backward', 'move_forvard'
                    # -------------------------------------------------
                    next_place = path.pop(0)
                    prev_place = soldier.place
                    move = soldier.move(self.tile_size, place.rough)
                    self.change_place(prev_place, next_place, soldier.uuid)
                # Если точка занята ездовым животным бойца, то можно двигаться:
                elif not place.free and place.units\
                        and soldier.__dict__.get('mount_uuid')\
                        and 'mount' in place.units[0]\
                        and soldier.mount_uuid in place.units[0]:
                    next_place = path.pop(0)
                    prev_place = soldier.place
                    move = soldier.move(self.tile_size, place.rough)
                    self.change_place(prev_place, next_place, soldier.uuid)
                # Если размер существа маленький, то их может быть по 4 на точке:
                elif not place.free and place.units\
                        and soldier.size == 'tiny'\
                        and len(place.units) < 4:
                    next_place = path.pop(0)
                    prev_place = soldier.place
                    move = soldier.move(self.tile_size, place.rough)
                    self.change_place(prev_place, next_place, soldier.uuid)
                # Командой можно уплотнить строй:
                elif not place.free and place.units\
                        and close_order\
                        and len(place.units) < 2:
                    next_place = path.pop(0)
                    prev_place = soldier.place
                    move = soldier.move(self.tile_size, place.rough)
                    self.change_place(prev_place, next_place, soldier.uuid)
                # Если точка занята союзником, можно поменяться с ним местами:
                elif not place.free and allow_replace and place.units\
                        and soldier.ally_side in place.units[0]:
                    unit_uuid = place.units[0][-1]
                    next_place = path.pop(0)
                    prev_place = soldier.place
                    move = soldier.move(self.tile_size, place.rough)
                    self.change_place(prev_place, next_place, soldier.uuid)
                    # Многотайловых лошадей не трогаем, мимо протискиваемся:
                    if not 'mount' in place.units[0]:
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
                        near_place = self.check_place(soldier, destination)
                        # TODO: проверка на опасность должна быть частью функции check_place
                        if near_place.free:
                            if danger_path or not 'danger' in soldier.commands:
                                path[0] = destination
                                break
                            elif 'danger' in soldier.commands\
                                    and not destination in squad.enemy_recon.get('danger_places',[]):
                                path[0] = destination
                                break
                            else:
                                pass
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
                if soldier.size == 'medium'\
                        or soldier.size == 'small'\
                        or soldier.size == 'tiny':
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
                elif soldier.size == 'huge':
                    soldier_place_field = self.point_to_field(coordinates, 4)
                    for point in soldier_place_field:
                        if point in self.dict_battlespace\
                                and soldier_tuple in self.dict_battlespace[point]:
                            self.dict_battlespace[point].remove(el)
                    #self.dict_battlespace[destination].append(soldier_tuple)
                    destination_field = self.point_to_field(destination)
                    for point in destination_field:
                        if point in self.dict_battlespace and point != coordinates:
                            self.dict_battlespace[point].append(soldier_tuple)
                            self.dict_battlespace[point].append('mount_height')
                    soldier.set_coordinates(destination)
                # Добавляем эффекты движения:
                if soldier.__dict__.get('darkness'):
                    # TODO: Замечены редкие зависания. В бою с паладинской конницей. Непотняо, почему.
                    spell_dict = soldier.darkness_dict
                    zone_radius = round(spell_dict['radius'] / self.tile_size)
                    self.change_place_effect(spell_dict['effect'], coordinates, soldier.place, zone_radius)
                    self.change_place_effect('obscure_terrain', coordinates, soldier.place, zone_radius)
                if soldier.concentration\
                        and soldier.concentration.get('zone_effect')\
                        and soldier.concentration.get('zone_self'):
                    spell_dict = soldier.concentration
                    zone_radius = round(spell_dict['radius'] / self.tile_size)
                    self.change_place_effect(spell_dict['effect'], coordinates, soldier.place, zone_radius)
                    # TODO: эти эффекты добавляй по списку ['dange_terrain','obscure_terrain']
                    # Пусть будет список в zone_effect.
                    if spell_dict.get('zone_danger'):
                        self.change_place_effect('danger_terrain', coordinates, soldier.place, zone_radius)
        # Показывает ходы бойца:
        if namespace.visual and not namespace.test:
            print_ascii_map(self.gen_battlemap())
            time.sleep(0.02)

    def change_place_effect(self, effect, old_place, new_place, zone_radius, zone_shape = False):
        """Передвигаем эффект зоны.
        
        Например: Spirit_Guardians, Darkness, Crusaders_Mantle.
        """
        # Развеиваем по старым координатам:
        zone_list = [point for point in self.find_points_in_zone(old_place, zone_radius)\
                if inside_circle(point, old_place, zone_radius)]
        for point in zone_list:
            if effect in self.dict_battlespace[point]:
                self.dict_battlespace[point].remove(effect)
        # Создаём по новым координатам:
        zone_list = [point for point in self.find_points_in_zone(new_place, zone_radius)\
                if inside_circle(point, new_place, zone_radius)]
        for point in zone_list:
            if not effect in self.dict_battlespace[point]:
                self.dict_battlespace[point].append(effect)

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

    def provoke_attack_chain(self, soldier, squad, provoke_attacks_list):
        """Боец провоцирует атаки и получает их.
        
        - Если возможо, старается уклоняться с Disengage_Action
        https://www.dandwiki.com/wiki/5e_SRD:Disengage_Action
        """
        if not soldier.disengage_action:
            disengage = soldier.use_disengage_action()
            for enemy in provoke_attacks_list:
                enemy_soldier = self.metadict_soldiers[enemy[-1]]
                enemy_squad = [enemy_squad for enemy_squad in self.squads.values()
                        if enemy_soldier.uuid in enemy_squad.metadict_soldiers][0]
                # Взгляд со стороны врага:
                recon_dict = self.recon(soldier.place,
                        soldier_coordinates = enemy_soldier.place)
                if soldier.uuid in recon_dict.keys():
                    soldier_tuple = recon_dict[soldier.uuid]
                    if not soldier.disengage_action\
                            or enemy_soldier.class_features.get('Feat_Sentinel'):
                        if enemy_soldier.class_features.get('Feat_War_Caster'):
                            # Сначала пытаемся колдовать, потом атакуем, если не вышло:
                            attack_dict = self.spellcast_action(
                                    enemy_soldier, enemy_squad,
                                    soldier_tuple, reaction = True)
                            attack_dict = self.attack_action(
                                    enemy_soldier, enemy_squad,
                                    soldier_tuple, reaction = True)
                        else:
                            attack_dict = self.attack_action(
                                    enemy_soldier, enemy_squad,
                                    soldier_tuple, reaction = True)
                        if attack_dict:
                            if enemy_soldier.class_features.get('Feat_Sentinel'):
                                soldier.move_pool = 0
                        #    # 15-20 провоцированных атак за минуту боя, 30-50 атак за бой.
                            #print('{side_1}, {c1} {s} PROVOKE >> {side_2} {c2} {e} act {a} dodge {d}'.format(
                            #    side_1 = enemy_soldier.ally_side,
                            #    c1 = enemy_soldier.place,
                            #    s = enemy_soldier.behavior,
                            #    side_2 = soldier.ally_side,
                            #    c2 = soldier.place,
                            #    e = soldier.behavior,
                            #    a = soldier.battle_action,
                            #    d = soldier.dodge_action,
                            #    ))

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
            if 'volley_random' in soldier.commands:
                target = random.choice(self.point_to_field(target, round(distance / 5)))
            elif hasattr(soldier, 'place_in_order') and soldier.place_in_order:
                target_point = [c1 + c2 for c1, c2 in zip(target, soldier.place_in_order)]
                if target_point:
                    target_field = self.point_to_field(target_point, round(distance / 10))
                    if target_field:
                        target = random.choice(target_field)
                else:
                    target_field = self.point_to_field(target, round(distance / 10))
                    if target_field:
                        target = random.choice(target_field)
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
                        enemy = self.namedtuple_target(value[0],value[1],value[2],
                                target,distance,cover,uuid)
                        self.attack_action(soldier, squad, enemy, attack_choice = attack_choice)
                        break
                else:
                    # Стрелы расходуются, если летят совсем не туда:
                    soldier.use_ammo(soldier.attacks[attack_choice], squad.metadict_soldiers)
                    self.set_squad_battle_stat(soldier.attacks.get(attack_choice), squad, attack_choice)
                    # Артиллерия и заклинания в стрелах:
                    if soldier.attacks[attack_choice].get('spell_dict'):
                        spell_dict = soldier.attacks[attack_choice].get('spell_dict')
                        if spell_dict.get('ammo', 0) > 0 and enemy_soldier.behavior == 'commander'\
                                or spell_dict.get('ammo') == None:
                            if spell_dict.get('zone') and not spell_dict.get('crit_only'):
                                self.fireball_action(soldier, squad, spell_dict, target)
                            elif attack_result['hit'] and not spell_dict.get('crit_only'):
                                self.fireball_action(soldier, squad, spell_dict, target,
                                        single_target = enemy)
                            elif attack_result['crit'] and spell_dict.get('crit_only'):
                                self.fireball_action(soldier, squad, spell_dict, target,
                                        single_target = enemy)

    def attack_action(self, soldier, squad, enemy, attack_choice = None,
            reaction = False, spell_action = False):
        """Боец выбирает противника и атакует."""
        # Данные о враге:
        enemy_soldier = self.metadict_soldiers[enemy.uuid]
        enemy_squad = [enemy_squad for enemy_squad in self.squads.values()
                if enemy_soldier.uuid in enemy_squad.metadict_soldiers][0]
        # Для атаки используется действие, бонусное действие, или реакция:
        if soldier.battle_action or reaction and soldier.reaction or spell_action:
            # Смотрим, возможно ли атаковать:
            if not attack_choice:
                attack_choice = soldier.select_attack(squad, enemy,
                        self.tile_size, namespace.weather)
                if attack_choice == None:
                    return False
            # Готовим цепь атак:
            attacks_number = soldier.attacks_number
            attacks_chain = [attack_choice] * attacks_number
            # Оцениваем угрозу контратаки, прежде чем нападать:
            danger_offence = self.check_danger_offence(soldier, enemy)
            if reaction and soldier.reaction:
                # Атака реакцией может быть только одна:
                soldier.reaction = False
                attacks_chain = [attacks_chain[0]]
            # Атака с заклинанием, вроде Green_Flame_Blade:
            elif spell_action:
                if soldier.class_features.get('War_Magic')\
                        and len(attacks_chain) >= 2\
                        and soldier.bonus_action:
                    attacks_chain = attacks_chain[:2]
                    soldier.bonus_action = False
                else:
                    attacks_chain = [attacks_chain[0]]
            else:
                soldier.battle_action = False
                # TODO: бонусы классов в отдельную функцию:
                attacks_chain_bonus = []
                # Боец может использовать парное оружие (в том числе метательное), если нет щита:
                if soldier.class_features.get('Fighting_Style_Two_Weapon_Fighting'):
                    if attack_choice[0] == 'close' or attack_choice[0] == 'throw':
                        attacks_chain_bonus = soldier.set_two_weapon_fighting(attack_choice)
                # Жрецы домена войны могут получить атаку за счёт бонусного действия:
                if soldier.class_features.get('War_Priest') and soldier.war_priest > 0:
                        attacks_chain_bonus += attack_choice
                        soldier.bonus_action = False
                        soldier.war_priest -= 1
                # Монахи усиливают атаку за счёт Ки:
                if soldier.class_features.get('Martial_Arts'):
                    if attack_choice[0] == 'close':
                        attacks_chain_bonus = soldier.set_martial_arts()
                # Варвары добавляют бонусы ярости:
                if soldier.char_class == 'Barbarian':
                    if attack_choice[0] == 'close':
                        soldier.set_rage()
                    if attack_choice[0] == 'close' and danger_offence:
                        attacks_chain_bonus = soldier.set_frenzy(attack_choice)
                # Рейнджеры выбирают групповые цели:
                elif soldier.char_class == 'Ranger':
                    if attack_choice[0] == 'ranged':
                        if soldier.class_features.get('Hunter_Horde_Breaker')\
                                and enemy_soldier.near_allies:
                            attacks_chain_bonus = [attack_choice]
                attacks_chain.extend(attacks_chain_bonus)
            # Начинаем цепь атак:
            hit = False
            while attacks_chain:
                # Иногда заканчиваются боеприпасы:
                if not soldier.attacks.get(attacks_chain[0]):
                    break
                # Иногда заканчиваются и враги:
                if not enemy:
                    break
                # Перенаправление атаки: лошадь --> всадник с Feat_Mounted_Combatant:
                if enemy_soldier.behavior == 'mount'\
                        and enemy_soldier.__dict__.get('master_uuid') in self.metadict_soldiers:
                    master = self.metadict_soldiers[enemy_soldier.master_uuid]
                    near_allies_uuid = [ally[-1] for ally in enemy_soldier.near_allies]
                    if master.uuid in near_allies_uuid\
                            and master.class_features.get('Feat_Mounted_Combatant')\
                            and master.hitpoints > master.hitpoints_max / 2:
                        enemy_soldier = master
                        enemy = self.get_enemy_tuple(soldier, enemy_soldier)
                # Перенаправление атаки: маг --> Mirror_Image:
                # Иллюзии остаются, но попадание распознаёт их.
                if 'mirror_image' in enemy_soldier.buffs:
                    spell_dict = enemy_soldier.buffs['mirror_image']
                    targets = [image for image in spell_dict['images'].values()
                            if image.hitpoints > 0]
                    if targets:
                        targets.append(enemy_soldier)
                        enemy_soldier = random.choice(targets)
                        enemy = self.get_enemy_tuple(soldier, enemy_soldier)
                    else:
                        enemy_soldier.buffs.pop('mirror_image')
                # Боец подготавливает атаку:
                attack_choice = attacks_chain.pop(0)
                advantage, disadvantage = self.test_enemy_defence(soldier, enemy_soldier, attack_choice)
                # Вместо атаки можно перейти в рукопашный бой (сбивание с ног, захваты, разоружение):
                if self.check_wrestling_action(attack_choice, soldier, squad, enemy_soldier):
                    wrestling_action = self.wrestling_action(soldier, squad,
                            enemy_soldier, advantage, disadvantage)
                    if wrestling_action != None:
                        continue
                # Используем приёмы вроде help_action союзника по строю:
                if not advantage:
                    advantage = self.break_enemy_defence(soldier, squad, enemy_soldier, attack_choice)
                # Боец реализует атаку:
                attack_dict = soldier.attack(soldier.attacks[attack_choice], attack_choice,
                        enemy, self.metadict_soldiers,
                        advantage = advantage, disadvantage = disadvantage)
                # Противник получает атаку:
                attack_result = enemy_soldier.take_attack(
                        attack_choice, attack_dict, self.metadict_soldiers)
                # TODO: всё это в отдельную функцию.
                # Атака заклинанием в оружии:
                if attack_result.get('spell_dict'):
                    spell_dict = attack_result['spell_dict']
                    if spell_dict.get('ammo', 0) > 0 and enemy_soldier.behavior == 'commander'\
                            or spell_dict.get('ammo') == None:
                        if spell_dict.get('zone') and not spell_dict.get('crit_only'):
                            self.fireball_action(soldier, squad, spell_dict, enemy.place)
                        elif attack_result['hit'] and not spell_dict.get('crit_only'):
                            self.fireball_action(soldier, squad, spell_dict, enemy.place,
                                    single_target = enemy)
                        elif attack_result['crit'] and spell_dict.get('crit_only'):
                            self.fireball_action(soldier, squad, spell_dict, enemy.place,
                                    single_target = enemy)
                # Эффект Crusaders_Mantle (срабатывает только для атак оружием):
                if attack_result['hit'] and attack_dict.get('weapon') == True\
                        and 'crusaders_mantle' in self.dict_battlespace[soldier.place]:
                    # Находим создателя "Мантии крестоносца", если он союзный:
                    spell_dict = [ally_soldier.concentration\
                            for ally_soldier in self.metadict_soldiers.values()
                            if ally_soldier.ally_side == soldier.ally_side
                            and ally_soldier.concentration
                            and ally_soldier.concentration.get('effect') == 'crusaders_mantle']
                    if spell_dict:
                        spell_dict = spell_dict[0]
                        #spell_choice = 'aura', 'Crusaders_Mantle'
                        #spell_dict['spell_choice'] = spell_choice
                        self.fireball_action(soldier, squad, spell_dict, enemy.place,
                                single_target = enemy)
                # Монашьи боласы могут сбить с ног:
                #if attack_result['hit'] and 'prone' in attack_result['weapon_type']\
                #        and not enemy_soldier.prone:
                #    prone = enemy_soldier.set_fall_prone(soldier, advantage, disadvantage)
                # Ошеломляющий удар монаха, только по командирам врага:
                if attack_dict['hit'] and soldier.class_features.get('Stunning_Strike')\
                        and enemy_soldier.behavior == 'commander'\
                        and not enemy_soldier.stunned:
                    soldier.use_stunning_strike(enemy_soldier)
                # Враг сбивается с ног, или лишается реакции:
                # Атака применяется только с Flurry_of_Blows
                elif attack_dict['hit'] and 'Open_Hand_Technique' in attack_dict:
                    if not enemy_soldier.prone:
                        enemy_soldier.set_fall_prone(soldier)
                    else:
                        enemy_soldier.reaction = False
                # Осьминоги могут оплести щупальцами и затащить в воду:
                if attack_result['hit'] and 'restrained' in attack_result['weapon_type']\
                        and not enemy_soldier.restrained:
                    restrained = enemy_soldier.set_restained(attack_dict['restained_difficult'],
                            advantage, disadvantage)
                    if restrained:
                        destination = self.find_spawn(soldier.place, soldier.ally_side, random_range = 1)
                        self.move_action(soldier, squad, destination, close_order = True)
                        self.change_place(enemy_soldier.place, soldier.place, enemy_soldier.uuid)
                # Заклинание Hex:
                if attack_result['hit'] and soldier.concentration\
                        and soldier.concentration.get('effect') == 'hex'\
                        and soldier.concentration['effect'] in enemy_soldier.debuffs\
                        and soldier.concentration.get('target_uuid') == enemy_soldier.uuid:
                    spell_dict = soldier.concentration
                    self.fireball_action(soldier, squad, spell_dict, enemy.place,
                            single_target = enemy)
                # Атаку рейнджера дополняет шрапнель от Hail_of_Thorns:
                if attack_result['hit'] and soldier.concentration\
                        and soldier.concentration.get('effect') == 'thorns':
                    if enemy_soldier.near_allies and len(enemy_soldier.near_allies) >= 2\
                            or enemy_soldier.behavior == 'commander':
                        self.fireball_action(soldier, squad, soldier.concentration, enemy.place)
                        soldier.set_concentration_break(autofail = True)
                # Паладин добивает врага с помощью Divine_Smite:
                if attack_result['hit'] and not attack_result['fatal_hit']\
                        and soldier.spells_generator.find_spell('Divine_Smite')\
                        and 'spellcast' in soldier.commands:
                    spell_choice = soldier.spells_generator.find_spell('Divine_Smite')
                    self.spellcast_action(soldier, squad, enemy,
                            spell_choice, subspell = True, use_spell = True)
                # Заклинание Absorb_Elements усиливает атаку за счёт поглощённой энергии:
                if attack_result['hit'] and 'absorb_elements' in soldier.buffs:
                    if attack_choice[0] == 'close' or attack_choice[0] == 'reach':
                        spell_dict = soldier.buffs.pop('absorb_elements')
                        self.fireball_action(soldier, squad, spell_dict, enemy.place,
                                single_target = enemy)
                # Мастер тяжёлого оружия получает бонусную атаку, если убивает врага:
                # 20 варварам 2 lvl это добавляет 25% атак. От 10 до 30 атак за минуту боя.
                if attack_result['crit'] or attack_result['fatal_hit']:
                    if attack_dict.get('weapon_skills_use')\
                            and 'Feat_Great_Weapon_Master' in attack_dict['weapon_skills_use']\
                            and soldier.bonus_action:
                        attacks_chain.append(attack_choice)
                        soldier.bonus_action = False
                # Победа приносит бойцу опыт:
                if attack_result['fatal_hit']:
                    soldier.set_victory_and_enemy_defeat(enemy_soldier)
                    # Критический удар калечит цель:
                    if attack_result['crit'] and not 'unarmed' in soldier.commands:
                        enemy_soldier.set_disabled()
                    # Врага можно повязать за счёт боевого действия следующего раунда:
                    if 'enslave' in soldier.commands:
                        wrestling_action = self.wrestling_action(soldier, squad,
                                enemy_soldier, advantage, disadvantage)
                        soldier.help_action = False
                        enemy_soldier.captured = True
                # Убираем противника из списка целей и с карты:
                if attack_result['fatal_hit']:
                    if 'kill' in soldier.commands:
                        enemy_soldier.killer_mark = True
                    self.clear_battlemap()
                    fall_place = enemy_soldier.place
                    self.dict_battlespace[fall_place].append('fall_place')
                    self.dict_battlespace[fall_place].append(enemy_soldier.ally_side)
                    # Осматриваемся, убираем жертву из списка целей бойца.
                    self.recon_action(soldier, squad)
                    if squad.enemies and enemy.uuid in squad.enemies:
                        squad.enemies.pop(enemy.uuid)
                    # Выбираем новую цель:
                    if soldier.near_enemies:
                        enemy = random.choice(soldier.near_enemies)
                        enemy_soldier = self.metadict_soldiers[enemy.uuid]
                    else: 
                        enemy = self.find_enemy(soldier, squad)
                        if enemy:
                            enemy_soldier = self.metadict_soldiers[enemy.uuid]
                # TODO: в отдельную функцию
                # Контратаки врага:
                if len(soldier.near_enemies) >= 1:
                    for soldier_tuple in soldier.near_enemies:
                        enemy_ally = self.metadict_soldiers[soldier_tuple.uuid]
                        if enemy_ally.class_features.get('Feat_Sentinel')\
                                and enemy_ally.reaction == True\
                                and enemy_ally.uuid != enemy_soldier.uuid:
                            soldier_tuple = self.get_enemy_tuple(enemy_ally, soldier)
                            enemy_squad = [enemy_squad for enemy_squad in self.squads.values()
                                    if enemy_ally.uuid in enemy_squad.metadict_soldiers][0]
                            self.attack_action(
                                    enemy_ally, enemy_squad,
                                    soldier_tuple, reaction = True)
                if attack_result['hit'] and not attack_result['fatal_hit']:
                    if enemy_soldier.class_features.get('Wrath_of_the_Storm'):
                        # Взгляд со стороны врага:
                        recon_dict = self.recon(soldier.place,
                                soldier_coordinates = enemy_soldier.place)
                        if soldier.uuid in recon_dict.keys():
                            soldier_tuple = recon_dict[soldier.uuid]
                            if not soldier_tuple.distance > 1:
                                spell_choice = 'channel', 'Wrath_of_the_Storm'
                                spell_dict = enemy_soldier.spells[spell_choice]
                                self.fireball_action(enemy_soldier, enemy_squad, spell_dict,
                                        soldier_tuple.place, single_target = soldier_tuple)
                # Доспех Агатиса
                if attack_result['hit']:
                    if 'armor_of_agathys' in enemy_soldier.buffs:
                        if attack_choice[0] == 'close' or attack_choice[0] == 'reach':
                            recon_dict = self.recon(soldier.place,
                                    soldier_coordinates = enemy_soldier.place)
                            if soldier.uuid in recon_dict.keys():
                                soldier_tuple = recon_dict[soldier.uuid]
                                spell_dict = enemy_soldier.buffs['armor_of_agathys']
                                self.fireball_action(enemy_soldier, enemy_squad, spell_dict,
                                        soldier_tuple.place, single_target = soldier_tuple)
                            if enemy_soldier.bonus_hitpoints <= 0:
                                enemy_soldier.buffs.pop('armor_of_agathys', False)
                # Обобщаем статистику атак (расход боеприпасов и прочее):
                self.set_squad_battle_stat(attack_result, squad)
                if attack_result['hit']:
                    hit = True
            if hit:
                return attack_result

    def check_wrestling_action(self, attack_choice, soldier, squad, enemy_soldier):
        """Проверяем, возможно ли перейти в рукопашный бой.
        
        """
        wrestling_check = False
        if attack_choice[0] == 'close' and not 'no_grapple' in soldier.commands:
            if len(soldier.near_allies) > 2 and len(soldier.near_enemies) == 1\
                    or 'grapple' in soldier.commands\
                    or enemy_soldier.paralyzed\
                    or enemy_soldier.stunned\
                    or 'sleep' in enemy_soldier.debuffs:
                wrestling_check = True
            if enemy_soldier.size == 'huge'\
                    or enemy_soldier.size == 'large'\
                    or enemy_soldier.__dict__.get('air_walk'):
                wrestling_check = False
                return wrestling_check
            if enemy_soldier.__dict__.get('mount_uuid')\
                    and self.metadict_soldiers.get(enemy_soldier.mount_uuid):
                enemy_mount = self.metadict_soldiers[enemy_soldier.mount_uuid]
                if enemy_mount.__dict__.get('place') == enemy_soldier.place\
                        and not enemy_mount.prone\
                        and not enemy_mount.defeat:
                    wrestling_check = False
                    return wrestling_check
        return wrestling_check

    def wrestling_action(self, soldier, squad, enemy_soldier, advantage = False, disadvantage = False):
        """Рукопашный бой вместо обычных атак.
        
        1) Пытаемся сбить врага с ног.
        2) Сбитого с ног врага хватаем, чтобы не встал.
        3) Схваченного врага пытаемся разоружить.

        advantage/disadvantage указаны на броски атаки, они не используются в звахатах/сбивании.
        """
        # TODO: бонусные атаки нельзя заменить захватами:
        # ------------------------------------------------------------
        # Пусть возвращает True, если рукопашный бой уместен, и тогда continue
        # You cannot replace bonus action attacks with grapples.
        # (e.g. from the Monk or a Barbarian's Frenzy)
        # ------------------------------------------------------------
        # Умелый монах предпочитает "Ошеломляющие удары":
        if not enemy_soldier.stunned and soldier.class_features.get('Stunning_Strike')\
                and not disadvantage\
                and soldier.ki_points > 0:
            return None
        # Сбитого с ног врага пытаемся схватить:
        if not enemy_soldier.grappled:
            grappled = enemy_soldier.set_grappled(soldier)
            # Боец становится на место схваченного врага, а борцуха-монах выдирает его из строя:
            if grappled and not enemy_soldier.behavior == 'mount':
                if 'grapple' in soldier.commands:
                    destination = self.find_spawn(soldier.place, soldier.ally_side)
                    self.move_action(soldier, squad, destination, close_order = True)
                    self.change_place(enemy_soldier.place, soldier.place, enemy_soldier.uuid)
                else:
                    self.change_place(soldier.place, enemy_soldier.place, soldier.uuid)
            return grappled
        # Пытаемся сбить врага с ног:
        elif not enemy_soldier.prone:
            prone = enemy_soldier.set_fall_prone(soldier)
            return prone
        # У схваченного врага пытаемся вырвать щит:
        elif enemy_soldier.armor['shield_use'] and not enemy_soldier.class_features.get('Weapon_Bond'):
            disarmed = enemy_soldier.set_disarm_shield(soldier)
            return disarmed
        # И наконец, отбираем у схваченного врага оружие и тащим его к нашим:
        elif len(enemy_soldier.get_weapon_list(close = True)) >= 1\
                and not enemy_soldier.class_features.get('Weapon_Bond'):
            disarmed = enemy_soldier.set_disarm_weapon(soldier)
            if disarmed and len(soldier.near_allies) >= 1:
                destination = self.find_spawn(soldier.place, soldier.ally_side)
                self.move_action(soldier, squad, destination, close_order = True)
                self.change_place(enemy_soldier.place, soldier.place, enemy_soldier.uuid)
                return disarmed

    def prepare_spell_action(self, soldier, squad, enemy):
        """Боец подготавливает заклинание с концентрацией.
        
        Например:
        - Hex колдуна
        - Hail_of_Thorns следопыта
        """
        # TODO: допиливай прочее.
        # - смайты паладина
        enemy_soldier = self.metadict_soldiers[enemy.uuid]
        if not soldier.concentration:
            spells_list = [
                    'Hex',
                    'Hail_of_Thorns',
                    'Melf_Minute_Meteors',
                    'Spirit_Guardians',
                    'Crusaders_Mantle',
                    'Blur',
                    ]
            for spell in spells_list:
                soldier.try_spellcast(spell, gen_spell = True)
        if soldier.concentration and soldier.bonus_action:
            # Hex перенацеливается за счёт бонусного действия:
            if soldier.concentration.get('effect') == 'hex':
                soldier.concentration['target_uuid'] = enemy_soldier.uuid
                enemy_soldier.debuffs[soldier.concentration['effect']] = soldier.concentration
                soldier.bonus_action = False
            if soldier.concentration.get('effect') == 'minute_meteors':
                self.fireball_action(soldier, squad, soldier.concentration)
                self.fireball_action(soldier, squad, soldier.concentration)
                soldier.bonus_action = False

    def spellcast_action(self, soldier, squad, enemy,
            spell_choice = None, subspell = False, use_spell = True, reaction = False):
        """Боец атакует заклинанием."""
        enemy_soldier = self.metadict_soldiers[enemy.uuid]
        if reaction and soldier.reaction and not soldier.battle_action:
            soldier.battle_action = True
            soldier.reaction = False
        if hasattr(soldier, 'spells') and soldier.spells and soldier.battle_action\
                or spell_choice and subspell:
            # Смотрим, возможно ли атаковать:
            if not spell_choice:
                spell_choice = soldier.select_spell(squad, enemy, self.tile_size)
                if spell_choice == None:
                    return False
            if use_spell:
                spell_dict = soldier.try_spellcast(spell_choice)
            else:
                spell_dict = soldier.spells[spell_choice]
            attacks_number = spell_dict['attacks_number']
            spell_chain = [spell_choice] * attacks_number
            while spell_chain:
                spell_choice = spell_chain.pop(0)
                advantage, disadvantage = self.test_enemy_defence(soldier, enemy_soldier, spell_choice)
                # Заклинание Green_Flame_Blade, сочетающееся с атакой оружием:
                # Срабатывает, только если атака прошла:
                if spell_dict.get('weapon_attack'):
                    attack_dict = self.attack_action(soldier, squad, enemy, spell_action = True)
                    if not attack_dict:
                        continue
                # Заклинание "Create_Bonfire" создаёт пожары:
                if spell_dict.get('effect') == 'bonfire':
                    spell_dict = soldier.concentration
                    self.fireball_action(soldier, squad, spell_dict, enemy_soldier.place)
                    continue
                # Срабатывают вредоносные эффекты заклинаний:
                if spell_dict.get('debuff'):
                    spell_dict['target_uuid'] = enemy_soldier.uuid
                    debuff_dict = enemy_soldier.set_debuff(spell_dict)
                    if debuff_dict:
                        debuff_dict['hit'] = True
                    if debuff_dict and not namespace.test:
                        effect_upper = debuff_dict.get('effect', spell_choice[-1]).upper()
                        print('[+++] {side_1}, {c1} {s} {effect_upper} >> {side_2} {c2} {e} {r}'.format(
                            side_1 = soldier.ally_side,
                            c1 = soldier.place,
                            s = soldier.behavior,
                            side_2 = enemy_soldier.ally_side,
                            c2 = enemy_soldier.place,
                            e = enemy_soldier.behavior,
                            r = enemy_soldier.rank,
                            effect_upper = effect_upper
                            ))
                # Заклинание Word_of_Radiance, избирательно бьющее по врагам вблизи.
                elif spell_dict.get('effect') == 'burst':
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
                        #if fear:
                        #    print('{side_1}, {c1} {s} FEAR >> {side_2} {c2} {e}'.format(
                        #        side_1 = soldier.ally_side,
                        #        c1 = soldier.place,
                        #        s = soldier.behavior,
                        #        side_2 = enemy_soldier.ally_side,
                        #        c2 = enemy_soldier.place,
                        #        e = enemy_soldier.behavior,
                        #        ))
                    continue
                elif spell_dict.get('effect') == 'darkness':
                    # TODO: Сделай уже функцию draw_circle.
                    zone_radius = round(spell_dict['radius'] / self.tile_size)
                    zone_list = self.find_points_in_zone(enemy_soldier.place, zone_radius)
                    zone_list_circle = [point for point in zone_list\
                            if inside_circle(point, enemy_soldier.place, zone_radius)]
                    for point in zone_list_circle:
                        self.dict_battlespace[point].append('obscure_terrain')
                    enemy_soldier.darkness = True
                    enemy_soldier.darkness_dict = spell_dict
                    continue
                elif spell_dict.get('effect') == 'fog':
                    zone_radius = round(spell_dict['radius'] / self.tile_size)
                    zone_list = self.find_points_in_zone(enemy_soldier.place, zone_radius)
                    zone_list_circle = [point for point in zone_list\
                            if inside_circle(point, enemy_soldier.place, zone_radius)]
                    for point in zone_list_circle:
                        self.dict_battlespace[point].append('obscure_terrain')
                    continue
                # Заклинание Entangle:
                # TODO: это должно быть зональное заклинание в fireball_action
                # ------------------------------------------------------------
                # Хинт. можно уменьшат опасность зоны прямо в словаре отряда.
                # Лучше просто не учитывать врага как угрозу в enemy_recon, если он опутан.
                # ------------------------------------------------------------
                elif spell_dict.get('effect') == 'entangle':
                    enemy_soldier = self.find_target_for_debuff(soldier, enemy, 'restrained')
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
                        if 'sleep' in enemy_soldier.debuffs or enemy_soldier.hitpoints > sleep_pool:
                            enemy_soldier = self.find_target_for_debuff(soldier, enemy, 'sleep')
                            if not enemy_soldier:
                                break
                        sleep_pool -= enemy_soldier.hitpoints
                        if sleep_pool > 0:
                            self.fireball_action_target(soldier, squad, spell_dict, enemy)
                    continue
                if spell_dict.get('damage_dice'):
                    # Magic_Missile всегда попадает.
                    if spell_dict.get('direct_hit'):
                        attack_dict = soldier.spell_attack(spell_dict, enemy,
                                squad.metadict_soldiers,
                                advantage = advantage, disadvantage = disadvantage)
                        attack_result = enemy_soldier.take_attack(
                                spell_choice, attack_dict, self.metadict_soldiers)
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
                elif spell_dict.get('debuff') and debuff_dict:
                    attack_result = debuff_dict
                else:
                    attack_result = spell_dict
                # Заклинание Hex:
                if attack_result.get('hit') and soldier.concentration\
                        and soldier.concentration.get('effect') == 'hex'\
                        and soldier.concentration['effect'] in enemy_soldier.debuffs\
                        and soldier.concentration.get('target_uuid') == enemy_soldier.uuid:
                    spell_dict = soldier.concentration
                    self.fireball_action(soldier, squad, spell_dict, enemy.place,
                            single_target = enemy)
                # Победа приносит бойцу опыт:
                if attack_result.get('fatal_hit'):
                    soldier.set_victory_and_enemy_defeat(enemy_soldier)
                    # Критический удар калечит цель:
                    if attack_result['crit']:
                        enemy_soldier.set_disabled()
                # Убираем противника из списка целей и с карты:
                if attack_result.get('fatal_hit'):
                    if 'kill' in soldier.commands:
                        enemy_soldier.killer_mark = True
                    self.clear_battlemap()
                    fall_place = enemy_soldier.place
                    self.dict_battlespace[fall_place].append('fall_place')
                    self.dict_battlespace[fall_place].append(enemy_soldier.ally_side)
                    if squad.enemies and enemy.uuid in squad.enemies:
                        squad.enemies.pop(enemy.uuid)
                # Обобщаем статистику атак (расход боеприпасов и прочее):
                self.set_squad_battle_stat(attack_result, squad)

    def channel_action(self, soldier, squad, enemy):
        """Боец использует божественный канал."""
        if soldier.battle_action\
                and soldier.__dict__.get('channel_divinity')\
                and soldier.channel_divinity > 0:
            enemy_soldier = self.metadict_soldiers[enemy.uuid]
            if soldier.class_features.get('Channel_Dreadful_Aspect')\
                    and soldier.near_enemies and len(soldier.near_enemies) > 1:
                spell_choice = 'channel', 'Dreadful_Aspect'
                spell_dict = soldier.spells[spell_choice]
                spell_dict['spell_choice'] = spell_choice
                self.fireball_action(soldier, squad, spell_dict, soldier.place, safe = True)
                soldier.channel_divinity -= 1
            elif soldier.class_features.get('Channel_Radiance_of_the_Dawn')\
                    and soldier.near_enemies and len(soldier.near_enemies) > 1:
                # TODO: добавь развеивание темноты "Darkness".
                # Обязательно, потому что Сияние рассвета поражает только видимые цели.
                spell_choice = 'channel', 'Radiance_of_the_Dawn'
                spell_dict = soldier.spells[spell_choice]
                spell_dict['spell_choice'] = spell_choice
                self.fireball_action(soldier, squad, spell_dict, soldier.place, safe = True)
                soldier.channel_divinity -= 1
            elif soldier.class_features.get('Channel_Sacred_Weapon')\
                    and not soldier.sacred_weapon:
                soldier.sacred_weapon = soldier.mods['charisma']
                soldier.sacred_weapon_timer = 10
                soldier.channel_divinity -= 1
                soldier.battle_action = False
            # Жрец домена бури усиливает заклинание до предела:
            elif soldier.class_features.get('Channel_Destructive_Wrath')\
                    and not soldier.destructive_wrath:
                soldier.destructive_wrath = True
                self.fireball_action(soldier, squad)
                soldier.channel_divinity -= 1

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
            if debuff not in enemy_soldier.debuffs:
                return enemy_soldier

    def counterspell_action(self, spell_dict, soldier, targets):
        """Контрзаклинание.
        
        - Если заклинание 3+ круга.
        - Если заклинание зональное.
        - Если враг видит заклинателя.
        """
        # TODO: проверка базовой характеристики, СЛ 10 + уровень_заклинания.
        # Это если рассеивать заклинания выше уровня контрзаклинания.
        spell_choice = spell_dict['spell_choice']
        counterspell_enemies = [enemy_soldier\
                for enemy_soldier in self.metadict_soldiers.values()\
                if enemy_soldier.__dict__.get('place')\
                and enemy_soldier.ally_side == soldier.enemy_side\
                and enemy_soldier.spells_generator.find_spell('counterspell', effect = True)]
        if counterspell_enemies:
            for enemy_soldier in counterspell_enemies:
                # Контрзаклинание срабатывает только если враг видит мага,
                # И если под ударом заклинания есть союзники контркастера:
                targets_enemy_allies = [target for target in targets
                        if target.side == enemy_soldier.ally_side]
                vision_tuple = self.calculate_enemy_cover(enemy_soldier.place, soldier.place)
                if vision_tuple.visibility and targets_enemy_allies:
                    counterspell_dict = enemy_soldier.try_spellcast('counterspell')
                    if counterspell_dict:
                        # Прерывание концентрации мага:
                        if soldier.concentration and spell_dict == soldier.concentration:
                            soldier.set_concentration_break(autofail = True)
                            if not namespace.test:
                                print('DISPELL', soldier.ally_side, soldier.place, spell_choice, '<<',
                                        enemy_soldier.ally_side, enemy_soldier.place,
                                        counterspell_dict['spell_choice'])
                        else:
                            if not namespace.test:
                                print('COUNTERSPELL', soldier.ally_side, soldier.place, spell_choice, '<<',
                                        enemy_soldier.ally_side, enemy_soldier.place,
                                        counterspell_dict['spell_choice'])
                        return True

    def fireball_action(self, soldier, squad, spell_dict = None, zone_center = None,
            safe = False, single_target = False):
        """Маг работает артиллерией."""
        if hasattr(soldier, 'spells') and soldier.battle_action\
                and self.select_zone_spell(soldier, squad)\
                or spell_dict and zone_center\
                or spell_dict:
            if spell_dict and zone_center:
                # Точка удара заклинания предопределена:
                spell_choice = spell_dict['spell_choice']
                auto_zone_target = False
                #soldier.use_spell_ammo(spell_dict)
            elif spell_dict:
                # Поиск точки удара для выбранного заклинания:
                spell_choice = spell_dict['spell_choice']
                auto_zone_target = True
                if self.select_zone_spell(soldier, squad, spell_choice_once = spell_choice):
                    spell_choice, zone_center = self.select_zone_spell(soldier, squad,
                            spell_choice_once = spell_choice)
                    soldier.use_spell_ammo(spell_dict)
                else:
                    return False
            else:
                # Поиск подходящего заклинания и точки удара для него:
                auto_zone_target = True
                spell_choice, zone_center = self.select_zone_spell(soldier, squad)
                # Зональная атака из словаря концентрации. Call_Lightning, Moonbeam и т.д.
                if soldier.concentration\
                        and soldier.concentration.get('spell_choice')\
                        and spell_choice == soldier.concentration['spell_choice']:
                    #spell_dict = soldier.try_spellcast(spell_choice,
                    #        use_spell_slot = False, use_action = True,
                    #        gen_spell = soldier.concentration)
                    if soldier.check_action_to_spellcast(spell_choice):
                        spell_dict = soldier.concentration
                        soldier.use_action_to_spellcast(spell_dict)
                        #soldier.use_spell_ammo(spell_dict)
                    else:
                        return False
                # Зональная атака из списка атак. Дыхание дракона, молния штормового великана и т.д.
                elif spell_choice in soldier.attacks:
                    spell_dict = soldier.attacks[spell_choice]
                    spell_dict['spell_choice'] = spell_choice
                    soldier.use_ammo(soldier.attacks[spell_choice], squad.metadict_soldiers)
                # Используется слот заклинания:
                else:
                    spell_dict = soldier.try_spellcast(spell_choice)
            # Зона заклинания превращается в список кортежей с целями:
            targets = self.find_targets_in_zone(
                    zone_center = zone_center,
                    zone_shape = spell_dict.get('zone_shape'),
                    zone_radius = round(spell_dict.get('radius', 0) / self.tile_size),
                    distance = round(spell_dict.get('attack_range', 0) / self.tile_size),
                    point_of_view = soldier.place
                    )
            if targets:
                # Вражеское контрзаклинание, если наше заклинание 3+ круга:
                if spell_choice[0][0].isnumeric() and int(spell_choice[0][0]) >= 3:
                    counterspell = self.counterspell_action(spell_dict, soldier, targets)
                    if counterspell:
                        return False
                if single_target:
                    targets = [target for target in targets
                            if target.uuid == single_target.uuid]
                # Жрец домена бури усиливает заклинание до предела:
                if soldier.destructive_wrath and len(targets) > 3 and spell_dict.get('damage_type'):
                    if spell_dict['damage_type'] == 'thunder' or spell_dict['damage_type'] == 'lightning':
                        spell_dict['destructive_wrath'] = True
                        damage_mod = spell_dict['damage_mod']
                        damage_mod += int(spell_dict['damage_dice'][0]) * int(spell_dict['damage_dice'][-1])
                        spell_dict['damage_dice'] = '0d0'
                        spell_dict['damage_mod'] = damage_mod
                        soldier.destructive_wrath = False
                # Неподвижные зональные заклинания:
                if spell_dict.get('effect') == 'sickening_radiance':
                    zone_radius = round(spell_dict['radius'] / self.tile_size)
                    if not spell_dict.get('zone_center'):
                        spell_dict['zone_center'] = zone_center
                        spell_dict['concentration_ready'] = True
                        try:
                            self.change_place_effect(spell_dict['effect'],
                                    spell_dict['zone_center'], zone_center, zone_radius)
                            if spell_dict.get('zone_danger'):
                                self.change_place_effect('danger_terrain',
                                        spell_dict['zone_center'], zone_center, zone_radius)
                        except ValueError:
                            #traceback.print_exc()
                            pass
                    if not single_target:
                        return False
                # Подвижные зональные заклинания вроде Flaming_Sphere:
                if spell_dict.get('effect') == 'dawn'\
                        or spell_dict.get('effect') == 'bonfire'\
                        or spell_dict.get('effect') == 'vitriolic_sphere'\
                        or spell_dict.get('effect') == 'flaming_sphere'\
                        or spell_dict.get('effect') == 'moonbeam':
                    zone_radius = round(spell_dict['radius'] / self.tile_size)
                    if not spell_dict.get('zone_center'):
                        spell_dict['zone_center'] = zone_center
                        if spell_dict.get('effect') == 'flaming_sphere':
                            path = sight_line_to_list(soldier.place, zone_center)
                            for place in path:
                                place = self.check_place(soldier, place)
                                if place.free:
                                    zone_center = place.place
                                    spell_dict['zone_center'] = zone_center
                    # TODO: эту селекцию можно использовать для любых заклинаний:
                    # Накат "Пламенного шара", только одна цель. Выбор кастером из ближайших:
                    elif not single_target and spell_dict.get('effect') == 'flaming_sphere':
                        # Сфера перемещается дальше радиуса начального каста. Пока костыль:
                        path = sight_line_to_list(spell_dict['zone_center'], zone_center)
                        for n, place in enumerate(path):
                            place = self.check_place(soldier, place)
                            if not place.free:
                                zone_center = path[n-1]
                                break
                        targets = self.find_targets_in_zone(
                                zone_center = zone_center,
                                zone_shape = spell_dict.get('zone_shape'),
                                zone_radius = round(spell_dict.get('radius', 0) / self.tile_size),
                                distance = round(spell_dict.get('attack_range', 0) / self.tile_size),
                                point_of_view = soldier.place
                                )
                        if targets and len(targets) > 0:
                            targets = [target for target in targets if target.side == soldier.enemy_side]
                            targets = [soldier.select_enemy(targets)]
                        # Убираем точку удара, чтобы следующие "Flaming_Sphere" не били в одно место:
                        if zone_center in squad.danger_points:
                            squad.danger_points.pop(zone_center)
                        if not targets or len(targets) == 0 or not targets[0]:
                            return False
                    if not single_target:
                        try:
                            self.change_place_effect(spell_dict['effect'],
                                    spell_dict['zone_center'], zone_center, zone_radius)
                            if spell_dict.get('zone_danger'):
                                self.change_place_effect('danger_terrain',
                                        spell_dict['zone_center'], zone_center, zone_radius)
                        except ValueError:
                            #traceback.print_exc()
                            pass
                    # Первая атака лучом по всем в зоне:
                    if not single_target and spell_dict.get('ammo'):
                        spell_dict['zone_center'] = zone_center
                        spell_dict['ammo'] -=1
                    # Перенацеливание луча, без мгновенного урона:
                    elif not single_target and spell_dict.get('ammo') == 0:
                        spell_dict['zone_center'] = zone_center
                        return False
                    else:
                        spell_dict['zone_center'] = zone_center
                # Перемещение в центр зоны заклинания (whirlwind воздушного элементаля)
                if spell_dict.get('effect') == 'move':
                    self.change_place(soldier.place, zone_center, soldier.uuid)
                # Субзаклинание для заклинаний вроде "Ice_Storm"
                subspell_dict = None
                if spell_dict.get('subspell'):
                    subspell_dict = soldier.try_spellcast(spell_dict.get('subspell'),
                            use_spell_slot = False, use_action = False, gen_spell = True)
                # Зональное заклинание поражает цели:
                for enemy in targets:
                    self.fireball_action_target(soldier, squad, spell_dict, enemy, safe)
                    if subspell_dict:
                        self.fireball_action_target(soldier, squad, subspell_dict, enemy, safe)
                # TODO: сделай декоратор.
                # Переоцениваем опасные зоны на текущий ход:
                if auto_zone_target and squad.commanders_list:
                    squad.danger_points = battle.find_danger_zones(
                            squad.enemy_side, zone_length = 5,
                            soldier_coordinates = squad.commanders_list[0].place)

    def fireball_action_target(self, soldier, squad, spell_dict, enemy, safe = False):
        """Зональное заклинание ранит отдельную цель.
        
        """
        spell_choice = spell_dict['spell_choice']
        enemy_soldier = self.metadict_soldiers[enemy.uuid]
        # Не вредит своим
        if spell_dict.get('safe'):
            safe = spell_dict['safe']
        if safe and enemy.side in soldier.ally_side:
            return False
        # Вредит только нечисти:
        if spell_dict.get('effect') == 'holy_water'\
                and not races.dict_races[enemy_soldier.race].get('unholy')\
                and not enemy_soldier.__dict__.get('unholy'):
            return False
        # Огненные заклинания в воде наносят 50% урона:
        if 'water' in self.dict_battlespace[enemy_soldier.place]\
                and spell_dict.get('damage_type') == 'fire':
            spell_dict['damage_halved'] = True
        # Срабатывают вредоносные эффекты заклинаний:
        if spell_dict.get('debuff'):
            spell_dict['target_uuid'] = enemy_soldier.uuid
            debuff_dict = enemy_soldier.set_debuff(spell_dict)
            if debuff_dict:
                debuff_dict['hit'] = True
                # Показываем усыплённых:
                if debuff_dict.get('effect') == 'sleep':
                    fall_place = enemy_soldier.place
                    self.dict_battlespace[fall_place].append('fall_place')
                    self.dict_battlespace[fall_place].append(enemy_soldier.ally_side)
                if not namespace.test:
                    effect_upper = debuff_dict.get('effect', spell_choice[-1]).upper()
                    print('[+++] {side_1}, {c1} {s} {effect_upper} >> {side_2} {c2} {e} {r}'.format(
                        side_1 = soldier.ally_side,
                        c1 = soldier.place,
                        s = soldier.behavior,
                        side_2 = enemy_soldier.ally_side,
                        c2 = enemy_soldier.place,
                        e = enemy_soldier.behavior,
                        r = enemy_soldier.rank,
                        effect_upper = effect_upper
                        ))
            # Если заклинание не наносит урона, то прерывание:
            #if not spell_dict.get('damage_dice'):
            #    return True
        # TODO: всё это переносить в функции заклинаний и set_debuff:
        # Вызов страха от паладинского Dreadful_Aspect и заклинания "Fear"
        if spell_dict.get('effect') == 'fear':
            fear = enemy_soldier.set_fear(soldier, spell_dict['spell_save_DC'])
            if fear:
                # Враг бросает оружие и бежит:
                enemy_soldier.unset_shield(disarm = True)
                enemy_soldier.unset_weapon(enemy_soldier.weapon_ready, disarm = True)
                #print('[+++] {side_1}, {c1} {s} FEAR >> {side_2} {c2} {e}'.format(
                #    side_1 = soldier.ally_side,
                #    c1 = soldier.place,
                #    s = soldier.behavior,
                #    side_2 = enemy_soldier.ally_side,
                #    c2 = enemy_soldier.place,
                #    e = enemy_soldier.behavior,
                #    ))
            if not spell_dict.get('damage_dice'):
                return True
        # TODO: всё это переносить в функции заклинаний и set_debuff:
        if spell_dict.get('effect') == 'stun':
            stunned = enemy_soldier.set_stunned(
                    spell_dict['spell_save_DC'], spell_dict['effect_timer'])
            #if stunned:
            #    print('[+++] {side_1}, {c1} {s} STUNNED >> {side_2} {c2} {e}'.format(
            #        side_1 = soldier.ally_side,
            #        c1 = soldier.place,
            #        s = soldier.behavior,
            #        side_2 = enemy_soldier.ally_side,
            #        c2 = enemy_soldier.place,
            #        e = enemy_soldier.behavior,
            #        ))
            if not spell_dict.get('damage_dice'):
                return True
        # TODO: всё это переносить в функции заклинаний и set_debuff:
        if spell_dict.get('effect') == 'paralyze':
            paralyzed = enemy_soldier.set_paralyzed(
                    spell_dict['spell_save_DC'], spell_dict['effect_timer'])
            #if paralyzed:
            #    print('[+++] {side_1}, {c1} {s} PARALYZED >> {side_2} {c2} {e}'.format(
            #        side_1 = soldier.ally_side,
            #        c1 = soldier.place,
            #        s = soldier.behavior,
            #        side_2 = enemy_soldier.ally_side,
            #        c2 = enemy_soldier.place,
            #        e = enemy_soldier.behavior,
            #        ))
            if not spell_dict.get('damage_dice'):
                return True
        # TODO: всё это переносить в функции заклинаний и set_debuff:
        #elif spell_dict.get('effect') == 'sleep':
        #    sleep = enemy_soldier.set_sleep(
        #            spell_dict['spell_save_DC'], spell_dict['effect_timer'])
        #    if sleep:
        #        self.clear_battlemap()
        #        fall_place = enemy_soldier.place
        #        self.dict_battlespace[fall_place].append('fall_place')
        #        self.dict_battlespace[fall_place].append(enemy_soldier.ally_side)
        #        print('[+++] {side_1}, {c1} {s} SLEEP >> {side_2} {c2} {e}'.format(
        #            side_1 = soldier.ally_side,
        #            c1 = soldier.place,
        #            s = soldier.behavior,
        #            side_2 = enemy_soldier.ally_side,
        #            c2 = enemy_soldier.place,
        #            e = enemy_soldier.behavior,
        #            ))
        #    if not spell_dict.get('damage_dice'):
        #        return True
        # У заклинания Ice_Knife есть и шрапнель, и основной поражающий элемент:
        if spell_dict.get('effect') == 'ice_knife' and enemy.place == zone_center:
            self.spellcast_action(soldier, squad, enemy,
                    spell_choice = spell_dict['subspell'], subspell = True, use_spell = False)
        # Атака заклинанием:
        if spell_dict.get('damage_dice'):
            advantage, disadvantage = self.test_enemy_defence(soldier, enemy_soldier, spell_choice)
            if spell_dict.get('direct_hit'):
                attack_dict = soldier.spell_attack(spell_dict, enemy,
                        squad.metadict_soldiers,
                        advantage = advantage, disadvantage = disadvantage)
                attack_result = enemy_soldier.take_attack(
                        spell_choice, attack_dict, self.metadict_soldiers)
            # Заклинания с показателем атаки мало отличаются от стрел и мечей:
            elif spell_dict.get('attack_mod') or spell_dict.get('attack_mod') == 0:
                attack_dict = soldier.attack(spell_dict, spell_choice,
                        enemy, self.metadict_soldiers,
                        advantage = advantage, disadvantage = disadvantage)
                attack_result = enemy_soldier.take_attack(
                        spell_choice, attack_dict, self.metadict_soldiers)
            else:
                print('NYA. Недопиленое заклинание', spell_choice, spell_dict)
                return False
            if spell_dict.get('effect') == 'steal_life':
                bonus_hitpoints_bless = attack_result['damage']
                if bonus_hitpoints_bless > soldier.bonus_hitpoints:
                    soldier.set_hitpoints(bonus_hitpoints = bonus_hitpoints_bless)
        elif spell_dict.get('debuff') and debuff_dict:
            attack_result = debuff_dict
        else:
            attack_result = spell_dict
        # Победа приносит бойцу опыт:
        if attack_result.get('fatal_hit'):
            soldier.set_victory_and_enemy_defeat(enemy_soldier)
            # Критический удар калечит цель:
            if attack_result['crit']:
                enemy_soldier.set_disabled()
        # Убираем противника из списка целей и с карты:
        if attack_result.get('fatal_hit'):
            if 'kill' in soldier.commands:
                enemy_soldier.killer_mark = True
            self.clear_battlemap()
            fall_place = enemy_soldier.place
            self.dict_battlespace[fall_place].append('fall_place')
            self.dict_battlespace[fall_place].append(enemy_soldier.ally_side)
            if squad.enemies and enemy.uuid in squad.enemies:
                squad.enemies.pop(enemy.uuid)
        # Обобщаем статистику атак (расход боеприпасов и прочее):
        self.set_squad_battle_stat(attack_result, squad)
        if attack_result.get('hit'):
            return True
        else:
            return False

    def select_zone_spell(self, soldier, squad, spell_choice_once = False):
        """Выбор заклинания, бьющего по территории и точки атаки для него."""
        spell_choice_list = []
        if soldier.concentration and type(soldier.concentration) == dict\
                and 'zone' in soldier.concentration\
                and soldier.concentration.get('spell_choice'):
            spell_choice_list.append(soldier.concentration.get('spell_choice'))
        for attack_choice, attack_dict in soldier.attacks.items():
            if attack_choice[0] == 'zone' and 'zone' in attack_dict:
                spell_choice_list.append(attack_choice)
        for spell_slot in soldier.spellslots:
            # Без приказа только заклинания 1 круга:
            if int(spell_slot[0]) < 2 or 'fireball' in soldier.commands:
                slot_spells_list = [attack for attack in soldier.spells if attack[0] == spell_slot
                        and soldier.spells[attack].get('zone')]
                spell_choice_list.extend(slot_spells_list)
        if spell_choice_list or spell_choice_once:
            if spell_choice_once:
                spell_choice_list = [spell_choice_once]
            else:
                # Сортируем. Сначала заклинания высших уровней:
                spell_choice_list = sorted(spell_choice_list, reverse = True)
            for spell_choice in spell_choice_list:
                # Заклинание может быть в списке атак:
                if spell_choice in soldier.attacks:
                    spell_dict = soldier.attacks[spell_choice]
                elif soldier.concentration and spell_choice == soldier.concentration.get('spell_choice'):
                    spell_dict = soldier.concentration
                else:
                    spell_dict = soldier.spells[spell_choice]
                # Подготовленные залкинания вроде Hail_of_Thorns пропускаем:
                if 'concentration_ready' in spell_dict and not spell_choice_once:
                    continue
                # Полезные заклинания пропускаем:
                elif spell_dict.get('buff'):
                    continue
                attack_range = round(spell_dict['attack_range'] / self.tile_size)
                for zone_center, danger in squad.danger_points.items():
                    distance = round(distance_measure(soldier.place, zone_center))
                    # На себя не наводим:
                    if not distance == 0:
                        targets = self.find_targets_in_zone(
                                zone_center = zone_center,
                                zone_shape = spell_dict.get('zone_shape'),
                                zone_radius = round(spell_dict.get('radius', 0) / self.tile_size),
                                distance = round(spell_dict.get('attack_range', 0) / self.tile_size),
                                point_of_view = soldier.place
                                )
                        if targets:
                            # Пропускаем точку удара, если союзники страдают больше врагов.
                            target_allies = [target for target in targets
                                    if target.side == soldier.ally_side]
                            target_enemies = [target for target in targets
                                    if target.side == soldier.enemy_side]
                            if len(target_allies) * self.danger_factor >= len(target_enemies)\
                                    and not spell_dict.get('safe'):
                                continue
                            # Пропускаем точку удара, если там есть союзные бойцы.
                            if spell_dict.get('accurate') or 'accurate' in soldier.commands\
                                    and not spell_dict.get('safe')\
                                    and target_allies:
                                    continue
                            if not spell_dict.get('zone_shape') == 'cone'\
                                    and not spell_dict.get('zone_shape') == 'ray'\
                                    and distance <= attack_range:
                                return spell_choice, zone_center
                            elif spell_dict.get('zone_shape') == 'cone'\
                                    and distance <= attack_range / 2\
                                    and not distance == 0:
                                return spell_choice, zone_center
                            elif spell_dict.get('zone_shape') == 'ray'\
                                    and distance <= attack_range / 2\
                                    and not distance == 0:
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

    def test_enemy_defence(self, soldier, enemy_soldier, attack_choice):
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
        # Homebrew, постоянная помеха:
        # TODO: замени на отравление алкоголем и "добряникой" сатиров:
        if soldier.__dict__.get('squad_disadvantage'):
            disadvantage = True
        # Homebrew, идеальное взаимодействие свиты:
        if enemy_soldier.__dict__.get('squad_advantage'):
            disadvantage = True
        # Homebrew, солдаты без умения плавать уязвимы (по правилам из "Книги игрока" -- нет):
        #if not enemy_soldier.water_walk and 'water' in self.dict_battlespace[enemy_soldier.place]:
        #    advantage = True
        # Две цели на одной точке. Легче попасть.
        # "Книга игрока", "Протискивание в меньшее пространство"
        if len([el for el in self.dict_battlespace[enemy_soldier.place]
            if type(el) == tuple and not el[1] == 'mount' and not el[-1] == soldier.uuid]) >= 2:
            if not enemy_soldier.size == 'tiny':
                advantage = True
        # Ошеломлённый уязвим:
        if enemy_soldier.stunned:
            advantage = True
        # Парализованный уязвим:
        if enemy_soldier.paralyzed:
            advantage = True
        # Опутанный уязвим:
        if enemy_soldier.restrained:
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
        # Преимущество от "Тактики стаи", если союзник рядом с врагом:
        if soldier.class_features.get('Pack_Tactic') and len(enemy_soldier.near_enemies) > 1:
            advantage = True
        # Верховой боец атакует с преимуществом, если цель не всадник:
        if attack_choice[0] == 'close' or attack_choice[0] == 'reach':
            if soldier.class_features.get('Feat_Mounted_Combatant')\
                    and soldier.mount_combat\
                    and hasattr(soldier, 'mount_uuid')\
                    and self.metadict_soldiers.get(soldier.mount_uuid)\
                    and self.metadict_soldiers[soldier.mount_uuid].place == soldier.place:
                if not hasattr(enemy_soldier, 'mount_uuid')\
                        or hasattr(enemy_soldier, 'mount_uuid')\
                        and hasattr(self.metadict_soldiers[enemy_soldier.mount_uuid], 'place')\
                        and not self.metadict_soldiers[enemy_soldier.mount_uuid].place == enemy_soldier.place:
                    advantage = True
        # Отравленный получает помеху на атаки:
        if 'poisoned' in soldier.debuffs:
            disadvantage = True
        # Опутанный получает помеху на атаки:
        if soldier.restrained == True:
            disadvantage = True
        # Наш боец может быть сбит с ног (и ему не удалось подняться в начале раунда):
        if soldier.prone == True:
            disadvantage = True
        # Учитываем, что противник может защищаться:
        if enemy_soldier.dodge_action == True:
            disadvantage = True
        # Заклинание 'Размытый образ' прикрывает от атак:
        if 'blur' in enemy_soldier.buffs:
            disadvantage = True
        # В темноте/тумане сложно атаковать:
        if 'obscure_terrain' in self.dict_battlespace[enemy_soldier.place]:
            disadvantage = True
        # Два наших бойца на одной точке. Сложно целиться:
        # "Книга игрока", "Протискивание в меньшее пространство"
        if len([el for el in self.dict_battlespace[soldier.place]
            if type(el) == tuple and not el[1] == 'mount' and not el[-1] == enemy_soldier.uuid]) >= 2:
            if not enemy_soldier.size == 'tiny':
                disadvantage = True
        # Влияние погоды:
        if attack_choice[0] == 'throw' or attack_choice[0] == 'ranged' or attack_choice[0] == 'volley':
            # Сильный ветер мешает стрелкам:
            if 'warding_wind' in self.dict_battlespace[enemy_soldier.place]:
                disadvantage = True
            # Вода мешает стрелкам:
            if 'water' in self.dict_battlespace[soldier.place] and not soldier.water_walk:
                disadvantage = True
        # TODO: перенеси это в attack класса бойца:
        if not disadvantage:
            # Frostbite портит одиночкую атаку:
            if 'frostbite' in soldier.debuffs:
                soldier.debuffs.pop('frostbite')
                disadvantage = True
            if 'mockery' in soldier.debuffs:
                soldier.debuffs.pop('mockery')
                disadvantage = True
            # Противника может защитить товарищ с Fighting_Style_Protection:
            if len(enemy_soldier.near_allies) > 1:
                for soldier_tuple in enemy_soldier.near_allies:
                    enemy_ally = self.metadict_soldiers[soldier_tuple.uuid]
                    if enemy_ally.class_features.get('Fighting_Style_Protection')\
                            and enemy_ally.reaction == True\
                            and enemy_ally.uuid != enemy_soldier.uuid\
                            and enemy_ally.armor['shield_use'] != None\
                            and enemy_ally.shield_ready:
                        disadvantage = enemy_ally.set_protection(enemy_soldier)
                        #print('{0} {1} {2} attack {3} {4} {5} reaction protect from {6} {7} {8}'.format(
                        #    soldier.ally_side, soldier.place, soldier.behavior,
                        #    enemy_soldier.ally_side, enemy_soldier.place, enemy_soldier.behavior,
                        #    enemy_ally.ally_side, enemy_ally.place, enemy_ally.behavior))
                        break
            # TODO: перенеси это в attack класса бойца:
            # Жрец домена света может поставить помеху на одиночную атаку (на дистанции до 30 футов):
            if hasattr(enemy_soldier, 'warding_flare') and enemy_soldier.warding_flare > 0\
                    and enemy_soldier.reaction\
                    and distance_measure(enemy_soldier.place, soldier.place) <= 30 / self.tile_size:
                enemy_soldier.warding_flare -= 1
                enemy_soldier.reaction = False
                disadvantage = True
        return advantage, disadvantage

    def break_enemy_defence(self, soldier, squad, enemy_soldier, attack_choice):
        """Проверяем, есть ли преимущества или помехи в атаке на врага."""
        advantage = False
        # Homebrew, идеальное взаимодействие свиты:
        if soldier.__dict__.get('squad_advantage'):
            advantage = True
            return advantage
        # Подсвеченный уязвим:
        if 'guiding_bolt' in enemy_soldier.debuffs:
            enemy_soldier.debuffs.pop('guiding_bolt')
            advantage = True
            return advantage
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
                                and not 'dodge' in soldier.commands\
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
            return soldier.select_enemy(soldier.near_enemies)
        # Если приказано брать пленных, то дальнее оружие не используем.
        elif 'enslave' in soldier.commands and not soldier.near_enemies:
            return None
        if 'reach' in [attack[0] for attack in soldier.attacks]:
            near_enemies = self.find_enemies_near(soldier, distance = 2)
            if near_enemies:
                return soldier.select_enemy(near_enemies)
        if 'throw' in [attack[0] for attack in soldier.attacks]:
            near_enemies = self.find_enemies_near(soldier, distance = 2)
            if near_enemies:
                return soldier.select_enemy(near_enemies)
        # Командир выбирает целью вражеских командиров:
        if squad.enemies and soldier.behavior == 'commander'\
                or squad.enemies and "select_strongest" in soldier.commands:
            sorted_enemies = self.refind_soldiers_distance(soldier.place, squad.enemies)
            visible_enemies = self.find_visible_soldiers(
                    soldier.place, soldier.enemy_side, sorted_enemies,
                    max_number = 60, max_try = 120)
            return soldier.select_enemy(visible_enemies, select_strongest = True)
        # Сортируем цели по дистанции и берём по три, чтобы захватить всадника и коня:
        elif squad.enemies:
            sorted_enemies = self.refind_soldiers_distance(soldier.place, squad.enemies)
            visible_enemies = self.find_visible_soldiers(
                    soldier.place, soldier.enemy_side, sorted_enemies,
                    max_number = 3, max_try = 6)
            return soldier.select_enemy(visible_enemies)
        # Ищем цели в зоне видимости без указания командира:
        if 'seek' in soldier.commands:
            visible_enemies = self.find_visible_soldiers(soldier.place, soldier.enemy_side,
                    max_number = 3, max_try = 6)
            return soldier.select_enemy(visible_enemies)

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
        
        - Он выбирает случайную точку спавна врага в диапазоне дистанций и следует к ней.
        - Если не находит, то возвращает координаты самого бойца.
        """
        coord_dict = {}
        for el in self.spawn_list:
            if side in self.dict_battlespace[el.place]\
                    and 'spawn' in self.dict_battlespace[el.place]:
                distance = round(distance_measure(soldier_coordinates, el.place))
                coord_dict[el.place] = distance
        coord_dict = OrderedDict(sorted(coord_dict.items(),key=lambda x: x[1]))
        if len(coord_dict) < random_range:
            random_range = len(coord_dict)
        if len(coord_dict) > 0:
            key_number = random.randrange(0, int(len(coord_dict) / random_range))
            for n, key in enumerate(coord_dict.keys()):
                if n == key_number:
                    return key
        else:
            return False

    def fall_to_death(self, squad):
        """Тяжелораненые делают спасброски от смерти в начале каждого хода.
        
        Death Saving Throws:
        https://www.dandwiki.com/wiki/5e_SRD:Dropping_to_0_Hit_Points
        """
        for soldier in squad.metadict_soldiers.values():
            # Спящего от заклинания Sleep разбудят (или сам проснётся)
            if 'sleep' in soldier.debuffs and not soldier.captured:
                self.rescue(soldier, squad)
            # Тяжелораненые играют в рулетку с мрачным жнецом:
            if soldier.hitpoints <= 0 and not soldier.death and not soldier.stable:
                soldier.set_death()
            if soldier.hitpoints <= 0 and not soldier.death and not soldier.stable:
                if hasattr(squad, 'commands') and 'rescue' in squad.commands:
                    self.rescue(soldier, squad)
                    # TODO: спасаем магией начиная с 1 lvl, или со 2 lvl?
                    if not soldier.stable and soldier.death_save_loss >= 1\
                            or not soldier.stable and soldier.hero:
                        self.rescue_magic(soldier)
            # Офицеров лечат эссенциями и добряникой:
            elif soldier.hitpoints <= 0 and soldier.stable and not soldier.captured:
                if hasattr(squad, 'commands') and 'rescue' in squad.commands:
                    if soldier.level >= 3 or soldier.hero:
                        self.rescue(soldier, squad)
                        self.rescue_magic(soldier)

    def rescue(self, soldier, squad):
        """Товарищи стабилизируют тяжелораненых и будят спящих.
        
        Как это работает:
        1) Тяжелораненые и спящие "просят" помощи у всех вокруг.
        2) Если кто-то способен помочь, он помогает с help_action.
        3) Товарищ оттаскивает раненого к себе и пытается перевязать.
        """
        # Раненого можно вытащить, если он не схвачен:
        if not soldier.grappled\
                and not soldier.behavior == 'mount'\
                and not soldier.__dict__.get('mechanism'):
            self.recon_action(soldier, squad)
            for ally in soldier.near_allies:
                ally_soldier = self.metadict_soldiers[ally.uuid]
                if len(ally_soldier.near_enemies) <= 1\
                        and not ally_soldier.hitpoints <= 0\
                        and not ally_soldier.uuid == soldier.uuid\
                        and not ally_soldier.escape\
                        and not 'sleep' in ally_soldier.debuffs:
                    # Если рядом враги, раненого вытаскивают из боя:
                    if len(soldier.near_enemies) > 0:
                        if 'fall_place' in self.dict_battlespace[soldier.place]\
                                and not soldier.place == ally_soldier.place\
                                and soldier.ally_side in self.dict_battlespace[soldier.place]:
                            self.dict_battlespace[soldier.place].remove('fall_place')
                            self.dict_battlespace[soldier.place].remove(soldier.ally_side)
                        self.change_place(soldier.place, ally_soldier.place, soldier.uuid)
                    if soldier.killer_mark:
                        soldier.killer_mark = False
                    if 'sleep' in soldier.debuffs:
                        soldier.debuffs.pop('sleep')
                        if 'fall_place' in self.dict_battlespace[soldier.place]\
                                and soldier.ally_side in self.dict_battlespace[soldier.place]:
                            self.dict_battlespace[soldier.place].remove('fall_place')
                            self.dict_battlespace[soldier.place].remove(soldier.ally_side)
                        break
                    elif soldier.captured:
                        soldier.captured = False
                        break
                    # Только одна попытка первой помощи за ход:
                    # Сначала перевязка. Затем откармливание добряникой.
                    else:
                        if not soldier.stable:
                            ally_soldier.first_aid(soldier)
                        elif soldier.stable and soldier.hitpoints <= 0:
                            ally_soldier.first_aid(soldier)
                        if not soldier.stable\
                                and not 'fall_place' in self.dict_battlespace[soldier.place]:
                            self.dict_battlespace[soldier.place].append('fall_place')
                            self.dict_battlespace[soldier.place].append(soldier.ally_side)
                        break

    def rescue_magic(self, soldier):
        """Клирик спасает раненого, используя Healing_Word."""
        for healer in self.metadict_soldiers.values():
            if healer.spells_generator.find_spell('Healing_Word')\
                    and not healer.defeat and not healer.fall\
                    and healer.ally_side == soldier.ally_side\
                    and healer.__dict__.get('place')\
                    and 'spellcast' in healer.commands:
                spell_choice = healer.spells_generator.find_spell('Healing_Word')
                spell_dict = healer.spells_generator.get_spell_dict(spell_choice)
                distance_max = spell_dict['attack_range'] / self.tile_size
                vision_tuple = self.calculate_enemy_cover(healer.place, soldier.place)
                if vision_tuple.visibility and vision_tuple.distance < distance_max:
                    healer.try_spellcast(spell_choice, gen_spell = {'target_uuid':soldier.uuid})
                    if soldier.stable:
                        if 'fall_place' in self.dict_battlespace[soldier.place]\
                                and soldier.ally_side in self.dict_battlespace[soldier.place]:
                            self.dict_battlespace[soldier.place].remove('fall_place')
                            self.dict_battlespace[soldier.place].remove(soldier.ally_side)
                        break

    def clear_battlemap(self, uuid_for_clear = None):
        """Чистим карту от павших/беглецов.
        
        Убираем всех, у кого хитов меньше нуля. А также сбежавших с поля боя.
        """
        for place, content in self.dict_battlespace.items():
            for el in content:
                if type(el) == tuple:
                    uuid = el[-1]
                    soldier = self.metadict_soldiers[uuid]
                    if soldier.defeat\
                            and not soldier.__dict__.get('mechanism')\
                            and not soldier.__dict__.get('killer_mark')\
                            or soldier.death\
                            or soldier.hitpoints < -(soldier.hitpoints_max)\
                            or soldier.death and soldier.__dict__.get('mechanism')\
                            or soldier.defeat and soldier.__dict__.get('mechanism_construct')\
                            or uuid_for_clear == soldier.uuid:
                        content.remove(el)
                        #soldier.place = None
                        #if 'fall_place' in content and soldier.ally_side in content:
                        #    content.remove('fall_place')
                        #    content.remove(soldier.ally_side)
                    elif soldier.escape and 'exit' in content:
                        content.remove(el)
                        soldier.defeat = True
                        if not namespace.test:
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

    def all_clear_spells(self):
        """Работает таймер заклинаний.
        
        - Отмечаем закончившиеся заклинания.
        """
        for soldier in self.metadict_soldiers.values():
            if soldier.spells_active:
                for spell_uuid, spell in soldier.spells_active.items():
                    if spell.get('effect_timer', 0) > 0:
                        spell['effect_timer'] -= 1
                    if spell.get('concentration_timer', 0) > 0:
                        spell['concentration_timer'] -= 1
            # Создаём список закончившихся заклинаний:
            spells_delite_list = self.create_end_spells_list(soldier.spells_active)
            spells_delite_list.extend(self.create_end_spells_list(soldier.buffs))
            spells_delite_list.extend(self.create_end_spells_list(soldier.debuffs))
            if spells_delite_list:
                for spell_uuid in spells_delite_list:
                    # Концентрация:
                    if soldier.concentration and spell_uuid == soldier.concentration['spell_uuid']:
                        soldier.set_concentration_break(autofail = True)
                    # Бафф:
                    if spell_uuid in [el['spell_uuid'] for el in soldier.buffs.values()]:
                        effect_end = [el['effect'] for el in soldier.buffs.values()
                                if spell_uuid == el['spell_uuid']]
                        spell_dict = soldier.buffs.pop(effect_end[0])
                        #print('NYA', soldier.rank, spell_dict['spell_choice'])
                    # Дебафф:
                    if spell_uuid in [el['spell_uuid'] for el in soldier.debuffs.values()]:
                        effect_end = [el['effect'] for el in soldier.debuffs.values()
                                if spell_uuid == el['spell_uuid']]
                        spell_dict = soldier.debuffs.pop(effect_end[0])
                    # Само заклинание, чтобы не засоряло БД:
                    # ------------------------------------------------------------
                    # TODO: Заодно можно отправлять заклинанию сигнал о завершении:
                    # И снимать так, например, сопротивляемость от Absorb_Elements.
                    # Функция заклинания из словаря, боец под эффектом отсюда.
                    # ------------------------------------------------------------
                    if spell_uuid in soldier.spells_active:
                        spell_dict = soldier.spells_active.pop(spell_uuid)
                        #print('NYA', spell_dict['spell_choice'])

    def create_end_spells_list(self, metadict_spells):
        """Список uuid закончившихся заклинаний.
        
        Закончившимися считаются заклинания:
        - Без таймеров концентрации или эффекта.
        - С нулевым таймером концентрации.
        - С нулевым таймером эффекта.
        - С меткой concentration_break
        """
        spells_delite_list = []
        for spell_dict in metadict_spells.values():
            spell_uuid = spell_dict['spell_uuid']
            if not spell_dict.get('effect_timer'):
                spells_delite_list.append(spell_uuid)
            elif spell_dict.get('concentration') and not spell_dict.get('concentration_timer'):
                spells_delite_list.append(spell_uuid)
            elif spell_dict.get('concentration_break'):
                spells_delite_list.append(spell_uuid)
        return spells_delite_list

    def all_get_buffs(self):
        """Срабатывают заклинания в списке buffs.

        Если в заклинании указано, что оно повторяющееся.
        """
        for soldier in self.metadict_soldiers.values():
            if soldier.buffs:
                for effect, spell_dict in soldier.buffs.items():
                    if spell_dict.get('repeat'):
                        soldier.spells_generator.use_buff(spell_dict['spell_choice'],
                                gen_spell = spell_dict, use_spell = False)

    def release_captures(self, side):
        """Пленные победившей стороны освобождаются после боя.

        - Только если была команда -S --stop (namespace.stop)
        """
        if side:
            for soldier in self.metadict_soldiers.values():
                if soldier.ally_side == side and soldier.captured:
                    soldier.captured = False
                # Раненые получают перевязку:
                if soldier.ally_side == side and not soldier.stable and not soldier.death:
                    soldier.stable = True

    def print_battle_statistics(self, short = False):
        """Вывод статистики после боя. Убитые, раненые по отрядам."""
        # Сортируем отряды по номерам зон:
        squads = OrderedDict(sorted(self.squads.items(),key=lambda x: x[0].zone))
        for key, squad in squads.items():
            casualty = squad.casualty
            # Опыт отряда, это сумма опыта солдат:
            squad.experience = sum([soldier.experience for soldier in squad.metadict_soldiers.values()])
            # Израсходованное солдатами снаряжение:
            if not squad.__dict__.get('drop_items_dict'):
                squad.drop_items_dict = {}
            for soldier in squad.metadict_soldiers.values():
                squad.drop_items_dict = dict(Counter(squad.drop_items_dict)\
                        + Counter(soldier.drop_items_dict))
            # Использованные заклинания:
            if not squad.__dict__.get('drop_spells_dict'):
                squad.drop_spells_dict = {}
            for soldier in squad.metadict_soldiers.values():
                squad.drop_spells_dict = dict(Counter(squad.drop_spells_dict)\
                        + Counter(soldier.drop_spells_dict))
            # Трофеи:
            if not squad.__dict__.get('trophy_items_dict'):
                squad.trophy_items_dict = {}
            for soldier in squad.metadict_soldiers.values():
                squad.trophy_items_dict = dict(Counter(squad.trophy_items_dict)\
                        + Counter(soldier.trophy_items_dict))
            # Травмы солдат:
            if not squad.__dict__.get('traumas_dict'):
                squad.traumas_dict = {}
            for soldier in squad.metadict_soldiers.values():
                if not soldier.death:
                    squad.traumas_dict = dict(Counter(squad.traumas_dict) + Counter(soldier.traumas_dict))
            # Сумма хитпоинтов отряда:
            squad_hitpoints_max = sum([soldier.hitpoints_max for soldier\
                in squad.metadict_soldiers.values()])
            squad_hitpoints_new = sum([soldier.hitpoints for soldier\
                in squad.metadict_soldiers.values()\
                if not soldier.hitpoints <= 0])
            squad_bonus_hitpoints_new = sum([soldier.bonus_hitpoints for soldier\
                in squad.metadict_soldiers.values()])
            dict_dead = {}
            dict_disabled = {}
            dict_capture = {}
            dict_fall = {}
            for soldier in squad.metadict_soldiers.values():
                if soldier.death:
                    if not soldier.rank in dict_dead:
                        dict_dead[soldier.rank] = 1
                    elif soldier.rank in dict_dead:
                        dict_dead[soldier.rank] += 1
                elif soldier.disabled:
                    if not soldier.rank in dict_disabled:
                        dict_disabled[soldier.rank] = 1
                    elif soldier.rank in dict_disabled:
                        dict_disabled[soldier.rank] += 1
                elif soldier.captured:
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
            if hasattr(squad, 'battle_stat'):
                battle_stat = squad.battle_stat
                battle_stat = OrderedDict(sorted(battle_stat.items(),key=lambda x: x))
                # TODO: единички, чтобы не было деления на ноль. Позже подправлю.
                damage_sum = 1
                miss_sum = 1
                hit_sum = 1
                for attack, stat in battle_stat.items():
                    if attack[-1] == 'damage':
                        damage_sum += stat
                    if attack[-1] == 'damage_temp_hp':
                        damage_sum += stat
                    if attack[-1] == 'hit':
                        hit_sum += stat
                    if attack[-1] == 'miss':
                        miss_sum += stat
            if squad.ally_side == self.winner:
                squad_combativity = '●'
            else:
                squad_combativity = '○'
            if short and hasattr(squad, 'battle_stat'):
                print('{0} {1} {2} {3} exp {4} hp {hp}% hit_rate {hr} DPR {dpr}'.format(
                        squad_combativity, squad.ally_side, key.zone, key.type, squad.experience,
                        hp = round((squad_hitpoints_new / squad_hitpoints_max) * 100),
                        # damage_per_hit,
                        # damage_per_round,
                        # hits_per_round,
                        # hit_rate,
                        dmg = damage_sum,
                        dph = round(damage_sum / hit_sum, 1),
                        dpr = round(damage_sum / self.battle_round),
                        hpr = round(hit_sum / self.battle_round),
                        hr = round(hit_sum / (hit_sum + miss_sum), 2),
                        r = self.battle_round
                        ))
            elif short:
                print('{0} {1} {2} {3} exp {4} hp {hp}%'.format(
                        squad_combativity, squad.ally_side, key.zone, key.type, squad.experience,
                        hp = round((squad_hitpoints_new / squad_hitpoints_max) * 100),
                        ))
            else:
                print('--------------------------------------------------------------------------------')
                #print('{0} {1} {2} exp {3} hp {4}/{5} (dead {6}% disabled {7}% captured {8}%) fall {9}%, injured {10}%, light {11}%, escape {12}% lucky {13}%'.format(
                print('{0} {1} {2} {3} exp {4} hp {5}/{6} (temp_hp {n}/{b}) (dead {7}% disabled {8}% captured {9}%) fall {10}%, injured {11}%, light {12}%, escape {13}% lucky {14}%'.format(
                        squad_combativity, squad.ally_side, key.zone, key.type, squad.experience,
                        squad_hitpoints_new, squad_hitpoints_max,
                        casualty['dead_percent'], casualty['disabled_percent'],
                        casualty['captured_percent'], casualty['fall_percent'],
                        casualty['injured_percent'], casualty['light_injured_percent'],
                        casualty['escape_percent'], casualty['lucky_one_percent'],
                        b = squad.bonus_hitpoints_max,
                        n = squad_bonus_hitpoints_new,
                        ))
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
                    print('damage_sum:', damage_sum,
                            'damage_per_hit:', round(damage_sum / hit_sum, 1),
                            'hits_per_round:', round(hit_sum / self.battle_round),
                            'hit_per_attack:', round(hit_sum / (hit_sum + miss_sum), 2),
                            'damage_per_round:', round(damage_sum / self.battle_round))
                # Потерянное снаряжение и трофеи:
                if squad.trophy_items_dict and casualty['lucky_one_percent'] > casualty['escape_percent']:
                    squad.trophy_items_dict = dict(OrderedDict(reversed(sorted(
                        squad.trophy_items_dict.items(),key=lambda x: x[1]
                        ))))
                    print('trophy:', squad.trophy_items_dict)
                if squad.drop_items_dict:
                    squad.drop_items_dict = dict(OrderedDict(reversed(sorted(
                        squad.drop_items_dict.items(),key=lambda x: x[1]
                        ))))
                    print('loss:', squad.drop_items_dict)
                if squad.drop_spells_dict:
                    squad.drop_spells_dict = dict(OrderedDict(reversed(sorted(
                        squad.drop_spells_dict.items(),key=lambda x: x
                        ))))
                    print('spells:', squad.drop_spells_dict)
                if squad.traumas_dict:
                    squad.traumas_dict = dict(OrderedDict(reversed(sorted(
                        squad.traumas_dict.items(),key=lambda x: x[1]
                        ))))
                    print('traumas:', squad.traumas_dict)

    def save_soldiers_to_database(self):
        """Сохраняем солдат в базу данных."""
        # TODO: добавь запрос на "y", прежде чем сохранять.
        squads_list_DB = self.database.print_squads()
        for squad in self.squads.values():
            if squad.name in squads_list_DB:
                string_number = input('---Сохраняем исход боя? (y/n)')
                if string_number and string_number == 'y':
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
        spawn_zones_dict = self.spawn_zones_dict
        spawn_zones_list = list(spawn_zones_dict.keys())
        squads_list = list(sorted(squads.metadict_squads.keys()))
        # Пополняем список отрядами из базы данных:
        print('Database [{n}]: {squads}'.format(
            n = len(self.database.print_squads()),
            squads = self.database.print_squads(),
            ))
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
    if not namespace.test:
        battle.prepare_battlefield(selected_map, zones_squads_dict)
        try:
            battle.start(max_rounds = namespace.rounds, commands = namespace.commands)
            # Смотрим сколько народу пострадало:
            battle.print_battle_statistics()
            # Сохраняем отряды в БД:
            if namespace.save:
                battle.save_soldiers_to_database()
        except KeyboardInterrupt:
            #traceback.print_exc()
            battle.print_battle_statistics()
    elif namespace.test:
        winners_list = []
        for test in range(0, namespace.test):
            battle.prepare_battlefield(selected_map, zones_squads_dict)
            try:
                start = timeit.default_timer()
                battle.start(max_rounds = namespace.rounds, commands = namespace.commands)
                stop = timeit.default_timer()
                # TODO: сделай временное сохранение отрядов BLUEFOR, чтобы испытывать в длительных боях:
                # Смотрим сколько народу пострадало:
                print('------------------------------------------------------------')
                print('№', test, 'rounds:', battle.battle_round, 'time:', round(stop - start, 3))
                battle.print_battle_statistics(short = True)
                winners_list.append(battle.winner)
                battle.winner = None
                # Сохраняем отряды в БД:
                if namespace.save:
                    battle.save_soldiers_to_database()
            except KeyboardInterrupt:
                #traceback.print_exc()
                battle.print_battle_statistics(short = True)
                winners_dict = dict(Counter(winners_list))
                for key, stat in winners_dict.items():
                    print(key, round(stat / sum(winners_dict.values()), 2))
        #print(Counter(winners_list))
        winners_dict = dict(Counter(winners_list))
        for key, stat in winners_dict.items():
            print(key, round(stat / sum(winners_dict.values()), 2))
