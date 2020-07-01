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
        'Humanoid-big':{
            'hero':False,
            'size':'large',
            'base_speed':40,
            'height_base_inches':6 * 12 + 8,
            'height_mod_dice':'2d10',
            'weight_base_lb':210,
            'weight_mod_dice':'2d4',
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
        'Human-dummy':{
            # Чучело, без скорости передвижения.
            'armor_class_natural':15,
            'hero':False,
            'size':'medium',
            'base_speed':0,
            'height_base_inches':4 * 12 + 8,
            'height_mod_dice':'2d10',
            'weight_base_lb':110,
            'weight_mod_dice':'2d4',
            },
        'Satyr':{
            # Умеют создавать пьянящую добрянику.
            # Сложно очаровать, невозможно усыпить магией.
            # Преимущество на спасброски против ядов/алкоголя.
            'hero':False,
            'size':'medium',
            'base_speed':40,
            'height_base_inches':4 * 12 + 8,
            'height_mod_dice':'2d10',
            'weight_base_lb':110,
            'weight_mod_dice':'2d4',
            'constitution':+2,
            'charisma':+1,
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
        'Human-hero-big':{
            # Большие герои
            'hero':True,
            'size':'large',
            'base_speed':40,
            'height_base_inches':6 * 12 + 8,
            'height_mod_dice':'2d10',
            'weight_base_lb':210,
            'weight_mod_dice':'2d4',
            'strength':+1,
            'dexterity':+1,
            'constitution':+1,
            'intelligence':+1,
            'wisdom':+1,
            'charisma':+1,
            },
        'Dog':{
            # Мастиффы.
            'hero':False,
            'size':'small',
            'base_speed':40,
            'height_base_inches':12,
            'height_mod_dice':'1d2',
            'weight_base_lb':4,
            'weight_mod_dice':'1d2',
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
            'base_speed':40,
            'armor_class_natural':13,
            'height_base_inches':6 * 12 + 8,
            'height_mod_dice':'2d10',
            'weight_base_lb':210,
            'weight_mod_dice':'2d4',
            },
        'Primevial-medium':{
            'hero':False,
            'size':'medium',
            'base_speed':30,
            'armor_class_natural':12,
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
        'Horseclaw':{
            # Чокобо, когтеклюв:
            # https://www.dandwiki.com/wiki/Chocobo_(3.5e_Creature)
            # У них прочные перья, природная броня -- 11.
            'hero':False,
            'size':'large',
            'base_speed':60,
            'armor_class_natural':11,
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
        'Catapult':{
            # Какая там базовая защита у деревянных предметов?
            'hero':False,
            'size':'large',
            'base_speed':0,
            'armor_class_natural':15,
            'height_base_inches':56,
            'height_mod_dice':'2d4',
            'weight_base_lb':4000,
            'weight_mod_dice':'2d20',
            },
        }
