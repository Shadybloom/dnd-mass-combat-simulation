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
        victories = 0
        defeats = 0
        death = 0
        disabled = 0
        captured = 0
        # TODO: сброс параметров лучше сделать методом в классе soldier_fight.
        # Можно этот метод прямо здесь и вызвать.
        # Сбрасываем параметры:
        soldier.escape = False
        soldier.grappled = False
        soldier.ally_side = None
        soldier.enemy_side = None
        soldier.initiative = None
        soldier.place = None
        soldier.place_in_order = None
        soldier.danger = 0
        soldier.near_zone = []
        soldier.near_allies = []
        soldier.near_enemies = []
        soldier.enemy_grappler = None
        # Все раненые в конце боя считаются стабилизированными:
        if soldier.hitpoints <= 0 and not soldier.death and not soldier.stable:
            soldier.death_save_success = 0
            soldier.death_save_loss = 0
            soldier.stable = True
        #for key, el in soldier.__dict__.items():
        #    print(key, el)
        soldier_dict_pickle = pickle.dumps(soldier.__dict__)
        # TODO: избавься от этих hasattr:
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
        self.cursor.execute("INSERT OR REPLACE INTO soldiers VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", [\
            str(soldier.uuid),\
            squad_name,\
            soldier.rank,\
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
        # TODO: здесь нужно синхронизировать таблицы БД и словарь бойца (который в pickle).
        # Обновляй галочки на death и disabled; числа hitpoints, hitpoints_max, hitpoints_heal.
        sql_query = "SELECT * FROM soldiers WHERE id='{uuid}'".format(uuid=uuid_string)
        soldier_raw = self.cursor.execute(sql_query).fetchall()[0]
        soldier_dict = pickle.loads(soldier_raw[-1])
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
                squad_name TEXT DEFAULT NULL,
                rank TEXT DEFAULT NULL,
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
                squad_name,
                rank,
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
        return squads_list

    def print_squad_soldiers(self, squad_name):
        """Список uuid бойцов по имени отряда."""
        sql_query = "SELECT id FROM soldiers WHERE squad_name='{n}'".format(n=squad_name)
        soldiers_uuid_list = self.cursor.execute(sql_query).fetchall()
        soldiers_uuid_list = [el[0] for el in set(soldiers_uuid_list)]
        return soldiers_uuid_list
