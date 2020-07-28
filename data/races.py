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
            'unholy':True,
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
        'Primevial-large':{
            # Эмпиреи, Empyrean
            'hero':True,
            'unholy':True,
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
            'unholy':True,
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
        'Bird-medium':{
            # TODO: скорость 150-300 футов.
            # Но пока disengage недопилен, пусть будет так.
            'hero':False,
            'size':'medium',
            'base_speed':60,
            'height_base_inches':4 * 12 + 8,
            'height_mod_dice':'2d10',
            'weight_base_lb':110,
            'weight_mod_dice':'2d4',
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
        'Elemental-air':{
            'hero':False,
            'size':'large',
            'base_speed':90,
            'height_base_inches':56,
            'height_mod_dice':'2d4',
            'weight_base_lb':2000,
            'weight_mod_dice':'2d20',
            },
        'Elemental-earth':{
            'hero':False,
            'size':'large',
            'base_speed':30,
            'armor_class_natural':18,
            'height_base_inches':56,
            'height_mod_dice':'2d4',
            'weight_base_lb':2000,
            'weight_mod_dice':'2d20',
            },
        'Object-wood-big':{
            # У больших деревянных предметов 15 AC
            'hero':False,
            'size':'large',
            'base_speed':0,
            'armor_class_natural':15,
            'height_base_inches':56,
            'height_mod_dice':'2d4',
            'weight_base_lb':4000,
            'weight_mod_dice':'2d20',
            },
        'Object-stone-big':{
            'hero':False,
            'size':'large',
            'base_speed':0,
            'armor_class_natural':17,
            'height_base_inches':56,
            'height_mod_dice':'0d0',
            'weight_base_lb':2000,
            'weight_mod_dice':'0d0',
            },
        'Object-wood-ship-part':{
            # 10x10-футовая часть корпуса.
            # Водоизмещение триеры -- 50 тонны (1/50 часть корпуса = 2000 lb)
            'hero':False,
            'size':'large',
            'base_speed':0,
            'armor_class_natural':15,
            'height_base_inches':56,
            'height_mod_dice':'2d4',
            'weight_base_lb':2000,
            'weight_mod_dice':'2d20',
            },
        'Object-steel-tiny':{
            # Оживление вещей.
            'hero':False,
            'size':'tiny',
            'base_speed':30,
            'armor_class_natural':14,
            'height_base_inches':12,
            'height_mod_dice':'1d2',
            'weight_base_lb':4,
            'weight_mod_dice':'1d2',
            },
        'Object-force-tiny':{
            # Меч Морденкайнена.
            'hero':False,
            'size':'tiny',
            'base_speed':60,
            'armor_class_natural':14,
            'height_base_inches':12,
            'height_mod_dice':'1d2',
            'weight_base_lb':4,
            'weight_mod_dice':'1d2',
            },
        }
