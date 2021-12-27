#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Загружаем комплекты снаряжения (soldiers_pack)
from data.items import *

#----
# Лишённые индивидуальности заготовки солдат. Используются в squad_generation

metadict_chars = {}

#----
# Сельское ополчение (крестьяне и городская беднота):

metadict_chars['Commoner 1 lvl (recruit)'] = {
    # Отсеиваются из состава отряда на этапе генерации.
    # Отражают отбор в отряд лучших солдат:
        # 100 рекрутов на 100 должностей = 100 раных солдат, 30 из которых негодные.
        # 200 рекрутов на 100 должностей = 100 сильных и ловких солдат.
        # 500 рекрутов на 100 должностей = 100 бойцов уровня ветеранов.
    'level':1,
    'recruit_selection':True,
    'char_class':'Commoner',
    'behavior':'Warrior',
    'hit_dice':'1d8',
    'race':'Human-common',
    'weapon_skill':['simple'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':{},
    'equipment_backpack':{},
    'equipment_weapon':{},
    }

metadict_chars['Commoner 1 lvl (militia javeliner)'] = {
    # Пельтасты, левисы. Ополченцы с метательными копьями.
        # https://ru.wikipedia.org/wiki/Левисы
        # https://ru.wikipedia.org/wiki/Рорарии
    # Таких оборванцев можно набрать по 600 на 6000 сельского населения (регион 6x6 миль).
    'level':1,
    'char_class':'Commoner',
    'behavior':'archer',
    'hit_dice':'1d8',
    'race':'Human-common',
    'weapon_skill':['simple'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':militia_pack,
    'equipment_weapon':{
        'Leather Armor':1,
        'Shield':1,
        'Dagger':1,
        'Javelin':6,
        },
    }

metadict_chars['Commoner 2 lvl (militia javeliner-corporal)'] = {
    # Авторитетный горожанин, или вожак сельского ополчения.
        # Чтобы получить 2 lvl ему нужно 300 xp (12 побед в бою)
        # Броня -- усиленный бронзовыми бляхами линоторакс (его делали из кожи, а не изо льна).
    'level':2,
    'char_class':'Commoner',
    'behavior':'archer',
    'hit_dice':'1d8',
    'race':'Human-common',
    'weapon_skill':['simple'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Studded Leather':1,
        'Shield':1,
        'Mace':1,
        'Javelin':6,
        },
    }

metadict_chars['Warrior 3 lvl (militia javeliner-sergeant)'] = {
    # Обычно это старики-ветераны из профессиональной армии.
    'level':3,
    'char_class':'Warrior',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        #'Fighting_Style_Defence':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Breastplate':1,
        'Heavy Shield':1,
        'Shortsword':1,
        'Javelin':6,
        },
    }

metadict_chars['Warrior 4 lvl (militia javeliner-lieutenant)'] = {
    # Офицеры-отставники.
    'level':4,
    'char_class':'Warrior',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        #'Fighting_Style_Defence':True,
        'Feat_Inspiring_Leader':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Shielding':1,
        'Breastplate':1,
        'Heavy Shield':1,
        'Shortsword':1,
        'Javelin':6,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Commoner 1 lvl (militia slinger)'] = {
    # Акцензы. Пращу используют вместе со щитом.
        # https://ru.wikipedia.org/wiki/Акцензы
        # Снаряды тяжёлые, весят по 1 фунту (450 грамм) (глиняные "жёлуди" или галька)
    'level':1,
    'char_class':'Commoner',
    'behavior':'archer',
    'hit_dice':'1d8',
    'race':'Human-common',
    'weapon_skill':['simple'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':militia_pack,
    'equipment_weapon':{
        'Leather Armor':1,
        'Shield':1,
        'Dagger':1,
        'Sling real':1,
        'Sling Bullet':10,
        },
    }

metadict_chars['Commoner 2 lvl (militia slinger-corporal)'] = {
    'level':2,
    'char_class':'Commoner',
    'behavior':'archer',
    'hit_dice':'1d8',
    'race':'Human-common',
    'weapon_skill':['simple'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Studded Leather':1,
        'Shield':1,
        'Dagger':1,
        'Sling real':1,
        'Sling Bullet':10,
        },
    }

metadict_chars['Warrior 3 lvl (militia slinger-sergeant)'] = {
    'level':3,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        #'Fighting_Style_Archery':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Breastplate':1,
        'Shield':1,
        'Shortsword':1,
        'Sling real':1,
        'Sling Bullet':10,
        },
    }

metadict_chars['Warrior 4 lvl (militia slinger-lieutenant)'] = {
    'level':4,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        #'Fighting_Style_Archery':True,
        'Feat_Sharpshooter':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Shielding':1,
        'Breastplate':1,
        'Shield':1,
        'Shortsword':1,
        'Sling real':1,
        'Sling Bullet':10,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Commoner 1 lvl (militia bowman)'] = {
    # Лучник с коротким луком. Охотник.
        # Примитивный лук (1d4 урона) и охотничьи стрелы с кремниевыми наконечниками.
    'level':1,
    'char_class':'Commoner',
    'behavior':'archer',
    'hit_dice':'1d8',
    'race':'Human-common',
    'weapon_skill':['simple'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':militia_pack,
    'equipment_weapon':{
        'Leather Armor':1,
        'Dagger':1,
        'Hunting Bow':1,
        'Hunting Arrow':40,
        },
    }

metadict_chars['Commoner 2 lvl (militia bowman-corporal)'] = {
    'level':2,
    'char_class':'Commoner',
    'behavior':'archer',
    'hit_dice':'1d8',
    'race':'Human-common',
    'weapon_skill':['simple'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Studded Leather':1,
        'Shield':1,
        'Dagger':1,
        'Hunting Bow':1,
        'Hunting Arrow':40,
        },
    }

metadict_chars['Warrior 3 lvl (militia bowman-sergeant)'] = {
    'level':3,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        #'Fighting_Style_Archery':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Breastplate':1,
        'Shield':1,
        'Shortsword':1,
        'Shortbow':1,
        'Arrow':40,
        },
    }

metadict_chars['Warrior 4 lvl (militia bowman-lieutenant)'] = {
    # Лучший стрелок. Командует бойцами, направляя град стрел.
    # Азимут такой-то, угол стрельбы такой-то. Всё на личном примере.
    'level':4,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        #'Fighting_Style_Archery':True,
        'Feat_Sharpshooter':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Breastplate':1,
        'Shield':1,
        'Shortsword':1,
        'Shortbow':1,
        'Arrow':40,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{},
    }

metadict_chars['Commoner 1 lvl (militia spearman)'] = {
    # Типичный гастат ранней республики, ибо легион значит "ополчение".
        # https://ru.wikipedia.org/wiki/Гастаты
    'level':1,
    'char_class':'Commoner',
    'behavior':'warrior',
    'hit_dice':'1d8',
    'race':'Human-common',
    'weapon_skill':['simple'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':militia_pack,
    'equipment_weapon':{
        'Leather Armor':1,
        'Heavy Shield':1,
        'Spear':1,
        'Pilum':2,
        },
    }

metadict_chars['Commoner 2 lvl (militia spearman-corporal)'] = {
    # Принцип ранней республики.
    'level':2,
    'char_class':'Commoner',
    'behavior':'warrior',
    'hit_dice':'1d8',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Studded Leather':1,
        'Heavy Shield':1,
        'Spear':1,
        'Pilum':2,
        },
    }

metadict_chars['Warrior 3 lvl (militia spearman-sergeant)'] = {
    'level':3,
    'close_order_AI':True,
    'char_class':'Warrior',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        #'Fighting_Style_Defence':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Breastplate':1,
        'Heavy Shield':1,
        'Shortsword':1,
        'Pilum':4,
        },
    }

metadict_chars['Warrior 4 lvl (militia spearman-lieutenant)'] = {
    'level':4,
    'close_order_AI':True,
    'char_class':'Warrior-officer',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        #'Fighting_Style_Defence':True,
        'Feat_Inspiring_Leader':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Shielding':1,
        'Breastplate':1,
        'Heavy Shield':1,
        'Shortsword':1,
        'Pilum':4,
        },
    'mount_combat':False,
    'mount_type':'Riding Horse',
    'equipment_mount':{
        },
    }

metadict_chars['Commoner 1 lvl (militia swordsman)'] = {
    # Кельты, галлы.
    'level':1,
    'char_class':'Commoner',
    'behavior':'warrior',
    'hit_dice':'1d8',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':militia_pack,
    'equipment_weapon':{
        'Hide Armor':1,
        'Shield':1,
        'Shortsword':1,
        'Javelin':2,
        #'Potion of Heroism':1,
        #'Potion of Bravery':1,
        #'Potion of Rage':1,
        },
    }

metadict_chars['Commoner 2 lvl (militia swordsman-corporal)'] = {
    'level':2,
    'char_class':'Commoner',
    'behavior':'warrior',
    'hit_dice':'1d8',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Hide Armor':1,
        'Heavy Shield':1,
        'Shortsword':1,
        #'Javelin':2,
        },
    }

metadict_chars['Warrior 3 lvl (militia swordsman-sergeant)'] = {
    'level':3,
    'close_order_AI':True,
    'char_class':'Warrior',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        #'Fighting_Style_Dueling':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':2,
        'Scale Mail':1,
        'Heavy Shield':1,
        'Longsword':1,
        #'Javelin':6,
        },
    }

metadict_chars['Warrior 4 lvl (militia swordsman-lieutenant)'] = {
    'level':4,
    'close_order_AI':True,
    'char_class':'Warrior-officer',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        #'Fighting_Style_Dueling':True,
        'Feat_Inspiring_Leader':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':3,
        'Half Plate':1,
        'Heavy Shield':1,
        'Longsword':1,
        'Javelin':6,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Commoner 1 lvl (militia crossbowman)'] = {
    # Арбалетчики Гастрафеты.
    'level':1,
    'char_class':'Commoner',
    'behavior':'archer',
    'hit_dice':'1d8',
    'race':'Human-common',
    'weapon_skill':['simple'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':militia_pack,
    'equipment_weapon':{
        'Padded Armor':1,
        'Dagger':1,
        'Crossbow, Light':1,
        'Crossbow Bolt':40,
        },
    }

metadict_chars['Commoner 2 lvl (militia crossbowman-corporal)'] = {
    'level':2,
    'char_class':'Commoner',
    'behavior':'archer',
    'hit_dice':'1d8',
    'race':'Human-common',
    'weapon_skill':['simple'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Studded Leather':1,
        'Shield':1,
        'Dagger':1,
        'Crossbow, Light':1,
        'Crossbow Bolt':40,
        },
    }

metadict_chars['Warrior 3 lvl (militia crossbowman-sergeant)'] = {
    'level':3,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        #'Fighting_Style_Archery':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Breastplate':1,
        'Shield':1,
        'Shortsword':1,
        'Crossbow, Light':1,
        'Crossbow Bolt':40,
        },
    }

metadict_chars['Warrior 4 lvl (militia crossbowman-lieutenant)'] = {
    # Лучший стрелок. Командует бойцами, направляя град стрел.
    # Азимут такой-то, угол стрельбы такой-то. Всё на личном примере.
    'level':4,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        #'Fighting_Style_Archery':True,
        'Feat_Sharpshooter':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Breastplate':1,
        'Shield':1,
        'Shortsword':1,
        'Crossbow, Light':1,
        'Crossbow Bolt':40,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{},
    }

metadict_chars['Commoner 1 lvl (militia heavy crossbowman)'] = {
    # Арбалетчики. "Скорпионы"
    'level':1,
    'char_class':'Commoner',
    'behavior':'archer',
    'hit_dice':'1d8',
    'race':'Human-common',
    'weapon_skill':['simple'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':militia_pack,
    'equipment_weapon':{
        'Padded Armor':1,
        'Dagger':1,
        'Crossbow, Heavy':1,
        'Crossbow Bolt':40,
        },
    }

metadict_chars['Commoner 2 lvl (militia heavy crossbowman-corporal)'] = {
    'level':2,
    'char_class':'Commoner',
    'behavior':'archer',
    'hit_dice':'1d8',
    'race':'Human-common',
    'weapon_skill':['simple'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Studded Leather':1,
        'Shield':1,
        'Dagger':1,
        'Crossbow, Heavy':1,
        'Crossbow Bolt':40,
        },
    }

metadict_chars['Warrior 3 lvl (militia heavy crossbowman-sergeant)'] = {
    'level':3,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        #'Fighting_Style_Archery':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Breastplate':1,
        'Shield':1,
        'Shortsword':1,
        'Crossbow, Heavy':1,
        'Crossbow Bolt':40,
        },
    }

metadict_chars['Warrior 4 lvl (militia heavy crossbowman-lieutenant)'] = {
    # Лучший стрелок. Командует бойцами, направляя град стрел.
    # Азимут такой-то, угол стрельбы такой-то. Всё на личном примере.
    'level':4,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        #'Fighting_Style_Archery':True,
        'Feat_Sharpshooter':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Breastplate':1,
        'Shield':1,
        'Shortsword':1,
        'Crossbow, Heavy':1,
        'Crossbow Bolt':40,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{},
    }


#----
# Городское ополчение (отборные и неплохо вооружённые гоплиты)
    # TODO: подправь, теперь второй параметр для большинства бойцов, это ловкость.
    # Среднее арифметическое от суммы параметров -- 63 (средние параметры -- 10.5)
    # Распределение силы (главный параметр, на 10 000 выборке):
        # 18 -- 2.5%
        # 16+ -- 22.5%
        # 14+ -- 40%
        # 12+ -- 28.7%
        # 10+ -- 5.8%
        # <10 -- 0.5%
    # Распределение телосложения (второй параметр, на 10 000 выборке):
        # 16+ -- 2.5%
        # 14+ -- 22%
        # 12+ -- 47%
        # 10+ -- 25.7%
        # <10 -- 2.8%
    # Распределение ловкости (третий параметр, на 10 000 выборке):
        # 14+ -- 5%
        # 12+ -- 35%
        # 10+ -- 45%
        # <10 -- 15%
    # Ловкость и средня броня:
        # Только 5% профи могут реализовать +2 AC от ловкости к средней броне.
        # Впрочем, 35% с +1 AC тоже стоит учесть. Scale Mail -- лучшее решение.
    # Сила и переносимый вес (на 10 000 выборке):
        # Сила x 5 = лёгкая нагрузка (50 фунтов, или 25 кг при силе 10)
        # Сила x 10 = перегрузка (100 фунтов, или 50 кг, но при -10 футов к скорости)
        # 95% бойцов (STR 12+) могут нести по 60 фунтов.
        # 85% крестьян (STR 8+) могут нести по 40 фунтов.
        # Кстати, последнее число -- уставная норма для армий 19 века.

metadict_chars['Warrior 1 lvl (achean hoplite)'] = {
    # Городское ополчение. Гоплиты.
        # Таких не больше 1000 на 10 000 городского и 30 000 сельского населения.
        # Копьё -- ~3 метра. Большой щит -- гоплон (апис)
        # Броня -- "линоторакс" с щитком на груди, шлем.
    'level':1,
    'char_class':'Warrior',
    'behavior':'warrior',
    'hit_dice':'1d8',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Studded Leather':1,
        'Heavy Shield':1,
        'Shortsword':1,
        'Long Spear':1,
        'Javelin':5,
        },
    }

metadict_chars['Warrior 2 lvl (achean hoplite-corporal)'] = {
    # "Прослуживший" 10 лет гоплит. Такие нередко уходят в наёмники.
        # Чтобы получить 2 lvl ему нужно 300 xp (12 побед в бою)
        # Броня -- чешуйчатая (бронзовые пластины на кожаной основе)
    'level':2,
    'char_class':'Warrior',
    'behavior':'elite_warrior',
    'hit_dice':'1d8',
    'class_features':{
        # Изначально ветераны не обладают боевым стилем. Этому их обучают герои-бойцы.
        #'Fighting_Style_Protection':True,
        'Fighting_Style_Dueling':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Scale Mail':1,
        'Heavy Shield':1,
        'Shortsword':1,
        'Long Spear':1,
        },
    }

metadict_chars['Warrior 3 lvl (achean hoplite-sergeant)'] = {
    # Состоятельный горожанин и авторитетный командир.
        # Чтобы получит 3 lvl нужно 300+900=1200 exp (24-48 побед в бою)
        # Броня -- бронзовый панцирь, поножи, шлем.
    'level':3,
    'char_class':'Warrior',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        #'Fighting_Style_Protection':True,
        'Fighting_Style_Dueling':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Breastplate':1,
        'Heavy Shield':1,
        'Shortsword':1,
        'Long Spear':1,
        },
    }

metadict_chars['Warrior 4 lvl (achean hoplite-lieutenant)'] = {
    # Командир 30 бойцов.
        # Чтобы получит 4 lvl нужно 300+900+2700 xp (78-156 побед в бою)
    'level':4,
    'char_class':'Warrior-officer',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        #'Fighting_Style_Protection':True,
        'Fighting_Style_Dueling':True,
        'Feat_Inspiring_Leader':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Breastplate':1,
        'Heavy Shield':1,
        'Shortsword':1,
        'Long Spear':1,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Warrior 5 lvl (achean hoplite-captain)'] = {
    # Сотник гоплитов
        # Бронзовый панцирь с рельефом, поножи с набедренниками, закрытый шлем.
        # Чтобы получить 5 lvl нужно 300+900+2700+6500 xp (208-416 побед в бою)
    'level':5,
    'char_class':'Warrior-officer',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        #'Fighting_Style_Protection':True,
        'Fighting_Style_Dueling':True,
        'Feat_Inspiring_Leader':True,
        'Extra_Attack':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Half Plate':1,
        'Heavy Shield':1,
        'Shortsword':1,
        'Long Spear':1,
        },
    'mount_combat':False,
    'mount_type':'Riding Horse',
    'equipment_mount':{
        },
    }

#----
# Городское ополчение (сариссофоры)

metadict_chars['Warrior 1 lvl (city pikeman)'] = {
    # Сила пикионеров -- плотный строй, но это не реализовать.
        # В мире, где летают огнешары, плотное построение фаланги слишком опасно.
        # https://ru.wikipedia.org/wiki/Сариссофор
    'level':1,
    'char_class':'Warrior-heavy',
    'behavior':'warrior',
    'hit_dice':'1d8',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Ring Mail':1,
        'Shortsword':1,
        'Shield':1,
        'Pike':1,
        },
    }

metadict_chars['Warrior 2 lvl (city pikeman-corporal)'] = {
    'level':2,
    'char_class':'Warrior-heavy',
    'behavior':'elite_warrior',
    'hit_dice':'1d8',
    'class_features':{
        'Fighting_Style_Defence':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Chain Mail':1,
        'Shortsword':1,
        'Shield':1,
        'Pike':1,
        },
    }

metadict_chars['Warrior 3 lvl (city pikeman-sergeant)'] = {
    'level':3,
    'char_class':'Warrior-heavy',
    'behavior':'elite_warrior',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Defence':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Chain Mail':1,
        'Shortsword':1,
        'Shield':1,
        'Pike':1,
        },
    }

metadict_chars['Warrior 4 lvl (city pikeman-lieutenant)'] = {
    'level':4,
    'char_class':'Warrior-officer',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Defence':True,
        'Feat_Inspiring_Leader':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Half Plate':1,
        'Shortsword':1,
        'Shield':1,
        'Pike':1,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Warrior 5 lvl (city pikeman-captain)'] = {
    'level':5,
    #'close_order_AI':True,
    'char_class':'Warrior-officer',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Defence':True,
        'Feat_Inspiring_Leader':True,
        'Extra_Attack':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Half Plate':1,
        'Shortsword':1,
        'Shield':1,
        'Pike':1,
        },
    'mount_combat':False,
    'mount_type':'Riding Horse',
    'equipment_mount':{
        },
    }

#----
# Лучники-специалисты.

metadict_chars['Warrior 1 lvl (sqythian bowman)'] = {
    # Персы, скифы, сарматы. Отличные композитные луки, а вместо защиты стёганки.
    'level':1,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'archer',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Padded Armor':1,
        'Dagger':1,
        'Longbow':1,
        'Arrow':40,
        },
    }

metadict_chars['Warrior 2 lvl (sqythian bowman-corporal)'] = {
    'level':2,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'archer',
    'class_features':{
        'Fighting_Style_Archery':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Scale Mail':1,
        'Dagger':1,
        'Longbow':1,
        'Arrow':40,
        },
    }

metadict_chars['Warrior 3 lvl (sqythian bowman-sergeant)'] = {
    'level':3,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Archery':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Breastplate':1,
        'Dagger':1,
        'Longbow':1,
        'Arrow':40,
        },
    }

metadict_chars['Warrior 4 lvl (sqythian bowman-lieutenant)'] = {
    # Лучший стрелок. Командует сотней бойцов, направляя град стрел.
    # Азимут такой-то, угол стрельбы такой-то. Всё на личном примере.
    'level':4,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Archery':True,
        'Feat_Sharpshooter':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Shielding':1,
        'Breastplate':1,
        'Shield':1,
        'Shortsword':1,
        'Longbow':1,
        'Arrow':40,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{},
    }

metadict_chars['Warrior 5 lvl (sqythian bowman-captain)'] = {
    'level':5,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Archery':True,
        'Feat_Sharpshooter':True,
        'Extra_Attack':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Half Plate':1,
        'Shield':1,
        'Shortsword':1,
        'Longbow':1,
        'Arrow':40,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{},
    }


#----
# Лучники-универсалы.

metadict_chars['Warrior 1 lvl (persian bowman)'] = {
    # Кроме луков вооружены акинаками и щитами.
    'level':1,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'archer',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Studded Leather':1,
        'Shield':1,
        'Shortsword':1,
        'Shortbow':1,
        'Arrow':40,
        },
    }

metadict_chars['Warrior 2 lvl (persian bowman-corporal)'] = {
    # Ветераны после 10 лет службы. Мастерски стреляют. Умело сражаются и в ближнем бою.
    'level':2,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'archer',
    'class_features':{
        'Fighting_Style_Archery':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Scale Mail':1,
        'Shield':1,
        'Shortsword':1,
        'Shortbow':1,
        'Arrow':40,
        },
    }

metadict_chars['Warrior 3 lvl (persian bowman-sergeant)'] = {
    'level':3,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Archery':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Breastplate':1,
        'Shield':1,
        'Shortsword':1,
        'Shortbow':1,
        'Arrow':40,
        },
    }

metadict_chars['Warrior 4 lvl (persian bowman-lieutenant)'] = {
    # Лучший стрелок. Командует 30 бойцами, направляя град стрел.
    # Азимут такой-то, угол стрельбы такой-то. Всё на личном примере.
    'level':4,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Archery':True,
        'Feat_Sharpshooter':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Shielding':1,
        'Breastplate':1,
        'Shield':1,
        'Shortsword':1,
        'Shortbow':1,
        'Arrow':40,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{},
    }

metadict_chars['Warrior 5 lvl (persian bowman-captain)'] = {
    # Командир сотни наёмных лучников.
    'level':5,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Archery':True,
        'Feat_Sharpshooter':True,
        'Extra_Attack':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Half Plate':1,
        'Shield':1,
        'Shortsword':1,
        'Shortbow':1,
        'Arrow':40,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{},
    }

#----
# Стрелки с мушкетами, мушкетёры.

metadict_chars['Warrior 1 lvl (musketeer line-infantry)'] = {
    # Вооружены алебардой, шпагой/саблей и мушкетом.
    # Кожаный жилет, перчатки, сапоги.
    'level':1,
    'char_class':'Warrior-pirate',
    'hit_dice':'1d8',
    'behavior':'warrior',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Studded Leather':1,
        'Halberd':1,
        'Shortsword':1,
        'Muskete':1,
        'Muskete Bullet':60,
        },
    }

metadict_chars['Warrior 2 lvl (musketeer line-infantry-corporal)'] = {
    'level':2,
    'char_class':'Warrior-pirate',
    'hit_dice':'1d8',
    'behavior':'elite_warrior',
    'class_features':{
        'Fighting_Style_Archery':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Rune of Shielding':1,
        'Breastplate, 17 century':1,
        'Halberd':1,
        'Rapier':1,
        'Muskete':1,
        'Muskete Bullet':60,
        },
    }

metadict_chars['Warrior 3 lvl (musketeer line-infantry-sergeant)'] = {
    'level':3,
    'firearm_AI':True,
    'char_class':'Warrior-pirate',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Archery':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Shielding':1,
        'Breastplate, 17 century':1,
        'Halberd':1,
        'Rapier':1,
        'Muskete, Lorenzony':1,
        'Muskete Bullet':60,
        },
    }

metadict_chars['Warrior 4 lvl (musketeer line-infantry-lieutenant)'] = {
    'level':4,
    'firearm_AI':True,
    'char_class':'Warrior-pirate',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Archery':True,
        'Feat_Inspiring_Leader':True,
        #'Feat_Martial_Adept':True,
        #'Menacing_Attack':True,
        #'Parry':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Breastplate, 17 century':1,
        'Halberd':1,
        'Rapier':1,
        'Muskete, Lorenzony':1,
        'Muskete Bullet':60,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{},
    }

metadict_chars['Warrior 5 lvl (musketeer line-infantry-captain)'] = {
    # Капитан роты мушкетёров.
    'level':5,
    'firearm_AI':True,
    'char_class':'Warrior-pirate',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Archery':True,
        'Feat_Inspiring_Leader':True,
        #'Feat_Martial_Adept':True,
        #'Menacing_Attack':True,
        #'Parry':True,
        'Extra_Attack':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Breastplate, 17 century':1,
        'Halberd':1,
        'Rapier':1,
        'Muskete, Lorenzony':1,
        'Muskete Bullet':60,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{},
    }

#----
# Метатели гранат, гренадёры.
# https://en.wikipedia.org/wiki/Grenadier

metadict_chars['Warrior 1 lvl (grenadier line-infantry)'] = {
    # Вооружены палашом, щитом, алебардой и сумкой гранат.
    'level':1,
    'char_class':'Warrior-heavy',
    'hit_dice':'1d8',
    'behavior':'warrior',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Studded Leather':1,
        'Halberd':1,
        'Shortsword':1,
        'Shield':1,
        'Pistol':1,
        'Muskete Bullet':30,
        'Hand Grenade':5,
        'Smoke Grenade':1,
        },
    }

metadict_chars['Warrior 2 lvl (grenadier line-infantry-corporal)'] = {
    'level':2,
    'char_class':'Warrior-heavy',
    'hit_dice':'1d8',
    'behavior':'elite_warrior',
    'class_features':{
        'Fighting_Style_Blind_Fighting':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Rune of Shielding':1,
        'Breastplate, 17 century':1,
        'Halberd':1,
        'Shortsword':1,
        'Shield':1,
        'Pistol':1,
        'Muskete Bullet':30,
        'Hand Grenade':5,
        'Smoke Grenade':1,
        },
    }

metadict_chars['Warrior 3 lvl (grenadier line-infantry-sergeant)'] = {
    'level':3,
    'carefull_AI':True,
    'grenadier_AI':True,
    'char_class':'Warrior-heavy',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Blind_Fighting':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Shielding':1,
        'Breastplate, 17 century':1,
        'Halberd':1,
        'Shortsword':1,
        'Shield':1,
        'Pistol, Lorenzony':1,
        'Muskete Bullet':30,
        'Hand Grenade':5,
        'Smoke Grenade':1,
        },
    }

metadict_chars['Warrior 4 lvl (grenadier line-infantry-lieutenant)'] = {
    'level':4,
    'carefull_AI':True,
    'grenadier_AI':True,
    'char_class':'Warrior-officer',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Blind_Fighting':True,
        'Feat_Inspiring_Leader':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Breastplate, 17 century':1,
        'Halberd':1,
        'Shortsword':1,
        'Shield':1,
        'Pistol, Lorenzony':1,
        'Muskete Bullet':30,
        'Hand Grenade':5,
        'Smoke Grenade':1,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{},
    }

metadict_chars['Warrior 5 lvl (grenadier line-infantry-captain)'] = {
    # Капитан роты гренадеров.
    'level':5,
    'carefull_AI':True,
    'grenadier_AI':True,
    'char_class':'Warrior-officer',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Blind_Fighting':True,
        'Feat_Inspiring_Leader':True,
        'Extra_Attack':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Breastplate, 17 century':1,
        'Halberd':1,
        'Shortsword':1,
        'Shield':1,
        'Pistol, Lorenzony':1,
        'Muskete Bullet':30,
        'Hand Grenade':5,
        'Smoke Grenade':1,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{},
    }

#----
# Гренадеры с ручными мортирками

metadict_chars['Warrior 1 lvl (bombardier line-infantry)'] = {
    # Вооружены алебардой и ручной мортиркой.
    'level':1,
    'char_class':'Warrior-heavy',
    'hit_dice':'1d8',
    'behavior':'warrior',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Studded Leather':1,
        'Halberd':1,
        'Pistol':1,
        'Muskete Bullet':30,
        'Hand Mortar':1,
        '2lb Bomb':10,
        'Smoke Grenade':1,
        },
    }

metadict_chars['Warrior 2 lvl (bombardier line-infantry-corporal)'] = {
    'level':2,
    'char_class':'Warrior-heavy',
    'hit_dice':'1d8',
    'behavior':'elite_warrior',
    'class_features':{
        'Fighting_Style_Blind_Fighting':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Rune of Shielding':1,
        'Breastplate, 17 century':1,
        'Halberd':1,
        'Pistol':1,
        'Muskete Bullet':30,
        'Hand Mortar':1,
        '2lb Bomb':10,
        'Smoke Grenade':1,
        },
    }

metadict_chars['Warrior 3 lvl (bombardier line-infantry-sergeant)'] = {
    'level':3,
    'firearm_AI':True,
    'grenadier_AI':True,
    'defence_AI':True,
    'char_class':'Warrior-heavy',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Blind_Fighting':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Shielding':1,
        'Breastplate, 17 century':1,
        'Halberd':1,
        'Pistol, Lorenzony':1,
        'Muskete Bullet':30,
        'Hand Mortar':1,
        '2lb Bomb':10,
        'Smoke Grenade':1,
        },
    }

metadict_chars['Warrior 4 lvl (bombardier line-infantry-lieutenant)'] = {
    'level':4,
    'firearm_AI':True,
    'grenadier_AI':True,
    'defence_AI':True,
    'char_class':'Warrior-officer',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Blind_Fighting':True,
        'Feat_Inspiring_Leader':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Breastplate, 17 century':1,
        'Halberd':1,
        'Pistol, Lorenzony':1,
        'Muskete Bullet':30,
        'Hand Mortar':1,
        '2lb Bomb':10,
        'Smoke Grenade':1,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{},
    }

metadict_chars['Warrior 5 lvl (bombardier line-infantry-captain)'] = {
    # Капитан роты гренадеров.
    'level':5,
    'firearm_AI':True,
    'grenadier_AI':True,
    'defence_AI':True,
    'char_class':'Warrior-officer',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Blind_Fighting':True,
        'Feat_Inspiring_Leader':True,
        'Extra_Attack':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Breastplate, 17 century':1,
        'Halberd':1,
        'Pistol, Lorenzony':1,
        'Muskete Bullet':30,
        'Hand Mortar':1,
        '2lb Bomb':10,
        'Smoke Grenade':1,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{},
    }

#----
# Стрелки с фузилями, фузилёры.
# https://en.wikipedia.org/wiki/Fusilier

metadict_chars['Warrior 1 lvl (fusilier line-infantry)'] = {
    # Вооружены штыком и мушкетом.
    'level':1,
    'char_class':'Warrior-pirate',
    'hit_dice':'1d8',
    'behavior':'archer',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Leather Armor':1,
        'Bayonet':1,
        'Muskete':1,
        'Muskete Bullet':30,
        },
    }

metadict_chars['Warrior 2 lvl (fusilier line-infantry-corporal)'] = {
    'level':2,
    'char_class':'Warrior-pirate',
    'hit_dice':'1d8',
    'behavior':'archer',
    'class_features':{
        'Fighting_Style_Archery':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Rune of Shielding':1,
        'Leather Armor':1,
        'Bayonet':1,
        'Muskete':1,
        'Muskete Bullet':30,
        },
    }

metadict_chars['Warrior 3 lvl (fusilier line-infantry-sergeant)'] = {
    'level':3,
    'firearm_AI':True,
    'carefull_AI':True,
    'char_class':'Warrior-pirate',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Archery':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Shielding':1,
        'Leather Armor':1,
        'Rapier':1,
        'Muskete, Lorenzony':1,
        'Muskete Bullet':30,
        },
    }

metadict_chars['Warrior 4 lvl (fusilier line-infantry-lieutenant)'] = {
    'level':4,
    'firearm_AI':True,
    'carefull_AI':True,
    'char_class':'Warrior-pirate',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Archery':True,
        'Feat_Inspiring_Leader':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Shielding':1,
        'Rune of Armor':1,
        'Rapier':1,
        'Muskete, Lorenzony':1,
        'Muskete Bullet':30,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{},
    }

metadict_chars['Warrior 5 lvl (fusilier line-infantry-captain)'] = {
    # Капитан роты мушкетёров.
    'level':5,
    'firearm_AI':True,
    'carefull_AI':True,
    'char_class':'Warrior-pirate',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Archery':True,
        'Feat_Inspiring_Leader':True,
        'Extra_Attack':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Shielding':1,
        'Rune of Armor':1,
        'Rapier':1,
        'Muskete, Lorenzony':1,
        'Muskete Bullet':30,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{},
    }

#----
# Вспомогательные войска, пращники.

metadict_chars['Warrior 1 lvl (balear slinger)'] = {
    'level':1,
    'char_class':'Warrior-bowman',
    'behavior':'warrior',
    'hit_dice':'1d8',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Hide Armor':1,
        'Heavy Shield':1,
        'Mace':1,
        'Sling real':1,
        'Sling Bullet':10,
        },
    }

metadict_chars['Warrior 2 lvl (balear slinger-corporal)'] = {
    'level':2,
    'char_class':'Warrior-bowman',
    'behavior':'elite_warrior',
    'class_features':{
        'Fighting_Style_Protection':True,
        },
    'hit_dice':'1d8',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Hide Armor':1,
        'Heavy Shield':1,
        'Mace':1,
        'Sling real':1,
        'Sling Bullet':10,
        },
    }

metadict_chars['Warrior 3 lvl (balear slinger-sergeant)'] = {
    'level':3,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Protection':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Breastplate':1,
        'Heavy Shield':1,
        'Mace':1,
        'Sling real':1,
        'Sling Bullet':10,
        },
    }

metadict_chars['Warrior 4 lvl (balear slinger-lieutenant)'] = {
    'level':4,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Protection':True,
        'Feat_Sharpshooter':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Shielding':1,
        'Breastplate':1,
        'Heavy Shield':1,
        'Mace':1,
        'Sling real':1,
        'Sling Bullet':10,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Warrior 5 lvl (balear slinger-captain)'] = {
    'level':5,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Protection':True,
        'Feat_Sharpshooter':True,
        'Extra_Attack':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Half Plate':1,
        'Heavy Shield':1,
        'Mace':1,
        'Sling real':1,
        'Sling Bullet':10,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

#----
# Вспомогательные войска, лучники.

metadict_chars['Warrior 1 lvl (cilician infantry)'] = {
    # Так-то стрелки, но склонны к ближнему бою. Пираты.
    'level':1,
    'char_class':'Warrior-pirate',
    'hit_dice':'1d8',
    'behavior':'warrior',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Studded Leather':1,
        'Shield':1,
        'Shortsword':1,
        'Shortbow':1,
        'Arrow':40,
        },
    }

metadict_chars['Warrior 2 lvl (cilician infantry-corporal)'] = {
    # Используют парное оружие. Своеобразные ребята.
    'level':2,
    'char_class':'Warrior-pirate',
    'hit_dice':'1d8',
    'behavior':'elite_warrior',
    'class_features':{
        'Fighting_Style_Two_Weapon_Fighting':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Scale Mail':1,
        'Shield':1,
        'Rapier':1,
        'Dagger':1,
        'Shortbow':1,
        'Arrow':40,
        },
    }

metadict_chars['Warrior 3 lvl (cilician infantry-sergeant)'] = {
    'level':3,
    'char_class':'Warrior-pirate',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Two_Weapon_Fighting':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Breastplate':1,
        'Shield':1,
        'Rapier':1,
        'Dagger':1,
        'Shortbow':1,
        'Arrow':40,
        },
    }

metadict_chars['Warrior 4 lvl (cilician infantry-lieutenant)'] = {
    'level':4,
    'char_class':'Warrior-pirate',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Two_Weapon_Fighting':True,
        'Feat_Inspiring_Leader':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Shielding':1,
        'Breastplate':1,
        'Shield':1,
        'Rapier':1,
        'Dagger':1,
        'Shortbow':1,
        'Arrow':40,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Warrior 5 lvl (cilician infantry-captain)'] = {
    'level':5,
    'char_class':'Warrior-pirate',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Two_Weapon_Fighting':True,
        'Feat_Inspiring_Leader':True,
        'Extra_Attack':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Shielding':1,
        'Rune of Armor':1,
        'Shield':1,
        'Rapier':1,
        'Dagger':1,
        'Shortbow':1,
        'Arrow':40,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{},
    }

#----
# Вспомогательные войска, кавалерия.

metadict_chars['Warrior 1 lvl (cavalry archer)'] = {
    # Лёгкая кавалерия кочевников
    'level':1,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'archer',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Padded Armor':1,
        'Dagger':1,
        'Shortbow':1,
        'Arrow':40,
        },
    'mount_combat':True,
    'mount_type':'Light Warhorse',
    'equipment_mount':{
        },
    }

metadict_chars['Warrior 2 lvl (cavalry archer-corporal)'] = {
    'level':2,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'archer',
    'class_features':{
        'Fighting_Style_Archery':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Studded Leather':1,
        'Shortsword':1,
        'Shortbow':1,
        'Arrow':40,
        },
    'mount_combat':True,
    'mount_type':'Light Warhorse',
    'equipment_mount':{
        },
    }

metadict_chars['Warrior 3 lvl (cavalry archer-sergeant)'] = {
    'level':3,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Archery':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Breastplate':1,
        'Shortsword':1,
        'Shortbow':1,
        'Arrow':40,
        },
    'mount_combat':True,
    'mount_type':'Warhorse',
    'equipment_mount':{
        },
    }

metadict_chars['Warrior 4 lvl (cavalry archer-lieutenant)'] = {
    'level':4,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Archery':True,
        'Feat_Sharpshooter':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Shielding':1,
        'Breastplate':1,
        'Shortsword':1,
        'Shortbow':1,
        'Arrow':40,
        },
    'mount_combat':True,
    'mount_type':'Warhorse',
    'equipment_mount':{
        },
    }

metadict_chars['Warrior 5 lvl (cavalry archer-captain)'] = {
    'level':5,
    'char_class':'Warrior-officer',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Archery':True,
        'Feat_Sharpshooter':True,
        'Extra_Attack':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Shielding':1,
        'Rune of Armor':1,
        'Shortsword':1,
        'Shortbow':1,
        'Arrow':40,
        },
    'mount_combat':True,
    'mount_type':'Warhorse',
    'equipment_mount':{
        },
    }

#----
# Фракийцы.

metadict_chars['Warrior 1 lvl (thracian infantry)'] = {
    # Штурмовики
    # Щиты используют против лучников, но не в ближнем бою.
    'level':1,
    'char_class':'Warrior',
    'hit_dice':'1d8',
    'behavior':'warrior',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Hide Armor':1,
        'Shield':1,
        'Shortsword':1,
        'Glaive':1,
        'Javelin':6,
        },
    }

metadict_chars['Warrior 2 lvl (thracian infantry-corporal)'] = {
    'level':2,
    'char_class':'Warrior',
    'hit_dice':'1d8',
    'behavior':'elite_warrior',
    'class_features':{
        'Fighting_Style_Great_Weapon_Fighting':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Hide Armor':1,
        'Shield':1,
        'Shortsword':1,
        'Glaive':1,
        'Javelin':6,
        },
    }

metadict_chars['Warrior 3 lvl (thracian infantry-sergeant)'] = {
    'level':3,
    'char_class':'Warrior',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Great_Weapon_Fighting':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Breastplate':1,
        'Shield':1,
        'Shortsword':1,
        'Glaive':1,
        'Javelin':6,
        },
    }

metadict_chars['Warrior 4 lvl (thracian infantry-lieutenant)'] = {
    'level':4,
    'char_class':'Warrior-officer',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Great_Weapon_Fighting':True,
        'Feat_Inspiring_Leader':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Regeneration':1,
        'Half Plate':1,
        'Shield':1,
        'Shortsword':1,
        'Glaive':1,
        'Javelin':6,
        },
    'mount_combat':False,
    'mount_type':'Riding Horse',
    'equipment_mount':{
        },
    }

metadict_chars['Warrior 5 lvl (thracian infantry-captain)'] = {
    'level':5,
    'char_class':'Warrior-officer',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Great_Weapon_Fighting':True,
        'Feat_Inspiring_Leader':True,
        'Extra_Attack':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Regeneration':1,
        'Infusion of Heroism':1,
        'Half Plate':1,
        'Shield':1,
        'Shortsword':1,
        'Glaive':1,
        'Javelin':6,
        },
    'mount_combat':False,
    'mount_type':'Riding Horse',
    'equipment_mount':{
        },
    }


#----
# Кельты, галлы.

metadict_chars['Warrior 1 lvl (celtian infantry)'] = {
    'level':1,
    'char_class':'Warrior',
    'hit_dice':'1d8',
    'behavior':'warrior',
    'class_features':{
        # Вообще, Reckless_Attack -- геройская способность 2 lvl, но кельты слабоваты.
        'Reckless_Attack':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Hide Armor':1,
        'Heavy Shield':1,
        'Longsword':1,
        'Javelin':6,
        },
    }

metadict_chars['Warrior 2 lvl (celtian infantry-corporal)'] = {
    'level':2,
    'char_class':'Warrior',
    'hit_dice':'1d8',
    'behavior':'elite_warrior',
    'class_features':{
        'Fighting_Style_Dueling':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Hide Armor':1,
        'Heavy Shield':1,
        'Longsword':1,
        'Javelin':6,
        },
    }

metadict_chars['Warrior 3 lvl (celtian infantry-sergeant)'] = {
    'level':3,
    'char_class':'Warrior',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Dueling':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':2,
        'Scale Mail':1,
        'Heavy Shield':1,
        'Longsword':1,
        'Javelin':6,
        },
    }

metadict_chars['Warrior 4 lvl (celtian infantry-lieutenant)'] = {
    'level':4,
    'char_class':'Warrior-officer',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Dueling':True,
        'Feat_Inspiring_Leader':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':3,
        'Half Plate':1,
        'Heavy Shield':1,
        'Longsword':1,
        'Javelin':6,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Warrior 5 lvl (celtian infantry-captain)'] = {
    'level':5,
    'char_class':'Warrior-officer',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Dueling':True,
        'Feat_Inspiring_Leader':True,
        'Extra_Attack':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':3,
        'Half Plate':1,
        'Heavy Shield':1,
        'Longsword':1,
        'Javelin':6,
        },
    'mount_combat':False,
    'mount_type':'Riding Horse',
    'equipment_mount':{
        },
    }

#----
# Шекелеш, шерданы:

metadict_chars['Warrior 1 lvl (shekelesh infantry)'] = {
    # Ламинарные медные доспехи.
    'level':1,
    'char_class':'Warrior',
    'hit_dice':'1d8',
    'behavior':'warrior',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Ring Mail':1,
        'Shield':1,
        'Spear':1,
        'Shortbow':1,
        'Arrow':40,
        },
    }

metadict_chars['Warrior 2 lvl (shekelesh infantry-corporal)'] = {
    'level':2,
    'char_class':'Warrior',
    'hit_dice':'1d8',
    'behavior':'elite_warrior',
    'class_features':{
        'Fighting_Style_Defence':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Scale Mail':1,
        'Shield':1,
        'Longsword':1,
        'Shortbow':1,
        'Arrow':40,
        },
    }

metadict_chars['Warrior 3 lvl (shekelesh infantry-sergeant)'] = {
    'level':3,
    'char_class':'Warrior',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Defence':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Breastplate':1,
        'Shield':1,
        'Longsword':1,
        'Shortbow':1,
        'Arrow':40,
        },
    }

metadict_chars['Warrior 4 lvl (shekelesh infantry-lieutenant)'] = {
    'level':4,
    'char_class':'Warrior-officer',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Defence':True,
        'Feat_Inspiring_Leader':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Shielding':1,
        'Breastplate':1,
        'Shield':1,
        'Longsword':1,
        'Shortbow':1,
        'Arrow':40,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Warrior 5 lvl (shekelesh infantry-captain)'] = {
    'level':5,
    'char_class':'Warrior-officer',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Defence':True,
        'Feat_Inspiring_Leader':True,
        'Extra_Attack':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Half Plate':1,
        'Shield':1,
        'Longsword':1,
        'Shortbow':1,
        'Arrow':40,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

#----
# Легион, ромеи

metadict_chars['Warrior 1 lvl (legionary infantry-siege)'] = {
    # С двуручной киркой, чтобы разбивать укрепления. Чисто для тестов.
    'level':1,
    'char_class':'Warrior',
    'hit_dice':'1d8',
    'behavior':'warrior',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Studded Leather':1,
        'Greataxe':1,
        },
    }

metadict_chars['Warrior 2 lvl (legionary infantry-siege-corporal)'] = {
    'level':2,
    'char_class':'Warrior',
    'hit_dice':'1d8',
    'behavior':'elite_warrior',
    'class_features':{
        'Fighting_Style_Great_Weapon_Fighting':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Scale Mail':1,
        'Greataxe':1,
        },
    }

metadict_chars['Warrior 3 lvl (legionary infantry-siege-sergeant)'] = {
    # Десятник (декан, урагос)
    'level':3,
    'seeker_AI':True,
    'fearless_AI':True,
    'char_class':'Warrior',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Great_Weapon_Fighting':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Breastplate':1,
        'Greataxe':1,
        },
    }

#----
# Легион, ромеи (осадное вооружение)

metadict_chars['Warrior 1 lvl (legionary infantry)'] = {
    # Исторически носили по 2 пилума, но шесть весомее (вот только пехота столько не унесёт).
    'level':1,
    'char_class':'Warrior',
    'hit_dice':'1d8',
    'behavior':'warrior',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Studded Leather':1,
        'Heavy Shield':1,
        'Shortsword':1,
        'Pilum':6,
        },
    }

metadict_chars['Warrior 2 lvl (legionary infantry-corporal)'] = {
    'level':2,
    'char_class':'Warrior',
    'hit_dice':'1d8',
    'behavior':'elite_warrior',
    'class_features':{
        'Fighting_Style_Protection':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Scale Mail':1,
        'Heavy Shield':1,
        'Shortsword':1,
        'Pilum':4,
        },
    }

metadict_chars['Warrior 3 lvl (legionary infantry-sergeant)'] = {
    # Десятник (декан, урагос)
    'level':3,
    'char_class':'Warrior',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Protection':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Breastplate':1,
        'Heavy Shield':1,
        'Shortsword':1,
        'Pilum':4,
        },
    }

metadict_chars['Warrior 4 lvl (legionary infantry-lieutenant)'] = {
    # Командир 30 легионеров, старший сержант (опцион, тессерарий)
    'level':4,
    'char_class':'Warrior-officer',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Protection':True,
        'Feat_Inspiring_Leader':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Shielding':1,
        'Breastplate':1,
        'Heavy Shield':1,
        'Shortsword':1,
        'Pilum':4,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Warrior 5 lvl (legionary infantry-captain)'] = {
    # Командир сотни легионеров, центурион (кентурион).
    'level':5,
    'char_class':'Warrior-officer',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Protection':True,
        'Feat_Inspiring_Leader':True,
        'Extra_Attack':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Half Plate':1,
        'Heavy Shield':1,
        'Shortsword':1,
        'Pilum':4,
        },
    'mount_combat':False,
    'mount_type':'Riding Horse',
    'equipment_mount':{
        },
    }

#----
# Тяжёлая пехота наёмников:

metadict_chars['Warrior 1 lvl (mercenary heavy-infantry)'] = {
    # Щиты используют против лучников, но не в ближнем бою.
    'level':1,
    'char_class':'Warrior-heavy',
    'hit_dice':'1d8',
    'behavior':'warrior',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Ring Mail':1,
        'Shield':1,
        'Glaive':1,
        },
    }

metadict_chars['Warrior 2 lvl (mercenary heavy-infantry-corporal)'] = {
    'level':2,
    'char_class':'Warrior-heavy',
    'hit_dice':'1d8',
    'behavior':'elite_warrior',
    'class_features':{
        'Fighting_Style_Great_Weapon_Fighting':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Ring Mail':1,
        'Shield':1,
        'Glaive':1,
        },
    }

metadict_chars['Warrior 3 lvl (mercenary heavy-infantry-sergeant)'] = {
    'level':3,
    'char_class':'Warrior-heavy',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Great_Weapon_Fighting':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Chain Mail':1,
        'Shield':1,
        'Glaive':1,
        },
    }

metadict_chars['Warrior 4 lvl (mercenary heavy-infantry-lieutenant)'] = {
    'level':4,
    'char_class':'Warrior-officer',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Great_Weapon_Fighting':True,
        'Feat_Inspiring_Leader':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Chain Mail':1,
        'Shield':1,
        'Glaive':1,
        },
    'mount_combat':False,
    'mount_type':'Riding Horse',
    'equipment_mount':{
        },
    }

metadict_chars['Warrior 5 lvl (mercenary heavy-infantry-captain)'] = {
    'level':5,
    'char_class':'Warrior-officer',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Great_Weapon_Fighting':True,
        'Feat_Inspiring_Leader':True,
        'Extra_Attack':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Splint Armor':1,
        'Shield':1,
        'Glaive':1,
        },
    'mount_combat':False,
    'mount_type':'Riding Horse',
    'equipment_mount':{
        },
    }

#----
# Вспомогательные войска, инженеры.

metadict_chars['Warrior 2 lvl (siege engineer-apprentice) (trebuchet-light)'] = {
    'level':2,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'archer',
    'class_features':{
        'Fighting_Style_Archery':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Chain Shirt':1,
        'Shield':1,
        'Shortsword':1,
        'Trebuchet, Light':1,
        'Sling Bullets (x25)':100,
        #'Boulder (25 lb)':100,
        #'Boulder (10 lb)':100,
        },
    'mount_combat':True,
    'mount_type':'Onager',
    'equipment_mount':{
        },
    }

metadict_chars['Warrior 2 lvl (siege engineer-apprentice) (trebuchet-heavy)'] = {
    'level':2,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'archer',
    'class_features':{
        'Fighting_Style_Archery':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Chain Shirt':1,
        'Shield':1,
        'Shortsword':1,
        'Trebuchet, Heavy':1,
        'Boulder (200 lb)':100,
        },
    'mount_combat':True,
    'mount_type':'Onager',
    'equipment_mount':{
        },
    }

metadict_chars['Warrior 2 lvl (siege engineer-apprentice) (ballista-siege)'] = {
    'level':2,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'archer',
    'class_features':{
        'Fighting_Style_Archery':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Chain Shirt':1,
        'Shield':1,
        'Shortsword':1,
        'Ballista, Heavy':1,
        'Boulder (50 lb)':100,
        },
    'mount_combat':True,
    'mount_type':'Onager',
    'equipment_mount':{
        },
    }

metadict_chars['Warrior 2 lvl (siege engineer-apprentice) (ballista-medium)'] = {
    'level':2,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'archer',
    'class_features':{
        'Fighting_Style_Archery':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Chain Shirt':1,
        'Shield':1,
        'Shortsword':1,
        'Ballista, Medium':1,
        #'Ballista Bolt (1 lb)':100,
        'Ballista Bolt (5 lb)':100,
        #'Ballista Bolt (25 lb)':100,
        #'Alchemist\'s Fire (10/25 lb)':100,
        },
    'mount_combat':True,
    'mount_type':'Onager',
    'equipment_mount':{
        },
    }

metadict_chars['Warrior 2 lvl (siege engineer-apprentice) (onager-siege)'] = {
    'level':2,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'archer',
    'class_features':{
        'Fighting_Style_Archery':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Chain Shirt':1,
        'Shield':1,
        'Shortsword':1,
        'Onager':1,
        'Boulder (50 lb)':100,
        },
    'mount_combat':True,
    'mount_type':'Onager',
    'equipment_mount':{
        },
    }

metadict_chars['Warrior 2 lvl (siege engineer-apprentice) (onager-fire)'] = {
    'level':2,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'archer',
    'class_features':{
        'Fighting_Style_Archery':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Chain Shirt':1,
        'Shield':1,
        'Shortsword':1,
        'Onager':1,
        'Alchemist\'s Fire (25/50 lb)':10,
        },
    'mount_combat':True,
    'mount_type':'Onager',
    'equipment_mount':{
        },
    }

metadict_chars['Warrior 4 lvl (siege engineer-master)'] = {
    # Командует онаграми, сам не стреляет.
    'level':4,
    'volley_AI':True,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Archery':True,
        'Feat_Sharpshooter':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Shielding':1,
        'Breastplate':1,
        'Shield':1,
        'Shortsword':1,
        },
    }

#----
# Герои

metadict_chars['Fighter 1 lvl (legionary sentinel-battler)'] = {
    # Бойцы в тяжёлых доспехах.
    'level':1,
    'char_class':'Fighter',
    'hit_dice':'1d10',
    'behavior':'elite_warrior',
    'class_features':{
        # Feat_Heavy_Armor_Master увеличивает силу на 1.
        'Feat_Heavy_Armor_Master':True,
        'Ability_Score_Improvement':{
            'strength':+1,
            },
        'Fighting_Style_Protection':True,
        'Second_Wind':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Chain Mail':1,
        'Heavy Shield':1,
        'Long Spear':1,
        'Shortsword':1,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Fighter 2 lvl (legionary sentinel-shieldman)'] = {
    'level':2,
    'char_class':'Fighter',
    'hit_dice':'1d10',
    'behavior':'elite_warrior',
    'class_features':{
        'Feat_Heavy_Armor_Master':True,
        'Ability_Score_Improvement':{
            'strength':+1,
            },
        'Fighting_Style_Protection':True,
        'Second_Wind':True,
        'Action_Surge':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Chain Mail':1,
        'Heavy Shield':1,
        'Long Spear':1,
        'Shortsword':1,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Fighter 3 lvl (legionary sentinel-mystic)'] = {
    'level':3,
    'char_class':'Eldritch_Knight',
    'hit_dice':'1d10',
    'behavior':'commander',
    'class_features':{
        'Feat_Heavy_Armor_Master':True,
        'Ability_Score_Improvement':{
            'strength':+1,
            },
        'Fighting_Style_Protection':True,
        'Second_Wind':True,
        'Action_Surge':True,
        'Martial_Archetype_Eldritch_Knight':True,
        'Weapon_Bond':True,
        'Spellcasting':True,
        'Spells':[
            ('cantrip', 'Sword_Burst'),
            ('cantrip', 'Frostbite'),
            ('1_lvl', 'Absorb_Elements'),
            ('1_lvl', 'Magic_Missile'),
            ('1_lvl', 'Fog_Cloud'),
            ],
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':3,
        'Splint Armor':1,
        'Heavy Shield':1,
        'Longsword':1,
        },
    }

metadict_chars['Fighter 4 lvl (legionary sentinel-lieutenant)'] = {
    'level':4,
    'no_grappler_AI':True,
    'char_class':'Eldritch_Knight',
    'hit_dice':'1d10',
    'behavior':'commander',
    'class_features':{
        'Feat_Heavy_Armor_Master':True,
        'Ability_Score_Improvement':{
            'strength':+1,
            'intelligence':+2,
            },
        'Fighting_Style_Defence':True,
        'Second_Wind':True,
        'Action_Surge':True,
        'Martial_Archetype_Eldritch_Knight':True,
        'Weapon_Bond':True,
        'Spellcasting':True,
        'Spells':[
            ('cantrip', 'Sword_Burst'),
            ('cantrip', 'Frostbite'),
            ('1_lvl', 'Shield'),
            ('1_lvl', 'Absorb_Elements'),
            ('1_lvl', 'Magic_Missile'),
            ('1_lvl', 'Fog_Cloud'),
            ],
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':3,
        'Splint Armor':1,
        'Heavy Shield':1,
        'Longsword +1':1,
        },
    }

metadict_chars['Fighter 5 lvl (legionary sentinel-captain)'] = {
    'level':5,
    'no_grappler_AI':True,
    'char_class':'Eldritch_Knight',
    'hit_dice':'1d10',
    'behavior':'commander',
    'class_features':{
        'Feat_Heavy_Armor_Master':True,
        'Ability_Score_Improvement':{
            'strength':+1,
            'intelligence':+2,
            },
        'Fighting_Style_Defence':True,
        'Second_Wind':True,
        'Action_Surge':True,
        'Martial_Archetype_Eldritch_Knight':True,
        'Weapon_Bond':True,
        'Spellcasting':True,
        'Spells':[
            ('cantrip', 'Sword_Burst'),
            ('cantrip', 'Frostbite'),
            ('1_lvl', 'Shield'),
            ('1_lvl', 'Absorb_Elements'),
            ('1_lvl', 'Magic_Missile'),
            ('1_lvl', 'Fog_Cloud'),
            ],
        'Extra_Attack':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':3,
        'Splint Armor':1,
        'Heavy Shield':1,
        'Longsword +1':1,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

#----
# Бойцы с двуручниками.

metadict_chars['Fighter 1 lvl (legionary slayer-rookie)'] = {
    'level':1,
    'char_class':'Fighter',
    'hit_dice':'1d10',
    'behavior':'elite_warrior',
    'class_features':{
        'Feat_Great_Weapon_Master':True,
        'Fighting_Style_Great_Weapon_Fighting':True,
        'Second_Wind':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Scale Mail':1,
        'Shield':1,
        'Greatsword':1,
        'Javelin':6,
        },
    }

metadict_chars['Fighter 2 lvl (legionary slayer-flanker)'] = {
    'level':2,
    'char_class':'Fighter',
    'hit_dice':'1d10',
    'behavior':'elite_warrior',
    'class_features':{
        'Feat_Great_Weapon_Master':True,
        'Fighting_Style_Great_Weapon_Fighting':True,
        'Second_Wind':True,
        'Action_Surge':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Chain Mail':1,
        'Shield':1,
        'Greatsword':1,
        },
    }

metadict_chars['Fighter 3 lvl (legionary slayer-champion)'] = {
    # TODO: В общем и целом бойцы-чемпионы уступают варварам. Самураев испытай.
    # Пока что мастер боевых искусств.
    'level':3,
    'char_class':'Battlemaster',
    'hit_dice':'1d10',
    'behavior':'commander',
    'class_features':{
        'Feat_Great_Weapon_Master':True,
        'Fighting_Style_Great_Weapon_Fighting':True,
        'Second_Wind':True,
        'Action_Surge':True,
        'Martial_Archetype_Battlemaster':True,
        'Combat_Superiority':True,
        'Student_of_War':True,
        'Parry':True,
        'Menacing_Attack':True,
        'Precision_Attack':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Chain Mail':1,
        'Shield':1,
        'Greatsword':1,
        },
    }

metadict_chars['Fighter 4 lvl (legionary slayer-lieutenant)'] = {
    'level':4,
    'no_grappler_AI':True,
    'char_class':'Battlemaster',
    'hit_dice':'1d10',
    'behavior':'commander',
    'class_features':{
        'Feat_Great_Weapon_Master':True,
        'Fighting_Style_Great_Weapon_Fighting':True,
        'Second_Wind':True,
        'Action_Surge':True,
        'Martial_Archetype_Battlemaster':True,
        'Combat_Superiority':True,
        'Student_of_War':True,
        'Parry':True,
        'Menacing_Attack':True,
        'Precision_Attack':True,
        'Feat_Heavy_Armor_Master':True,
        'Ability_Score_Improvement':{
            'strength':+1,
            },
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Splint Armor':1,
        'Shield':1,
        'Greatsword':1,
        },
    }

metadict_chars['Fighter 5 lvl (legionary slayer-captain)'] = {
    # Samurai
    'level':5,
    'no_grappler_AI':True,
    'char_class':'Battlemaster',
    'hit_dice':'1d10',
    'behavior':'commander',
    'class_features':{
        'Feat_Great_Weapon_Master':True,
        'Fighting_Style_Great_Weapon_Fighting':True,
        'Second_Wind':True,
        'Action_Surge':True,
        'Martial_Archetype_Battlemaster':True,
        'Combat_Superiority':True,
        'Student_of_War':True,
        'Parry':True,
        'Menacing_Attack':True,
        'Precision_Attack':True,
        'Feat_Heavy_Armor_Master':True,
        'Ability_Score_Improvement':{
            'strength':+1,
            },
        'Extra_Attack':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Regeneration':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Splint Armor':1,
        'Shield':1,
        'Greatsword +1':1,
        },
    }

#----
# Всадники легиона.

metadict_chars['Fighter 1 lvl (legionary horseman)'] = {
    # Профессиональная конница на боевых конях.
    'level':1,
    'char_class':'Fighter',
    'hit_dice':'1d10',
    'behavior':'elite_warrior',
    'class_features':{
        'Feat_Mounted_Combatant':True,
        'Fighting_Style_Dueling':True,
        'Second_Wind':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Scale Mail':1,
        'Shield':1,
        'Lance':1,
        'Longsword':1,
        'Pilum':6,
        },
    'mount_combat':True,
    'mount_type':'Light Warhorse',
    'equipment_mount':{
        },
    }

metadict_chars['Fighter 2 lvl (legionary horseman-corporal)'] = {
    # Катафракты.
    'level':2,
    'char_class':'Fighter',
    'hit_dice':'1d10',
    'behavior':'elite_warrior',
    'class_features':{
        'Feat_Mounted_Combatant':True,
        'Fighting_Style_Dueling':True,
        'Second_Wind':True,
        'Action_Surge':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Chain Mail':1,
        'Shield':1,
        'Lance':1,
        'Longsword':1,
        'Pilum':6,
        },
    'mount_combat':True,
    'mount_type':'Warhorse',
    'equipment_mount':{
        },
    }

metadict_chars['Fighter 3 lvl (legionary horseman-sergeant)'] = {
    'level':3,
    'char_class':'Fighter',
    'hit_dice':'1d10',
    'behavior':'commander',
    'class_features':{
        'Feat_Mounted_Combatant':True,
        'Fighting_Style_Dueling':True,
        'Second_Wind':True,
        'Action_Surge':True,
        'Martial_Archetype_Champion':True,
        'Champion_Improved_Critical':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Chain Mail':1,
        'Shield':1,
        'Lance':1,
        'Longsword':1,
        'Pilum':6,
        },
    'mount_combat':True,
    'mount_type':'Warhorse',
    'equipment_mount':{
        'Horse Scale Mail':1,
        },
    }

metadict_chars['Fighter 4 lvl (legionary horseman-lieutenant)'] = {
    'level':4,
    'char_class':'Fighter',
    'hit_dice':'1d10',
    'behavior':'commander',
    'class_features':{
        'Feat_Mounted_Combatant':True,
        'Fighting_Style_Dueling':True,
        'Second_Wind':True,
        'Action_Surge':True,
        'Martial_Archetype_Champion':True,
        'Champion_Improved_Critical':True,
        'Feat_Heavy_Armor_Master':True,
        'Ability_Score_Improvement':{
            'strength':+1,
            },
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Splint Armor':1,
        'Shield':1,
        'Lance':1,
        'Longsword':1,
        'Pilum':6,
        },
    'mount_combat':True,
    'mount_type':'Warhorse',
    'equipment_mount':{
        'Horse Scale Mail':1,
        },
    }

metadict_chars['Fighter 5 lvl (legionary horseman-captain)'] = {
    'level':5,
    'char_class':'Fighter',
    'hit_dice':'1d10',
    'behavior':'commander',
    'class_features':{
        'Feat_Mounted_Combatant':True,
        'Fighting_Style_Dueling':True,
        'Second_Wind':True,
        'Action_Surge':True,
        'Martial_Archetype_Champion':True,
        'Champion_Improved_Critical':True,
        'Feat_Heavy_Armor_Master':True,
        'Ability_Score_Improvement':{
            'strength':+1,
            },
        'Extra_Attack':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Splint Armor':1,
        'Shield':1,
        'Lance':1,
        'Longsword +1':1,
        'Pilum':6,
        },
    'mount_combat':True,
    'mount_type':'Warhorse',
    'equipment_mount':{
        'Horse Scale Mail':1,
        },
    }

#----
# Монахи:

metadict_chars['Monk 1 lvl (city windsong-apprentice)'] = {
    'level':1,
    'char_class':'Monk',
    'hit_dice':'1d8',
    'behavior':'elite_warrior',
    'class_features':{
        'Feat_Defensive_Duelist':True,
        'Unarmored_Defense':True,
        'Martial_Arts':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':[],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Armor':1,
        'Shortsword':1,
        #'Bolas':6,
        },
    }

metadict_chars['Monk 2 lvl (city windsong-gatekeeper)'] = {
    'level':2,
    'char_class':'Monk',
    'hit_dice':'1d8',
    'behavior':'elite_warrior',
    'class_features':{
        'Feat_Defensive_Duelist':True,
        'Unarmored_Defense':True,
        'Martial_Arts':True,
        'Flurry_of_Blows':True,
        'Patient_Defense':True,
        'Step_of_the_Wind':True,
        'Unarmored_Movement':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':[],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Armor':1,
        'Shortsword':1,
        #'Bolas':6,
        },
    }

metadict_chars['Monk 3 lvl (city windsong-lorekeeper)'] = {
    # Путь открытой ладони
    'level':3,
    'char_class':'Monk',
    'hit_dice':'1d8',
    'behavior':'commander',
    'grappler_AI':True,
    'class_features':{
        'Feat_Defensive_Duelist':True,
        'Unarmored_Defense':True,
        'Martial_Arts':True,
        'Flurry_of_Blows':True,
        'Patient_Defense':True,
        'Step_of_the_Wind':True,
        'Unarmored_Movement':True,
        'Deflect_Missiles':True,
        'Open_Hand_Technique':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':[],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Armor':1,
        'Shortsword':1,
        #'Bolas':6,
        },
    }

metadict_chars['Monk 4 lvl (city windsong-oathkeeper)'] = {
    'level':4,
    'char_class':'Monk',
    'hit_dice':'1d8',
    'behavior':'commander',
    'grappler_AI':True,
    'class_features':{
        'Feat_Defensive_Duelist':True,
        'Unarmored_Defense':True,
        'Martial_Arts':True,
        'Flurry_of_Blows':True,
        'Patient_Defense':True,
        'Step_of_the_Wind':True,
        'Unarmored_Movement':True,
        'Deflect_Missiles':True,
        'Open_Hand_Technique':True,
        'Ability_Score_Improvement':{
            'dexterity':+2,
            },
        'Slow_Fall':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':[],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Shortsword':1,
        #'Bolas':6,
        },
    }

metadict_chars['Monk 5 lvl (city windsong-warmonger)'] = {
    'level':5,
    'char_class':'Monk',
    'hit_dice':'1d8',
    'behavior':'commander',
    'grappler_AI':True,
    'class_features':{
        # TODO:
        # Тактика такова:
        # - Атаковать с Flurry_of_Blows и Stunning_Strike (который обнуляет спасброски)
        # - Второй атакой схватить (автоматический успех) и тащить в строй своих.
        'Feat_Defensive_Duelist':True,
        'Unarmored_Defense':True,
        'Martial_Arts':True,
        'Flurry_of_Blows':True,
        'Patient_Defense':True,
        'Step_of_the_Wind':True,
        'Stunning_Strike':True,
        'Unarmored_Movement':True,
        'Deflect_Missiles':True,
        'Open_Hand_Technique':True,
        'Ability_Score_Improvement':{
            'dexterity':+2,
            },
        'Slow_Fall':True,
        'Extra_Attack':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':[],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Shortsword +1':1,
        #'Bolas':6,
        },
    }

#----
# Варвары:

metadict_chars['Barbarian 1 lvl (thracian slayer-dogface)'] = {
    # Фракийцы с ромфаями.
    'level':1,
    'char_class':'Barbarian',
    'hit_dice':'1d12',
    'behavior':'elite_warrior',
    'class_features':{
        'Feat_Great_Weapon_Master':True,
        'Unarmored_Defense':True,
        'Rage':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Scale Mail':1,
        'Heavy Shield':1,
        'Greatsword':1,
        'Javelin':6,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Barbarian 2 lvl (thracian slayer-slasher)'] = {
    'level':2,
    'char_class':'Barbarian',
    'hit_dice':'1d12',
    'behavior':'elite_warrior',
    'class_features':{
        'Feat_Great_Weapon_Master':True,
        'Unarmored_Defense':True,
        'Rage':True,
        'Reckless_Attack':True,
        'Danger_Sense':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':2,
        'Scale Mail':1,
        'Heavy Shield':1,
        'Greatsword':1,
        'Javelin':6,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Barbarian 3 lvl (thracian slayer-juggernaught)'] = {
    'level':3,
    'char_class':'Barbarian',
    'hit_dice':'1d12',
    'behavior':'commander',
    'class_features':{
        'Feat_Great_Weapon_Master':True,
        'Unarmored_Defense':True,
        'Rage':True,
        'Reckless_Attack':True,
        'Danger_Sense':True,
        'Primal_Path_Berserker':True,
        'Berserker_Frenzy':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':3,
        'Scale Mail':1,
        'Heavy Shield':1,
        'Greatsword':1,
        'Javelin':6,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Barbarian 4 lvl (thracian slayer-thane)'] = {
    'level':4,
    'no_grappler_AI':True,
    'char_class':'Barbarian',
    'hit_dice':'1d12',
    'behavior':'commander',
    'class_features':{
        'Feat_Great_Weapon_Master':True,
        'Unarmored_Defense':True,
        'Rage':True,
        'Reckless_Attack':True,
        'Danger_Sense':True,
        'Primal_Path_Berserker':True,
        'Berserker_Frenzy':True,
        'Ability_Score_Improvement':{
            'strength':+2,
            },
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Regeneration':1,
        'Infusion of Heroism':1,
        'Rune of Absorbtion':1,
        'Half Plate':1,
        'Heavy Shield':1,
        'Greatsword':1,
        'Javelin':6,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Barbarian 5 lvl (thracian slayer-lord)'] = {
    'level':5,
    'no_grappler_AI':True,
    'char_class':'Barbarian',
    'hit_dice':'1d12',
    'behavior':'commander',
    'class_features':{
        'Feat_Great_Weapon_Master':True,
        'Unarmored_Defense':True,
        'Rage':True,
        'Reckless_Attack':True,
        'Danger_Sense':True,
        'Primal_Path_Berserker':True,
        'Berserker_Frenzy':True,
        'Ability_Score_Improvement':{
            'strength':+2,
            },
        'Extra_Attack':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Regeneration':1,
        'Infusion of Heroism':1,
        'Rune of Absorbtion':1,
        'Half Plate':1,
        'Heavy Shield':1,
        'Greatsword +1':1,
        'Javelin':6,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

#----
# Варлоки, колдуны:

metadict_chars['Warlock 1 lvl (otherworld seeker-follower)'] = {
    'level':1,
    'char_class':'Warlock',
    'hit_dice':'1d8',
    'behavior':'elite_warrior',
    'class_features':{
        #'Feat_Elemental_Adept':'fire',
        'Feat_Spellsniper':True,
        'Otherworldly_Patron':True,
        'Otherworldly_Patron_The_Fiend':True,
        'Pact_Magic':True,
        'Spells':[
            ('cantrip', 'Eldritch_Blast'),
            ('cantrip', 'Thunderclap'),
            #('cantrip', 'Prestidigitation'),
            #('1_lvl', 'Charm_Person'),
            #('1_lvl', 'Arms_of_Hadar'),
            #('1_lvl', 'Cause_Fear'),
            #('1_lvl', 'Armor_of_Agathys'),
            ('1_lvl', 'Burning_Hands'),
            ('1_lvl', 'Hex'),
            # 2d6 урона, 5x5 клеток вокруг себя:
            #('1_lvl', 'Arms_of_Hadar'),
            #('1_lvl', 'Expeditious_Retreat'),
            #('1_lvl', 'Hellish_Rebuke'),
            #('1_lvl', 'Witch_Bolt'),
            ],
        'Dark_One\'s_Blessing':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple'],
    'armor_skill':['light'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Armor':1,
        'Dagger':1,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Warlock 2 lvl (otherworld seeker-adept)'] = {
    'level':2,
    'char_class':'Warlock',
    'hit_dice':'1d8',
    'behavior':'elite_warrior',
    'class_features':{
        #'Feat_Elemental_Adept':'fire',
        'Feat_Spellsniper':True,
        'Otherworldly_Patron':True,
        'Otherworldly_Patron_The_Fiend':True,
        'Pact_Magic':True,
        'Spells':[
            ('cantrip', 'Eldritch_Blast'),
            ('cantrip', 'Thunderclap'),
            #('1_lvl', 'Charm_Person'),
            #('1_lvl', 'Protection_from_Evil_and_Good'),
            ('1_lvl', 'Burning_Hands'),
            ('1_lvl', 'Armor_of_Agathys'),
            ('1_lvl', 'Hex'),
            ],
        'Dark_One\'s_Blessing':True,
        'Eldritch_Invocations':True,
        'Invocation_Agonizing_Blast':True,
        'Invocation_Eldritch_Spear':True,
        #'Invocation_Mask_of_Many_Faces':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple'],
    'armor_skill':['light'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Armor':1,
        'Dagger':1,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Warlock 3 lvl (otherworld seeker-emissary)'] = {
    'level':3,
    'fireball_AI':True,
    'char_class':'Warlock',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        #'Feat_Elemental_Adept':'fire',
        'Feat_Spellsniper':True,
        'Otherworldly_Patron':True,
        'Otherworldly_Patron_The_Fiend':True,
        'Pact_Magic':True,
        'Spells':[
            ('cantrip', 'Eldritch_Blast'),
            ('cantrip', 'Thunderclap'),
            ('cantrip', 'Prestidigitation'),
            ('cantrip', 'Minor_Illusion'),
            ('cantrip', 'Message'),
            #('2_lvl', 'Charm_Person'),
            ('2_lvl', 'Armor_of_Agathys'),
            ('2_lvl', 'Protection_from_Evil_and_Good'),
            ('2_lvl', 'Invisibility'),
            ('2_lvl', 'Shatter'),
            #('2_lvl', 'Cause_Fear'),
            #('2_lvl', 'Invisibility'),
            #('2_lvl', 'Darkness'),
            # Ловля птиц, 300 футов:
            #('2_lvl', 'Earthbind'),
            #('2_lvl', 'Hold_Person'),
            #('2_lvl', 'Mind_Spike'),
            ],
        'Dark_One\'s_Blessing':True,
        'Eldritch_Invocations':True,
        'Invocation_Agonizing_Blast':True,
        'Invocation_Eldritch_Spear':True,
        'Pact_Boon':True,
        'Pact_of_the_Tome':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple'],
    'armor_skill':['light'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Armor':1,
        'Dagger':1,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Warlock 4 lvl (otherworld seeker-envoy)'] = {
    'level':4,
    'fireball_AI':True,
    'char_class':'Warlock',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        #'Feat_Elemental_Adept':'fire',
        'Feat_Spellsniper':True,
        'Otherworldly_Patron':True,
        'Otherworldly_Patron_The_Fiend':True,
        'Pact_Magic':True,
        'Spells':[
            ('cantrip', 'Eldritch_Blast'),
            ('cantrip', 'Thunderclap'),
            ('cantrip', 'Minor_Illusion'),
            ('cantrip', 'Prestidigitation'),
            ('cantrip', 'Message'),
            ('cantrip', 'Mage_Hand'),
            #('2_lvl', 'Charm_Person'),
            ('2_lvl', 'Armor_of_Agathys'),
            ('2_lvl', 'Protection_from_Evil_and_Good'),
            ('2_lvl', 'Invisibility'),
            ('2_lvl', 'Shatter'),
            ('2_lvl', 'Suggestion'),
            ],
        'Dark_One\'s_Blessing':True,
        'Eldritch_Invocations':True,
        'Invocation_Agonizing_Blast':True,
        'Invocation_Eldritch_Spear':True,
        'Pact_Boon':True,
        'Pact_of_the_Tome':True,
        'Ability_Score_Improvement':{
            'charisma':+2,
            },
        },
    'race':'Human-hero',
    'weapon_skill':['simple'],
    'armor_skill':['light'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Rune of Armor':1,
        'Dagger':1,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Warlock 5 lvl (otherworld seeker-ascendant)'] = {
    'level':5,
    'fireball_AI':True,
    'char_class':'Warlock',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Feat_Elemental_Adept':'fire',
        'Otherworldly_Patron':True,
        'Otherworldly_Patron_The_Fiend':True,
        'Pact_Magic':True,
        'Spells':[
            ('cantrip', 'Eldritch_Blast'),
            ('cantrip', 'Thunderclap'),
            ('cantrip', 'Minor_Illusion'),
            ('cantrip', 'Prestidigitation'),
            ('cantrip', 'Message'),
            ('cantrip', 'Mage_Hand'),
            ('ritual', 'Detect_Magic'),
            ('ritual', 'Identify'),
            #('3_lvl', 'Charm_Person'),
            #('3_lvl', 'Armor_of_Agathys'),
            ('3_lvl', 'Protection_from_Evil_and_Good'),
            ('3_lvl', 'Invisibility'),
            ('3_lvl', 'Suggestion'),
            ('3_lvl', 'Counterspell'),
            ('3_lvl', 'Fireball'),
            #('3_lvl', 'Fear'),
            #('3_lvl', 'Dispel_Magic'),
            ],
        'Dark_One\'s_Blessing':True,
        'Eldritch_Invocations':True,
        'Invocation_Agonizing_Blast':True,
        'Invocation_Eldritch_Spear':True,
        'Invocation_Book_of_Ancient_Secrets':True,
        'Pact_Boon':True,
        'Pact_of_the_Tome':True,
        'Ability_Score_Improvement':{
            'charisma':+2,
            },
        },
    'race':'Human-hero',
    'weapon_skill':['simple'],
    'armor_skill':['light'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Rune of Armor':1,
        'Dagger':1,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

#----
# Волшебники-кошки:

# Snooty
metadict_chars['Wizard 2 lvl (city cat-weaver)'] = {
    'level':2,
    'char_class':'Wizard',
    'hit_dice':'1d6',
    'behavior':'archer',
    'class_features':{
        'Arcane_Recovery':True,
        'Spellcasting':True,
        'Spells':[
            ('cantrip', 'Prestidigitation'),
            ('cantrip', 'Control_Flames'),
            ('cantrip', 'Fire_Bolt'),
            ('ritual', 'Identify'),
            ('ritual', 'Detect_Magic'),
            ('ritual', 'Unseen_Servant'),
            ('1_lvl', 'Shield'),
            ('1_lvl', 'Fog_Cloud'),
            #('1_lvl', 'Sleep'),
            ('1_lvl', 'Magic_Missile'),
            ('1_lvl', 'Absorb_Elements'),
            ],
        'Arcane_Ward':True,
        },
    'race':'Cat-hero',
    'weapon_skill':['simple'],
    'armor_skill':[],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Armor':1,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Wizard 5 lvl (city cat-seer)'] = {
    'level':5,
    'fireball_AI':True,
    'char_class':'Wizard',
    'hit_dice':'1d6',
    'behavior':'commander',
    'class_features':{
        'Arcane_Recovery':True,
        'Spellcasting':True,
        'Spells':[
            ('cantrip', 'Prestidigitation'),
            ('cantrip', 'Control_Flames'),
            ('cantrip', 'Fire_Bolt'),
            ('cantrip', 'Message'),
            ('ritual', 'Identify'),
            ('ritual', 'Detect_Magic'),
            ('ritual', 'Unseen_Servant'),
            ('ritual', 'Gentle_Repose'),
            ('1_lvl', 'Shield'),
            ('1_lvl', 'Fog_Cloud'),
            ('1_lvl', 'Magic_Missile'),
            ('1_lvl', 'Absorb_Elements'),
            ('2_lvl', 'Blur'),
            ('2_lvl', 'Flaming_Sphere'),
            ('2_lvl', 'Shatter'),
            ('3_lvl', 'Counterspell'),
            ('3_lvl', 'Fear'),
            #('3_lvl', 'Fireball'),
            ],
        'Arcane_Ward':True,
        'Ability_Score_Improvement':{
            'intelligence':+2,
            },
        },
    'race':'Cat-hero',
    'weapon_skill':['simple'],
    'armor_skill':[],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Rune of Armor':1,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

#----
# Волшебники:

metadict_chars['Wizard 1 lvl (otherworld mage-disciple)'] = {
    # В книге 1 lvl волшебника -- 6 заклинаний (далее +2 за уровень)
    # Число подготовленных заклинаний: уровень_мага + мод_интеллекта
    'level':1,
    'char_class':'Wizard',
    'hit_dice':'1d6',
    'behavior':'archer',
    'class_features':{
        'Arcane_Recovery':True,
        'Spellcasting':True,
        'Spells':[
            # Mold_Earth -- траншейная машина, 33 кубометра/минута, 900 метров траншеи/час.
            #('cantrip', 'Create_Bonfire'),
            #('cantrip', 'Shape_Water'),
            #('cantrip', 'Mold_Earth'),
            ('cantrip', 'Prestidigitation'),
            ('cantrip', 'Control_Flames'),
            ('cantrip', 'Fire_Bolt'),
            # Доступно 3-4 подготовленных заклинания (кроме ритуалов):
            #('ritual', 'Comprehend_Languages'),
            #('ritual', 'Illusory_Script'),
            #('ritual', 'Floating_Disk'),
            #('ritual', 'Find_Familiar'),
            #('ritual', 'Alarm'),
            ('ritual', 'Identify'),
            ('ritual', 'Detect_Magic'),
            ('ritual', 'Unseen_Servant'),
            ('1_lvl', 'Shield'),
            ('1_lvl', 'Fog_Cloud'),
            ('1_lvl', 'Magic_Missile'),
            ('1_lvl', 'Charm_Person'),
            #('1_lvl', 'Cause_Fear'),
            #('1_lvl', 'Disguise_Self'),
            #('1_lvl', 'Mage_Armor'),
            #('1_lvl', 'Absorb_Elements'),
            ],
        },
    'race':'Human-hero',
    'weapon_skill':['simple'],
    'armor_skill':[],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Armor':1,
        'Dagger':1,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Wizard 2 lvl (otherworld mage-weaver)'] = {
    # Abjurer
    'level':2,
    'char_class':'Wizard',
    'hit_dice':'1d6',
    'behavior':'archer',
    'class_features':{
        'Arcane_Recovery':True,
        'Spellcasting':True,
        'Spells':[
            ('cantrip', 'Prestidigitation'),
            ('cantrip', 'Control_Flames'),
            ('cantrip', 'Fire_Bolt'),
            ('ritual', 'Identify'),
            ('ritual', 'Detect_Magic'),
            ('ritual', 'Unseen_Servant'),
            ('1_lvl', 'Shield'),
            ('1_lvl', 'Fog_Cloud'),
            ('1_lvl', 'Magic_Missile'),
            ('1_lvl', 'Absorb_Elements'),
            ],
        'Arcane_Ward':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple'],
    'armor_skill':[],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Armor':1,
        'Dagger':1,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Wizard 3 lvl (otherworld mage-annalist)'] = {
    'level':3,
    'fireball_AI':True,
    'char_class':'Wizard',
    'hit_dice':'1d6',
    'behavior':'commander',
    'class_features':{
        'Arcane_Recovery':True,
        'Spellcasting':True,
        'Spells':[
            ('cantrip', 'Prestidigitation'),
            ('cantrip', 'Control_Flames'),
            ('cantrip', 'Fire_Bolt'),
            ('ritual', 'Identify'),
            ('ritual', 'Detect_Magic'),
            ('ritual', 'Unseen_Servant'),
            ('ritual', 'Gentle_Repose'),
            #('ritual', 'Magic_Mouth'),
            #('ritual', 'Skywrite'),
            ('1_lvl', 'Shield'),
            ('1_lvl', 'Fog_Cloud'),
            ('1_lvl', 'Magic_Missile'),
            #('2_lvl', 'Magic_Missile'),
            ('1_lvl', 'Absorb_Elements'),
            ('2_lvl', 'Blur'),
            ('2_lvl', 'Shatter'),
            #('2_lvl', 'Melfs_Acid_Arrow'),
            #('2_lvl', 'Continual_Flame'),
            #('2_lvl', 'Magic_Weapon'),
            #('2_lvl', 'Alter_Self'),
            #('2_lvl', 'Levitate'),
            #('2_lvl', 'Blur'),
            #('2_lvl', 'Mirror_Image'),
            #('2_lvl', 'Invisibility'),
            #('2_lvl', 'See_Invisibility'),
            #('2_lvl', 'Pyrotechnics'),
            #('2_lvl', 'Darkvision'),
            #('2_lvl', 'Darkness'),
            #('2_lvl', 'Knock'),
            # Хорошая защита от лучников (10 футов радиус, 21 тайл):
            #('2_lvl', 'Warding_Wind'),
            # Термобарический боеприпас от мира заклинаний (10 футов, 21 тайл):
            # https://www.reddit.com/r/dndnext/comments/bv14et/shatter_really_underrated_spell/
            #('2_lvl', 'Shatter'),
            # Чудовища-уничтожители (9 тайлов контроля, минута концентрации):
            #('2_lvl', 'Flaming_Sphere'),
            #('2_lvl', 'Dust_Devil'),
            # Пример бесполезного заклинания (требует броска атаки в отличии от Magic_Missile):
            #('2_lvl', 'Scorching_Ray'),
            ],
        'Arcane_Ward':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple'],
    'armor_skill':[],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Shielding':1,
        'Rune of Armor':1,
        'Dagger':1,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Wizard 4 lvl (otherworld mage-savant)'] = {
    'level':4,
    'fireball_AI':True,
    'char_class':'Wizard',
    'hit_dice':'1d6',
    'behavior':'commander',
    'class_features':{
        'Arcane_Recovery':True,
        'Spellcasting':True,
        'Spells':[
            ('cantrip', 'Prestidigitation'),
            ('cantrip', 'Control_Flames'),
            ('cantrip', 'Fire_Bolt'),
            ('cantrip', 'Message'),
            ('ritual', 'Identify'),
            ('ritual', 'Detect_Magic'),
            ('ritual', 'Unseen_Servant'),
            ('ritual', 'Gentle_Repose'),
            ('1_lvl', 'Shield'),
            ('1_lvl', 'Fog_Cloud'),
            ('1_lvl', 'Magic_Missile'),
            #('2_lvl', 'Magic_Missile'),
            ('1_lvl', 'Absorb_Elements'),
            ('2_lvl', 'Blur'),
            ('2_lvl', 'Flaming_Sphere'),
            ('2_lvl', 'Shatter'),
            ],
        'Arcane_Ward':True,
        'Ability_Score_Improvement':{
            'intelligence':+2,
            },
        },
    'race':'Human-hero',
    'weapon_skill':['simple'],
    'armor_skill':[],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Rune of Armor':1,
        'Dagger':1,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Wizard 5 lvl (otherworld mage-seer)'] = {
    'level':5,
    'fireball_AI':True,
    'char_class':'Wizard',
    'hit_dice':'1d6',
    'behavior':'commander',
    'class_features':{
        'Arcane_Recovery':True,
        'Spellcasting':True,
        'Spells':[
            ('cantrip', 'Prestidigitation'),
            ('cantrip', 'Control_Flames'),
            ('cantrip', 'Fire_Bolt'),
            ('cantrip', 'Message'),
            ('ritual', 'Identify'),
            ('ritual', 'Detect_Magic'),
            ('ritual', 'Unseen_Servant'),
            ('ritual', 'Gentle_Repose'),
            ('1_lvl', 'Shield'),
            ('1_lvl', 'Fog_Cloud'),
            ('1_lvl', 'Magic_Missile'),
            #('2_lvl', 'Magic_Missile'),
            ('1_lvl', 'Absorb_Elements'),
            ('2_lvl', 'Blur'),
            ('2_lvl', 'Flaming_Sphere'),
            ('2_lvl', 'Shatter'),
            ('3_lvl', 'Counterspell'),
            ('3_lvl', 'Fireball'),
            #('3_lvl', 'Blink'),
            #('3_lvl', 'Sending'),
            #('3_lvl', 'Remove_Curse'),
            #('3_lvl', 'Nondetection'),
            #('3_lvl', 'Magic_Circle'),
            #('3_lvl', 'Dispel_Magic'),
            #('3_lvl', 'Clairvoyance'),
            #('3_lvl', 'Major_Image'),
            #('3_lvl', 'Fly'),
            #('3_lvl', 'Slow'),
            # Sending не зависит от языка отправителя и получателя, срабатывает всегда:
            #('3_lvl', 'Sending'),
            #('3_lvl', 'Glyph_of_Warding'),
            # Clairvoyance можно кастовать раз за разом, всё дальше исследуя опасные места:
            #('3_lvl', 'Clairvoyance'),
            ],
        'Arcane_Ward':True,
        'Ability_Score_Improvement':{
            'intelligence':+2,
            },
        },
    'race':'Human-hero',
    'weapon_skill':['simple'],
    'armor_skill':[],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Rune of Armor':1,
        'Dagger':1,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

#----
# Барды:

metadict_chars['Bard 1 lvl (otherworld singer-follower)'] = {
    'level':1,
    'char_class':'Bard',
    'hit_dice':'1d8',
    'behavior':'archer',
    'class_features':{
        'Feat_Inspiring_Leader':True,
        'Bardic_Inspiration':True,
        'Spellcasting':True,
        'Spells':[
            # TODO: сделай Faerie_Fire
            ('cantrip', 'Prestidigitation'),
            ('cantrip', 'Vicious_Mockery'),
            #('ritual', 'Comprehend_Languages'),
            #('ritual', 'Illusory_Script'),
            #('ritual', 'Unseen_Servant'),
            #('ritual', 'Detect_Magic'),
            #('ritual', 'Identify'),
            ('1_lvl', 'Charm_Person'),
            ('1_lvl', 'Healing_Word'),
            ('1_lvl', 'Sleep'),
            # Faerie_Fire впечатляет, 2x2 квадрат, минута действия, преимущество на атаки.
            ('1_lvl', 'Faerie_Fire'),
            # Bane тоже божественный, три цели, -1d4 к броскам атаки и спасброскам.
            #('1_lvl', 'Bane'),
            # Героизм добавляет мод_харизмы бонусными хитпоинтами каждый ход.
            #('1_lvl', 'Heroism'),
            #('1_lvl', 'Disguise_Self'),
            #('1_lvl', 'Animal_Friendship'),
            ],
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Armor':1,
        'Shield':1,
        'Shortsword':1,
        'Shortbow':1,
        'Arrow':40,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Bard 2 lvl (otherworld singer-stranger)'] = {
    # TODO: Jack_of_All_Trades позволяет добавлять 1/2 бонуса мастерства к модификаторам характеристик.
    'level':2,
    'char_class':'Bard',
    'hit_dice':'1d8',
    'behavior':'archer',
    'class_features':{
        'Feat_Inspiring_Leader':True,
        'Bardic_Inspiration':True,
        'Spellcasting':True,
        'Spells':[
            ('cantrip', 'Prestidigitation'),
            ('cantrip', 'Vicious_Mockery'),
            ('ritual', 'Unseen_Servant'),
            ('1_lvl', 'Charm_Person'),
            ('1_lvl', 'Healing_Word'),
            ('1_lvl', 'Sleep'),
            ('1_lvl', 'Faerie_Fire'),
            ],
        'Jack_of_All_Trades':True,
        'Song_of_Rest':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Armor':1,
        'Shield':1,
        'Shortsword':1,
        'Shortbow':1,
        'Arrow':40,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Bard 3 lvl (otherworld singer-explorer)'] = {
    'level':3,
    'char_class':'Bard',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Feat_Inspiring_Leader':True,
        'Bardic_Inspiration':True,
        'Spellcasting':True,
        'Spells':[
            # TODO: пили "Боевое вдохновение"
            # Позволяет добавлять кость вдохновения к урону или AC.
            ('cantrip', 'Prestidigitation'),
            ('cantrip', 'Vicious_Mockery'),
            ('ritual', 'Unseen_Servant'),
            #('ritual', 'Magic_Mouth'),
            #('ritual', 'Animal_Messenger'),
            #('ritual', 'Locate_Animals_or_Plants'),
            ('1_lvl', 'Charm_Person'),
            ('1_lvl', 'Healing_Word'),
            ('1_lvl', 'Sleep'),
            ('2_lvl', 'Shatter'),
            ('2_lvl', 'Lesser_Restoration'),
            #('2_lvl', 'Hold_Person'),
            #('2_lvl', 'Invisibility'),
            #('2_lvl', 'Enhance_Ability'),
            # Радиус 20 футов, защита от страха для своих, успокоение врагов:
            #('2_lvl', 'Calm_Emotions'),
            # Чудовищно эффективное заклинание, поджаривает врага в броне:
            #('2_lvl', 'Heat_Metal'),
            ],
        'Jack_of_All_Trades':True,
        'Song_of_Rest':True,
        'College_of_Valor':True,
        'Expertise':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Shielding':1,
        'Half Plate':1,
        'Shield':1,
        'Shortsword':1,
        'Shortbow':1,
        'Arrow':40,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Bard 4 lvl (otherworld singer-pathfinder)'] = {
    'level':4,
    'char_class':'Bard',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Feat_Inspiring_Leader':True,
        'Bardic_Inspiration':True,
        'Spellcasting':True,
        'Spells':[
            ('cantrip', 'Prestidigitation'),
            ('cantrip', 'Vicious_Mockery'),
            ('cantrip', 'Message'),
            ('ritual', 'Unseen_Servant'),
            ('1_lvl', 'Charm_Person'),
            ('1_lvl', 'Healing_Word'),
            ('1_lvl', 'Sleep'),
            ('2_lvl', 'Shatter'),
            ('2_lvl', 'Lesser_Restoration'),
            ('2_lvl', 'Calm_Emotions'),
            ],
        'Jack_of_All_Trades':True,
        'Song_of_Rest':True,
        'College_of_Valor':True,
        'Expertise':True,
        'Ability_Score_Improvement':{
            'charisma':+2,
            },
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Half Plate':1,
        'Shield':1,
        'Shortsword':1,
        'Shortbow':1,
        'Arrow':40,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Bard 5 lvl (otherworld singer-leader)'] = {
    'level':5,
    'fireball_AI':True,
    'char_class':'Bard',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Feat_Inspiring_Leader':True,
        'Bardic_Inspiration':True,
        'Spellcasting':True,
        'Spells':[
            ('cantrip', 'Prestidigitation'),
            ('cantrip', 'Vicious_Mockery'),
            ('cantrip', 'Message'),
            ('ritual', 'Unseen_Servant'),
            ('1_lvl', 'Charm_Person'),
            ('1_lvl', 'Healing_Word'),
            ('2_lvl', 'Shatter'),
            ('2_lvl', 'Lesser_Restoration'),
            ('2_lvl', 'Calm_Emotions'),
            ('3_lvl', 'Sending'),
            ('3_lvl', 'Clairvoyance'),
            #('3_lvl', 'Tongues'),
            #('3_lvl', 'Nondetection'),
            #('3_lvl', 'Clairvoyance'),
            #('3_lvl', 'Dispel_Magic'),
            #('3_lvl', 'Glyph_of_Warding'),
            #('3_lvl', 'Speak_with_Dead'),
            #('3_lvl', 'Speak_with_Plants'),
            # Hypnotic_Pattern, 6x6 клеток, минута действия, останавливает врагов.
            #('3_lvl', 'Hypnotic_Pattern'),
            # Plant_Growth, 8 часов каста, радиус 1/2 мили, 269 гектаров, удвоение урожайности на год.
            # За год один маг может улучшить 96 840 гектаров земли, 100 000 тонн пшеницы при сам-12.
            # Каждый маг с этим заклинанием может дать еду лишним 50-150 тыс. населения.
            #('3_lvl', 'Plant_Growth'),
            ],
        'Jack_of_All_Trades':True,
        'Song_of_Rest':True,
        'College_of_Valor':True,
        'Expertise':True,
        'Ability_Score_Improvement':{
            'charisma':+2,
            },
        'Font_of_Inspiration':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Half Plate':1,
        'Shield':1,
        'Shortsword':1,
        'Shortbow +1':1,
        'Arrow':40,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

#----
# Жрецы -- домен войны:

metadict_chars['Cleric 1 lvl (war cleric)'] = {
    'level':1,
    'char_class':'Cleric',
    'abilityes_choice':['wisdom','strength','constitution','dexterity'],
    'hit_dice':'1d8',
    #'seeker_AI':True,
    #'killer_AI':True,
    'behavior':'commander',
    'class_features':{
        'Feat_Inspiring_Leader':True,
        'Spellcasting':True,
        'Spells':[
            ('cantrip', 'Mend'),
            ('cantrip', 'Sacred_Flame'),
            ('cantrip', 'Spare_the_Dying'),
            #('cantrip', 'Word_of_Radiance'),
            ('ritual', 'Detect_Poison_and_Disease'),
            ('ritual', 'Purify_Food_and_Drink'),
            #('ritual', 'Detect_Magic'),
            #('1_lvl', 'Healing_Word'),
            ('1_lvl', 'Bless'),
            #('1_lvl', 'Cure_Wounds'),
            ('1_lvl', 'Healing_Word'),
            #('1_lvl', 'Guiding_Bolt'),
            #('1_lvl', 'Shield_of_Faith'),
            ],
        'War_Domain':True,
        'War_Priest':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Splint Armor':1,
        'Shield':1,
        'Mace':1,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

#----
# Жрецы -- домен жизни:

metadict_chars['Cleric 1 lvl (city maatcarian-acolyte)'] = {
    # Список заклинания, это уровень жреца, плюс модификатор мудрости.
    'level':1,
    'char_class':'Cleric',
    'abilityes_choice':['wisdom','dexterity','constitution','charisma'],
    'hit_dice':'1d8',
    'behavior':'archer',
    'class_features':{
        # Homebrew: жрецы с Unarmored_Defense вместо брони:
        'Unarmored_Defense':True,
        'Feat_Healer':True,
        'Spellcasting':True,
        'Spells':[
            ('cantrip', 'Thaumaturgy'),
            ('cantrip', 'Spare_the_Dying'),
            ('cantrip', 'Sacred_Flame'),
            ('ritual', 'Detect_Poison_and_Disease'),
            ('ritual', 'Purify_Food_and_Drink'),
            #('ritual', 'Detect_Magic'),
            ('1_lvl', 'Healing_Word'),
            ('1_lvl', 'Bless'),
            #('1_lvl', 'Cure_Wounds'),
            #('1_lvl', 'Sanctuary'),
            #('1_lvl', 'Shield_of_Faith'),
            #('ritual', 'Ceremony'),
            ],
        'Life_Domain':True,
        'Disciple_of_Life':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Armor':1,
        'Healer Kit':1,
        'Shortsword':1,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Cleric 2 lvl (city maatcarian-celebrant)'] = {
    'level':2,
    'char_class':'Cleric',
    'abilityes_choice':['wisdom','dexterity','constitution','charisma'],
    'hit_dice':'1d8',
    'behavior':'archer',
    'class_features':{
        'Unarmored_Defense':True,
        'Feat_Healer':True,
        'Spellcasting':True,
        'Spells':[
            ('cantrip', 'Thaumaturgy'),
            ('cantrip', 'Spare_the_Dying'),
            ('cantrip', 'Sacred_Flame'),
            ('ritual', 'Detect_Poison_and_Disease'),
            ('ritual', 'Purify_Food_and_Drink'),
            ('1_lvl', 'Healing_Word'),
            ('1_lvl', 'Sanctuary'),
            ('1_lvl', 'Bless'),
            ],
        'Life_Domain':True,
        'Disciple_of_Life':True,
        'Channel_Turn_Undead':True,
        'Channel_Preserve_Life':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Armor':1,
        'Healer Kit':1,
        'Shortsword':1,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Cleric 3 lvl (city maatcarian-augur)'] = {
    'level':3,
    'fireball_AI':True,
    'char_class':'Cleric',
    'abilityes_choice':['wisdom','dexterity','constitution','charisma'],
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Unarmored_Defense':True,
        'Feat_Healer':True,
        'Spellcasting':True,
        'Spells':[
            ('cantrip', 'Thaumaturgy'),
            ('cantrip', 'Spare_the_Dying'),
            ('cantrip', 'Sacred_Flame'),
            ('ritual', 'Augury'),
            #('ritual', 'Silence'),
            ('1_lvl', 'Healing_Word'),
            ('2_lvl', 'Healing_Word'),
            ('1_lvl', 'Sanctuary'),
            ('2_lvl', 'Gentle_Repose'),
            ('2_lvl', 'Lesser_Restoration'),
            ('2_lvl', 'Continual_Flame'),
            #('2_lvl', 'Protection_from_Poison'),
            #('2_lvl', 'Prayer_of_Healing'),
            #('2_lvl', 'Spiritual_Weapon'),
            #('2_lvl', 'Zone_of_Truth'),
            #('2_lvl', 'Warding_Bond'),
            #('2_lvl', 'Find_Traps'),
            ],
        'Life_Domain':True,
        'Disciple_of_Life':True,
        'Channel_Turn_Undead':True,
        'Channel_Preserve_Life':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Shielding':1,
        'Rune of Armor':1,
        'Shortsword':1,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Cleric 4 lvl (city maatcarian-arbiter)'] = {
    'level':4,
    'fireball_AI':True,
    'char_class':'Cleric',
    'abilityes_choice':['wisdom','dexterity','constitution','charisma'],
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Unarmored_Defense':True,
        'Feat_Healer':True,
        'Spellcasting':True,
        'Spells':[
            ('cantrip', 'Thaumaturgy'),
            ('cantrip', 'Spare_the_Dying'),
            ('cantrip', 'Sacred_Flame'),
            ('cantrip', 'Guidance'),
            ('ritual', 'Augury'),
            ('1_lvl', 'Healing_Word'),
            ('2_lvl', 'Healing_Word'),
            ('1_lvl', 'Sanctuary'),
            ('2_lvl', 'Gentle_Repose'),
            ('2_lvl', 'Lesser_Restoration'),
            ('2_lvl', 'Continual_Flame'),
            ('2_lvl', 'Zone_of_Truth'),
            ('2_lvl', 'Find_Traps'),
            ],
        'Life_Domain':True,
        'Disciple_of_Life':True,
        'Channel_Turn_Undead':True,
        'Channel_Preserve_Life':True,
        'Ability_Score_Improvement':{
            'wisdom':+2,
            },
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Healer Kit':1,
        'Shortsword':1,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Cleric 5 lvl (city maatcarian-reviver)'] = {
    'level':5,
    'fireball_AI':True,
    'char_class':'Cleric',
    'abilityes_choice':['wisdom','dexterity','constitution','charisma'],
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Unarmored_Defense':True,
        'Feat_Healer':True,
        'Spellcasting':True,
        'Spells':[
            ('cantrip', 'Thaumaturgy'),
            ('cantrip', 'Spare_the_Dying'),
            ('cantrip', 'Sacred_Flame'),
            ('cantrip', 'Guidance'),
            ('ritual', 'Augury'),
            #('ritual', 'Water_Walk'),
            #('ritual', 'Meld_into_Stone'),
            ('1_lvl', 'Healing_Word'),
            ('2_lvl', 'Healing_Word'),
            ('3_lvl', 'Healing_Word'),
            ('1_lvl', 'Sanctuary'),
            ('2_lvl', 'Gentle_Repose'),
            ('2_lvl', 'Lesser_Restoration'),
            ('2_lvl', 'Zone_of_Truth'),
            ('3_lvl', 'Beacon_of_Hope'),
            ('3_lvl', 'Revivify'),
            ('3_lvl', 'Sending'),
            #('3_lvl', 'Remove_Curse'),
            #('3_lvl', 'Daylight'),
            #('3_lvl', 'Clairvoyance'),
            #('3_lvl', 'Mass_Healing_Word'),
            #('3_lvl', 'Glyph_of_Warding'),
            #('3_lvl', 'Spirit_Guardians'),
            #('3_lvl', 'Speak_with_Dead'),
            #('3_lvl', 'Tongues'),
            #('3_lvl', 'Sending'),
            #('3_lvl', 'Dispel_Magic'),
            ],
        'Life_Domain':True,
        'Disciple_of_Life':True,
        'Channel_Turn_Undead':True,
        'Channel_Preserve_Life':True,
        'Channel_Destroy_Undead':True,
        'Ability_Score_Improvement':{
            'wisdom':+2,
            },
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Healer Kit':1,
        'Shortsword':1,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

#----
# Жрецы -- домен света:

metadict_chars['Cleric 1 lvl (city luminary-acolyte)'] = {
    # Список заклинания, это уровень жреца, плюс модификатор мудрости.
    'level':1,
    'char_class':'Cleric',
    'abilityes_choice':['wisdom','strength','constitution','dexterity'],
    'hit_dice':'1d8',
    'behavior':'elite_warrior',
    'class_features':{
        'Feat_Healer':True,
        'Spellcasting':True,
        'Spells':[
            ('cantrip', 'Resistance'),
            ('cantrip', 'Spare_the_Dying'),
            ('cantrip', 'Word_of_Radiance'),
            ('cantrip', 'Light'),
            ('ritual', 'Purify_Food_and_Drink'),
            #('ritual', 'Detect_Magic'),
            #('ritual', 'Ceremony'),
            ('1_lvl', 'Faerie_Fire'),
            ('1_lvl', 'Burning_Hands'),
            #('1_lvl', 'Cure_Wounds'),
            ('1_lvl', 'Healing_Word'),
            ('1_lvl', 'Shield_of_Faith'),
            ('1_lvl', 'Bless'),
            #('1_lvl', 'Cure_Wounds'),
            #('1_lvl', 'Sanctuary'),
            ],
        'Light_Domain':True,
        'Warding_Flare':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Breastplate':1,
        'Heavy Shield':1,
        'Shortsword':1,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }


metadict_chars['Cleric 2 lvl (city luminary-celebrant)'] = {
    'level':2,
    'char_class':'Cleric',
    'abilityes_choice':['wisdom','strength','constitution','dexterity'],
    'hit_dice':'1d8',
    'behavior':'elite_warrior',
    'class_features':{
        'Feat_Healer':True,
        'Spellcasting':True,
        'Spells':[
            ('channel', 'Radiance_of_the_Dawn'),
            ('cantrip', 'Resistance'),
            ('cantrip', 'Spare_the_Dying'),
            ('cantrip', 'Word_of_Radiance'),
            ('cantrip', 'Light'),
            ('ritual', 'Ceremony'),
            ('ritual', 'Purify_Food_and_Drink'),
            ('1_lvl', 'Faerie_Fire'),
            ('1_lvl', 'Burning_Hands'),
            #('1_lvl', 'Cure_Wounds'),
            ('1_lvl', 'Healing_Word'),
            ('1_lvl', 'Shield_of_Faith'),
            ('1_lvl', 'Bless'),
            ],
        'Light_Domain':True,
        'Warding_Flare':True,
        'Channel_Turn_Undead':True,
        'Channel_Radiance_of_the_Dawn':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Breastplate':1,
        'Heavy Shield':1,
        'Shortsword':1,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Cleric 3 lvl (city luminary-augur)'] = {
    'level':3,
    'fireball_AI':True,
    'char_class':'Cleric',
    'abilityes_choice':['wisdom','strength','constitution','dexterity'],
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Feat_Healer':True,
        'Spellcasting':True,
        'Spells':[
            ('channel', 'Radiance_of_the_Dawn'),
            ('cantrip', 'Resistance'),
            ('cantrip', 'Spare_the_Dying'),
            ('cantrip', 'Word_of_Radiance'),
            ('cantrip', 'Light'),
            ('ritual', 'Augury'),
            #('ritual', 'Silence'),
            ('1_lvl', 'Faerie_Fire'),
            ('1_lvl', 'Burning_Hands'),
            #('2_lvl', 'Scorching_Ray'),
            #('2_lvl', 'Flaming_Sphere'),
            ('1_lvl', 'Healing_Word'),
            ('2_lvl', 'Healing_Word'),
            ('1_lvl', 'Shield_of_Faith'),
            ('2_lvl', 'Gentle_Repose'),
            ('2_lvl', 'Lesser_Restoration'),
            ('2_lvl', 'Continual_Flame'),
            #('2_lvl', 'Protection_from_Poison'),
            #('2_lvl', 'Prayer_of_Healing'),
            #('2_lvl', 'Spiritual_Weapon'),
            #('2_lvl', 'Zone_of_Truth'),
            #('2_lvl', 'Warding_Bond'),
            #('2_lvl', 'Find_Traps'),
            ],
        'Light_Domain':True,
        'Warding_Flare':True,
        'Channel_Turn_Undead':True,
        'Channel_Radiance_of_the_Dawn':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Breastplate':1,
        'Heavy Shield':1,
        'Shortsword':1,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Cleric 4 lvl (city luminary-arbiter)'] = {
    'level':4,
    'fireball_AI':True,
    'char_class':'Cleric',
    'abilityes_choice':['wisdom','strength','constitution','dexterity'],
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Feat_Healer':True,
        'Spellcasting':True,
        'Spells':[
            ('channel', 'Radiance_of_the_Dawn'),
            ('cantrip', 'Resistance'),
            ('cantrip', 'Spare_the_Dying'),
            ('cantrip', 'Word_of_Radiance'),
            ('cantrip', 'Thaumaturgy'),
            ('ritual', 'Augury'),
            ('1_lvl', 'Faerie_Fire'),
            ('1_lvl', 'Burning_Hands'),
            #('2_lvl', 'Scorching_Ray'),
            #('2_lvl', 'Flaming_Sphere'),
            ('1_lvl', 'Healing_Word'),
            ('2_lvl', 'Healing_Word'),
            ('1_lvl', 'Shield_of_Faith'),
            ('2_lvl', 'Gentle_Repose'),
            ('2_lvl', 'Lesser_Restoration'),
            ('2_lvl', 'Continual_Flame'),
            ('2_lvl', 'Zone_of_Truth'),
            ('2_lvl', 'Find_Traps'),
            ],
        'Light_Domain':True,
        'Warding_Flare':True,
        'Channel_Turn_Undead':True,
        'Channel_Radiance_of_the_Dawn':True,
        'Ability_Score_Improvement':{
            'wisdom':+2,
            },
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Half Plate':1,
        'Heavy Shield':1,
        'Shortsword':1,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Cleric 5 lvl (city luminary-reviver)'] = {
    'level':5,
    'fireball_AI':True,
    'char_class':'Cleric',
    'abilityes_choice':['wisdom','strength','constitution','dexterity'],
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Feat_Healer':True,
        'Spellcasting':True,
        'Spells':[
            ('channel', 'Radiance_of_the_Dawn'),
            ('cantrip', 'Guidance'),
            ('cantrip', 'Word_of_Radiance'),
            ('cantrip', 'Spare_the_Dying'),
            ('cantrip', 'Thaumaturgy'),
            ('ritual', 'Augury'),
            #('ritual', 'Water_Walk'),
            #('ritual', 'Meld_into_Stone'),
            ('1_lvl', 'Faerie_Fire'),
            ('1_lvl', 'Burning_Hands'),
            #('2_lvl', 'Scorching_Ray'),
            #('2_lvl', 'Flaming_Sphere'),
            #('3_lvl', 'Daylight'),
            ('3_lvl', 'Fireball'),
            ('1_lvl', 'Healing_Word'),
            ('2_lvl', 'Healing_Word'),
            ('1_lvl', 'Shield_of_Faith'),
            ('2_lvl', 'Gentle_Repose'),
            ('2_lvl', 'Lesser_Restoration'),
            ('2_lvl', 'Zone_of_Truth'),
            ('3_lvl', 'Beacon_of_Hope'),
            ('3_lvl', 'Revivify'),
            ('3_lvl', 'Sending'),
            #('3_lvl', 'Remove_Curse'),
            #('3_lvl', 'Daylight'),
            #('3_lvl', 'Clairvoyance'),
            #('3_lvl', 'Mass_Healing_Word'),
            #('3_lvl', 'Glyph_of_Warding'),
            #('3_lvl', 'Spirit_Guardians'),
            #('3_lvl', 'Speak_with_Dead'),
            #('3_lvl', 'Tongues'),
            #('3_lvl', 'Sending'),
            #('3_lvl', 'Dispel_Magic'),
            ],
        'Light_Domain':True,
        'Warding_Flare':True,
        'Channel_Turn_Undead':True,
        'Channel_Destroy_Undead':True,
        'Channel_Radiance_of_the_Dawn':True,
        'Ability_Score_Improvement':{
            'wisdom':+2,
            },
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Half Plate':1,
        'Heavy Shield':1,
        'Shortsword +1':1,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

#----
# Воры-котики:

metadict_chars['Rogue 1 lvl (city cat-nyamo)'] = {
    'level':1,
    'char_class':'Rogue',
    'hit_dice':'1d8',
    'behavior':'elite_warrior',
    'class_features':{
        'Feat_Alert':True,
        'Expertise':True,
        'Sneak_Attack':True,
        'Thieves\' Cant':True,
        },
    'race':'Cat-hero',
    'weapon_skill':['simple'],
    'armor_skill':[],
    'equipment_supply':{},
    'equipment_backpack':{},
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Armor':1,
        'Crossbow, Light':1,
        'Crossbow Bolt':40,
        'Dagger':1,
        },
    }

metadict_chars['Rogue 2 lvl (city cat-meow)'] = {
    'level':2,
    'char_class':'Rogue',
    'hit_dice':'1d8',
    'behavior':'elite_warrior',
    'class_features':{
        'Feat_Alert':True,
        'Expertise':True,
        'Sneak_Attack':True,
        'Thieves\' Cant':True,
        'Cunning_Action':True,
        },
    'race':'Cat-hero',
    'weapon_skill':['simple'],
    'armor_skill':[],
    'equipment_supply':{},
    'equipment_backpack':{},
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Armor':1,
        },
    }

metadict_chars['Rogue 3 lvl (city cat-dodger)'] = {
    # Это кошки. Волшебные, но кошки. Им неудобно бегать с оружием и в броне.
    # TODO: с другой стороны, есть же волшебная лапка, то есть Mage_Hand.
    'level':3,
    'char_class':'Arcane_Tricker',
    'hit_dice':'1d8',
    'behavior':'elite_warrior',
    'grappler_AI':True,
    'class_features':{
        'Feat_Alert':True,
        'Expertise':True,
        'Sneak_Attack':True,
        'Thieves\' Cant':True,
        'Cunning_Action':True,
        'Roguish_Archetype_Arcane_Tricker':True,
        'Spellcasting':True,
        'Spells':[
            ('cantrip', 'Mage_Hand'),
            ('cantrip', 'Minor_Illusion'),
            ('cantrip', 'Message'),
            ('1_lvl', 'Fog_Cloud'),
            ('1_lvl', 'Silent_Image'),
            #('1_lvl', 'Magic_Missile'),
            ('1_lvl', 'Sleep'),
            ],
        'Mage_Hand_Legerdemain':True,
        },
    'race':'Cat-hero',
    'weapon_skill':['simple'],
    'armor_skill':[],
    'equipment_supply':{},
    'equipment_backpack':{},
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Shielding':1,
        'Rune of Armor':1,
        },
    }

metadict_chars['Rogue 4 lvl (city cat-runner)'] = {
    'level':4,
    'char_class':'Arcane_Tricker',
    'hit_dice':'1d8',
    'behavior':'commander',
    'grappler_AI':True,
    'class_features':{
        'Feat_Alert':True,
        'Expertise':True,
        'Sneak_Attack':True,
        'Thieves\' Cant':True,
        'Cunning_Action':True,
        'Roguish_Archetype_Arcane_Tricker':True,
        'Spellcasting':True,
        'Spells':[
            ('cantrip', 'Mage_Hand'),
            ('cantrip', 'Minor_Illusion'),
            ('cantrip', 'Message'),
            ('ritual', 'Illusory_Script'),
            ('1_lvl', 'Fog_Cloud'),
            ('1_lvl', 'Silent_Image'),
            #('1_lvl', 'Magic_Missile'),
            ('1_lvl', 'Sleep'),
            ],
        'Mage_Hand_Legerdemain':True,
        'Ability_Score_Improvement':{
            'dexterity':+2,
            },
        },
    'race':'Cat-hero',
    'weapon_skill':['simple'],
    'armor_skill':[],
    'equipment_supply':{},
    'equipment_backpack':{},
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Infusion of Claws':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Rune of Armor':1,
        },
    }

metadict_chars['Rogue 5 lvl (city cat-mastermind)'] = {
    'level':5,
    'fireball_AI':True,
    'char_class':'Arcane_Tricker',
    'hit_dice':'1d8',
    'behavior':'commander',
    'grappler_AI':True,
    'class_features':{
        'Feat_Alert':True,
        'Expertise':True,
        'Sneak_Attack':True,
        'Thieves\' Cant':True,
        'Cunning_Action':True,
        'Roguish_Archetype_Arcane_Tricker':True,
        'Spellcasting':True,
        'Spells':[
            ('cantrip', 'Mage_Hand'),
            ('cantrip', 'Minor_Illusion'),
            ('cantrip', 'Message'),
            ('ritual', 'Illusory_Script'),
            ('1_lvl', 'Fog_Cloud'),
            ('1_lvl', 'Silent_Image'),
            #('1_lvl', 'Magic_Missile'),
            ('1_lvl', 'Sleep'),
            ],
        'Mage_Hand_Legerdemain':True,
        'Uncanny_Dodge':True,
        'Ability_Score_Improvement':{
            'dexterity':+2,
            },
        },
    'race':'Cat-hero',
    'weapon_skill':['simple'],
    'armor_skill':[],
    'equipment_supply':{},
    'equipment_backpack':{},
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Infusion of Claws':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Rune of Armor':1,
        },
    }

#----
# Воры:

metadict_chars['Rogue 1 lvl (mercenary phantom-blackeye)'] = {
    # TODO: Дай им чокобо вместо скучных лошадок.
    'level':1,
    'char_class':'Rogue',
    'hit_dice':'1d8',
    'behavior':'archer',
    'class_features':{
        'Feat_Sharpshooter':True,
        'Expertise':True,
        'Sneak_Attack':True,
        'Thieves\' Cant':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Studded Leather':1,
        'Shield':1,
        'Shortsword':1,
        'Longbow':1,
        'Arrow':40,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Rogue 2 lvl (mercenary phantom-hawkeye)'] = {
    'level':2,
    'char_class':'Rogue',
    'hit_dice':'1d8',
    'behavior':'archer',
    'class_features':{
        'Feat_Sharpshooter':True,
        'Expertise':True,
        'Sneak_Attack':True,
        'Thieves\' Cant':True,
        'Cunning_Action':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Studded Leather':1,
        'Shield':1,
        'Shortsword':1,
        'Longbow':1,
        'Arrow':40,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Rogue 3 lvl (mercenary phantom-deadeye)'] = {
    'level':3,
    'char_class':'Rogue',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Feat_Sharpshooter':True,
        'Expertise':True,
        'Sneak_Attack':True,
        'Thieves\' Cant':True,
        'Cunning_Action':True,
        'Roguish_Archetype_Assasin':True,
        'Assassinate':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Studded Leather':1,
        'Shield':1,
        'Shortsword':1,
        'Longbow':1,
        'Arrow':40,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Rogue 4 lvl (mercenary phantom-lieutenant)'] = {
    'level':4,
    'char_class':'Rogue',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Feat_Sharpshooter':True,
        'Expertise':True,
        'Sneak_Attack':True,
        'Thieves\' Cant':True,
        'Cunning_Action':True,
        'Roguish_Archetype_Assasin':True,
        'Assassinate':True,
        'Feat_Inspiring_Leader':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Studded Leather':1,
        'Shield':1,
        'Shortsword':1,
        'Longbow +1':1,
        'Arrow':40,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Rogue 5 lvl (mercenary phantom-captain)'] = {
    'level':5,
    'fireball_AI':True,
    'char_class':'Rogue',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Feat_Sharpshooter':True,
        'Expertise':True,
        'Sneak_Attack':True,
        'Thieves\' Cant':True,
        'Cunning_Action':True,
        'Roguish_Archetype_Assasin':True,
        'Assassinate':True,
        'Uncanny_Dodge':True,
        'Ability_Score_Improvement':{
            'dexterity':+2,
            },
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Shielding':1,
        'Rune of Armor':1,
        'Shield':1,
        'Shortsword':1,
        'Longbow +1':1,
        'Arrow':40,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

#----
# Рейнджеры:

metadict_chars['Ranger 1 lvl (otherworld wanderer-scout)'] = {
    'level':1,
    'char_class':'Ranger',
    'hit_dice':'1d10',
    'behavior':'archer',
    'class_features':{
        'Feat_Sharpshooter':True,
        'Favored_Enemy':['humans'],
        'Natural_Explorer':['forest'],
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Studded Leather':1,
        'Shield':1,
        'Shortsword':1,
        'Longbow':1,
        'Arrow':40,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Ranger 2 lvl (otherworld wanderer-marksman)'] = {
    'level':2,
    'char_class':'Ranger',
    'hit_dice':'1d10',
    'behavior':'archer',
    'class_features':{
        'Feat_Sharpshooter':True,
        'Favored_Enemy':['humans'],
        'Natural_Explorer':['forest'],
        'Spellcasting':True,
        'Spells':[
            #('ritual', 'Speak_with_Animals'),
            #('ritual', 'Detect_Poison_and_Disease'),
            #('ritual', 'Alarm'),
            ('1_lvl', 'Absorb_Elements'),
            ('1_lvl', 'Hail_of_Thorns'),
            #('1_lvl', 'Fog_Cloud'),
            #('1_lvl', 'Hunter\'s Mark'),
            #('1_lvl', 'Ensnaring_Strike'),
            #('1_lvl', 'Animal_Friendship'),
            #('1_lvl', 'Cure_Wounds'),
            #('1_lvl', 'Goodberry'),
            ],
        'Fighting_Style_Archery':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Breastplate':1,
        'Shield':1,
        'Shortsword':1,
        'Longbow':1,
        'Arrow':40,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Ranger 3 lvl (otherworld wanderer-hunter)'] = {
    'level':3,
    'char_class':'Ranger',
    'hit_dice':'1d10',
    'behavior':'commander',
    'class_features':{
        'Feat_Sharpshooter':True,
        'Favored_Enemy':['humans'],
        'Natural_Explorer':['forest'],
        'Spellcasting':True,
        'Spells':[
            ('1_lvl', 'Absorb_Elements'),
            ('1_lvl', 'Hail_of_Thorns'),
            ('1_lvl', 'Fog_Cloud'),
            ],
        'Fighting_Style_Archery':True,
        'Primeval_Awareness':True,
        'Ranger_Archetype_Hunter':True,
        'Hunter_Horde_Breaker':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Shielding':1,
        'Breastplate':1,
        'Shield':1,
        'Shortsword':1,
        'Longbow':1,
        'Arrow':40,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Ranger 4 lvl (otherworld wanderer-lieutenant)'] = {
    'level':4,
    'char_class':'Ranger',
    'hit_dice':'1d10',
    'behavior':'commander',
    'class_features':{
        'Feat_Sharpshooter':True,
        'Favored_Enemy':['humans'],
        'Natural_Explorer':['forest'],
        'Spellcasting':True,
        'Spells':[
            ('1_lvl', 'Absorb_Elements'),
            ('1_lvl', 'Hail_of_Thorns'),
            ('1_lvl', 'Fog_Cloud'),
            ],
        'Fighting_Style_Archery':True,
        'Primeval_Awareness':True,
        'Ranger_Archetype_Hunter':True,
        'Hunter_Horde_Breaker':True,
        'Feat_Mounted_Combatant':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Shielding':1,
        'Rune of Armor':1,
        'Shield':1,
        'Shortsword':1,
        'Longbow +1':1,
        'Arrow':40,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Ranger 5 lvl (otherworld wanderer-captain)'] = {
    'level':5,
    'char_class':'Ranger',
    'hit_dice':'1d10',
    'behavior':'commander',
    'class_features':{
        'Feat_Sharpshooter':True,
        'Favored_Enemy':['humans'],
        'Natural_Explorer':['forest'],
        'Spellcasting':True,
        'Spells':[
            ('ritual', 'Alarm'),
            #('ritual', 'Silence'),
            #('ritual', 'Beast_Sense'),
            #('ritual', 'Animal_Messenger'),
            #('ritual', 'Locate_Animals_or_Plants'),
            ('1_lvl', 'Absorb_Elements'),
            ('1_lvl', 'Hail_of_Thorns'),
            ('2_lvl', 'Healing_Spirit'),
            ('2_lvl', 'Pass_Without_Trace'),
            #('2_lvl', 'Lesser_Restoration'),
            #('2_lvl', 'Protection_from_Poison'),
            #('2_lvl', 'Cordon_of_Arrows'),
            #('2_lvl', 'Locate_Object'),
            #('2_lvl', 'Find_Traps'),
            # Контроль территории, 20-футов радиус, 10 минут:
            # 2d4 урона за каждую клетку движения.
            #('2_lvl', 'Spike_Growth'),
            ],
        'Fighting_Style_Archery':True,
        'Primeval_Awareness':True,
        'Ranger_Archetype_Hunter':True,
        'Hunter_Horde_Breaker':True,
        'Feat_Mounted_Combatant':True,
        'Extra_Attack':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Shielding':1,
        'Rune of Armor':1,
        'Shield':1,
        'Shortsword':1,
        'Longbow +1':1,
        'Arrow':40,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

#----
# Друиды:

# Gardener, grover,
metadict_chars['Druid 1 lvl (otherworld terian-forester)'] = {
    'level':1,
    'char_class':'Druid',
    'hit_dice':'1d8',
    'behavior':'archer',
    'class_features':{
        'Feat_Healer':True,
        'Spellcasting':True,
        'Spells':[
            # Число заклинаний -- мод_мудрости + уровень_друида:
            # Magic_Stone -- каждый друид значительно усиливает троих пращников.
            # Goodberry -- 2 слота = 20 хитов на завтра. 20 друидов 2 lvl = 600 хитов лечения.
            #('cantrip', 'Create_Bonfire'),
            #('cantrip', 'Control_Flames'),
            #('cantrip', 'Thorn_Whip'),
            #('cantrip', 'Guidance'),
            #('cantrip', 'Gust'),
            ('cantrip', 'Druidcraft'),
            ('cantrip', 'Mold_Earth'),
            ('cantrip', 'Magic_Stone'),
            #('ritual', 'Detect_Magic'),
            #('ritual', 'Detect_Poison_and_Disease'),
            #('ritual', 'Purify_Food_and_Drink'),
            #('ritual', 'Speak_with_Animals'),
            ('1_lvl', 'Absorb_Elements'),
            ('1_lvl', 'Healing_Word'),
            ('1_lvl', 'Entangle'),
            ('1_lvl', 'Ice_Knife'),
            #('1_lvl', 'Fog_Cloud'),
            #('1_lvl', 'Goodberry'),
            #('1_lvl', 'Charm_Person'),
            ],
        'Druidic_Language':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','Scimitar'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Hide Armor':1,
        'Heavy Shield':1,
        'Scimitar':1,
        'Sling real':1,
        'Sling Bullet':10,
        },
    #'mount_combat':True,
    #'mount_type':'Warhorse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Druid 2 lvl (otherworld terian-changer)'] = {
    'level':2,
    'char_class':'Druid',
    'hit_dice':'1d8',
    'behavior':'archer',
    'class_features':{
        'Feat_Healer':True,
        'Spellcasting':True,
        'Spells':[
            ('cantrip', 'Druidcraft'),
            ('cantrip', 'Mold_Earth'),
            ('cantrip', 'Magic_Stone'),
            ('cantrip', 'Shape_Water'),
            #('ritual', 'Detect_Magic'),
            #('ritual', 'Detect_Poison_and_Disease'),
            #('ritual', 'Purify_Food_and_Drink'),
            #('ritual', 'Speak_with_Animals'),
            ('1_lvl', 'Absorb_Elements'),
            ('1_lvl', 'Healing_Word'),
            ('1_lvl', 'Entangle'),
            ('1_lvl', 'Fog_Cloud'),
            ('1_lvl', 'Ice_Knife'),
            #('1_lvl', 'Goodberry'),
            #('1_lvl', 'Charm_Person'),
            ],
        'Druidic_Language':True,
        'Wild_Shape':True,
        'Druid_Circle_Forest':True,
        'Natural_Recovery':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','Scimitar'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':3,
        'Hide Armor':1,
        'Heavy Shield':1,
        'Scimitar':1,
        'Sling real':1,
        'Sling Bullet':10,
        },
    #'mount_combat':True,
    #'mount_type':'Warhorse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Druid 3 lvl (otherworld terian-wiseman)'] = {
    'level':3,
    'fireball_AI':True,
    'char_class':'Druid',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Feat_Healer':True,
        'Spellcasting':True,
        'Spells':[
            ('cantrip', 'Druidcraft'),
            ('cantrip', 'Mold_Earth'),
            ('cantrip', 'Magic_Stone'),
            ('cantrip', 'Shape_Water'),
            #('ritual', 'Skywrite'),
            #('ritual', 'Animal_Messenger'),
            #('ritual', 'Locate_Animals_or_Plants'),
            # Speak_with_Animals + Beast_Sense = разведка мышками и голубями.
            ('ritual', 'Speak_with_Animals'),
            ('ritual', 'Beast_Sense'),
            ('1_lvl', 'Absorb_Elements'),
            ('2_lvl', 'Pass_Without_Trace'),
            ('2_lvl', 'Lesser_Restoration'),
            ('2_lvl', 'Healing_Spirit'),
            # Moonbeam -- орбитальный лазер. Радиус 5 футов, ~5 целей, 2d10 урона/раунд, минута.
            ('2_lvl', 'Moonbeam'),
            #('2_lvl', 'Find_Traps'),
            #('2_lvl', 'Earthbind'),
            #('2_lvl', 'Darkvision'),
            #('2_lvl', 'Dust_Devil'),
            #('2_lvl', 'Heat_Metal'),
            #('2_lvl', 'Gust_of_Wind'),
            # Только горные друиды могут в "Spike_Growth"
            #('2_lvl', 'Spike_Growth'),
            ],
        'Druidic_Language':True,
        'Wild_Shape':True,
        'Druid_Circle_Forest':True,
        'Natural_Recovery':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','Scimitar'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Shielding':1,
        'Hide Armor':1,
        'Heavy Shield':1,
        'Scimitar':1,
        'Sling real':1,
        'Sling Bullet':10,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Druid 4 lvl (otherworld terian-wonderman)'] = {
    'level':4,
    'fireball_AI':True,
    'char_class':'Druid',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Feat_Healer':True,
        'Spellcasting':True,
        'Spells':[
            ('cantrip', 'Druidcraft'),
            ('cantrip', 'Mold_Earth'),
            ('cantrip', 'Magic_Stone'),
            ('cantrip', 'Shape_Water'),
            ('cantrip', 'Create_Bonfire'),
            ('ritual', 'Speak_with_Animals'),
            ('ritual', 'Beast_Sense'),
            ('1_lvl', 'Absorb_Elements'),
            ('2_lvl', 'Pass_Without_Trace'),
            ('2_lvl', 'Lesser_Restoration'),
            ('2_lvl', 'Healing_Spirit'),
            ('2_lvl', 'Gust_of_Wind'),
            ('2_lvl', 'Moonbeam'),
            ],
        'Druidic_Language':True,
        'Wild_Shape':True,
        'Druid_Circle_Forest':True,
        'Natural_Recovery':True,
        'Wild_Shape_Improvement':True,
        'Ability_Score_Improvement':{
            'wisdom':+2,
            },
        },
    'race':'Human-hero',
    'weapon_skill':['simple','Scimitar'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Shielding':1,
        'Rune of Armor':1,
        'Heavy Shield':1,
        'Scimitar':1,
        'Sling real':1,
        'Sling Bullet':10,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Druid 5 lvl (otherworld terian-loremaster)'] = {
    'level':5,
    'fireball_AI':True,
    'char_class':'Druid',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Feat_Healer':True,
        'Spellcasting':True,
        'Spells':[
            ('cantrip', 'Druidcraft'),
            ('cantrip', 'Mold_Earth'),
            ('cantrip', 'Magic_Stone'),
            ('cantrip', 'Shape_Water'),
            ('cantrip', 'Create_Bonfire'),
            #('ritual', 'Feign_Death'),
            #('ritual', 'Meld_into_Stone'),
            ('ritual', 'Speak_with_Animals'),
            ('ritual', 'Beast_Sense'),
            ('1_lvl', 'Absorb_Elements'),
            ('2_lvl', 'Pass_Without_Trace'),
            ('2_lvl', 'Lesser_Restoration'),
            ('2_lvl', 'Healing_Spirit'),
            ('2_lvl', 'Moonbeam'),
            ('3_lvl', 'Call_Lightning'),
            ('3_lvl', 'Conjure_Animals'),
            ('3_lvl', 'Plant_Growth'),
            #('3_lvl', 'Dispel_Magic'),
            #('3_lvl', 'Speak_with_Plants'),
            #('3_lvl', 'Protection_from_Energy'),
            # Только для арктических друидов:
            #('3_lvl', 'Sleet_Storm'),
            ],
        'Druidic_Language':True,
        'Wild_Shape':True,
        'Druid_Circle_Forest':True,
        'Natural_Recovery':True,
        'Wild_Shape_Improvement':True,
        'Ability_Score_Improvement':{
            'wisdom':+2,
            },
        },
    'race':'Human-hero',
    'weapon_skill':['simple','Scimitar'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Shielding':1,
        'Rune of Armor':1,
        'Heavy Shield':1,
        'Scimitar +1':1,
        'Sling real':1,
        'Sling Bullet':10,
        },
    #'mount_combat':True,
    #'mount_type':'Warhorse',
    #'equipment_mount':{
    #    },
    }

#----
# Чародеи:

metadict_chars['Sorcerer 1 lvl (otherworld wildfire-novice)'] = {
    # TODO: Драконья устойчивость даёт +1 hp за уровень, а не только Draconic_Scales.
    # Поведение бойцов, потому что Burning_Hands для ближнего боя.
    'level':1,
    'char_class':'Sorcerer',
    'hit_dice':'1d6',
    'behavior':'elite_warrior',
    'class_features':{
        #'Feat_Inspiring_Leader':True,
        # Игнорируем сопротивление к огню.
        'Feat_Elemental_Adept':'fire',
        'Sorcerous_Origin_Draconic_Bloodline':True,
        'Spellcasting':True,
        'Spells':[
            ('cantrip', 'Prestidigitation'),
            ('cantrip', 'Control_Flames'),
            ('cantrip', 'Create_Bonfire'),
            ('cantrip', 'Sword_Burst'),
            #('cantrip', 'Thunderclap'),
            #('cantrip', 'Acid_Splash'),
            #('cantrip', 'Fire_Bolt'),
            ('1_lvl', 'Shield'),
            ('1_lvl', 'Burning_Hands'),
            #('1_lvl', 'Absorb_Elements'),
            #('1_lvl', 'Magic_Missile'),
            ],
        },
    'race':'Human-hero',
    'weapon_skill':['simple'],
    'armor_skill':[],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Draconic_Scales':1,
        'Dagger':1,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Sorcerer 2 lvl (otherworld wildfire-burner)'] = {
    'level':2,
    'char_class':'Sorcerer',
    'hit_dice':'1d6',
    'behavior':'elite_warrior',
    'class_features':{
        #'Feat_Inspiring_Leader':True,
        'Feat_Elemental_Adept':'fire',
        'Sorcerous_Origin_Draconic_Bloodline':True,
        'Spellcasting':True,
        'Spells':[
            ('cantrip', 'Prestidigitation'),
            ('cantrip', 'Control_Flames'),
            ('cantrip', 'Create_Bonfire'),
            ('cantrip', 'Sword_Burst'),
            ('1_lvl', 'Shield'),
            ('1_lvl', 'Burning_Hands'),
            ('1_lvl', 'Absorb_Elements'),
            #('1_lvl', 'Magic_Missile'),
            ],
        'Font_of_Magic':True,
        'Font_of_Magic_Spellslot_1_lvl':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple'],
    'armor_skill':[],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Draconic_Scales':1,
        'Dagger':1,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Sorcerer 3 lvl (otherworld wildfire-enchanter)'] = {
    'level':3,
    'fireball_AI':True,
    #'disengage_AI':True,
    'char_class':'Sorcerer',
    'hit_dice':'1d6',
    'behavior':'commander',
    'class_features':{
        # TODO: Metamagic_Twinned_Spell сделай. Нужно же!
        #'Feat_Inspiring_Leader':True,
        'Feat_Elemental_Adept':'fire',
        'Sorcerous_Origin_Draconic_Bloodline':True,
        'Spellcasting':True,
        'Spells':[
            ('cantrip', 'Prestidigitation'),
            ('cantrip', 'Control_Flames'),
            ('cantrip', 'Create_Bonfire'),
            ('cantrip', 'Sword_Burst'),
            ('1_lvl', 'Shield'),
            ('1_lvl', 'Burning_Hands'),
            ('1_lvl', 'Absorb_Elements'),
            ('2_lvl', 'Flaming_Sphere'),
            ],
        'Font_of_Magic':True,
        'Metamagic':True,
        'Metamagic_Distant_Spell':True,
        'Metamagic_Twinned_Spell':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple'],
    'armor_skill':[],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Draconic_Scales':1,
        'Dagger':1,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Sorcerer 4 lvl (otherworld wildfire-paragon)'] = {
    'level':4,
    'fireball_AI':True,
    #'disengage_AI':True,
    'char_class':'Sorcerer',
    'hit_dice':'1d6',
    'behavior':'commander',
    'class_features':{
        #'Feat_Inspiring_Leader':True,
        'Feat_Elemental_Adept':'fire',
        'Sorcerous_Origin_Draconic_Bloodline':True,
        'Spellcasting':True,
        'Spells':[
            ('cantrip', 'Prestidigitation'),
            ('cantrip', 'Control_Flames'),
            ('cantrip', 'Create_Bonfire'),
            ('cantrip', 'Sword_Burst'),
            ('cantrip', 'Message'),
            ('1_lvl', 'Shield'),
            ('1_lvl', 'Burning_Hands'),
            ('1_lvl', 'Absorb_Elements'),
            ('2_lvl', 'Flaming_Sphere'),
            ('2_lvl', 'Mirror_Image'),
            #('2_lvl', 'Blur'),
            ],
        'Font_of_Magic':True,
        'Metamagic':True,
        'Metamagic_Distant_Spell':True,
        'Metamagic_Twinned_Spell':True,
        'Ability_Score_Improvement':{
            'charisma':+2,
            },
        },
    'race':'Human-hero',
    'weapon_skill':['simple'],
    'armor_skill':[],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Draconic_Scales':1,
        'Dagger':1,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Sorcerer 5 lvl (otherworld wildfire-ravager)'] = {
    'level':5,
    'fireball_AI':True,
    #'disengage_AI':True,
    'char_class':'Sorcerer',
    'hit_dice':'1d6',
    'behavior':'commander',
    'class_features':{
        #'Feat_Inspiring_Leader':True,
        'Feat_Elemental_Adept':'fire',
        'Sorcerous_Origin_Draconic_Bloodline':True,
        'Spellcasting':True,
        'Spells':[
            ('cantrip', 'Prestidigitation'),
            ('cantrip', 'Control_Flames'),
            ('cantrip', 'Create_Bonfire'),
            ('cantrip', 'Sword_Burst'),
            ('cantrip', 'Message'),
            ('1_lvl', 'Shield'),
            ('1_lvl', 'Burning_Hands'),
            ('1_lvl', 'Absorb_Elements'),
            ('2_lvl', 'Mirror_Image'),
            #('2_lvl', 'Blur'),
            ('3_lvl', 'Counterspell'),
            ('3_lvl', 'Fireball'),
            ],
        'Font_of_Magic':True,
        'Metamagic':True,
        'Metamagic_Distant_Spell':True,
        'Metamagic_Twinned_Spell':True,
        'Ability_Score_Improvement':{
            'charisma':+2,
            },
        },
    'race':'Human-hero',
    'weapon_skill':['simple'],
    'armor_skill':[],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Draconic_Scales':1,
        'Dagger':1,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

#----
# Паладины (конные):

# Sefet, wersefet, imeyer
metadict_chars['Paladin 1 lvl (city sentry-sefet)'] = {
    'level':1,
    'char_class':'Paladin',
    'hit_dice':'1d10',
    'behavior':'elite_warrior',
    'class_features':{
        'Feat_Mounted_Combatant':True,
        'Divine_Sense':True,
        'Lay_on_Hands':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Chain Mail':1,
        'Shield':1,
        'Lance':1,
        'Longsword':1,
        'Pilum':6,
        },
    'mount_combat':True,
    'mount_type':'Light Warhorse',
    'equipment_mount':{
        },
    }

metadict_chars['Paladin 2 lvl (city sentry-weresefet)'] = {
    'level':2,
    'char_class':'Paladin',
    'hit_dice':'1d10',
    'behavior':'elite_warrior',
    'class_features':{
        'Feat_Mounted_Combatant':True,
        'Divine_Sense':True,
        'Lay_on_Hands':True,
        'Fighting_Style_Defence':True,
        #'Fighting_Style_Protection':True,
        'Divine_Smite':True,
        'Spellcasting':True,
        'Spells':[
            # Число заклинаний: Charisma modifier + half your paladin level
            # В среднем 3 заклинания.
            ('1_lvl', 'Divine_Smite'),
            ('1_lvl', 'Bless'),
            ('1_lvl', 'Heroism'),
            ('1_lvl', 'Shield_of_Faith'),
            #('1_lvl', 'Searing_Smite'),
            #('1_lvl', 'Thunderous_Smite'),
            #('1_lvl', 'Protection_from_Evil_and_Good'),
            ],
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Chain Mail':1,
        'Shield':1,
        'Lance':1,
        'Longsword':1,
        'Pilum':6,
        },
    'mount_combat':True,
    'mount_type':'Warhorse',
    'equipment_mount':{
        },
    }

metadict_chars['Paladin 3 lvl (city sentry-imeyer)'] = {
    # TODO: Паладины 3 lvl с "Bless" и "Channel_Sacred_Weapon" имеют мод. атаки 12+
    # Это отлично сочетается с "Feat_Great_Weapon_Master" и +10 урона за счёт -5 к атаке.
    'level':3,
    'char_class':'Paladin',
    'hit_dice':'1d10',
    'behavior':'commander',
    'class_features':{
        'Feat_Mounted_Combatant':True,
        'Divine_Sense':True,
        'Lay_on_Hands':True,
        'Fighting_Style_Defence':True,
        #'Fighting_Style_Protection':True,
        'Divine_Smite':True,
        'Spellcasting':True,
        'Spells':[
            ('channel', 'Sacred_Weapon'),
            ('1_lvl', 'Divine_Smite'),
            ('1_lvl', 'Bless'),
            ('1_lvl', 'Heroism'),
            ('1_lvl', 'Shield_of_Faith'),
            ('1_lvl', 'Protection_from_Evil_and_Good'),
            ('1_lvl', 'Sanctuary'),
            ],
        'Divine_Health':True,
        'Oath_of_Devotion':True,
        'Channel_Turn_The_Unholy':True,
        'Channel_Sacred_Weapon':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Chain Mail':1,
        'Shield':1,
        'Lance':1,
        'Longsword':1,
        'Pilum':6,
        },
    'mount_combat':True,
    'mount_type':'Warhorse',
    'equipment_mount':{
        'Horse Scale Mail':1,
        },
    }

metadict_chars['Paladin 4 lvl (city sentry-lieutenant)'] = {
    'level':4,
    'char_class':'Paladin',
    'hit_dice':'1d10',
    'behavior':'commander',
    'class_features':{
        'Feat_Mounted_Combatant':True,
        'Divine_Sense':True,
        'Lay_on_Hands':True,
        'Fighting_Style_Defence':True,
        #'Fighting_Style_Protection':True,
        'Divine_Smite':True,
        'Spellcasting':True,
        'Spells':[
            ('channel', 'Sacred_Weapon'),
            ('1_lvl', 'Divine_Smite'),
            ('1_lvl', 'Bless'),
            ('1_lvl', 'Heroism'),
            ('1_lvl', 'Shield_of_Faith'),
            ('1_lvl', 'Protection_from_Evil_and_Good'),
            ('1_lvl', 'Sanctuary'),
            ],
        'Divine_Health':True,
        'Oath_of_Devotion':True,
        'Channel_Turn_The_Unholy':True,
        'Channel_Sacred_Weapon':True,
        'Feat_Heavy_Armor_Master':True,
        'Ability_Score_Improvement':{
            'strength':+1,
            },
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Splint Armor':1,
        'Shield':1,
        'Lance':1,
        'Longsword':1,
        'Pilum':6,
        },
    'mount_combat':True,
    'mount_type':'Warhorse',
    'equipment_mount':{
        'Horse Scale Mail':1,
        },
    }

metadict_chars['Paladin 5 lvl (city sentry-captain)'] = {
    # Да уж, паладины могучи. +12-15 мод. атаки с Bless и Sacred_Weapon. 40+ урона/раунд.
    'level':5,
    'char_class':'Paladin',
    'hit_dice':'1d10',
    'behavior':'commander',
    'class_features':{
        'Feat_Mounted_Combatant':True,
        'Divine_Sense':True,
        'Lay_on_Hands':True,
        'Fighting_Style_Defence':True,
        #'Fighting_Style_Protection':True,
        'Divine_Smite':True,
        'Spellcasting':True,
        'Spells':[
            ('channel', 'Sacred_Weapon'),
            ('1_lvl', 'Divine_Smite'),
            ('2_lvl', 'Divine_Smite'),
            ('1_lvl', 'Bless'),
            ('1_lvl', 'Heroism'),
            ('1_lvl', 'Shield_of_Faith'),
            ('1_lvl', 'Protection_from_Evil_and_Good'),
            ('1_lvl', 'Sanctuary'),
            ('1_lvl', 'Command'),
            ('2_lvl', 'Lesser_Restoration'),
            ('2_lvl', 'Zone_of_Truth'),
            ('2_lvl', 'Find_Steed'),
            #('2_lvl', 'Aid'),
            #('2_lvl', 'Branding_Smite'),
            #('2_lvl', 'Magic_Weapon'),
            ],
        'Divine_Health':True,
        'Oath_of_Devotion':True,
        'Channel_Turn_The_Unholy':True,
        'Channel_Sacred_Weapon':True,
        'Feat_Heavy_Armor_Master':True,
        'Ability_Score_Improvement':{
            'strength':+1,
            },
        'Extra_Attack':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Splint Armor':1,
        'Shield':1,
        'Lance':1,
        'Longsword +1':1,
        'Pilum':6,
        },
    'mount_combat':True,
    'mount_type':'Warhorse',
    'equipment_mount':{
        'Horse Scale Mail':1,
        },
    }

#----
# Сариссофоры (армия) (Протесилай):

metadict_chars['Warrior 1 lvl (Тзаангор) (гипасист)'] = {
    'level':1,
    'char_class':'Warrior',
    'behavior':'warrior',
    'hit_dice':'1d8',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'skills':[
        'Athletics',
        ],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Studded Leather':1,
        'Heavy Shield':1,
        'Shortsword':1,
        'Pike':1,
        },
    }

metadict_chars['Warrior 2 lvl (Тзаангор) (ветеран)'] = {
    'level':2,
    'char_class':'Warrior',
    'behavior':'elite_warrior',
    'hit_dice':'1d8',
    'class_features':{
        'Fighting_Style_Defence':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'skills':[
        'Athletics',
        ],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Breastplate':1,
        'Heavy Shield':1,
        'Shortsword':1,
        'Pike':1,
        },
    }

metadict_chars['Warrior 3 lvl (Тзаангор) (ур-лодакос)'] = {
    'level':3,
    'char_class':'Warrior',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Defence':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'skills':[
        'Athletics',
        ],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Breastplate':1,
        'Heavy Shield':1,
        'Longsword':1,
        'Pike':1,
        },
    }

metadict_chars['Warrior 4 lvl (Тзаангор) (лодакос)'] = {
    'level':4,
    'char_class':'Warrior-officer',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Defence':True,
        'Feat_Magic_Initiate':True,
        'Spellcasting':True,
        'Spells':[
            ('cantrip', 'Resistance'),
            ('cantrip', 'Spare_the_Dying'),
            ('1_lvl', 'Bless'),
            ],
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'skills':[
        'Athletics',
        ],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Shielding':1,
        'Breastplate':1,
        'Heavy Shield':1,
        'Longsword':1,
        'Pike':1,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Warrior 5 lvl (Тзаангор) (капитан)'] = {
    'level':5,
    'char_class':'Warrior-officer',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Defence':True,
        'Feat_Magic_Initiate':True,
        'Spellcasting':True,
        'Spells':[
            ('cantrip', 'Resistance'),
            ('cantrip', 'Spare_the_Dying'),
            ('1_lvl', 'Bless'),
            ],
        'Extra_Attack':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'skills':[
        'Athletics',
        ],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Half Plate':1,
        'Heavy Shield':1,
        'Longsword':1,
        'Pike':1,
        },
    'mount_combat':False,
    'mount_type':'Riding Horse',
    'equipment_mount':{
        },
    }

#----
# Паладины (свита) (Протесилай):

metadict_chars['Paladin 1 lvl (Тзаангор) (паладины)'] = {
    'level':1,
    'char_class':'Paladin',
    'hit_dice':'1d10',
    'behavior':'elite_warrior',
    'class_features':{
        'Feat_Heavy_Armor_Master':True,
        'Ability_Score_Improvement':{
            'strength':+1,
            },
        'Divine_Sense':True,
        'Lay_on_Hands':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'skills':[
        'Athletics',
        'Intimidation',
        ],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Splint Armor':1,
        'Heavy Shield':1,
        'Battleaxe':1,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Paladin 5 lvl (Тзаангор) (Протесилай II, «Держатель щита»)'] = {
    # Клятвопреступник 5 lvl / паладин / человек-дориец / принципиально-злой
    # https://dungeonmaster.ru/PlayerProfiles.aspx?module=9404
    'level':5,
    'fearless_AI':True,
    'char_class':'Paladin',
    'hit_dice':'1d10',
    'behavior':'commander',
    'hitpoints_medial':True,
    'abilityes':{
        'strength':18,
        'dexterity':10,
        'constitution':14,
        'intelligence':16,
        'wisdom':12,
        'charisma':18,
        },
    'class_features':{
        'Feat_Heavy_Armor_Master':True,
        'Divine_Sense':True,
        'Lay_on_Hands':True,
        'Fighting_Style_Defence':True,
        'Divine_Smite':True,
        'Spellcasting':True,
        'Spells':[
            # TODO: Допили Героизм и Wrathful_Smite.
            # Подготовленные заклинания: 10 = 4 ХАР +2 уровень (5/2) +4 Домен
            ('channel', 'Control_Undead'),
            ('channel', 'Dreadful_Aspect'),
            ('ritual', 'Zone_of_Truth'),
            ('ritual', 'Find_Steed'),
            ('1_lvl', 'Divine_Smite'),
            ('2_lvl', 'Divine_Smite'),
            ('1_lvl', 'Wrathful_Smite'),
            ('1_lvl', 'Heroism'),
            ('1_lvl', 'Command'),
            ('1_lvl', 'Compelled_Duel'),
            ('1_lvl', 'Hellish_Rebuke)'),
            ('1_lvl', 'Inflict_Wounds)'),
            ('2_lvl', 'Crown_of_madness'),
            ('2_lvl', 'Darkness'),
            ],
        'Divine_Health':True,
        'Oathbreaker':True,
        'Channel_Control_Undead':True,
        'Channel_Dreadful_Aspect':True,
        'Feat_Keen_Mind':True,
        'Extra_Attack':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'skills':[
        # === Strength
        'Athletics',
        # === Dexterity
        #'Acrobatics',
        #'Sleight_of_Hand',
        #'Stealth',
        # === Intelligence
        #'Arcana',
        #'History',
        #'Investigation',
        #'Nature',
        #'Religion',
        # === Wisdom
        #'Animal_Handling',
        'Insight',
        #'Medicine',
        'Perception',
        'Survival',
        # === Charisma
        #'Deception',
        'Intimidation',
        #'Performance',
        #'Persuasion',
        ],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':2,
        #'Rune of Shielding':1,
        'Splint Armor':1,
        'Heavy Shield':1,
        #'Shortsword':1,
        'Long Spear +1':1,
        #'Javelin':4,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

#----
# Дочери медведицы (армия) (Ианта):

metadict_chars['Warrior 1 lvl (Vaarsuvius) (дочерь медведицы Филлис)'] = {
    # Дочери Медведицы [80/80] [1 lvl] [ шкурная броня с медвежьим башкой вместо шлема, Оплон, ромфая, 6 дротиков] сдача 320 денариев
    'level':1,
    'char_class':'Warrior',
    'hit_dice':'1d8',
    'behavior':'warrior',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'skills':[
        'Stealth',
        ],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Goodberry':3,
        'Potion of Antidote':1,
        'Infusion of Longstrider':1,
        'Hide Armor':1,
        'Heavy Shield':1,
        'Glaive':1,
        'Javelin':6,
        'Poison Blade':10,
        },
    }

metadict_chars['Warrior 2 lvl (Vaarsuvius) (ветеран Филлис)'] = {
    'level':2,
    'char_class':'Warrior',
    'hit_dice':'1d8',
    'behavior':'elite_warrior',
    'class_features':{
        'Fighting_Style_Great_Weapon_Fighting':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'skills':[
        'Stealth',
        ],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Goodberry':4,
        'Potion of Antidote':1,
        'Infusion of Longstrider':1,
        'Infusion of False Life':1,
        'Infusion of Healing':1,
        #'Scale Mail':1,
        'Mage_Armor':1,
        'Heavy Shield':1,
        'Shortsword':1,
        #'Glaive':1,
        'Pilum':12,
        'Long Spear':1,
        'Poison Blade':40,
        },
    }

metadict_chars['Warrior 3 lvl (Vaarsuvius) (сержант Филлис)'] = {
    'level':3,
    'char_class':'Warrior',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Great_Weapon_Fighting':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'skills':[
        'Stealth',
        ],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Goodberry':4,
        'Potion of Antidote':1,
        'Infusion of Longstrider':1,
        'Infusion of False Life':1,
        'Rune of Absorbtion':1,
        #'Half Plate':1,
        'Mage_Armor':1,
        'Heavy Shield':1,
        'Shortsword':1,
        #'Glaive':1,
        'Pilum':12,
        'Long Spear':1,
        'Poison Blade':40,
        },
    }

metadict_chars['Warrior 4 lvl (Vaarsuvius) (лейтенант Филлис)'] = {
    'level':4,
    'char_class':'Warrior-officer',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Great_Weapon_Fighting':True,
        #'Fighting_Style_Defence':True,
        'Feat_Inspiring_Leader':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'skills':[
        'Stealth',
        ],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Goodberry':4,
        'Potion of Antidote':1,
        'Infusion of Longstrider':1,
        'Infusion of False Life':1,
        'Rune of Absorbtion':1,
        #'Half Plate':1,
        'Mage_Armor':1,
        'Heavy Shield':1,
        'Shortsword':1,
        #'Glaive':1,
        'Pilum':12,
        'Long Spear':1,
        'Poison Blade':40,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Warrior 5 lvl (Vaarsuvius) (капитан Филлис)'] = {
    'level':5,
    'char_class':'Warrior-officer',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Great_Weapon_Fighting':True,
        #'Fighting_Style_Defence':True,
        'Feat_Alert':True,
        'Extra_Attack':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'skills':[
        'Stealth',
        ],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Goodberry':4,
        'Potion of Antidote':1,
        'Infusion of Longstrider':1,
        'Infusion of False Life':1,
        'Rune of Absorbtion':1,
        #'Half Plate':1,
        'Mage_Armor':1,
        'Heavy Shield':1,
        'Shortsword':1,
        #'Glaive':1,
        'Pilum':12,
        'Long Spear':1,
        'Poison Blade':40,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Warrior 7 lvl (Vaarsuvius) (Филлис)'] = {
    # Сестра Ианты
    'level':7,
    'char_class':'Warrior-officer',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Great_Weapon_Fighting':True,
        #'Fighting_Style_Defence':True,
        'Feat_Alert':True,
        'Extra_Attack':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'skills':[
        'Stealth',
        ],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Goodberry':4,
        'Potion of Antidote':1,
        'Infusion of Longstrider':1,
        'Infusion of False Life':1,
        'Rune of Absorbtion':1,
        #'Half Plate':1,
        'Mage_Armor':1,
        'Heavy Shield':1,
        'Shortsword':1,
        #'Glaive':1,
        'Pilum':12,
        'Long Spear':1,
        'Poison Blade':40,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

#----
# Ополчение (армия) (Ианта):

metadict_chars['Commoner 1 lvl (Vaarsuvius) (охотница)'] = {
    'level':1,
    'char_class':'Commoner',
    'behavior':'archer',
    'hit_dice':'1d8',
    'race':'Human-common',
    'weapon_skill':['simple'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':militia_pack,
    'equipment_weapon':{
        'Studded Leather':1,
        'Shield':1,
        'Spear':1,
        'Hunting Bow':1,
        'Hunting Arrow':40,
        },
    }

metadict_chars['Commoner 2 lvl (Vaarsuvius) (охотница-ветеран)'] = {
    'level':2,
    'char_class':'Commoner',
    'behavior':'archer',
    'hit_dice':'1d8',
    'race':'Human-common',
    'weapon_skill':['simple'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':militia_pack,
    'equipment_weapon':{
        'Studded Leather':1,
        'Shield':1,
        'Spear':1,
        'Hunting Bow':1,
        'Hunting Arrow':40,
        },
    }

metadict_chars['Warrior 3 lvl (Vaarsuvius) (меткий стрелок-отставник)'] = {
    'level':3,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Archery':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Goodberry':5,
        'Potion of Antidote':1,
        'Infusion of Healing':1,
        'Breastplate':1,
        'Dagger':1,
        'Shield':1,
        'Longbow':1,
        'Arrow':40,
        },
    }

metadict_chars['Warrior 3 lvl (Vaarsuvius) (сержант Аксиотея)'] = {
    # Отряд Аксиотеи.
    'level':3,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'commander',
    'fearless_AI':True,
    'killer_AI':True,
    'class_features':{
        'Fighting_Style_Archery':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Goodberry':30,
        'Infusion of Healing':1,
        'Breastplate':1,
        'Dagger':1,
        'Shield':1,
        'Longbow':1,
        'Arrow':40,
        },
    }

metadict_chars['Commoner 1 lvl (Vaarsuvius) (дикарка)'] = {
    'level':1,
    'char_class':'Commoner',
    'behavior':'archer',
    'hit_dice':'1d8',
    'race':'Human-common',
    'weapon_skill':['simple'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':militia_pack,
    'equipment_weapon':{
        'Hide Armor':1,
        'Shield':1,
        'Handaxe':1,
        'Sling real':1,
        'Sling Bullet':10,
        },
    }

metadict_chars['Commoner 2 lvl (Vaarsuvius) (дикарка-ветеран)'] = {
    'level':2,
    'char_class':'Commoner',
    'behavior':'archer',
    'hit_dice':'1d8',
    'race':'Human-common',
    'weapon_skill':['simple'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':militia_pack,
    'equipment_weapon':{
        'Hide Armor':1,
        'Shield':1,
        'Handaxe':1,
        'Sling real':1,
        'Sling Bullet':10,
        },
    }

metadict_chars['Commoner 1 lvl (Vaarsuvius) (токсотай)'] = {
    'level':1,
    'char_class':'Commoner',
    'behavior':'archer',
    'hit_dice':'1d8',
    'race':'Human-common',
    'weapon_skill':['simple'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':militia_pack,
    'equipment_weapon':{
        'Studded Leather':1,
        'Shield':1,
        'Dagger':1,
        'Shortbow':1,
        'Arrow':40,
        },
    }

metadict_chars['Commoner 2 lvl (Vaarsuvius) (токсотай-ветеран)'] = {
    'level':2,
    'char_class':'Commoner',
    'behavior':'archer',
    'hit_dice':'1d8',
    'race':'Human-common',
    'weapon_skill':['simple'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':militia_pack,
    'equipment_weapon':{
        'Studded Leather':1,
        'Shield':1,
        'Dagger':1,
        'Shortbow':1,
        'Arrow':40,
        },
    }

#----
# Ополчение (армия) (Павсаний):

metadict_chars['Commoner 1 lvl (друг) (сатир-охотник)'] = {
    # Сатиры
    'level':1,
    'char_class':'Commoner',
    'behavior':'warrior',
    'hit_dice':'1d8',
    'race':'Satyr',
    'weapon_skill':['simple'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':militia_pack,
    'equipment_weapon':{
        'Studded Leather':1,
        'Shield':1,
        'Spear':1,
        'Hunting Bow':1,
        'Hunting Arrow':40,
        },
    }

metadict_chars['Commoner 2 lvl (друг) (сатир-ветеран)'] = {
    'level':2,
    'char_class':'Commoner',
    'behavior':'warrior',
    'hit_dice':'1d8',
    'race':'Satyr',
    'weapon_skill':['simple'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':militia_pack,
    'equipment_weapon':{
        'Studded Leather':1,
        'Shield':1,
        'Spear':1,
        'Hunting Bow':1,
        'Hunting Arrow':40,
        },
    }

metadict_chars['Warrior 3 lvl (друг) (сатир-сержант)'] = {
    'level':3,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Archery':True,
        },
    'race':'Satyr',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Breastplate':1,
        'Shield':1,
        'Shortsword':1,
        'Longbow':1,
        'Arrow':40,
        },
    }

metadict_chars['Warrior 4 lvl (друг) (сын Павсания)'] = {
    'level':4,
    'char_class':'Warrior-officer',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Archery':True,
        'Feat_Inspiring_Leader':True,
        },
    'race':'Satyr',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Shielding':1,
        'Breastplate':1,
        'Shield':1,
        'Shortsword':1,
        'Longbow':1,
        'Arrow':40,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{},
    }

#----
# Лучники (армия) (Ианта):

metadict_chars['Warrior 1 lvl (Vaarsuvius) (стрелок)'] = {
    # Амазонки Ианты
    'level':1,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'archer',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Goodberry':1,
        'Potion of Antidote':1,
        'Leather Armor':1,
        'Dagger':1,
        'Longbow':1,
        'Arrow':40,
        },
    }

metadict_chars['Warrior 2 lvl (Vaarsuvius) (стрелок-ветеран)'] = {
    'level':2,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'archer',
    'class_features':{
        'Fighting_Style_Archery':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Goodberry':1,
        'Potion of Antidote':1,
        'Scale Mail':1,
        'Dagger':1,
        'Shield':1,
        'Longbow':1,
        'Arrow':40,
        },
    }

metadict_chars['Warrior 3 lvl (Vaarsuvius) (меткий стрелок)'] = {
    'level':3,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Archery':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Goodberry':5,
        'Potion of Antidote':1,
        'Infusion of Healing':1,
        'Breastplate':1,
        'Dagger':1,
        'Shield':1,
        'Longbow':1,
        'Arrow':40,
        },
    }

metadict_chars['Warrior 4 lvl (Vaarsuvius) (стрелок-лейтенант)'] = {
    'level':4,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Archery':True,
        'Feat_Sharpshooter':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Potion of Antidote':1,
        'Infusion of Healing':1,
        'Rune of Shielding':1,
        'Breastplate':1,
        'Shield':1,
        'Dagger':1,
        'Longbow':1,
        'Arrow':40,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{},
    }

metadict_chars['Warrior 5 lvl (Vaarsuvius) (стрелок-капитан)'] = {
    'level':5,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Archery':True,
        'Feat_Sharpshooter':True,
        'Extra_Attack':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Potion of Antidote':1,
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Half Plate':1,
        'Shield':1,
        'Dagger':1,
        'Longbow':1,
        'Arrow':40,
        },
    'mount_combat':False,
    'mount_type':'Riding Horse',
    'equipment_mount':{},
    }

#----
# Друиды (свита) (Ианта):

metadict_chars['Druid 2 lvl (Vaarsuvius) (друид Ианты)'] = {
    'level':2,
    'char_class':'Druid',
    'abilityes_choice':['wisdom','dexterity','constitution','intelligence','charisma','strength'],
    'hit_dice':'1d8',
    'behavior':'elite_warrior',
    'class_features':{
        'Feat_Healer':True,
        'Spellcasting':True,
        'Spells':[
            ('cantrip', 'Druidcraft'),
            ('cantrip', 'Mold_Earth'),
            ('ritual', 'Speak_with_Animals'),
            ('1_lvl', 'Goodberry'),
            #('1_lvl', 'Cure_Wounds'),
            ('1_lvl', 'Healing_Word'),
            ('1_lvl', 'Entangle'),
            ('1_lvl', 'Fog_Cloud'),
            ],
        'Druidic_Language':True,
        'Wild_Shape':True,
        'Wild_Shape_Form':'Brown Bear (CR 1)',
        #'Wild_Shape_Form':'Giant Octopus (CR 1)',
        'Druid_Circle_Moon':True,
        'Combat_Wild_Shape':True,
        'Circle_Forms':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','Scimitar'],
    'armor_skill':['light','medium','shield'],
    'skills':[
        'Nature',
        'Animal_Handling',
        'Medicine',
        'Perception',
        'Survival',
        ],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Goodberry':20,
        'Potion of Antidote':1,
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Armor':1,
        },
    #'mount_combat':True,
    #'mount_type':'Warhorse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Druid 2 lvl (Vaarsuvius) (друид Ианты) (Агата)'] = {
    # Погибла в "Битве за Лемнос". Реинкарнирована в дракона. Повезло.
    'level':2,
    'seeker_AI':True,
    'killer_AI':True,
    'changer_AI':True,
    'fearless_AI':True,
    'char_class':'Druid',
    'abilityes':{
        'strength':10,
        'dexterity':14,
        'constitution':13,
        'intelligence':12,
        'wisdom':15,
        'charisma':12,
        },
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Feat_Healer':True,
        'Spellcasting':True,
        'Spells':[
            ('cantrip', 'Druidcraft'),
            ('cantrip', 'Mold_Earth'),
            ('ritual', 'Speak_with_Animals'),
            ('1_lvl', 'Goodberry'),
            #('1_lvl', 'Cure_Wounds'),
            ('1_lvl', 'Healing_Word'),
            ('1_lvl', 'Entangle'),
            ('1_lvl', 'Fog_Cloud'),
            ],
        'Druidic_Language':True,
        'Wild_Shape':True,
        'Wild_Shape_Form':'Brown Bear (CR 1)',
        #'Wild_Shape_Form':'Giant Octopus (CR 1)',
        'Druid_Circle_Moon':True,
        'Combat_Wild_Shape':True,
        'Circle_Forms':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','Scimitar'],
    'armor_skill':['light','medium','shield'],
    'skills':[
        'Nature',
        'Animal_Handling',
        'Medicine',
        'Perception',
        'Survival',
        ],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Goodberry':20,
        'Potion of Antidote':1,
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Armor':1,
        },
    #'mount_combat':True,
    #'mount_type':'Warhorse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Brass Dragon, (Vaarsuvius) (Агаталара Огненная)'] = {
    # Реинкарнация Агаты
    # Молодой латунный дракон
    'level':13,
    'Dash_AI':True,
    'fearless_AI':True,
    'disengage_AI':True,
    'recharge_AI':True,
    #'accurate_AI':True,
    'no_grappler_AI':True,
    'air_walk':True,
    'armor_class_natural':17,
    'challenge_rating':'6',
    'char_class':'Sorcerer',
    'behavior':'commander',
    'hitpoints_medial':True,
    'class_features':{
        'Extra_Attack':2,
        'immunity':['fire'],
        'Blindvision':30,
        'Darkvision':120,
        'Recharge':True,
        'Recharge_dice':'1d6',
        'Recharge_numbers':[5,6],
        # Способности Агаты:
        'Feat_Healer':True,
        'Spellcasting':True,
        'Spells':[
            ('cantrip', 'Druidcraft'),
            ('cantrip', 'Mold_Earth'),
            ('ritual', 'Speak_with_Animals'),
            #('1_lvl', 'Goodberry'),
            #('1_lvl', 'Cure_Wounds'),
            #('1_lvl', 'Healing_Word'),
            ('1_lvl', 'Absorb_Elements'),
            ('1_lvl', 'Fog_Cloud'),
            ],
        'Druidic_Language':True,
        'Wild_Shape':True,
        #'Wild_Shape_Form':'Brown Bear (CR 1)',
        #'Wild_Shape_Form':'Giant Octopus (CR 1)',
        'Druid_Circle_Moon':True,
        'Combat_Wild_Shape':True,
        'Circle_Forms':True,
        },
    'abilityes':{
        'strength':19,
        'dexterity':10,
        'constitution':17,
        # Характеристики Агаты:
        'intelligence':12,
        'wisdom':15,
        'charisma':12,
        },
    'hit_dice':'1d10',
    'attacks':{
        ('close', 'claws'): {
            'attack_mod':7,
            'damage_mod':4,
            'weapon': False,
            'weapon_type':['simple'],
            'damage_type':'slashing',
            'damage_dice':'2d6',
            'attack_range':5,
            'attack_type':'close',
            'weapon_skills_use': ['simple'],
            'attack_mod_type':'strength',
            'weapon_of_choice':'claws',
            },
        ('reach', 'bite'): {
            'attack_mod':7,
            'damage_mod':4,
            'weapon': False,
            'weapon_type':['simple'],
            'damage_type':'piercing',
            'damage_dice':'2d10',
            'attack_range':10,
            'attack_type':'close',
            'weapon_skills_use': ['simple'],
            'attack_mod_type':'strength',
            'weapon_of_choice':'bite'
            },
        ('zone', 'Unconscious'): {
            'zone':True,
            'debuff':True,
            'effect':'sleep',
            'effect_timer':100,
            'zone_shape':'cone',
            'attack_range':30,
            'direct_hit':True,
            'savethrow':True,
            'savethrow_ability':'constitution',
            'casting_time':'action',
            'spell_save_DC':14,
            'recharge': True,
            'ammo':1,
            'weapon_of_choice':'Unconscious'
            },
        ('zone', 'Fire_Ray'): {
            'zone':True,
            'accurate':True,
            'zone_shape':'ray',
            'attack_range':40,
            'direct_hit':True,
            'savethrow':True,
            'savethrow_ability':'dexterity',
            'casting_time':'action',
            'damage_type':'fire',
            'damage_dice':'12d6',
            'spell_save_DC':14,
            'recharge': True,
            'ammo':1,
            },
        },
    'race':'Dragon-big',
    'weapon_skill':[],
    'armor_skill':[],
    'equipment_weapon':{
        'Goodberry':100,
        'Potion of Antidote':1,
        'Infusion of Regeneration':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        },
    'equipment_backpack':{},
    'equipment_supply':{},
    }

metadict_chars['Druid 2 lvl (Vaarsuvius) (друид Ианты) (Психея)'] = {
    # Глава "Подводной стражи" Агаты, 45 лет, лицо в шрамах, садист.
    'level':2,
    'killer_AI':True,
    'changer_AI':True,
    'char_class':'Druid',
    'abilityes':{
        'strength':12,
        'dexterity':17,
        'constitution':17,
        'intelligence':15,
        'wisdom':18,
        'charisma':14,
        },
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Feat_Healer':True,
        'Spellcasting':True,
        'Spells':[
            ('cantrip', 'Druidcraft'),
            ('cantrip', 'Mold_Earth'),
            ('ritual', 'Speak_with_Animals'),
            ('1_lvl', 'Goodberry'),
            #('1_lvl', 'Cure_Wounds'),
            ('1_lvl', 'Healing_Word'),
            ('1_lvl', 'Entangle'),
            ('1_lvl', 'Fog_Cloud'),
            ],
        'Druidic_Language':True,
        'Wild_Shape':True,
        'Wild_Shape_Form':'Brown Bear (CR 1)',
        #'Wild_Shape_Form':'Giant Octopus (CR 1)',
        'Druid_Circle_Moon':True,
        'Combat_Wild_Shape':True,
        'Circle_Forms':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','Scimitar'],
    'armor_skill':['light','medium','shield'],
    'skills':[
        'Nature',
        'Animal_Handling',
        'Medicine',
        'Perception',
        'Survival',
        ],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Goodberry':20,
        'Potion of Antidote':1,
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Armor':1,
        },
    #'mount_combat':True,
    #'mount_type':'Warhorse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Druid 7 lvl (Vaarsuvius) (Ианта «Дочь бури»)'] = {
    'level':7,
    'changer_AI':True,
    'char_class':'Druid',
    'hit_dice':'1d8',
    'behavior':'commander',
    'hitpoints_medial':True,
    #'hitpoints_base':8 + 19,
    'abilityes':{
        'strength':10,
        'dexterity':14,
        'constitution':16,
        'intelligence':12,
        'wisdom':20,
        'charisma':16,
        },
    'class_features':{
        #'Feat_Inspiring_Leader':True,
        'Feat_Sharpshooter':True,
        'Spellcasting':True,
        'Spells':[
            ('cantrip', 'Druidcraft'),
            ('cantrip', 'Thorn_Whip'),
            ('cantrip', 'Shape_Water'),
            ('ritual', 'Detect_Magic'),
            ('ritual', 'Speak_with_Animals'),
            ('ritual', 'Beast_Sense'),
            ('ritual', 'Water_Breathing'),
            ('ritual', 'Water_Walk'),
            ('1_lvl', 'Jump'),
            ('2_lvl', 'Moonbeam'),
            ('2_lvl', 'Pass_Without_Trace'),
            ('2_lvl', 'Flaming_Sphere'),
            ('3_lvl', 'Call_Lightning'),
            ('3_lvl', 'Conjure_Animals'),
            ('3_lvl', 'Dispel_Magic'),
            #('3_lvl', 'Plant_Growth'),
            ('4_lvl', 'Polymorph'),
            ('4_lvl', 'Conjure_Woodlands_Beings'),
            ],
        'Druidic_Language':True,
        'Wild_Shape':True,
        'Wild_Shape_Form':'Giant Elk (CR 2)',
        #'Wild_Shape_Form':'Brown Bear (CR 1)',
        #'Wild_Shape_Form':'Giant Octopus (CR 1)',
        'Druid_Circle_Moon':True,
        'Combat_Wild_Shape':True,
        'Wild_Shape_Improvement':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','Scimitar'],
    'armor_skill':['light','medium','shield'],
    'skills':[
        # Учится "Убеждению", забивает на "Уход за животными".
        # === Intelligence
        'Nature',
        # === Wisdom
        'Animal_Handling',
        #'Insight',
        'Medicine',
        'Perception',
        'Survival',
        # === Charisma
        #'Deception',
        #'Intimidation',
        #'Performance',
        'Persuasion',
        ],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Potion of Antidote':1,
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Breastplate':1,
        'Shield':1,
        'Longbow +1':1,
        'Arrow':40,
        },
    #'mount_combat':True,
    #'mount_type':'Warhorse',
    #'equipment_mount':{
    #    },
    }

#----
# Бойцы (свита) (Артаманах):

metadict_chars['Fighter 1 lvl (ArbitraryNickname) (снайпер)'] = {
    # Снайперы, корректируют "Град стрел" ополчения.
    'level':1,
    'char_class':'Battlemaster',
    'abilityes_choice':['dexterity','constitution','strength','charisma'],
    'hit_dice':'1d10',
    'behavior':'archer',
    'class_features':{
        'Feat_Sharpshooter':True,
        'Fighting_Style_Archery':True,
        'Second_Wind':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'skills':[
        'Perception',
        ],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Rune of Armor':1,
        'Shield':1,
        'Shortsword':1,
        'Longbow':1,
        'Arrow':40,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Fighter 5 lvl (ArbitraryNickname) (Артаманах Рыбник)'] = {
    # Лучник, мастер боевых искусств
    'level':5,
    'char_class':'Battlemaster',
    'abilityes_choice':['dexterity','constitution','strength','charisma'],
    'hit_dice':'1d10',
    'behavior':'commander',
    'hitpoints_medial':True,
    'abilityes':{
        'strength':12,
        'dexterity':20,
        'constitution':12,
        'intelligence':15,
        'wisdom':10,
        'charisma':16,
        },
    'class_features':{
        # Сложные в реализации "Атака с манёвром" и "Удар командира"
        # Заменяются на "Точная атака" и "Атака с угрозой"
        'Feat_Sharpshooter':True,
        'Fighting_Style_Archery':True,
        'Second_Wind':True,
        'Action_Surge':True,
        'Martial_Archetype_Battlemaster':True,
        'Combat_Superiority':True,
        'Student_of_War':True,
        #'Commander\'s_Strike':True,
        #'Maneuvering_Attack':True,
        'Parry':True,
        'Menacing_Attack':True,
        'Precision_Attack':True,
        'Feat_Inspiring_Leader':True,
        'Extra_Attack':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Shielding':1,
        'Rune of Armor':1,
        'Shield':1,
        'Longbow +1':1,
        'Scimitar':1,
        'Dagger':1,
        'Arrow':40,
        },
    }

#----
# Жрецы (свита) (Патрокл «Македонянин»):
# Жрецы -- домен войны:

metadict_chars['Cleric 2 lvl (Vened) (жрец Патрокла)'] = {
    'level':2,
    'char_class':'Cleric',
    'abilityes_choice':['wisdom','strength','constitution','charisma'],
    'hit_dice':'1d8',
    'behavior':'elite_warrior',
    'class_features':{
        # Даём халявный Feat_Heavy_Armor_Master, потому что большим созданиям нелегко.
        'Feat_Inspiring_Leader':True,
        'Feat_Heavy_Armor_Master':True,
        'Ability_Score_Improvement':{
            'strength':+1,
            },
        'Spellcasting':True,
        'Spells':[
            ('cantrip', 'Mend'),
            ('cantrip', 'Sacred_Flame'),
            ('cantrip', 'Spare_the_Dying'),
            ('ritual', 'Detect_Poison_and_Disease'),
            ('ritual', 'Purify_Food_and_Drink'),
            #('ritual', 'Detect_Magic'),
            ('1_lvl', 'Healing_Word'),
            ('1_lvl', 'Bless'),
            ('1_lvl', 'Guiding_Bolt'),
            #('1_lvl', 'Shield_of_Faith'),
            ],
        'War_Domain':True,
        'War_Priest':True,
        },
    'race':'Human-hero-big',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Goodberry':10,
        'Potion of Antidote':1,
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Plate Armor':1,
        'Heavy Shield':1,
        'Long Spear':1,
        'Longsword':1,
        },
    # TODO: ездовые животные -- волы
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Cleric 7 lvl (Vened) (Патрокл «Македонянин»)'] = {
    'level':7,
    'fireball_AI':True,
    'char_class':'Cleric',
    'hit_dice':'1d8',
    'behavior':'commander',
    'hitpoints_medial':True,
    #'hitpoints_base':8 + 18 + 4,
    'abilityes':{
        'strength':19,
        'dexterity':10,
        'constitution':12,
        'intelligence':10,
        'wisdom':18,
        'charisma':18,
        },
    'class_features':{
        # TODO: Channel_Guided_Strike
        'Feat_Inspiring_Leader':True,
        'Feat_Heavy_Armor_Master':True,
        'Spellcasting':True,
        'Spells':[
            ('cantrip', 'Mend'),
            ('cantrip', 'Thaumaturgy'),
            ('cantrip', 'Sacred_Flame'),
            ('cantrip', 'Spare_the_Dying'),
            ('ritual', 'Water_Walk'),
            ('ritual', 'Purify_Food_and_Drink'),
            ('1_lvl', 'Guiding_Bolt'),
            #('1_lvl', 'Shield_of_Faith'),
            ('1_lvl', 'Healing_Word'),
            ('2_lvl', 'Magic_Weapon'),
            ('2_lvl', 'Spiritual_Weapon'),
            ('2_lvl', 'Gentle_Repose'),
            ('2_lvl', 'Zone_of_Truth'),
            #('3_lvl', 'Spirit_Guardians'),
            ('3_lvl', 'Crusaders_Mantle'),
            ('3_lvl', 'Dispel_Magic'),
            ('3_lvl', 'Revivify'),
            #('3_lvl', 'Glyph_of_Warding'),
            ('4_lvl', 'Divination'),
            ('4_lvl', 'Stone_Shape'),
            ('4_lvl', 'Freedom_of_Movement'),
            ('4_lvl', 'Stoneskin'),
            ],
        'War_Domain':True,
        'War_Priest':True,
        'Channel_Turn_Undead':True,
        'Channel_Guided_Strike':True,
        },
    'race':'Human-hero-big',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Goodberry':10,
        'Potion of Antidote':1,
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Plate Armor':1,
        'Heavy Shield':1,
        'Long Spear':1,
        'Longsword +1':1,
        },
    # TODO: ездовые животные -- волы
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

#----
# Жрецы (свита) (Патрокл «Македонянин»):

metadict_chars['Druid 2 lvl (Vened) (друид Патрокла)'] = {
    'level':2,
    'char_class':'Druid',
    'abilityes_choice':['wisdom','strength','constitution','intelligence'],
    'hit_dice':'1d8',
    'behavior':'elite_warrior',
    'class_features':{
        'Feat_Healer':True,
        'Spellcasting':True,
        'Spells':[
            # Число заклинаний -- мод_мудрости + уровень_друида:
            ('cantrip', 'Druidcraft'),
            ('cantrip', 'Thorn_Whip'),
            ('1_lvl', 'Thunderwave'),
            ('1_lvl', 'Goodberry'),
            ('1_lvl', 'Healing_Word'),
            #('1_lvl', 'Fog_Cloud'),
            ],
        'Druidic_Language':True,
        'Wild_Shape':True,
        'Wild_Shape_Form':'Brown Bear (CR 1)',
        #'Wild_Shape_Form':'Giant Octopus (CR 1)',
        'Druid_Circle_Moon':True,
        'Combat_Wild_Shape':True,
        'Circle_Forms':True,
        },
    'race':'Human-hero-big',
    'weapon_skill':['simple','Scimitar'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Goodberry':10,
        'Potion of Antidote':1,
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Plate Armor':1,
        'Heavy Shield':1,
        'Longsword':1,
        'Long Spear':1,
        },
    # TODO: ездовые животные -- волы
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Druid 7 lvl (Vened) (Брат Патрокла)'] = {
    'level':7,
    'fireball_AI':True,
    'char_class':'Druid',
    'abilityes_choice':['wisdom','strength','constitution','intelligence'],
    'hit_dice':'1d8',
    'behavior':'commander',
    'hitpoints_medial':True,
    'abilityes':{
        'strength':20,
        'dexterity':10,
        'constitution':12,
        'intelligence':18,
        'wisdom':18,
        'charisma':10,
        },
    'class_features':{
        'Feat_Healer':True,
        'Feat_Heavy_Armor_Master':True,
        'Spellcasting':True,
        'Spells':[
            ('cantrip', 'Thorn_Whip'),
            ('cantrip', 'Mend'),
            ('cantrip', 'Druidcraft'),
            #('ritual', 'Speak_with_Animals'),
            #('ritual', 'Water_Breathing'),
            ('ritual', 'Water_Walk'),
            ('1_lvl', 'Thunderwave'),
            ('1_lvl', 'Goodberry'),
            #('1_lvl', 'Cure_Wounds'),
            ('1_lvl', 'Healing_Word'),
            ('2_lvl', 'Heat_Metal'),
            ('2_lvl', 'Flame_Blade'),
            ('2_lvl', 'Spike_Growth'),
            ('3_lvl', 'Dispel_Magic'),
            ('3_lvl', 'Wind_Wall'),
            ('3_lvl', 'Conjure_Animals'),
            ('4_lvl', 'Conjure_Woodlands_Beings'),
            ],
        'Druidic_Language':True,
        'Wild_Shape':True,
        'Wild_Shape_Form':'Brown Bear (CR 1)',
        #'Wild_Shape_Form':'Giant Octopus (CR 1)',
        'Druid_Circle_Moon':True,
        'Combat_Wild_Shape':True,
        'Wild_Shape_Improvement':True,
        },
    'race':'Human-hero-big',
    'weapon_skill':['simple','Scimitar'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Goodberry':10,
        'Potion of Antidote':1,
        'Infusion of Healing':1,
        'Rune of Shielding':1,
        'Rune of Absorbtion':1,
        'Plate Armor':1,
        'Heavy Shield':1,
        'Longsword +1':1,
        'Long Spear':1,
        },
    # TODO: ездовые животные -- волы
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

#----
# Сариссофоры (армия) (Патрокл «Македонянин»):

metadict_chars['Warrior 1 lvl (Vened) (сариссофор Патрокла)'] = {
    'level':1,
    'char_class':'Warrior',
    'behavior':'warrior',
    'hit_dice':'1d8',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Goodberry':1,
        'Potion of Bravery':1,
        'Potion of Antidote':1,
        'Chain Shirt':1,
        'Shortsword':1,
        'Heavy Shield':1,
        'Pike':1,
        },
    }

metadict_chars['Warrior 2 lvl (Vened) (ветеран Патрокла)'] = {
    'level':2,
    'char_class':'Warrior',
    'behavior':'elite_warrior',
    'hit_dice':'1d8',
    'class_features':{
        'Fighting_Style_Defence':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        # Длинные копья для подводного боя:
        'Goodberry':4,
        'Potion of Antidote':1,
        'Infusion of False Life':1,
        'Infusion of Healing':1,
        'Scale Mail':1,
        'Shortsword':1,
        'Heavy Shield':1,
        #'Pike':1,
        'Long Spear':1,
        },
    }

metadict_chars['Warrior 3 lvl (Vened) (сержант Патрокла)'] = {
    'level':3,
    'char_class':'Warrior',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Defence':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Goodberry':4,
        'Potion of Antidote':1,
        'Infusion of False Life':1,
        'Infusion of Healing':1,
        'Half Plate':1,
        'Shortsword':1,
        'Heavy Shield':1,
        #'Pike':1,
        'Long Spear':1,
        },
    }

metadict_chars['Warrior 4 lvl (Vened) (лейтенант Патрокла)'] = {
    'level':4,
    'char_class':'Warrior-officer',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Defence':True,
        'Feat_Inspiring_Leader':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Goodberry':4,
        'Potion of Antidote':1,
        'Infusion of False Life':1,
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Half Plate':1,
        'Shortsword':1,
        'Heavy Shield':1,
        #'Pike':1,
        'Long Spear':1,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Warrior 5 lvl (Vened) (капитан Патрокла)'] = {
    'level':5,
    'char_class':'Warrior-officer',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Defence':True,
        'Feat_Inspiring_Leader':True,
        'Extra_Attack':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Goodberry':4,
        'Potion of Antidote':1,
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Half Plate':1,
        'Shortsword':1,
        'Heavy Shield':1,
        #'Pike':1,
        'Long Spear':1,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

#----
# Жрецы (свита) (Фарам «Друг богов»):

metadict_chars['Cleric 2 lvl (Mordodrukow) (жрец Фарама) (боевой)'] = {
    # Домен бури.
    'level':2,
    'char_class':'Cleric',
    'abilityes_choice':['wisdom','strength','constitution','dexterity'],
    'hit_dice':'1d8',
    'behavior':'elite_warrior',
    'class_features':{
        'Feat_Heavy_Armor_Master':True,
        'Ability_Score_Improvement':{
            'strength':+1,
            },
        'Spellcasting':True,
        'Spells':[
            ('channel', 'Wrath_of_the_Storm'),
            ('cantrip', 'Mend'),
            ('cantrip', 'Sacred_Flame'),
            ('cantrip', 'Word_of_Radiance'),
            ('ritual', 'Detect_Magic'),
            ('1_lvl', 'Create_or_Destroy_Water'),
            ('1_lvl', 'Thunderwave'),
            ('1_lvl', 'Healing_Word'),
            ('1_lvl', 'Bless'),
            #('1_lvl', 'Shield_of_Faith'),
            ],
        'Tempest_Domain':True,
        'Wrath_of_the_Storm':True,
        'Channel_Destructive_Wrath':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Potion of Antidote':1,
        'Infusion of Longstrider':1,
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Plate Armor':1,
        'Heavy Shield':1,
        'Longsword':1,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Cleric 2 lvl (Mordodrukow) (жрец Фарама) (лекарь)'] = {
    'level':2,
    'char_class':'Cleric',
    'abilityes_choice':['wisdom','strength','constitution','dexterity'],
    'hit_dice':'1d8',
    'behavior':'elite_warrior',
    'class_features':{
        'Feat_Healer':True,
        'Spellcasting':True,
        'Spells':[
            ('channel', 'Wrath_of_the_Storm'),
            ('cantrip', 'Mend'),
            ('cantrip', 'Sacred_Flame'),
            ('cantrip', 'Spare_the_Dying'),
            ('ritual', 'Detect_Magic'),
            ('1_lvl', 'Create_or_Destroy_Water'),
            ('1_lvl', 'Thunderwave'),
            ('1_lvl', 'Healing_Word'),
            #('1_lvl', 'Bless'),
            ('1_lvl', 'Shield_of_Faith'),
            ],
        'Tempest_Domain':True,
        'Wrath_of_the_Storm':True,
        'Channel_Destructive_Wrath':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Potion of Antidote':1,
        'Infusion of Longstrider':1,
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Plate Armor':1,
        'Heavy Shield':1,
        'Longsword':1,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Fighter 2 lvl (Mordodrukow) (темплар Фарама)'] = {
    'level':2,
    'char_class':'Fighter',
    'hit_dice':'1d10',
    'behavior':'elite_warrior',
    'class_features':{
        'Feat_Heavy_Armor_Master':True,
        'Ability_Score_Improvement':{
            'strength':+1,
            },
        'Fighting_Style_Defence':True,
        'Second_Wind':True,
        'Action_Surge':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Potion of Antidote':1,
        'Infusion of Longstrider':1,
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Plate Armor':1,
        'Heavy Shield':1,
        'Longsword':1,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Fighter 2 lvl (Mordodrukow) (снайпер Фарама)'] = {
    'level':2,
    'archer_AI':True,
    'char_class':'Battlemaster',
    'abilityes_choice':['dexterity','constitution','strength'],
    'hit_dice':'1d10',
    'behavior':'elite_warrior',
    'class_features':{
        'Feat_Sharpshooter':True,
        'Fighting_Style_Archery':True,
        'Second_Wind':True,
        'Action_Surge':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'skills':[
        'Perception',
        ],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Potion of Antidote':1,
        'Infusion of Longstrider':1,
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Half Plate':1,
        'Shield':1,
        'Scimitar':1,
        'Longbow':1,
        'Arrow':40,
        },
    #'mount_combat':True,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Fighter 7 lvl (Mordodrukow) (Лонгин)'] = {
    # Лучник, мастер боевых искусств
    'level':7,
    'killer_AI':True,
    'archer_AI':True,
    'commando_AI':True,
    'squad_advantage':True,
    'char_class':'Battlemaster',
    'hit_dice':'1d10',
    'behavior':'commander',
    'hitpoints_medial':True,
    'abilityes':{
        'strength':13,
        'dexterity':20,
        'constitution':18,
        'intelligence':10,
        'wisdom':18,
        'charisma':10,
        },
    'class_features':{
        # TODO: отталкивающая атака вместо Menacing_Attack.
        'Feat_Resilient':'dexterity',
        'Feat_Sharpshooter':True,
        'Fighting_Style_Archery':True,
        'Second_Wind':True,
        'Action_Surge':True,
        'Martial_Archetype_Battlemaster':True,
        'Combat_Superiority':True,
        'Student_of_War':True,
        'Parry':True,
        'Menacing_Attack':True,
        'Precision_Attack':True,
        'Extra_Attack':True,
        'Spellcasting':True,
        'Feat_Magic_Initiate':True,
        'Spells':[
            ('cantrip', 'Minor_Illusion'),
            ('cantrip', 'Blade_Ward'),
            ('1_lvl', 'Hex'),
            ],
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Potion of Antidote':1,
        'Infusion of Heroism':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Studded Leather':1,
        'Heavy Shield':1,
        'Longbow +1':1,
        'Scimitar':1,
        'Arrow':120,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Cleric 7 lvl (Mordodrukow) (Фарам «Друг Богов»)'] = {
    'level':7,
    'killer_AI':True,
    'commando_AI':True,
    'fireball_AI':True,
    'squad_advantage':True,
    'char_class':'Cleric',
    'hit_dice':'1d8',
    'behavior':'commander',
    'hitpoints_medial':True,
    'abilityes':{
        'strength':18,
        'dexterity':10,
        'constitution':20,
        'intelligence':10,
        'wisdom':18,
        'charisma':14,
        },
    'class_features':{
        'Feat_Resilient':'constitution',
        'Spellcasting':True,
        'Spells':[
            ('channel', 'Wrath_of_the_Storm'),
            ('cantrip', 'Guidance'),
            ('cantrip', 'Thaumaturgy'),
            ('cantrip', 'Sacred_Flame'),
            ('cantrip', 'Word_of_Radiance'),
            ('1_lvl', 'Fog_Cloud'),
            ('1_lvl', 'Thunderwave'),
            ('2_lvl', 'Gust_of_Wind'),
            ('2_lvl', 'Shatter'),
            ('2_lvl', 'Aid'),
            ('2_lvl', 'Hold_Person'),
            ('2_lvl', 'Spiritual_Weapon'),
            ('2_lvl', 'Warding_Bond'),
            #('3_lvl', 'Call_Lightning'),
            ('3_lvl', 'Sleet_Storm'),
            ('3_lvl', 'Clairvoyance'),
            ('3_lvl', 'Dispel_Magic'),
            ('3_lvl', 'Sending'),
            ('3_lvl', 'Spirit_Guardians'),
            ('3_lvl', 'Water_Walk'),
            ('4_lvl', 'Ice_Storm'),
            ('4_lvl', 'Control_Water'),
            ('4_lvl', 'Divination'),
            ('4_lvl', 'Stone_Shape'),
            ],
        'Tempest_Domain':True,
        'Wrath_of_the_Storm':True,
        'Channel_Turn_Undead':True,
        'Channel_Destructive_Wrath':True,
        'Feat_Heavy_Armor_Master':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'skills':[
        # === Strength
        'Athletics',
        # === Intelligence
        'Religion',
        # === Wisdom
        'Insight',
        'Medicine',
        'Perception',
        # === Charisma
        'Persuasion',
        ],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        # TODO: жезл +1, увеличивает сложность спасброска заклинаний.
        #'Infusion of Healing':1,
        'Potion of Antidote':1,
        'Infusion of Heroism':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Plate Armor':1,
        'Heavy Shield':1,
        'Longsword +1':1,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

#----
# Лучники (армия) (Фарам):

metadict_chars['Warrior 1 lvl (Mordodrukow) (лучник Фарама)'] = {
    'level':1,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'archer',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Potion of Antidote':1,
        'Studded Leather':1,
        'Dagger':1,
        'Longbow':1,
        'Arrow':40,
        },
    }

metadict_chars['Warrior 2 lvl (Mordodrukow) (ветеран Фарама)'] = {
    'level':2,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'archer',
    'class_features':{
        'Fighting_Style_Archery':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Potion of Antidote':1,
        'Infusion of Healing':1,
        'Studded Leather':1,
        'Dagger':1,
        'Shield':1,
        'Longbow':1,
        'Arrow':40,
        },
    }

metadict_chars['Warrior 3 lvl (Mordodrukow) (сержант Фарама)'] = {
    'level':3,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Archery':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Potion of Antidote':1,
        'Infusion of Healing':1,
        'Breastplate':1,
        'Scimitar':1,
        'Shield':1,
        'Longbow':1,
        'Arrow':40,
        },
    }

metadict_chars['Warrior 4 lvl (Mordodrukow) (лейтенант Фарама)'] = {
    'level':4,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Archery':True,
        'Feat_Sharpshooter':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Potion of Antidote':1,
        'Infusion of Healing':1,
        'Rune of Shielding':1,
        'Rune of Absorbtion':1,
        'Half Plate':1,
        'Shield':1,
        'Scimitar':1,
        'Longbow':1,
        'Arrow':40,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{},
    }

metadict_chars['Warrior 5 lvl (Mordodrukow) (капитан Фарама)'] = {
    'level':5,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Archery':True,
        'Feat_Sharpshooter':True,
        'Extra_Attack':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Potion of Antidote':1,
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Half Plate':1,
        'Shield':1,
        'Scimitar':1,
        'Longbow':1,
        'Arrow':40,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{},
    }

#----
# Бойцы (свита) (Гай Юлий):

metadict_chars['Fighter 1 lvl (Katorjnik) (преторианец Гая Юлия)'] = {
    # Преторианцы, всадники.
    'level':1,
    'char_class':'Fighter',
    'abilityes_choice':['strength','charisma','constitution','wisdom'],
    'hit_dice':'1d10',
    'behavior':'elite_warrior',
    'class_features':{
        # Халявный Feat_Mounted_Combatant:
        'Feat_Inspiring_Leader':True,
        'Feat_Mounted_Combatant':True,
        'Fighting_Style_Protection':True,
        'Second_Wind':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Potion of Antidote':1,
        'Infusion of Healing':1,
        'Splint Armor':1,
        'Shield':1,
        'Longsword':1,
        'Lance':1,
        'Pilum':6,
        },
    'mount_combat':True,
    'mount_type':'Warhorse',
    'equipment_mount':{
        },
    }

metadict_chars['Fighter 2 lvl (Katorjnik) (преторианец Гая Юлия)'] = {
    # Преторианцы, всадники.
    'level':2,
    'char_class':'Fighter',
    'abilityes_choice':['strength','charisma','constitution','wisdom'],
    'hit_dice':'1d10',
    'behavior':'elite_warrior',
    'class_features':{
        # Халявный Feat_Mounted_Combatant:
        'Feat_Inspiring_Leader':True,
        'Feat_Mounted_Combatant':True,
        'Fighting_Style_Protection':True,
        'Second_Wind':True,
        'Action_Surge':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Potion of Antidote':1,
        'Infusion of Longstrider':1,
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Plate Armor':1,
        'Heavy Shield':1,
        'Longsword':1,
        'Lance':1,
        'Pilum':6,
        },
    'mount_combat':True,
    'mount_type':'Warhorse',
    'equipment_mount':{
        'Horse Scale Mail':1,
        },
    }

metadict_chars['Fighter 7 lvl (Katorjnik) (Гай Юлий)'] = {
    'level':7,
    'char_class':'Fighter',
    'hit_dice':'1d10',
    'behavior':'commander',
    'hitpoints_medial':True,
    'abilityes':{
        'strength':20,
        'dexterity':10,
        'constitution':14,
        'intelligence':14,
        'wisdom':18,
        'charisma':16,
        },
    'class_features':{
        'Feat_Inspiring_Leader':True,
        'Feat_Mounted_Combatant':True,
        'Fighting_Style_Protection':True,
        'Second_Wind':True,
        'Action_Surge':True,
        'Martial_Archetype_Champion':True,
        'Champion_Improved_Critical':True,
        'Feat_Heavy_Armor_Master':True,
        'Extra_Attack':True,
        'Remarkable_Athlete':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        #'Infusion of Regeneration':1,
        'Potion of Antidote':1,
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Plate Armor':1,
        'Heavy Shield':1,
        'Sword of Life-Stealing':1,
        #'Longsword +1':1,
        'Lance':1,
        'Pilum':6,
        },
    'mount_combat':True,
    'mount_type':'Warhorse',
    'equipment_mount':{
        'Horse Scale Mail':1,
        },
    }

#----
# Легионеры (армия) (Гай Юлий):

metadict_chars['Warrior 1 lvl (Katorjnik) (манипуларий)'] = {
    # Исторически носили по 2 пилума, но шесть весомее (вот только пехота столько не унесёт).
    'level':1,
    'char_class':'Warrior',
    'hit_dice':'1d8',
    'behavior':'warrior',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Potion of Antidote':1,
        'Studded Leather':1,
        'Heavy Shield':1,
        'Shortsword':1,
        'Pilum':7,
        },
    }

metadict_chars['Warrior 2 lvl (Katorjnik) (ветеран) (кольчуга)'] = {
    'level':2,
    'char_class':'Warrior',
    'hit_dice':'1d8',
    'behavior':'warrior',
    'class_features':{
        'Fighting_Style_Protection':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Potion of Antidote':1,
        'Chain Shirt':1,
        'Heavy Shield':1,
        'Shortsword':1,
        'Pilum':7,
        },
    }

metadict_chars['Warrior 2 lvl (Katorjnik) (ветеран)'] = {
    'level':2,
    'char_class':'Warrior',
    'hit_dice':'1d8',
    'behavior':'elite_warrior',
    'class_features':{
        'Fighting_Style_Protection':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Potion of Antidote':1,
        'Scale Mail':1,
        'Heavy Shield':1,
        'Shortsword':1,
        'Pilum':2,
        },
    }

metadict_chars['Warrior 3 lvl (Katorjnik) (урагос)'] = {
    # Десятник (декан, урагос)
    'level':3,
    'char_class':'Warrior',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Protection':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Potion of Antidote':1,
        'Infusion of Healing':1,
        'Breastplate':1,
        'Heavy Shield':1,
        'Shortsword':1,
        'Pilum':7,
        },
    }

metadict_chars['Warrior 4 lvl (Katorjnik) (опцион)'] = {
    'level':4,
    'char_class':'Warrior-officer',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Defence':True,
        'Feat_Inspiring_Leader':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Potion of Antidote':1,
        'Infusion of Healing':1,
        'Rune of Shielding':1,
        'Breastplate':1,
        'Heavy Shield':1,
        'Shortsword':1,
        'Pilum':7,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Warrior 5 lvl (Katorjnik) (центурион)'] = {
    'level':5,
    'char_class':'Warrior-officer',
    'hit_dice':'1d8',
    #'carefull_AI':True,
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Defence':True,
        'Feat_Inspiring_Leader':True,
        'Extra_Attack':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Potion of Antidote':1,
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Half Plate':1,
        'Heavy Shield':1,
        'Shortsword':1,
        'Pilum':3,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

#----
# Следопыты (свита) (Сакатр Ка'Ален):

metadict_chars['Ranger 2 lvl (Gogan) (следопыт Сакатра)'] = {
    'level':2,
    'char_class':'Ranger',
    'hit_dice':'1d10',
    'behavior':'archer',
    'class_features':{
        'Feat_Sharpshooter':True,
        'Favored_Enemy':['humans'],
        'Natural_Explorer':['sea'],
        'Spellcasting':True,
        'Spells':[
            ('1_lvl', 'Fog_Cloud'),
            ('1_lvl', 'Hail_of_Thorns'),
            ],
        'Fighting_Style_Archery':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Goodberry':5,
        'Potion of Antidote':1,
        'Infusion of Healing':1,
        'Infusion of Longstrider':1,
        'Rune of Absorbtion':1,
        'Breastplate':1,
        'Shield':1,
        'Shortsword':1,
        'Longbow':1,
        'Arrow':40,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Ranger 7 lvl (Gogan) (Сакатр Ка-Ален)'] = {
    'level':7,
    'brave_AI':True,
    'archer_AI':True,
    #'killer_AI':True,
    'char_class':'Ranger',
    'hit_dice':'1d10',
    'behavior':'commander',
    'hitpoints_medial':True,
    'abilityes':{
        'strength':11,
        'dexterity':20,
        'constitution':14,
        'intelligence':14,
        'wisdom':16,
        'charisma':17,
        },
    'class_features':{
        # TODO: Сделай Hunter_Steel_Will -- преимущество на спасброски против испуга
        'Feat_Sharpshooter':True,
        'Favored_Enemy':['humans', 'sea_monsters'],
        'Natural_Explorer':['sea', 'coast'],
        'Spellcasting':True,
        'Spells':[
            # TODO: сделай Spike_Growth
            ('ritual', 'Animal_Messenger'),
            ('1_lvl', 'Goodberry'),
            ('1_lvl', 'Fog_Cloud'),
            ('1_lvl', 'Hail_of_Thorns'),
            ('2_lvl', 'Pass_Without_Trace'),
            #('2_lvl', 'Spike_Growth'),
            ],
        'Fighting_Style_Archery':True,
        'Primeval_Awareness':True,
        'Ranger_Archetype_Hunter':True,
        'Hunter_Horde_Breaker':True,
        'Hunter_Steel_Will':True,
        'Extra_Attack':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Goodberry':15,
        'Potion of Antidote':1,
        'Infusion of Healing':1,
        'Infusion of Longstrider':1,
        'Rune of Shielding':1,
        'Studded Leather':1,
        'Shield':1,
        'Scimitar':1,
        'Longbow +1':1,
        'Arrow':40,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

#----
# Пираты (армия) (Сакатр Ка'Ален):

metadict_chars['Warrior 1 lvl (Gogan) (кимерийский пират)'] = {
    'level':1,
    'char_class':'Warrior-pirate',
    'hit_dice':'1d8',
    'behavior':'warrior',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Potion of Antidote':1,
        'Studded Leather':1,
        'Shield':1,
        'Shortsword':1,
        'Shortbow':1,
        'Arrow':40,
        },
    }

metadict_chars['Warrior 2 lvl (Gogan) (кимерийский пират-ветеран)'] = {
    'level':2,
    'char_class':'Warrior-pirate',
    'hit_dice':'1d8',
    'behavior':'elite_warrior',
    'class_features':{
        'Fighting_Style_Archery':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Potion of Antidote':1,
        'Scale Mail':1,
        'Shield':1,
        'Rapier':1,
        'Dagger':1,
        'Shortbow':1,
        'Arrow':40,
        },
    }

metadict_chars['Warrior 3 lvl (Gogan) (кимерийский пират-сержант)'] = {
    'level':3,
    'char_class':'Warrior-pirate',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Archery':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Potion of Antidote':1,
        'Infusion of Healing':1,
        'Breastplate':1,
        'Shield':1,
        'Rapier':1,
        'Dagger':1,
        'Shortbow':1,
        'Arrow':40,
        },
    }

metadict_chars['Warrior 4 lvl (Gogan) (кимерийский пират-лейтенант)'] = {
    'level':4,
    'char_class':'Warrior-pirate',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Archery':True,
        'Feat_Inspiring_Leader':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Potion of Antidote':1,
        'Infusion of Healing':1,
        'Rune of Shielding':1,
        'Breastplate':1,
        'Shield':1,
        'Rapier':1,
        'Dagger':1,
        'Shortbow':1,
        'Arrow':40,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Warrior 5 lvl (Gogan) (кимерийский пират-капитан)'] = {
    'level':5,
    #'volley_AI':True,
    'char_class':'Warrior-pirate',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Archery':True,
        'Feat_Inspiring_Leader':True,
        'Extra_Attack':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Potion of Antidote':1,
        'Infusion of Healing':1,
        'Rune of Shielding':1,
        'Breastplate':1,
        'Shield':1,
        'Rapier':1,
        'Dagger':1,
        'Shortbow':1,
        'Arrow':40,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

#----
# Враги (герои) (кара'Ям):

metadict_chars['Warlock 1 lvl (враг) (колдун Кара\'Яма)'] = {
    'level':1,
    'char_class':'Warlock',
    'hit_dice':'1d8',
    'behavior':'archer',
    'class_features':{
        'Feat_Mounted_Combatant':True,
        'Otherworldly_Patron':True,
        'Otherworldly_Patron_The_Fiend':True,
        'Pact_Magic':True,
        'Spells':[
            ('cantrip', 'Eldritch_Blast'),
            ('cantrip', 'Create_Bonfire'),
            ('ritual', 'Unseen_Servant'),
            ('1_lvl', 'Burning_Hands'),
            ('1_lvl', 'Hex'),
            ],
        'Dark_One\'s_Blessing':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple'],
    'armor_skill':['light'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Armor':1,
        'Dagger':1,
        'Shortbow':1,
        'Arrow':40,
        },
    'mount_combat':True,
    'mount_type':'Horseclaw',
    'equipment_mount':{
        },
    }

metadict_chars['Warlock 5 lvl (враг) (Кара\'Ям)'] = {
    # Свободно накладывает на себя смену облика: Invocation_Mask_of_Many_Faces
    # Игнорирует сопротивление огню: Feat_Elemental_Adept
    'level':5,
    'fireball_AI':True,
    'char_class':'Warlock',
    'hit_dice':'1d8',
    'behavior':'commander',
    'hitpoints_medial':True,
    'abilityes':{
        'strength':10,
        'dexterity':18,
        'constitution':14,
        'intelligence':16,
        'wisdom':8,
        'charisma':18,
        },
    'class_features':{
        'Feat_Mounted_Combatant':True,
        'Otherworldly_Patron':True,
        'Otherworldly_Patron_The_Fiend':True,
        'Pact_Magic':True,
        'Spells':[
            # Unseen_Servant для разминирования. Для учеников.
            # Burning_Hands для учеников.
            # TODO: Сделай Green_Flame_Blade.
            ('cantrip', 'Eldritch_Blast'),
            ('cantrip', 'Create_Bonfire'),
            ('cantrip', 'Minor_Illusion'),
            ('ritual', 'Detect_Magic'),
            ('ritual', 'Unseen_Servant'),
            ('3_lvl', 'Burning_Hands'),
            ('3_lvl', 'Invisibility'),
            ('3_lvl', 'Suggestion'),
            ('3_lvl', 'Earthbind'),
            ('3_lvl', 'Fireball'),
            ('3_lvl', 'Fly'),
            ],
        'Dark_One\'s_Blessing':True,
        'Eldritch_Invocations':True,
        'Invocation_Eldritch_Spear':True,
        'Invocation_Agonizing_Blast':True,
        'Invocation_Mask_of_Many_Faces':True,
        'Pact_Boon':True,
        'Pact_of_the_Blade':True,
        'Feat_Elemental_Adept':'fire',
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        # Добряника от друида Тик-Бо:
        # Договор клинка, оружие +1.
        'Goodberry':30,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Rune of Armor':1,
        'Shortsword +1':1,
        'Shortbow +1':1,
        'Arrow':40,
        },
    'mount_combat':True,
    'mount_type':'Horseclaw',
    'equipment_mount':{
        },
    }

#----
# Враги (герои) (Кема'Эш):

metadict_chars['Warlock 1 lvl (враг) (колдун Кема\'Эша)'] = {
    'level':1,
    'char_class':'Warlock',
    'hit_dice':'1d8',
    'behavior':'archer',
    'class_features':{
        'Feat_Mounted_Combatant':True,
        'Otherworldly_Patron':True,
        'Otherworldly_Patron_The_Fiend':True,
        'Pact_Magic':True,
        'Spells':[
            ('cantrip', 'Eldritch_Blast'),
            ('cantrip', 'Create_Bonfire'),
            ('1_lvl', 'Charm_Person'),
            ('1_lvl', 'Burning_Hands'),
            ('1_lvl', 'Hex'),
            ],
        'Dark_One\'s_Blessing':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple'],
    'armor_skill':['light'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Armor':1,
        'Dagger':1,
        'Shortbow':1,
        'Arrow':40,
        },
    'mount_combat':True,
    'mount_type':'Horseclaw',
    'equipment_mount':{
        },
    }

metadict_chars['Warlock 5 lvl (враг) (Кема\'Эш)'] = {
    # Атакует издалека: Invocation_Eldritch_Spear.
    # Воодушевляет своих: Feat_Inspiring_Leader.
    # Передаёт команды с помощью Dancing_Lights и Message.
    'level':5,
    'fireball_AI':True,
    'char_class':'Warlock',
    'hit_dice':'1d8',
    'behavior':'commander',
    'hitpoints_medial':True,
    'abilityes':{
        'strength':10,
        'dexterity':16,
        'constitution':12,
        'intelligence':14,
        'wisdom':16,
        'charisma':18,
        },
    'class_features':{
        'Feat_Mounted_Combatant':True,
        'Otherworldly_Patron':True,
        'Otherworldly_Patron_The_Fiend':True,
        'Pact_Magic':True,
        'Spells':[
            ('cantrip', 'Eldritch_Blast'),
            ('cantrip', 'Minor_Illusion'),
            ('cantrip', 'Prestidigitation'),
            ('cantrip', 'Dancing_Lights'),
            ('cantrip', 'Message'),
            ('ritual', 'Detect_Magic'),
            ('ritual', 'Identify'),
            ('3_lvl', 'Charm_Person'),
            ('3_lvl', 'Hex'),
            ('3_lvl', 'Burning_Hands'),
            ('3_lvl', 'Summon_Lesser_Demons'),
            ('3_lvl', 'Fly'),
            ],
        'Dark_One\'s_Blessing':True,
        'Eldritch_Invocations':True,
        'Invocation_Agonizing_Blast':True,
        'Invocation_Eldritch_Spear':True,
        'Invocation_Book_of_Ancient_Secrets':True,
        'Pact_Boon':True,
        'Pact_of_the_Tome':True,
        'Feat_Inspiring_Leader':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Goodberry':30,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Rune of Armor':1,
        'Dagger':1,
        'Shortbow +1':1,
        'Arrow':40,
        },
    'mount_combat':True,
    'mount_type':'Horseclaw',
    'equipment_mount':{
        },
    }

#----
# Враги (герои) (Энзиф):

metadict_chars['Ranger 1 lvl (враг) (следопыт Энзифа)'] = {
    'level':1,
    'char_class':'Ranger',
    'hit_dice':'1d10',
    'behavior':'archer',
    'class_features':{
        'Feat_Sharpshooter':True,
        'Favored_Enemy':['humans'],
        'Natural_Explorer':['forest'],
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Studded Leather':1,
        'Shield':1,
        'Shortsword':1,
        'Longbow':1,
        'Arrow':40,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Ranger 5 lvl (враг) (Энзиф «Ходи-гора»)'] = {
    'level':5,
    'char_class':'Ranger',
    'hit_dice':'1d10',
    'behavior':'commander',
    'hitpoints_medial':True,
    'abilityes':{
        'strength':18,
        'dexterity':18,
        'constitution':16,
        'intelligence':8,
        'wisdom':12,
        'charisma':14,
        },
    'class_features':{
        'Feat_Sharpshooter':True,
        'Favored_Enemy':['humans'],
        'Natural_Explorer':['forest'],
        'Spellcasting':True,
        'Spells':[
            ('ritual', 'Animal_Messenger'),
            ('1_lvl', 'Absorb_Elements'),
            ('2_lvl', 'Pass_Without_Trace'),
            ('2_lvl', 'Find_Traps'),
            ('2_lvl', 'Spike_Growth'),
            ],
        'Fighting_Style_Archery':True,
        'Primeval_Awareness':True,
        'Ranger_Archetype_Hunter':True,
        'Hunter_Horde_Breaker':True,
        'Feat_Great_Weapon_Master':True,
        'Extra_Attack':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Studded Leather':1,
        'Shield':1,
        'Shortsword':1,
        'Longbow +1':1,
        'Arrow':40,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

#----
# Враги (герои) (Магор):

metadict_chars['Paladin 1 lvl (враг) (паладин Магора)'] = {
    'level':1,
    'char_class':'Paladin',
    'hit_dice':'1d10',
    'behavior':'elite_warrior',
    'class_features':{
        'Feat_Tough':True,
        'Feat_Heavy_Armor_Master':True,
        'Ability_Score_Improvement':{
            'strength':+1,
            },
        'Divine_Sense':True,
        'Lay_on_Hands':True,
        },
    'race':'Human-hero-big',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Splint Armor':1,
        'Heavy Shield':1,
        'Flait':1,
        'Long Spear':1,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Paladin 5 lvl (враг) (Магор «Детоед»)'] = {
    'level':5,
    'char_class':'Paladin',
    'hit_dice':'1d10',
    'behavior':'commander',
    #'fearless_AI':True,
    'killer_AI':True,
    'hitpoints_medial':True,
    'abilityes':{
        'strength':18,
        'dexterity':10,
        'constitution':18,
        'intelligence':10,
        'wisdom':12,
        'charisma':18,
        },
    'class_features':{
        # TODO: Сделай Feat_Shield_Master.
        'Feat_Tough':True,
        'Feat_Heavy_Armor_Master':True,
        'Ability_Score_Improvement':{
            'strength':+3,
            },
        'Divine_Sense':True,
        'Lay_on_Hands':True,
        'Fighting_Style_Defence':True,
        'Divine_Smite':True,
        'Spellcasting':True,
        'Spells':[
            ('channel', 'Sacred_Weapon'),
            ('1_lvl', 'Divine_Smite'),
            ('2_lvl', 'Divine_Smite'),
            ('1_lvl', 'Bless'),
            ('1_lvl', 'Heroism'),
            ('1_lvl', 'Shield_of_Faith'),
            ('1_lvl', 'Protection_from_Evil_and_Good'),
            ('1_lvl', 'Sanctuary'),
            ('1_lvl', 'Command'),
            ('2_lvl', 'Lesser_Restoration'),
            ('2_lvl', 'Zone_of_Truth'),
            ('2_lvl', 'Find_Steed'),
            ],
        'Divine_Health':True,
        'Oath_of_Devotion':True,
        'Channel_Turn_The_Unholy':True,
        'Channel_Sacred_Weapon':True,
        'Extra_Attack':True,
        },
    'race':'Human-hero-big',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':2,
        'Rune of Absorbtion':1,
        'Splint Armor':1,
        'Heavy Shield':1,
        'Flait +1':1,
        'Long Spear':1,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

#----
# Враги (герои) (Хана'Вам):

metadict_chars['Fighter 1 lvl (враг) (снайпер Хана\'Вама)'] = {
    # Снайперы, корректируют "Град стрел" ополчения.
    'level':1,
    'char_class':'Battlemaster',
    'abilityes_choice':['dexterity','constitution','strength','charisma'],
    'hit_dice':'1d10',
    'behavior':'archer',
    'class_features':{
        'Feat_Sharpshooter':True,
        'Fighting_Style_Archery':True,
        'Second_Wind':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'skills':[
        'Perception',
        ],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Rune of Armor':1,
        'Shield':1,
        'Shortsword':1,
        'Longbow':1,
        'Arrow':40,
        },
    'mount_combat':True,
    'mount_type':'Riding Horse',
    'equipment_mount':{
        },
    }

metadict_chars['Fighter 5 lvl (враг) (Хана\'Вам)'] = {
    # Лучник-чемпион
    'level':5,
    'char_class':'Battlemaster',
    'abilityes_choice':['dexterity','constitution','strength','charisma'],
    'hit_dice':'1d10',
    'behavior':'commander',
    'killer_AI':True,
    'hitpoints_medial':True,
    'abilityes':{
        'strength':12,
        'dexterity':20,
        'constitution':12,
        'intelligence':16,
        'wisdom':10,
        'charisma':16,
        },
    'class_features':{
        'Feat_Sharpshooter':True,
        'Fighting_Style_Archery':True,
        'Second_Wind':True,
        'Action_Surge':True,
        'Martial_Archetype_Champion':True,
        'Champion_Improved_Critical':True,
        'Feat_Inspiring_Leader':True,
        'Extra_Attack':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Shielding':1,
        'Rune of Armor':1,
        'Shield':1,
        'Scimitar +1':1,
        'Longbow +1':1,
        'Arrow':40,
        },
    'mount_combat':True,
    'mount_type':'Riding Horse',
    'equipment_mount':{
        },
    }

#----
# Враги (герои) (Тик-Бо):

metadict_chars['Druid 1 lvl (враг) (друид Тик-Бо)'] = {
    # На них "Водное дыхание" или "Хождение по воде"
    'level':1,
    'water_walk':True,
    'char_class':'Druid',
    'hit_dice':'1d8',
    'behavior':'archer',
    'class_features':{
        'Feat_Healer':True,
        'Spellcasting':True,
        'Spells':[
            # Число заклинаний -- мод_мудрости + уровень_друида:
            # Goodberry -- 2 слота = 20 хитов на завтра. 20 друидов 2 lvl = 600 хитов лечения.
            ('cantrip', 'Druidcraft'),
            ('cantrip', 'Mold_Earth'),
            #('cantrip', 'Magic_Stone'),
            #('ritual', 'Speak_with_Animals'),
            ('1_lvl', 'Healing_Word'),
            ('1_lvl', 'Entangle'),
            ('1_lvl', 'Fog_Cloud'),
            ('1_lvl', 'Goodberry'),
            ],
        'Druidic_Language':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','Scimitar'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Armor':1,
        'Heavy Shield':1,
        'Club':1,
        'Sling real':1,
        'Sling Bullet':10,
        },
    'mount_combat':True,
    'mount_type':'Riding Horse',
    'equipment_mount':{
        },
    }

metadict_chars['Druid 5 lvl (враг) (Тик-Бо «Робкий»)'] = {
    # Пацифист, призыватель зверей.
    'level':5,
    'fireball_AI':True,
    'water_walk':True,
    'char_class':'Druid',
    'hit_dice':'1d8',
    'behavior':'commander',
    #'fearless_AI':True,
    'hitpoints_medial':True,
    'abilityes':{
        'strength':10,
        'dexterity':14,
        'constitution':14,
        'intelligence':16,
        'wisdom':18,
        'charisma':14,
        },
    'class_features':{
        'Feat_Healer':True,
        'Spellcasting':True,
        'Spells':[
            ('cantrip', 'Druidcraft'),
            ('cantrip', 'Mold_Earth'),
            ('cantrip', 'Guidance'),
            ('ritual', 'Speak_with_Animals'),
            ('ritual', 'Water_Breathing'),
            ('ritual', 'Water_Walk'),
            ('1_lvl', 'Entangle'),
            ('1_lvl', 'Absorb_Elements'),
            ('2_lvl', 'Pass_Without_Trace'),
            ('2_lvl', 'Lesser_Restoration'),
            ('2_lvl', 'Healing_Spirit'),
            ('3_lvl', 'Conjure_Animals'),
            ('3_lvl', 'Plant_Growth'),
            ],
        'Druidic_Language':True,
        'Wild_Shape':True,
        'Druid_Circle_Forest':True,
        'Natural_Recovery':True,
        'Wild_Shape_Improvement':True,
        'Ability_Score_Improvement':{
            'wisdom':+2,
            },
        },
    'race':'Human-hero',
    'weapon_skill':['simple','Scimitar'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Goodberry':30,
        'Infusion of Healing':1,
        'Rune of Shielding':1,
        'Rune of Armor':1,
        'Heavy Shield':1,
        'Club':1,
        'Sling real':1,
        'Sling Bullet':10,
        },
    'mount_combat':True,
    'mount_type':'Riding Horse',
    'equipment_mount':{
        },
    }

#----
# Враги (армии) (демоны Кема'Эша):

metadict_chars['Commoner 1 lvl (враг) (карл)'] = {
    # Карлы с дубинками. Ничего особенного, только шкуры у них крепкие.
    'level':1,
    'char_class':'Commoner',
    'behavior':'warrior',
    'hit_dice':'1d8',
    'race':'Primevial-medium',
    'weapon_skill':['simple'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':militia_pack,
    'equipment_weapon':{
        'Mace':1,
        'Shield':1,
        'Javelin':6,
        },
    }

metadict_chars['Commoner 1 lvl (враг) (карл-ветеран)'] = {
    'level':2,
    'char_class':'Commoner',
    'behavior':'warrior',
    'hit_dice':'1d8',
    'race':'Primevial-medium',
    'weapon_skill':['simple'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':militia_pack,
    'equipment_weapon':{
        'Mace':1,
        'Shield':1,
        'Javelin':6,
        },
    }

metadict_chars['Warrior 3 lvl (враг) (демон Кема\'Эша)'] = {
    # Опасный гад.
    'level':3,
    #'fearless_AI':True,
    'seeker_AI':True,
    'killer_AI':True,
    'char_class':'Warrior-officer',
    'behavior':'commander',
    'class_features':{
        'Regeneration':3,
        },
    'hitpoints_medial':True,
    'abilityes':{
        'strength':18,
        'dexterity':14,
        'constitution':18,
        'intelligence':10,
        'wisdom':12,
        'charisma':16,
        },
    'hit_dice':'1d10',
    'race':'Primevial-large',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':militia_pack,
    'equipment_weapon':{
        'Battleaxe':1,
        'Shield':1,
        'Javelin':6,
        },
    }

#----
# Нейтралы (свита) (волшебники Менона):

metadict_chars['Wizard 4 lvl (нейтрал) (волшебник Менона)'] = {
    'level':4,
    'archer_AI':True,
    'fireball_AI':True,
    'char_class':'Wizard',
    'hit_dice':'1d6',
    'behavior':'commander',
    'class_features':{
        'Feat_Resilient':'constitution',
        'Ability_Score_Improvement':{
            'constitution':+1,
            'intelligence':+2,
            },
        'Arcane_Recovery':True,
        'Spellcasting':True,
        'Spells':[
            # Уровень_персонажа + мод_интеллекта (8 заклинаний)
            ('cantrip', 'Prestidigitation'),
            ('cantrip', 'Shape_Water'),
            ('cantrip', 'Mold_Earth'),
            ('cantrip', 'Message'),
            # Ритуалы из книги заклинаний:
            ('ritual', 'Alarm'),
            ('ritual', 'Identify'),
            ('ritual', 'Detect_Magic'),
            ('ritual', 'Unseen_Servant'),
            ('ritual', 'Gentle_Repose'),
            ('ritual', 'Find_Familiar'),
            ('ritual', 'Comprehend_Languages'),
            ('1_lvl', 'Shield'),
            ('1_lvl', 'Fog_Cloud'),
            ('1_lvl', 'Magic_Missile'),
            ('1_lvl', 'Absorb_Elements'),
            ('2_lvl', 'Warding_Wind'),
            ('2_lvl', 'Invisibility'),
            ('2_lvl', 'Flaming_Sphere'),
            ('2_lvl', 'See_Invisibility'),
            #('2_lvl', 'Dragon_Breath'),
            #('2_lvl', 'Suggestion'),
            #('2_lvl', 'Shatter'),
            ],
        # TODO:
        # - Grim_Harvest -- лечение x2 круг заклинания, или x3, если некромантия.
        'School_of_Necromancy':True,
        'Grim_Harvest':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple'],
    'armor_skill':[],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Rune of Armor':1,
        'Dagger':1,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Wizard 12 lvl (нейтрал) (Менон Теварин)'] = {
    # Wizard 1 lvl (otherworld mage-disciple) sum:100 STR:16 DEX:17 CON:17 INT:19 WIS:17 CHA:14
    # "Предосторожность" (Contingency) хранит заклинание Otiluke_Resilent_Sphere, или Wall_of_Force.
    # "Feat_Alert", -- нельзя застать врасплох. "Feat_Keen_Mind" -- помнит всё.
    'level':12,
    'fireball_AI':True,
    'disengage_AI':True,
    'char_class':'Wizard',
    'hit_dice':'1d6',
    'behavior':'commander',
    'hitpoints_medial':True,
    'abilityes':{
        'strength':16,
        'dexterity':17,
        'constitution':17,
        'intelligence':19,
        'wisdom':17,
        'charisma':14,
        },
    'class_features':{
        'Feat_Alert':True,
        'Feat_Keen_Mind':True,
        'Feat_Resilient':'constitution',
        'Ability_Score_Improvement':{
            'dexterity':+1,
            'constitution':+1,
            'intelligence':+1,
            'wisdom':+1,
            },
        'Arcane_Recovery':True,
        'Spellcasting':True,
        'Spells':[
            # Уровень_персонажа + мод_интеллекта (17 заклинаний)
            ('cantrip', 'Prestidigitation'),
            ('cantrip', 'Shape_Water'),
            ('cantrip', 'Mold_Earth'),
            ('cantrip', 'Message'),
            ('cantrip', 'Minor_Illusion'),
            # Ритуалы из книги заклинаний:
            ('ritual', 'Alarm'),
            ('ritual', 'Identify'),
            ('ritual', 'Detect_Magic'),
            ('ritual', 'Unseen_Servant'),
            ('ritual', 'Gentle_Repose'),
            ('ritual', 'Find_Familiar'),
            ('ritual', 'Comprehend_Languages'),
            ('ritual', 'Feign_Death'),
            ('ritual', 'Water_Breathing'),
            ('ritual', 'Leomund_Tiny_Hut'),
            ('ritual', 'Rary_Telepathic_Bond'),
            ('ritual', 'Contact_Other_Plane'),
            # Для свиты:
            ('1_lvl', 'Shield'),
            ('1_lvl', 'Fog_Cloud'),
            ('1_lvl', 'Magic_Missile'),
            ('1_lvl', 'Absorb_Elements'),
            ('2_lvl', 'Warding_Wind'),
            ('2_lvl', 'Invisibility'),
            ('2_lvl', 'Flaming_Sphere'),
            ('2_lvl', 'See_Invisibility'),
            #('2_lvl', 'Dragon_Breath'),
            #('2_lvl', 'Suggestion'),
            #('2_lvl', 'Shatter'),
            # Личные (9 заклинаний):
            ('3_lvl', 'Counterspell'),
            ('3_lvl', 'Fireball'),
            ('3_lvl', 'Sending'),
            ('4_lvl', 'Fabricate'),
            ('4_lvl', 'Dimension_Door'),
            ('5_lvl', 'Teleportation_Circle'),
            ('5_lvl', 'Animated_Objects'),
            ('5_lvl', 'Cone_of_Cold'),
            ('6_lvl', 'Soul_Cage'),
            # ----
            #('3_lvl', 'Blink'),
            #('3_lvl', 'Animate_Dead'),
            #('3_lvl', 'Dispel_Magic'),
            #('3_lvl', 'Vampiric_Touch'),
            #('3_lvl', 'Melf_Minute_Meteors'),
            # ----
            #('4_lvl', 'Stoneskin'),
            #('4_lvl', 'Arcane_Eye'),
            #('4_lvl', 'Control_Water'),
            #('4_lvl', 'Leomund_Secret_Chest'),
            #('4_lvl', 'Otiluke_Resilent_Sphere'),
            #('4_lvl', 'Mordenkainen_Private_Sanctum'),
            #('4_lvl', 'Conjure_Minor_Elementals'),
            #('4_lvl', 'Sickening_Radiance'),
            #('4_lvl', 'Ice_Storm'),
            #('4_lvl', 'Banishment'),
            # ----
            #('5_lvl', 'Enervation'),
            #('5_lvl', 'Cone_of_Cold'),
            #('5_lvl', 'Danse_Macabre'),
            #('5_lvl', 'Negative_Energy_Flood'),
            #('5_lvl', 'Conjure_Elemental'),
            #('5_lvl', 'Wall_of_Force'),
            #('5_lvl', 'Cloudkill'),
            #('5_lvl', 'Passwall'),
            #('5_lvl', 'Scrying'),
            # ----
            #('6_lvl', 'Create_Undead'),
            #('6_lvl', 'Circle_of_Death'),
            #('6_lvl', 'Programmed_Illusion'),
            #('6_lvl', 'Arcane_Gate'),
            #('6_lvl', 'True_Seeing'),
            #('6_lvl', 'Magic_Jar'),
            #('6_lvl', 'Contingency'),
            #('6_lvl', 'Create_Undead'),
            ],
        # TODO:
        # - Grim_Harvest -- лечение x2 круг заклинания, или x3, если некромантия.
        # - Undead_Thralls -- 2 цели "Animate_Dead", +уровень_мага к max_hp, +бонус_мастерства к урону.
        # - Inured_to_Undeath -- сопротивление к урону некротикой, максимум хитов не уменьшается.
        'School_of_Necromancy':True,
        'Grim_Harvest':True,
        'Undead_Thralls':True,
        'Inured_to_Undeath':True,
        'resistance':['necrotic_energy'],
        },
    'race':'Human-hero',
    'weapon_skill':['simple'],
    'armor_skill':[],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        # TODO: руны 3-4 круга
        # - Rune of Flying
        # - Rune of Stoneskin
        # - Rune of Greater Invisibility
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Rune of Armor':1,
        'Dagger':1,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Wizard 12 lvl (нейтрал) (симулякр Менона)'] = {
    # "Feat_Alert", -- нельзя застать врасплох. "Feat_Keen_Mind" -- помнит всё.
    # Связан с самим Меноном через Rary_Telepathic_Bond.
    'level':12,
    'simulacrum':True,
    'fireball_AI':True,
    'disengage_AI':True,
    'char_class':'Wizard',
    'hit_dice':'1d6',
    'behavior':'commander',
    'hitpoints_medial':True,
    'abilityes':{
        'strength':16,
        'dexterity':17,
        'constitution':17,
        'intelligence':19,
        'wisdom':17,
        'charisma':14,
        },
    'class_features':{
        'Feat_Alert':True,
        'Feat_Keen_Mind':True,
        'Feat_Resilient':'constitution',
        'Ability_Score_Improvement':{
            'dexterity':+1,
            'constitution':+1,
            'intelligence':+1,
            'wisdom':+1,
            },
        'Arcane_Recovery':True,
        'Spellcasting':True,
        'Spells':[
            # Уровень_персонажа + мод_интеллекта (17 заклинаний)
            # https://www.dandwiki.com/wiki/5e_SRD:Wizard
            ('cantrip', 'Prestidigitation'),
            ('cantrip', 'Shape_Water'),
            ('cantrip', 'Mold_Earth'),
            ('cantrip', 'Message'),
            ('cantrip', 'Minor_Illusion'),
            # Ритуалы из книги заклинаний:
            ('ritual', 'Alarm'),
            ('ritual', 'Identify'),
            ('ritual', 'Detect_Magic'),
            ('ritual', 'Unseen_Servant'),
            ('ritual', 'Gentle_Repose'),
            ('ritual', 'Water_Breathing'),
            ('ritual', 'Leomund_Tiny_Hut'),
            ('ritual', 'Rary_Telepathic_Bond'),
            ('1_lvl', 'Shield'),
            ('2_lvl', 'Invisibility'),
            ('2_lvl', 'Mirror_Image'),
            ('2_lvl', 'Knock'),
            ('3_lvl', 'Counterspell'),
            ('3_lvl', 'Dispel_Magic'),
            ('3_lvl', 'Enemies_Abound'),
            ('3_lvl', 'Blink'),
            ('4_lvl', 'Arcane_Eye'),
            ('4_lvl', 'Dimension_Door'),
           # ('4_lvl', 'Sickening_Radiance'),
            ('5_lvl', 'Teleportation_Circle'),
            ('5_lvl', 'Conjure_Elemental'),
            ('5_lvl', 'Danse_Macabre'),
            ('5_lvl', 'Passwall'),
            #('6_lvl', 'Circle_of_Death'),
            ('6_lvl', 'Arcane_Gate'),
            ],
        'School_of_Necromancy':True,
        #'Grim_Harvest':True,
        'Undead_Thralls':True,
        'Inured_to_Undeath':True,
        'resistance':['necrotic_energy'],
        },
    'race':'Human-hero',
    'weapon_skill':['simple'],
    'armor_skill':[],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        # Симулякру не полагаются драгоценные руны.
        'Rune of Absorbtion':2,
        'Rune of Armor':1,
        'Dagger':1,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

#----
# Нейтралы (армии) (Бронзовые гоплиты Менона):

metadict_chars['Warrior 4 lvl (нейтрал) (бронзовый гоплит Менона)'] = {
    # Умертвие.
    'level':4,
    'sneak_AI':True,
    'killer_AI':True,
    'fearless_AI':True,
    'char_class':'Warrior-officer',
    'hit_dice':'1d8',
    'behavior':'elite_warrior',
    'class_features':{
        'immunity':['poison','poisoned'],
        'Fighting_Style_Blind_Fighting':True,
        'Feat_Magic_Initiate':True,
        'Spellcasting':True,
        'Spells':[
            ('cantrip', 'Sword_Burst'),
            ('cantrip', 'Mold_Earth'),
            #('cantrip', 'Frostbite'),
            #('cantrip', 'Fire_Bolt'),
            #('cantrip', 'Create_Bonfire'),
            ('1_lvl', 'Fog_Cloud'),
            #('1_lvl', 'Magic_Missile'),
            ],
        },
    'race':'Human-hero-undead',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        # Нежить не может использовать эссенции:
        #'Infusion of Healing':1,
        'Infusion of False Life':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Plate Armor':1,
        'Heavy Shield':1,
        'Long Spear':1,
        'Longsword':1,
        'Plumbata':12,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Warrior 5 lvl (нейтрал) (бронзовый гоплит-капитан Менона)'] = {
    'level':5,
    'sneak_AI':True,
    'killer_AI':True,
    'fearless_AI':True,
    #'carefull_AI':True,
    #'no_grappler_AI':True,
    #'fearless_AI':True,
    #'seeker_AI':True,
    'char_class':'Warrior-officer',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'immunity':['poison','poisoned'],
        'Fighting_Style_Blind_Fighting':True,
        'Feat_Magic_Initiate':True,
        'Spellcasting':True,
        'Spells':[
            ('cantrip', 'Sword_Burst'),
            ('cantrip', 'Mold_Earth'),
            #('cantrip', 'Frostbite'),
            #('cantrip', 'Fire_Bolt'),
            #('cantrip', 'Create_Bonfire'),
            #('cantrip', 'Message'),
            ('1_lvl', 'Fog_Cloud'),
            #('1_lvl', 'Magic_Missile'),
            ],
        'Extra_Attack':True,
        },
    'race':'Human-hero-undead',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        # Нежить не может использовать эссенции:
        #'Infusion of Healing':1,
        'Infusion of False Life':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Plate Armor':1,
        'Heavy Shield':1,
        'Long Spear':1,
        'Longsword':1,
        'Plumbata':12,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

#----
# Нейтралы (армия) (ветераны Карагос):

metadict_chars['Warrior 1 lvl (нейтрал) (пират Карагоса)'] = {
    # Щиты используют против лучников, но не в ближнем бою.
    'level':1,
    'char_class':'Warrior',
    'hit_dice':'1d8',
    'behavior':'warrior',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Hide Armor':1,
        'Shield':1,
        'Longsword':1,
        'Shortbow':1,
        'Arrow':40,
        },
    }

metadict_chars['Warrior 2 lvl (нейтрал) (ветеран Карагоса)'] = {
    # Штурмовики-ветераны
    'level':2,
    'char_class':'Warrior',
    'hit_dice':'1d8',
    'behavior':'elite_warrior',
    'class_features':{
        'Fighting_Style_Great_Weapon_Fighting':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Hide Armor':1,
        'Shield':1,
        'Shortsword':1,
        'Glaive':1,
        'Javelin':6,
        },
    }

metadict_chars['Warrior 3 lvl (нейтрал) (сержант Карагоса)'] = {
    'level':3,
    'char_class':'Warrior',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Great_Weapon_Fighting':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Breastplate':1,
        'Heavy Shield':1,
        'Shortsword':1,
        'Glaive':1,
        'Javelin':6,
        },
    }

metadict_chars['Warrior 4 lvl (нейтрал) (лейтенант Карагоса)'] = {
    'level':4,
    'char_class':'Warrior-officer',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Great_Weapon_Fighting':True,
        'Feat_Inspiring_Leader':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':3,
        'Half Plate':1,
        'Heavy Shield':1,
        'Shortsword':1,
        'Glaive':1,
        },
    'mount_combat':False,
    'mount_type':'Riding Horse',
    'equipment_mount':{
        },
    }

metadict_chars['Warrior 5 lvl (нейтрал) (капитан Карагоса)'] = {
    'level':5,
    'char_class':'Warrior-officer',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Great_Weapon_Fighting':True,
        'Feat_Inspiring_Leader':True,
        'Extra_Attack':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Half Plate':1,
        'Heavy Shield':1,
        'Shortsword':1,
        'Glaive':1,
        },
    'mount_combat':False,
    'mount_type':'Riding Horse',
    'equipment_mount':{
        },
    }

#----
# Нейтралы (герои) (Карагос):

metadict_chars['Barbarian 9 lvl (нейтрал) (Карагос «Мудрый»)'] = {
    # Barbarian 1 lvl (thracian slayer-dogface) sum:108 STR:19 DEX:18 CON:19 INT:18 WIS:16 CHA:18
    'level':9,
    'hunter_AI':True,
    'fearless_AI':True,
    'no_grappler_AI':True,
    'squad_advantage':True,
    'char_class':'Barbarian',
    'hit_dice':'1d12',
    'behavior':'commander',
    'hitpoints_medial':True,
    'abilityes':{
        'strength':19,
        'dexterity':18,
        'constitution':19,
        'intelligence':16,
        'wisdom':18,
        'charisma':18,
        },
    'class_features':{
        # TODO:
        # 4. сделай Mindless_Rage (защищает от очарования и страха)
        'Feat_Great_Weapon_Master':True,
        'Unarmored_Defense':True,
        'Rage':True,
        'Reckless_Attack':True,
        'Danger_Sense':True,
        'Primal_Path_Berserker':True,
        'Berserker_Frenzy':True,
        'Fast_Movement':True,
        'Feral_Instinct':True,
        'Mindless_Rage':True,
        'Extra_Attack':True,
        'Brutal_Critical':True,
        'Ability_Score_Improvement':{
            'dexterity':+2,
            'strength':+1,
            'constitution':+1,
            },
        },
    'race':'Human-hero-big',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Potion of Antidote':1,
        'Infusion of Regeneration':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        #'Sword of Life-Stealing':1,
        #'Sword of Sharpness':1,
        'Sword of the Past +2':1,
        },
    #'mount_combat':False,
    #'mount_type':'Warhorse',
    #'equipment_mount':{
    #    },
    }

#----
# Нейтралы (герои) (Кирос):

metadict_chars['Fighter 4 lvl (нейтрал) (боец Кироса)'] = {
    'level':4,
    'char_class':'Eldritch_Knight',
    'hit_dice':'1d10',
    'behavior':'commander',
    'class_features':{
        'Feat_Mounted_Combatant':True,
        #'Feat_Sentinel':True,
        'Feat_Heavy_Armor_Master':True,
        'Ability_Score_Improvement':{
            'strength':+1,
            },
        'Fighting_Style_Dueling':True,
        'Second_Wind':True,
        'Action_Surge':True,
        'Martial_Archetype_Eldritch_Knight':True,
        'Weapon_Bond':True,
        'Spellcasting':True,
        'Spells':[
            ('cantrip', 'Message'),
            ('cantrip', 'Green_Flame_Blade'),
            ('ritual', 'Alarm'),
            ('1_lvl', 'Shield'),
            ('1_lvl', 'Magic_Missile'),
            ('1_lvl', 'Absorb_Elements'),
            #('1_lvl', 'Fog_Cloud'),
            ],
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Heroism':1,
        'Infusion of Regeneration':1,
        'Rune of Absorbtion':1,
        'Plate Armor':1,
        'Heavy Shield':1,
        'Longsword +1':1,
        'Lance':1,
        #'Pilum':6,
        },
    'mount_combat':True,
    'mount_type':'Warhorse',
    'equipment_mount':{
        'Rune of Absorbtion':1,
        'Infusion of Regeneration':1,
        'Horse Scale Mail':1,
        },
    }

metadict_chars['Fighter 13 lvl (нейтрал) (Кирос «Симарх»)'] = {
    # Fighter 1 lvl (legionary sentinel-battler) sum:103 STR:19 DEX:17 CON:18 INT:16 WIS:16 CHA:17
    # Использует "Обнаружение мыслей" (Detect_Thoughts), чтобы читать мысли других.
    'level':13,
    'fearless_AI':True,
    'no_grappler_AI':True,
    'char_class':'Eldritch_Knight',
    'hit_dice':'1d10',
    'behavior':'commander',
    'hitpoints_medial':True,
    'abilityes':{
        'strength':19,
        'dexterity':17,
        'constitution':18,
        'intelligence':16,
        'wisdom':16,
        'charisma':17,
        },
    'class_features':{
        # TODO:
        # - Eldritch_Strike -- удачный удар = помеха на спасброски от закл. до конца следующего хода.
        'Feat_Mounted_Combatant':True,
        'Feat_War_Caster':True,
        #'Feat_Sentinel':True,
        'Feat_Heavy_Armor_Master':True,
        'Ability_Score_Improvement':{
            'strength':+1,
            'intelligence':+4,
            },
        'Fighting_Style_Dueling':True,
        'Second_Wind':True,
        'Action_Surge':True,
        'Martial_Archetype_Eldritch_Knight':True,
        'Weapon_Bond':True,
        'Spellcasting':True,
        'Spells':[
            # 9 заклинаний на 13 lvl (2 заклинания вне школ evocation и abjuration)
            ('cantrip', 'Message'),
            ('cantrip', 'Green_Flame_Blade'),
            ('cantrip', 'Prestidigitation'),
            ('ritual', 'Alarm'),
            ('1_lvl', 'Shield'),
            #('2_lvl', 'Shield'),
            #('1_lvl', 'Magic_Missile'),
            #('1_lvl', 'Fog_Cloud'),
            ('2_lvl', 'Blur'),
            ('3_lvl', 'Blur'),
            ('2_lvl', 'Detect_Thoughts'),
            ('2_lvl', 'Warding_Wind'),
            ('2_lvl', 'Gust_of_Wind'),
            ('3_lvl', 'Counterspell'),
            ('3_lvl', 'Sending'),
            ],
        'Extra_Attack':True,
        'Indomitable':True,
        'War_Magic':True,
        'Eldritch_Strike':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Heroism':1,
        'Infusion of Regeneration':1,
        'Rune of Absorbtion':1,
        'Plate Armor':1,
        'Heavy Shield +1':1,
        #'Sword of Flame Tongue':1,
        'Longsword +2':1,
        'Lance':1,
        #'Pilum':6,
        },
    'mount_combat':True,
    'mount_type':'Warhorse',
    'equipment_mount':{
        'Rune of Absorbtion':1,
        'Infusion of Regeneration':1,
        'Horse Scale Mail':1,
        },
    }

#----
# Враги (герои) (Радамант):

metadict_chars['Barbarian 2 lvl (враг) (варвар Радаманта)'] = {
    'level':2,
    'char_class':'Barbarian',
    'hit_dice':'1d12',
    'behavior':'elite_warrior',
    'class_features':{
        'Feat_Mounted_Combatant':True,
        'Unarmored_Defense':True,
        'Rage':True,
        'Reckless_Attack':True,
        'Danger_Sense':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':2,
        'Scale Mail':1,
        'Shield':1,
        'Longsword':1,
        'Lance':1,
        'Javelin':6,
        },
    'mount_combat':True,
    'mount_type':'Warhorse',
    'equipment_mount':{
        'Scale Mail':1,
        },
    }

metadict_chars['Barbarian 5 lvl (враг) (Радамант «Бдительный»)'] = {
    'level':5,
    'char_class':'Barbarian',
    'hit_dice':'1d12',
    'behavior':'commander',
    'hitpoints_medial':True,
    'abilityes':{
        'strength':18,
        'dexterity':14,
        'constitution':18,
        'intelligence':10,
        'wisdom':12,
        'charisma':16,
        },
    'class_features':{
        'Feat_Alert':True,
        'Feat_Mounted_Combatant':True,
        'Unarmored_Defense':True,
        'Rage':True,
        'Reckless_Attack':True,
        'Danger_Sense':True,
        'Primal_Path_Berserker':True,
        'Berserker_Frenzy':True,
        'Extra_Attack':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':3,
        'Half Plate':1,
        'Shield':1,
        'Longsword +1':1,
        'Lance':1,
        'Javelin':6,
        },
    'mount_combat':True,
    'mount_type':'Warhorse',
    'equipment_mount':{
        'Scale Mail':1,
        },
    }

#----
# Враги (свита) (Чара Атенак):

metadict_chars['Warlock 3 lvl (враг) (колдун Чары)'] = {
    # Фамильяр -- бес. Разведчик-невидимка.
    'level':3,
    'fireball_AI':True,
    'disengage_AI':True,
    #'archer_AI':True,
    'char_class':'Warlock',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Feat_Resilient':'constitution',
        'Ability_Score_Improvement':{
            'constitution':+1,
            },
        #'Feat_Spellsniper':True,
        #'Feat_Elemental_Adept':'fire',
        'Otherworldly_Patron':True,
        'Otherworldly_Patron_The_Fiend':True,
        'Pact_Magic':True,
        'Spells':[
            # Дополнительный кантрип за Feat_Spellsniper
            ('cantrip', 'Eldritch_Blast'),
            ('cantrip', 'Create_Bonfire'),
            ('cantrip', 'Message'),
            ('ritual', 'Find_Familiar'),
            ('2_lvl', 'Armor_of_Agathys'),
            ('2_lvl', 'Flaming_Sphere'),
            ('2_lvl', 'Invisibility'),
            #('2_lvl', 'Shatter'),
            ],
        'Dark_One\'s_Blessing':True,
        'Eldritch_Invocations':True,
        'Invocation_Agonizing_Blast':True,
        'Invocation_Eldritch_Spear':True,
        'Pact_Boon':True,
        'Pact_of_the_Chain':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple'],
    'armor_skill':['light'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Regeneration':1,
        'Rune of Absorbtion':1,
        'Rune of Armor':1,
        'Shortsword':1,
        'Shortbow':1,
        'Arrow':40,
        'Poison Arrow':40,
        'Poison Blade':10,
        },
    #'mount_combat':True,
    #'mount_type':'Horseclaw',
    #'equipment_mount':{
    #    'Horse Scale Mail':1,
    #    },
    }

metadict_chars['Warlock 11 lvl (враг) (Чара Атенак)'] = {
     # Warlock 1 lvl (otherworld seeker-follower) sum:97 STR:15 DEX:18 CON:16 INT:15 WIS:15 CHA:18
        # 18 слотов/сутки под "Вещий сон" (Dream) и "Наблюдение" (Scrying)
        # Неограниченный "Разговор с мёртвыми" (Speak_with_Dead).
        # Фамильяр (попугай) может передавать голос Чары.
        # Ритуальный заклинатель (заклинания волшебника):
    'level':11,
    'fireball_AI':True,
    'disengage_AI':True,
    #'archer_AI':True,
    'char_class':'Warlock',
    'hit_dice':'1d8',
    'behavior':'commander',
    'hitpoints_medial':True,
    'abilityes':{
        'strength':15,
        'dexterity':18,
        'constitution':16,
        'intelligence':15,
        'wisdom':15,
        'charisma':18,
        },
    'class_features':{
        'Feat_Resilient':'constitution',
        'Ability_Score_Improvement':{
            'constitution':+1,
            'charisma':+2,
            },
        #'Feat_Spellsniper':True,
        #'Feat_Elemental_Adept':'fire',
        'Otherworldly_Patron':True,
        'Otherworldly_Patron_The_Fiend':True,
        'Pact_Magic':True,
        'Spells':[
            # Дополнительный кантрип за Feat_Spellsniper
            ('cantrip', 'Eldritch_Blast'),
            ('cantrip', 'Create_Bonfire'),
            ('cantrip', 'Prestidigitation'),
            ('cantrip', 'Minor_Illusion'),
            ('cantrip', 'Message'),
            # Pact_of_the_Chain:
            ('ritual', 'Find_Familiar'),
            # Ритуальный заклинатель (волшебник):
            ('ritual', 'Alarm'),
            ('ritual', 'Identify'),
            ('ritual', 'Detect_Magic'),
            ('ritual', 'Unseen_Servant'),
            ('ritual', 'Comprehend_Languages'),
            ('ritual', 'Water_Breathing'),
            ('ritual', 'Leomund_Tiny_Hut'),
            ('ritual', 'Rary_Telepathic_Bond'),
            ('ritual', 'Contact_Other_Plane'),
            # Для свиты:
            ('5_lvl', 'Armor_of_Agathys'),
            ('5_lvl', 'Flaming_Sphere'),
            ('5_lvl', 'Invisibility'),
            #('5_lvl', 'Shatter'),
            # Личные:
            ('5_lvl', 'Dream'),
            ('5_lvl', 'Scrying'),
            ('5_lvl', 'Counterspell'),
            #('5_lvl', 'Wall_of_Fire'),
            ('5_lvl', 'Synaptic_Static'),
            ('5_lvl', 'Summon_Greater_Demon'),
            ('5_lvl', 'Dimension_Door'),
            ('5_lvl', 'Banishment'),
            # Invocation_Minios_of_Chaos:
            ('5_lvl', 'Conjure_Elemental'),
            # Таинственный арканум:
            ('6_lvl', 'True_Seeing'),
            ],
        # TODO:
        # - Удача темнейшего, +1d10 к спасброску/проверке характеристики. 1 раз/кор.отдых.
        # - Устойчивость исчадия, сопротивление типу урона. Даже к колющему/рубящему.
        'Dark_One\'s_Blessing':True,
        'Dark_One\'s_Own_Luck':True,
        'Fiendish_Resilience':True,
        'resistance':['piercing'],
        # 11 lvl, 5 инвокаций:
        'Eldritch_Invocations':True,
        'Invocation_Eldritch_Spear':True,
        'Invocation_Agonizing_Blast':True,
        'Invocation_Minios_of_Chaos':True,
        'Invocation_Voice_of_the_Chain_Master':True,
        'Invocation_Whispers_of_the_Grave':True,
        # Договор цепи:
        'Pact_Boon':True,
        'Pact_of_the_Chain':True,
        # Черта на 8 lvl:
        'Feat_Ritual_Caster':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        # Магические предметы:
        # d6    | Ритуальная магия Шекелеш  |  Свойства                                             
        # ----- | ------------------------- | ------------------------------------------------------
        # 1     | Жезл договора*            | Восстанавливает ячейку заклинания колдуна. 1 раз/сутки
        # 2     | Мантия глаз*              | Всестороннее зрение. Тёмное, эфирный план, 120 футов. 
        # 3     | Кольцо заклинаний*        | Хранит любое заклинание 1-3 lvl. Перезарядка магом.   
        # 4     | Оковы измерений           | Служат как наручники. Запрещают телепорты всех форм.  
        # 5     | Подковы скорости          | Увеличивает скорость лошади на 30 футов/раунд         
        # 6     | Подковы ветра             | Лошадь свободно бежит по сложной местности, воде.     
        # Чара не использует руны, привязка к магическим предметам.
        #'Rune of Absorbtion':1,
        #'Rune of Shielding':1,
        'Mage_Armor':1,
        'Shortsword +1':1,
        'Shortbow +1':1,
        'Arrow':40,
        'Poison Arrow':40,
        'Poison Blade':10,
        },
    # TODO: летучий зверь вместо когтеклюва:
    #'mount_combat':True,
    #'mount_type':'Horseclaw',
    #'equipment_mount':{
    #    'Horse Scale Mail':1,
    #    },
    }


#----
# Враги (армии) (мирмидоны Чары):

metadict_chars['Warrior 1 lvl (враг) (мирмидон)'] = {
    # Армия Номисто. "Универсальные солдаты", x2 стоимость снаряжения.
    'level':1,
    'char_class':'Warrior',
    'behavior':'warrior',
    'hit_dice':'1d8',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Chain Shirt':1,
        'Heavy Shield':1,
        'Shortsword':1,
        'Long Spear':1,
        'Shortbow':1,
        'Arrow':30,
        'Poison Arrow':10,
        'Poison Blade':10,
        },
    }

metadict_chars['Warrior 2 lvl (враг) (мирмидон-ветеран)'] = {
    'level':2,
    'char_class':'Warrior',
    'behavior':'elite_warrior',
    'hit_dice':'1d8',
    'class_features':{
        'Fighting_Style_Defence':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Breastplate':1,
        'Heavy Shield':1,
        'Shortsword':1,
        'Long Spear':1,
        'Shortbow':1,
        'Arrow':30,
        'Poison Arrow':10,
        'Poison Blade':10,
        },
    }

metadict_chars['Warrior 3 lvl (враг) (мирмидон-сержант)'] = {
    'level':3,
    'char_class':'Warrior',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Defence':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Shielding':1,
        'Breastplate':1,
        'Heavy Shield':1,
        'Shortsword':1,
        'Long Spear':1,
        'Shortbow':1,
        'Arrow':30,
        'Poison Arrow':10,
        'Poison Blade':10,
        },
    }

metadict_chars['Warrior 4 lvl (враг) (мирмидон-лейтенант)'] = {
    'level':4,
    'char_class':'Warrior-officer',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Defence':True,
        'Feat_Inspiring_Leader':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Heroism':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Half Plate':1,
        'Heavy Shield':1,
        'Shortsword':1,
        'Long Spear':1,
        'Shortbow':1,
        'Poison Arrow':40,
        'Poison Blade':10,
        },
    'mount_combat':False,
    'mount_type':'Riding Horse',
    'equipment_mount':{
        },
    }

metadict_chars['Warrior 5 lvl (враг) (мирмидон-капитан)'] = {
    'level':5,
    'char_class':'Warrior-officer',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Defence':True,
        'Feat_Inspiring_Leader':True,
        'Extra_Attack':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Heroism':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Half Plate':1,
        'Heavy Shield':1,
        'Shortsword':1,
        'Long Spear':1,
        'Shortbow':1,
        'Poison Arrow':40,
        'Poison Blade':10,
        },
    'mount_combat':False,
    'mount_type':'Riding Horse',
    'equipment_mount':{
        },
    }

#----
# Враги (армии) (легионеры Акхена):

metadict_chars['Warrior 1 lvl (враг) (легионер Акхена)'] = {
    # "Универсальные солдаты", удвоенная стоимость снаряжения.
    # Пользуются усыпляющим ядом. Очень хороши против варваров и больших зверей.
    'level':1,
    'char_class':'Warrior',
    'hit_dice':'1d8',
    'behavior':'warrior',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Studded Leather':1,
        'Heavy Shield':1,
        'Shortsword':1,
        'Javelin':8,
        'Sleep Blade':10,
        },
    }

metadict_chars['Warrior 2 lvl (враг) (ветеран Акхена)'] = {
    'level':2,
    'char_class':'Warrior',
    'hit_dice':'1d8',
    'behavior':'elite_warrior',
    'class_features':{
        'Fighting_Style_Protection':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Breastplate':1,
        'Heavy Shield':1,
        'Shortsword':1,
        'Javelin':5,
        'Sleep Blade':10,
        },
    }

metadict_chars['Warrior 3 lvl (враг) (сержант Акхена)'] = {
    'level':3,
    'char_class':'Warrior',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Protection':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Infusion of Heroism':1,
        'Breastplate':1,
        'Heavy Shield':1,
        'Shortsword':1,
        'Javelin':5,
        'Sleep Blade':10,
        },
    }

metadict_chars['Warrior 4 lvl (враг) (лейтенант Акхена)'] = {
    'level':4,
    'char_class':'Warrior-officer',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Protection':True,
        'Feat_Inspiring_Leader':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Infusion of Heroism':1,
        'Rune of Shielding':1,
        'Half Plate':1,
        'Heavy Shield':1,
        'Shortsword':1,
        'Javelin':5,
        'Sleep Blade':10,
        },
    'mount_combat':False,
    'mount_type':'Riding Horse',
    'equipment_mount':{
        },
    }

metadict_chars['Warrior 5 lvl (враг) (капитан Акхена)'] = {
    'level':5,
    'char_class':'Warrior-officer',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Protection':True,
        'Feat_Inspiring_Leader':True,
        'Extra_Attack':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Infusion of Heroism':1,
        'Rune of Shielding':1,
        'Half Plate':1,
        'Heavy Shield':1,
        'Shortsword':1,
        'Javelin':5,
        'Sleep Blade':10,
        },
    'mount_combat':False,
    'mount_type':'Riding Horse',
    'equipment_mount':{
        },
    }

#----
# Враги (свита) (чародеи Ашеры):

metadict_chars['Sorcerer 3 lvl (otherworld wildfire-enchanter)'] = {
    'level':3,
    'fireball_AI':True,
    'disengage_AI':True,
    'char_class':'Sorcerer',
    'hit_dice':'1d6',
    'behavior':'commander',
    'class_features':{
        'Feat_Elemental_Adept':'fire',
        'Spellcasting':True,
        'Spells':[
            ('cantrip', 'Prestidigitation'),
            ('cantrip', 'Control_Flames'),
            ('cantrip', 'Create_Bonfire'),
            ('cantrip', 'Fire_Bolt'),
            ('1_lvl', 'Shield'),
            ('1_lvl', 'Burning_Hands'),
            ('1_lvl', 'Absorb_Elements'),
            ('2_lvl', 'Flaming_Sphere'),
            ],
        'Font_of_Magic':True,
        'Metamagic':True,
        #'Metamagic_Subtle_Spell':True,
        'Metamagic_Extended_Spell':True,
        'Metamagic_Distant_Spell':True,
        },
    'race':'Primevial-large',
    'weapon_skill':['simple'],
    'armor_skill':[],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Dagger':1,
        },
    }

#----
# Враги (армии) (демоны Ашеры):

metadict_chars['Warrior 1 lvl (враг) (демон-рядовой)'] = {
    # У них природный доспех с 12 AC. Крепкая шкура. В лёгкой броне демоны не нуждаются.
    'level':1,
    'char_class':'Warrior',
    'behavior':'warrior',
    'hit_dice':'1d8',
    'race':'Primevial-medium',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':militia_pack,
    'equipment_weapon':{
        'Shield':1,
        'Battleaxe':1,
        'Long Spear':1,
        'Javelin':6,
        },
    }

metadict_chars['Warrior 2 lvl (враг) (демон-ветеран)'] = {
    # У демонов-ветеранов сопротивляемость к огню и обычному оружию.
    # Уязвимость к излучению и серебру.
    'level':2,
    'char_class':'Warrior',
    'behavior':'elite_warrior',
    'class_features':{
        'resistance':['slashing','piercing','bludgeoning'],
        'vultenability':['radiant'],
        },
    'hit_dice':'1d8',
    'race':'Primevial-medium',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':militia_pack,
    'equipment_weapon':{
        'Infusion of Regeneration':1,
        'Heavy Shield':1,
        'Battleaxe':1,
        'Long Spear':1,
        'Javelin':6,
        },
    }

metadict_chars['Warrior 3 lvl (враг) (демон-сержант)'] = {
    'level':3,
    'brave_AI':True,
    'killer_AI':True,
    'carefull_AI':True,
    'char_class':'Warrior-officer',
    'behavior':'commander',
    'class_features':{
        'resistance':['slashing','piercing','bludgeoning'],
        'vultenability':['radiant'],
        },
    'hit_dice':'1d10',
    'race':'Primevial-large',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':militia_pack,
    'equipment_weapon':{
        'Infusion of Regeneration':1,
        'Infusion of Heroism':1,
        'Heavy Shield':1,
        'Battleaxe':1,
        'Long Spear':1,
        'Javelin':6,
        },
    }

metadict_chars['Warrior 4 lvl (враг) (демон-лейтенант)'] = {
    'level':4,
    'brave_AI':True,
    'killer_AI':True,
    'carefull_AI':True,
    'char_class':'Warrior-officer',
    'behavior':'commander',
    'class_features':{
        'resistance':['slashing','piercing','bludgeoning'],
        'vultenability':['radiant'],
        },
    'hit_dice':'1d10',
    'race':'Primevial-large',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':militia_pack,
    'equipment_weapon':{
        'Infusion of Regeneration':1,
        'Infusion of Heroism':1,
        'Rune of Absorbtion':1,
        'Heavy Shield':1,
        'Battleaxe':1,
        'Long Spear':1,
        'Javelin':6,
        },
    }

metadict_chars['Warrior 5 lvl (враг) (демон-капитан)'] = {
    'level':5,
    'brave_AI':True,
    'killer_AI':True,
    'carefull_AI':True,
    'char_class':'Warrior-officer',
    'behavior':'commander',
    'class_features':{
        'resistance':['slashing','piercing','bludgeoning'],
        'vultenability':['radiant'],
        },
    'hit_dice':'1d10',
    'race':'Primevial-large',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':militia_pack,
    'equipment_weapon':{
        'Infusion of Regeneration':1,
        'Infusion of Heroism':1,
        'Rune of Absorbtion':1,
        'Half Plate':1,
        'Heavy Shield':1,
        'Battleaxe':1,
        'Long Spear':1,
        'Javelin':6,
        },
    }

#----
# Враги (армии) (водяные Нингиримы):

metadict_chars['Warrior 1 lvl (враг) (гоплит Нингиримы)'] = {
    'level':1,
    'water_walk':True,
    'char_class':'Warrior',
    'behavior':'warrior',
    'hit_dice':'1d8',
    'race':'Humanoid-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Potion of Antidote':1,
        'Studded Leather':1,
        'Heavy Shield':1,
        'Shortsword':1,
        'Long Spear':1,
        'Poison Blade':10,
        },
    }

metadict_chars['Warrior 2 lvl (враг) (гоплит-ветеран Нингиримы)'] = {
    'level':2,
    'water_walk':True,
    'char_class':'Warrior',
    'behavior':'elite_warrior',
    'hit_dice':'1d8',
    'class_features':{
        'Fighting_Style_Dueling':True,
        },
    'race':'Humanoid-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Potion of Antidote':1,
        'Scale Mail':1,
        'Heavy Shield':1,
        'Shortsword':1,
        'Long Spear':1,
        'Poison Blade':10,
        },
    }

metadict_chars['Warrior 3 lvl (враг) (гоплит-сержант Нингиримы)'] = {
    'level':3,
    'water_walk':True,
    'char_class':'Warrior',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Dueling':True,
        },
    'race':'Humanoid-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Potion of Antidote':1,
        'Infusion of Healing':1,
        'Breastplate':1,
        'Heavy Shield':1,
        'Shortsword':1,
        'Long Spear':1,
        'Poison Blade':10,
        },
    }

metadict_chars['Warrior 4 lvl (враг) (гоплит-лейтенант Нингиримы)'] = {
    'level':4,
    #'close_order_AI':True,
    'water_walk':True,
    'char_class':'Warrior-officer',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Dueling':True,
        'Feat_Inspiring_Leader':True,
        },
    'race':'Humanoid-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Potion of Antidote':1,
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Breastplate':1,
        'Heavy Shield':1,
        'Shortsword':1,
        'Long Spear':1,
        'Poison Blade':10,
        },
    }

metadict_chars['Warrior 5 lvl (враг) (гоплит-капитан Нингиримы)'] = {
    'level':5,
    #'close_order_AI':True,
    'water_walk':True,
    'char_class':'Warrior-officer',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Dueling':True,
        'Feat_Inspiring_Leader':True,
        'Extra_Attack':True,
        },
    'race':'Humanoid-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Potion of Antidote':1,
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Half Plate':1,
        'Heavy Shield':1,
        'Shortsword':1,
        'Long Spear':1,
        'Poison Blade':10,
        },
    }

#----
# Союзники (герои) (Кумар):

metadict_chars['Monk 3 lvl (друг) (монах Кумара)'] = {
    # Путь тени
    'level':3,
    'grappler_AI':True,
    'carefull_AI':True,
    'char_class':'Monk',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Feat_Defensive_Duelist':True,
        'Unarmored_Defense':True,
        'Martial_Arts':True,
        'Flurry_of_Blows':True,
        'Patient_Defense':True,
        'Step_of_the_Wind':True,
        'Unarmored_Movement':True,
        'Deflect_Missiles':True,
        'Shadow_Arts':True,
        'Spells':[
            ('2_lvl', 'Pass_Without_Trace'),
            ('2_lvl', 'Darkvision'),
            #('2_lvl', 'Darkness'),
            ('2_lvl', 'Silence'),
            ],
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':[],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Potion of Antidote':1,
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Armor':1,
        'Shortsword +1':1,
        },
    }

metadict_chars['Monk 9 lvl (друг) (Кумар «Чугуннорукий»)'] = {
    # Путь тени
    # Monk 1 lvl (city windsong-apprentice) sum:104 STR:17 DEX:19 CON:17 INT:16 WIS:18 CHA:17
    'level':9,
    'grappler_AI':True,
    'carefull_AI':True,
    'char_class':'Monk',
    'hit_dice':'1d8',
    'behavior':'commander',
    'hitpoints_medial':True,
    'abilityes':{
        'strength':17,
        'dexterity':19,
        'constitution':17,
        'intelligence':16,
        'wisdom':18,
        'charisma':17,
        },
    'class_features':{
        # TODO:
        # 2. Shadow_Step -- телепорт на 60 футов от тени к тени бонусным действием.
        # ------
        # 5. Stillness_of_Mind -- действием снимает очарование или испуг.
        # 6. Unarmored_Movement_improvement -- бег по вертикальным стенам и воде
        'Feat_Defensive_Duelist':True,
        'Unarmored_Defense':True,
        'Martial_Arts':True,
        'Flurry_of_Blows':True,
        'Patient_Defense':True,
        'Step_of_the_Wind':True,
        'Unarmored_Movement':True,
        'Deflect_Missiles':True,
        'Shadow_Arts':True,
        'Spells':[
            ('2_lvl', 'Pass_Without_Trace'),
            ('2_lvl', 'Darkvision'),
            #('2_lvl', 'Darkness'),
            ('2_lvl', 'Silence'),
            ],
        'Slow_Fall':True,
        'Extra_Attack':True,
        'Stunning_Strike':True,
        'Ability_Score_Improvement':{
            'wisdom':+2,
            'dexterity':+1,
            'constitution':+1,
            },
        'Ki_Empowered_Strikes':True,
        'Shadow_Step':True,
        'Evasion':True,
        'Stillness_of_Mind':True,
        'Unarmored_Movement_improvement':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':[],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        # TODO:
            # 2. Наручи защиты.
            # 3. Руны 3-4 круга.
        # Посох ударов продан за 4000 эфесов на оборону Илиона
        'Potion of Antidote':1,
        'Infusion of Healing':1,
        'Infusion of Heroism':1,
        'Bracers of Defence':1,
        'Rune of Shielding':1,
        #'Staff of Striking +3':1,
        'Shortsword +1':1,
        },
    }

#----
# Союзники (герои) (Тинв):

metadict_chars['Wizard 3 lvl (друг) (кошка Тинв)'] = {
    'level':3,
    'fireball_AI':True,
    'char_class':'Wizard',
    'hit_dice':'1d6',
    'behavior':'archer',
    'class_features':{
        'Arcane_Recovery':True,
        'Spellcasting':True,
        'Spells':[
            ('cantrip', 'Friends'),
            ('cantrip', 'Mold_Earth'),
            ('cantrip', 'Message'),
            ('ritual', 'Detect_Magic'),
            ('1_lvl', 'Fog_Cloud'),
            ('1_lvl', 'Charm_Person'),
            ('1_lvl', 'Sleep'),
            ('2_lvl', 'Blur'),
            ('2_lvl', 'Suggestion'),
            ('2_lvl', 'Hold_Person'),
            ('2_lvl', 'Invisibility'),
            ],
        'School_of_Enchantment':True,
        'Hypnotic_Gaze':True,
        },
    'race':'Cat-hero',
    'weapon_skill':['simple'],
    'armor_skill':[],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Infusion of Healing':1,
        'Rune of Shielding':1,
        'Rune of Armor':1,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Wizard 9 lvl (друг) (Тинв)'] = {
    # Тинв, коттаямская кошка, волшебница школы Очарования.
    # Wizard 2 lvl (city cat-weaver) sum:101 STR:14 DEX:19 CON:17 INT:19 WIS:16 CHA:16
    # Feat_Observant +5 к пассивной внимательности. Читает по губам.
    'level':9,
    'fireball_AI':True,
    'char_class':'Wizard',
    'hit_dice':'1d6',
    'behavior':'commander',
    'hitpoints_medial':True,
    'abilityes':{
        'strength':14,
        'dexterity':21,
        'constitution':18,
        'intelligence':20,
        'wisdom':18,
        'charisma':16,
        },
    'class_features':{
        # TODO: сделай Instinctive_Charm -- перенаправление атаки врага на другого, за счёт реакции.
        'Feat_Resilient':'constitution',
        'Feat_Observant':True,
        'Arcane_Recovery':True,
        'Spellcasting':True,
        'Spells':[
            ('cantrip', 'Friends'),
            ('cantrip', 'Minor_Illusion'),
            ('cantrip', 'Mold_Earth'),
            ('cantrip', 'Message'),
            ('ritual', 'Detect_Magic'),
            ('1_lvl', 'Fog_Cloud'),
            ('1_lvl', 'Charm_Person'),
            ('1_lvl', 'Sleep'),
            #('2_lvl', 'Blur'),
            ('2_lvl', 'Suggestion'),
            ('2_lvl', 'Hold_Person'),
            ('2_lvl', 'Invisibility'),
            ('3_lvl', 'Counterspell'),
            ('3_lvl', 'Nondetection'),
            ('3_lvl', 'Fireball'),
            ('3_lvl', 'Melf_Minute_Meteors'),
            #('4_lvl', 'Fear'),
            ('4_lvl', 'Arcane_Eye'),
            ('5_lvl', 'Teleportation_Circle'),
            ('5_lvl', 'Geas'),
            ],
        'School_of_Enchantment':True,
        'Hypnotic_Gaze':True,
        'Instinctive_Charm':True,
        },
    'race':'Cat-hero',
    'weapon_skill':['simple'],
    'armor_skill':[],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        # TODO: добавить руны 3-4 круга.
        # Добавить кошачьи волшебные вещи.
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Rune of Armor':1,
        },
    }

#----
# Союзники (армия) (Кумар):

metadict_chars['Warrior 1 lvl (друг) (легионер Илиона)'] = {
    'level':1,
    'char_class':'Warrior',
    'hit_dice':'1d8',
    'behavior':'warrior',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Potion of Antidote':1,
        'Studded Leather':1,
        'Heavy Shield':1,
        'Shortsword':1,
        'Fire Spear':4,
        'Holy Blade':10,
        },
    }

metadict_chars['Warrior 2 lvl (друг) (ветеран Илиона)'] = {
    'level':2,
    'char_class':'Warrior',
    'hit_dice':'1d8',
    'behavior':'elite_warrior',
    'class_features':{
        'Fighting_Style_Defence':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Potion of Antidote':1,
        'Scale Mail':1,
        'Heavy Shield':1,
        'Shortsword':1,
        'Fire Spear':2,
        'Holy Blade':10,
        },
    }

metadict_chars['Warrior 3 lvl (друг) (сержант Илиона)'] = {
    'level':3,
    'char_class':'Warrior',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Defence':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Potion of Antidote':1,
        'Infusion of Healing':1,
        'Breastplate':1,
        'Heavy Shield':1,
        'Shortsword':1,
        'Fire Spear':2,
        'Holy Blade':10,
        },
    }

metadict_chars['Warrior 4 lvl (друг) (лейтенант Илиона)'] = {
    'level':4,
    #'rearm_AI':True,
    'defence_AI':True,
    'carefull_AI':True,
    'char_class':'Warrior-officer',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Defence':True,
        'Feat_Inspiring_Leader':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Potion of Antidote':1,
        'Infusion of Healing':1,
        'Rune of Shielding':1,
        'Breastplate':1,
        'Heavy Shield':1,
        'Shortsword':1,
        'Fire Spear':2,
        'Holy Blade':10,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Warrior 5 lvl (друг) (капитан Илиона)'] = {
    # Сидит на месте, обороняется. На врага не ведёт.
    'level':5,
    #'rearm_AI':True,
    'defence_AI':True,
    'carefull_AI':True,
    'char_class':'Warrior-officer',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Defence':True,
        'Feat_Inspiring_Leader':True,
        'Extra_Attack':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Potion of Antidote':1,
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Half Plate':1,
        'Heavy Shield':1,
        'Shortsword':1,
        'Fire Spear':2,
        'Holy Blade':10,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Commoner 1 lvl (друг) (пращник Илиона)'] = {
    # Пращники Илиона
    'level':1,
    'char_class':'Commoner',
    'behavior':'archer',
    'hit_dice':'1d8',
    'race':'Human-common',
    'weapon_skill':['simple'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':militia_pack,
    'equipment_weapon':{
        'Leather Armor':1,
        'Shield':1,
        'Dagger':1,
        'Sling real':1,
        #'Holy Bullet':10,
        'Lead Bullet':10,
        #'Sling Bullet':10,
        },
    }

metadict_chars['Commoner 2 lvl (друг) (ветеран пращников Илиона)'] = {
    'level':2,
    'char_class':'Commoner',
    'behavior':'archer',
    'hit_dice':'1d8',
    'race':'Human-common',
    'weapon_skill':['simple'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Studded Leather':1,
        'Shield':1,
        'Dagger':1,
        'Sling real':1,
        #'Holy Bullet':10,
        'Lead Bullet':10,
        #'Sling Bullet':10,
        },
    }

metadict_chars['Warrior 3 lvl (друг) (сержант пращников Илиона)'] = {
    'level':3,
    'rearm_AI':True,
    'volley_AI':True,
    'defence_AI':True,
    'carefull_AI':True,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        #'Fighting_Style_Archery':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Potion of Antidote':1,
        'Infusion of Healing':1,
        'Breastplate':1,
        'Shield':1,
        'Shortsword':1,
        'Sling real':1,
        #'Holy Bullet':10,
        'Lead Bullet':10,
        #'Sling Bullet':10,
        },
    }

#----
# Союзники (герои) (Тетро):

metadict_chars['Bard 2 lvl (друг) (бард Тетры)'] = {
    # TODO: Jack_of_All_Trades позволяет добавлять 1/2 бонуса мастерства к модификаторам характеристик.
    'level':2,
    'char_class':'Bard',
    'hit_dice':'1d8',
    'behavior':'elite_warrior',
    'abilityes_choice':['charisma','dexterity','constitution'],
    'class_features':{
        'Feat_Inspiring_Leader':True,
        'Bardic_Inspiration':True,
        'Spellcasting':True,
        'Spells':[
            # 2 lvl -- 5 заклинаний
            ('cantrip', 'Message'),
            ('cantrip', 'Prestidigitation'),
            ('ritual', 'Unseen_Servant'),
            ('1_lvl', 'Charm_Person'),
            ('1_lvl', 'Healing_Word'),
            ('1_lvl', 'Silent_Image'),
            ('1_lvl', 'Dissonant_Whispers'),
            #('1_lvl', 'Sleep'),
            ],
        'Jack_of_All_Trades':True,
        'Song_of_Rest':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Potion of Antidote':1,
        'Infusion of Healing':1,
        'Rune of Shielding':1,
        'Rune of Armor':1,
        'Rapier':1,
        'Longbow':1,
        'Arrow':40,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Bard 6 lvl (друг) (Тетра Курио)'] = {
    'level':6,
    'fireball_AI':True,
    'char_class':'Bard',
    'hit_dice':'1d8',
    'behavior':'commander',
    'hitpoints_medial':True,
    'abilityes':{
        # sum:85 STR:10 DEX:16 CON:15 INT:14 WIS:14 CHA:16
        'strength':10,
        'dexterity':16,
        'constitution':15,
        'intelligence':14,
        'wisdom':14,
        'charisma':16,
        },
    'class_features':{
        'Feat_Inspiring_Leader':True,
        'Bardic_Inspiration':True,
        'Spellcasting':True,
        'Spells':[
            # 6 lvl -- 9 заклинаний
            # TODO: "Тишина" (Silence) на 2 lvl. Защита от урона громом.
            ('cantrip', 'Message'),
            ('cantrip', 'Prestidigitation'),
            ('cantrip', 'Dancing_Lights'),
            ('ritual', 'Unseen_Servant'),
            ('1_lvl', 'Charm_Person'),
            ('1_lvl', 'Healing_Word'),
            ('1_lvl', 'Silent_Image'),
            ('1_lvl', 'Dissonant_Whispers'),
            #('1_lvl', 'Sleep'),
            ('2_lvl', 'Shatter'),
            ('3_lvl', 'Crusaders_Mantle'),
            ('3_lvl', 'Counterspell'),
            ('3_lvl', 'Sending'),
            ],
        'Jack_of_All_Trades':True,
        'Song_of_Rest':True,
        'Expertise':True,
        'College_of_Lore':True,
        'Bonus_Proficiencies':True,
        'Cutting_Words':True,
        'Font_of_Inspiration':True,
        'Ability_Score_Improvement':{
            'charisma':+2,
            },
        'Additional_Magical_Secrets':True,
        'Countercharm':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'skills':[
        # 8 = 2 предыстория + 3 бард + 3 Bonus_Proficiencies
        # === Intelligence
        'Arcana',
        'Investigation',
        'Religion',
        # === Wisdom
        'Insight',
        'Perception',
        # === Charisma
        'Deception',
        'Intimidation',
        'Persuasion',
        ],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Potion of Antidote':1,
        'Infusion of Heroism':1,
        'Rune of Shielding':1,
        'Rune of Armor':1,
        'Rapier +1':1,
        'Longbow':1,
        'Arrow':40,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

#----
# Союзники (армии) (Тетро):

metadict_chars['Warrior 1 lvl (друг) (арбалетчик Тетры)'] = {
    'level':1,
    #'archer_AI':True,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'warrior',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Potion of Antidote':1,
        'Studded Leather':1,
        'Shield':1,
        'Shortsword':1,
        'Crossbow, Heavy':1,
        'Crossbow Bolt':40,
        },
    }

metadict_chars['Warrior 2 lvl (друг) (арбалетчик-ветеран Тетры)'] = {
    'level':2,
    #'archer_AI':True,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'elite_warrior',
    'class_features':{
        'Fighting_Style_Archery':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Potion of Antidote':1,
        'Chain Shirt':1,
        'Shield':1,
        'Shortsword':1,
        'Crossbow, Heavy':1,
        'Crossbow Bolt':40,
        },
    }

metadict_chars['Warrior 3 lvl (друг) (арбалетчик-сержант Тетры)'] = {
    'level':3,
    #'archer_AI':True,
    'brave_AI':True,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Archery':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Potion of Antidote':1,
        'Infusion of Healing':1,
        'Breastplate':1,
        'Shield':1,
        'Shortsword':1,
        'Crossbow, Heavy':1,
        'Crossbow Bolt':40,
        },
    }

metadict_chars['Warrior 4 lvl (друг) (арбалетчик-лейтенант Тетры)'] = {
    'level':4,
    #'archer_AI':True,
    'brave_AI':True,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Archery':True,
        'Feat_Sharpshooter':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Potion of Antidote':1,
        'Infusion of Healing':1,
        'Rune of Shielding':1,
        'Breastplate':1,
        'Shield':1,
        'Shortsword':1,
        'Crossbow, Heavy':1,
        'Crossbow Bolt':40,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Warrior 5 lvl (друг) (арбалетчик-капитан Тетры)'] = {
    'level':5,
    #'archer_AI':True,
    'brave_AI':True,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Archery':True,
        'Feat_Sharpshooter':True,
        'Extra_Attack':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Potion of Antidote':1,
        'Infusion of Healing':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Breastplate':1,
        'Shield':1,
        'Shortsword':1,
        'Crossbow, Heavy':1,
        'Crossbow Bolt':40,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

#----
# Союзники (армии) (Коза):

metadict_chars['Warlock 2 lvl (друг) (гневнорожка Козы)'] = {
    'level':2,
    'char_class':'Warlock',
    'hit_dice':'1d8',
    'behavior':'elite_warrior',
    'class_features':{
        'Otherworldly_Patron':True,
        'Pact_Magic':True,
        'Spells':[
            ('cantrip', 'Thunderclap'),
            ('cantrip', 'Eldritch_Blast'),
            ('1_lvl', 'Armor_of_Agathys'),
            ],
        'Eldritch_Invocations':True,
        'Invocation_Eldritch_Spear':True,
        },
    'race':'Fourlegged-common',
    'weapon_skill':['simple'],
    'armor_skill':['light'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Potion of Antidote':1,
        #'Infusion of Claws':1,
        #'Infusion of Barkskin':1,
        'Infusion of Regeneration':1,
        },
    }

metadict_chars['Warlock 3 lvl (друг) (главнорожка Козы)'] = {
    'level':3,
    'char_class':'Warlock',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Otherworldly_Patron':True,
        'Otherworldly_Patron_The_Fiend':True,
        'Pact_Magic':True,
        'Spells':[
            ('cantrip', 'Thunderclap'),
            ('cantrip', 'Eldritch_Blast'),
            ('2_lvl', 'Armor_of_Agathys'),
            #('2_lvl', 'Invisibility'),
            #('2_lvl', 'Suggestion'),
            #('2_lvl', 'Shatter'),
            #('2_lvl', 'Hex'),
            ],
        'Dark_One\'s_Blessing':True,
        'Eldritch_Invocations':True,
        'Invocation_Eldritch_Spear':True,
        'Invocation_Agonizing_Blast':True,
        },
    'race':'Fourlegged-common',
    'weapon_skill':['simple'],
    'armor_skill':['light'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Potion of Antidote':1,
        #'Infusion of Claws':1,
        'Infusion of Barkskin':1,
        'Infusion of Regeneration':1,
        },
    }

metadict_chars['Warlock 3 lvl (друг) (Сефо Форонейская)'] = {
    'level':3,
    #'defence_AI':True,
    'fireball_AI':True,
    'char_class':'Warlock',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        # TODO: пакт фамильяра
        'Otherworldly_Patron':True,
        'Otherworldly_Patron_The_Fiend':True,
        'Pact_Magic':True,
        'Spells':[
            ('cantrip', 'Thunderclap'),
            ('cantrip', 'Eldritch_Blast'),
            ('cantrip', 'Prestidigitation'),
            ('2_lvl', 'Armor_of_Agathys'),
            ('2_lvl', 'Invisibility'),
            ('2_lvl', 'Suggestion'),
            #('2_lvl', 'Shatter'),
            #('2_lvl', 'Hex'),
            ],
        'Dark_One\'s_Blessing':True,
        'Eldritch_Invocations':True,
        'Invocation_Agonizing_Blast':True,
        'Invocation_Eldritch_Spear':True,
        'Pact_Boon':True,
        'Pact_of_the_Tome':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple'],
    'armor_skill':['light'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Potion of Antidote':1,
        'Infusion of Regeneration':1,
        'Rune of Absorbtion':1,
        'Rune of Armor':1,
        'Dagger':1,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

#----
# Союзники (герои) (Кема'Эш):

metadict_chars['Warlock 2 lvl (друг) (колдун Кема\'Эша)'] = {
    'level':2,
    'char_class':'Warlock',
    'hit_dice':'1d8',
    'behavior':'archer',
    'class_features':{
        'Feat_Mounted_Combatant':True,
        'Otherworldly_Patron':True,
        'Otherworldly_Patron_The_Archfey':True,
        'Pact_Magic':True,
        'Spells':[
            ('cantrip', 'Shape_Water'),
            ('cantrip', 'Eldritch_Blast'),
            ('1_lvl', 'Charm_Person'),
            ('1_lvl', 'Armor_of_Agathys'),
            ('1_lvl', 'Sleep'),
            ],
        # TODO: пили бонусы архифеи Козы.
        # - 1 lvl Fey_Presence, пугает/очаровывает на ход, 10-футовый куб на себя.
        'Fey_Presence':True,
        'Eldritch_Invocations':True,
        'Invocation_Agonizing_Blast':True,
        'Invocation_Mask_of_Many_Faces':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple'],
    'armor_skill':['light'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        # Коза даёт своим эссенцию регенерации:
        'Infusion of Regeneration':1,
        'Potion of Antidote':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Rune of Armor':1,
        'Shortsword':1,
        'Shortbow':1,
        'Arrow':40,
        },
    #'mount_combat':True,
    #'mount_type':'Horseclaw',
    #'equipment_mount':{
    #    'Horse Scale Mail':1,
    #    },
    }

metadict_chars['Warlock 6 lvl (друг) (Кема\'Эш «Ловкач»)'] = {
    'level':6,
    'fireball_AI':True,
    'char_class':'Warlock',
    'hit_dice':'1d8',
    'behavior':'commander',
    'hitpoints_medial':True,
    'abilityes':{
        'strength':10,
        'dexterity':16,
        'constitution':12,
        'intelligence':14,
        'wisdom':16,
        'charisma':18,
        },
    'class_features':{
        'Feat_Mounted_Combatant':True,
        'Otherworldly_Patron':True,
        'Otherworldly_Patron_The_Archfey':True,
        'Pact_Magic':True,
        'Spells':[
            # Козочка даёт кантрип Shape_Water вместо Create_Bonfire Ашеры:
            ('cantrip', 'Shape_Water'),
            ('cantrip', 'Eldritch_Blast'),
            ('cantrip', 'Minor_Illusion'),
            ('cantrip', 'Prestidigitation'),
            ('cantrip', 'Message'),
            ('ritual', 'Detect_Magic'),
            ('ritual', 'Identify'),
            ('3_lvl', 'Sleep'),
            ('3_lvl', 'Charm_Person'),
            ('3_lvl', 'Armor_of_Agathys'),
            ('3_lvl', 'Summon_Lesser_Demons'),
            ('3_lvl', 'Counterspell'),
            # Коза не даёт лётных заклинаний, не умеет:
            #('3_lvl', 'Fly'),
            ],
        # TODO: пили бонусы архифеи Козы.
        # - 1 lvl Fey_Presence, пугает/очаровывает на ход, 10-футовый куб на себя.
        # - 6 lvl Misty_Escape, телепорт на 60 футов, реакцией, после ранения. Плюс невидимость на ход.
        'Fey_Presence':True,
        'Misty_Escape':True,
        'Eldritch_Invocations':True,
        'Invocation_Agonizing_Blast':True,
        'Invocation_Mask_of_Many_Faces':True,
        'Invocation_Book_of_Ancient_Secrets':True,
        'Pact_Boon':True,
        'Pact_of_the_Tome':True,
        'Feat_Inspiring_Leader':True,
        },
    'race':'Human-hero',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        # Коза даёт своим эссенцию регенерации:
        'Infusion of Regeneration':1,
        'Potion of Antidote':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Rune of Armor':1,
        'Shortsword +1':1,
        'Shortbow':1,
        'Arrow':40,
        },
    #'mount_combat':True,
    #'mount_type':'Horseclaw',
    #'equipment_mount':{
    #    'Horse Scale Mail':1,
    #    },
    }

#----
# Союзники (герои) (Тави):

metadict_chars['Wizard 2 lvl (друг) (кошка Тави)'] = {
    'level':2,
    'commando_AI':True,
    'char_class':'Wizard',
    'hit_dice':'1d6',
    'behavior':'archer',
    'class_features':{
        'Arcane_Recovery':True,
        'Spellcasting':True,
        'Spells':[
            ('cantrip', 'Mend'),
            ('cantrip', 'Water_Shape'),
            ('cantrip', 'Mold_Earth'),
            ('ritual', 'Identify'),
            ('ritual', 'Detect_Magic'),
            ('ritual', 'Unseen_Servant'),
            ('1_lvl', 'Shield'),
            ('1_lvl', 'Fog_Cloud'),
            #('1_lvl', 'Sleep'),
            ('1_lvl', 'Magic_Missile'),
            ('1_lvl', 'Absorb_Elements'),
            ],
        },
    'race':'Cat-hero',
    'weapon_skill':['simple'],
    'armor_skill':[],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Goodberry':10,
        'Potion of Antidote':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Rune of Armor':1,
        },
    }

metadict_chars['Wizard 7 lvl (друг) (Тави)'] = {
    'level':7,
    'archer_AI':True,
    'commando_AI':True,
    'fireball_AI':True,
    'squad_advantage':True,
    'char_class':'Wizard',
    'hit_dice':'1d6',
    'behavior':'commander',
    'class_features':{
        # Школа Преобразования. Feat_Resilient за счёт камня преобразования.
        'Feat_Resilient':'constitution',
        'Arcane_Recovery':True,
        'Spellcasting':True,
        'Spells':[
            ('cantrip', 'Mend'),
            ('cantrip', 'Water_Shape'),
            ('cantrip', 'Mold_Earth'),
            ('cantrip', 'Message'),
            ('ritual', 'Identify'),
            ('ritual', 'Detect_Magic'),
            ('ritual', 'Unseen_Servant'),
            ('1_lvl', 'Shield'),
            ('1_lvl', 'Fog_Cloud'),
            #('1_lvl', 'Sleep'),
            ('1_lvl', 'Magic_Missile'),
            ('1_lvl', 'Absorb_Elements'),
            # Не нуждается в Blur, "Идеальное взаимодействие"
            #('2_lvl', 'Blur'),
            ('2_lvl', 'Suggestion'),
            ('2_lvl', 'Hold_Person'),
            ('2_lvl', 'Invisibility'),
            ('3_lvl', 'Counterspell'),
            ('3_lvl', 'Nondetection'),
            ('3_lvl', 'Sending'),
            #('3_lvl', 'Dispel_Magic'),
            # Огнешары неэффективны под водой:
            #('3_lvl', 'Fireball'),
            #('3_lvl', 'Melf_Minute_Meteors'),
            #('4_lvl', 'Ice_Storm'),
            ('4_lvl', 'Arcane_Eye'),
            ('4_lvl', 'Control_Water'),
            #('4_lvl', 'Greater_Invisibility'),
            #('4_lvl', 'Polymorph'),
            ],
        'Ability_Score_Improvement':{
            'intelligence':+2,
            },
        },
    'race':'Cat-hero',
    'weapon_skill':['simple'],
    'armor_skill':[],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Goodberry':10,
        'Potion of Antidote':1,
        'Rune of Absorbtion':1,
        'Rune of Shielding':1,
        'Rune of Armor':1,
        },
    }

#----
# Союзники (армии) (Тави):

metadict_chars['Warrior 1 lvl (друг) (легионер Тави)'] = {
    'level':1,
    'char_class':'Warrior',
    'hit_dice':'1d8',
    'behavior':'warrior',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Potion of Antidote':1,
        'Chain Shirt':1,
        'Heavy Shield':1,
        'Shortsword':1,
        'Pilum':6,
        },
    }

metadict_chars['Warrior 2 lvl (друг) (ветеран Тави)'] = {
    'level':2,
    'char_class':'Warrior',
    'hit_dice':'1d8',
    'behavior':'elite_warrior',
    'class_features':{
        'Fighting_Style_Protection':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Goodberry':4,
        'Potion of Antidote':1,
        'Infusion of Longstrider':1,
        'Infusion of False Life':1,
        'Infusion of Healing':1,
        #'Scale Mail':1,
        'Mage_Armor':1,
        'Heavy Shield':1,
        'Shortsword':1,
        'Pilum':12,
        'Sleep Blade':40,
        },
    }

metadict_chars['Warrior 3 lvl (друг) (сержант Тави)'] = {
    'level':3,
    'char_class':'Warrior',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Protection':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Goodberry':4,
        'Potion of Antidote':1,
        'Infusion of Longstrider':1,
        'Infusion of False Life':1,
        'Rune of Absorbtion':1,
        #'Half Plate':1,
        'Mage_Armor':1,
        'Heavy Shield':1,
        'Shortsword':1,
        'Pilum':12,
        'Sleep Blade':40,
        },
    }

metadict_chars['Warrior 4 lvl (друг) (лейтенант Тави)'] = {
    'level':4,
    'char_class':'Warrior-officer',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Protection':True,
        'Feat_Alert':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Goodberry':4,
        'Potion of Antidote':1,
        'Infusion of Longstrider':1,
        'Infusion of False Life':1,
        'Rune of Absorbtion':1,
        #'Half Plate':1,
        'Mage_Armor':1,
        'Heavy Shield':1,
        'Shortsword':1,
        'Pilum':12,
        'Sleep Blade':40,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Warrior 5 lvl (друг) (капитан Тави)'] = {
    # Командир сотни легионеров, центурион (кентурион).
    'level':5,
    'char_class':'Warrior-officer',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        'Fighting_Style_Protection':True,
        'Extra_Attack':True,
        'Feat_Alert':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Goodberry':4,
        'Potion of Antidote':1,
        'Infusion of Longstrider':1,
        'Infusion of False Life':1,
        'Rune of Absorbtion':1,
        #'Half Plate':1,
        'Mage_Armor':1,
        'Heavy Shield':1,
        'Shortsword':1,
        'Pilum':12,
        'Sleep Blade':40,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }
