#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import pickle
import os

#-------------------------------------------------------------------------
# Функции:

def correct_path (database_path_partial):
    """Возвращает абсолютный путь к базе данных."""
    # Получаем абсолютный путь к каталогу скрипта:
    script_path = os.path.dirname(os.path.abspath(__file__))
    database_path_full = script_path + '/' + database_path_partial
    return database_path_full

#-------------------------------------------------------------------------
# Классы:

class database():
    """Переносит параметры солдат в базу данных."""
    database_path = 'dnd_army.sqlite'
    database_path = correct_path(database_path)
    database = sqlite3.connect(database_path)
    cursor = database.cursor()

    def __init__(self):
        """Создаём бд, если её нет."""
        self.create_soldiers_table()
        #self.purge_soldiers_table()

    def soldier_to_database(self, soldier):
        """Параметры бойца в базу данных.
        
        Не забывай, commit отдельно.
        """
        experience = 0
        victories = 0
        defeats = 0
        death = 0
        disabled = 0
        captured = 0
        side = None
        ally_side = None
        enemy_side = None
        # TODO: сброс параметров лучше сделать методом в классе soldier_fight.
        # Можно этот метод прямо здесь и вызвать.
        # Сбрасываем параметры:
        soldier.escape = False
        soldier.grappled = False
        soldier.concentration = False
        soldier.hex = False
        #soldier.ally_side = None
        #soldier.enemy_side = None
        soldier.initiative = None
        soldier.place = None
        soldier.place_in_order = None
        soldier.danger = 0
        soldier.buffs = {}
        soldier.debuffs = {}
        soldier.recon_near = []
        soldier.near_zone = []
        soldier.near_allies = []
        soldier.near_enemies = []
        soldier.enemy_fear = None
        soldier.enemy_grappler = None
        # Сбрасываем параметры человеческой формы друида, но сохраняем её:
        if soldier.__dict__.get('wild_shape_old_form'):
            soldier.wild_shape_old_form['escape'] = False
            soldier.wild_shape_old_form['grappled'] = False
            soldier.wild_shape_old_form['ally_side'] = None
            soldier.wild_shape_old_form['enemy_side'] = None
            soldier.wild_shape_old_form['initiative'] = None
            soldier.wild_shape_old_form['place'] = None
            soldier.wild_shape_old_form['place_in_order'] = None
            soldier.wild_shape_old_form['danger'] = 0
            soldier.wild_shape_old_form['recon_near'] = []
            soldier.wild_shape_old_form['near_zone'] = []
            soldier.wild_shape_old_form['near_allies'] = []
            soldier.wild_shape_old_form['near_enemies'] = []
            soldier.wild_shape_old_form['enemy_fear'] = None
            soldier.wild_shape_old_form['enemy_grappler'] = None
        # Все раненые в конце боя считаются стабилизированными:
        if soldier.hitpoints <= 0 and not soldier.death and not soldier.stable:
            soldier.death_save_success = 0
            soldier.death_save_loss = 0
            soldier.stable = True
        #for key, el in soldier.__dict__.items():
        #    print(key, el)
        soldier_dict_pickle = pickle.dumps(soldier.__dict__)
        # TODO: избавься от этих hasattr:
        if hasattr(soldier, 'ally_side'):
            side = soldier.ally_side
        if hasattr(soldier, 'experience'):
            experience = soldier.experience
        if hasattr(soldier, 'victories'):
            victories = soldier.victories
        if hasattr(soldier, 'defeats'):
            defeats = soldier.defeats
        if hasattr(soldier, 'death') and soldier.death:
            death = 1
        if hasattr(soldier, 'disabled') and soldier.disabled:
            disabled = 1
        if hasattr(soldier, 'captured') and soldier.captured:
            captured = 1
        if hasattr(soldier, 'hitpoints'):
            hitpoints = soldier.hitpoints
        else:
            hitpoints = soldier.hitpoints_max
        if hasattr(soldier, 'hitpoints_heal'):
            hitpoints_heal = soldier.hitpoints_heal
        else:
            hitpoints_heal = 0
        soldier_name = ' '.join(soldier.name)
        soldier_name_translate = ' '.join(soldier.name_translate)
        squad_name = ' '.join(soldier.squad_name)
        self.cursor.execute("INSERT OR REPLACE INTO soldiers VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", [\
            str(soldier.uuid),\
            side,\
            squad_name,\
            soldier.rank,\
            experience,\
            victories,\
            defeats,\
            death,\
            disabled,\
            captured,\
            soldier_name,\
            soldier_name_translate,\
            hitpoints,\
            soldier.hitpoints_max,\
            hitpoints_heal,\
            soldier.abilityes['strength'],\
            soldier.abilityes['dexterity'],\
            soldier.abilityes['constitution'],\
            soldier.abilityes['intelligence'],\
            soldier.abilityes['wisdom'],\
            soldier.abilityes['charisma'],\
            soldier_dict_pickle
            ])
        #self.database.commit()

    def commit(self):
        self.database.commit()

    def soldier_from_database(self, uuid_string):
        """Берём из базы данных параметры бойца. По его uuid в строчном представлении.
        
        При этом распаковываем словарь в pickle и обновляем его.
        """
        sql_query = "SELECT * FROM soldiers WHERE id='{uuid}'".format(uuid=uuid_string)
        soldier_raw = self.cursor.execute(sql_query).fetchall()[0]
        soldier_dict = pickle.loads(soldier_raw[-1])
        # Синхронизируем таблицу и словарь бойца (если правили БД):
        soldier_experience = int(soldier_raw[4])
        soldier_death = int(soldier_raw[7])
        soldier_disabled = int(soldier_raw[8])
        soldier_captured = int(soldier_raw[9])
        soldier_hitpoints = int(soldier_raw[12])
        soldier_hitpoints_max = int(soldier_raw[13])
        soldier_hitpoints_heal = int(soldier_raw[14])
        squad_name = [str(soldier_raw[2])]
        # TODO: это лучше не править. Сторона задаётся в бою.
        #side = str(soldier_raw[1])
        #soldier_dict['ally_side'] = side
        #soldier_dict['enemy_side'] = None
        if soldier_experience:
            soldier_dict['experience'] = soldier_experience
        if soldier_death:
            soldier_dict['death'] = True
        else:
            soldier_dict['death'] = False
        if soldier_disabled:
            soldier_dict['disabled'] = True
        else:
            soldier_dict['disabled'] = False
        if soldier_captured:
            soldier_dict['captured'] = True
        else:
            soldier_dict['captured'] = False
        soldier_dict['squad_name'] = squad_name
        soldier_dict['hitpoints'] = soldier_hitpoints
        soldier_dict['hitpoints_max'] = soldier_hitpoints_max
        soldier_dict['hitpoints_heal'] = soldier_hitpoints_heal
        if soldier_hitpoints > 0:
            soldier_dict['fall'] = False
        return soldier_dict

    def purge_soldiers_table(self):
        """Пересоздаём таблицы"""
        self.cursor.execute("DROP TABLE IF EXISTS soldiers")
        self.database.commit()
    
    def create_soldiers_table (self):
        """Создаёт базу данных солдат."""
        # Сначала проверяем, нет ли таблицы:
        sql_query = """SELECT name FROM sqlite_master WHERE type='table' AND name='soldiers'"""
        if not self.cursor.execute(sql_query).fetchall():
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS soldiers (
                id TEXT NOT NULL PRIMARY KEY UNIQUE,
                side TEXT DEFAULT NULL,
                squad_name TEXT DEFAULT NULL,
                rank TEXT DEFAULT NULL,
                experience INTEGER DEFAULT 0,
                victories INTEGER DEFAULT 0,
                defeats INTEGER DEFAULT 0,
                death INTEGER DEFAULT 0,
                disabled INTEGER DEFAULT 0,
                captured INTEGER DEFAULT 0,
                name TEXT DEFAULT NULL,
                name_translate TEXT DEFAULT NULL,
                hitpoints INTEGER DEFAULT NULL,
                hitpoints_max INTEGER DEFAULT NULL,
                hitpoints_heal INTEGER DEFAULT NULL,
                strength INTEGER DEFAULT NULL,
                dexterity INTEGER DEFAULT NULL,
                constitution INTEGER DEFAULT NULL,
                intelligence INTEGER DEFAULT NULL,
                wisdom INTEGER DEFAULT NULL,
                charisma INTEGER DEFAULT NULL,
                soldier_dict BLOB DEFAULT NULL
                )""")
            self.cursor.execute("""CREATE INDEX IF NOT EXISTS index_soldiers ON soldiers (
                id,
                side,
                squad_name,
                rank,
                experience,
                victories,
                defeats,
                death,
                disabled,
                captured,
                name,
                name_translate,
                hitpoints,
                hitpoints_max,
                hitpoints_heal,
                strength,
                dexterity,
                constitution,
                intelligence,
                wisdom,
                charisma,
                soldier_dict
                )""")
            print("[OK] CREATE:",self.database_path)
        #else:
        #    print("[OK] EXIST:",self.database_path)

    def print_squads(self):
        """Названия отрядов в базе данных."""
        sql_query = "SELECT squad_name FROM soldiers"
        squads_list = self.cursor.execute(sql_query).fetchall()
        squads_list = [el[0] for el in set(squads_list)]
        squads_list = list(sorted(squads_list))
        return squads_list

    def print_squad_soldiers(self, squad_name):
        """Список uuid бойцов по имени отряда."""
        sql_query = "SELECT id FROM soldiers WHERE squad_name='{n}'".format(n=squad_name)
        soldiers_uuid_list = self.cursor.execute(sql_query).fetchall()
        soldiers_uuid_list = [el[0] for el in set(soldiers_uuid_list)]
        return soldiers_uuid_list
