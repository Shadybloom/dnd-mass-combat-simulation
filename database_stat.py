#!/usr/bin/env python
# -*- coding: utf-8 -*-

from data import database
from squad_generation import *

from collections import Counter

#-------------------------------------------------------------------------
# Аргументы командной строки:

class database_stat():
    """Описание класса.
    
    """
    database = database.database()
    # Опыт от показателя опасности:
    challenge_rating_experience_dict = {
            '-':10,
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

    def print_squads_names(self):
        """Имена отрядов из базы данных."""
        print('Database [{n}]: {squads}'.format(
            n = len(self.database.print_squads()),
            squads = self.database.print_squads(),
            ))

    def test_squads(self):
        """Данные по отрядам из БД.
        
        """
        metadict_squads_stat = {}
        #trophy_dict = {}
        # TODO: Сохраняй это в словаре (что уже сделано). А вывод потом.
        # Ключи словаря -- кортежи (bluefor, squad_name)
        print('[1/1 -- командиры] [100/100 -- боеспособные] [c:0 -- пленные] [i:0 -- калеки] [d:0 -- погибшие]')
        print('--------------------------------------------------------------------------------')
        for squad_name in self.database.print_squads():
            squad = squad_generation()
            squad.load_squad_from_DB(squad_name, get_all = True)
            for soldier in squad.metadict_soldiers.values():
                soldier.set_actions_base(squad)
            squad.victories = sum([soldier.__dict__.get('victories',0) for soldier\
                in squad.metadict_soldiers.values()])
            squad.experience = sum([soldier.__dict__.get('experience',0) for soldier\
                in squad.metadict_soldiers.values()])
            squad.hitpoints_max = sum([soldier.hitpoints_max for soldier\
                in squad.metadict_soldiers.values()])
            squad.hitpoints_new = sum([soldier.hitpoints for soldier\
                in squad.metadict_soldiers.values()\
                if not soldier.hitpoints <= 0])
            squad.soldiers_number = len([soldier for soldier\
                in squad.metadict_soldiers.values()\
                if not soldier.behavior == 'mount'
                and not soldier.__dict__.get('mechanism')])
            squad.soldiers_number_ready = len([soldier for soldier\
                in squad.metadict_soldiers.values()\
                if soldier.hitpoints >= soldier.hitpoints_max / 2\
                and not soldier.__dict__.get('mechanism')\
                and not soldier.behavior == 'mount'])
            squad.commanders_number = len([soldier for soldier\
                in squad.metadict_soldiers.values()\
                if soldier.behavior == 'commander'
                and not soldier.__dict__.get('mechanism')])
            squad.commanders_number_ready = len([soldier for soldier\
                in squad.metadict_soldiers.values()\
                if soldier.behavior == 'commander'
                and soldier.hitpoints >= soldier.hitpoints_max / 3
                and not soldier.__dict__.get('mechanism')])
            dict_dead = {}
            dict_disabled = {}
            dict_capture = {}
            dict_fall = {}
            # Стоимость пополнения, по стоимости снаряжения:
            squad.reinforce_cost = 0
            # Стоимость трофеев и потерянного снаряжения:
            squad.trophy_cost = 0
            squad.drop_items_cost = 0
            squad.drop_ammo_cost = 0
            # Словари трофеев и потерянного снаряжения:
            squad.trophy_dict = {}
            squad.drop_items_dict = {}
            for soldier in squad.metadict_soldiers.values():
                squad.trophy_dict = dict(Counter(squad.trophy_dict)\
                        + Counter(soldier.trophy_items_dict))
                squad.drop_items_dict = dict(Counter(squad.drop_items_dict)\
                        + Counter(soldier.drop_items_dict))
                if hasattr(soldier, 'death') and soldier.death == True\
                        and not soldier.behavior == 'mount':
                    if not soldier.rank in dict_dead:
                        dict_dead[soldier.rank] = 1
                    elif soldier.rank in dict_dead:
                        dict_dead[soldier.rank] += 1
                    squad.reinforce_cost += soldier.unit_cost['equipment_cost']
                    #trophy_cost += soldier.unit_cost['equipment_cost']
                    #trophy_dict = dict(Counter(trophy_dict) + Counter(soldier.equipment_weapon))
                elif hasattr(soldier, 'disabled') and soldier.disabled == True\
                        and not soldier.behavior == 'mount':
                    if not soldier.rank in dict_disabled:
                        dict_disabled[soldier.rank] = 1
                    elif soldier.rank in dict_disabled:
                        dict_disabled[soldier.rank] += 1
                    # Стоимость лечения у жрецов -- 10 эфесов/100 солдат
                    squad.reinforce_cost += 0.1
                elif hasattr(soldier, 'captured') and soldier.captured == True\
                        and not soldier.behavior == 'mount':
                    if not soldier.rank in dict_capture:
                        dict_capture[soldier.rank] = 1
                    elif soldier.rank in dict_capture:
                        dict_capture[soldier.rank] += 1
                    #trophy_cost += soldier.unit_cost['equipment_cost']
                    #trophy_dict = dict(Counter(trophy_dict) + Counter(soldier.equipment_weapon))
                elif soldier.hitpoints <= 0:
                    if not soldier.rank in dict_fall:
                        dict_fall[soldier.rank] = 1
                    elif soldier.rank in dict_fall:
                        dict_fall[soldier.rank] += 1
            dict_dead = OrderedDict(reversed(sorted(dict_dead.items(),key=lambda x: x)))
            dict_disabled = OrderedDict(reversed(sorted(dict_disabled.items(),key=lambda x: x)))
            dict_capture = OrderedDict(reversed(sorted(dict_capture.items(),key=lambda x: x)))
            dict_fall = OrderedDict(reversed(sorted(dict_fall.items(),key=lambda x: x)))
            # Словарь израсходованной аммуниции (кроме рун):
            squad.drop_ammo_dict = {}
            for item, number in squad.drop_items_dict.items():
                if item in soldier.metadict_items:
                    if soldier.metadict_items[item].get('ammo') == True\
                            or soldier.metadict_items[item].get('weapon') == True\
                            or soldier.metadict_items[item].get('shield') == True\
                            or soldier.metadict_items[item].get('armor') == True:
                        squad.drop_ammo_dict[item] = number
            # Стоимость трофеев и потерянного снаряжения:
            squad.trophy_cost = round(calculate_equipment_cost(squad.trophy_dict,
                soldier.metadict_items))
            squad.drop_items_cost = round(calculate_equipment_cost(squad.drop_items_dict,
                soldier.metadict_items))
            squad.drop_ammo_cost = round(calculate_equipment_cost(squad.drop_ammo_dict,
                soldier.metadict_items))
            squad.reinforce_cost = round(squad.reinforce_cost)
            # Боеспособность отряда:
            if squad.soldiers_number_ready >= squad.soldiers_number / 2\
                    and squad.commanders_number_ready >= 1:
                squad_combativity = '●'
            else:
                squad_combativity = '○'
            #print('{s} [{c}/{c_max}] [{n:>3}/{n_max:<3}] [capt:{cap:<2}] [dead:{dead:<2}] [dis:{dis:<2}] {name}'.format(
            print('{s} [{c}/{c_max}] [{n:>3}/{n_max:<3}] [c:{cap:<2}] [i:{dis:<2}] [d:{dead:<2}] {name} (exp {exp})'.format(
            #print('{s} [{c}/{c_max}] [{n:>3}/{n_max:<3}] [v:{vic:<2}] [c:{cap:<2}] [i:{dis:<2}] [d:{dead:<2}] {name}'.format(
            #print('{s} [{c}/{c_max}] [{n:>3}/{n_max:<3}] [c:{cap:<2}] [d:{dead:<2}] [r:{re:<2}] {name}'.format(
                    s = squad_combativity,
                    n = squad.soldiers_number_ready,
                    n_max = squad.soldiers_number,
                    c = squad.commanders_number_ready,
                    c_max = squad.commanders_number,
                    name = squad.name,
                    hp = squad.hitpoints_new,
                    hp_max = squad.hitpoints_max,
                    vic = squad.victories,
                    re = round(squad.reinforce_cost),
                    exp = round(squad.experience),
                    #trophy = round(trophy_cost),
                    dead = sum(dict_dead.values()),
                    dis = sum(dict_disabled.values()),
                    cap = sum(dict_capture.values()),
                    fall = sum(dict_fall.values()),
                    ))
            print('--------------------------------------------------------------------------------')
            print('* Восполнение потерь (солдат): {re} эфес'.format(re = squad.reinforce_cost))
            print('* Восполнение потерь (снаряжения): {ammo} эфес'.format(ammo = squad.drop_ammo_cost))
            print('* Трофеи солдат: {trophy} эфес'.format(trophy = squad.trophy_cost))
            for key, el in dict_dead.items():
                print('dead', el, key)
            for key, el in dict_disabled.items():
                print('disabled', el, key)
            for key, el in dict_capture.items():
                print('captured', el, key)
            #for key, el in dict_fall.items():
            #    print('fall', el, key)
            metadict_squads_stat[squad_name] = squad
            print('Потери:', squad.drop_ammo_dict)
            print('Трофеи:', squad.trophy_dict)
            print('--------------------------------------------------------------------------------')
        # Список трофеев:
        #for key, value in trophy_dict.items():
        #    print(key, value)
        return metadict_squads_stat

if __name__ == '__main__':
    stat = database_stat()
    stat.test_squads()
