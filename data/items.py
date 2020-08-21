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
# Варианты боеприпасов:

blade_poisons = [
        # Покрытия для ближнего оружия:
        'Holy Blade',
        'Poison Blade',
        'Sleep Blade',
        ]

catapult_shells = [
        # Боеприпасы катапульт, онагров, требуше:
        'Ballista Bolt (0.2 lb)',
        'Ballista Bolt (1 lb)',
        'Ballista Bolt (5 lb)',
        'Ballista Bolt (25 lb)',
        'Sling Bullets (x10)',
        'Sling Bullets (x25)',
        'Boulder (10 lb)',
        'Boulder (25 lb)',
        'Boulder (50 lb)',
        'Boulder (100 lb)',
        'Boulder (200 lb)',
        'Alchemist\'s Fire (10/25 lb)',
        'Alchemist\'s Fire (25/50 lb)',
        'Alchemist\'s Fire (100/200 lb)',
        ]

longbow_arrows = [
        # ammo_type
        'Arrow',
        'Arrow +1',
        'Silver Arrow',
        'Hunting Arrow',
        'Slashing Arrow',
        'Poison Arrow',
        'Fire Arrow',
        'Acid Arrow',
        ]

crossbow_bolts = [
        'Crossbow Bolt',
        'Crossbow Bolt +1',
        'Silver Bolt',
        'Hunting Bolt',
        'Slashing Bolt',
        'Poison Bolt',
        'Fire Bolt',
        'Acid Bolt',
        ]

sling_bullets = [
        'Sling Bullet',
        'Sling Bullet +1',
        'Lead Bullet',
        'Fire Bullet',
        'Acid Bullet',
        'Holy Bullet',
        ]

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

metadict_items['Greatclub'] = {
    'weapon':True,
    'weapon_type':['simple','close','two_handed'],
    'damage_type':'bludgeoning',
    'damage_dice':'1d8',
    'weight (lb)':10,
    'cost (sp)':1,
    'cost (grams_of_gold)':1 / 60,
    }

metadict_items['Dagger'] = {
    # Пугио, скрамасакс, паразониум (по-гречески, "на поясе")
    # https://ru.wikipedia.org/wiki/Пугио
    'weapon':True,
    'ammo_type':blade_poisons,
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
    'ammo_type':blade_poisons,
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
    'ammo_type':blade_poisons,
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
    'ammo_type':blade_poisons,
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
    'ammo_type':crossbow_bolts,
    'weapon_type':['simple','ranged','volley','two_handed'],
    'damage_type':'piercing',
    'damage_dice':'1d6',
    'shoot_range':80,
    'shoot_range_max':320,
    'weight (lb)':5,
    'cost (gp)':25,
    'cost (grams_of_gold)':30,
    }

metadict_items['Crossbow, Heavy'] = {
    # Скорпион. Считается простым оружием.
    'weapon':True,
    'loading':True,
    'ammo_type':crossbow_bolts,
    'weapon_type':['simple','ranged','volley','two_handed','heavy'],
    'damage_type':'piercing',
    'damage_dice':'1d10',
    'shoot_range':100,
    'shoot_range_max':600,
    'weight (lb)':18,
    'cost (gp)':50,
    'cost (grams_of_gold)':50,
    }

metadict_items['Dart'] = {
    'weapon':True,
    'ammo_type':blade_poisons,
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
    'ammo_type':longbow_arrows,
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
    'ammo_type':sling_bullets,
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
    'ammo_type':blade_poisons,
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
    'ammo_type':blade_poisons,
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
    'ammo_type':blade_poisons,
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
    'ammo_type':blade_poisons,
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
    'ammo_type':blade_poisons,
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
    # Боевой конь (400 килограмм), плюс всадник 100 килограмм:
        # https://www.dandwiki.com/wiki/SRD:Heavy_Warhorse
        # Скорость -- 16 км/час (4.4 м/с) (80 футов/раунд)
        # Импульс: (400 + 100) * 4.4 = 2200 кг*м/с
        # Полная энергия: (500 * 4.4 ** 2) / 2 = 4 840 джоулей (как пуля АКМ)
    # Сила удара рыцарского лэнса (16 км/час) -- 300-600 Дж (600 Дж пробивает 2-мм кирасу)
    'weapon':True,
    'ammo_type':blade_poisons,
    'one_hand_mounted':True,
    'disadvantage_close':True,
    'weapon_type':['martial','close','reach','heavy'],
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
    'ammo_type':blade_poisons,
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
    'ammo_type':blade_poisons,
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
    'ammo_type':blade_poisons,
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
    'ammo_type':blade_poisons,
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
    'ammo_type':blade_poisons,
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
    'ammo_type':blade_poisons,
    'weapon_type':['martial','close','finesse','light'],
    'damage_type':'piercing',
    'damage_dice':'1d6',
    'weight (lb)':2,
    'cost (gp)':10,
    'cost (grams_of_gold)':10,
    }

#----
# Martial Ranged Weapons

metadict_items['Longbow'] = {
    # Композитный лук, но не английский "длинный лук":
        # https://upload.wikimedia.org/wikipedia/commons/c/c5/KaiyuanBowStrung.jpg
    # Стрела лонгбоу на 10 метрах (натяжение 150 фунтов, длина натяжения 30 дюймов) -- 150 Дж 
    # Урон 1d6, потому что иначе лучники просто уничтожают.
    'weapon':True,
    'ammo_type':longbow_arrows,
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

#-------------------------------------------------------------------------
# Simple Melee Weapons (homebrew)

metadict_items['Pick-axe'] = {
    # Кирко-мотыга для земляных работ.
    # https://en.wikipedia.org/wiki/Dolabra
    'weapon':True,
    'ammo_type':blade_poisons,
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
    'ammo_type':blade_poisons,
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

metadict_items['Fire Spear'] = {
    # Огненное копьё, заряд чёрного пороха и металлическая картечь.
    # [b]Илионские огненные копья[/b]:
    # - Урон копья: 1d6
    # - Дальность броска: 10/30 футов (масса копья 6 lb)
    # - Урон взрыва: 1d6, 10-футовый радиус, спасбросок ловкости полный.
    # - Не требует попадания, осколки поражают зону 300 кв. футов.
    # - Спасбросок ловкости полный. Достаточно пригнуться. Осколки не пробьют наклоненный щит.
    # 
    # [b]Заряд и картечь:[/b]
    # - Насыпная плотность пороха -- 0.5 кг/литр
    # - Заряд: 500 грамм картечи, 500 грамм чёрного пороха:
    # - Тротиловый эквивалент дымного пороха -- 0.33 (от 4.184 МДж)
    # 0.5 * 4.184 * 0.33 = 0.7 МДж = 700 кДж (35 кДж энергии картечи при 5% энергии взрыва)
    # КПД взрыва ничтожен, у нас глиняная трубка вместо оболочки. Большую часть пороха просто разбросает.
    # 
    # [b]Зона поражения:[/b]
    # - 10-футовая сфера (3.3 метра радиус)
    # - Плоскость тела стоящего человека 1.8*0.6=1.08 м²
    # - Осколки массой от 2 до 5 грамм (в среднем 3 грамма)
    # (4*3.14159265*3.3^2)*1.08=148 осколков для 100% вероятности попадания (450 грамм картечи).
    # Энергия отдельного осколка -- 236 джоулей (стрела лонгоу на 10 метрах -- 150 джоулей)
    'weapon':True,
    'shield_breaker':True,
    'shield_breaker_absolute':True,
    'weapon_type':['simple','throw'],
    'damage_type':'piercing',
    'damage_dice':'1d6',
    'throw_range':10,
    'throw_range_max':30,
    'spell_dict':{
            'zone':True,
            'safe':False,
            #'zone_shape':'2x2',
            'radius':10,
            'direct_hit':True,
            'savethrow':True,
            'savethrow_all':True,
            'savethrow_ability':'dexterity',
            'damage_type':'piercing',
            'damage_dice':'1d6',
            'spell_save_DC':10,
            'spell_choice':('Fire Spear','Explosion'),
            },
    'weight (lb)':6,
    'cost (gp)':10,
    'cost (grams_of_gold)':10,
    }

metadict_items['Plumbata'] = {
    # Тяжёлый дротик, плюмбата (маттиобарбули, "марсова колючка")
        # Оружие поздней Римской империи, 3-4 века нашей эры.
        # Длина 30-50 см, вес 200-350 грамм
        # https://ru.wikipedia.org/wiki/Плюмбата
    # Метается на 30-60 метров (100-200 футов).
    'weapon':True,
    'ammo_type':blade_poisons,
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
    'ammo_type':sling_bullets,
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
    'ammo_type':longbow_arrows,
    'weapon_type':['simple','ranged','volley','two_handed'],
    'damage_type':'piercing',
    'damage_dice':'1d4',
    'shoot_range':60,
    'shoot_range_max':320,
    'weight (lb)':2,
    'cost (gp)':25,
    'cost (grams_of_gold)':5,
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
    'ammo_type':blade_poisons,
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
    'ammo_type':blade_poisons,
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
    'armor_type':'Mage_Armor',
    'armor_class_armor':13,
    'weight (lb)':0,
    'cost (gp)':1,
    'cost (grams_of_gold)':1,
    }

metadict_items['Barkskin'] = {
    # Создаётся заклинанием Barkskin, действует 1 час концентрации.
    'armor':True,
    'armor_type':'Barkskin',
    'armor_class_armor':16,
    'weight (lb)':0,
    'cost (gp)':1,
    'cost (grams_of_gold)':1,
    }

metadict_items['Draconic_Scales'] = {
    # От чародейского Draconic_Bloodline
    'armor':True,
    'armor_type':'Mage_Armor',
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

metadict_items['Healer Kit'] = {
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

metadict_items['Goodberry'] = {
    # Лечит 1 hp, стабилизирует раненого.
    # Стоимость заклинания от 1 lvl друида: 0.6 gp/10 ягод.
    # Калорийность ягоды -- 2000 килокалорий (400 грамм)
        # - Сумка с 30 ягодами – 30 фунтов.
        # - Корзина с 60 ягодами – 60 фунтов (аттический талант)
        # - Бочка с 1000 ягодами – 1000 фунтов (вес упряжной телеги)
    'potion':True,
    'use_goodberry':True,
    'create_goodberry':False,
    'spell':'Goodberry',
    'weight (lb)':1,
    'cost (gp)':0.6,
    'cost (grams_of_gold)':0.6,
    }

metadict_items['Potion of Bravery'] = {
    # Даёт 1d6 бонусных хитов.
    # Крепкая выпивка, пьянит.
    'spell':'False_Life',
    'potion':True,
    'debuff':True,
    'effect':'poisoned',
    'effect_timer':100,
    'healing_dice':'1d6',
    'healing_mod':0,
    'spell_save_DC':15,
    'weight (lb)':1,
    'cost (gp)':0.06,
    'cost (grams_of_gold)':0.06,
    }

metadict_items['Potion of Antidote'] = {
    # Антидот. Даёт преимущество к спасброскам от ядов.
    'spell':'Antidote',
    'buff':True,
    'potion':True,
    'effect_timer':600,
    'weight (lb)':0.5,
    'cost (gp)':6,
    'cost (grams_of_gold)':6,
    }

metadict_items['Infusion of Healing'] = {
    'potion':True,
    'spell':'Cure_Wounds',
    'weight (lb)':0,
    'cost (gp)':50,
    'cost (grams_of_gold)':60,
    }

metadict_items['Infusion of False Life'] = {
    'potion':True,
    'spell':'False_Life',
    'weight (lb)':0,
    'cost (gp)':60 * 2,
    'cost (grams_of_gold)':60 * 2,
    }

metadict_items['Infusion of Barkskin'] = {
    'potion':True,
    'concentration':False,
    'spell':'Barkskin',
    'weight (lb)':0,
    'cost (gp)':60 * 4,
    'cost (grams_of_gold)':60 * 4,
    }

metadict_items['Infusion of Regeneration'] = {
    # TODO: не работает. Заклинание не указано, да и не сделано.
    'potion':True,
    'effect':'healing',
    #'healing_dice':'1d4',
    'healing_mod':1,
    'weight (lb)':0,
    'cost (gp)':50 * 4,
    'cost (grams_of_gold)':60 * 4,
    }

metadict_items['Infusion of Longstrider'] = {
    'potion':True,
    'spell':'Longstrider',
    'weight (lb)':0,
    'cost (gp)':60,
    'cost (grams_of_gold)':60,
    }

metadict_items['Infusion of Heroism'] = {
    'potion':True,
    'concentration':False,
    'spell':'Heroism',
    'weight (lb)':0,
    'cost (gp)':50,
    'cost (grams_of_gold)':60 * 4,
    }

metadict_items['Infusion of Claws'] = {
    # TODO: переделай в заклинание. Пусть даёт дополнительную атаку.
    # Эссенции "перезаряжаются" друидами и жрецами.
    'potion':True,
    'weapon':True,
    'weapon_type':['simple','close','finesse','magic','+1'],
    'damage_type':'piercing',
    'damage_dice':'1d6',
    'weight (lb)':0,
    'cost (gp)':240,
    'cost (grams_of_gold)':60 * 4,
    }

metadict_items['Rune of Absorbtion'] = {
    # Руны перезаряжаются магами.
    'potion':True,
    'spell':'Absorb_Elements',
    'weight (lb)':1/2,
    'cost (gp)':240,
    'cost (grams_of_gold)':60 * 4,
    }

metadict_items['Rune of Shielding'] = {
    'potion':True,
    'spell':'Shield',
    'weight (lb)':1/2,
    'cost (gp)':240,
    'cost (grams_of_gold)':60 * 4,
    }

metadict_items['Rune of Armor'] = {
    # Стоит как полулаты, зато очень лёгкая.
    'potion':True,
    'spell':'Mage_Armor',
    'weight (lb)':1/2,
    'cost (gp)':240,
    'cost (grams_of_gold)':60 * 4,
    }

metadict_items['Bracers of Defence'] = {
    'effect':'defence',
    'armor_type':'shield',
    'armor_class_shield':2,
    'weight (lb)':2,
    'cost (gp)':60 * 100,
    'cost (grams_of_gold)':60 * 100,
    }

#----
# Magic Weapon (homebrew)

metadict_items['Sword of the Past +2'] = {
    # Клинок былого
    'weapon':True,
    'weapon_type':['martial','close','two_handed','heavy','magic','+2','sword_burst'],
    'damage_type':'slashing',
    'damage_dice':'2d6',
    'spell_dict':{
            'safe':True,
            'zone':True,
            'zone_shape':'square',
            'effect':'burst',
            'direct_hit':True,
            'savethrow':True,
            'savethrow_all':True,
            'savethrow_ability':'dexterity',
            'radius':5,
            'damage_type':'force',
            'damage_dice':'1d6',
            'spell_save_DC':12,
            'spell_choice':('subspell','Sword_Burst'),
            },
    'weight (lb)':6,
    'cost (gp)':5000*60,
    'cost (grams_of_gold)':5000*60,
    }

metadict_items['Sword of Life-Stealing'] = {
    # TODO: сделай это модификациями мечей. Не забудь увеличение стоимости.
    # При крите наносит 10 урона некторической энергией и даёт 10 бонусных хитов.
    'weapon':True,
    #'ammo_type':blade_poisons,
    'weapon_type':['martial','close','versatile','magic'],
    'damage_type':'slashing',
    'damage_dice':'1d8',
    'damage_dice_versatile':'1d10',
    'spell_dict':{
            'safe':True,
            'effect':'steal_life',
            'crit_only':True,
            'direct_hit':True,
            'attacks_number':1,
            'damage_type':'necrotic',
            'damage_dice':'0d0',
            'damage_mod':10,
            'spell_choice':('Sword of Life-Stealing','Steal Life'),
            },
    'weight (lb)':3,
    'cost (gp)':30*60,
    'cost (grams_of_gold)':30*60,
    }

metadict_items['Sword of Sharpness'] = {
    # Наносит предметам максимальный урон.
    # При крите наносит 14 дополнительного урона и при повторном d20 отрубает конечность.
    # Светится на 10+10 футов, активация действием.
    'weapon':True,
    #'ammo_type':blade_poisons,
    'weapon_type':['martial','close','versatile','magic','sharpness'],
    'damage_type':'slashing',
    'damage_dice':'1d8',
    'damage_dice_versatile':'1d10',
    'spell_dict':{
            'safe':True,
            'effect':'sharpness',
            'crit_only':True,
            'direct_hit':True,
            'attacks_number':1,
            'weapon_type':['magic','sharpness'],
            'damage_type':'slashing',
            'damage_dice':'0d0',
            'damage_mod':14,
            'spell_choice':('Sword of Sharpness','Sharpness'),
            },
    'weight (lb)':3,
    'cost (gp)':30*60,
    'cost (grams_of_gold)':30*60,
    }

metadict_items['Staff of Striking +3'] = {
    # Посох ударов
    'weapon':True,
    'versatile':True,
    'weapon_type':['simple','close','versatile','magic','+3'],
    'damage_type':'bludgeoning',
    'damage_dice':'1d6',
    'damage_dice_versatile':'1d8',
    'spell_dict':{
            'safe':True,
            'direct_hit':True,
            'attacks_number':1,
            'attack_range':5,
            'radius':0,
            'damage_type':'force',
            'damage_dice':'3d6',
            'components':[],
            'casting_time':'free_action',
            'damage_mod':0,
            'spell_level':2,
            'spell_save_DC':15,
            'spell_choice':('strike','Staff of Striking'),
            'ammo':3,
            },
    'weight (lb)':4,
    'cost (gp)':4000*60,
    'cost (grams_of_gold)':4000*60,
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
    'ammo_type':blade_poisons,
    'weapon_type':['martial','close','finesse','light','magic','+1'],
    'damage_type':'piercing',
    'damage_dice':'1d6',
    'weight (lb)':2,
    'cost (gp)':30*60,
    'cost (grams_of_gold)':30*60,
    }

metadict_items['Rapier +1'] = {
    # "Рапиры бронзового века"
    'weapon':True,
    'ammo_type':blade_poisons,
    'weapon_type':['martial','close','finesse'],
    'damage_type':'piercing',
    'damage_dice':'1d8',
    'weight (lb)':2,
    'cost (gp)':25,
    'cost (grams_of_gold)':30,
    }

metadict_items['Scimitar +1'] = {
    'weapon':True,
    'ammo_type':blade_poisons,
    'weapon_type':['martial','close','finesse','light','magic','+1'],
    'damage_type':'slashing',
    'damage_dice':'1d6',
    'weight (lb)':3,
    'cost (gp)':30*60,
    'cost (grams_of_gold)':30*60,
    }

metadict_items['Longsword +1'] = {
    'weapon':True,
    'ammo_type':blade_poisons,
    'weapon_type':['martial','close','versatile','magic','+1'],
    'damage_type':'slashing',
    'damage_dice':'1d8',
    'damage_dice_versatile':'1d10',
    'weight (lb)':3,
    'cost (gp)':30*60,
    'cost (grams_of_gold)':30*60,
    }

metadict_items['Battleaxe +1'] = {
    'weapon':True,
    'ammo_type':blade_poisons,
    'weapon_type':['martial','close','versatile','magic','+1'],
    'damage_type':'slashing',
    'damage_dice':'1d8',
    'damage_dice_versatile':'1d10',
    'weight (lb)':4,
    'cost (gp)':30*60,
    'cost (grams_of_gold)':30*60,
    }

metadict_items['Flait +1'] = {
    'weapon':True,
    'ammo_type':blade_poisons,
    'weapon_type':['martial','close','magic','+1'],
    'damage_type':'bludgeoning',
    'damage_dice':'1d8',
    'weight (lb)':2,
    'cost (gp)':30*60,
    'cost (grams_of_gold)':30*60,
    }

metadict_items['Greatsword +1'] = {
    'weapon':True,
    #'shield_breaker':True,
    'ammo_type':blade_poisons,
    'weapon_type':['martial','close','two_handed','heavy','magic','+1'],
    'damage_type':'slashing',
    'damage_dice':'2d6',
    'weight (lb)':6,
    'cost (gp)':30*60,
    'cost (grams_of_gold)':30*60,
    }

metadict_items['Glaive +1'] = {
    'weapon':True,
    #'shield_breaker':True,
    'ammo_type':blade_poisons,
    'weapon_type':['martial','close','reach','two_handed','heavy','magic','+1'],
    'damage_type':'slashing',
    'damage_dice':'1d10',
    'weight (lb)':6,
    'cost (gp)':30*60,
    'cost (grams_of_gold)':30*60,
    }

metadict_items['Long Spear +1'] = {
    'weapon':True,
    'ammo_type':blade_poisons,
    'weapon_type':['martial','close','reach','versatile','heavy','magic','+1'],
    'damage_type':'piercing',
    'damage_dice':'1d6',
    'damage_dice_versatile':'1d8',
    'weight (lb)':6,
    'cost (gp)':30*60,
    'cost (grams_of_gold)':30*60,
    }

metadict_items['Lance +1'] = {
    'weapon':True,
    'ammo_type':blade_poisons,
    'one_hand_mounted':True,
    'disadvantage_close':True,
    'weapon_type':['martial','close','reach','heavy','magic','+1'],
    'damage_type':'piercing',
    'damage_dice':'1d12',
    'weight (lb)':6,
    'cost (gp)':10,
    'cost (grams_of_gold)':5,
    }

#----
# Ranged Weapons +1

metadict_items['Shortbow +1'] = {
    # Стрелы не имеют тега "magic". Они не волшебные.
    'weapon':True,
    'ammo_type':longbow_arrows,
    'weapon_type':['simple','ranged','volley','two_handed','+1'],
    'damage_type':'piercing',
    'damage_dice':'1d6',
    'shoot_range':80,
    'shoot_range_max':320,
    'weight (lb)':2,
    'cost (gp)':30*60,
    'cost (grams_of_gold)':30*60,
    }

metadict_items['Longbow +1'] = {
    # Стрелы не имеют тега "magic". Они не волшебные.
    'weapon':True,
    'ammo_type':longbow_arrows,
    'weapon_type':['martial','ranged','volley','two_handed','+1'],
    'damage_type':'piercing',
    #'damage_dice':'1d8',
    'damage_dice':'1d6',
    'shoot_range':150,
    'shoot_range_max':600,
    'weight (lb)':2,
    'cost (gp)':30*60,
    'cost (grams_of_gold)':30*60,
    }

#----
# Artillery, осадное вооружение

metadict_items['Trebuchet, Heavy'] = {
    'weapon':True,
    'ammo_type':catapult_shells,
    'weapon_type':['martial','volley'],
    'shoot_range':150,
    'shoot_range_max':1200,
    'weight (lb)':12000,
    'cost (gp)':8 * 60,
    'cost (grams_of_gold)':8 * 60,
    }

metadict_items['Trebuchet, Light'] = {
    # Лёгкий требушет, мангонон
    'weapon':True,
    'ammo_type':catapult_shells,
    'weapon_type':['martial','volley'],
    'shoot_range':150,
    'shoot_range_max':600,
    'weight (lb)':1200,
    'cost (gp)':1 * 2,
    'cost (grams_of_gold)':1 * 2,
    }

metadict_items['Onager'] = {
    # Онагр, монанкон (греческий)
    # Стреляет только навесом.
    'weapon':True,
    'ammo_type':catapult_shells,
    'weapon_type':['martial','volley'],
    'shoot_range':150,
    'shoot_range_max':600,
    'weight (lb)':4000,
    'cost (gp)':16 * 60,
    'cost (grams_of_gold)':16 * 60,
    }

metadict_items['Ballista, Heavy'] = {
    # Тяжёлая баллиста
    'weapon':True,
    'ammo_type':catapult_shells,
    'weapon_type':['martial','ranged','volley'],
    'shoot_range':300,
    'shoot_range_max':1200,
    'weight (lb)':12000,
    'cost (gp)':40 * 60,
    'cost (grams_of_gold)':40 * 60,
    }

metadict_items['Ballista, Medium'] = {
    # Средняя баллиста
    'weapon':True,
    'ammo_type':catapult_shells,
    'weapon_type':['martial','ranged','volley'],
    'shoot_range':300,
    'shoot_range_max':1200,
    'weight (lb)':1200,
    'cost (gp)':8 * 60,
    'cost (grams_of_gold)':8 * 60,
    }

metadict_items['Ballista, Light'] = {
    # Лёгкая баллиста, Карробаллиста
    'weapon':True,
    'ammo_type':catapult_shells,
    'weapon_type':['martial','ranged','volley'],
    'shoot_range':150,
    'shoot_range_max':600,
    'weight (lb)':400,
    'cost (gp)':4 * 60,
    'cost (grams_of_gold)':4 * 60,
    }

#-------------------------------------------------------------------------
# Боеприпасы (снаряды катапульт), catapult_shells

metadict_items['Boulder (200 lb)'] = {
    'ammo':True,
    'direct_hit':True,
    'savethrow':True,
    'savethrow_all':True,
    'savethrow_ability':'dexterity',
    'weapon_type':['siege'],
    'damage_type':'bludgeoning',
    'damage_dice':'8d10',
    'weight (lb)':200,
    'cost (gp)':10/60,
    'cost (grams_of_gold)':10/60,
    }

metadict_items['Boulder (100 lb)'] = {
    'ammo':True,
    'direct_hit':True,
    'savethrow':True,
    'savethrow_all':True,
    'savethrow_ability':'dexterity',
    'weapon_type':['siege'],
    'damage_type':'bludgeoning',
    'damage_dice':'5d10',
    'weight (lb)':100,
    'cost (gp)':10/60,
    'cost (grams_of_gold)':10/60,
    }

metadict_items['Boulder (50 lb)'] = {
    # Каменное ядро. Талант веса (26 кг)
    # Обработка камня до круглой формы -- 6-8 часов.
    'ammo':True,
    #'direct_hit':True,
    #'savethrow':True,
    #'savethrow_all':True,
    #'savethrow_ability':'dexterity',
    'weapon_type':['siege'],
    'damage_type':'bludgeoning',
    'damage_dice':'3d10',
    'weight (lb)':50,
    'cost (gp)':10/60,
    'cost (grams_of_gold)':10/60,
    }

metadict_items['Boulder (25 lb)'] = {
    'ammo':True,
    #'direct_hit':True,
    #'savethrow':True,
    #'savethrow_all':True,
    #'savethrow_ability':'dexterity',
    'damage_type':'bludgeoning',
    'damage_dice':'2d10',
    'weight (lb)':25,
    'cost (gp)':10/60,
    'cost (grams_of_gold)':10/60,
    }

metadict_items['Boulder (10 lb)'] = {
    'ammo':True,
    #'direct_hit':True,
    #'savethrow':True,
    #'savethrow_all':True,
    #'savethrow_ability':'dexterity',
    'damage_type':'bludgeoning',
    'damage_dice':'1d10',
    'weight (lb)':25,
    'cost (gp)':10/60,
    'cost (grams_of_gold)':10/60,
    }

metadict_items['Sling Bullets (x10)'] = {
    'ammo':True,
    'direct_hit':True,
    'spell_dict':{
            'zone':True,
            'radius':10,
            'attack_mod':0,
            'attack_range':5,
            'damage_mod':0,
            'damage_type':'bludgeoning',
            'damage_dice':'1d4',
            'spell_choice':('volley','Sling Bullet'),
            },
    'damage_type':'bludgeoning',
    'damage_dice':'0d0',
    'weight (lb)':25,
    'cost (gp)':10/60,
    'cost (grams_of_gold)':10/60,
    }

metadict_items['Sling Bullets (x25)'] = {
    'ammo':True,
    'direct_hit':True,
    'spell_dict':{
            'zone':True,
            'radius':15,
            'attack_mod':0,
            'attack_range':5,
            'damage_mod':0,
            'damage_type':'bludgeoning',
            'damage_dice':'1d4',
            'spell_choice':('volley','Sling Bullet'),
            },
    'damage_type':'bludgeoning',
    'damage_dice':'0d0',
    'weight (lb)':25,
    'cost (gp)':10/60,
    'cost (grams_of_gold)':10/60,
    }

metadict_items['Ballista Bolt (25 lb)'] = {
    'ammo':True,
    'damage_type':'piercing',
    'damage_dice':'3d10',
    'weight (lb)':25,
    'cost (gp)':60 / 60,
    'cost (grams_of_gold)':60 / 60,
    }

metadict_items['Ballista Bolt (5 lb)'] = {
    'ammo':True,
    'damage_type':'piercing',
    'damage_dice':'3d6',
    'weight (lb)':5,
    'cost (gp)':30 / 60,
    'cost (grams_of_gold)':30 / 60,
    }

metadict_items['Ballista Bolt (1 lb)'] = {
    'ammo':True,
    'damage_type':'piercing',
    'damage_dice':'2d6',
    'weight (lb)':1,
    'cost (gp)':10 / 60,
    'cost (grams_of_gold)':10 / 60,
    }

metadict_items['Ballista Bolt (0.2 lb)'] = {
    # Снаряд полибола: 0.2 lb (90 м/с, 600 футов)
    'ammo':True,
    'damage_dice':'1d6',
    'damage_type':'piercing',
    'weight (lb)':4/20,
    'cost (gp)':1/20,
    'cost (grams_of_gold)':4 / 60,
    }

metadict_items['Alchemist\'s Fire (100/200 lb)'] = {
    # Для тяжёлого требушета
    'ammo':True,
    'direct_hit':True,
    'savethrow':True,
    'savethrow_ability':'dexterity',
    'damage_dice':'8d6',
    'damage_type':'fire',
    'spell_dict':{
            'zone':True,
            'radius':20,
            'direct_hit':True,
            'savethrow':True,
            'savethrow_ability':'dexterity',
            'attacks_number':1,
            'attack_range':600,
            'damage_type':'fire',
            'damage_dice':'2d6',
            'spell_save_DC':15,
            'spell_choice':('Explosion','Alchemist\'s Fire'),
            },
    'weight (lb)':200,
    'cost (gp)':60,
    'cost (grams_of_gold)':60,
    }

metadict_items['Alchemist\'s Fire (25/50 lb)'] = {
    'ammo':True,
    'direct_hit':True,
    'savethrow':True,
    'savethrow_ability':'dexterity',
    'damage_dice':'4d6',
    'damage_type':'fire',
    'spell_dict':{
            'zone':True,
            'zone_shape':'2x2',
            'direct_hit':True,
            'savethrow':True,
            'savethrow_ability':'dexterity',
            'attacks_number':1,
            'attack_range':600,
            'damage_type':'fire',
            'damage_dice':'2d6',
            'spell_save_DC':15,
            'spell_choice':('Explosion','Alchemist\'s Fire'),
            },
    'weight (lb)':50,
    'cost (gp)':15,
    'cost (grams_of_gold)':15,
    }

metadict_items['Alchemist\'s Fire (10/25 lb)'] = {
    'ammo':True,
    'direct_hit':True,
    'savethrow':True,
    'savethrow_ability':'dexterity',
    'damage_dice':'2d6',
    'damage_type':'fire',
    'spell_dict':{
            'zone':True,
            'zone_shape':'2x2',
            'direct_hit':True,
            'savethrow':True,
            'savethrow_ability':'dexterity',
            'attacks_number':1,
            'attack_range':600,
            'damage_type':'fire',
            'damage_dice':'2d6',
            'spell_save_DC':15,
            'spell_choice':('Explosion','Alchemist\'s Fire'),
            },
    'weight (lb)':50,
    'cost (gp)':15,
    'cost (grams_of_gold)':15,
    }

#-------------------------------------------------------------------------
# Боеприпасы (снаряды пращ), sling_bullets

metadict_items['Sling Bullet'] = {
    # Глиняные шарики, одинаковые по форме и размеру.
    # Масса хорошего снаряда для пращи -- 300-400 грамм.
    'ammo':True,
    'damage_dice':'1d4',
    'damage_type':'bludgeoning',
    'weight (lb)':0.9,
    'cost (sp)':1 / 20,
    'cost (grams_of_gold)':1 / 60,
    }

metadict_items['Lead Bullet'] = {
    # Свинцовые шарики -- 400 грамм.
    # Свинцовые/железные шарики, но они дорогие (чугун 4 / 60 gp).
    'ammo':True,
    'damage_dice':'1d6',
    'damage_type':'bludgeoning',
    'weight (lb)':0.9,
    'cost (grams_of_gold)':4 / 60,
    }

metadict_items['Holy Bullet'] = {
    # Керамический снаряд с водой.
    'ammo':True,
    'damage_dice':'1d4',
    'damage_type':'bludgeoning',
    'spell_dict':{
            'effect':'holy_water',
            'direct_hit':True,
            'savethrow':True,
            'savethrow_all':True,
            'savethrow_ability':'charisma',
            'damage_dice':'1d6',
            'damage_type':'radiant',
            'spell_save_DC':10,
            'spell_choice':('Holy Bullet','Святая вода'),
            },
    'weight (lb)':0.9,
    'cost (grams_of_gold)':40 / 60,
    }

metadict_items['Sling Bullet +1'] = {
    'ammo':True,
    'damage_dice':'1d6',
    'damage_type':'bludgeoning',
    'weapon_type':['magic','+1'],
    'weight (lb)':0.9,
    'cost (grams_of_gold)':4 / 60,
    }

#-------------------------------------------------------------------------
# Боеприпасы (стрелы), longbow_arrows

metadict_items['Arrow'] = {
    # Нормальная стрела длинного/композитного лука весит 70 грамм.
    # Следовательно, 20 стрел -- 3 фунта, а не 1 фунт, как в правилах D&D.
    # Изготовление стрел -- 0.5-2 человеко-часа (включая железный наконечник, работу кузнеца)
    # Другие данные -- 1000 стрел за два месяца (17 стрел/сутки)
    'ammo':True,
    'damage_dice':'1d6',
    'damage_type':'piercing',
    'weight (lb)':3/20,
    'cost (gp)':1/20,
    'cost (grams_of_gold)':4 / 60,
    }

metadict_items['Arrow +1'] = {
    'ammo':True,
    'damage_dice':'1d6',
    'damage_type':'piercing',
    'weapon_type':['magic','+1'],
    'weight (lb)':3/20,
    'cost (gp)':1/20,
    'cost (grams_of_gold)':60 * 2,
    }

metadict_items['Slashing Arrow'] = {
    # Дороже и тяжелее из-за широкого наконечника.
    'ammo':True,
    'damage_dice':'1d6',
    'damage_type':'slashing',
    'weight (lb)':4/20,
    'cost (gp)':1/20,
    'cost (grams_of_gold)':6 / 60,
    }

metadict_items['Hunting Arrow'] = {
    # Охотничья стрела с оперением, наконечник из заострённого камня.
    'ammo':True,
    'damage_dice':'1d4',
    'damage_type':'piercing',
    'weight (lb)':2/20,
    'cost (gp)':1/20,
    'cost (grams_of_gold)':1 / 60,
    }

metadict_items['Fire Arrow'] = {
    # Алхимический огонь
    # Сложно сделать прицельный выстрел.
    'ammo':True,
    'shoot_range':60,
    'shoot_range_max':600,
    'damage_dice':'1d4',
    'damage_type':'piercing',
    'spell_dict':{
            'safe':True,
            'direct_hit':True,
            'savethrow':True,
            'savethrow_all':True,
            'savethrow_ability':'dexterity',
            'damage_type':'fire',
            'damage_dice':'1d4',
            'spell_save_DC':10,
            'spell_choice':('Fire Arrow','Alchemist\'s Fire'),
            },
    'weight (lb)':4/20,
    'cost (gp)':1/20,
    'cost (grams_of_gold)':8 / 60,
    }

metadict_items['Poison Arrow'] = {
    'ammo':True,
    'damage_dice':'1d6',
    'damage_type':'piercing',
    'spell_dict':{
            'safe':True,
            'effect':'poison',
            'effect_timer':10,
            'direct_hit':True,
            'savethrow':True,
            'savethrow_all':True,
            'savethrow_ability':'constitution',
            'damage_type':'poison',
            'damage_dice':'1d4',
            'spell_save_DC':10,
            'spell_choice':('Poison Arrow','Яд морского Йобы'),
            },
    'weight (lb)':4/20,
    'cost (gp)':1/20,
    'cost (grams_of_gold)':40 / 60,
    }

#-------------------------------------------------------------------------
# Боеприпасы (болты)

metadict_items['Crossbow Bolt'] = {
    'ammo':True,
    'damage_dice':'1d6',
    'damage_type':'piercing',
    'weight (lb)':3/20,
    'cost (gp)':1/20,
    'cost (grams_of_gold)':4 / 60,
    }

metadict_items['Crossbow Bolt +1'] = {
    'ammo':True,
    'damage_dice':'1d6',
    'damage_type':'piercing',
    'weapon_type':['magic','+1'],
    'weight (lb)':3/20,
    'cost (gp)':1/20,
    'cost (grams_of_gold)':4 / 60,
    }

metadict_items['Slashing Bolt'] = {
    # Дороже и тяжелее из-за широкого наконечника.
    'ammo':True,
    'damage_dice':'1d6',
    'damage_type':'slashing',
    'weight (lb)':4/20,
    'cost (gp)':1/20,
    'cost (grams_of_gold)':6 / 60,
    }

metadict_items['Hunting Bolt'] = {
    # Охотничья стрела с оперением, наконечник из заострённого камня.
    'ammo':True,
    'damage_dice':'1d4',
    'damage_type':'piercing',
    'weight (lb)':2/20,
    'cost (gp)':1/20,
    'cost (grams_of_gold)':1 / 60,
    }

#-------------------------------------------------------------------------
# Боеприпасы (оружейные яды)

metadict_items['Poison Blade'] = {
    'ammo':True,
    'spell_dict':{
            'safe':True,
            'effect':'poison',
            'effect_timer':10,
            'direct_hit':True,
            'savethrow':True,
            'savethrow_all':True,
            'savethrow_ability':'constitution',
            'damage_dice':'1d4',
            'damage_type':'poison',
            'spell_save_DC':10,
            'spell_choice':('Poison Blade','Яд морского Йобы'),
            },
    'weight (lb)':1/20,
    'cost (gp)':1/20,
    'cost (grams_of_gold)':40 / 60,
    }

metadict_items['Sleep Blade'] = {
    'ammo':True,
    'spell_dict':{
            'safe':True,
            'effect':'sleep',
            'effect_timer':10,
            'direct_hit':True,
            'savethrow':True,
            'savethrow_ability':'constitution',
            'spell_save_DC':10,
            'spell_choice':('Sleep Blade','Яд лесного Йобы'),
            },
    'weight (lb)':1/20,
    'cost (gp)':1/20,
    'cost (grams_of_gold)':1.2,
    }

metadict_items['Holy Blade'] = {
    'ammo':True,
    'spell_dict':{
            'safe':True,
            'effect':'holy_water',
            'direct_hit':True,
            'savethrow':True,
            'savethrow_all':True,
            'savethrow_ability':'charisma',
            'damage_dice':'1d6',
            'damage_type':'radiant',
            'spell_save_DC':10,
            'spell_choice':('Holy Blade','Святая вода'),
            },
    'weight (lb)':1/20,
    'cost (gp)':1/20,
    'cost (grams_of_gold)':40 / 60,
    }
