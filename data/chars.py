#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Загружаем комплекты снаряжения (soldiers_pack)
from data.items import *

#----
# Лишённые индивидуальности заготовки солдат. Используются в squad_generation

metadict_chars = {}

#----
# Сельское ополчение (крестьяне и городская беднота):

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
        'Hunting Arrow':60,
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
        'Hunting Arrow':60,
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
        'Arrow':60,
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
        'Arrow':60,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    #'Arrow':60,
    #    },
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
        'Javelin':2,
        },
    }

metadict_chars['Warrior 3 lvl (militia swordsman-sergeant)'] = {
    'level':3,
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
        'Javelin':6,
        },
    }

metadict_chars['Warrior 4 lvl (militia swordsman-lieutenant)'] = {
    'level':4,
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
        # Ветераны не обладают боевым стилем. Этому их обучают герои-бойцы.
        #'Fighting_Style_Protection':True,
        #'Fighting_Style_Dueling':True,
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
        #'Fighting_Style_Dueling':True,
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
        #'Fighting_Style_Defence':True,
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
        'Scimitar':1,
        'Shield':1,
        'Pike':1,
        },
    }

metadict_chars['Warrior 2 lvl (city pikeman-corporal)'] = {
    'level':2,
    'char_class':'Warrior',
    'behavior':'elite_warrior',
    'hit_dice':'1d8',
    'class_features':{
        #'Fighting_Style_Defence':True,
        },
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Scale Mail':1,
        'Scimitar':1,
        'Shield':1,
        'Pike':1,
        },
    }

metadict_chars['Warrior 3 lvl (city pikeman-sergeant)'] = {
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
        'Scimitar':1,
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
        'Rune of Absorbtion':1,
        'Breastplate':1,
        'Scimitar':1,
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
    'char_class':'Warrior-officer',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        #'Fighting_Style_Defence':True,
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
        'Scimitar':1,
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
        'Arrow':60,
        },
    }

metadict_chars['Warrior 2 lvl (sqythian bowman-corporal)'] = {
    'level':2,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'archer',
    'class_features':{
        #'Fighting_Style_Archery':True,
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
        'Arrow':60,
        },
    }

metadict_chars['Warrior 3 lvl (sqythian bowman-sergeant)'] = {
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
        'Dagger':1,
        'Longbow':1,
        'Arrow':60,
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
        'Longbow':1,
        'Arrow':60,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    #'Arrow':60,
    #    },
    }

metadict_chars['Warrior 5 lvl (sqythian bowman-captain)'] = {
    'level':5,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        #'Fighting_Style_Archery':True,
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
        'Arrow':60,
        },
    'mount_combat':False,
    'mount_type':'Riding Horse',
    'equipment_mount':{
        #'Arrow':60,
        },
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
        'Arrow':60,
        },
    }

metadict_chars['Warrior 2 lvl (persian bowman-corporal)'] = {
    # Ветераны после 10 лет службы. Мастерски стреляют. Умело сражаются и в ближнем бою.
    'level':2,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'archer',
    'class_features':{
        #'Fighting_Style_Archery':True,
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
        'Arrow':60,
        },
    }

metadict_chars['Warrior 3 lvl (persian bowman-sergeant)'] = {
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
        'Arrow':60,
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
        'Shortbow':1,
        'Arrow':60,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    #'Arrow':60,
    #    },
    }

metadict_chars['Warrior 5 lvl (persian bowman-captain)'] = {
    # Командир сотни наёмных лучников.
    'level':5,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        #'Fighting_Style_Archery':True,
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
        'Arrow':60,
        },
    'mount_combat':False,
    'mount_type':'Riding Horse',
    'equipment_mount':{
        #'Arrow':60,
        },
    }

#----
# Вспомогательные войска, лучники.

metadict_chars['Warrior 1 lvl (cilician infantry)'] = {
    # Так-то стрелки, но склонны к ближнему бою. Пираты.
    'level':1,
    'char_class':'Warrior-bowman',
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
        'Arrow':60,
        },
    }

metadict_chars['Warrior 2 lvl (cilician infantry-corporal)'] = {
    # Используют парное оружие. Своеобразные ребята.
    'level':2,
    'char_class':'Warrior-bowman',
    'hit_dice':'1d8',
    'behavior':'elite_warrior',
    'class_features':{
        #'Fighting_Style_Two_Weapon_Fighting':True,
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
        'Arrow':60,
        },
    }

metadict_chars['Warrior 3 lvl (cilician infantry-sergeant)'] = {
    'level':3,
    'char_class':'Warrior',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        #'Fighting_Style_Two_Weapon_Fighting':True,
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
        'Arrow':60,
        },
    }

metadict_chars['Warrior 4 lvl (cilician infantry-lieutenant)'] = {
    'level':4,
    'char_class':'Warrior-officer',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        #'Fighting_Style_Two_Weapon_Fighting':True,
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
        'Arrow':60,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Warrior 5 lvl (cilician infantry-captain)'] = {
    'level':5,
    'char_class':'Warrior-officer',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        #'Fighting_Style_Two_Weapon_Fighting':True,
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
        'Arrow':60,
        },
    'mount_combat':False,
    'mount_type':'Riding Horse',
    'equipment_mount':{
        },
    }

#----
# Фракийцы.

metadict_chars['Warrior 1 lvl (thracian infantry)'] = {
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
        #'Fighting_Style_Great_Weapon_Fighting':True,
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
        #'Fighting_Style_Great_Weapon_Fighting':True,
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
        #'Fighting_Style_Defence':True,
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
        #'Fighting_Style_Defence':True,
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
        'Shield':1,
        'Shortsword':1,
        'Glaive +1':1,
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
        #'Reckless_Attack':True,
        #'Fighting_Style_Dueling':True,
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
        #'Reckless_Attack':True,
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
        'Javelin':6,
        },
    }

metadict_chars['Warrior 4 lvl (celtian infantry-lieutenant)'] = {
    'level':4,
    'char_class':'Warrior-officer',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        #'Reckless_Attack':True,
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

metadict_chars['Warrior 5 lvl (celtian infantry-captain)'] = {
    'level':5,
    'char_class':'Warrior-officer',
    'hit_dice':'1d8',
    'behavior':'commander',
    'class_features':{
        #'Reckless_Attack':True,
        #'Fighting_Style_Dueling':True,
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
        'Longsword +1':1,
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
        'Arrow':60,
        },
    }

metadict_chars['Warrior 2 lvl (shekelesh infantry-corporal)'] = {
    'level':2,
    'char_class':'Warrior',
    'hit_dice':'1d8',
    'behavior':'elite_warrior',
    'class_features':{
        #'Fighting_Style_Defence':True,
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
        'Arrow':60,
        },
    }

metadict_chars['Warrior 3 lvl (shekelesh infantry-sergeant)'] = {
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
        'Shield':1,
        'Longsword':1,
        'Shortbow':1,
        'Arrow':60,
        },
    }

metadict_chars['Warrior 4 lvl (shekelesh infantry-lieutenant)'] = {
    'level':4,
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
        'Shield':1,
        'Longsword':1,
        'Shortbow':1,
        'Arrow':60,
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
        #'Fighting_Style_Defence':True,
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
        'Arrow':60,
        },
    'mount_combat':False,
    'mount_type':'Riding Horse',
    'equipment_mount':{
        },
    }

#----
# Легион, ромеи

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
        #'Fighting_Style_Protection':True,
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
        #'Fighting_Style_Protection':True,
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
        #'Fighting_Style_Defence':True,
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
        #'Fighting_Style_Great_Weapon_Fighting':True,
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
        #'Fighting_Style_Great_Weapon_Fighting':True,
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
        #'Fighting_Style_Defence':True,
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
# Герои

metadict_chars['Fighter 1 lvl (legionary sentinel-battler)'] = {
    # Бойцы в тяжёлых доспехах.
    # TODO: Feat_Heavy_Armor_Master увеличивает силу на 1. Но он и так занебесно крут.
    'level':1,
    'char_class':'Fighter',
    'hit_dice':'1d10',
    'behavior':'elite_warrior',
    'class_features':{
        'Feat_Heavy_Armor_Master':True,
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
    'char_class':'Eldritch_Knight',
    'hit_dice':'1d10',
    'behavior':'commander',
    'class_features':{
        'Feat_Heavy_Armor_Master':True,
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
        'Ability_Score_Improvement':{
            'intelligence':+2,
            },
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
    'char_class':'Eldritch_Knight',
    'hit_dice':'1d10',
    'behavior':'commander',
    'class_features':{
        'Feat_Heavy_Armor_Master':True,
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
        'Ability_Score_Improvement':{
            'intelligence':+2,
            },
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
    'level':3,
    'char_class':'Fighter',
    'hit_dice':'1d10',
    'behavior':'commander',
    'class_features':{
        'Feat_Great_Weapon_Master':True,
        'Fighting_Style_Great_Weapon_Fighting':True,
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
        'Greatsword':1,
        },
    }

metadict_chars['Fighter 4 lvl (legionary slayer-lieutenant)'] = {
    'level':4,
    'char_class':'Fighter',
    'hit_dice':'1d10',
    'behavior':'commander',
    'class_features':{
        'Feat_Great_Weapon_Master':True,
        'Fighting_Style_Great_Weapon_Fighting':True,
        'Second_Wind':True,
        'Action_Surge':True,
        'Martial_Archetype_Champion':True,
        'Champion_Improved_Critical':True,
        'Ability_Score_Improvement':{
            'strength':+2,
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
    'char_class':'Fighter',
    'hit_dice':'1d10',
    'behavior':'commander',
    'class_features':{
        'Feat_Great_Weapon_Master':True,
        'Fighting_Style_Great_Weapon_Fighting':True,
        'Second_Wind':True,
        'Action_Surge':True,
        'Martial_Archetype_Champion':True,
        'Champion_Improved_Critical':True,
        'Ability_Score_Improvement':{
            'strength':+2,
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
        'Heavy Shield':1,
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
    'level':3,
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
    'class_features':{
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
        'Infusion of Healing':3,
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
        'Infusion of Healing':3,
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
        'Feat_Elemental_Adept':'fire',
        'Otherworldly_Patron':True,
        'Otherworldly_Patron_The_Fiend':True,
        'Pact_Magic':True,
        'Spells':[
            ('cantrip', 'Eldritch_Blast'),
            ('cantrip', 'Thunderclap'),
            #('cantrip', 'Prestidigitation'),
            ('1_lvl', 'Charm_Person'),
            ('1_lvl', 'Burning_Hands'),
            #('1_lvl', 'Arms_of_Hadar'),
            #('1_lvl', 'Cause_Fear'),
            #('1_lvl', 'Hex'),
            #('1_lvl', 'Armor_of_Agathys'),
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
        'Feat_Elemental_Adept':'fire',
        'Otherworldly_Patron':True,
        'Otherworldly_Patron_The_Fiend':True,
        'Pact_Magic':True,
        'Spells':[
            ('cantrip', 'Eldritch_Blast'),
            ('cantrip', 'Thunderclap'),
            ('1_lvl', 'Charm_Person'),
            ('1_lvl', 'Burning_Hands'),
            ('1_lvl', 'Protection_from_Evil_and_Good'),
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
            ('cantrip', 'Prestidigitation'),
            ('cantrip', 'Minor_Illusion'),
            ('cantrip', 'Message'),
            ('2_lvl', 'Charm_Person'),
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
            ('2_lvl', 'Charm_Person'),
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
            ('3_lvl', 'Charm_Person'),
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
        'Invocation_Book of_Ancient_Secrets':True,
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
        'Arrow':60,
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
        'Arrow':60,
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
        'Bard_College':True,
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
        'Arrow':60,
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
        'Bard_College':True,
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
        'Arrow':60,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Bard 5 lvl (otherworld singer-leader)'] = {
    'level':5,
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
        'Bard_College':True,
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
        'Arrow':60,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

#----
# Жрецы -- домен жизни:

metadict_chars['Cleric 1 lvl (city maatcarian-acolyte)'] = {
    # TODO: жрецы домена бури могут вызывать Fog_Cloud и Call_Lightning.
    # Домен природы даёт Plant_Growth и Spike_Growth на 3 lvl жреца.
    # Список заклинания, это уровень жреца, плюс модификатор мудрости.
    'level':1,
    'char_class':'Cleric',
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
        'Healer\'s Kit':1,
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
        'Healer\'s Kit':1,
        'Shortsword':1,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Cleric 3 lvl (city maatcarian-augur)'] = {
    'level':3,
    'char_class':'Cleric',
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
    'char_class':'Cleric',
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
        'Healer\'s Kit':1,
        'Shortsword':1,
        },
    #'mount_combat':False,
    #'mount_type':'Riding Horse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Cleric 5 lvl (city maatcarian-reviver)'] = {
    'level':5,
    'char_class':'Cleric',
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
        'Healer\'s Kit':1,
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
    'char_class':'Cleric-heavy',
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
            ('1_lvl', 'Cure_Wounds'),
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
    'char_class':'Cleric-heavy',
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
            ('1_lvl', 'Cure_Wounds'),
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
    'char_class':'Cleric-heavy',
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
    'char_class':'Cleric-heavy',
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
    'char_class':'Cleric-heavy',
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

metadict_chars['Rogue 2 lvl (city cat-meow)'] = {
    'level':2,
    'char_class':'Rogue',
    'hit_dice':'1d8',
    'behavior':'elite_warrior',
    'class_features':{
        #'Grappler_AI':True,
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
    'class_features':{
        #'Grappler_AI':True,
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
    'char_class':'Arcane_Tricker',
    'hit_dice':'1d8',
    'behavior':'commander',
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
        'Arrow':60,
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
        'Arrow':60,
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
        'Arrow':60,
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
        'Arrow':60,
        },
    #'mount_combat':True,
    #'mount_type':'Light Warhorse',
    #'equipment_mount':{
    #    },
    }

metadict_chars['Rogue 5 lvl (mercenary phantom-captain)'] = {
    'level':5,
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
        'Shortsword +1':1,
        'Longbow +1':1,
        'Arrow':60,
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
        'Favored_Enemy_Humans':True,
        'Natural_Explorer':True,
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
        'Arrow':60,
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
        'Favored_Enemy_Humans':True,
        'Natural_Explorer':True,
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
        'Arrow':60,
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
        'Favored_Enemy_Humans':True,
        'Natural_Explorer':True,
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
        'Arrow':60,
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
        'Favored_Enemy_Humans':True,
        'Natural_Explorer':True,
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
        'Arrow':60,
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
        'Favored_Enemy_Humans':True,
        'Natural_Explorer':True,
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
        'Arrow':60,
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
            ('2_lvl', 'Moonbeam'),
            ('2_lvl', 'Gust_of_Wind'),
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
            ('2_lvl', 'Blur'),
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
            ('2_lvl', 'Blur'),
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
# Паладины (пехота):

