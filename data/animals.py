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
    'mechanism':True,
    'challenge_rating':'-',
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
    'race':'Object-wood-big',
    'weapon_skill':[],
    'armor_skill':[],
    'equipment_weapon':{},
    'equipment_backpack':{},
    'equipment_supply':{},
    }

#----
# Объекты.

metadict_animals['Palisade (wood)'] = {
    # Частокол, палисад
    'level':10,
    'mechanism':True,
    'ignore_damage':15,
    'savethrow_autofall':True,
    'inactive_AI':True,
    'challenge_rating':'-',
    'char_class':'Commoner',
    'behavior':'commander',
    'hitpoints_medial':True,
    'class_features':{
        'Wood_Object_Resistance':True,
        },
    'abilityes':{
        'strength':10,
        'dexterity':10,
        'constitution':10, 
        'intelligence':10,
        'wisdom':10,
        'charisma':10,
        },
    'hit_dice':'1d10',
    'race':'Object-wood-big',
    'weapon_skill':[],
    'armor_skill':[],
    'equipment_weapon':{},
    'equipment_backpack':{},
    'equipment_supply':{},
    }

metadict_animals['Wall (stone)'] = {
    # Крепостная стена, каменная стена
    'level':20,
    'mechanism':True,
    'ignore_damage':30,
    'savethrow_autofall':True,
    'inactive_AI':True,
    'challenge_rating':'-',
    'char_class':'Commoner',
    'behavior':'commander',
    'hitpoints_medial':True,
    'class_features':{
        'Earth_Elemental_Resistance':True,
        'Earth_Elemental_Vulnerability':True,
        },
    'abilityes':{
        'strength':10,
        'dexterity':10,
        'constitution':10, 
        'intelligence':10,
        'wisdom':10,
        'charisma':10,
        },
    'hit_dice':'1d10',
    'race':'Object-stone-big',
    'weapon_skill':[],
    'armor_skill':[],
    'equipment_weapon':{},
    'equipment_backpack':{},
    'equipment_supply':{},
    }

metadict_animals['Bridge-support (stone)'] = {
    # Каменная опора моста
    'level':10,
    'mechanism':True,
    'ignore_damage':20,
    'savethrow_autofall':True,
    'inactive_AI':True,
    'challenge_rating':'-',
    'char_class':'Commoner',
    'behavior':'commander',
    'hitpoints_medial':True,
    'class_features':{
        'Earth_Elemental_Resistance':True,
        'Earth_Elemental_Vulnerability':True,
        },
    'abilityes':{
        'strength':10,
        'dexterity':10,
        'constitution':10, 
        'intelligence':10,
        'wisdom':10,
        'charisma':10,
        },
    'hit_dice':'1d10',
    'race':'Object-stone-big',
    'weapon_skill':[],
    'armor_skill':[],
    'equipment_weapon':{},
    'equipment_backpack':{},
    'equipment_supply':{},
    }

metadict_animals['Bridge (stone)'] = {
    # Пролёт моста
    'level':5,
    'mechanism':True,
    'ignore_damage':20,
    'savethrow_autofall':True,
    'inactive_AI':True,
    'challenge_rating':'-',
    'char_class':'Commoner',
    'behavior':'warrior',
    'hitpoints_medial':True,
    'class_features':{
        'Earth_Elemental_Resistance':True,
        'Earth_Elemental_Vulnerability':True,
        },
    'abilityes':{
        'strength':10,
        'dexterity':10,
        'constitution':10, 
        'intelligence':10,
        'wisdom':10,
        'charisma':10,
        },
    'hit_dice':'1d10',
    'race':'Object-stone-big',
    'weapon_skill':[],
    'armor_skill':[],
    'equipment_weapon':{},
    'equipment_backpack':{},
    'equipment_supply':{},
    }

#----
# Корабли.

metadict_animals['Ship trireme (deck)'] = {
    # Палуба триеры. Порог урона -- 10
    'level':5,
    'mechanism':True,
    'ignore_damage':10,
    'savethrow_autofall':True,
    'inactive_AI':True,
    'challenge_rating':'-',
    'char_class':'Commoner',
    'behavior':'warrior',
    'hitpoints_medial':True,
    'class_features':{
        'Wood_Object_Resistance':True,
        },
    'abilityes':{
        'strength':10,
        'dexterity':10,
        'constitution':10, 
        'intelligence':10,
        'wisdom':10,
        'charisma':10,
        },
    'hit_dice':'1d10',
    'race':'Object-wood-ship-part',
    'weapon_skill':[],
    'armor_skill':[],
    'equipment_weapon':{},
    'equipment_backpack':{},
    'equipment_supply':{},
    }

metadict_animals['Ship trireme (board)'] = {
    # Борт триеры.
    'level':5,
    'mechanism':True,
    'ignore_damage':20,
    'savethrow_autofall':True,
    'inactive_AI':True,
    'challenge_rating':'-',
    'char_class':'Commoner',
    'behavior':'elite_warrior',
    'hitpoints_medial':True,
    'class_features':{
        'Wood_Object_Resistance':True,
        },
    'abilityes':{
        'strength':10,
        'dexterity':10,
        'constitution':10, 
        'intelligence':10,
        'wisdom':10,
        'charisma':10,
        },
    'hit_dice':'1d10',
    'race':'Object-wood-ship-part',
    'weapon_skill':[],
    'armor_skill':[],
    'equipment_weapon':{},
    'equipment_backpack':{},
    'equipment_supply':{},
    }

metadict_animals['Ship trireme (command)'] = {
    # Нос и корма триеры.
    'level':10,
    'mechanism':True,
    'ignore_damage':20,
    'inactive_AI':True,
    'challenge_rating':'1',
    'char_class':'Commoner',
    'behavior':'commander',
    'hitpoints_medial':True,
    'class_features':{
        'Wood_Object_Resistance':True,
        },
    'abilityes':{
        'strength':10,
        'dexterity':10,
        'constitution':10, 
        'intelligence':10,
        'wisdom':10,
        'charisma':10,
        },
    'hit_dice':'1d10',
    'race':'Object-wood-ship-part',
    'weapon_skill':[],
    'armor_skill':[],
    'equipment_weapon':{},
    'equipment_backpack':{},
    'equipment_supply':{},
    }

metadict_animals['Ship pentere (deck)'] = {
    # Палуба пентеры.
    'level':5,
    'mechanism':True,
    'ignore_damage':15,
    'savethrow_autofall':True,
    'inactive_AI':True,
    'challenge_rating':'-',
    'char_class':'Commoner',
    'behavior':'warrior',
    'hitpoints_medial':True,
    'class_features':{
        'Wood_Object_Resistance':True,
        },
    'abilityes':{
        'strength':10,
        'dexterity':10,
        'constitution':10, 
        'intelligence':10,
        'wisdom':10,
        'charisma':10,
        },
    'hit_dice':'1d10',
    'race':'Object-wood-ship-part',
    'weapon_skill':[],
    'armor_skill':[],
    'equipment_weapon':{},
    'equipment_backpack':{},
    'equipment_supply':{},
    }

metadict_animals['Ship pentere (board)'] = {
    # Борт пентеры. Больше хитов.
    'level':10,
    'mechanism':True,
    'ignore_damage':20,
    'savethrow_autofall':True,
    'inactive_AI':True,
    'challenge_rating':'-',
    'char_class':'Commoner',
    'behavior':'elite_warrior',
    'hitpoints_medial':True,
    'class_features':{
        'Wood_Object_Resistance':True,
        },
    'abilityes':{
        'strength':10,
        'dexterity':10,
        'constitution':10, 
        'intelligence':10,
        'wisdom':10,
        'charisma':10,
        },
    'hit_dice':'1d10',
    'race':'Object-wood-ship-part',
    'weapon_skill':[],
    'armor_skill':[],
    'equipment_weapon':{},
    'equipment_backpack':{},
    'equipment_supply':{},
    }

metadict_animals['Ship pentere (command)'] = {
    # Нос и корма пентеры.
    'level':10,
    'mechanism':True,
    'ignore_damage':20,
    'inactive_AI':True,
    'challenge_rating':'1',
    'char_class':'Commoner',
    'behavior':'commander',
    'hitpoints_medial':True,
    'class_features':{
        'Wood_Object_Resistance':True,
        },
    'abilityes':{
        'strength':10,
        'dexterity':10,
        'constitution':10, 
        'intelligence':10,
        'wisdom':10,
        'charisma':10,
        },
    'hit_dice':'1d10',
    'race':'Object-wood-ship-part',
    'weapon_skill':[],
    'armor_skill':[],
    'equipment_weapon':{},
    'equipment_backpack':{},
    'equipment_supply':{},
    }

metadict_animals['Ship trage (deck)'] = {
    # Палуба торгового корабля.
    'level':5,
    'mechanism':True,
    'ignore_damage':10,
    'savethrow_autofall':True,
    'inactive_AI':True,
    'challenge_rating':'-',
    'char_class':'Commoner',
    'behavior':'warrior',
    'hitpoints_medial':True,
    'class_features':{
        'Wood_Object_Resistance':True,
        },
    'abilityes':{
        'strength':10,
        'dexterity':10,
        'constitution':10, 
        'intelligence':10,
        'wisdom':10,
        'charisma':10,
        },
    'hit_dice':'1d10',
    'race':'Object-wood-ship-part',
    'weapon_skill':[],
    'armor_skill':[],
    'equipment_weapon':{},
    'equipment_backpack':{},
    'equipment_supply':{},
    }

metadict_animals['Ship trage (board)'] = {
    'level':5,
    'mechanism':True,
    'ignore_damage':18,
    'savethrow_autofall':True,
    'inactive_AI':True,
    'challenge_rating':'-',
    'char_class':'Commoner',
    'behavior':'elite_warrior',
    'hitpoints_medial':True,
    'class_features':{
        'Wood_Object_Resistance':True,
        },
    'abilityes':{
        'strength':10,
        'dexterity':10,
        'constitution':10, 
        'intelligence':10,
        'wisdom':10,
        'charisma':10,
        },
    'hit_dice':'1d10',
    'race':'Object-wood-ship-part',
    'weapon_skill':[],
    'armor_skill':[],
    'equipment_weapon':{},
    'equipment_backpack':{},
    'equipment_supply':{},
    }

metadict_animals['Ship trage (command)'] = {
    'level':5,
    'mechanism':True,
    'ignore_damage':15,
    'inactive_AI':True,
    'challenge_rating':'1',
    'char_class':'Commoner',
    'behavior':'commander',
    'hitpoints_medial':True,
    'class_features':{
        'Wood_Object_Resistance':True,
        },
    'abilityes':{
        'strength':10,
        'dexterity':10,
        'constitution':10, 
        'intelligence':10,
        'wisdom':10,
        'charisma':10,
        },
    'hit_dice':'1d10',
    'race':'Object-wood-ship-part',
    'weapon_skill':[],
    'armor_skill':[],
    'equipment_weapon':{},
    'equipment_backpack':{},
    'equipment_supply':{},
    }

#----
# Непогода.

metadict_animals['Weather (lightning)'] = {
    'level':5,
    'volley_AI':True,
    'mechanism':True,
    'challenge_rating':'-',
    'char_class':'Commoner',
    'behavior':'archer',
    'hitpoints_medial':True,
    'abilityes':{
        'strength':10,
        'dexterity':10,
        'constitution':10, 
        'intelligence':10,
        'wisdom':10,
        'charisma':10,
        },
    'hit_dice':'1d10',
    'attacks':{
        ('volley', 'Lightning'): {
            'attack_mod':5,
            'damage_mod':0,
            'weapon': False,
            'direct_hit':True,
            'weapon_type':['simple','ranged','volley','artillery','burning_shell'],
            'spell_dict':{
                    'zone':True,
                    'zone_shape':'2x2',
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_ability':'dexterity',
                    'attacks_number':1,
                    'attack_range':600,
                    'radius':5,
                    'damage_type':'lightning',
                    'damage_dice':'3d10',
                    'components':[],
                    'casting_time':'action',
                    'damage_mod':0,
                    'spell_level':3,
                    'spell_save_DC':15,
                    'spell_choice':('storm','Lightning'),
                    },
            'damage_type':'lightning',
            'damage_dice':'0d0',
            'ammo':1000,
            'attack_range':150,
            'attack_range_max':600,
            'weapon_skills_use': ['simple'],
            'attack_mod_type':'strength',
            'weapon_of_choice':'Lightning'},
        },
    'race':'Object-wood-ship-part',
    'weapon_skill':[],
    'armor_skill':[],
    'equipment_weapon':{},
    'equipment_backpack':{},
    'equipment_supply':{},
    }

metadict_animals['Weather (waves)'] = {
    # TODO:
    # Корабль без управления всегда проваливает спасброски,
    # Корабль с капитаном и рулевым на палубе бросает капитанские спасброски ловкости.
    'level':5,
    'volley_AI':True,
    'mechanism':True,
    'challenge_rating':'-',
    'char_class':'Commoner',
    'behavior':'archer',
    'hitpoints_medial':True,
    'abilityes':{
        'strength':10,
        'dexterity':10,
        'constitution':10, 
        'intelligence':10,
        'wisdom':10,
        'charisma':10,
        },
    'hit_dice':'1d10',
    'attacks':{
        ('volley', 'Waves'): {
            'attack_mod':5,
            'damage_mod':0,
            'weapon': True,
            'direct_hit':True,
            'weapon_type':['simple','ranged','volley','artillery','burning_shell'],
            'spell_dict':{
                    'zone':True,
                    #'zone_shape':'2x2',
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_ability':'dexterity',
                    'attacks_number':1,
                    'attack_range':600,
                    'radius':120,
                    'damage_type':'bludgeoning',
                    # Удвоенный урон сооружениям:
                    'weapon_type':['siege'],
                    'damage_dice':'2d6',
                    'components':[],
                    'casting_time':'action',
                    'damage_mod':0,
                    'spell_level':3,
                    'spell_save_DC':15,
                    'spell_choice':('storm','Waves'),
                    },
            'damage_type':'bludgeoning',
            'damage_dice':'0d0',
            'ammo':1000,
            'attack_range':150,
            'attack_range_max':600,
            'weapon_skills_use': ['simple'],
            'attack_mod_type':'strength',
            'weapon_of_choice':'Waves'},
        },
    'race':'Object-wood-ship-part',
    'weapon_skill':[],
    'armor_skill':[],
    'equipment_weapon':{},
    'equipment_backpack':{},
    'equipment_supply':{},
    }

metadict_animals['Weather (storm-god)'] = {
    'level':19,
    'volley_AI':True,
    'volley_AI_random':True,
    #'inactive_AI':True,
    'challenge_rating':'23',
    'hitpoints_medial':True,
    'fearless_AI':True,
    'char_class':'Empyrean',
    'class_features':{
        'Extra_Attack':True,
        'Unarmored_Defense':True,
        'Legendary_Resistance':True,
        'Spell_Resistance':True,
        'Trembling_Strike':True,
        'Empyrean_Immunity':True,
        'Bolster':True,
        'Spells':[
            ('cantrip', 'Empyrean_Bolt'),
            ('1_lvl', 'Shield'),
            ('2_lvl', 'Absorb_Elements'),
            ('3_lvl', 'Counterspell'),
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
    'race':'Primevial-large',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':{},
    'equipment_backpack':{},
    'equipment_weapon':{
        'Empyrean_Maul':1,
        },
    }

#----
# Ловушки.

metadict_animals['Trap (commander)'] = {
    'level':5,
    'volley_AI':True,
    'seeker_AI':True,
    'fearless_AI':True,
    'no_grappler_AI':True,
    #'inactive_AI':True,
    'challenge_rating':'-',
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
    'race':'Object-wood-big',
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
    'challenge_rating':'-',
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
    'race':'Object-wood-big',
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
    'challenge_rating':'-',
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
    'race':'Object-wood-big',
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
    'challenge_rating':'-',
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
    'race':'Object-wood-big',
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
    'challenge_rating':'-',
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
    'challenge_rating':'-',
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
    #'seeker_AI':True,
    #'killer_AI':True,
    'hunter_AI':True,
    'grappler_AI':True,
    'fearless_AI':True,
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

metadict_animals['Giant Octopus (commander) (CR 1)'] = {
    # Призванное существо.
    'level':8,
    'challenge_rating':'1',
    'char_class':'Commoner',
    'behavior':'commander',
    'hitpoints_medial':True,
    'water_walk':True,
    #'seeker_AI':True,
    #'killer_AI':True,
    'hunter_AI':True,
    'grappler_AI':True,
    'fearless_AI':True,
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
    #'seeker_AI':True,
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

metadict_animals['Mastiff, dog (CR 1/8)'] = {
    # TODO: могут сбить с ног
    # https://roll20.net/compendium/dnd5e/Mastiff
    'level':1,
    'challenge_rating':'1/8',
    'char_class':'Commoner',
    'behavior':'warrior',
    'hitpoints_medial':True,
    #'fearless_AI':True,
    'grappler_AI':True,
    'seeker_AI':True,
    'predator_AI':True,
    'class_features':{
        'Keen_Smell':True,
        },
    'abilityes':{
        'strength':13,
        'dexterity':14,
        'constitution':12, 
        'intelligence':3,
        'wisdom':12,
        'charisma':7,
        },
    'hit_dice':'1d8',
    'attacks':{
        ('close', 'bite'): {
            'attack_mod':3,
            'damage_mod':1,
            'weapon': False,
            'weapon_type':['simple'],
            'damage_type':'piercing',
            'damage_dice':'1d6',
            'attack_range':5,
            'attack_type':'close',
            'weapon_skills_use': ['simple'],
            'attack_mod_type':'strength',
            'weapon_of_choice':'bite'},
        },
    'race':'Dog',
    'weapon_skill':[],
    'armor_skill':['light','medium','heavy'],
    'equipment_weapon':{
            },
    'equipment_backpack':{},
    'equipment_supply':{},
    }

metadict_animals['Mastiff, big-dog (CR 1/2)'] = {
    # TODO: переделай в лютоволка.
    'level':3,
    'challenge_rating':'1/2',
    'char_class':'Commoner',
    'behavior':'commander',
    'hitpoints_medial':True,
    'fearless_AI':True,
    'grappler_AI':True,
    'seeker_AI':True,
    'predator_AI':True,
    'class_features':{
        'Keen_Smell':True,
        },
    'abilityes':{
        'strength':18,
        'dexterity':18,
        'constitution':18, 
        'intelligence':3,
        'wisdom':14,
        'charisma':7,
        },
    'hit_dice':'1d10',
    'attacks':{
        ('close', 'bite'): {
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
            'weapon_of_choice':'bite'},
        },
    'race':'Dog',
    'weapon_skill':[],
    'armor_skill':['light','medium','heavy'],
    'equipment_weapon':{
            },
    'equipment_backpack':{},
    'equipment_supply':{},
    }

#----
# Чудовища из "Monsters_Manual":

metadict_animals['Zombie (CR 1/4)'] = {
    # Зомби.
    'level':3,
    'fearless_AI':True,
    'challenge_rating':'1/4',
    'char_class':'Commoner',
    'behavior':'warrior',
    'hitpoints_medial':True,
    #'grappler_AI':True,
    #'predator_AI':True,
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

metadict_animals['Zombie (Danse_Macabre) (CR 1/2)'] = {
    # TODO: сделай помеху атакам, если броня тяжелее лёгкой.
    # Зомби с кучей усилений.
    'level':3,
    'killer_AI':True,
    'predator_AI':True,
    'fearless_AI':True,
    'bonus_hitpoints':10,
    'challenge_rating':'1/2',
    #'squad_disadvantage':True,
    'char_class':'Commoner',
    'behavior':'warrior',
    'hitpoints_medial':True,
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
            # +5 атаки/урона от Danse_Macabre
            # +4 урона от школы некромантии
            'attack_mod':3 + 5,
            'damage_mod':1 + 5 + 4,
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
        'Studded Leather':1,
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
# Призванные существа, элементали:

metadict_animals['Air Elemental (CR 5)'] = {
    'level':12,
    'killer_AI':True,
    'seeker_AI':True,
    #'hunter_AI':True,
    #'predator_AI':True,
    'fearless_AI':True,
    'no_grappler_AI':True,
    'air_walk':True,
    'water_walk':True,
    'challenge_rating':'5',
    'char_class':'Warrior',
    'behavior':'commander',
    'hitpoints_medial':True,
    'class_features':{
        'Extra_Attack':True,
        'Air_Elemental_Resistance':True,
        'Air_Form':True,
        'Recharge':True,
        'Recharge_dice':'1d6',
        'Recharge_numbers':[4,5,6],
        },
    'abilityes':{
        'strength':14,
        'dexterity':20,
        'constitution':14,
        'intelligence':6,
        'wisdom':10,
        'charisma':6,
        },
    'hit_dice':'1d10',
    'attacks':{
        ('close', 'slam'): {
            'attack_mod':8,
            'damage_mod':5,
            'weapon': False,
            'weapon_type':['simple','close'],
            'damage_type':'bludgeoning',
            'damage_dice':'2d8',
            'attack_range':5,
            'attack_type':'close',
            'weapon_skills_use': ['simple'],
            'attack_mod_type':'dexterity',
            'weapon_of_choice':'whirlwind'},
        ('close', 'whirlwind'): {
            # TODO добавь отбрасывание и сбивание с ног.
            'attack_mod':8,
            'damage_mod':0,
            'direct_hit':True,
            'savethrow':True,
            'savethrow_ability':'strength',
            'weapon': False,
            'weapon_type':['simple','close'],
            'spell_dict':{
                    'zone':True,
                    'effect':'move',
                    'zone_shape':'2x2',
                    #'zone_shape':'square',
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_ability':'strength',
                    'attacks_number':1,
                    'attack_range':5,
                    'radius':5,
                    'damage_type':'bludgeoning',
                    'damage_dice':'3d8',
                    'components':[],
                    'casting_time':'bonus_action',
                    'damage_mod':2,
                    'spell_level':1,
                    'spell_save_DC':13,
                    'spell_choice':('subspell','whirlwind'),
                    },
            'damage_type':'bludgeoning',
            'damage_dice':'0d0',
            'ammo':1,
            'attack_range':5,
            'attack_type':'close',
            'weapon_skills_use': [],
            'attack_mod_type':'dexterity',
            'weapon_of_choice':'whirlwind'},
        },
    'race':'Elemental-air',
    'weapon_skill':[],
    'armor_skill':[],
    'equipment_weapon':{},
    'equipment_backpack':{},
    'equipment_supply':{},
    }

metadict_animals['Earth Elemental (CR 5)'] = {
    # TODO: уязвимость к урону звуком.
    # TODO: сделай особенность оружия "siege". Удвоенный урон предметам.
    'level':12,
    'killer_AI':True,
    'seeker_AI':True,
    #'hunter_AI':True,
    #'predator_AI':True,
    'fearless_AI':True,
    'no_grappler_AI':True,
    'challenge_rating':'5',
    'char_class':'Warrior',
    'behavior':'commander',
    'hitpoints_medial':True,
    'class_features':{
        'Extra_Attack':True,
        'Earth_Elemental_Resistance':True,
        'Earth_Elemental_Vulnerability':True,
        'Earth_Glide':True,
        'Siege_Monster':True,
        },
    'abilityes':{
        'strength':20,
        'dexterity':8,
        'constitution':20,
        'intelligence':5,
        'wisdom':10,
        'charisma':5,
        },
    'hit_dice':'1d10',
    'attacks':{
        ('close', 'slam'): {
            'attack_mod':8,
            'damage_mod':5,
            'weapon': False,
            'weapon_type':['simple','close','siege'],
            'damage_type':'bludgeoning',
            'damage_dice':'2d8',
            'attack_range':5,
            'attack_type':'close',
            'weapon_skills_use': ['simple'],
            'attack_mod_type':'strength',
            'weapon_of_choice':'slam'},
        ('reach', 'slam'): {
            'attack_mod':8,
            'damage_mod':5,
            'weapon': False,
            'weapon_type':['simple','reach','siege'],
            'damage_type':'bludgeoning',
            'damage_dice':'2d8',
            'attack_range':10,
            'attack_type':'reach',
            'weapon_skills_use': ['simple'],
            'attack_mod_type':'strength',
            'weapon_of_choice':'slam'},
        },
    'race':'Elemental-earth',
    'weapon_skill':[],
    'armor_skill':[],
    'equipment_weapon':{},
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
# Тестовые существа:

metadict_animals['Warrior 1 lvl (standard) (Shortbow) (archery)'] = {
    'level':1,
    'challenge_rating':'1/8',
    'char_class':'Commoner',
    'behavior':'archer',
    'seeker_AI':True,
    'fearless_AI':True,
    'hitpoints_base':10,
    'class_features':{
        'Fighting_Style_Archery':True,
        },
    'abilityes':{
        'strength':10,
        'dexterity':10,
        'constitution':10,
        'intelligence':10,
        'wisdom':10,
        'charisma':10,
        },
    'hit_dice':'1d8',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_weapon':{
        'Ring Mail':1,
        'Shortbow':1,
        'Arrow':60,
        },
    'equipment_backpack':{},
    'equipment_supply':{},
    }

metadict_animals['Warrior 1 lvl (standard) (Shortbow)'] = {
    'level':1,
    'challenge_rating':'1/8',
    'char_class':'Commoner',
    'behavior':'archer',
    'seeker_AI':True,
    'fearless_AI':True,
    'hitpoints_base':10,
    #'class_features':{
    #    'Fighting_Style_Archery':True,
    #    },
    'abilityes':{
        'strength':10,
        'dexterity':10,
        'constitution':10,
        'intelligence':10,
        'wisdom':10,
        'charisma':10,
        },
    'hit_dice':'1d8',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_weapon':{
        'Ring Mail':1,
        'Shortbow':1,
        'Arrow':60,
        },
    'equipment_backpack':{},
    'equipment_supply':{},
    }

metadict_animals['Warrior 1 lvl (standard) (Greataxe)'] = {
    # Боец средних параметров с Greataxe.
    'level':1,
    'challenge_rating':'1/8',
    'char_class':'Commoner',
    'behavior':'warrior',
    'seeker_AI':True,
    'fearless_AI':True,
    'hitpoints_base':10,
    'abilityes':{
        'strength':10,
        'dexterity':10,
        'constitution':10,
        'intelligence':10,
        'wisdom':10,
        'charisma':10,
        },
    'hit_dice':'1d8',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_weapon':{
        'Ring Mail':1,
        'Greataxe':1,
        },
    'equipment_backpack':{},
    'equipment_supply':{},
    }

metadict_animals['Warrior 1 lvl (standard) (disadvantage) (Greataxe)'] = {
    # Боец средних параметров с Greataxe.
    'level':1,
    'challenge_rating':'1/8',
    'char_class':'Commoner',
    'behavior':'warrior',
    'seeker_AI':True,
    'fearless_AI':True,
    'squad_disadvantage':True,
    'hitpoints_base':10,
    'abilityes':{
        'strength':10,
        'dexterity':10,
        'constitution':10,
        'intelligence':10,
        'wisdom':10,
        'charisma':10,
        },
    'hit_dice':'1d8',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_weapon':{
        'Ring Mail':1,
        'Greataxe':1,
        },
    'equipment_backpack':{},
    'equipment_supply':{},
    }

metadict_animals['Warrior 1 lvl (standard) (bless + disadvantage) (Greataxe)'] = {
    'level':1,
    'challenge_rating':'1/8',
    'char_class':'Commoner',
    'behavior':'warrior',
    'seeker_AI':True,
    'fearless_AI':True,
    'squad_disadvantage':True,
    'hitpoints_base':10,
    'abilityes':{
        'strength':10,
        'dexterity':10,
        'constitution':10,
        'intelligence':10,
        'wisdom':10,
        'charisma':10,
        },
    'class_features':{
        'Feat_Magic_Initiate':True,
        'Spellcasting':True,
        'Spells':[
            ('1_lvl', 'Bless'),
            ],
        },
    'hit_dice':'1d8',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_weapon':{
        'Ring Mail':1,
        'Greataxe':1,
        },
    'equipment_backpack':{},
    'equipment_supply':{},
    }

metadict_animals['Warrior 1 lvl (standard) (Battleaxe + Shield)'] = {
    # Боец средних параметров с Greataxe.
    'level':1,
    'challenge_rating':'1/8',
    'char_class':'Commoner',
    'behavior':'warrior',
    'seeker_AI':True,
    'fearless_AI':True,
    'hitpoints_base':10,
    'abilityes':{
        'strength':10,
        'dexterity':10,
        'constitution':10,
        'intelligence':10,
        'wisdom':10,
        'charisma':10,
        },
    'hit_dice':'1d8',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_weapon':{
        'Ring Mail':1,
        'Battleaxe':1,
        'Shield':1,
        },
    'equipment_backpack':{},
    'equipment_supply':{},
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
    'race':'Primevial-large',
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

#----
# Homebrew: дактили (датикили)

metadict_animals['Дактиль-кусатель (CR 1/2)'] = {
    'level':2,
    'water_walk':True,
    'challenge_rating':'1/2',
    #'hitpoints_medial':True,
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
    'attacks':{
        ('close', 'tentacles'): {
            'attack_mod':5,
            'damage_mod':3,
            'weapon': False,
            'weapon_type':['simple', 'close', 'restained'],
            'damage_type':'bludgeoning',
            'damage_dice':'1d6',
            'attack_range':5,
            'attack_type':'close',
            'restained_difficult':16,
            'weapon_skills_use': ['simple'],
            'attack_mod_type':'strength',
            'weapon_of_choice':'tentacles'},
        ('close', 'bite'): {
            'attack_mod':5,
            'damage_mod':3,
            'weapon': False,
            'weapon_type':['simple'],
            'damage_type':'piercing',
            'damage_dice':'1d6',
            'attack_range':5,
            'attack_type':'close',
            'weapon_skills_use': ['simple'],
            'attack_mod_type':'strength',
            'weapon_of_choice':'bite'},
        },
    'behavior':'warrior',
    'race':'Primevial-medium',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Shield':1,
        'Javelin':6,
        },
    }

metadict_animals['Дактиль-хвататель (CR 1/2)'] = {
    'level':2,
    'grapple':True,
    'water_walk':True,
    'behavior':'elite_warrior',
    'challenge_rating':'1/2',
    #'hitpoints_medial':True,
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
    'attacks':{
        ('close', 'tentacles'): {
            'attack_mod':5,
            'damage_mod':3,
            'weapon': False,
            'weapon_type':['simple', 'close', 'restained'],
            'damage_type':'bludgeoning',
            'damage_dice':'1d6',
            'attack_range':5,
            'attack_type':'close',
            'restained_difficult':16,
            'weapon_skills_use': ['simple'],
            'attack_mod_type':'strength',
            'weapon_of_choice':'tentacles'},
        ('close', 'bite'): {
            'attack_mod':5,
            'damage_mod':3,
            'weapon': False,
            'weapon_type':['simple'],
            'damage_type':'piercing',
            'damage_dice':'1d6',
            'attack_range':5,
            'attack_type':'close',
            'weapon_skills_use': ['simple'],
            'attack_mod_type':'strength',
            'weapon_of_choice':'bite'},
        ('reach', 'tentacles'): {
            'attack_mod':5,
            'damage_mod':3,
            'weapon': False,
            'weapon_type':['simple', 'reach', 'restained'],
            'damage_type':'bludgeoning',
            'damage_dice':'1d6',
            'attack_range':10,
            'attack_type':'close',
            'restained_difficult':16,
            'weapon_skills_use': ['simple'],
            'attack_mod_type':'strength',
            'weapon_of_choice':'tentacles'},
        },
    'race':'Primevial-medium',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Shield':1,
        'Javelin':6,
        },
    }

metadict_animals['Дактиль-ломатель (CR 1)'] = {
    'level':4,
    'water_walk':True,
    'behavior':'elite_warrior',
    'challenge_rating':'1/2',
    #'hitpoints_medial':True,
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
        ('close', 'bite'): {
            'attack_mod':5,
            'damage_mod':3,
            'weapon': False,
            'weapon_type':['simple'],
            'damage_type':'piercing',
            'damage_dice':'2d6',
            'attack_range':5,
            'attack_type':'close',
            'weapon_skills_use': ['simple'],
            'attack_mod_type':'strength',
            'weapon_of_choice':'bite'},
        ('reach', 'tentacles'): {
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
    'race':'Primevial-large',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Shield':1,
        'Javelin':6,
        },
    }

metadict_animals['Дактиль-сжиратель (CR 2)'] = {
    'level':5,
    'water_walk':True,
    'killer_AI':True,
    'carefull_AI':True,
    #'fearless_AI':True,
    'challenge_rating':'2',
    #'hitpoints_medial':True,
    'char_class':'Warrior-officer',
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
        'charisma':18,
        },
    'hit_dice':'1d8',
    'attacks':{
        ('close', 'bite'): {
            'attack_mod':6,
            'damage_mod':4,
            'weapon': False,
            'weapon_type':['simple'],
            'damage_type':'slashing',
            'damage_dice':'2d6',
            'attack_range':5,
            'attack_type':'close',
            'weapon_skills_use': ['simple'],
            'attack_mod_type':'strength',
            'weapon_of_choice':'bite'},
        ('close', 'tentacles'): {
            'attack_mod':6,
            'damage_mod':4,
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
            'attack_mod':6,
            'damage_mod':4,
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
    'behavior':'commander',
    'race':'Primevial-large',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Shield':1,
        'Javelin':6,
        },
    }

#----
# Homebrew: Громовые птицы

metadict_animals['Громовая птица (Thunderbird) (CR 1)'] = {
    # TODO: иммунитет к урону молнией
    # TODO: сделай air_walk
    'level':4,
    'air_walk':True,
    'water_walk':True,
    'behavior':'archer',
    'challenge_rating':'1',
    'char_class':'Warrior',
    #'class_features':{
    #    'Feat_Sharpshooter':True,
    #    },
    'abilityes':{
        'strength':10,
        'dexterity':16,
        'constitution':12,
        'intelligence':6,
        'wisdom':12,
        'charisma':7,
        },
    'hit_dice':'1d8',
    'attacks':{
        ('close', 'beak'): {
            'attack_mod':5,
            'damage_mod':3,
            'weapon': False,
            'weapon_type':['simple', 'close'],
            'damage_type':'piercing',
            'damage_dice':'1d6',
            'attack_range':5,
            'attack_type':'close',
            'weapon_skills_use': ['simple'],
            'attack_mod_type':'dexterity',
            'weapon_of_choice':'beak'},
        ('ranged', 'thunder-feather'): {
            'attack_mod':5,
            'damage_mod':3,
            'weapon': False,
            'direct_hit':False,
            'weapon_type':['simple','ranged'],
            'spell_dict':{
                    'zone':True,
                    #'zone_shape':'2x2',
                    #'zone_shape':'square',
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_all':True,
                    'savethrow_ability':'constitution',
                    'attacks_number':1,
                    'attack_range':5,
                    'radius':5,
                    'damage_type':'thunder',
                    'damage_dice':'1d6',
                    'components':[],
                    'casting_time':'bonus_action',
                    'damage_mod':0,
                    'spell_level':1,
                    'spell_save_DC':13,
                    'spell_choice':('subspell','Thunderclap'),
                    },
            'damage_type':'piercing',
            'damage_dice':'1d6',
            'ammo':10,
            'ammo_type':'feather',
            'attack_type':'ranged',
            'attack_range':60,
            'attack_range_max':300,
            'weapon_skills_use': ['simple'],
            'attack_mod_type':'dexterity',
            'weapon_of_choice':'thunder-feather'},
        ('ranged', 'arrow-feather'): {
            'attack_mod':5,
            'damage_mod':3,
            'weapon': False,
            'direct_hit':False,
            'weapon_type':['simple','ranged'],
            'damage_type':'piercing',
            'damage_dice':'1d6',
            'ammo':100,
            'ammo_type':'feather',
            'attack_type':'ranged',
            'attack_range':60,
            'attack_range_max':300,
            'weapon_skills_use': ['simple'],
            'attack_mod_type':'dexterity',
            'weapon_of_choice':'thunder-feather'},
        },
    'race':'Bird-medium',
    'weapon_skill':[],
    'armor_skill':[],
    'equipment_supply':{},
    'equipment_backpack':{},
    'equipment_weapon':{},
    }

metadict_animals['Громовая птица-вожак (Thunderbird) (CR 1)'] = {
    # TODO: иммунитет к урону молнией
    # TODO: сделай air_walk
    'level':5,
    #'volley_AI':True,
    #'killer_AI':True,
    'air_walk':True,
    'water_walk':True,
    'behavior':'commander',
    'challenge_rating':'1',
    'char_class':'Warrior',
    #'class_features':{
    #    'Feat_Sharpshooter':True,
    #    },
    'abilityes':{
        'strength':10,
        'dexterity':16,
        'constitution':12,
        'intelligence':6,
        'wisdom':12,
        'charisma':7,
        },
    'hit_dice':'1d8',
    'attacks':{
        ('close', 'beak'): {
            'attack_mod':5,
            'damage_mod':3,
            'weapon': False,
            'weapon_type':['simple', 'close'],
            'damage_type':'piercing',
            'damage_dice':'1d6',
            'attack_range':5,
            'attack_type':'close',
            'weapon_skills_use': ['simple'],
            'attack_mod_type':'dexterity',
            'weapon_of_choice':'beak'},
        ('ranged', 'thunder-feather'): {
            'attack_mod':5,
            'damage_mod':3,
            'weapon': False,
            'direct_hit':False,
            'weapon_type':['simple','ranged'],
            'spell_dict':{
                    'zone':True,
                    #'zone_shape':'2x2',
                    #'zone_shape':'square',
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_all':True,
                    'savethrow_ability':'constitution',
                    'attacks_number':1,
                    'attack_range':5,
                    'radius':5,
                    'damage_type':'thunder',
                    'damage_dice':'1d6',
                    'components':[],
                    'casting_time':'bonus_action',
                    'damage_mod':0,
                    'spell_level':1,
                    'spell_save_DC':13,
                    'spell_choice':('subspell','Thunderclap'),
                    },
            'damage_type':'piercing',
            'damage_dice':'1d6',
            'ammo':10,
            'ammo_type':'feather',
            'attack_type':'ranged',
            'attack_range':60,
            'attack_range_max':300,
            'weapon_skills_use': ['simple'],
            'attack_mod_type':'dexterity',
            'weapon_of_choice':'thunder-feather'},
        ('ranged', 'arrow-feather'): {
            'attack_mod':5,
            'damage_mod':3,
            'weapon': False,
            'direct_hit':False,
            'weapon_type':['simple','ranged'],
            'damage_type':'piercing',
            'damage_dice':'1d6',
            'ammo':100,
            'ammo_type':'feather',
            'attack_type':'ranged',
            'attack_range':60,
            'attack_range_max':300,
            'weapon_skills_use': ['simple'],
            'attack_mod_type':'dexterity',
            'weapon_of_choice':'thunder-feather'},
        },
    'race':'Bird-medium',
    'weapon_skill':[],
    'armor_skill':[],
    'equipment_supply':{},
    'equipment_backpack':{},
    'equipment_weapon':{},
    }

#----
# Homebrew: Оживлённые вещи.

metadict_animals['Animated swords (CR 1)'] = {
    # Заклинание 5 круга "Оживление вещей" (Animated_Objects)
    'level':9,
    'killer_AI':True,
    'seeker_AI':True,
    'fearless_AI':True,
    'no_grappler_AI':True,
    'air_walk':True,
    'water_walk':True,
    'mechanism':True,
    'mechanism_construct':True,
    'challenge_rating':'1',
    'behavior':'elite_warrior',
    'char_class':'Warrior',
    'hitpoints_base':20,
    'abilityes':{
        'strength':4,
        'dexterity':18,
        'constitution':10,
        'intelligence':3,
        'wisdom':3,
        'charisma':1,
        },
    'hit_dice':'1d4',
    'race':'Object-steel-tiny',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Scimitar':1,
        },
    }

metadict_animals['Mordenkainen Sword (CR 10)'] = {
    # Заклинание 7 круга "Меч Морденкайнена" (Mordenkainen_Sword)
    'level':13,
    'hunter_AI':True,
    #'predator_AI':True,
    'fearless_AI':True,
    'no_grappler_AI':True,
    'air_walk':True,
    'water_walk':True,
    'mechanism':True,
    'mechanism_construct':True,
    'challenge_rating':'10',
    'behavior':'commander',
    'char_class':'Warrior',
    'class_features':{
        #'Extra_Attack':True,
        'Empyrean_Immunity':True,
        },
    'hitpoints_base':1200,
    'abilityes':{
        'strength':10,
        'dexterity':20,
        'constitution':10,
        'intelligence':3,
        'wisdom':3,
        'charisma':1,
        },
    'hit_dice':'1d4',
    'attacks':{
        ('close', 'Mordenkainen Sword'): {
            'attack_mod':12,
            'damage_mod':0,
            'weapon': True,
            'weapon_type':['martial', 'close', 'magic'],
            'damage_type':'force',
            'damage_dice':'7d10',
            'attack_range':5,
            'attack_type':'close',
            'weapon_skills_use': ['martial'],
            'attack_mod_type':'dexterity',
            'weapon_of_choice':'Mordenkainen Sword'},
        },
    'race':'Object-force-tiny',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{},
    }
