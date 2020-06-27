#!/usr/bin/env python
# -*- coding: utf-8 -*-

from data import database
from squad_generation import *

#-------------------------------------------------------------------------
# Аргументы командной строки:

class database_stat():
    """Описание класса.
    
    """
    database = database.database()
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

    def print_squads_names(self):
        """Имена отрядов из базы данных."""
        print('Database [{n}]: {squads}'.format(
            n = len(self.database.print_squads()),
            squads = self.database.print_squads(),
            ))

    def test_squads(self):
        """Данные по отрядам из БД.
        
        """
        for squad_name in self.database.print_squads():
            squad = squad_generation()
            squad.load_squad_from_DB(squad_name, get_all = True)
            squad_victories = sum([soldier.__dict__.get('victories',0) for soldier\
                in squad.metadict_soldiers.values()])
            squad_hitpoints_max = sum([soldier.hitpoints_max for soldier\
                in squad.metadict_soldiers.values()])
            squad_hitpoints_new = sum([soldier.hitpoints for soldier\
                in squad.metadict_soldiers.values()\
                if not soldier.hitpoints <= 0])
            all_soldiers = len([soldier for soldier\
                in squad.metadict_soldiers.values()\
                if not soldier.behavior == 'mount'])
            ready_soldiers = len([soldier for soldier\
                in squad.metadict_soldiers.values()\
                if soldier.hitpoints >= soldier.hitpoints_max / 2\
                and not soldier.behavior == 'mount'])
            commanders = len([soldier for soldier\
                in squad.metadict_soldiers.values()\
                if soldier.behavior == 'commander'])
            ready_commanders = len([soldier for soldier\
                in squad.metadict_soldiers.values()\
                if soldier.behavior == 'commander'
                and soldier.hitpoints >= soldier.hitpoints_max / 3])
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
            if ready_soldiers >= all_soldiers / 2 and ready_commanders >= 1:
                squad_combativity = '●'
            else:
                squad_combativity = '○'
            #print('{s} [{c}/{c_max}] [{n:>3}/{n_max:<3}] [capt:{cap:<2}] [dead:{dead:<2}] [dis:{dis:<2}] {name}'.format(
            #print('[?/? -- командиры] [??/??? -- боеспособные] [c -- пленные] [d -- убитые]')
            print('{s} [{c}/{c_max}] [{n:>3}/{n_max:<3}] [c:{cap:<2}] [d:{dead:<2}] {name}'.format(
                    s = squad_combativity,
                    n = ready_soldiers,
                    n_max = all_soldiers,
                    c = ready_commanders,
                    c_max = commanders,
                    name = squad.name,
                    hp = squad_hitpoints_new,
                    hp_max = squad_hitpoints_max,
                    dead = sum(dict_dead.values()),
                    dis = sum(dict_disabled.values()),
                    cap = sum(dict_capture.values()),
                    fall = sum(dict_fall.values()),
                    ))
            #for key, el in dict_dead.items():
            #    print('dead', el, key)
            #for key, el in dict_disabled.items():
            #    print('disabled', el, key)
            #for key, el in dict_capture.items():
            #    print('captured', el, key)
            #for key, el in dict_fall.items():
            #    print('fall', el, key)

if __name__ == '__main__':
    stat = database_stat()
    stat.test_squads()
