#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dices import *

#-------------------------------------------------------------------------
# Отряды

metadict_squads = {}

#----
# Тестовые

metadict_squads['характеристики правителей'] = {
    # Влом делать отдельно, так рольнём:
        # 1 герой 5+ lvl на 16 героев 1 lvl
        # 1 герой 7+ lvl на 62 героев 1 lvl
        # 1 герой 9+ lvl на 250 героев 1 lvl
    # Дер-Кето
    # Cleric 1 lvl (city maatcarian-acolyte) sum:104 STR:16 DEX:18 CON:17 INT:17 WIS:19 CHA:17
    #'Cleric 1 lvl (city maatcarian-acolyte)':250,
    # Тинв:
    # Wizard 2 lvl (city cat-weaver) sum:101 STR:14 DEX:19 CON:17 INT:19 WIS:16 CHA:16
    #'Wizard 2 lvl (city cat-weaver)':250,
    # Ри:
    # Rogue 1 lvl (city cat-nyamo) sum:97 STR:12 DEX:20 CON:16 INT:17 WIS:15 CHA:17
    #'Rogue 1 lvl (city cat-nyamo)':250,
    # Акхен:
    # Druid 1 lvl (otherworld terian-forester) sum:101 STR:12 DEX:19 CON:18 INT:18 WIS:19 CHA:15
    #'Druid 1 lvl (otherworld terian-forester)':250,
    # Кумар:
    # Monk 1 lvl (city windsong-apprentice) sum:104 STR:17 DEX:19 CON:17 INT:16 WIS:18 CHA:17
    #'Monk 1 lvl (city windsong-apprentice)':250,
    # Карагос:
    # Barbarian 1 lvl (thracian slayer-dogface) sum:108 STR:19 DEX:18 CON:19 INT:18 WIS:16 CHA:18
    #'Barbarian 1 lvl (thracian slayer-dogface)':250,
    # Накиями:
    # Ranger 1 lvl (otherworld wanderer-scout) sum:101 STR:15 DEX:18 CON:15 INT:18 WIS:17 CHA:18
    #'Ranger 1 lvl (otherworld wanderer-scout)':250,
    # Крассиус:
    # Bard 1 lvl (otherworld singer-follower) sum:95 STR:15 DEX:18 CON:10 INT:16 WIS:17 CHA:19
    #'Bard 1 lvl (otherworld singer-follower)':250,
    # Руна:
    # Paladin 1 lvl (city sentry-sefet) sum:100 STR:18 DEX:16 CON:17 INT:17 WIS:15 CHA:17
    #'Paladin 1 lvl (city sentry-sefet)':250,
    # Чара:
    # Warlock 1 lvl (otherworld seeker-follower) sum:97 STR:15 DEX:18 CON:16 INT:15 WIS:15 CHA:18
    # Ашера:
    # Empyrean (CR 23) sum:151 STR:30 DEX:21 CON:30 INT:21 WIS:22 CHA:27
    # Менон:
    # Wizard 1 lvl (otherworld mage-disciple) sum:100 STR:16 DEX:17 CON:17 INT:19 WIS:17 CHA:14
    #'Wizard 1 lvl (otherworld mage-disciple)':1000,
    # Кирос:
    # Fighter 1 lvl (legionary sentinel-battler) sum:103 STR:19 DEX:17 CON:18 INT:16 WIS:16 CHA:17
    #'Fighter 1 lvl (legionary sentinel-battler)':2000,
    }

metadict_squads['характеристики героев'] = {
    # Влом делать отдельно, так рольнём:
        # 1 герой 5+ lvl на 16 героев 1 lvl
        # 1 герой 7+ lvl на 62 героев 1 lvl
        # 1 герой 9+ lvl на 250 героев 1 lvl
    # Тетра Курио:
    # Bard 1 lvl (otherworld singer-follower) sum:85 STR:10 DEX:16 CON:15 INT:14 WIS:14 CHA:16
    #'Bard 1 lvl (otherworld singer-follower)':32,
    }

#----
# Тестовые (осадное вооружение)

metadict_squads['10 onagers (siege)'] = {
    # Онагры, катапульты
    'Warrior 2 lvl (siege engineer-apprentice) (onager-siege)':10,
    'Warrior 4 lvl (siege engineer-master)':1,
    }

metadict_squads['10 onagers (fire)'] = {
    'Warrior 2 lvl (siege engineer-apprentice) (onager-fire)':10,
    'Warrior 4 lvl (siege engineer-master)':1,
    }

metadict_squads['Company-regular (осадные инженеры)'] = {
    # С двуручными кирками, Greataxe
    'Warrior 1 lvl (legionary infantry-siege)':80 + dice_throw('1d12'),
    'Warrior 2 lvl (legionary infantry-siege-corporal)':10,
    'Warrior 3 lvl (legionary infantry-siege-sergeant)':3,
    }

#----
# Тестовые (ложные цели)

metadict_squads['Company-dummy (куклы)'] = {
    # Просто чучела на кораблях.
    'Dummy (AC 17)':100,
    }

#----
# Тестовые (герои из Monsters_Manual)

metadict_squads['Single-hero (druid)'] = {
    'Druid (CR 2)':1,
    }

metadict_squads['Single-hero (mage)'] = {
    'Mage (CR 6)':1,
    }

metadict_squads['Single-hero (archmage)'] = {
    'Archmage (CR 12)':1,
    }

metadict_squads['Single-hero (dragon)'] = {
    # Дракон
    'Red Dragon, Young (CR 10)':1,
    }

metadict_squads['Single-hero (storm giant)'] = {
    'Storm Giant (CR 13)':1,
    }

metadict_squads['Single-hero (empyrean)'] = {
    'Empyrean (CR 23)':1,
    }

#----
# Тестовые (отряды из Monsters_Manual)

metadict_squads['Squad-animal-herd (horseclaws)'] = {
    'Horseclaw':dice_throw('2d6'),
    }

metadict_squads['Squad-elite (veterans)'] = {
    'Veteran (CR 3)':10,
    }

metadict_squads['Squad-elite (wights)'] = {
    'Wight (CR 3)':10,
    }

metadict_squads['Squad-elite (hill giants)'] = {
    # Холмовые великаны
    'Hill Giant (CR 5)':6,
    }

metadict_squads['Squad-elite (stone giants)'] = {
    # Каменные великаны
    'Stone Giant (CR 7)':6,
    }

metadict_squads['Squad-elite (frost giants)'] = {
    # Ледяные великаны
    'Frost Giant (CR 8)':6,
    }

metadict_squads['Squad-elite (fire giants)'] = {
    # Огненные великаны
    'Fire Giant (CR 9)':6,
    }

metadict_squads['Squad-elite (storm giants)'] = {
    # Штормовые великаны
    'Storm Giant (CR 13)':6,
    }

#----
# Тестовые (отряды из Monsters_Manual)

metadict_squads['Company-regular (sentinels)'] = {
    # Для тестов сравнительной силы отрядов.
    # Считаются бесстрашными, fearless_AI
    'Sentinel (CR 1/8)':100,
    }

metadict_squads['Company-regular (tribe warriors)'] = {
    'Tribe Warrior (CR 1/8)':100,
    }

metadict_squads['Company-militia (zombies)'] = {
    'Zombie (CR 1/4)':100,
    }

metadict_squads['Company-militia (bandits)'] = {
    'Bandit (CR 1/8)':100,
    }

metadict_squads['Company-veteran (thugs)'] = {
    'Thug (CR 1/2)':100,
    }

metadict_squads['Company-militia (goblins)'] = {
    'Goblin (CR 1/4)':80 + dice_throw('3d12'),
    'Goblin Boss (CR 1)':3,
    }

metadict_squads['Company-veteran (hobgoblins)'] = {
    'Hobgoblin (CR 1/2)':80 + dice_throw('3d12'),
    'Hobgoblin-captain (CR 3)':1,
    }

metadict_squads['Company-veteran (orks)'] = {
    'Ork (CR 1/2)':80 + dice_throw('3d12'),
    'Orog (CR 2)':3,
    'Ork war chief (CR 4)':1,
    }

metadict_squads['Company-elite (bugbears)'] = {
    'Bugbear (CR 1)':100,
    }

#----
# Тестовые (партии)

metadict_squads['Band-hero (party 1 lvl)'] = {
    # TODO: они должны быть бесстрашными.
    # Тестовая партия для оценки CR:
    # Воин, клирик, вор и маг:
        # Боец -- лучник с боевым стилем
        # Клерик -- "Воодушевляющий лидер" и командир, колдует "Bless"
        # Рога -- с ножом и арбалетом
        # Волшебник -- с "Волшебной стрелой"
    'Cleric 1 lvl (war cleric)':1,
    'Rogue 1 lvl (city cat-nyamo)':1,
    'Wizard 1 lvl (otherworld mage-disciple)':1,
    'Barbarian 1 lvl (thracian slayer-dogface)':1,
    #'Fighter 1 lvl (ArbitraryNickname) (снайпер)':1,
    }

#----
# Тестовые (отряды)

metadict_squads['Company-test (standard) (shortbow)'] = {
    'Warrior 1 lvl (standard) (Shortbow)':100,
    }

metadict_squads['Company-test (standard) (shortbow) (archery)'] = {
    'Warrior 1 lvl (standard) (Shortbow) (archery)':100,
    }

metadict_squads['Company-test (standard) (greataxes)'] = {
    # Тесты типовых отрядов для Vened'а.
    'Warrior 1 lvl (standard) (Greataxe)':100,
    }

metadict_squads['Company-test (standard) (disadvantage) (greataxes)'] = {
    'Warrior 1 lvl (standard) (disadvantage) (Greataxe)':100,
    }

metadict_squads['Company-test (standard) (bless + disadvantage) (greataxes)'] = {
    'Warrior 1 lvl (standard) (bless + disadvantage) (Greataxe)':100,
    }

metadict_squads['Company-test (standard) (battleaxes)'] = {
    'Warrior 1 lvl (standard) (Battleaxe + Shield)':100,
    }

metadict_squads['Company-test (standard) (Feat_Heavy_Armor_Master)'] = {
    'Warrior 4 lvl (standard) (Feat_Heavy_Armor_Master)':100,
    }

metadict_squads['Company-test (standard) (Feat_Polearm_Master)'] = {
    'Warrior 4 lvl (standard) (Feat_Polearm_Master)':100,
    }

metadict_squads['Company-test (standard) (Feat_Great_Weapon_Master)'] = {
    'Warrior 4 lvl (standard) (Feat_Great_Weapon_Master)':100,
    }

metadict_squads['Company-test (standard) (Feat_Sentinel)'] = {
    'Warrior 4 lvl (standard) (Feat_Sentinel)':100,
    }

metadict_squads['Company-test (standard) (Feat_Martial_Adept)'] = {
    'Warrior 4 lvl (standard) (Feat_Martial_Adept)':100,
    }

metadict_squads['Company-test (standard) (Feat_Magic_Initiate)'] = {
    'Warrior 4 lvl (standard) (Feat_Magic_Initiate)':100,
    }

#----
# Тестовые отряды

metadict_squads['Band-test (standard) (Feat_Heavy_Armor_Master)'] = {
    'Warrior 4 lvl (standard) (Feat_Heavy_Armor_Master)':10,
    }

metadict_squads['Band-test (standard) (Feat_Polearm_Master)'] = {
    'Warrior 4 lvl (standard) (Feat_Polearm_Master)':10,
    }

metadict_squads['Band-test (standard) (Feat_Great_Weapon_Master)'] = {
    'Warrior 4 lvl (standard) (Feat_Great_Weapon_Master)':10,
    }

metadict_squads['Band-test (standard) (Feat_Sentinel)'] = {
    'Warrior 4 lvl (standard) (Feat_Sentinel)':10,
    }

metadict_squads['Band-test (standard) (Feat_Martial_Adept)'] = {
    'Warrior 4 lvl (standard) (Feat_Martial_Adept)':10,
    }

metadict_squads['Band-test (standard) (Feat_Magic_Initiate)'] = {
    'Warrior 4 lvl (standard) (Feat_Magic_Initiate)':10,
    }

metadict_squads['Band-test (standard) (Feat_Defensive_Duelist)'] = {
    'Warrior 4 lvl (standard) (Feat_Defensive_Duelist)':10,
    }

metadict_squads['Band-test (standard) (Feat_Mounted_Combatant)'] = {
    'Warrior 4 lvl (standard) (Feat_Mounted_Combatant)':10,
    }

metadict_squads['Band-test (standard) (Feat_Tough)'] = {
    'Warrior 4 lvl (standard) (Feat_Tough)':10,
    }

metadict_squads['Band-test (standard) (Feat_Durable)'] = {
    'Warrior 4 lvl (standard) (Feat_Durable)':10,
    }

metadict_squads['Band-test (standard) (Feat_Dual_Wielder)'] = {
    'Warrior 4 lvl (standard) (Feat_Dual_Wielder)':10,
    }

metadict_squads['Band-test (standard) (Feat_Shield_Master)'] = {
    'Warrior 4 lvl (standard) (Feat_Shield_Master)':10,
    }

metadict_squads['Band-test (standard) (Feat_Firearms_Expert)'] = {
    'Warrior 4 lvl (standard) (Feat_Firearms_Expert)':10,
    }

#----
# Погода, глобальные заклинания

metadict_squads['weather (lightning-storm)'] = {
    # Морской шторм
    'Weather (waves)':4,
    'Weather (lightning)':4,
    #'Weather (storm-god)':1,
    }

metadict_squads['weather (молнии Зевса)'] = {
    'Weather (lightning)':4,
    #'Weather (storm-god)':1,
    }

metadict_squads['weather (шторм Посейдона)'] = {
    'Weather (waves)':4,
    #'Weather (storm-god)':1,
    }

#----
# Ловушки

metadict_squads['traps (lightning)'] = {
    # TODO: переделать, старый код.
    # Защитные руны
    'Trap (Glyph of Warding) (Lightning)':1,
    #'Trap (commander)':1,
    }

metadict_squads['traps (fire) (octopus)'] = {
    # Осьминожки со 100 lb. бочками алхимического огня.
    # Восемь бочек алхимичесого огня на корабль.
    'Trap (Alchemist\'s Fire)':8,
    #'Trap (commander)':1,
    }

metadict_squads['traps (fire) (bombarding)'] = {
    # 12 бочей на гигантских орлах.
    # 1200 lb. алхимического огня.
    'Trap (Alchemist\'s Fire)':12,
    #'Trap (commander)':1,
    }

#----
# Укрепления, фортификации, строения

metadict_squads['каменный мост'] = {
    # 50-футовый участок, ширина 20 футов (десять 10x10-футовых "пролётов", четыре опоры)
        # Заклинание "Призыв Молнии" (Call_Lightning) ломает опору за 10 минут.
        # Бойцы с секирами на 1d12 урона справляются за 60 минут.
    'Bridge-support (stone)':4,
    'Bridge (stone)':10,
    }

metadict_squads['частокол (120 hp)'] = {
    # 1 фут толщины. Один ряд стволов.
    'Palisade (wood) (120 hp)':5,
    }

metadict_squads['частокол (600 hp)'] = {
    # 5 футов толщины. 5 рядов стволов.
    'Palisade (wood) (600 hp)':5,
    }

metadict_squads['крепостная стена (Arcane_Lock)'] = {
    'Wall (stone) (1200 hp + Arcane_Lock)':5,
    }

metadict_squads['крепостная стена (1200 hp)'] = {
    # 50-футовый участок, пять 10x10 футовых участков.
        # Земляные элементали ломают сегмент за 10 минут.
        # Онагры делают 10-футовый прлом за 60 минут.
    'Wall (stone) (1200 hp)':5,
    }

#----
# Корабли:

metadict_squads['Ship (trage)'] = {
    'Ship trage (deck)':24,
    'Ship trage (board)':24,
    'Ship trage (command)':2,
    }

metadict_squads['Ship (trireme)'] = {
    # Триера. 50 тонн водоизмещения (пустая), 50 объектов 10x10 футов.
    'Ship trireme (deck)':24,
    'Ship trireme (board)':24,
    'Ship trireme (command)':2,
    }

metadict_squads['Ship (pentere)'] = {
    # Пентера. 150 тонн водоизмещения, 50 объектов 10x10 футов.
    'Ship pentere (deck)':24,
    'Ship pentere (board)':24,
    'Ship pentere (command)':2,
    }

#----
# Чудовища, Homebrew:

metadict_squads['Company-regular (дактили горы Ушур) (враг)'] = {
    'Дактиль-кусатель (CR 1/2)':50,
    'Дактиль-хвататель (CR 1/2)':40,
    'Дактиль-ломатель (CR 1)':9,
    'Дактиль-сжиратель (CR 2)':3,
    }

metadict_squads['Company-hero (гневнорожки Сефо) (друг)'] = {
    # Союзные отряды (армия Козы):
    'Warlock 2 lvl (друг) (гневнорожка Козы)':80,
    'Warlock 3 lvl (друг) (главнорожка Козы)':10,
    'Warlock 3 lvl (друг) (Сефо Форонейская)':1,
    }

#----
# Призванные существа:

metadict_squads['Squad-summon (оживлённые вещи)'] = {
    # Заклинание 5 круга "Оживление вещей" (Animated_Objects)
    # Homebrew: Можно анимировать 36 предметов с CR 1 на 10 минут.
    'Animated swords (CR 1)':36,
    }

metadict_squads['Squad-summon (меч Морденкайнена)'] = {
    'Mordenkainen Sword (CR 10)':1,
    }

metadict_squads['Squad-summon (громовые птицы)'] = {
    'Громовая птица (Thunderbird) (CR 1)':12,
    }

metadict_squads['Squad-summon (воздушные элементали)'] = {
    'Air Elemental (CR 5)':6,
    }

metadict_squads['Squad-summon (земляные элементали)'] = {
    'Earth Elemental (CR 5)':6,
    }

metadict_squads['Single-summon (земляной элементаль)'] = {
    'Earth Elemental (CR 5)':1,
    }

metadict_squads['Single-summon (воздушный элементаль)'] = {
    'Air Elemental (CR 5)':1,
    }

metadict_squads['Squad-summon (гигантские осьминоги)'] = {
    'Giant Octopus (CR 1)':12,
    }

metadict_squads['Company-militia (мастиффы)'] = {
    # Призванные собаки:
    'Mastiff, dog (CR 1/8)':96,
    }

#-------------------------------------------------------------------------
# Армии и герои

#----
# Свита Кироса:

metadict_squads['Squad-hero (бойцы Кироса) (нейтрал)'] = {
    'Fighter 4 lvl (нейтрал) (боец Кироса)':16,
    'Fighter 13 lvl (нейтрал) (Кирос «Симарх»)':1,
    }

metadict_squads['Single-hero (боец Кироса) (нейтрал)'] = {
    'Fighter 4 lvl (нейтрал) (боец Кироса)':1,
    }

metadict_squads['Single-hero (лично Кирос) (нейтрал)'] = {
    'Fighter 13 lvl (нейтрал) (Кирос «Симарх»)':1,
    }

#----
# Армия Кироса:

#----
# Свита Менона:

metadict_squads['Squad-hero (волшебники Менона) (нейтрал)'] = {
    'Wizard 4 lvl (нейтрал) (волшебник Менона)':14,
    'Wizard 12 lvl (нейтрал) (Менон Теварин)':1,
    }

metadict_squads['Band-hero (волшебники Менона) (нейтрал)'] = {
    'Wizard 4 lvl (нейтрал) (волшебник Менона)':2,
    }

metadict_squads['Single-hero (волшебник Менона) (нейтрал)'] = {
    'Wizard 4 lvl (нейтрал) (волшебник Менона)':1,
    }

metadict_squads['Single-hero (лично Менон) (нейтрал)'] = {
    'Wizard 12 lvl (нейтрал) (Менон Теварин)':1,
    }

metadict_squads['Single-hero (симулякр Менона) (нейтрал)'] = {
    'Wizard 12 lvl (нейтрал) (симулякр Менона)':1,
    }

#----
# Армия Менона:

metadict_squads['Squad-hero (бронзовые гоплиты Менона) (нейтрал)'] = {
    'Warrior 4 lvl (нейтрал) (бронзовый гоплит Менона)':15,
    'Warrior 5 lvl (нейтрал) (бронзовый гоплит-капитан Менона)':5,
    }

metadict_squads['Company-hero (бронзовые гоплиты Менона) (нейтрал)'] = {
    # Всего у Менона 110 бронзовых гоплитов:
    'Warrior 4 lvl (нейтрал) (бронзовый гоплит Менона)':67,
    'Warrior 5 lvl (нейтрал) (бронзовый гоплит-капитан Менона)':25,
    }

metadict_squads['Squad-hero (зомби и гоплиты Менона) (нейтрал)'] = {
    'Warrior 4 lvl (нейтрал) (бронзовый гоплит Менона)':10,
    'Warrior 5 lvl (нейтрал) (бронзовый гоплит-капитан Менона)':4,
    #'Zombie (CR 1/4)':80 + dice_throw('1d12'),
    'Zombie (Danse_Macabre) (CR 1/2)':60,
    }

metadict_squads['Squad-hero (60 зомби Менона) (нейтрал)'] = {
    # Зомби под Danse_Macabre с +5 атаки и +9 урона.
    'Zombie (Danse_Macabre) (CR 1/2)':60,
    'Warrior 4 lvl (нейтрал) (бронзовый гоплит Менона)':3,
    'Warrior 5 lvl (нейтрал) (бронзовый гоплит-капитан Менона)':1,
    }

metadict_squads['Squad-hero (5 зомби Danse_Macabre) (нейтрал)'] = {
    # Зомби под Danse_Macabre с +5 атаки и +9 урона (+5 заклинание +4 бонус мастерства некроманта)
    # Также они получают +9 hp за счёт способности "Неживые рабы"
    'Zombie (Danse_Macabre) (CR 1/2)':5,
    }

metadict_squads['Squad-hero (упыри Менона) (нейтрал)'] = {
    # TODO: лучше бы смешать их с зомбями.
    'Ghoul (CR 1)':80 + dice_throw('1d12'),
    'Ghast (CR 2)':8,
    }

#----
# Свита Карагоса:

metadict_squads['Single-hero (лично Карагос) (нейтрал)'] = {
    # Он потерял всю свою свиту.
    'Barbarian 9 lvl (нейтрал) (Карагос «Мудрый»)':1,
    }

#----
# Армия Карагоса:

metadict_squads['Company-regular (пираты Карагоса) (нейтрал)'] = {
    'Warrior 1 lvl (нейтрал) (пират Карагоса)':70 + dice_throw('1d12'),
    'Warrior 2 lvl (нейтрал) (ветеран Карагоса)':20,
    'Warrior 3 lvl (нейтрал) (сержант Карагоса)':6,
    'Warrior 4 lvl (нейтрал) (лейтенант Карагоса)':2,
    'Warrior 5 lvl (нейтрал) (капитан Карагоса)':1,
    }

metadict_squads['Company-veteran (ветераны Карагоса) (нейтрал)'] = {
    # Опытный отряд с двумя капитанами
    'Warrior 2 lvl (нейтрал) (ветеран Карагоса)':85 + dice_throw('1d12'),
    'Warrior 3 lvl (нейтрал) (сержант Карагоса)':6,
    'Warrior 5 lvl (нейтрал) (капитан Карагоса)':2,
    'Warrior 4 lvl (нейтрал) (лейтенант Карагоса)':2,
    }

#----
# Свита Акхена Ваджета:

metadict_squads['Squad-hero (варвары Радаманта) (враг)'] = {
    'Barbarian 2 lvl (враг) (варвар Радаманта)':9,
    'Barbarian 5 lvl (враг) (Радамант «Бдительный»)':1,
    }

#----
# Армия Акхена Ваджета:

metadict_squads['Company-regular (легионеры Акхена) (враг)'] = {
    'Warrior 1 lvl (враг) (легионер Акхена)':80 + dice_throw('1d12'),
    'Warrior 2 lvl (враг) (ветеран Акхена)':10,
    'Warrior 3 lvl (враг) (сержант Акхена)':3,
    'Warrior 5 lvl (враг) (капитан Акхена)':1,
    'Warrior 4 lvl (враг) (лейтенант Акхена)':1,
    }

#----
# Свита Чары:

metadict_squads['Squad-hero (колдуны Чары) (враг)'] = {
    'Warlock 3 lvl (враг) (колдун Чары)':16,
    'Warlock 11 lvl (враг) (Чара Атенак)':1,
    }

metadict_squads['Squad-hero (колдун Чары) (враг)'] = {
    'Warlock 3 lvl (враг) (колдун Чары)':1,
    }

metadict_squads['Squad-hero (лично Чара) (враг)'] = {
    'Warlock 11 lvl (враг) (Чара Атенак)':1,
    }

#----
# Армия Чары:

metadict_squads['Company-regular (мирмидоны Чары) (враг)'] = {
    'Warrior 1 lvl (враг) (мирмидон)':180 + dice_throw('1d12'),
    'Warrior 2 lvl (враг) (мирмидон-ветеран)':10,
    'Warrior 3 lvl (враг) (мирмидон-сержант)':3,
    'Warrior 5 lvl (враг) (мирмидон-капитан)':1,
    'Warrior 4 lvl (враг) (мирмидон-лейтенант)':1,
    }

metadict_squads['Company-regular (тяжёлые баллисты Чары) (друг)'] = {
    'Warrior 2 lvl (siege engineer-apprentice) (ballista-siege)':10,
    'Warrior 4 lvl (siege engineer-master)':1,
    }

#----
# Армия Ашеры:

metadict_squads['Company-regular (демоны Ашеры) (враг)'] = {
    'Warrior 1 lvl (враг) (демон-рядовой)':180 + dice_throw('1d12'),
    'Warrior 2 lvl (враг) (демон-ветеран)':10,
    'Warrior 3 lvl (враг) (демон-сержант)':3,
    'Warrior 5 lvl (враг) (демон-капитан)':1,
    'Warrior 4 lvl (враг) (демон-лейтенант)':1,
    }

metadict_squads['Company-regular (карлы Ашеры) (враг)'] = {
    'Commoner 1 lvl (враг) (карл)':180 + dice_throw('3d12'),
    'Commoner 1 lvl (враг) (карл-ветеран)':4,
    'Warrior 3 lvl (враг) (демон-сержант)':1,
    }

#----
# Свита Тинв:

metadict_squads['Squad-hero (кошки Тинв) (друг)'] = {
    # TODO:
    # Её телохранитель Ри всегда рядом.
    # Половина свиты -- мистические ловкачи Ри.
    'Wizard 3 lvl (друг) (кошка Тинв)':12,
    'Wizard 9 lvl (друг) (Тинв)':1,
    }

metadict_squads['Squad-hero (кошки Тави) (друг)'] = {
    'Wizard 2 lvl (друг) (кошка Тави)':10,
    'Wizard 7 lvl (друг) (Тави)':1,
    }

#----
# Армия Тинв:

metadict_squads['Company-elite (гвардия Тави) (друг)'] = {
    'Warrior 2 lvl (друг) (ветеран Тави)':60,
    'Warrior 3 lvl (друг) (сержант Тави)':18,
    'Warrior 4 lvl (друг) (лейтенант Тави)':6,
    'Warrior 5 lvl (друг) (капитан Тави)':6,
    'Commoner 1 lvl (recruit)':500,
    }

#----
# Свита Крассиуса:

#----
# Армия Крассиуса:

metadict_squads['Company-hero (арбалетчики Тетры) (друг)'] = {
    # в отряде два капитана и +3 лейтенанта
    'Warrior 1 lvl (друг) (арбалетчик Тетры)':80 + dice_throw('1d12'),
    'Warrior 2 lvl (друг) (арбалетчик-ветеран Тетры)':10,
    'Warrior 3 lvl (друг) (арбалетчик-сержант Тетры)':3,
    'Warrior 4 lvl (друг) (арбалетчик-лейтенант Тетры)':4,
    'Warrior 5 lvl (друг) (арбалетчик-капитан Тетры)':2,
    }

#----
# Свита Кумара

metadict_squads['Squad-hero (монахи Кумара) (друг)'] = {
    # Свита из 13 монахов-теневиков. "Верные ученики".
    'Monk 9 lvl (друг) (Кумар «Чугуннорукий»)':1,
    'Monk 3 lvl (друг) (монах Кумара)':13,
    }

metadict_squads['Single-hero (лично Кумар) (друг)'] = {
    'Monk 9 lvl (друг) (Кумар «Чугуннорукий»)':1,
    }

#----
# Армия Кумара

metadict_squads['Company-militia (пращники Илиона) (друг)'] = {
    # Свинцовые снаряды
    'Commoner 1 lvl (друг) (пращник Илиона)':80 + dice_throw('3d12'),
    'Commoner 2 lvl (друг) (ветеран пращников Илиона)':5,
    'Warrior 3 lvl (друг) (сержант пращников Илиона)':1,
    }

metadict_squads['Company-regular (легионеры Илиона) (друг)'] = {
    # Огненные копья
    'Warrior 1 lvl (друг) (легионер Илиона)':80 + dice_throw('1d12'),
    'Warrior 2 lvl (друг) (ветеран Илиона)':10,
    'Warrior 3 lvl (друг) (сержант Илиона)':3,
    'Warrior 5 lvl (друг) (капитан Илиона)':1,
    'Warrior 4 lvl (друг) (лейтенант Илиона)':1,
    }

metadict_squads['Company-regular (средние баллисты Илиона) (друг)'] = {
    'Warrior 2 lvl (siege engineer-apprentice) (ballista-medium)':10,
    'Warrior 4 lvl (siege engineer-master)':1,
    }

metadict_squads['Company-regular (тяжёлые требушеты Илиона) (друг)'] = {
    'Warrior 2 lvl (siege engineer-apprentice) (trebuchet-heavy)':10,
    'Warrior 4 lvl (siege engineer-master)':1,
    }

metadict_squads['Company-regular (лёгкие требушеты Илиона) (друг)'] = {
    'Warrior 2 lvl (siege engineer-apprentice) (trebuchet-light)':10,
    'Warrior 4 lvl (siege engineer-master)':1,
    }

#----
# Друзья (битва за Лемнос):

metadict_squads['Company-militia (сатиры Павсания) (друг)'] = {
    'Commoner 1 lvl (друг) (сатир-охотник)':95,
    'Commoner 2 lvl (друг) (сатир-ветеран)':5,
    'Warrior 3 lvl (друг) (сатир-сержант)':1,
    }

metadict_squads['Company-militia (сатиры Павсания, сына Павсания) (друг)'] = {
    'Commoner 1 lvl (друг) (сатир-охотник)':95,
    'Commoner 2 lvl (друг) (сатир-ветеран)':5,
    'Warrior 4 lvl (друг) (сын Павсания)':1,
    'Warrior 3 lvl (друг) (сатир-сержант)':1,
    }

metadict_squads['Company-regular (легионеры мостовика Отто) (друг)'] = {
    # Сам Отто бежал с Фарамом, отряд остался оборонять мост.
    'Warrior 1 lvl (legionary infantry)':80 + dice_throw('1d12'),
    'Warrior 2 lvl (legionary infantry-corporal)':10,
    'Warrior 3 lvl (legionary infantry-sergeant)':3,
    'Warrior 4 lvl (legionary infantry-lieutenant)':1,
    #'Warrior 5 lvl (legionary infantry-captain)':1,
    }

#----
# Враги (битва за Лемнос):

metadict_squads['Band-hero (колдуны Кара\'Яма) (враг)'] = {
    # Кара'Яма сожрали буреспрайты, отряд разбит и продан в рабство.
    'Warlock 5 lvl (враг) (Кара\'Ям)':1,
    'Warlock 1 lvl (враг) (колдун Кара\'Яма)':12,
    }

#metadict_squads['Band-hero (колдуны Кема\'Эша) (враг)'] = {
#    'Warlock 5 lvl (враг) (Кема\'Эш)':1,
#    'Warlock 1 lvl (враг) (колдун Кема\'Эша)':6,
#    }

metadict_squads['Band-hero (следопыты Энзифа) (враг)'] = {
    # Захвачен Гаем Юлием
    'Ranger 5 lvl (враг) (Энзиф «Ходи-гора»)':1,
    'Ranger 1 lvl (враг) (следопыт Энзифа)':12,
    }

metadict_squads['Band-hero (паладины Магора) (враг)'] = {
    # Побеждён кентурией Марселлия и Патроклом
    'Paladin 5 lvl (враг) (Магор «Детоед»)':1,
    'Paladin 1 lvl (враг) (паладин Магора)':6,
    }

metadict_squads['Band-hero (снайперы Хана-Вама) (враг)'] = {
    # Взяты в плен Фарамом
    # "Верные ученики" и "Многочисленная свита"
    'Fighter 5 lvl (враг) (Хана\'Вам)':1,
    'Fighter 1 lvl (враг) (снайпер Хана\'Вама)':12,
    }

metadict_squads['Band-hero (друиды Тик-Бо) (враг)'] = {
    # Сбежали. Сдались Сакатру.
    'Druid 5 lvl (враг) (Тик-Бо «Робкий»)':1,
    'Druid 1 lvl (враг) (друид Тик-Бо)':6,
    #'Giant Octopus (conjured) (CR 1)':12,
    }

metadict_squads['Company-militia (демоны Кема\'Эша) (враг)'] = {
    # Выбиты Агатой и отрядом Аксиотеи:
    'Commoner 1 lvl (враг) (карл)':80,
    'Commoner 1 lvl (враг) (карл-ветеран)':4,
    'Warrior 3 lvl (враг) (демон Кема\'Эша)':1,
    }

metadict_squads['Company-regular (лучники Энзифа) (враг)'] = {
    # Побеждены Гаем Юлием и сатирами Павсания.
    'Warrior 1 lvl (sqythian bowman)':185,
    'Warrior 2 lvl (sqythian bowman-corporal)':10,
    'Warrior 3 lvl (sqythian bowman-sergeant)':3,
    'Warrior 4 lvl (sqythian bowman-lieutenant)':1,
    }

metadict_squads['Company-regular (сариссофоры Магора) (враг)'] = {
    # Побеждены Патроклом и кентурией Марселлия
    'Warrior 1 lvl (city pikeman)':75,
    'Warrior 2 lvl (city pikeman-corporal)':20,
    'Warrior 3 lvl (city pikeman-sergeant)':6,
    'Warrior 4 lvl (city pikeman-lieutenant)':2,
    }

metadict_squads['Company-regular (лучники Хана-Вама) (враг)'] = {
    # Уничтожены Подводной стражей Психеи
    'Warrior 1 lvl (sqythian bowman)':75,
    'Warrior 2 lvl (sqythian bowman-corporal)':10,
    'Warrior 3 lvl (sqythian bowman-sergeant)':3,
    'Warrior 4 lvl (sqythian bowman-lieutenant)':1,
    'Warrior 5 lvl (sqythian bowman-captain)':1,
    }

metadict_squads['Company-regular (пираты Кара-Яма) (конные) (враг)'] = {
    # Взяты в плен Фарамом
    'Warrior 1 lvl (cavalry archer)':6,
    'Warrior 2 lvl (cavalry archer-corporal)':10,
    'Warrior 3 lvl (cavalry archer-sergeant)':3,
    'Warrior 4 lvl (cavalry archer-lieutenant)':1,
    }

metadict_squads['Company-regular (пираты Кара-Яма) (пешие) (враг)'] = {
    # Взяты в плен Патроклом в битве за корабли.
    # Лучшие в конном отряде.
    'Warrior 1 lvl (cilician infantry)':70,
    'Warrior 3 lvl (cilician infantry-sergeant)':1,
    }

metadict_squads['Company-regular (пираты Кема-Эша) (враг)'] = {
    # Сбежали, пострадали от дактилей, сдались Сакатру.
    'Warrior 1 lvl (cilician infantry)':75,
    'Warrior 2 lvl (cilician infantry-corporal)':10,
    'Warrior 3 lvl (cilician infantry-sergeant)':3,
    'Warrior 4 lvl (cilician infantry-lieutenant)':1,
    }

metadict_squads['Company-regular (пращники Тик-Бо) (враг)'] = {
    # Сбежали, пострадали от дактилей, сдались Сакатру.
    'Warrior 1 lvl (balear slinger)':75,
    'Warrior 2 lvl (balear slinger-corporal)':10,
    'Warrior 3 lvl (balear slinger-sergeant)':3,
    'Warrior 4 lvl (balear slinger-lieutenant)':1,
    }

#----
# Армия Нингиримы:

metadict_squads['Company-veteran (гоплиты Нингиримы) (враг)'] = {
    # Опытный отряд.
    'Warrior 1 lvl (враг) (гоплит Нингиримы)':46 + dice_throw('1d12'),
    'Warrior 2 lvl (враг) (гоплит-ветеран Нингиримы)':46,
    'Warrior 3 lvl (враг) (гоплит-сержант Нингиримы)':3,
    'Warrior 5 lvl (враг) (гоплит-капитан Нингиримы)':2,
    'Warrior 4 lvl (враг) (гоплит-лейтенант Нингиримы)':1,
    'Commoner 1 lvl (recruit)':100,
    }

metadict_squads['Company-veteran (гоплиты Клеомена) (враг)'] = {
    # Опытный отряд.
    'Warrior 2 lvl (враг) (гоплит-ветеран Нингиримы)':90,
    'Warrior 3 lvl (враг) (гоплит-сержант Нингиримы)':6,
    'Warrior 5 lvl (враг) (гоплит-капитан Нингиримы)':2,
    'Warrior 4 lvl (враг) (гоплит-лейтенант Нингиримы)':2,
    'Commoner 1 lvl (recruit)':100,
    }

#-------------------------------------------------------------------------
# Игроки

#----
# Свита Сакатра

metadict_squads['Squad-hero (следопыты Сакатра) (Gogan)'] = {
    'Ranger 7 lvl (Gogan) (Сакатр Ка-Ален)':1,
    'Ranger 2 lvl (Gogan) (следопыт Сакатра)':10,
    }

#----
# Армия Сакатра

metadict_squads['Company-regular (пираты Сакатра) (Gogan)'] = {
    # Многочисленные бойцы
    'Warrior 1 lvl (Gogan) (кимерийский пират)':185,
    'Warrior 2 lvl (Gogan) (кимерийский пират-ветеран)':10,
    'Warrior 3 lvl (Gogan) (кимерийский пират-сержант)':3,
    'Warrior 5 lvl (Gogan) (кимерийский пират-капитан)':1,
    'Warrior 4 lvl (Gogan) (кимерийский пират-лейтенант)':1,
    }

metadict_squads['Company-militia (пращники Сакатра) (Gogan)'] = {
    'Commoner 1 lvl (militia slinger)':80 + dice_throw('3d12'),
    'Commoner 2 lvl (militia slinger-corporal)':5,
    'Warrior 3 lvl (militia slinger-sergeant)':1,
    }

metadict_squads['Squad-hero (колдуны Кема\'Эша) (друг)'] = {
    'Warlock 6 lvl (друг) (Кема\'Эш «Ловкач»)':1,
    'Warlock 2 lvl (друг) (колдун Кема\'Эша)':10,
    }

#----
# Свита Гая Юлия

metadict_squads['Squad-hero (преторианцы Гая Юлия) (Katorjnik)'] = {
    'Fighter 7 lvl (Katorjnik) (Гай Юлий)':1,
    'Fighter 2 lvl (Katorjnik) (преторианец Гая Юлия)':10,
    }

#----
# Армия Гая Юлия

metadict_squads['Company-regular (легионеры Гая Юлия) (Katorjnik)'] = {
    # Опытный отряд.
    'Warrior 1 lvl (Katorjnik) (манипуларий)':75,
    'Warrior 2 lvl (Katorjnik) (ветеран)':20,
    'Warrior 3 lvl (Katorjnik) (урагос)':6,
    'Warrior 4 lvl (Katorjnik) (опцион)':2,
    'Warrior 5 lvl (Katorjnik) (центурион)':1,
    }

metadict_squads['Company-veteran (ветераны Гая Юлия) (Katorjnik)'] = {
    # Два капитана, опытный отряд.
    'Warrior 2 lvl (Katorjnik) (ветеран) (кольчуга)':50,
    'Warrior 2 lvl (Katorjnik) (ветеран)':40,
    'Warrior 3 lvl (Katorjnik) (урагос)':6,
    'Warrior 5 lvl (Katorjnik) (центурион)':2,
    'Warrior 4 lvl (Katorjnik) (опцион)':2,
    'Commoner 1 lvl (recruit)':100,
    }

metadict_squads['Company-veteran (гвардия Гая Юлия) (Katorjnik)'] = {
    # Три опытных капитана, от каждого удвоенный опыт.
    'Warrior 2 lvl (Katorjnik) (ветеран)':60,
    'Warrior 3 lvl (Katorjnik) (урагос)':30,
    'Warrior 5 lvl (Katorjnik) (центурион)':3,
    'Warrior 4 lvl (Katorjnik) (опцион)':6,
    'Commoner 1 lvl (recruit)':300,
    }

metadict_squads['Company-militia (гастаты Гая Юлия) (Katorjnik)'] = {
    'Commoner 1 lvl (militia spearman)':95,
    'Commoner 2 lvl (militia spearman-corporal)':5,
    'Warrior 3 lvl (militia spearman-sergeant)':1,
    }

#----
# Свита Фарама

metadict_squads['Squad-hero (жрецы Фарама) (Mordodrukow)'] = {
    'Cleric 7 lvl (Mordodrukow) (Фарам «Друг Богов»)':1,
    'Fighter 7 lvl (Mordodrukow) (Лонгин)':1,
    'Fighter 2 lvl (Mordodrukow) (снайпер Фарама)':2,
    'Fighter 2 lvl (Mordodrukow) (темплар Фарама)':2,
    'Cleric 2 lvl (Mordodrukow) (жрец Фарама) (лекарь)':2,
    'Cleric 2 lvl (Mordodrukow) (жрец Фарама) (боевой)':3,
    }

metadict_squads['Band-hero (Фарам и Лонгин) (Mordodrukow)'] = {
    # Отдельно от свиты
    'Cleric 7 lvl (Mordodrukow) (Фарам «Друг Богов»)':1,
    'Fighter 7 lvl (Mordodrukow) (Лонгин)':1,
    }

metadict_squads['Band-hero (снайпер Лонгин) (Mordodrukow)'] = {
    # Отдельно от команды Фарама:
    'Fighter 7 lvl (Mordodrukow) (Лонгин)':1,
    }

metadict_squads['Squad-hero (барды Тетры) (друг)'] = {
    'Bard 2 lvl (друг) (бард Тетры)':10,
    'Bard 6 lvl (друг) (Тетра Курио)':1,
    }

#----
# Армия Фарама

metadict_squads['Company-regular (лучники Фарама) (Mordodrukow)'] = {
    'Warrior 1 lvl (Mordodrukow) (лучник Фарама)':85,
    'Warrior 2 lvl (Mordodrukow) (ветеран Фарама)':10,
    'Warrior 3 lvl (Mordodrukow) (сержант Фарама)':3,
    'Warrior 5 lvl (Mordodrukow) (капитан Фарама)':1,
    'Warrior 4 lvl (Mordodrukow) (лейтенант Фарама)':1,
    }

#----
# Свита Патрокла

metadict_squads['Squad-hero (жрецы Патрокла) (Vened)'] = {
    'Cleric 7 lvl (Vened) (Патрокл «Македонянин»)':1,
    'Cleric 2 lvl (Vened) (жрец Патрокла)':12,
    }

metadict_squads['Squad-hero (друиды Патрокла) (Vened)'] = {
    'Druid 7 lvl (Vened) (Брат Патрокла)':1,
    'Druid 2 lvl (Vened) (друид Патрокла)':10,
    }

#----
# Армия Патрокла

metadict_squads['Company-elite (гвардия Патрокла) (Vened)'] = {
    # Сводный отряд ветеранов:
    'Warrior 2 lvl (Vened) (ветеран Патрокла)':60,
    'Warrior 3 lvl (Vened) (сержант Патрокла)':18,
    'Warrior 4 lvl (Vened) (лейтенант Патрокла)':6,
    'Warrior 5 lvl (Vened) (капитан Патрокла)':6,
    'Commoner 1 lvl (recruit)':500,
    }

metadict_squads['Company-regular (сариссофоры Патрокла) (Vened)'] = {
    'Warrior 1 lvl (Vened) (сариссофор Патрокла)':80 + dice_throw('1d12'),
    'Warrior 2 lvl (Vened) (ветеран Патрокла)':10,
    'Warrior 3 lvl (Vened) (сержант Патрокла)':3,
    'Warrior 4 lvl (Vened) (лейтенант Патрокла)':1,
    'Warrior 5 lvl (Vened) (капитан Патрокла)':1,
    }

metadict_squads['Company-regular (онагры Патрокла) (fire) (Vened)'] = {
    'Warrior 2 lvl (siege engineer-apprentice) (onager-fire)':10,
    'Warrior 4 lvl (siege engineer-master)':1,
    }

metadict_squads['Company-regular (онагры Патрокла) (siege) (Vened)'] = {
    'Warrior 2 lvl (siege engineer-apprentice) (onager-siege)':10,
    'Warrior 4 lvl (siege engineer-master)':1,
    }

metadict_squads['Company-militia (тяжёлые арбалетчики Патрокла) (Vened)'] = {
    # Отряд ополчения с тяжёлыми арбалетами:
    'Commoner 1 lvl (militia heavy crossbowman)':80 + dice_throw('3d12'),
    'Commoner 2 lvl (militia heavy crossbowman-corporal)':5,
    'Warrior 3 lvl (militia heavy crossbowman-sergeant)':1,
    }

metadict_squads['Company-militia (арбалетчики Патрокла) (Vened)'] = {
    'Commoner 1 lvl (militia crossbowman)':80 + dice_throw('3d12'),
    'Commoner 2 lvl (militia crossbowman-corporal)':5,
    'Warrior 3 lvl (militia crossbowman-sergeant)':1,
    }

#----
# Свита Ианты

metadict_squads['Squad-hero (друиды Ианты) (Vaarsuvius)'] = {
    'Druid 7 lvl (Vaarsuvius) (Ианта «Дочь бури»)':1,
    'Druid 2 lvl (Vaarsuvius) (друид Ианты) (Психея)':1,
    'Druid 2 lvl (Vaarsuvius) (друид Ианты)':19,
    }

metadict_squads['Band-hero (дракон Ианты) (Агаталара Огненная) (Vaarsuvius)'] = {
    'Brass Dragon, (Vaarsuvius) (Агаталара Огненная)':1,
    }

#----
# Армия Ианты

metadict_squads['Company-elite (гвардия Филлис) (Vaarsuvius)'] = {
    'Warrior 2 lvl (Vaarsuvius) (ветеран Филлис)':60,
    'Warrior 3 lvl (Vaarsuvius) (сержант Филлис)':18,
    'Warrior 4 lvl (Vaarsuvius) (лейтенант Филлис)':6,
    'Warrior 5 lvl (Vaarsuvius) (капитан Филлис)':6,
    'Warrior 7 lvl (Vaarsuvius) (Филлис)':1,
    'Commoner 1 lvl (recruit)':500,
    }

metadict_squads['Company-regular (дочери медведицы Ианты) (Vaarsuvius)'] = {
    'Warrior 1 lvl (Vaarsuvius) (дочерь медведицы Филлис)':85,
    'Warrior 2 lvl (Vaarsuvius) (ветеран Филлис)':10,
    'Warrior 3 lvl (Vaarsuvius) (сержант Филлис)':3,
    'Warrior 4 lvl (Vaarsuvius) (лейтенант Филлис)':1,
    'Warrior 5 lvl (Vaarsuvius) (капитан Филлис)':1,
    'Warrior 7 lvl (Vaarsuvius) (Филлис)':1,
    }

metadict_squads['Company-regular (лучники Ианты) (Vaarsuvius)'] = {
    'Warrior 1 lvl (Vaarsuvius) (стрелок)':85,
    'Warrior 2 lvl (Vaarsuvius) (стрелок-ветеран)':10,
    'Warrior 3 lvl (Vaarsuvius) (меткий стрелок)':3,
    'Warrior 4 lvl (Vaarsuvius) (стрелок-лейтенант)':1,
    'Warrior 5 lvl (Vaarsuvius) (стрелок-капитан)':1,
    }

metadict_squads['Company-militia (охотницы Ианты) (Vaarsuvius)'] = {
    'Commoner 1 lvl (Vaarsuvius) (охотница)':95,
    'Commoner 2 lvl (Vaarsuvius) (охотница-ветеран)':5,
    'Warrior 3 lvl (Vaarsuvius) (меткий стрелок-отставник)':1,
    }

metadict_squads['Company-militia (дикарки Ианты) (Vaarsuvius)'] = {
    'Commoner 1 lvl (Vaarsuvius) (дикарка)':95,
    'Commoner 2 lvl (Vaarsuvius) (дикарка-ветеран)':5,
    'Warrior 3 lvl (Vaarsuvius) (меткий стрелок-отставник)':1,
    }

metadict_squads['Company-militia (токсотаи Ианты) (Vaarsuvius)'] = {
    'Commoner 1 lvl (Vaarsuvius) (токсотай)':95,
    'Commoner 2 lvl (Vaarsuvius) (токсотай-ветеран)':5,
    'Warrior 3 lvl (Vaarsuvius) (меткий стрелок-отставник)':1,
    }

#----
# Геройские отряды (армия Протесилая):

metadict_squads['Band-hero (паладины Протесилая) (Тзаангор)'] = {
    'Paladin 5 lvl (Тзаангор) (Протесилай II, «Держатель щита»)':1,
    'Paladin 1 lvl (Тзаангор) (паладины)':6,
    }

metadict_squads['Company-regular (сариссофоры Протесилая) (Тзаангор)'] = {
    'Warrior 1 lvl (Тзаангор) (гипасист)':75,
    'Warrior 2 lvl (Тзаангор) (ветеран)':20,
    'Warrior 3 lvl (Тзаангор) (ур-лодакос)':6,
    'Warrior 4 lvl (Тзаангор) (лодакос)':2,
    }

#----
# Геройские отряды (армия Артаманаха):

metadict_squads['Band-hero (снайперы Артаманаха) (ArbitraryNickname)'] = {
    'Fighter 5 lvl (ArbitraryNickname) (Артаманах Рыбник)':1,
    'Fighter 1 lvl (ArbitraryNickname) (снайпер)':6,
    }

#-------------------------------------------------------------------------
# Базовые отряды

#----
# Ополчение

metadict_squads['Company-militia (skirmisher-peltasts)'] = {
    # У нас не хватит лейтенантов на все отряды ополчения, да и сержантов тоже мало.
    'Commoner 1 lvl (militia javeliner)':80 + dice_throw('3d12'),
    'Commoner 2 lvl (militia javeliner-corporal)':5,
    'Warrior 3 lvl (militia javeliner-sergeant)':1,
    #'Warrior 4 lvl (militia javeliner-lieutenant)':1,
    }

metadict_squads['Company-militia (infantry-spearmans)'] = {
    'Commoner 1 lvl (militia spearman)':80 + dice_throw('3d12'),
    'Commoner 2 lvl (militia spearman-corporal)':5,
    'Warrior 3 lvl (militia spearman-sergeant)':1,
    #'Warrior 4 lvl (militia spearman-lieutenant)':1,
    }

metadict_squads['Company-militia (infantry-swordsmans)'] = {
    'Commoner 1 lvl (militia swordsman)':80 + dice_throw('3d12'),
    'Commoner 2 lvl (militia swordsman-corporal)':5,
    'Warrior 3 lvl (militia swordsman-sergeant)':1,
    #'Warrior 4 lvl (militia swordsman-lieutenant)':1,
    }

metadict_squads['Company-militia (skirmisher-slingers)'] = {
    'Commoner 1 lvl (militia slinger)':80 + dice_throw('3d12'),
    'Commoner 2 lvl (militia slinger-corporal)':5,
    'Warrior 3 lvl (militia slinger-sergeant)':1,
    #'Warrior 4 lvl (militia slinger-lieutenant)':1,
    }

metadict_squads['Company-militia (bowmans-hunters)'] = {
    'Commoner 1 lvl (militia bowman)':80 + dice_throw('3d12'),
    'Commoner 2 lvl (militia bowman-corporal)':5,
    'Warrior 3 lvl (militia bowman-sergeant)':1,
    #'Warrior 4 lvl (militia bowman-lieutenant)':1,
    }

metadict_squads['Company-militia (crossbowmans)'] = {
    'Commoner 1 lvl (militia crossbowman)':80 + dice_throw('3d12'),
    'Commoner 2 lvl (militia crossbowman-corporal)':5,
    'Warrior 3 lvl (militia crossbowman-sergeant)':1,
    #'Warrior 4 lvl (militia crossbowman-lieutenant)':1,
    }

metadict_squads['Company-militia (heavy crossbowmans)'] = {
    'Commoner 1 lvl (militia heavy crossbowman)':80 + dice_throw('3d12'),
    'Commoner 2 lvl (militia heavy crossbowman-corporal)':5,
    'Warrior 3 lvl (militia heavy crossbowman-sergeant)':1,
    #'Warrior 4 lvl (militia heavy crossbowman-lieutenant)':1,
    }

#----
# Регулярная армия:

metadict_squads['Company-regular (infantry-hoplites)'] = {
    # По "Тактике" Флавия Арриана:
    # http://militera.lib.ru/science/arrianus01/index.html
    # Лохом называют колонну сариссофоров, длина которой равна глубине строя.
    # - Лохом (8-16 бойцов), командует лохаг (протостат, гегемон);
    # - Два лоха зовутся дилохией, из тридцати двух человек, и дилохит её командир;
    # - Четыре лоха – тетрархия, и его командир – тетрарх, начальник шестидесяти четырех мужей;
    # - Две тетрархии – таксис, лохов же восемь, а мужей сто двадцать восемь, и их командир – таксиарх;
    # - Когда подразделение состоит из сотни, ее командир называется сотник (гекатонтарх).
    'Warrior 1 lvl (achean hoplite)':80 + dice_throw('1d12'),
    'Warrior 2 lvl (achean hoplite-corporal)':10,
    'Warrior 3 lvl (achean hoplite-sergeant)':3,
    'Warrior 4 lvl (achean hoplite-lieutenant)':1,
    'Warrior 5 lvl (achean hoplite-captain)':1,
    }

metadict_squads['Company-regular (infantry-legionary)'] = {
    # Распределение опыта по уровням:
        # 2 lvl -- 300 * 10 = 3000
        # 3 lvl -- 1200 * 3 = 3600
        # 4 lvl -- 3900 * 1 = 3900
    # Всего около 10 500 опыта (как у героя 5 lvl)
        # 5 lvl -- 10400 * 1 = 10 400
    'Warrior 1 lvl (legionary infantry)':80 + dice_throw('1d12'),
    'Warrior 2 lvl (legionary infantry-corporal)':10,
    'Warrior 3 lvl (legionary infantry-sergeant)':3,
    'Warrior 4 lvl (legionary infantry-lieutenant)':1,
    'Warrior 5 lvl (legionary infantry-captain)':1,
    }

metadict_squads['Company-regular (infantry-pikemans)'] = {
    'Warrior 1 lvl (city pikeman)':80 + dice_throw('1d12'),
    'Warrior 2 lvl (city pikeman-corporal)':10,
    'Warrior 3 lvl (city pikeman-sergeant)':3,
    'Warrior 4 lvl (city pikeman-lieutenant)':1,
    'Warrior 5 lvl (city pikeman-captain)':1,
    }

metadict_squads['Company-regular (infantry-thracian)'] = {
    'Warrior 1 lvl (thracian infantry)':80 + dice_throw('1d12'),
    'Warrior 2 lvl (thracian infantry-corporal)':10,
    'Warrior 3 lvl (thracian infantry-sergeant)':3,
    'Warrior 4 lvl (thracian infantry-lieutenant)':1,
    'Warrior 5 lvl (thracian infantry-captain)':1,
    }

metadict_squads['Company-regular (infantry-cilician)'] = {
    'Warrior 1 lvl (cilician infantry)':80 + dice_throw('1d12'),
    'Warrior 2 lvl (cilician infantry-corporal)':10,
    'Warrior 3 lvl (cilician infantry-sergeant)':3,
    'Warrior 4 lvl (cilician infantry-lieutenant)':1,
    'Warrior 5 lvl (cilician infantry-captain)':1,
    }

metadict_squads['Company-regular (bowmans-scythian)'] = {
    'Warrior 1 lvl (sqythian bowman)':80 + dice_throw('1d12'),
    'Warrior 2 lvl (sqythian bowman-corporal)':10,
    'Warrior 3 lvl (sqythian bowman-sergeant)':3,
    'Warrior 4 lvl (sqythian bowman-lieutenant)':1,
    'Warrior 5 lvl (sqythian bowman-captain)':1,
    }

#----
# Регулярная армия (огнестрел):

metadict_squads['Company-regular (line-infantry-musketeers)'] = {
    'Warrior 1 lvl (musketeer line-infantry)':80 + dice_throw('1d12'),
    'Warrior 2 lvl (musketeer line-infantry-corporal)':10,
    'Warrior 3 lvl (musketeer line-infantry-sergeant)':3,
    'Warrior 4 lvl (musketeer line-infantry-lieutenant)':1,
    'Warrior 5 lvl (musketeer line-infantry-captain)':1,
    }

metadict_squads['Company-regular (line-infantry-grenadiers)'] = {
    'Warrior 1 lvl (grenadier line-infantry)':80 + dice_throw('1d12'),
    'Warrior 2 lvl (grenadier line-infantry-corporal)':10,
    'Warrior 3 lvl (grenadier line-infantry-sergeant)':3,
    'Warrior 4 lvl (grenadier line-infantry-lieutenant)':1,
    'Warrior 5 lvl (grenadier line-infantry-captain)':1,
    }

metadict_squads['Company-regular (line-infantry-bombardiers)'] = {
    'Warrior 1 lvl (bombardier line-infantry)':80 + dice_throw('1d12'),
    'Warrior 2 lvl (bombardier line-infantry-corporal)':10,
    'Warrior 3 lvl (bombardier line-infantry-sergeant)':3,
    'Warrior 4 lvl (bombardier line-infantry-lieutenant)':1,
    'Warrior 5 lvl (bombardier line-infantry-captain)':1,
    }

metadict_squads['Company-regular (line-infantry-fusiliers)'] = {
    'Warrior 1 lvl (fusilier line-infantry)':80 + dice_throw('1d12'),
    'Warrior 2 lvl (fusilier line-infantry-corporal)':10,
    'Warrior 3 lvl (fusilier line-infantry-sergeant)':3,
    'Warrior 4 lvl (fusilier line-infantry-lieutenant)':1,
    'Warrior 5 lvl (fusilier line-infantry-captain)':1,
    }

#----
# Регулярная армия:

#metadict_squads['Company-regular (infantry-polearms)'] = {
#    'Warrior 1 lvl (mercenary heavy-infantry)':80 + dice_throw('1d12'),
#    'Warrior 2 lvl (mercenary heavy-infantry-corporal)':10,
#    'Warrior 3 lvl (mercenary heavy-infantry-sergeant)':3,
#    'Warrior 4 lvl (mercenary heavy-infantry-lieutenant)':1,
#    'Warrior 5 lvl (mercenary heavy-infantry-captain)':1,
#    }

#metadict_squads['Company-regular (infantry-shekelesh)'] = {
#    'Warrior 1 lvl (shekelesh infantry)':80 + dice_throw('1d12'),
#    'Warrior 2 lvl (shekelesh infantry-corporal)':10,
#    'Warrior 3 lvl (shekelesh infantry-sergeant)':3,
#    'Warrior 4 lvl (shekelesh infantry-lieutenant)':1,
#    'Warrior 5 lvl (shekelesh infantry-captain)':1,
#    }
#
#metadict_squads['Company-regular (infantry-celtian)'] = {
#    'Warrior 1 lvl (celtian infantry)':80 + dice_throw('1d12'),
#    'Warrior 2 lvl (celtian infantry-corporal)':10,
#    'Warrior 3 lvl (celtian infantry-sergeant)':3,
#    'Warrior 4 lvl (celtian infantry-lieutenant)':1,
#    'Warrior 5 lvl (celtian infantry-captain)':1,
#    }
#

#metadict_squads['Company-regular (bowmans-persian)'] = {
#    'Warrior 1 lvl (persian bowman)':80 + dice_throw('1d12'),
#    'Warrior 2 lvl (persian bowman-corporal)':10,
#    'Warrior 3 lvl (persian bowman-sergeant)':3,
#    'Warrior 4 lvl (persian bowman-lieutenant)':1,
#    'Warrior 5 lvl (persian bowman-captain)':1,
#    }

#metadict_squads['Company-regular (slingers-balear)'] = {
#    'Warrior 1 lvl (balear slinger)':80 + dice_throw('1d12'),
#    'Warrior 2 lvl (balear slinger-corporal)':10,
#    'Warrior 3 lvl (balear slinger-sergeant)':3,
#    'Warrior 4 lvl (balear slinger-lieutenant)':1,
#    'Warrior 5 lvl (balear slinger-captain)':1,
#    }

#----
# Ветеранские отряды:
# Тесты боёв:
    # 400 000 неписей сражалось ради этих тестов.
    # sqythian  | cilician  | pikemans  | thracian  | hoplites  | legionary | vs
    # --------- | --------- | --------- | --------- | --------- | --------- | ---------
    # -         | -         | -         | -         | -         | -         | sqythian
    # -         | -         | 67/29     | 55/45     | 76/24     | 53/46     | cilician
    # -         | 29/67     | -         | 28/66     | 63/36     | 49/49     | pikemans
    # -         | 45/55     | 66/28     | -         | 85/13     | 67/30     | thracian
    # -         | 24/76     | 36/63     | 13/85     | -         | 63/36     | hoplites
    # -         | 46/53     | 49/49     | 30/67     | 36/63     | -         | legionary

#metadict_squads['Company-veteran (infantry-hoplites)'] = {
#    # Отряд героя 6 lvl
#    # Два капитана и 20 800 exp на отряд, +34 ветерана.
#    # Отборный отряд -- 200 рекрутов на 100 солдат
#    # Fighting_Style_Dueling
#    'Warrior 1 lvl (achean hoplite)':46 + dice_throw('1d12'),
#    'Warrior 2 lvl (achean hoplite-corporal)':44,
#    'Warrior 3 lvl (achean hoplite-sergeant)':3,
#    'Warrior 4 lvl (achean hoplite-lieutenant)':1,
#    'Warrior 5 lvl (achean hoplite-captain)':2,
#    'Commoner 1 lvl (recruit)':100,
#    }
#
#metadict_squads['Company-veteran (infantry-legionary)'] = {
#    # Fighting_Style_Protection
#    'Warrior 1 lvl (legionary infantry)':46 + dice_throw('1d12'),
#    'Warrior 2 lvl (legionary infantry-corporal)':44,
#    'Warrior 3 lvl (legionary infantry-sergeant)':3,
#    'Warrior 4 lvl (legionary infantry-lieutenant)':1,
#    'Warrior 5 lvl (legionary infantry-captain)':2,
#    'Commoner 1 lvl (recruit)':100,
#    }
#
#metadict_squads['Company-veteran (infantry-pikemans)'] = {
#    # Fighting_Style_Defence
#    'Warrior 1 lvl (city pikeman)':46 + dice_throw('1d12'),
#    'Warrior 2 lvl (city pikeman-corporal)':44,
#    'Warrior 3 lvl (city pikeman-sergeant)':3,
#    'Warrior 4 lvl (city pikeman-lieutenant)':1,
#    'Warrior 5 lvl (city pikeman-captain)':2,
#    'Commoner 1 lvl (recruit)':100,
#    }
#
#metadict_squads['Company-veteran (infantry-thracian)'] = {
#    # Fighting_Style_Great_Weapon_Fighting
#    'Warrior 1 lvl (thracian infantry)':46 + dice_throw('1d12'),
#    'Warrior 2 lvl (thracian infantry-corporal)':44,
#    'Warrior 3 lvl (thracian infantry-sergeant)':3,
#    'Warrior 4 lvl (thracian infantry-lieutenant)':1,
#    'Warrior 5 lvl (thracian infantry-captain)':2,
#    'Commoner 1 lvl (recruit)':100,
#    }
#
#metadict_squads['Company-veteran (infantry-cilician)'] = {
#    # Fighting_Style_Two_Weapon_Fighting
#    'Warrior 1 lvl (cilician infantry)':46 + dice_throw('1d12'),
#    'Warrior 2 lvl (cilician infantry-corporal)':44,
#    'Warrior 3 lvl (cilician infantry-sergeant)':3,
#    'Warrior 4 lvl (cilician infantry-lieutenant)':1,
#    'Warrior 5 lvl (cilician infantry-captain)':2,
#    'Commoner 1 lvl (recruit)':100,
#    }
#
#metadict_squads['Company-veteran (bowmans-scythian)'] = {
#    # Fighting_Style_Archery
#    'Warrior 1 lvl (sqythian bowman)':46 + dice_throw('1d12'),
#    'Warrior 2 lvl (sqythian bowman-corporal)':44,
#    'Warrior 3 lvl (sqythian bowman-sergeant)':3,
#    'Warrior 4 lvl (sqythian bowman-lieutenant)':1,
#    'Warrior 5 lvl (sqythian bowman-captain)':2,
#    'Commoner 1 lvl (recruit)':100,
#    }

#----
# Ветеранские отряды:

metadict_squads['Company-veteran (infantry-hoplites)'] = {
    # Отряд героя 7 lvl
    # Шесть капитанов и 62 400 exp на отряд.
    # Отборный отряд (сумма параметров 63+) -- 200 рекрутов на 100 солдат
    'Warrior 2 lvl (achean hoplite-corporal)':60,
    'Warrior 3 lvl (achean hoplite-sergeant)':18,
    'Warrior 4 lvl (achean hoplite-lieutenant)':6,
    'Warrior 5 lvl (achean hoplite-captain)':6,
    'Commoner 1 lvl (recruit)':100,
    }

metadict_squads['Company-veteran (infantry-legionary)'] = {
    'Warrior 2 lvl (legionary infantry-corporal)':60,
    'Warrior 3 lvl (legionary infantry-sergeant)':18,
    'Warrior 4 lvl (legionary infantry-lieutenant)':6,
    'Warrior 5 lvl (legionary infantry-captain)':6,
    'Commoner 1 lvl (recruit)':100,
    }

metadict_squads['Company-veteran (infantry-pikemans)'] = {
    'Warrior 2 lvl (city pikeman-corporal)':60,
    'Warrior 3 lvl (city pikeman-sergeant)':18,
    'Warrior 4 lvl (city pikeman-lieutenant)':6,
    'Warrior 5 lvl (city pikeman-captain)':6,
    'Commoner 1 lvl (recruit)':100,
    }

metadict_squads['Company-veteran (infantry-thracian)'] = {
    'Warrior 2 lvl (thracian infantry-corporal)':60,
    'Warrior 3 lvl (thracian infantry-sergeant)':18,
    'Warrior 4 lvl (thracian infantry-lieutenant)':6,
    'Warrior 5 lvl (thracian infantry-captain)':6,
    'Commoner 1 lvl (recruit)':100,
    }

metadict_squads['Company-veteran (infantry-cilician)'] = {
    'Warrior 2 lvl (cilician infantry-corporal)':60,
    'Warrior 3 lvl (cilician infantry-sergeant)':18,
    'Warrior 4 lvl (cilician infantry-lieutenant)':6,
    'Warrior 5 lvl (cilician infantry-captain)':6,
    'Commoner 1 lvl (recruit)':100,
    }

metadict_squads['Company-veteran (bowmans-scythian)'] = {
    'Warrior 2 lvl (sqythian bowman-corporal)':60,
    'Warrior 3 lvl (sqythian bowman-sergeant)':18,
    'Warrior 4 lvl (sqythian bowman-lieutenant)':6,
    'Warrior 5 lvl (sqythian bowman-captain)':6,
    'Commoner 1 lvl (recruit)':100,
    }

metadict_squads['Company-veteran (line-infantry-musketeers)'] = {
    'Warrior 2 lvl (musketeer line-infantry-corporal)':60,
    'Warrior 3 lvl (musketeer line-infantry-sergeant)':18,
    'Warrior 4 lvl (musketeer line-infantry-lieutenant)':6,
    'Warrior 5 lvl (musketeer line-infantry-captain)':6,
    'Commoner 1 lvl (recruit)':100,
    }

metadict_squads['Company-veteran (line-infantry-grenadiers)'] = {
    'Warrior 2 lvl (grenadier line-infantry-corporal)':60,
    'Warrior 3 lvl (grenadier line-infantry-sergeant)':18,
    'Warrior 4 lvl (grenadier line-infantry-lieutenant)':6,
    'Warrior 5 lvl (grenadier line-infantry-captain)':6,
    'Commoner 1 lvl (recruit)':100,
    }

metadict_squads['Company-veteran (line-infantry-bombardiers)'] = {
    'Warrior 2 lvl (bombardier line-infantry-corporal)':60,
    'Warrior 3 lvl (bombardier line-infantry-sergeant)':18,
    'Warrior 4 lvl (bombardier line-infantry-lieutenant)':6,
    'Warrior 5 lvl (bombardier line-infantry-captain)':6,
    'Commoner 1 lvl (recruit)':100,
    }

#----
# Элитные отряды:

metadict_squads['Company-elite (line-infantry-musketeers)'] = {
    # Гвардия героев 11+ lvl
    # 25 капитанов и 260 000 exp на отряд.
    # Отличный отряд (сумма параметров 69+) -- 400 рекрутов на 100 солдат
    'Warrior 4 lvl (musketeer line-infantry-lieutenant)':67,
    'Warrior 5 lvl (musketeer line-infantry-captain)':25,
    'Commoner 1 lvl (recruit)':300,
    }

metadict_squads['Company-elite (line-infantry-grenadiers)'] = {
    'Warrior 4 lvl (grenadier line-infantry-lieutenant)':67,
    'Warrior 5 lvl (grenadier line-infantry-captain)':25,
    'Commoner 1 lvl (recruit)':300,
    }

metadict_squads['Company-elite (line-infantry-bombardier)'] = {
    'Warrior 4 lvl (bombardier line-infantry-lieutenant)':67,
    'Warrior 5 lvl (bombardier line-infantry-captain)':25,
    'Commoner 1 lvl (recruit)':300,
    }

#----
# Герои (свиты):

metadict_squads['Squad-hero (barbarians)'] = {
    'Barbarian 5 lvl (thracian slayer-lord)':1,
    #'Barbarian 4 lvl (thracian slayer-thane)':1,
    #'Barbarian 3 lvl (thracian slayer-juggernaught)':12,
    'Barbarian 2 lvl (thracian slayer-slasher)':12,
    #'Barbarian 1 lvl (thracian slayer-dogface)':12,
    }

metadict_squads['Squad-hero (fighters-horsemans)'] = {
    'Fighter 5 lvl (legionary horseman-captain)':1,
    #'Fighter 4 lvl (legionary horseman-lieutenant)':1,
    #'Fighter 3 lvl (legionary horseman-sergeant)':12,
    'Fighter 2 lvl (legionary horseman-corporal)':12,
    #'Fighter 1 lvl (legionary horseman)':12,
    }

metadict_squads['Squad-hero (fighters-samurai)'] = {
    'Fighter 5 lvl (legionary slayer-captain)':1,
    #'Fighter 4 lvl (legionary slayer-lieutenant)':1,
    #'Fighter 3 lvl (legionary slayer-champion)':12,
    'Fighter 2 lvl (legionary slayer-flanker)':12,
    #'Fighter 1 lvl (legionary slayer-rookie)':12,
    }

metadict_squads['Squad-hero (fighters-shieldmans)'] = {
    'Fighter 5 lvl (legionary sentinel-captain)':1,
    #'Fighter 4 lvl (legionary sentinel-lieutenant)':1,
    #'Fighter 3 lvl (legionary sentinel-mystic)':12,
    'Fighter 2 lvl (legionary sentinel-shieldman)':12,
    #'Fighter 1 lvl (legionary sentinel-battler)':12,
    }

metadict_squads['Squad-hero (rogues)'] = {
    'Rogue 5 lvl (mercenary phantom-captain)':1,
    #'Rogue 4 lvl (mercenary phantom-lieutenant)':1,
    #'Rogue 3 lvl (mercenary phantom-deadeye)':12,
    'Rogue 2 lvl (mercenary phantom-hawkeye)':12,
    #'Rogue 1 lvl (mercenary phantom-blackeye)':12,
    }

metadict_squads['Squad-hero (rogues-arcane)'] = {
    'Rogue 3 lvl (city cat-dodger)':12,
    #'Rogue 4 lvl (city cat-runner)':1,
    'Rogue 5 lvl (city cat-mastermind)':1,
    }

metadict_squads['Squad-hero (cats-rogues)'] = {
    #'Rogue 2 lvl (city cat-meow)':12,
    'Rogue 2 lvl (city cat-meow)':6,
    'Rogue 5 lvl (city cat-mastermind)':1,
    }

metadict_squads['Squad-hero (cats-wizards)'] = {
    #'Wizard 2 lvl (city cat-weaver)':12,
    'Wizard 2 lvl (city cat-weaver)':6,
    'Wizard 5 lvl (city cat-seer)':1,
    }

metadict_squads['Squad-hero (rangers)'] = {
    'Ranger 5 lvl (otherworld wanderer-captain)':1,
    #'Ranger 4 lvl (otherworld wanderer-lieutenant)':1,
    #'Ranger 3 lvl (otherworld wanderer-hunter)':12,
    'Ranger 2 lvl (otherworld wanderer-marksman)':12,
    #'Ranger 1 lvl (otherworld wanderer-scout)':12,
    }

metadict_squads['Squad-hero (wizards)'] = {
    'Wizard 5 lvl (otherworld mage-seer)':1,
    #'Wizard 4 lvl (otherworld mage-savant)':1,
    #'Wizard 3 lvl (otherworld mage-annalist)':12,
    'Wizard 2 lvl (otherworld mage-weaver)':12,
    #'Wizard 1 lvl (otherworld mage-disciple)':12,
    }

metadict_squads['Squad-hero (druids)'] = {
    'Druid 5 lvl (otherworld terian-loremaster)':1,
    #'Druid 4 lvl (otherworld terian-wonderman)':1,
    #'Druid 3 lvl (otherworld terian-wiseman)':12,
    'Druid 2 lvl (otherworld terian-changer)':12,
    #'Druid 1 lvl (otherworld terian-forester)':12,
    }

metadict_squads['Squad-hero (sorcerers)'] = {
    'Sorcerer 5 lvl (otherworld wildfire-ravager)':1,
    #'Sorcerer 4 lvl (otherworld wildfire-paragon)':1,
    #'Sorcerer 3 lvl (otherworld wildfire-enchanter)':12,
    'Sorcerer 2 lvl (otherworld wildfire-burner)':12,
    #'Sorcerer 1 lvl (otherworld wildfire-novice)':12,
    }

metadict_squads['Squad-hero (warlocks)'] = {
    'Warlock 5 lvl (otherworld seeker-ascendant)':1,
    #'Warlock 4 lvl (otherworld seeker-envoy)':1,
    #'Warlock 3 lvl (otherworld seeker-emissary)':12,
    'Warlock 2 lvl (otherworld seeker-adept)':12,
    #'Warlock 1 lvl (otherworld seeker-follower)':12,
    }

metadict_squads['Squad-hero (clerics-life)'] = {
    'Cleric 5 lvl (city maatcarian-reviver)':1,
    #'Cleric 4 lvl (city maatcarian-arbiter)':1,
    #'Cleric 3 lvl (city maatcarian-augur)':12,
    'Cleric 2 lvl (city maatcarian-celebrant)':12,
    #'Cleric 1 lvl (city maatcarian-acolyte)':12,
    }

metadict_squads['Squad-hero (clerics-light)'] = {
    'Cleric 5 lvl (city luminary-reviver)':1,
    #'Cleric 4 lvl (city luminary-arbiter)':1,
    #'Cleric 3 lvl (city luminary-augur)':12,
    'Cleric 2 lvl (city luminary-celebrant)':12,
    #'Cleric 1 lvl (city luminary-acolyte)':12,
    }

metadict_squads['Squad-hero (bards)'] = {
    'Bard 5 lvl (otherworld singer-leader)':1,
    #'Bard 4 lvl (otherworld singer-pathfinder)':1,
    #'Bard 3 lvl (otherworld singer-explorer)':12,
    'Bard 2 lvl (otherworld singer-stranger)':12,
    #'Bard 1 lvl (otherworld singer-follower)':12,
    }

metadict_squads['Squad-hero (monks)'] = {
    'Monk 5 lvl (city windsong-warmonger)':1,
    #'Monk 4 lvl (city windsong-oathkeeper)':1,
    #'Monk 3 lvl (city windsong-lorekeeper)':12,
    'Monk 2 lvl (city windsong-gatekeeper)':12,
    #'Monk 1 lvl (city windsong-apprentice)':12,
    }

metadict_squads['Squad-hero (paladins)'] = {
    'Paladin 5 lvl (city sentry-captain)':1,
    #'Paladin 4 lvl (city sentry-lieutenant)':1,
    #'Paladin 3 lvl (city sentry-imeyer)':12,
    'Paladin 2 lvl (city sentry-weresefet)':12,
    #'Paladin 1 lvl (city sentry-sefet)':12,
    }


#----
# Герои (свиты):

metadict_squads['Band-hero (barbarians)'] = {
    #'Barbarian 5 lvl (thracian slayer-lord)':1,
    'Barbarian 4 lvl (thracian slayer-thane)':1,
    #'Barbarian 3 lvl (thracian slayer-juggernaught)':6,
    #'Barbarian 2 lvl (thracian slayer-slasher)':6,
    'Barbarian 1 lvl (thracian slayer-dogface)':6,
    }

metadict_squads['Band-hero (fighters-horsemans)'] = {
    #'Fighter 5 lvl (legionary horseman-captain)':1,
    'Fighter 4 lvl (legionary horseman-lieutenant)':1,
    #'Fighter 3 lvl (legionary horseman-sergeant)':6,
    #'Fighter 2 lvl (legionary horseman-corporal)':6,
    'Fighter 1 lvl (legionary horseman)':6,
    }

metadict_squads['Band-hero (fighters-samurai)'] = {
    #'Fighter 5 lvl (legionary slayer-captain)':1,
    'Fighter 4 lvl (legionary slayer-lieutenant)':1,
    #'Fighter 3 lvl (legionary slayer-champion)':6,
    #'Fighter 2 lvl (legionary slayer-flanker)':6,
    'Fighter 1 lvl (legionary slayer-rookie)':6,
    }

metadict_squads['Band-hero (fighters-shieldmans)'] = {
    #'Fighter 5 lvl (legionary sentinel-captain)':1,
    'Fighter 4 lvl (legionary sentinel-lieutenant)':1,
    #'Fighter 3 lvl (legionary sentinel-mystic)':6,
    #'Fighter 2 lvl (legionary sentinel-shieldman)':6,
    'Fighter 1 lvl (legionary sentinel-battler)':6,
    }

metadict_squads['Band-hero (rogues)'] = {
    #'Rogue 5 lvl (mercenary phantom-captain)':1,
    'Rogue 4 lvl (mercenary phantom-lieutenant)':1,
    #'Rogue 3 lvl (mercenary phantom-deadeye)':6,
    #'Rogue 2 lvl (mercenary phantom-hawkeye)':6,
    'Rogue 1 lvl (mercenary phantom-blackeye)':6,
    }

metadict_squads['Band-hero (rogues-arcane)'] = {
    'Rogue 4 lvl (city cat-runner)':1,
    'Rogue 2 lvl (city cat-meow)':6,
    }

metadict_squads['Band-hero (rangers)'] = {
    #'Ranger 5 lvl (otherworld wanderer-captain)':1,
    'Ranger 4 lvl (otherworld wanderer-lieutenant)':1,
    #'Ranger 3 lvl (otherworld wanderer-hunter)':6,
    #'Ranger 2 lvl (otherworld wanderer-marksman)':6,
    'Ranger 1 lvl (otherworld wanderer-scout)':6,
    }

metadict_squads['Band-hero (wizards)'] = {
    #'Wizard 5 lvl (otherworld mage-seer)':1,
    'Wizard 4 lvl (otherworld mage-savant)':1,
    #'Wizard 3 lvl (otherworld mage-annalist)':6,
    #'Wizard 2 lvl (otherworld mage-weaver)':6,
    'Wizard 1 lvl (otherworld mage-disciple)':6,
    }

metadict_squads['Band-hero (druids)'] = {
    #'Druid 5 lvl (otherworld terian-loremaster)':1,
    'Druid 4 lvl (otherworld terian-wonderman)':1,
    #'Druid 3 lvl (otherworld terian-wiseman)':6,
    #'Druid 2 lvl (otherworld terian-changer)':6,
    'Druid 1 lvl (otherworld terian-forester)':6,
    }

metadict_squads['Band-hero (sorcerers)'] = {
    #'Sorcerer 5 lvl (otherworld wildfire-ravager)':1,
    'Sorcerer 4 lvl (otherworld wildfire-paragon)':1,
    #'Sorcerer 3 lvl (otherworld wildfire-enchanter)':6,
    #'Sorcerer 2 lvl (otherworld wildfire-burner)':6,
    'Sorcerer 1 lvl (otherworld wildfire-novice)':6,
    }

metadict_squads['Band-hero (warlocks)'] = {
    #'Warlock 5 lvl (otherworld seeker-ascendant)':1,
    'Warlock 4 lvl (otherworld seeker-envoy)':1,
    #'Warlock 3 lvl (otherworld seeker-emissary)':6,
    #'Warlock 2 lvl (otherworld seeker-adept)':6,
    'Warlock 1 lvl (otherworld seeker-follower)':6,
    }

metadict_squads['Band-hero (clerics-life)'] = {
    #'Cleric 5 lvl (city maatcarian-reviver)':1,
    'Cleric 4 lvl (city maatcarian-arbiter)':1,
    #'Cleric 3 lvl (city maatcarian-augur)':6,
    #'Cleric 2 lvl (city maatcarian-celebrant)':6,
    'Cleric 1 lvl (city maatcarian-acolyte)':6,
    }

metadict_squads['Band-hero (clerics-light)'] = {
    #'Cleric 5 lvl (city luminary-reviver)':1,
    'Cleric 4 lvl (city luminary-arbiter)':1,
    #'Cleric 3 lvl (city luminary-augur)':6,
    #'Cleric 2 lvl (city luminary-celebrant)':6,
    'Cleric 1 lvl (city luminary-acolyte)':6,
    }

metadict_squads['Band-hero (bards)'] = {
    #'Bard 5 lvl (otherworld singer-leader)':1,
    'Bard 4 lvl (otherworld singer-pathfinder)':1,
    #'Bard 3 lvl (otherworld singer-explorer)':6,
    #'Bard 2 lvl (otherworld singer-stranger)':6,
    'Bard 1 lvl (otherworld singer-follower)':6,
    }

metadict_squads['Band-hero (monks)'] = {
    #'Monk 5 lvl (city windsong-warmonger)':1,
    'Monk 4 lvl (city windsong-oathkeeper)':1,
    #'Monk 3 lvl (city windsong-lorekeeper)':6,
    #'Monk 2 lvl (city windsong-gatekeeper)':6,
    'Monk 1 lvl (city windsong-apprentice)':6,
    }

metadict_squads['Band-hero (paladins)'] = {
    #'Paladin 5 lvl (city sentry-captain)':1,
    'Paladin 4 lvl (city sentry-lieutenant)':1,
    #'Paladin 3 lvl (city sentry-imeyer)':6,
    #'Paladin 2 lvl (city sentry-weresefet)':6,
    'Paladin 1 lvl (city sentry-sefet)':6,
    }

#----
# Герои (одиночки):

metadict_squads['Single-hero (barbarians)'] = {
    'Barbarian 5 lvl (thracian slayer-lord)':1,
    }

metadict_squads['Single-hero (samurai)'] = {
    'Fighter 5 lvl (legionary slayer-captain)':1,
    }

metadict_squads['Single-hero (sentinels)'] = {
    'Fighter 5 lvl (legionary sentinel-captain)':1,
    }

metadict_squads['Single-hero (horsemans)'] = {
    'Fighter 5 lvl (legionary horseman-captain)':1,
    }

metadict_squads['Single-hero (rogues)'] = {
    'Rogue 5 lvl (mercenary phantom-captain)':1,
    }

metadict_squads['Single-hero (rangers)'] = {
    'Ranger 5 lvl (otherworld wanderer-captain)':1,
    }

metadict_squads['Single-hero (wizards)'] = {
    'Wizard 5 lvl (otherworld mage-seer)':1,
    }

metadict_squads['Single-hero (druids)'] = {
    'Druid 5 lvl (otherworld terian-loremaster)':1,
    }

metadict_squads['Single-hero (sorcerers)'] = {
    'Sorcerer 5 lvl (otherworld wildfire-ravager)':1,
    }

metadict_squads['Single-hero (warlocks)'] = {
    'Warlock 5 lvl (otherworld seeker-ascendant)':1,
    }

metadict_squads['Single-hero (monks)'] = {
    'Monk 5 lvl (city windsong-warmonger)':1,
    }
