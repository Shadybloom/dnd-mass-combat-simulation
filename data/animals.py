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

metadict_animals['Palisade (wood) (120 hp)'] = {
    # Частокол, палисад
    'level':1,
    'hitpoints_base':120,
    'armor_class_natural':15,
    'ignore_damage':15,
    'mechanism':True,
    'savethrow_autofall':True,
    'inactive_AI':True,
    'challenge_rating':'-',
    'char_class':'Commoner',
    'behavior':'commander',
    'class_features':{
        'resistance':['piercing','bludgeoning'],
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

metadict_animals['Palisade (wood) (600 hp)'] = {
    # Частокол, палисад
    'level':1,
    'hitpoints_base':600,
    'armor_class_natural':15,
    'ignore_damage':15,
    'mechanism':True,
    'savethrow_autofall':True,
    'inactive_AI':True,
    'challenge_rating':'-',
    'char_class':'Commoner',
    'behavior':'commander',
    'class_features':{
        'resistance':['piercing','bludgeoning'],
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

metadict_animals['Wall (stone) (1200 hp)'] = {
    # 10 футов стены. Каждый фут 120 hp
    'level':5,
    'mechanism':True,
    'savethrow_autofall':True,
    'inactive_AI':True,
    'hitpoints_base':1200,
    'armor_class_natural':17,
    'ignore_damage':20,
    'challenge_rating':'-',
    'char_class':'Commoner',
    'behavior':'commander',
    'class_features':{
        'resistance':['slashing','piercing','bludgeoning'],
        'vultenability':['thunder'],
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

metadict_animals['Wall (stone) (1200 hp + Arcane_Lock)'] = {
    # 10 футов стены. Каждый фут 120 hp.
    # Arcane_Lock даёт 17 AC --> 20 AC
    'level':5,
    'mechanism':True,
    'savethrow_autofall':True,
    'inactive_AI':True,
    'hitpoints_base':1200,
    'armor_class_natural':20,
    'ignore_damage':20,
    'challenge_rating':'-',
    'char_class':'Commoner',
    'behavior':'commander',
    'class_features':{
        'resistance':['slashing','piercing','bludgeoning'],
        'vultenability':['thunder'],
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
    # 5 футов камня опоры. Каждый фут 120 hp.
    'level':5,
    'hitpoints_base':600,
    'armor_class_natural':17,
    'ignore_damage':20,
    'mechanism':True,
    'savethrow_autofall':True,
    'inactive_AI':True,
    'challenge_rating':'-',
    'char_class':'Commoner',
    'behavior':'commander',
    'class_features':{
        'resistance':['slashing','piercing','bludgeoning'],
        'vultenability':['thunder'],
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
    # 1 фут камня.
    'level':5,
    'hitpoints_base':120,
    'armor_class_natural':17,
    'ignore_damage':20,
    'mechanism':True,
    'savethrow_autofall':True,
    'inactive_AI':True,
    'challenge_rating':'-',
    'char_class':'Commoner',
    'behavior':'warrior',
    'class_features':{
        'resistance':['slashing','piercing','bludgeoning'],
        'vultenability':['thunder'],
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
    # Палуба триеры. Дюймовые доски.
        # Прочность по толщине:
        # (25/330)*120 = 9 hp
    'level':1,
    'hitpoints_base':9,
    'armor_class_natural':15,
    'ignore_damage':10,
    'inactive_AI':True,
    'mechanism':True,
    'savethrow_autofall':True,
    'challenge_rating':'-',
    'char_class':'Commoner',
    'behavior':'warrior',
    'class_features':{
        'resistance':['piercing','bludgeoning'],
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
    # Борт триеры. 4 слоя 1.5-дюймовых планок.
        # Прочность по толщине:
        # (150/330)*120 = 54 hp
    'level':2,
    'hitpoints_base':54,
    'armor_class_natural':15,
    'ignore_damage':15,
    'inactive_AI':True,
    'mechanism':True,
    'savethrow_autofall':True,
    'challenge_rating':'-',
    'char_class':'Commoner',
    'behavior':'elite_warrior',
    'class_features':{
        'resistance':['piercing','bludgeoning'],
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
    'level':3,
    'hitpoints_base':54,
    'armor_class_natural':15,
    'ignore_damage':15,
    'inactive_AI':True,
    'mechanism':True,
    'savethrow_autofall':True,
    'challenge_rating':'-',
    'char_class':'Commoner',
    'behavior':'commander',
    'class_features':{
        'resistance':['piercing','bludgeoning'],
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
    # Палуба пентеры. 2-дюймовые доски.
        # Прочность по толщине:
        # (50/330)*120 = 18 hp
    'level':1,
    'hitpoints_base':18,
    'armor_class_natural':15,
    'ignore_damage':10,
    'inactive_AI':True,
    'mechanism':True,
    'savethrow_autofall':True,
    'challenge_rating':'-',
    'char_class':'Commoner',
    'behavior':'warrior',
    'class_features':{
        'resistance':['piercing','bludgeoning'],
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
    # Борт пентеры. 6 слоёв 1.5-дюймовых планок
        # Прочность по толщине:
        # (225/330)*120 = 81 hp
    'level':2,
    'hitpoints_base':81,
    'armor_class_natural':15,
    'ignore_damage':15,
    'inactive_AI':True,
    'mechanism':True,
    'savethrow_autofall':True,
    'challenge_rating':'-',
    'char_class':'Commoner',
    'behavior':'elite_warrior',
    'class_features':{
        'resistance':['piercing','bludgeoning'],
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
    # Нос и корма пернтеры.
    'level':3,
    'hitpoints_base':81,
    'armor_class_natural':15,
    'ignore_damage':15,
    'inactive_AI':True,
    'mechanism':True,
    'savethrow_autofall':True,
    'challenge_rating':'-',
    'char_class':'Commoner',
    'behavior':'commander',
    'class_features':{
        'resistance':['piercing','bludgeoning'],
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
    # Палуба торгового судна. Дюймовые доски.
        # Прочность по толщине:
        # (25/330)*120 = 9 hp
    'level':1,
    'hitpoints_base':9,
    'armor_class_natural':15,
    'ignore_damage':10,
    'inactive_AI':True,
    'mechanism':True,
    'savethrow_autofall':True,
    'challenge_rating':'-',
    'char_class':'Commoner',
    'behavior':'warrior',
    'class_features':{
        'resistance':['piercing','bludgeoning'],
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
    # Борт торгового судна. 3 слоя 1.5-дюймовых планок.
        # Прочность по толщине:
        # (112/330)*120 = 41 hp
    'level':2,
    'hitpoints_base':41,
    'armor_class_natural':15,
    'ignore_damage':15,
    'inactive_AI':True,
    'mechanism':True,
    'savethrow_autofall':True,
    'challenge_rating':'-',
    'char_class':'Commoner',
    'behavior':'elite_warrior',
    'class_features':{
        'resistance':['piercing','bludgeoning'],
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
    'level':3,
    'hitpoints_base':41,
    'armor_class_natural':15,
    'ignore_damage':15,
    'inactive_AI':True,
    'mechanism':True,
    'savethrow_autofall':True,
    'challenge_rating':'-',
    'char_class':'Commoner',
    'behavior':'commander',
    'class_features':{
        'resistance':['piercing','bludgeoning'],
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
        'immunity':['slashing','piercing','bludgeoning'],
        'Extra_Attack':True,
        'Unarmored_Defense':True,
        'Legendary_Resistance':True,
        'Spell_Resistance':True,
        'Trembling_Strike':True,
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
        'resistance':['slashing','piercing','bludgeoning','necrotic_energy'],
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

metadict_animals['Ghast (CR 2)'] = {
    # Вурдалак
    'level':8,
    #'fearless_AI':True,
    'Brave_AI':True,
    'killer_AI':True,
    'predator_AI':True,
    'challenge_rating':'2',
    'char_class':'Warrior',
    'behavior':'commander',
    'hitpoints_medial':True,
    'class_features':{
        # TODO: вонь отравляет всех в пределах 5 футов. СЛ 10.
        'Ghast_Stench':True,
        'Turn_Defiance':True,
        'Darkvision':60,
        },
    'abilityes':{
        'strength':16,
        'dexterity':17,
        'constitution':10,
        'intelligence':11,
        'wisdom':10,
        'charisma':8,
        },
    'hit_dice':'1d8',
    'attacks':{
        ('close', 'bite'): {
            'attack_mod':3,
            'damage_mod':3,
            'weapon': False,
            'weapon_type':['simple'],
            'damage_type':'piercing',
            'damage_dice':'2d8',
            'attack_range':5,
            'attack_type':'close',
            'weapon_skills_use': ['simple'],
            'attack_mod_type':'dexterity',
            'weapon_of_choice':'claws'},
        ('close', 'claws'): {
            'attack_mod':5,
            'damage_mod':3,
            'weapon': False,
            'weapon_type':['simple'],
            'damage_type':'slashing',
            'spell_dict':{
                    'safe':True,
                    'effect':'paralyze',
                    'effect_timer':10,
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_ability':'constitution',
                    'spell_save_DC':10,
                    'spell_choice':('claws','paralyze'),
                    },
            'damage_dice':'2d6',
            'attack_range':5,
            'attack_type':'close',
            'weapon_skills_use': ['simple'],
            'attack_mod_type':'dexterity',
            'weapon_of_choice':'claws'},
        },
    'race':'Human-undead',
    'weapon_skill':['simple'],
    'armor_skill':['light','medium'],
    'equipment_weapon':{
        },
    'equipment_backpack':{},
    'equipment_supply':{},
    }

metadict_animals['Ghoul (CR 1)'] = {
    # Упырь
    'level':5,
    'killer_AI':True,
    'predator_AI':True,
    'challenge_rating':'1',
    'char_class':'Warrior',
    'behavior':'warrior',
    'hitpoints_medial':True,
    'class_features':{
        'Darkvision':60,
        },
    'abilityes':{
        'strength':13,
        'dexterity':15,
        'constitution':10,
        'intelligence':7,
        'wisdom':10,
        'charisma':6,
        },
    'hit_dice':'1d8',
    'attacks':{
        ('close', 'bite'): {
            'attack_mod':2,
            'damage_mod':2,
            'weapon': False,
            'weapon_type':['simple'],
            'damage_type':'piercing',
            'damage_dice':'2d6',
            'attack_range':5,
            'attack_type':'close',
            'weapon_skills_use': ['simple'],
            'attack_mod_type':'dexterity',
            'weapon_of_choice':'claws'},
        ('close', 'claws'): {
            'attack_mod':4,
            'damage_mod':2,
            'weapon': False,
            'weapon_type':['simple'],
            'damage_type':'slashing',
            'spell_dict':{
                    'safe':True,
                    'effect':'paralyze',
                    'effect_timer':10,
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_ability':'constitution',
                    'spell_save_DC':10,
                    'spell_choice':('claws','paralyze'),
                    },
            'damage_dice':'2d4',
            'attack_range':5,
            'attack_type':'close',
            'weapon_skills_use': ['simple'],
            'attack_mod_type':'dexterity',
            'weapon_of_choice':'claws'},
        },
    'race':'Human-undead',
    'weapon_skill':['simple'],
    'armor_skill':['light','medium'],
    'equipment_weapon':{
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
        'resistance':['slashing','piercing','bludgeoning','thunder','lightning'],
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
                    'safe':True,
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
        'resistance':['slashing','piercing','bludgeoning'],
        'vultenability':['thunder'],
        'Extra_Attack':True,
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
# Гиганты. Великаны из Monsters_Manual:

metadict_animals['Hill Giant (CR 5)'] = {
    # Холмовой великан
    'level':10,
    'seeker_AI':True,
    'fearless_AI':True,
    'no_grappler_AI':True,
    'armor_class_natural':14,
    'challenge_rating':'5',
    'hitpoints_medial':True,
    'char_class':'Warrior',
    'behavior':'commander',
    'class_features':{
        'Extra_Attack':True,
        },
    'abilityes':{
        'strength':21,
        'dexterity':8,
        'constitution':19,
        'intelligence':5,
        'wisdom':9,
        'charisma':6,
        },
    'hit_dice':'1d12',
    # TODO: делай атаки через свойства оружия.
    # - у него 10-футовая досягаемость атак. 'reach' атака дубиной.
    # - лучше бы сделать метательный булыжник для великанов.
    'attacks':{
        ('reach', 'Greatclub'): {
            'attack_mod':8,
            'damage_mod':5,
            'weapon': False,
            'weapon_type':['simple','reach','siege'],
            'damage_type':'bludgeoning',
            'damage_dice':'3d8',
            'attack_range':10,
            'attack_type':'reach',
            'weapon_skills_use': ['simple'],
            'attack_mod_type':'strength',
            'weapon_of_choice':'Greatclub'
            },
        ('throw', 'Boulder (50 lb)'): {
            'attack_mod':8,
            'damage_mod':5,
            'weapon': False,
            'weapon_type':['simple','throw','siege'],
            'damage_type':'bludgeoning',
            'damage_dice':'3d10',
            'attack_range':60,
            'attack_range_max':240,
            'attack_type':'throw',
            'weapon_skills_use': ['simple'],
            'attack_mod_type':'strength',
            'ammo':6,
            'ammo_type':'Boulder (50 lb)',
            'weapon_of_choice':'Boulder (50 lb)'
            },
        },
    'race':'Humanoid-huge',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':{},
    'equipment_backpack':{},
    'equipment_weapon':{
        'Greatclub':1,
        'Boulder (50 lb)':6,
        },
    }

metadict_animals['Stone Giant (CR 7)'] = {
    # Каменный великан
    'level':11,
    'seeker_AI':True,
    'fearless_AI':True,
    'no_grappler_AI':True,
    'armor_class_natural':15,
    'challenge_rating':'7',
    'hitpoints_medial':True,
    'char_class':'Warrior',
    'behavior':'commander',
    'class_features':{
        'Extra_Attack':True,
        'Stone_Camouflage':True,
        'Darkvision':60,
        },
    'abilityes':{
        'strength':23,
        'dexterity':15,
        'constitution':20,
        'intelligence':10,
        'wisdom':12,
        'charisma':9,
        },
    'hit_dice':'1d12',
    'attacks':{
        ('reach', 'Greatclub'): {
            'attack_mod':9,
            'damage_mod':6,
            'weapon': False,
            'weapon_type':['simple','reach','siege'],
            'damage_type':'bludgeoning',
            'damage_dice':'3d8',
            'attack_range':10,
            'attack_type':'reach',
            'weapon_skills_use': ['simple'],
            'attack_mod_type':'strength',
            'weapon_of_choice':'Greatclub'
            },
        ('throw', 'Boulder (50 lb)'): {
            # TODO: сбивает с ног, СЛ 17
            # Сделано через 'prone', но там состязание вместо СЛ.
            'attack_mod':9,
            'damage_mod':6,
            'weapon': False,
            'weapon_type':['simple','throw','siege','prone'],
            'damage_type':'bludgeoning',
            'damage_dice':'3d10',
            'attack_range':60,
            'attack_range_max':240,
            'attack_type':'throw',
            'weapon_skills_use': ['simple'],
            'attack_mod_type':'strength',
            'ammo':6,
            'ammo_type':'Boulder (50 lb)',
            'weapon_of_choice':'Boulder (50 lb)'
            },
        },
    'race':'Humanoid-huge',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':{},
    'equipment_backpack':{},
    'equipment_weapon':{
        'Greatclub':1,
        'Boulder (50 lb)':6,
        },
    }

metadict_animals['Frost Giant (CR 8)'] = {
    # Ледяной великан, морозный гигант.
    'level':12,
    'seeker_AI':True,
    'fearless_AI':True,
    'no_grappler_AI':True,
    'armor_class_natural':16,
    'challenge_rating':'8',
    'hitpoints_medial':True,
    'char_class':'Warrior',
    'behavior':'commander',
    'class_features':{
        'immunity':['cold'],
        'Extra_Attack':True,
        },
    'abilityes':{
        'strength':23,
        'dexterity':9,
        'constitution':21,
        'intelligence':9,
        'wisdom':10,
        'charisma':12,
        },
    'hit_dice':'1d12',
    'attacks':{
        ('reach', 'Greataxe'): {
            'attack_mod':9,
            'damage_mod':6,
            'weapon': False,
            'weapon_type':['martial','reach','siege'],
            'damage_type':'slashing',
            'damage_dice':'3d12',
            'attack_range':10,
            'attack_type':'reach',
            'weapon_skills_use': ['martial'],
            'attack_mod_type':'strength',
            'weapon_of_choice':'Greataxe'
            },
        ('throw', 'Boulder (50 lb)'): {
            'attack_mod':9,
            'damage_mod':6,
            'weapon': False,
            'weapon_type':['simple','throw','siege'],
            'damage_type':'bludgeoning',
            'damage_dice':'4d10',
            'attack_range':60,
            'attack_range_max':240,
            'attack_type':'throw',
            'weapon_skills_use': ['simple'],
            'attack_mod_type':'strength',
            'ammo':6,
            'ammo_type':'Boulder (50 lb)',
            'weapon_of_choice':'Boulder (50 lb)'
            },
        },
    'race':'Humanoid-huge',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':{},
    'equipment_backpack':{},
    'equipment_weapon':{
        'Greataxe':1,
        'Boulder (50 lb)':6,
        },
    }

metadict_animals['Fire Giant (CR 9)'] = {
    # Огненный великан.
    'level':13,
    'seeker_AI':True,
    'fearless_AI':True,
    'no_grappler_AI':True,
    #'armor_class_natural':16,
    'challenge_rating':'9',
    'hitpoints_medial':True,
    'char_class':'Warrior',
    'behavior':'commander',
    'class_features':{
        'immunity':['fire'],
        'Extra_Attack':True,
        },
    'abilityes':{
        'strength':25,
        'dexterity':9,
        'constitution':23,
        'intelligence':10,
        'wisdom':14,
        'charisma':13,
        },
    'hit_dice':'1d12',
    'attacks':{
        ('reach', 'Greatsword'): {
            'attack_mod':11,
            'damage_mod':7,
            'weapon': False,
            'weapon_type':['martial','reach','siege'],
            'damage_type':'slashing',
            'damage_dice':'6d6',
            'attack_range':10,
            'attack_type':'reach',
            'weapon_skills_use': ['martial'],
            'attack_mod_type':'strength',
            'weapon_of_choice':'Greatsword'
            },
        ('throw', 'Boulder (50 lb)'): {
            'attack_mod':11,
            'damage_mod':7,
            'weapon': False,
            'weapon_type':['simple','throw','siege'],
            'damage_type':'bludgeoning',
            'damage_dice':'4d10',
            'attack_range':60,
            'attack_range_max':240,
            'attack_type':'throw',
            'weapon_skills_use': ['simple'],
            'attack_mod_type':'strength',
            'ammo':6,
            'ammo_type':'Boulder (50 lb)',
            'weapon_of_choice':'Boulder (50 lb)'
            },
        },
    'race':'Humanoid-huge',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':{},
    'equipment_backpack':{},
    'equipment_weapon':{
        'Greatsword':1,
        'Plate Armor':1,
        'Boulder (50 lb)':6,
        },
    }

metadict_animals['Storm Giant (CR 13)'] = {
    # Штормовой великан.
    'level':20,
    'archer_AI':True,
    'fearless_AI':True,
    'no_grappler_AI':True,
    #'armor_class_natural':16,
    'challenge_rating':'13',
    'hitpoints_medial':True,
    'char_class':'Warrior',
    'behavior':'commander',
    'class_features':{
        'immunity':['lightning','thunder'],
        'Extra_Attack':True,
        'Recharge':True,
        'Recharge_dice':'1d6',
        'Recharge_numbers':[5,6],
        },
    'abilityes':{
        'strength':29,
        'dexterity':14,
        'constitution':20,
        'intelligence':16,
        'wisdom':18,
        'charisma':18,
        },
    'hit_dice':'1d12',
    'attacks':{
        ('reach', 'Greatsword'): {
            'attack_mod':14,
            'damage_mod':9,
            'weapon': False,
            'weapon_type':['martial','reach','siege'],
            'damage_type':'slashing',
            'damage_dice':'6d6',
            'attack_range':10,
            'attack_type':'reach',
            'weapon_skills_use': ['martial'],
            'attack_mod_type':'strength',
            'weapon_of_choice':'Greatsword'
            },
        ('throw', 'Boulder (50 lb)'): {
            'attack_mod':14,
            'damage_mod':9,
            'weapon': False,
            'weapon_type':['simple','throw','siege'],
            'damage_type':'bludgeoning',
            'damage_dice':'4d12',
            'attack_range':60,
            'attack_range_max':240,
            'attack_type':'throw',
            'weapon_skills_use': ['simple'],
            'attack_mod_type':'strength',
            'ammo':6,
            'ammo_type':'Boulder (50 lb)',
            'weapon_of_choice':'Lightning'
            },
        ('throw', 'Lightning'): {
            'weapon': False,
            'direct_hit':True,
            'weapon_type':['simple','throw'],
            'spell_dict':{
                    'zone':True,
                    'radius':15,
                    'direct_hit':True,
                    'savethrow':True,
                    'savethrow_ability':'dexterity',
                    'attacks_number':1,
                    'attack_range':500,
                    'damage_type':'lightning',
                    'damage_dice':'12d8',
                    'casting_time':'action',
                    'spell_level':3,
                    'spell_save_DC':17,
                    'spell_choice':('storm','Lightning'),
                    },
            'damage_type':'lightning',
            'damage_dice':'0d0',
            'ammo':1,
            'attack_range':500,
            'attack_range_max':500,
            'weapon_skills_use': ['simple'],
            'attack_mod_type':'strength',
            'weapon_of_choice':'Lightning'
            },
        },
    'race':'Humanoid-huge',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':{},
    'equipment_backpack':{},
    'equipment_weapon':{
        'Greatsword':1,
        'Scale Mail':1,
        'Boulder (50 lb)':6,
        },
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
# NPC, неписи, персонажи мастера из Monsters_Manual:

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

metadict_animals['Mage (CR 6)'] = {
    # Маг
    'level':9,
    'archer_AI':True,
    'fireball_AI':True,
    'challenge_rating':'6',
    'hitpoints_medial':True,
    'char_class':'Wizard',
    'class_features':{
        'Spellcasting':True,
        'Spells':[
            ('cantrip', 'Mage_Hand'),
            ('cantrip', 'Fire_Bolt'),
            ('cantrip', 'Light'),
            ('cantrip', 'Prestidigitation'),
            ('ritual', 'Detect_Magic'),
            ('1_lvl', 'Magic_Missile'),
            ('1_lvl', 'Mage_Armor'),
            ('1_lvl', 'Shield'),
            ('2_lvl', 'Suggestion'),
            ('2_lvl', 'Misty_Step'),
            ('3_lvl', 'Counterspell'),
            ('3_lvl', 'Lightning_Bolt'),
            #('3_lvl', 'Fireball'),
            ('3_lvl', 'Fly'),
            ('4_lvl', 'Greater_Invisibility'),
            ('4_lvl', 'Ice_Storm'),
            ('5_lvl', 'Cone_of_Cold'),
            ],
        },
    'abilityes':{
        'strength':9,
        'dexterity':14,
        'constitution':11,
        'intelligence':17,
        'wisdom':12,
        'charisma':11,
        },
    'hit_dice':'1d8',
    'behavior':'commander',
    'race':'Human-common',
    'weapon_skill':['simple','martial'],
    'armor_skill':['light','medium','heavy','shield'],
    'equipment_supply':soldier_supply,
    'equipment_backpack':soldiers_pack,
    'equipment_weapon':{
        'Dagger':1,
        },
    }

#----
# Эпические чудовища из Monsters_Manual:

metadict_animals['Empyrean (CR 23)'] = {
    # Эмпирей
    # https://dnd-5e.herokuapp.com/monsters/empyrean
    'level':19,
    'air_walk':True,
    'fearless_AI':True,
    'armor_class_natural':17,
    'challenge_rating':'23',
    'hitpoints_medial':True,
    'char_class':'Empyrean',
    'class_features':{
        # TODO:
        # - Сделай Spell_Resistance
        # - Вторая атака легендартным действием.
        # - Преимущество на спасброски против магии.
        # - Его атаки ошеломляют на ход. СЛ 15, телосложение.
        'immunity':['slashing','piercing','bludgeoning'],
        'Extra_Attack':True,
        'Legendary_Resistance':True,
        'Spell_Resistance':True,
        'Trembling_Strike':True,
        'Bolster':True,
        'Spells':[
            # TODO: Сделай Fire_Storm
            ('cantrip', 'Empyrean_Bolt'),
            ('unlimit', 'Pass_Without_Trace'),
            ('unlimit', 'Greater_Restoration'),
            ('unlimit', 'Water_Breathing'),
            ('unlimit', 'Water_Walk'),
            ('1/day', 'Earthquake'),
            ('1/day', 'Commune'),
            ('1/day', 'Fire_Storm'),
            ('1/day', 'Dispel_Evil_and_Good'),
            ('1/day', 'Plane_Shift'),
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
    'race':'Primevial-huge',
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
        'immunity':['slashing','piercing','bludgeoning'],
        #'Extra_Attack':True,
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
