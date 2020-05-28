#!/usr/bin/env python
# -*- coding: utf-8 -*-

#----
# Расовые особенности.

dict_races = {
        # Базовая скорость, зависит от расы:
        # https://www.dandwiki.com/wiki/5e_SRD:Races
        # https://www.dandwiki.com/wiki/5e_SRD:Movement#Speed
        'Human-common':{
            # Средние параметры gen_abilityes -- 10.5 на каждую характеристику.
            # Это близко к Commoner из "Monster Manial", расовые бонусы не нужны.
            'hero':False,
            'size':'medium',
            'base_speed':30,
            'height_base_inches':4 * 12 + 8,
            'height_mod_dice':'2d10',
            'weight_base_lb':110,
            'weight_mod_dice':'2d4',
            #'strength':+1,
            #'dexterity':+1,
            #'constitution':+1,
            #'intelligence':+1,
            #'wisdom':+1,
            #'charisma':+1,
            },
        'Human-undead':{
            'hero':False,
            'size':'medium',
            'base_speed':30,
            'height_base_inches':4 * 12 + 8,
            'height_mod_dice':'2d10',
            'weight_base_lb':110,
            'weight_mod_dice':'2d4',
            },
        'Human-hero':{
            # У героев средние параметры -- 12, с модификатором получается 13.
            # Сумма по медиане -- 81 (такие параметры у 1/100 из обычных людей)
            'hero':True,
            'size':'medium',
            'base_speed':30,
            'height_base_inches':4 * 12 + 8,
            'height_mod_dice':'2d10',
            'weight_base_lb':110,
            'weight_mod_dice':'2d4',
            'strength':+1,
            'dexterity':+1,
            'constitution':+1,
            'intelligence':+1,
            'wisdom':+1,
            'charisma':+1,
            },
        'Cat-hero':{
            # Коттаямские котики.
            'hero':True,
            'size':'small',
            'base_speed':40,
            'height_base_inches':12,
            'height_mod_dice':'1d2',
            'weight_base_lb':4,
            'weight_mod_dice':'1d2',
            'dexterity':+2,
            'intelligence':+1,
            'wisdom':+1,
            },
        'Primevial':{
            # Эмпиреи, Empyrean
            'hero':True,
            'size':'large',
            'base_speed':50,
            'height_base_inches':6 * 12 + 8,
            'height_mod_dice':'2d10',
            'weight_base_lb':210,
            'weight_mod_dice':'2d4',
            },
        'Horse':{
            # Верховые кони (высота в холке).
            'hero':False,
            'size':'large',
            'base_speed':60,
            'height_base_inches':56,
            'height_mod_dice':'2d4',
            'weight_base_lb':1000,
            'weight_mod_dice':'2d20',
            },
        'Bear':{
            # TODO: рост/вес подправь.
            'hero':False,
            'size':'large',
            'base_speed':40,
            'armor_class_natural':11,
            'height_base_inches':56,
            'height_mod_dice':'2d4',
            'weight_base_lb':1000,
            'weight_mod_dice':'2d20',
            },
        'Giant_octopus':{
            # TODO: а какие осьминожки по росту/весу?
            'hero':False,
            'size':'large',
            'base_speed':60,
            'armor_class_natural':11,
            'height_base_inches':56,
            'height_mod_dice':'2d4',
            'weight_base_lb':1000,
            'weight_mod_dice':'2d20',
            },
        }
