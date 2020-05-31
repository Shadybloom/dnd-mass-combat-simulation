#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------
# Стоимость снаряжения:

# Эфес (55 грамм золота) -- 60 gp в DnD.
# Это год службы профессионального солдата.
# Это стоимость чешуйчатых доспехов, комплекта вооружения, или обученного верхового коня.
# Это 1/30 аттического таланта серебра, или 60 шекелей, 200 драхм, 300 денариев, 3600 фоллисов.
# Это год скромной жизни (рыба, каша, оливковое масло) -- 10 фоллисов/день для семьи в 6 человек.
# Будем считать, что 15-граммовый серебряный шекель (эквивалент грамма золота), это 1 золотая монета в DnD.

# 1 грамм золота
# 15 грамм серебра
# 750 грамм бронзы
# 3.8 килограмма ковкого железа
# 8.4 килограмма хрупкого чугуна
# 60 килограмм пшеницы
# 100 килограмм овса

#-------------------------------------------------------------------------
# Наборы снаряжения:

soldier_supply = {
    'Food supply (1 day)':360,
    }

horse_supply = {
    'Warhorse supply (1 day)':360,
    }

soldiers_pack = {
    # TODO: допилить
        # Вместо спальников шерстяные плащи.
        # Без топорика, ножа и лопаты никуда.
        # Но это часть группового снаряжения.
        # Палатка тоже одна на 10 бойцов, как и котёл.
        # Групповой снарягой предлагаю ослика нагрузить.
    # В пределах 20 фунтов (10 фунтов еда и вода)
        # https://en.wikipedia.org/wiki/File:Roman_legionar_satchel.jpg
        # https://en.wikipedia.org/wiki/Roman_military_personal_equipment#Sarcina
        # https://en.wikipedia.org/wiki/Sarcina
        # https://www.larp.com/legioxx/packs.html
        # https://www.larp.com/legioxx/messgear.html
        # https://www.larp.com/legioxx/tools.html
        # https://www.larp.com/legioxx/tentcamp.html
    'Dagger':1,
    'Handaxe':1,
    #'Clothes, Common':1,
    'Waterskin (full)':1,
    'Rations (1 day)':3,
    'Tinderbox':1,
    'Mess Kit':1,
    'Cloak':1,
    'Backpack':1,
    }

militia_pack = {
    #'Clothes, Common':1,
    'Waterskin (full)':1,
    'Rations (1 day)':3,
    'Tinderbox':1,
    'Cloak':1,
    }

#-------------------------------------------------------------------------
# Все предметы

metadict_items = {}


#-------------------------------------------------------------------------
# Пища (homebrew)

metadict_items['Food supply (1 day)'] = {
    # Пшеничные/ячменные лепёшки, овсяная и бобовая каши, оливковое масло, овощи, рыба и вино.
    'Food supply':True,
    'weight (lb)':2,
    'cost (grams_of_gold)':2 / 60,
    }

metadict_items['Warhorse supply (1 day)'] = {
    # Корма 2% веса в день, 20% концетрированные (в походе) -- 1.8 кг/день, 600 кг/год.
    # Килограмм овса -- 0.5 Folles
    'Food supply':True,
    'weight (lb)':4,
    'cost (grams_of_gold)':2 / 60,
    }

#-------------------------------------------------------------------------
# Оружие
# https://www.dandwiki.com/wiki/5e_SRD:Weapons

#----
# Simple Melee Weapons 

metadict_items['Club'] = {
    'weapon':True,
    'weapon_type':['simple','close','light'],
    'damage_type':'bludgeoning',
    'damage_dice':'1d4',
    'weight (lb)':2,
    'cost (sp)':1,
    'cost (grams_of_gold)':1 / 60,
    }

metadict_items['Dagger'] = {
    # Пугио, скрамасакс, паразониум (по-гречески, "на поясе")
    # https://ru.wikipedia.org/wiki/Пугио
    'weapon':True,
    'weapon_type':['simple','close','finesse','light'],
    'damage_type':'piercing',
    'damage_dice':'1d4',
    'throw_range':20,
    'throw_range_max':60,
    'weight (lb)':1,
    'cost (gp)':2,
    'cost (grams_of_gold)':2,
    }

metadict_items['Handaxe'] = {
    # Скепарнос (скапто -- рыть/рубить)
    # Вес лезвия -- 600 грамм.
    'weapon':True,
    'weapon_type':['simple','close','light'],
    'damage_type':'slashing',
    'damage_dice':'1d6',
    'throw_range':20,
    'throw_range_max':60,
    'weight (lb)':2,
    'cost (gp)':5,
    'cost (grams_of_gold)':2,
    }

metadict_items['Javelin'] = {
    'weapon':True,
    'weapon_type':['simple','close','throw'],
    'damage_type':'piercing',
    'damage_dice':'1d6',
    'throw_range':30,
    'throw_range_max':120,
    'weight (lb)':2,
    'cost (sp)':5,
    'cost (grams_of_gold)':10 / 60,
    }

metadict_items['Mace'] = {
    # Булава (бронзовая, залитая свинцом).
    # Навершие -- 100-350 грамм.
    'weapon':True,
    'weapon_type':['simple','close'],
    'damage_type':'bludgeoning',
    'damage_dice':'1d6',
    'weight (lb)':4,
    'cost (gp)':5,
    'cost (grams_of_gold)':2,
    }

metadict_items['Quarterstaff'] = {
    'weapon':True,
    'weapon_type':['simple','close','versatile'],
    'damage_type':'bludgeoning',
    'damage_dice':'1d6',
    'damage_dice_versatile':'1d8',
    'versatile':True,
    'weight (lb)':4,
    'cost (sp)':2,
    'cost (grams_of_gold)':1 / 60,
    }

metadict_items['Spear'] = {
    # Прочное копьё с бронзовым наконечником.
    'weapon':True,
    'weapon_type':['simple','close','versatile'],
    'damage_type':'piercing',
    'damage_dice':'1d6',
    'damage_dice_versatile':'1d8',
    'throw_range':20,
    'throw_range_max':60,
    'weight (lb)':3,
    'cost (gp)':1,
    'cost (grams_of_gold)':1,
    }

#----
# Simple Ranged Weapons

metadict_items['Crossbow, Light'] = {
    # Гастрафет, аркубаллиста
    'weapon':True,
    'loading':True,
    'ammo_type':'Crossbow Bolt',
    'weapon_type':['simple','ranged','volley','two_handed'],
    'damage_type':'piercing',
    'damage_dice':'1d6',
    'shoot_range':80,
    'shoot_range_max':320,
    'weight (lb)':5,
    'cost (gp)':25,
    'cost (grams_of_gold)':50,
    }

metadict_items['Dart'] = {
    'weapon':True,
    'weapon_type':['simple','finesse','throw'],
    'damage_type':'piercing',
    'damage_dice':'1d6',
    'throw_range':20,
    'throw_range_max':60,
    'weight (lb)':1/4,
    'cost (cp)':5,
    'cost (grams_of_gold)':5 / 60,
    }

metadict_items['Shortbow'] = {
    # Композитный, весьма качественный для своего времени.
    'weapon':True,
    'ammo_type':'Arrow',
    'weapon_type':['simple','ranged','volley','two_handed'],
    'damage_type':'piercing',
    'damage_dice':'1d6',
    'shoot_range':80,
    'shoot_range_max':320,
    'weight (lb)':2,
    'cost (gp)':25,
    'cost (grams_of_gold)':20,
    }

metadict_items['Sling'] = {
    # Дальность бросков из пращи -- 600 футов (но это неприцельно)
    # Лучше всего свинцовые шарики (плотные, меньше трутся о воздух)
    'weapon':True,
    'ammo_type':'Sling Bullet',
    'weapon_type':['simple','ranged','volley'],
    'damage_type':'bludgeoning',
    'damage_dice':'1d4',
    'shoot_range':30,
    'shoot_range_max':120,
    'weight (lb)':1,
    'cost (sp)':1,
    'cost (grams_of_gold)':10 / 60,
    }

#----
# Martial Melee Weapons

metadict_items['Battleaxe'] = {
    # Секира. Вес лезвия -- 450 грамм
    'weapon':True,
    'weapon_type':['martial','close','versatile'],
    'damage_type':'slashing',
    'damage_dice':'1d8',
    'damage_dice_versatile':'1d10',
    'weight (lb)':4,
    'cost (gp)':10,
    'cost (grams_of_gold)':10,
    }

metadict_items['Flait'] = {
    # Гиря -- 100-300 грамм, бронзовая, залита свинцом.
    # На прочной цепочке, поэтому гораздо дороже булавы.
    'weapon':True,
    'weapon_type':['martial','close'],
    'damage_type':'bludgeoning',
    'damage_dice':'1d8',
    'weight (lb)':2,
    'cost (gp)':10,
    'cost (grams_of_gold)':10,
    }

metadict_items['Glaive'] = {
    # Ромфая (длинная рукоять, как у нагинаты)
    # https://ru.wikipedia.org/wiki/Ромфея
    # https://lurkmore.so/images/d/d1/Rhomphaia.jpg
    'weapon':True,
    #'shield_breaker':True,
    'weapon_type':['martial','close','reach','two_handed','heavy'],
    'damage_type':'slashing',
    'damage_dice':'1d10',
    'weight (lb)':6,
    'cost (gp)':20,
    'cost (grams_of_gold)':30,
    }

metadict_items['Greataxe'] = {
    # Бердыш, секира
    'weapon':True,
    #'shield_breaker':True,
    'weapon_type':['martial','close','two_handed','heavy'],
    'damage_type':'slashing',
    'damage_dice':'1d12',
    'weight (lb)':7,
    'cost (gp)':30,
    'cost (grams_of_gold)':30,
    }

metadict_items['Greatsword'] = {
    'weapon':True,
    #'shield_breaker':True,
    'weapon_type':['martial','close','two_handed','heavy'],
    'damage_type':'slashing',
    'damage_dice':'2d6',
    'weight (lb)':6,
    'cost (gp)':50,
    'cost (grams_of_gold)':50,
    }

metadict_items['Halberd'] = {
    'weapon':True,
    #'shield_breaker':True,
    'weapon_type':['martial','close','reach','two_handed','heavy'],
    'damage_type':'slashing',
    'damage_dice':'1d10',
    'weight (lb)':6,
    'cost (gp)':20,
    'cost (grams_of_gold)':20,
    }

metadict_items['Lance'] = {
    # Контос (contus).
    # You have disadvantage when you use a lance to attack a target within 5 feet of you.
    # Also, a lance requires two hands to wield when you aren't mounted. 
    'weapon':True,
    'only_mounted':True,
    'disadvantage_close':True,
    'weapon_type':['martial','close','reach'],
    'damage_type':'piercing',
    'damage_dice':'1d12',
    'weight (lb)':6,
    'cost (gp)':10,
    'cost (grams_of_gold)':5,
    }

metadict_items['Longsword'] = {
    # Гладиус майор, спата (спафа, спатула -- лопата),
    # Энсис (римский термин) (от санскритского "аси" -- меч/нож)
        # https://en.wikipedia.org/wiki/Spatha
        # https://en.wikipedia.org/wiki/Sword_of_Goujian
        # https://lurkmore.so/images/7/79/Jian_true.jpg
        # https://upload.wikimedia.org/wikipedia/commons/0/01/Spadalongobarda.jpg
    # Sword and Lance: About two pounds (32 gp)
    'weapon':True,
    'weapon_type':['martial','close','versatile'],
    'damage_type':'slashing',
    'damage_dice':'1d8',
    'damage_dice_versatile':'1d10',
    'weight (lb)':3,
    'cost (gp)':15,
    'cost (grams_of_gold)':25,
    }

metadict_items['Maul'] = {
    'weapon':True,
    #'shield_breaker':True,
    'weapon_type':['martial','close','heavy','two_handed'],
    'damage_type':'bludgeoning',
    'damage_dice':'2d6',
    'weight (lb)':10,
    'cost (gp)':10,
    'cost (grams_of_gold)':5,
    }

metadict_items['Morningstar'] = {
    'weapon':True,
    'weapon_type':['martial','close'],
    'damage_type':'piercing',
    'damage_dice':'1d8',
    'weight (lb)':4,
    'cost (gp)':15,
    'cost (grams_of_gold)':10,
    }

metadict_items['Pike'] = {
    # Сарисса, ~6 метров.
    'weapon':True,
    'weapon_type':['martial','close','reach','two_handed','heavy'],
    'damage_type':'piercing',
    'damage_dice':'1d10',
    'weight (lb)':18,
    'cost (gp)':5,
    'cost (grams_of_gold)':5,
    }

metadict_items['Rapier'] = {
    # "Рапиры бронзового века"
    'weapon':True,
    'weapon_type':['martial','close','finesse'],
    'damage_type':'piercing',
    'damage_dice':'1d8',
    'weight (lb)':2,
    'cost (gp)':25,
    'cost (grams_of_gold)':30,
    }

metadict_items['Scimitar'] = {
    # Копис (буквально -- "рубило"), сика, махайра ("маха, махиа" -- бой), фальката (ensis falcatus)
    # Копис -- клинок с обратным изгибом, утяжелённое к концу лезвие в ~65 см.
    # https://en.wikipedia.org/wiki/Sica
    'weapon':True,
    'weapon_type':['martial','close','finesse','light'],
    'damage_type':'slashing',
    'damage_dice':'1d6',
    'weight (lb)':3,
    'cost (gp)':25,
    'cost (grams_of_gold)':25,
    }

metadict_items['Shortsword'] = {
    # От дня до недели работы мастера (50-200 мечей/год, 5 gp/клинок)
    # Акинак (акинакос), ксифос (греческий), гладиус, гладия (стебель), семи-спата (полу-меч).
    # Гладия (кладес -- ущерб/рана, от "келлад", прото-индоевропейский "кел" -- ударять/бить)
        # https://en.wikipedia.org/wiki/Acinaces
        # https://ru.wikipedia.org/wiki/Гладиус
        # https://www.larp.com/legioxx/gladius.html
    'weapon':True,
    'weapon_type':['martial','close','finesse','light'],
    'damage_type':'piercing',
    'damage_dice':'1d6',
    'weight (lb)':2,
    'cost (gp)':10,
    'cost (grams_of_gold)':10,
    }

#----
# Martial Ranged Weapons

metadict_items['Crossbow, Heavy'] = {
    # Скорпион.
    'weapon':True,
    'loading':True,
    'ammo_type':'Crossbow Bolt',
    'weapon_type':['martial','ranged','volley','two_handed','heavy'],
    'damage_type':'piercing',
    'damage_dice':'1d8',
    'shoot_range':100,
    'shoot_range_max':400,
    'weight (lb)':18,
    'cost (gp)':50,
    'cost (grams_of_gold)':100,
    }

metadict_items['Longbow'] = {
    # TODO: урон 1d6, потому что иначе лучники просто уничтожают.
    # Композитный лук, но не английский "длинный лук":
    # https://upload.wikimedia.org/wikipedia/commons/c/c5/KaiyuanBowStrung.jpg
    'weapon':True,
    'ammo_type':'Arrow',
    'weapon_type':['martial','ranged','volley','two_handed'],
    'damage_type':'piercing',
    #'damage_dice':'1d8',
    'damage_dice':'1d6',
    'shoot_range':150,
    'shoot_range_max':600,
    'weight (lb)':2,
    'cost (gp)':50,
    'cost (grams_of_gold)':50,
    }

#----
# Martial Ranged Weapons

metadict_items['Arrow'] = {
    # Нормальная стрела длинного/композитного лука весит 70 грамм.
    # Следовательно, 20 стрел -- 3 фунта, а не 1 фунт, как в правилах D&D.
    # Изготовление стрел -- 0.5-2 человеко-часа (включая железный наконечник, работу кузнеца)
    # Другие данные -- 1000 стрел за два месяца (17 стрел/сутки)
    'ammo':True,
    'weight (lb)':3/20,
    'cost (gp)':1/20,
    'cost (grams_of_gold)':4 / 60,
    }

metadict_items['Crossbow Bolt'] = {
    'ammo':True,
    'weight (lb)':3/20,
    'cost (gp)':1/20,
    'cost (grams_of_gold)':4 / 60,
    }

metadict_items['Sling Bullet'] = {
    # Глиняные шарики, одинаковые по форме и размеру.
    # Масса хорошего снаряда для пращи -- 300-400 грамм.
    # Лучше бы свинцовые/железные шарики, но они дорогие (чугун 140 грамм/фоллис).
    'ammo':True,
    'weight (lb)':0.9,
    'cost (sp)':1/20,
    'cost (grams_of_gold)':2 / 60,
    }

#-------------------------------------------------------------------------
# Simple Melee Weapons (homebrew)

metadict_items['Pick-axe'] = {
    # Кирко-мотыга для земляных работ.
    # https://en.wikipedia.org/wiki/Dolabra
    'weapon':True,
    'weapon_type':['simple','close','light'],
    'damage_type':'piercing',
    'damage_dice':'1d6',
    'weight (lb)':2,
    'cost (gp)':5,
    'cost (grams_of_gold)':1,
    }

#----
# Simple Throw Weapons (homebrew)

metadict_items['Pilum'] = {
    # Пилум. Длина 1.8 метра, вес 2-5 фунтов (0.9-2.3 кг).
    # Половина длины -- железный наконечник. Хрен обрубишь.
    # Метается на 10-30 метров. Застревают в щитах.
    'weapon':True,
    'shield_breaker':True,
    'weapon_type':['simple','throw'],
    'damage_type':'piercing',
    'damage_dice':'1d6',
    'throw_range':30,
    'throw_range_max':120,
    'weight (lb)':3,
    'cost (sp)':5,
    'cost (grams_of_gold)':30 / 60,
    }

metadict_items['Plumbata'] = {
    # Тяжёлый дротик, плюмбата (маттиобарбули, "марсова колючка")
        # Оружие поздней Римской империи, 3-4 века нашей эры.
        # Длина 30-50 см, вес 200-350 грамм
        # https://ru.wikipedia.org/wiki/Плюмбата
    # Метается на 30-60 метров (100-200 футов).
    'weapon':True,
    'weapon_type':['simple','finesse','throw'],
    'damage_type':'piercing',
    'damage_dice':'1d6',
    'throw_range':30,
    'throw_range_max':120,
    'weight (lb)':1,
    'cost (sp)':1,
    'cost (grams_of_gold)':20 / 60,
    }

metadict_items['Bolas'] = {
    # Болас. Два камня и верёвка. Может сбить с ног (DC 10):
    # https://www.dandwiki.com/wiki/Bolas_(5e_Equipment)
    'weapon':True,
    'weapon_type':['simple','throw','prone'],
    'damage_type':'bludgeoning',
    'damage_dice':'1d4',
    'throw_range':20,
    'throw_range_max':60,
    'weight (lb)':2,
    'cost (gp)':1,
    'cost (grams_of_gold)':10 / 60,
    }

#----
# Simple Ranged Weapons (homebrew)

metadict_items['Sling real'] = {
    # Дальность бросков из пращи -- 600 футов (но это неприцельно)
    # Лучше всего свинцовые шарики (плотные, меньше трутся о воздух)
    'weapon':True,
    'ammo_type':'Sling Bullet',
    'weapon_type':['simple','ranged','volley'],
    'damage_type':'bludgeoning',
    'damage_dice':'1d4',
    'shoot_range':60,
    'shoot_range_max':300,
    'weight (lb)':1,
    'cost (sp)':1,
    'cost (grams_of_gold)':10 / 60,
    }

metadict_items['Hunting Bow'] = {
    # Оружие ополченцев, лёгкие стрелы с кремневыми наконечниками.
    'weapon':True,
    'ammo_type':'Hunting Arrow',
    'weapon_type':['simple','ranged','volley','two_handed'],
    'damage_type':'piercing',
    'damage_dice':'1d4',
    'shoot_range':60,
    'shoot_range_max':320,
    'weight (lb)':2,
    'cost (gp)':25,
    'cost (grams_of_gold)':5,
    }

metadict_items['Hunting Arrow'] = {
    # Охотничья стрела с оперением, наконечник из заострённого камня.
    'ammo':True,
    'weight (lb)':2/20,
    'cost (gp)':1/20,
    'cost (grams_of_gold)':1 / 60,
    }

#-------------------------------------------------------------------------
# Martial Melee Weapons (homebrew)

metadict_items['Long Spear'] = {
    # Дори, копьё гоплитов. 3 метра, 1-2 килограмма.
        # https://en.wikipedia.org/wiki/Dory_(spear)
        # https://en.wikipedia.org/wiki/Hoplite#Spear
        # Древко 2.5 см диаметр, ясень -- 650 кг/кубометр:
        # Древко: 3.14159265*0.0125^2*3*650=0.96 килограмма.
    'weapon':True,
    'weapon_type':['martial','close','reach','versatile','heavy'],
    'damage_type':'piercing',
    'damage_dice':'1d6',
    'damage_dice_versatile':'1d8',
    'weight (lb)':6,
    'cost (gp)':5,
    'cost (grams_of_gold)':5,
    }

#-------------------------------------------------------------------------
# Martial Ranged Weapons (homebrew)

metadict_items['Chakram'] = {
    # https://www.flight-toys.com/rings/chackrum.html
    # https://www.dandwiki.com/wiki/Chakram_(5e_Equipment)
    # https://www.dandwiki.com/wiki/Chakri_(5e_Equipment)
    'weapon':True,
    'weapon_type':['martial','finesse','light','throw'],
    'damage_type':'slashing',
    'damage_dice':'1d6',
    'throw_range':60,
    'throw_range_max':300,
    'weight (lb)':1,
    'cost (gp)':15,
    'cost (grams_of_gold)':2,
    }

#-------------------------------------------------------------------------
# Доспехи
# https://www.dandwiki.com/wiki/5e_SRD:Armor

#----
# Light Armor

metadict_items['Padded Armor'] = {
    # Стёганка, гамбезон, subarmalis, лорика линтеа
        # https://www.larp.com/legioxx/subarm.html
    # Линоторакс (15-30 слоёв прошитой ткани, ~60 кв.метров)
        # https://en.wikipedia.org/wiki/Linothorax
        # https://www.larp.com/hoplite/linothor.html
        # https://www.larp.com/hoplite/unglued6.jpg
        # https://www.larp.com/hoplite/unglued7.jpg
    # Quality gambeson and other clothing items: About five to ten shillings (4-8 gp)
    'armor':True,
    'armor_type':'light',
    'armor_class_armor':11,
    'armor_stealth_disadvantage':True,
    'weight (lb)':8,
    'cost (gp)':5,
    'cost (grams_of_gold)':5,
    }

metadict_items['Leather Armor'] = {
    # Spolas -- Leather Tube-and-Yoke Cuirass:
        # 12 to 14-ounce vegetable-tanned leather. It weighs ten pounds.
        # https://www.larp.com/hoplite/spolas1.jpg
    'armor':True,
    'armor_type':'light',
    'armor_class_armor':11,
    'weight (lb)':10,
    'cost (gp)':10,
    'cost (grams_of_gold)':10,
    }

metadict_items['Studded Leather'] = {
    # Кожаная броня (Spolas), шлем, широкий бронзовый пояс, нагрудная пластина:
        # Доспех италийского воина (5-4 век до н.э.):
        # https://andrewbek-1974.livejournal.com/874141.html
        # Снаряжение самнитского воина, 4/3 век до нашей эры:
        # https://andrewbek-1974.livejournal.com/619601.html
        # Шлемы иллирийского типа:
        # https://andrewbek-1974.livejournal.com/1125034.html
        # Шлем республиканского легионера:
        # https://andrewbek-1974.livejournal.com/1001125.html
    'armor':True,
    'armor_type':'light',
    'armor_class_armor':12,
    'weight (lb)':15,
    'cost (gp)':20,
    'cost (grams_of_gold)':20,
    }

#----
# Medium Armor

metadict_items['Hide Armor'] = {
    'armor':True,
    'armor_type':'medium',
    'armor_class_armor':12,
    'weight (lb)':12,
    'cost (gp)':10,
    'cost (grams_of_gold)':10,
    }

metadict_items['Chain Shirt'] = {
    # Кольчуга, Лорика хамата (макула):
        # https://www.larp.com/legioxx/hamata.html
        # https://en.wikipedia.org/wiki/Lorica_hamata
        # http://home.armourarchive.org/members/andersh/Reenactment/Joutij%e4rvi.pdf
    # Изготовление кольчужной рубахи (10-13 век н.э.) -- 20-30 тыс. колец, 250-750 человеко-часов.
        # Вес от 7-11 килограмм (14-22 фунта), до 12-13 кг (24 фунта).
        # Кольца диаметром 5-10 мм, плоские, вырезали из листового железа, плетение четыре в одно.
        # Кольца смазывали жиром, чтобы не ржавели (но не оливковым/льняным маслом -- оно липнет)
        # https://upload.wikimedia.org/wikipedia/commons/e/ea/Legio_XXI_Rapax_-_Reparatur_Lorica_hamata_-_Sechsel%C3%A4uten_2011-04-11_15-30-58.jpg
    # Mail armor: Five to eight English pounds (80-144 gp).
    'armor':True,
    'armor_type':'medium',
    'armor_class_armor':13,
    'weight (lb)':20,
    'cost (gp)':50,
    'cost (grams_of_gold)':60,
    }

metadict_items['Scale Mail'] = {
    # Чешуйчатый доспех (лорика сквамата)
        # https://www.larp.com/legioxx/squamata.html
            # https://www.larp.com/legioxx/squam.gif
            # https://www.larp.com/legioxx/squam1.jpg
            # https://www.larp.com/legioxx/DMlam.jpg
        # https://en.wikipedia.org/wiki/Lorica_squamata
            # https://upload.wikimedia.org/wikipedia/commons/4/45/Roman_scale_armour_detail.JPG
    # The Shoulder-Flap-Cuirass from Golyamata Mogila
        # https://www.larp.com/hoplite/f2278.jpg
        # https://bookandsword.com/2016/02/27/the-shoulder-flap-cuirass-from-golyamata-mogila/
    # Византийский ламмеляр (12-13 век н.э.) -- 25x13x0.8-мм чешуи, 10 кг (20 фунтов)
    # 1-2 кв.метр, 3000-6000 железных/бронзовых чешуй -- 200-800 человеко-часов.
    # Бронник зарабатывает 300 gp/год (3-12 доспехов/год, 25-100 gp/доспех)
    'armor':True,
    'armor_type':'medium',
    'armor_class_armor':14,
    'armor_stealth_disadvantage':True,
    'weight (lb)':40,
    'cost (gp)':50,
    'cost (grams_of_gold)':60,
    }

metadict_items['Breastplate'] = {
    # Снаряжение гоплита. Гелоторакс (Helotorax). Бронзовый панцирь, поножи, шлем.
        # https://en.wikipedia.org/wiki/Hoplite
        # Доспех этрусского воина (3-4 век до н.э.):
        # https://andrewbek-1974.livejournal.com/874690.html
        # Снаряжение гоплита (7-5 век до н.э.)
        # https://andrewbek-1974.livejournal.com/597112.html
        # https://andrewbek-1974.livejournal.com/1509338.html
        # https://andrewbek-1974.livejournal.com/1289428.html
        # https://upload.wikimedia.org/wikipedia/commons/e/ea/Greek_bronze_panoply_in_RMO_AvL.JPG
    # Вес бронзы комплекта доспехов -- ~12 кг (16 gp стоимость)
        # Шлем коринфского типа -- 1.5 кг (с подшлемником ~3 lb)
        # Кираса -- 3 кг при 0.5-мм толщине (6 кг при средних 1-мм)
        # Поножи -- 0.7x2=1.4 кг. Оба с подкладками -- 3 lb
        # https://www.larp.com/hoplite/greekarmor.html
    # Бронник зарабатывает 300 gp/год (3-12 доспехов/год, 25-100 gp/доспех)
    'armor':True,
    'armor_type':'medium',
    'armor_class_armor':14,
    'weight (lb)':30,
    'cost (gp)':400,
    'cost (grams_of_gold)':120,
    }

metadict_items['Half Plate'] = {
    # Шлем, рельефный панцирь, поножи, набедренники, но без наручей:
        # https://en.wikipedia.org/wiki/Muscle_cuirass
        # Полная броня античного воина, бронза, 4-3 век до н.э.
        # https://andrewbek-1974.livejournal.com/531607.html
        # ДОСПЕХ ЭТРУССКОГО ВОИНА, 5-4 века до нашей эры:
        # https://andrewbek-1974.livejournal.com/687068.html
        # Шлем халкидского типа
        # https://andrewbek-1974.livejournal.com/967215.html?nojs=1
    'armor':True,
    'armor_type':'medium',
    'armor_class_armor':15,
    'armor_stealth_disadvantage':True,
    'weight (lb)':40,
    'cost (gp)':750,
    'cost (grams_of_gold)':240,
    }

#----
# Heavy Armor

metadict_items['Ring Mail'] = {
    # Ламинарный доспех (лорика сегментата)
        # Доспех Римской империи, 1-4 века нашей эры.
        # 40 крупных пластин, внахлёст, 8-10 килограмм.
        # https://ru.wikipedia.org/wiki/Ламинарный_доспех
        # https://ru.wikipedia.org/wiki/Лорика_сегментата
        # https://www.larp.com/legioxx/lorica.html
        # https://www.larp.com/legioxx/lorbag2.jpg
    'armor':True,
    'armor_type':'heavy',
    'armor_class_armor':14,
    'armor_stealth_disadvantage':True,
    'weight (lb)':40,
    'cost (gp)':30,
    'cost (grams_of_gold)':30,
    }

metadict_items['Chain Mail'] = {
    # Изготовление хауберка -- 50 тыс. колец, 500-1500 человеко-часов.
    # Mail armor: Five to eight English pounds (80-144 gp).
    'armor':True,
    'armor_type':'heavy',
    'armor_class_armor':16,
    'armor_stealth_disadvantage':True,
    #'armor_need_strenght':13,
    'weight (lb)':55,
    'cost (gp)':75,
    'cost (grams_of_gold)':120,
    }

metadict_items['Splint Armor'] = {
    # "Наборный доспех", бахтерец, колонтарь:
        # https://ru.wikipedia.org/wiki/Колонтарь
        # https://upload.wikimedia.org/wikipedia/commons/2/2d/Indian_mail_and_plate_armour%2C_Met_Museum.jpg
        # https://upload.wikimedia.org/wikipedia/commons/b/be/Tatami_gusoku_Met_14.100.538_n2.jpg
    # Лорика серта. Лорика плюмата. Чешуйчатый доспех на кольчужной основе.
        # https://en.wikipedia.org/wiki/Lorica_plumata
        # https://www.tapatalk.com/groups/romanarmytalk/lorica-plumata-scales-t696.html
    'armor':True,
    'armor_type':'heavy',
    'armor_class_armor':17,
    'armor_stealth_disadvantage':True,
    #'armor_need_strenght':15,
    'weight (lb)':60,
    'cost (gp)':200,
    'cost (grams_of_gold)':240,
    }

metadict_items['Plate Armor'] = {
    'armor':True,
    'armor_type':'heavy',
    'armor_class_armor':18,
    'armor_stealth_disadvantage':True,
    #'armor_need_strenght':15,
    'weight (lb)':65,
    'cost (gp)':1500,
    'cost (grams_of_gold)':1500,
    }

#-------------------------------------------------------------------------
# Light Armor (homebrew)

metadict_items['Mage_Armor'] = {
    # Создаётся заклинанием Mage_Armor, действует 8 часов.
    'armor':True,
    'armor_type':'Force',
    'armor_class_armor':13,
    'weight (lb)':0,
    'cost (gp)':1,
    'cost (grams_of_gold)':1,
    }

metadict_items['Draconic_Scales'] = {
    # От чародейского Draconic_Bloodline
    'armor':True,
    'armor_type':'Force',
    'armor_class_armor':13,
    'weight (lb)':0,
    'cost (gp)':1,
    'cost (grams_of_gold)':1,
    }

#----
# Броня для лошадей (homebrew):

metadict_items['Horse Scale Mail'] = {
    'armor':True,
    'armor_type':'medium',
    'armor_class_armor':14,
    'armor_stealth_disadvantage':True,
    'weight (lb)':45 * 2,
    'cost (gp)':50 * 4,
    'cost (grams_of_gold)':60 * 4,
    }

#----
# Shield

metadict_items['Shield'] = {
    # Shield: About five to ten shillings, or a quarter to half pound (4-8 gp)
    'shield':True,
    'armor_type':'shield',
    'armor_class_shield':2,
    'weight (lb)':6,
    'cost (gp)':10,
    'cost (grams_of_gold)':5,
    }

#----
# Shield (homebrew)
    # TODO: щит с AC 3, или щит с AC 5. Сложный вопрос.
    # ------------------------------------------------------------
    # Щиты AC 3; 150 лучников, 6000 стрел (400 gp), 4 минуты неприцельного обстрела:
    # - Расход стрел по гоплитам....(16.1 AC) 1300/100 урона (45 стрел/попадание)
    # - Расход стрел по копейщикам..(15.0 AC) 1000/100 урона (38 стрел/попадание)
    # - Расход стрел по пращникам...(13.3 AC) 500/100 урона (18 стрел/попадание)
    # - Расход стрел по лучникам....(11.4 AC) 400/100 урона (13 стрел/попадание)
    # ------------------------------------------------------------
    # Щиты AC 5; 150 лучников, 6000 стрел (400 gp), 4 минуты неприцельного обстрела:
    # - Расход стрел по гоплитам....(18.0 AC) 2600/100 урона (110 стрел/попадание)
    # - Расход стрел по копейщикам..(17.0 AC) 1700/100 урона (70 стрел/попадание)
    # ------------------------------------------------------------

metadict_items['Heavy Shield'] = {
    # Гоплон (оплон, аспис), римский ростовый (туреос, фуреос) -- 14-18 фунтов, (6.5-8 кг)
        # Диаметр 0.8-1 метр. Кожа, дерево, 0.5 мм бронзы (3.3 кг бронзы на щит, 5 gp)
        # https://ru.wikipedia.org/wiki/Гоплон
        # https://en.wikipedia.org/wiki/Aspis
        # https://en.wikipedia.org/wiki/Hoplite#Shield
        # https://www.larp.com/hoplite/hoplon.html
    # Скутум -- 10 килограмм. Республиканские овальные, имперские прямоугольные.
        # https://www.larp.com/legioxx/scutum.html
    'shield':True,
    'mounted_disadvantage':True,
    'armor_type':'shield',
    'armor_class_shield':3,
    'weight (lb)':16,
    'cost (gp)':20,
    'cost (grams_of_gold)':20,
    }

metadict_items['Tower Shield'] = {
    # Павеза. Непригоден для ближнего боя.
    'shield':True,
    'melee_disadvantage':True,
    'mounted_disadvantage':True,
    'armor_type':'shield',
    'armor_class_shield':5,
    'weight (lb)':32,
    'cost (gp)':20,
    'cost (grams_of_gold)':20,
    }

#-------------------------------------------------------------------------
# Mounts (homebrew)

metadict_items['Donkey'] = {
    # Тяговое усилие -- 0.15 массы тела.
    # Груз во вьюках -- 0.3 массы тела (240 lb)
    'mount':True,
    'weight (lb)':800,
    'carring capacity (lb)':240,
    'cost (gp)':8,
    'cost (grams_of_gold)':12,
    }

metadict_items['Riding Horse'] = {
    # Нормальная нагрузка верховой лошади -- 200-240 фунтов (а не дикие 480 lb)
    # Byzantine warhorse maximum value was -- 10 solidi (50 grams_of_gold)
    'mount':True,
    'weight (lb)':800,
    'carring capacity (lb)':240,
    'cost (gp)':75,
    'cost (grams_of_gold)':60,
    }

metadict_items['Warhorse'] = {
    # Это не рыцарские тяжеловозы, обычные коняги весом в 500 килограмм, только обученные бою.
    # Quality war horse and gear: At least ten pounds, up to fifty for a top of the line mount (160-800 gp)
    'mount':True,
    'weight (lb)':1000,
    'carring capacity (lb)':240,
    'cost (gp)':400,
    'cost (grams_of_gold)':240,
    }

#-------------------------------------------------------------------------
# Adventuring Gear
# https://www.dandwiki.com/wiki/5e_SRD:Adventuring_Gear

metadict_items['Healer\'s Kit'] = {
    # На 10 использований:
    'gear':True,
    'healer':True,
    'weight (lb)':3,
    'cost (gp)':5,
    'cost (grams_of_gold)':5,
    }

metadict_items['Clothes, Common'] = {
    # Льняная туника или шерстяной хитон.
        # Размеры 0.9x1.2 метра (~1 кв. метра)
        # https://www.larp.com/legioxx/tunic.html
        # https://www.larp.com/legioxx/caligae.html
        # https://www.larp.com/legioxx/leather.html
        # https://www.larp.com/hoplite/greekclothes.html
    # DIOCLETIAN'S EDICT ON MAXIMUM PRICES:
        # Товар                      | Денарии  | Мера         | Перевод (60 Folles = 1 gp)
        # -------------------------- | -------- | ------------ | -----------------
        # soldier's winter tunic     | 60       |              | 6 Folles
        # boots for soldiers         | 100      |              | 10 Folles
        # soldier's shoes            | 75       |              | 7.5 Folles
        # Gallic sandals for runners | 60       |              | 6 Folles
    'gear':True,
    'weight (lb)':3,
    'cost (sp)':5,
    'cost (grams_of_gold)':1,
    }

metadict_items['Clothes, Fine'] = {
    # Тога, размеры 1.8x3.6 метра (6.5 кв.метра)
        # https://www.larp.com/legioxx/civcloth.html
    # DIOCLETIAN'S EDICT ON MAXIMUM PRICES:
        # Товар                      | Денарии  | Мера         | Перевод (60 Folles = 1 gp)
        # -------------------------- | -------- | ------------ | -----------------
        # patrician's shoes          | 150      |              | 15 Folles
        # Dalmatian tunic            | 2000     |              | 200 Folles
        # Fuller (Wool weaver)       | 175      | per cloak    | 17.5 Folles/плащ
        # wool from Tarentum         | 100      | Libra        | 30 Folles/кг
        # white silk                 | 12,000   | Libra        | 3600 Folles/кг
    'gear':True,
    'weight (lb)':6,
    'cost (gp)':15,
    'cost (grams_of_gold)':15,
    }

metadict_items['Saddle'] = {
    # https://www.dandwiki.com/wiki/5e_SRD:Mounts_and_Vehicles
    # DIOCLETIAN'S EDICT ON MAXIMUM PRICES:
        # Товар                      | Денарии  | Мера         | Перевод (60 Folles = 1 gp)
        # -------------------------- | -------- | ------------ | -----------------
        # Saddle                     | 500      |              | 50 Folles
    'gear':True,
    'weight (lb)':3,
    'cost (gp)':10,
    'cost (grams_of_gold)':1,
    }

metadict_items['Waterskin (full)'] = {
    'gear':True,
    'weight (lb)':5,
    'cost (sp)':2,
    'cost (grams_of_gold)':10 / 60,
    }

metadict_items['Rations (1 day)'] = {
    # Рационы, это важно! Здесь мы определяем стоимость найма ополченцев. Да и проф. солдат.
    # Пшеничные/ячменные лепёшки, овсяная и бобовая каши, оливковое масло, рыба и вино.
    'gear':True,
    'weight (lb)':2,
    'cost (sp)':5,
    'cost (grams_of_gold)':2 / 60,
    }

metadict_items['Tinderbox'] = {
    'gear':True,
    'weight (lb)':1,
    'cost (sp)':5,
    'cost (grams_of_gold)':30 / 60,
    }

metadict_items['Mess Kit'] = {
    'gear':True,
    'weight (lb)':1,
    'cost (sp)':2,
    'cost (grams_of_gold)':1,
    }

metadict_items['Cloak'] = {
    # Шерстяной плащ, он же спальник, Bedroll
        # https://www.larp.com/legioxx/cloak.html
    # DIOCLETIAN'S EDICT ON MAXIMUM PRICES:
        # Товар                      | Денарии  | Мера         | Перевод (60 Folles = 1 gp)
        # -------------------------- | -------- | ------------ | -----------------
        # African cloak              | 500      |              | 50 Folles
        # hooded cloak, Laodicean    | 4500     |              | 450 Folles
        # wool from Tarentum         | 100      | Libra        | 30 Folles/кг
        # Fuller (Wool weaver)       | 175      | per cloak    | 17.5 Folles/плащ
    # Плащ с капюшоном делают из куска ~4 кв. метра (форма овальная, капюшон из обрезков)
    # Ткачество -- 1.7 дней/1 кв.метр, 7 дней/плащ (~30 плащей/год)
    'gear':True,
    'weight (lb)':4,
    'cost (gp)':1,
    'cost (grams_of_gold)':1,
    }

metadict_items['Backpack'] = {
    'gear':True,
    'weight (lb)':5,
    'cost (gp)':2,
    'cost (grams_of_gold)':1,
    }

#----
# Magic items:

metadict_items['Infusion of Healing'] = {
    # Эссенции "перезаряжаются" друидами и жрецами.
    # Лечение равно костям хитов бойца. Для варвара 5 lvl это 5d12, в среднем 30 hp.
    'potion':True,
    'effect':'healing',
    #'healing_dice':'2d4',
    #'healing_mod':2,
    'weight (lb)':1/2,
    'cost (gp)':50,
    'cost (grams_of_gold)':60,
    }

metadict_items['Infusion of Claws'] = {
    # Эссенции "перезаряжаются" друидами и жрецами.
    'potion':True,
    'weapon':True,
    'weapon_type':['simple','close','finesse','magic','+1'],
    'damage_type':'piercing',
    'damage_dice':'1d6',
    'weight (lb)':1/2,
    'cost (gp)':240,
    'cost (grams_of_gold)':240,
    }

metadict_items['Rune of Absorbtion'] = {
    # Руны перезаряжаются магами.
    'potion':True,
    'effect':'absorb',
    'absorb_damage_type':['acid','cold','fire','lightning','thunder'],
    'damage_type':'absorbed',
    'damage_dice':'1d6',
    'weight (lb)':1/2,
    'cost (gp)':240,
    'cost (grams_of_gold)':240,
    }

metadict_items['Rune of Shielding'] = {
    'potion':True,
    'effect':'shield',
    'weight (lb)':1/2,
    'cost (gp)':240,
    'cost (grams_of_gold)':240,
    }

metadict_items['Rune of Armor'] = {
    # Стоит как полулаты, зато очень лёгкая.
    'armor':True,
    'potion':True,
    'effect':'armor',
    'armor_type':'Force',
    'armor_class_armor':13,
    'weight (lb)':1/2,
    'cost (gp)':240,
    'cost (grams_of_gold)':240,
    }

#----
# Magic Weapon (homebrew)

#metadict_items['Sword of the Past'] = {
#    'weapon':True,
#    'weapon_type':['martial','close','versatile','+2','sword_burst'],
#    'damage_type':'slashing',
#    'damage_dice':'1d8',
#    'damage_dice_versatile':'1d10',
#    'weight (lb)':3,
#    'cost (gp)':300*60,
#    'cost (grams_of_gold)':300*60,
#    }

metadict_items['Sword of the Past'] = {
    # Клинок былого
    'weapon':True,
    'weapon_type':['martial','close','two_handed','heavy','magic','+2','sword_burst'],
    'damage_type':'slashing',
    'damage_dice':'2d6',
    'weight (lb)':6,
    'cost (gp)':300*60,
    'cost (grams_of_gold)':300*60,
    }

metadict_items['Empyrean_Maul'] = {
    # Большие существа теперь наносят x2 урона оружием 2d6 --> 4d6:
    'weapon':True,
    'weapon_type':['martial','close','two_handed','heavy','magic', '+1'],
    'damage_type':'bludgeoning',
    'damage_dice':'2d6',
    #'damage_dice':'6d6',
    'weight (lb)':10*4,
    'cost (gp)':300*60,
    'cost (grams_of_gold)':300*60,
    }

#----
# Martial Weapons +1

metadict_items['Shortsword +1'] = {
    'weapon':True,
    'weapon_type':['martial','close','finesse','light','magic','+1'],
    'damage_type':'piercing',
    'damage_dice':'1d6',
    'weight (lb)':2,
    'cost (gp)':600,
    'cost (grams_of_gold)':600,
    }

metadict_items['Scimitar +1'] = {
    'weapon':True,
    'weapon_type':['martial','close','finesse','light','magic','+1'],
    'damage_type':'slashing',
    'damage_dice':'1d6',
    'weight (lb)':3,
    'cost (gp)':600,
    'cost (grams_of_gold)':600,
    }

metadict_items['Longsword +1'] = {
    'weapon':True,
    'weapon_type':['martial','close','versatile','magic','+1'],
    'damage_type':'slashing',
    'damage_dice':'1d8',
    'damage_dice_versatile':'1d10',
    'weight (lb)':3,
    'cost (gp)':600,
    'cost (grams_of_gold)':600,
    }

metadict_items['Greatsword +1'] = {
    'weapon':True,
    #'shield_breaker':True,
    'weapon_type':['martial','close','two_handed','heavy','magic','+1'],
    'damage_type':'slashing',
    'damage_dice':'2d6',
    'weight (lb)':6,
    'cost (gp)':600,
    'cost (grams_of_gold)':600,
    }

metadict_items['Glaive +1'] = {
    'weapon':True,
    #'shield_breaker':True,
    'weapon_type':['martial','close','reach','two_handed','heavy','magic','+1'],
    'damage_type':'slashing',
    'damage_dice':'1d10',
    'weight (lb)':6,
    'cost (gp)':600,
    'cost (grams_of_gold)':600,
    }

metadict_items['Long Spear +1'] = {
    'weapon':True,
    'weapon_type':['martial','close','reach','versatile','heavy','magic','+1'],
    'damage_type':'piercing',
    'damage_dice':'1d6',
    'damage_dice_versatile':'1d8',
    'weight (lb)':6,
    'cost (gp)':600,
    'cost (grams_of_gold)':600,
    }

#----
# Ranged Weapons +1

metadict_items['Shortbow +1'] = {
    'weapon':True,
    'ammo_type':'Arrow',
    'weapon_type':['simple','ranged','volley','two_handed','magic', '+1'],
    'damage_type':'piercing',
    'damage_dice':'1d6',
    'shoot_range':80,
    'shoot_range_max':320,
    'weight (lb)':2,
    'cost (gp)':600,
    'cost (grams_of_gold)':600,
    }

metadict_items['Longbow +1'] = {
    'weapon':True,
    'ammo_type':'Arrow',
    'weapon_type':['martial','ranged','volley','two_handed','magic', '+1'],
    'damage_type':'piercing',
    #'damage_dice':'1d8',
    'damage_dice':'1d6',
    'shoot_range':150,
    'shoot_range_max':600,
    'weight (lb)':2,
    'cost (gp)':600,
    'cost (grams_of_gold)':600,
    }
