#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Загружаем комплекты снаряжения (soldiers_pack)
from data.items import *

#----
# Болванчики из "Monsters_Manual" и верховые животные:

metadict_animals = {}

#----
# Осадное вооружение:

metadict_animals['Onager'] = {
    # Игромеханически -- ездовые животные
    # Онагр
    'level':5,
    'challenge_rating':'1/4',
    'char_class':'Commoner',
    'behavior':'mount',
    'hitpoints_medial':True,
    'abilityes':{
        'strength':10,
        'dexterity':10,
        'constitution':10, 
        'intelligence':10,
        'wisdom':10,
        'charisma':10,
        },
    'hit_dice':'1d12',
    'race':'Catapult',
    'weapon_skill':[],
    'armor_skill':[],
    'equipment_weapon':{},
    'equipment_backpack':{},
    'equipment_supply':{},
    }

#----
# Ловушки.

metadict_animals['Trap (commander)'] = {
    'level':5,
    'volley_AI':True,
    #'inactive_AI':True,
    'challenge_rating':'1/4',
    'char_class':'Commoner',
    'behavior':'commander',
    'hitpoints_medial':True,
    'class_features':{
        'Feat_Sharpshooter':True,
        },
    'abilityes':{
        'strength':10,
        'dexterity':10,
        'constitution':10, 
        'intelligence':10,
        'wisdom':10,
        'charisma':10,
        },
    'hit_dice':'1d12',
    'race':'Catapult',
    'weapon_skill':['simple','martial'],
    'armor_skill':[],
    'equipment_weapon':{
        #'Glyph (lightning)':1,
        #'Glyph':1,
        },
    'equipment_backpack':{},
    'equipment_supply':{},
    }

metadict_animals['Trap (Glyph of Warding) (Lightning)'] = {
    'level':5,
    'volley_AI':True,
    #'inactive_AI':True,
    'challenge_rating':'1/4',
    'char_class':'Commoner',
    'behavior':'archer',
    'hitpoints_medial':True,
    'class_features':{
        'Feat_Sharpshooter':True,
        },
    'abilityes':{
        'strength':10,
        'dexterity':10,
        'constitution':10, 
        'intelligence':10,
        'wisdom':10,
        'charisma':10,
        },
    'hit_dice':'1d12',
    'race':'Catapult',
    'weapon_skill':['simple','martial'],
    'armor_skill':[],
    'equipment_weapon':{
        'Glyph (lightning)':1,
        'Glyph':1,
        },
    'equipment_backpack':{},
    'equipment_supply':{},
    }

metadict_animals['Trap (Alchemist\'s Fire)'] = {
    'level':5,
    'volley_AI':True,
    #'inactive_AI':True,
    'challenge_rating':'1/4',
    'char_class':'Commoner',
    'behavior':'archer',
    'hitpoints_medial':True,
    'class_features':{
        'Feat_Sharpshooter':True,
        },
    'abilityes':{
        'strength':10,
        'dexterity':10,
        'constitution':10, 
        'intelligence':10,
        'wisdom':10,
        'charisma':10,
        },
    'hit_dice':'1d12',
    'race':'Catapult',
    'weapon_skill':['simple','martial'],
    'armor_skill':[],
    'equipment_weapon':{
        'Trap (fire)':1,
        'Alchemist\'s Fire (100 lb)':1,
        },
    'equipment_backpack':{},
    'equipment_supply':{},
    }

metadict_animals['Trap (Boulders)'] = {
    'level':5,
    'volley_AI':True,
    #'inactive_AI':True,
    'challenge_rating':'1/4',
    'char_class':'Commoner',
    'behavior':'archer',
    'hitpoints_medial':True,
    'class_features':{
        'Feat_Sharpshooter':True,
        },
    'abilityes':{
        'strength':10,
        'dexterity':10,
        'constitution':10, 
        'intelligence':10,
        'wisdom':10,
        'charisma':10,
        },
    'hit_dice':'1d12',
    'race':'Catapult',
    'weapon_skill':['simple','martial'],
    'armor_skill':[],
    'equipment_weapon':{
        'Trap (Boulders)':1,
        'Boulders':1,
        },
    'equipment_backpack':{},
    'equipment_supply':{},
    }

#----
# Предметы:

metadict_animals['Dummy (CR 0)'] = {
    # Просто чучело в броне.
    'level':1,
    'challenge_rating':'0',
    'char_class':'Commoner',
    'behavior':'warrior',
    'inactive_AI':True,
    'hitpoints_medial':True,
    'class_features':{
        'Undead_Fortitude':True,
        },
    'abilityes':{
        'strength':0,
        'dexterity':0,
        'constitution':10,
        'intelligence':0,
        'wisdom':0,
        'charisma':0,
        },
    'hit_dice':'1d8',
    'race':'Human-dummy',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_weapon':{
        #'Ring Mail':1,
        #'Heavy Shield':1,
        },
    'equipment_backpack':{},
    'equipment_supply':{},
    }

metadict_animals['Dummy-officer (CR 0)'] = {
    # Чучело офицера
    'level':3,
    'challenge_rating':'0',
    'char_class':'Commoner',
    'behavior':'commander',
    'inactive_AI':True,
    'hitpoints_medial':True,
    'class_features':{
        'Undead_Fortitude':True,
        },
    'abilityes':{
        'strength':0,
        'dexterity':0,
        'constitution':10,
        'intelligence':0,
        'wisdom':0,
        'charisma':0,
        },
    'hit_dice':'1d8',
    'race':'Human-dummy',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_weapon':{
        #'Splint Armor':1,
        'Ring Mail':1,
        'Heavy Shield':1,
        },
    'equipment_backpack':{},
    'equipment_supply':{},
    }

#----
# Звери (дикий облик друида):

metadict_animals['Giant Octopus (CR 1)'] = {
    # Осьминожки Психеи убивают врагов.
    # https://roll20.net/compendium/dnd5e/Giant%20Octopus
    'level':8,
    'challenge_rating':'1',
    'char_class':'Commoner',
    'behavior':'elite_warrior',
    'hitpoints_medial':True,
    'water_walk':True,
    'hunter_AI':True,
    'killer_AI':True,
    'grappler_AI':True,
    #'fearless_AI':True,
    'class_features':{
        'Hold_Breath':True,
        'Water_Breathing':True,
        'Underwater_Camouflage':True,
        'Ink_Cloud':True,
        },
    'abilityes':{
        'strength':17,
        'dexterity':13,
        'constitution':13, 
        'intelligence':4,
        'wisdom':10,
        'charisma':4,
        },
    'hit_dice':'1d10',
    'attacks':{
        ('close', 'tentacles'): {
            'attack_mod':5,
            'damage_mod':3,
            'weapon': False,
            'weapon_type':['simple', 'close', 'restained'],
            'damage_type':'bludgeoning',
            'damage_dice':'2d6',
            'attack_range':5,
            'attack_type':'close',
            'restained_difficult':16,
            'weapon_skills_use': ['simple'],
            'attack_mod_type':'strength',
            'weapon_of_choice':'tentacles'},
        ('reach', 'tentacles'): {
            # TODO: Досягаемость тентаклей 15 футов, дальше чем копья.
            # Но цель на кораблей, тянемся по диагонали, поэтому 10 футов.
            'attack_mod':5,
            'damage_mod':3,
            'weapon': False,
            'weapon_type':['simple', 'reach', 'restained'],
            'damage_type':'bludgeoning',
            'damage_dice':'2d6',
            'attack_range':10,
            'attack_type':'close',
            'restained_difficult':16,
            'weapon_skills_use': ['simple'],
            'attack_mod_type':'strength',
            'weapon_of_choice':'tentacles'},
        },
    'race':'Giant_octopus',
    'weapon_skill':[],
    'armor_skill':[],
    # TODO: Лучше сделай передачу руны от друида:
    'equipment_weapon':{
            'Rune of Armor':1,
            },
    'equipment_backpack':{},
    'equipment_supply':{},
    }

metadict_animals['Giant Octopus (conjured) (CR 1)'] = {
    # Осьминоги Тик-Бо стараются не убивать.
    # Призванное существо.
    'level':8,
    'challenge_rating':'1',
    'char_class':'Commoner',
    'behavior':'elite_warrior',
    'hitpoints_medial':True,
    'water_walk':True,
    #'killer_AI':True,
    #'hunter_AI':True,
    'grappler_AI':True,
    #'fearless_AI':True,
    'class_features':{
        'Hold_Breath':True,
        'Water_Breathing':True,
        'Underwater_Camouflage':True,
        'Ink_Cloud':True,
        },
    'abilityes':{
        'strength':17,
        'dexterity':13,
        'constitution':13, 
        'intelligence':4,
        'wisdom':10,
        'charisma':4,
        },
    'hit_dice':'1d10',
    'attacks':{
        ('close', 'tentacles'): {
            'attack_mod':5,
            'damage_mod':3,
            'weapon': False,
            'weapon_type':['simple', 'close', 'restained'],
            'damage_type':'bludgeoning',
            'damage_dice':'2d6',
            'attack_range':5,
            'attack_type':'close',
            'restained_difficult':16,
            'weapon_skills_use': ['simple'],
            'attack_mod_type':'strength',
            'weapon_of_choice':'tentacles'},
        ('reach', 'tentacles'): {
            # TODO: Досягаемость тентаклей 15 футов, дальше чем копья.
            # Но цель на кораблей, тянемся по диагонали, поэтому 10 футов.
            'attack_mod':5,
            'damage_mod':3,
            'weapon': False,
            'weapon_type':['simple', 'reach', 'restained'],
            'damage_type':'bludgeoning',
            'damage_dice':'2d6',
            'attack_range':10,
            'attack_type':'close',
            'restained_difficult':16,
            'weapon_skills_use': ['simple'],
            'attack_mod_type':'strength',
            'weapon_of_choice':'tentacles'},
        },
    'race':'Giant_octopus',
    'weapon_skill':[],
    'armor_skill':[],
    'equipment_weapon':{},
    'equipment_backpack':{},
    'equipment_supply':{},
    }

metadict_animals['Giant Octopus (mount) (CR 1)'] = {
    # Призванное существо
    'level':8,
    'challenge_rating':'1',
    'char_class':'Commoner',
    'behavior':'mount',
    'hitpoints_medial':True,
    'water_walk':True,
    #'hunter_AI':True,
    #'killer_AI':True,
    #'grappler_AI':True,
    #'fearless_AI':True,
    'class_features':{
        'Hold_Breath':True,
        'Water_Breathing':True,
        'Underwater_Camouflage':True,
        'Ink_Cloud':True,
        },
    'abilityes':{
        'strength':17,
        'dexterity':13,
        'constitution':13, 
        'intelligence':4,
        'wisdom':10,
        'charisma':4,
        },
    'hit_dice':'1d10',
    'attacks':{
        ('close', 'tentacles'): {
            'attack_mod':5,
            'damage_mod':3,
            'weapon': False,
            'weapon_type':['simple', 'close', 'restained'],
            'damage_type':'bludgeoning',
            'damage_dice':'2d6',
            'attack_range':5,
            'attack_type':'close',
            'restained_difficult':16,
            'weapon_skills_use': ['simple'],
            'attack_mod_type':'strength',
            'weapon_of_choice':'tentacles'},
        ('reach', 'tentacles'): {
            # TODO: Досягаемость тентаклей 15 футов, дальше чем копья.
            # Но цель на кораблей, тянемся по диагонали, поэтому 10 футов.
            'attack_mod':5,
            'damage_mod':3,
            'weapon': False,
            'weapon_type':['simple', 'reach', 'restained'],
            'damage_type':'bludgeoning',
            'damage_dice':'2d6',
            'attack_range':10,
            'attack_type':'close',
            'restained_difficult':16,
            'weapon_skills_use': ['simple'],
            'attack_mod_type':'strength',
            'weapon_of_choice':'tentacles'},
        },
    'race':'Giant_octopus',
    'weapon_skill':[],
    'armor_skill':[],
    'equipment_weapon':{},
    'equipment_backpack':{},
    'equipment_supply':{},
    }

metadict_animals['Brown Bear (CR 1)'] = {
    # https://roll20.net/compendium/dnd5e/Brown%20Bear
    'level':4,
    'challenge_rating':'1',
    'char_class':'Commoner',
    'behavior':'elite_warrior',
    'hitpoints_medial':True,
    #'fearless_AI':True,
    'class_features':{
        'Keen_Smell':True,
        'Extra_Attack':True,
        },
    'abilityes':{
        'strength':19,
        'dexterity':10,
        'constitution':16, 
        'intelligence':2,
        'wisdom':13,
        'charisma':7,
        },
    'hit_dice':'1d10',
    'attacks':{
        ('close', 'claws'): {
            'attack_mod':5,
            'damage_mod':4,
            'weapon': False,
            'weapon_type':['simple'],
            'damage_type':'slashing',
            'damage_dice':'2d6',
            'attack_range':5,
            'attack_type':'close',
            'weapon_skills_use': ['simple'],
            'attack_mod_type':'strength',
            'weapon_of_choice':'claws'},
        ('close', 'bite'): {
            'attack_mod':5,
            'damage_mod':4,
            'weapon': False,
            'weapon_type':['simple'],
            'damage_type':'piercing',
            'damage_dice':'1d8',
            'attack_range':5,
            'attack_type':'close',
            'weapon_skills_use': ['simple'],
            'attack_mod_type':'strength',
            'weapon_of_choice':'bite'},
        },
    'race':'Bear',
    'weapon_skill':[],
    # Медведи в доспехах? Почему бы и нет:
    'armor_skill':['light','medium','heavy'],
    'equipment_weapon':{
            'Rune of Armor':1,
            },
    'equipment_backpack':{},
    'equipment_supply':horse_supply,
    }

#----
# Чудовища из "Monsters_Manual":

metadict_animals['Zombie (CR 1/4)'] = {
    # Зомби.
    'level':3,
    'challenge_rating':'1/4',
    'char_class':'Commoner',
    'behavior':'warrior',
    'fearless_AI':True,
    'hitpoints_medial':True,
    #'grappler_AI':True,
    #'hunter_AI':True,
    #'killer_AI':True,
    'class_features':{
        'Undead_Fortitude':True,
        },
    'abilityes':{
        'strength':13,
        'dexterity':6,
        'constitution':16,
        'intelligence':3,
        'wisdom':6,
        'charisma':5,
        },
    'hit_dice':'1d8',
    'attacks':{
        ('close', 'grasp'): {
            'attack_mod':3,
            'damage_mod':1,
            'weapon': False,
            'weapon_type':['simple'],
            'damage_type':'bludgeoning',
            'damage_dice':'1d6',
            'attack_range':5,
            'attack_type':'close',
            'weapon_skills_use': ['simple'],
            'attack_mod_type':'strength',
            'weapon_of_choice':'grasp'},
        },
    'race':'Human-undead',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_weapon':{
        #'Ring Mail':1,
        },
    'equipment_backpack':{},
    'equipment_supply':{},
    }

metadict_animals['Wight (CR 3)'] = {
    # Умертвие.
    # TODO: Помеха на броски атаки и внимательность при свете солнца.
    'level':6,
    'challenge_rating':'3',
    'char_class':'Warrior-officer',
    'behavior':'commander',
    #'fearless_AI':True,
    'hitpoints_medial':True,
    'sunlight_sensitive':True,
    'class_features':{
        'Extra_Attack':True,
        'Wight_Resistance':True,
        },
    'abilityes':{
        'strength':15,
        'dexterity':14,
        'constitution':16,
        'intelligence':10,
        'wisdom':13,
        'charisma':15,
        },
    'hit_dice':'1d8',
    'attacks':{
        ('close', 'life_drain'): {
            'attack_mod':4,
            'damage_mod':2,
            'weapon': False,
            'weapon_type':['simple', 'drain_max_hp'],
            'damage_type':'necrotic_energy',
            'damage_dice':'1d6',
            'attack_range':5,
            'attack_type':'close',
            'weapon_skills_use': ['simple'],
            'attack_mod_type':'strength',
            'weapon_of_choice':'life_drain'},
        },
    'race':'Human-undead',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_weapon':{
        'Studded Leather':1,
        'Longsword':1,
        'Longbow':1,
        'Arrow':60,
        },
    'equipment_backpack':{},
    'equipment_supply':{},
    }

#----
# Гоблиноиды из Monsters_Manual:

metadict_animals['Goblin (CR 1/4)'] = {
    # Гоблин
    # TODO: расу подправь.
    'level':2,
    'challenge_rating':'1/4',
    'hitpoints_medial':True,
    'char_class':'Rogue',
    'class_features':{
        'Nimble_Escape':True,
        },
    'abilityes':{
        'strength':8,
        'dexterity':14,
        'constitution':10,
        'intelligence':10,
        'wisdom':8,
        'charisma':8,
        },
    'hit_dice':'1d6',
    'behavior':'archer',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Leather Armor':1,
        'Shield':1,
        'Scimitar':1,
        'Shortbow':1,
        'Arrow':60,
        },
    }

metadict_animals['Goblin Boss (CR 1)'] = {
    # Босс гоблинов
    # TODO: расу подправь. Допили способности
    # ------------------------------------------------------------
    # Redirect_Attack меняется местами с соседом по строю. Реакции не требует?
    # ------------------------------------------------------------
    'level':6,
    'challenge_rating':'1',
    'hitpoints_medial':True,
    'char_class':'Rogue',
    'class_features':{
        'Nimble_Escape':True,
        'Redirect_Attack':True,
        },
    'abilityes':{
        'strength':10,
        'dexterity':14,
        'constitution':10,
        'intelligence':10,
        'wisdom':8,
        'charisma':10,
        },
    'hit_dice':'1d6',
    'behavior':'commander',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        # Пока оставим ему короткий лук.
        'Chain Mail':1,
        'Shield':1,
        'Scimitar':1,
        'Shortbow':1,
        'Arrow':60,
        },
    }

metadict_animals['Hobgoblin (CR 1/2)'] = {
    # Хобгоблин
    # TODO: расу подправь. Допили способности
    # ------------------------------------------------------------
    # Martial_Advantage даёт +2d6 урона к удачной атаке, если рядом с врагом союзник.
    # ------------------------------------------------------------
    'level':2,
    'challenge_rating':'1/2',
    'hitpoints_medial':True,
    'char_class':'Rogue',
    'class_features':{
        #'Martial_Advantage':True,
        'Sneak_Attack':True,
        },
    'abilityes':{
        'strength':13,
        'dexterity':12,
        'constitution':12,
        'intelligence':10,
        'wisdom':10,
        'charisma':9,
        },
    'hit_dice':'1d8',
    'behavior':'warrior',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Chain Mail':1,
        'Shield':1,
        'Longsword':1,
        'Longbow':1,
        'Arrow':60,
        },
    }

metadict_animals['Hobgoblin-captain (CR 3)'] = {
    # Капитан хобгоблинов.
    # TODO: расу подправь.
    # ------------------------------------------------------------
    # Martial_Advantage даёт +2d6 урона к удачной атаке, если рядом с врагом союзник.
    # ------------------------------------------------------------
    'level':6,
    'challenge_rating':'1/2',
    'hitpoints_medial':True,
    'char_class':'Rogue',
    'class_features':{
        #'Martial_Advantage':True,
        'Sneak_Attack':True,
        'Extra_Attack':True,
        'Leadership':True,
        },
    'abilityes':{
        'strength':15,
        'dexterity':14,
        'constitution':14,
        'intelligence':12,
        'wisdom':10,
        'charisma':13,
        },
    'hit_dice':'1d8',
    'behavior':'commander',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Splint Armor':1,
        'Greatsword':1,
        'Javelin':6,
        },
    }

metadict_animals['Ork (CR 1/2)'] = {
    # Орк, обычный орк.
    # TODO: расу подправь. Допили способности
    # ------------------------------------------------------------
    # Aggressive. Движение на 30 футов бонусным действием. В engage_action
    # ------------------------------------------------------------
    'level':2,
    'challenge_rating':'1/2',
    'hitpoints_medial':True,
    'char_class':'Warrior',
    'class_features':{
        'Aggressive':True,
        },
    'abilityes':{
        'strength':16,
        'dexterity':12,
        'constitution':16,
        'intelligence':7,
        'wisdom':11,
        'charisma':10,
        },
    'hit_dice':'1d8',
    'behavior':'warrior',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Hide Armor':1,
        'Greataxe':1,
        'Javelin':6,
        },
    }

metadict_animals['Ogre (CR 2)'] = {
    # Огры
    'level':7,
    'challenge_rating':'2',
    'hitpoints_medial':True,
    'char_class':'Warrior',
    'behavior':'elite_warrior',
    #'fearless_AI':True,
    'class_features':{
        },
    'abilityes':{
        'strength':19,
        'dexterity':8,
        'constitution':16,
        'intelligence':5,
        'wisdom':7,
        'charisma':7,
        },
    'hit_dice':'1d8',
    'race':'Humanoid-big',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Hide Armor':1,
        'Maul':1,
        'Javelin':6,
        },
    }

metadict_animals['Orog (CR 2)'] = {
    # Орог. Умный орк.
    # TODO: расу подправь. Допили способности
    # ------------------------------------------------------------
    # Aggressive. Движение на 30 футов бонусным действием. В engage_action
    # ------------------------------------------------------------
    'level':5,
    'challenge_rating':'2',
    'hitpoints_medial':True,
    'char_class':'Warrior',
    'class_features':{
        'Aggressive':True,
        'Extra_Attack':True,
        },
    'abilityes':{
        'strength':18,
        'dexterity':12,
        'constitution':18,
        'intelligence':12,
        'wisdom':11,
        'charisma':12,
        },
    'hit_dice':'1d8',
    'behavior':'commander',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Plate Armor':1,
        'Greataxe':1,
        'Javelin':6,
        },
    }

metadict_animals['Ork war chief (CR 4)'] = {
    # Боевой вождь орков.
    # TODO: расу подправь. Допили способности
    # ------------------------------------------------------------
    # Aggressive. Движение на 30 футов бонусным действием. В engage_action
    # Gruumsh’s Fury. 1d8 дополнительного урона.
    # Battle Cry (1/Day). Преимущество союзникам в радиусе 30 футов на один ход. Плюс бонусная атака.
    # ------------------------------------------------------------
    'level':11,
    'challenge_rating':'4',
    'hitpoints_medial':True,
    'char_class':'Warrior',
    'class_features':{
        'Aggressive':True,
        'Extra_Attack':True,
        },
    'abilityes':{
        'strength':18,
        'dexterity':12,
        'constitution':18,
        'intelligence':11,
        'wisdom':11,
        'charisma':16,
        },
    'hit_dice':'1d8',
    'behavior':'commander',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Chain Mail':1,
        'Greataxe':1,
        'Javelin':6,
        },
    }

metadict_animals['Bugbear (CR 1)'] = {
    # Медвежатник, багбир
    # TODO: расу подправь. Допили способности
    # Это большое существо 2x2 тайла.
    # ------------------------------------------------------------
    # Brute. дополнительная кость урона оружия.
    # Surprise_Attack. лишние 2d6 урона если атакует внезапно.
    # ------------------------------------------------------------
    'level':5,
    'challenge_rating':'1',
    'hitpoints_medial':True,
    'char_class':'Warrior',
    'class_features':{
        'Brute':True,
        'Surprise_Attack':True,
        },
    'abilityes':{
        'strength':15,
        'dexterity':14,
        'constitution':13,
        'intelligence':8,
        'wisdom':11,
        'charisma':9,
        },
    'hit_dice':'1d8',
    'behavior':'commander',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Hide Armor':1,
        'Shield':1,
        'Morningstar':1,
        'Javelin':6,
        },
    }

#----
# Персонажи мастера из Monsters_Manual:

metadict_animals['Sentinel (CR 1/8)'] = {
    # Страж
    'level':2,
    'challenge_rating':'1/8',
    'hitpoints_medial':True,
    'char_class':'Warrior',
    'abilityes':{
        'strength':13,
        'dexterity':12,
        'constitution':12,
        'intelligence':10,
        'wisdom':11,
        'charisma':10,
        },
    'hit_dice':'1d8',
    'behavior':'warrior',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Chain Shirt':1,
        'Shield':1,
        'Spear':1,
        'Javelin':4,
        },
    }

metadict_animals['Bandit (CR 1/8)'] = {
    # Разбойник
    'level':2,
    'challenge_rating':'1/8',
    'hitpoints_medial':True,
    'char_class':'Warrior',
    'abilityes':{
        'strength':11,
        'dexterity':12,
        'constitution':12,
        'intelligence':10,
        'wisdom':10,
        'charisma':10,
        },
    'hit_dice':'1d8',
    'behavior':'warrior',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Leather Armor':1,
        'Scimitar':1,
        'Crossbow, Light':1,
        'Crossbow Bolt':60,
        },
    }

metadict_animals['Thug (CR 1/2)'] = {
    # Головорез
    'level':5,
    'challenge_rating':'1/2',
    'hitpoints_medial':True,
    'char_class':'Warrior',
    'class_features':{
        'Extra_Attack':True,
        },
    'abilityes':{
        'strength':15,
        'dexterity':11,
        'constitution':14,
        'intelligence':10,
        'wisdom':10,
        'charisma':11,
        },
    'hit_dice':'1d8',
    'behavior':'elite_warrior',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Leather Armor':1,
        'Mace':1,
        'Crossbow, Heavy':1,
        'Crossbow Bolt':60,
        },
    }

metadict_animals['Veteran (CR 3)'] = {
    # Ветеран
    'level':9,
    'challenge_rating':'3',
    'hitpoints_medial':True,
    'char_class':'Warrior',
    'class_features':{
        'Fighting_Style_Two_Weapon_Fighting':True,
        'Extra_Attack':True,
        },
    'abilityes':{
        'strength':16,
        'dexterity':13,
        'constitution':14,
        'intelligence':10,
        'wisdom':11,
        'charisma':10,
        },
    'hit_dice':'1d8',
    'behavior':'commander',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Splint Armor':1,
        'Longsword':1,
        'Shortsword':1,
        'Crossbow, Heavy':1,
        'Crossbow Bolt':60,
        },
    }

#----
# Эпические чудовища из Monsters_Manual:

metadict_animals['Empyrean (CR 23)'] = {
    # Эмпирей
    # https://dnd-5e.herokuapp.com/monsters/empyrean
    'level':19,
    'challenge_rating':'23',
    'hitpoints_medial':True,
    'fearless_AI':True,
    'char_class':'Empyrean',
    'class_features':{
        # Вторая атака легендартным действием.
        # Преимущество на спасброски против магии.
        # Unarmored_Defense даёт ему 21 AC, когда должно быть 22.
        'Extra_Attack':True,
        'Unarmored_Defense':True,
        'Legendary_Resistance':True,
        'Spell_Resistance':True,
        'Trembling_Strike':True,
        'Empyrean_Immunity':True,
        'Bolster':True,
        'Spells':[
            # TODO: добавь fire storm
            ('cantrip', 'Empyrean_Bolt'),
            #('2_lvl', 'Scorching_Ray'),
            ('1_lvl', 'Shield'),
            #('2_lvl', 'Shatter'),
            #('2_lvl', 'Melfs_Acid_Arrow'),
            #('2_lvl', 'Cause_Fear'),
            #('3_lvl', 'Fear'),
            #('3_lvl', 'Call_Lightning'),
            #('3_lvl', 'Fireball'),
            #('4_lvl', 'Fireball'),
            #('5_lvl', 'Fireball'),
            ('4_lvl', 'Counterspell'),
            ('5_lvl', 'Counterspell'),
            ]
        },
    'abilityes':{
        'strength':30,
        'dexterity':21,
        'constitution':30,
        'intelligence':21,
        'wisdom':22,
        'charisma':27,
        },
    'hit_dice':'1d12',
    'behavior':'commander',
    'race':'Primevial',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':{},
    'equipment_backpack':{},
    'equipment_weapon':{
        'Empyrean_Maul':1,
        #'Infusion of Healing':1,
        #'Rune of Absorbtion':1,
        #'Rune of Shielding':1,
        },
    }

#----
# Домашние животные, питомцы:

metadict_animals['Riding Horse'] = {
    # Ездовая лошадь.
    # Лошади античности маленькие. 5 век до н.э. -- 134 см. в холке. Считай пони, 200 килограмм.
    # https://www.dandwiki.com/wiki/5e_SRD:Riding_Horse
    'level':2,
    'challenge_rating':'1/4',
    'char_class':'Commoner',
    'behavior':'mount',
    #'hitpoints_medial':True,
    'abilityes':{
        'strength':16,
        'dexterity':10,
        'constitution':12, 
        'intelligence':2,
        'wisdom':11,
        'charisma':7,
        },
    'hit_dice':'1d10',
    'attacks':{
        ('close', 'hooves'): {
            'attack_mod':5,
            'damage_mod':3,
            'weapon': False,
            'weapon_type':['simple'],
            'damage_type':'bludgeoning',
            'damage_dice':'2d4',
            'attack_range':5,
            'attack_type':'close',
            'weapon_skills_use': ['simple'],
            'attack_mod_type':'strength',
            'weapon_of_choice':'hooves'},
        },
    'race':'Horse',
    'weapon_skill':[],
    'armor_skill':[],
    'equipment_weapon':{},
    'equipment_backpack':{},
    'equipment_supply':horse_supply,
    }

metadict_animals['Light Warhorse'] = {
    # Ездовая лошадь.
    # Byzantine warhorse maximum value was -- 10 solidi (48 gp)
    # A cow in ancient Athens cost 50 drachma while a horse cost 1200 drachma (300 gp)
    # Quality war horse and gear: At least ten pounds, up to fifty for a top of the line mount (160-800 gp)
    # https://www.dandwiki.com/wiki/5e_SRD:Riding_Horse
    'level':2,
    'challenge_rating':'1/4',
    'char_class':'Commoner',
    'behavior':'mount',
    #'hitpoints_medial':True,
    'abilityes':{
        'strength':16,
        'dexterity':10,
        'constitution':12, 
        'intelligence':2,
        'wisdom':11,
        'charisma':7,
        },
    'hit_dice':'1d10',
    'attacks':{
        ('close', 'hooves'): {
            'attack_mod':5,
            'damage_mod':3,
            'weapon': False,
            'weapon_type':['simple'],
            'damage_type':'bludgeoning',
            'damage_dice':'2d4',
            'attack_range':5,
            'attack_type':'close',
            'weapon_skills_use': ['simple'],
            'attack_mod_type':'strength',
            'weapon_of_choice':'hooves'},
        },
    'race':'Horse',
    'weapon_skill':[],
    'armor_skill':[],
    'equipment_weapon':{},
    'equipment_backpack':{},
    'equipment_supply':horse_supply,
    }

metadict_animals['Warhorse'] = {
    # Боевой конь.
    # https://www.dandwiki.com/wiki/5e_SRD:Warhorse
    'level':3,
    'challenge_rating':'1/2',
    'char_class':'Commoner',
    'behavior':'mount',
    #'hitpoints_medial':True,
    'abilityes':{
        'strength':18,
        'dexterity':12,
        'constitution':13, 
        'intelligence':3,
        'wisdom':12,
        'charisma':7,
        },
    'hit_dice':'1d10',
    'attacks':{
        ('close', 'hooves'): {
            'attack_mod':6,
            'damage_mod':4,
            'weapon': False,
            'weapon_type':['simple'],
            'damage_type':'bludgeoning',
            'damage_dice':'2d6',
            'attack_range':5,
            'attack_type':'close',
            'weapon_skills_use': ['simple'],
            'attack_mod_type':'strength',
            'weapon_of_choice':'hooves'},
        },
    'race':'Horse',
    'weapon_skill':[],
    # Боевых коней учат бегать в доспехах:
    'armor_skill':['light','medium','heavy'],
    'equipment_weapon':{},
    'equipment_backpack':{},
    'equipment_supply':horse_supply,
    }

metadict_animals['Horseclaw'] = {
    # Когте-конь, когтеклюв, страус, чокобо.
    # https://www.dandwiki.com/wiki/Chocobo_(3.5e_Creature)
    'level':3,
    'challenge_rating':'1/2',
    'char_class':'Commoner',
    'behavior':'mount',
    #'hitpoints_medial':True,
    'abilityes':{
        'strength':18,
        'dexterity':15,
        'constitution':14, 
        'intelligence':2,
        'wisdom':11,
        'charisma':7,
        },
    'hit_dice':'1d10',
    'attacks':{
        ('close', 'claws'): {
            'attack_mod':6,
            'damage_mod':4,
            'weapon': False,
            'weapon_type':['simple'],
            'damage_type':'piercing',
            'damage_dice':'2d6',
            'attack_range':5,
            'attack_type':'close',
            'weapon_skills_use': ['simple'],
            'attack_mod_type':'strength',
            'weapon_of_choice':'claws'},
        },
    'race':'Horseclaw',
    'weapon_skill':[],
    # Чокобо учат бегать в доспехах:
    'armor_skill':['light','medium','heavy'],
    'equipment_weapon':{},
    'equipment_backpack':{},
    'equipment_supply':horse_supply,
    }
