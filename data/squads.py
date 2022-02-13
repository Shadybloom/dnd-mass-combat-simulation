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
    # Чёрные флаги Ост-Индии:
        # 1 герой 5-6 lvl на 16 героев 1-2 lvl
        # 1 герой 7-8 lvl на 62 героев 1-2 lvl
        # 1 герой 9+ lvl на 250 героев 1 lvl
    # Салиф:
    # Wizard 1 lvl (otherworld mage-disciple) sum:94 STR:13 DEX:17 CON:16 INT:19 WIS:14 CHA:15
    #'Wizard 1 lvl (otherworld mage-disciple)':250,
    # Намулис:
    # Monk 1 lvl (city windsong-apprentice) sum:97 STR:16 DEX:19 CON:17 INT:14 WIS:19 CHA:12
    #'Monk 1 lvl (city windsong-apprentice)':250,
    # Зуахир:
    # Monk 1 lvl (city windsong-apprentice) sum:97 STR:16 DEX:17 CON:17 INT:14 WIS:17 CHA:16
    #'Monk 1 lvl (city windsong-apprentice)':250,
    # Вааму Лютый:
    # Monk 1 lvl (city windsong-apprentice) sum:96 STR:17 DEX:19 CON:18 INT:12 WIS:18 CHA:12
    #'Monk 1 lvl (city windsong-apprentice)':250,
    # Генри Эвери:
    # Fighter 1 lvl (legionary slayer-rookie) sum:100 STR:19 DEX:18 CON:19 INT:15 WIS:12 CHA:17
    #'Fighter 1 lvl (legionary slayer-rookie)':250,
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
    'Warrior 2 lvl (legionary infantry-siege-veteran)':10,
    'Warrior 3 lvl (legionary infantry-siege-corporal)':3,
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

# Обычные бойцы дл тестовых поединков
#----

metadict_squads['Single-regular (infantry-lieutenant)'] = {
    #'Warrior 5 lvl (legionary infantry-lieutenant)':1,
    #'Warrior 5 lvl (thracian infantry-lieutenant)':1,
    'Warrior 5 lvl (achean hoplite-lieutenant)':1,
    #'Warrior 5 lvl (grenadier line-infantry-lieutenant)':1,
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
# Тестовые отряды (Чёрные флаги Ост-Индии)

metadict_squads['Company-veteran (pirate-infantry-grenadiers)'] = {
    # Абордажная команда, палубная команда.
    'Warrior 2 lvl (grenadier line-infantry-veteran) (assault)':65,
    'Warrior 4 lvl (grenadier line-infantry-sergeant) (assault)':3,
    'Warrior 5 lvl (grenadier line-infantry-lieutenant) (assault)':3,
    'Commoner 1 lvl (recruit)':100,
    }

metadict_squads['Company-veteran (pirate-infantry-fusiliers)'] = {
    # Артиллерийская команда.
    'Warrior 2 lvl (fusilier line-infantry-veteran)':65,
    'Warrior 4 lvl (fusilier line-infantry-sergeant)':3,
    'Warrior 5 lvl (fusilier line-infantry-lieutenant)':3,
    'Commoner 1 lvl (recruit)':100,
    }

#----
# Тестовые отряды (Чёрные флаги Ост-Индии)

metadict_squads['Band-regular (black-flags) (healers)'] = {
    # Испытываем свиты героев.
    'Warrior 4 lvl (healer-sergeant)':3,
    'Warrior 5 lvl (healer-lieutenant)':1,
    'Commoner 1 lvl (recruit)':6,
    }

metadict_squads['Band-regular (black-flags) (assault, 8)'] = {
    # Испытываем свиты героев.
    'Warrior 3 lvl (grenadier line-infantry-corporal) (assault)':6,
    'Warrior 4 lvl (grenadier line-infantry-sergeant) (assault)':1,
    'Warrior 5 lvl (grenadier line-infantry-lieutenant) (assault)':1,
    'Commoner 1 lvl (recruit)':8 * 3,
    }

metadict_squads['Band-regular (black-flags) (assault, 10)'] = {
    'Warrior 3 lvl (grenadier line-infantry-corporal) (assault)':9,
    'Warrior 5 lvl (grenadier line-infantry-lieutenant) (assault)':1,
    'Commoner 1 lvl (recruit)':10 * 3,
    }

metadict_squads['Band-regular (black-flags) (snipers, 4)'] = {
    'Warrior 4 lvl (fusilier line-infantry-sergeant) (sniper)':3,
    'Warrior 5 lvl (fusilier line-infantry-lieutenant) (sniper)':1,
    'Commoner 1 lvl (recruit)':4 * 6,
    }

metadict_squads['Band-regular (black-flags) (stormtroopers, 4)'] = {
    'Warrior 4 lvl (grenadier line-infantry-sergeant) (stormtrooper)':3,
    'Warrior 5 lvl (grenadier line-infantry-lieutenant) (stormtrooper)':1,
    'Commoner 1 lvl (recruit)':4 * 6,
    }

#----
# Тестовые отряды (тестим Feats)

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
# Корабли (Чёрные флаги Ост-Индии) (фрегат):

metadict_squads['Ship frigate (верхняя палуба)'] = {
    'Ship frigate (обшивка палубы)':20,
    }

metadict_squads['Ship frigate (орудийная палуба)'] = {
    'Ship frigate (обшивка орудийной палубы)':20,
    }

metadict_squads['Ship frigate (корма)'] = {
    'Ship frigate (руль)':1,
    'Ship frigate (обшивка борта)':3,
    }

metadict_squads['Ship frigate (верхняя палуба) (левый борт)'] = {
    'Ship frigate (шпангоут)':15,
    'Ship frigate (обшивка борта)':15,
    }

metadict_squads['Ship frigate (орудийная палуба) (левый борт)'] = {
    'Ship frigate (шпангоут)':15,
    'Ship frigate (обшивка борта)':15,
    }

metadict_squads['Ship frigate (верхняя палуба) (правый борт)'] = {
    'Ship frigate (шпангоут)':15,
    'Ship frigate (обшивка борта)':15,
    }

metadict_squads['Ship frigate (орудийная палуба) (правый борт)'] = {
    'Ship frigate (шпангоут)':15,
    'Ship frigate (обшивка борта)':15,
    }

metadict_squads['Ship frigate (паруса, основные)'] = {
    # Основные паруса
    'Ship frigate (фок-брамсель)':1,
    'Ship frigate (фок-марсель)':2,
    'Ship frigate (фок)':3,
    'Ship frigate (грот-брамсель)':1,
    'Ship frigate (грот-марсель)':3,
    'Ship frigate (грот)':3,
    'Ship frigate (крюйс-брамсель)':1,
    'Ship frigate (крюйс-марсель)':1,
    'Ship frigate (крюйс)':1,
    'Ship frigate (бизань-гафель)':1,
    }

metadict_squads['Ship frigate (паруса, косые)'] = {
    # Косые паруса
    'Ship frigate (кливер)':1,
    'Ship frigate (мидель-кливер)':1,
    'Ship frigate (бом-кливер)':1,
    'Ship frigate (фока-стаксель)':1,
    'Ship frigate (грота-стаксель)':1,
    'Ship frigate (грот-стень-стаксель)':1,
    'Ship frigate (грот-брам-стень-стаксель)':1,
    'Ship frigate (апсель)':1,
    'Ship frigate (крюйс-стень-стаксель)':1,
    'Ship frigate (крюйс-брам-стень-стаксель)':1,
    }

metadict_squads['Ship frigate (рангоут)'] = {
    # Мачты
    'Ship frigate (бушприт)':1,
    'Ship frigate (фок-мачта)':1,
    'Ship frigate (грот-мачта)':1,
    'Ship frigate (бизань-мачта)':1,
    'Ship frigate (углетарь)':1,
    'Ship frigate (фор-стеньга)':1,
    'Ship frigate (грот-стеньга)':1,
    'Ship frigate (крюйс-стеньга)':1,
    'Ship frigate (фор-брам-стеньга)':1,
    'Ship frigate (грот-брам-стеньга)':1,
    'Ship frigate (крюйс-брам-стеньга)':1,
    # Реи
    'Ship frigate (фока-рей)':1,
    'Ship frigate (грота-рей)':1,
    'Ship frigate (крюйс-рей)':1,
    'Ship frigate (бегин-рей)':1,
    'Ship frigate (блинда-рей)':1,
    'Ship frigate (фор-марса-рей)':1,
    'Ship frigate (грот-марса-рей)':1,
    'Ship frigate (крюйс-марса-рей)':1,
    'Ship frigate (бом-блинда-рей)':1,
    'Ship frigate (фор-брам-рей)':1,
    'Ship frigate (грот-брам-рей)':1,
    'Ship frigate (крюйс-брам-рей)':1,
    }

#----
# Корабли (Чёрные флаги Ост-Индии) (шлюп):

metadict_squads['Ship sloop (верхняя палуба) (борт)'] = {
    'Ship sloop (шпангоут)':9,
    'Ship sloop (обшивка борта)':9,
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
    'Warlock 2 lvl (гневнорожка Козы)':80,
    'Warlock 3 lvl (главнорожка Козы)':10,
    'Warlock 3 lvl (Сефо Форонейская)':1,
    }

#----
# Призванные существа:

metadict_squads['Company-summon (мастиффы)'] = {
    # Призванные собаки:
    'Mastiff, dog (CR 1/8)':96,
    }

metadict_squads['Squad-summon (оживлённые вещи)'] = {
    # Заклинание 5 круга "Оживление вещей" (Animated_Objects)
    'Animated swords (CR 1)':10,
    }

metadict_squads['Squad-summon (гигантские осьминоги)'] = {
    'Giant Octopus (CR 1)':12,
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

metadict_squads['Single-summon (меч Морденкайнена)'] = {
    'Mordenkainen Sword (CR 10)':1,
    }

metadict_squads['Single-summon (Force Ballista)'] = {
    'Eldritch Cannon (force ballista)':1,
    }

metadict_squads['Single-summon (земляной элементаль)'] = {
    'Earth Elemental (CR 5)':1,
    }

metadict_squads['Single-summon (воздушный элементаль)'] = {
    'Air Elemental (CR 5)':1,
    }

#-------------------------------------------------------------------------
# Армии и герои

#----
# Свита Кироса:

metadict_squads['Squad-hero (бойцы Кироса) (нейтрал)'] = {
    'Fighter 4 lvl (боец Кироса)':16,
    'Fighter 13 lvl (Кирос «Симарх»)':1,
    }

metadict_squads['Single-hero (боец Кироса) (нейтрал)'] = {
    'Fighter 4 lvl (боец Кироса)':1,
    }

metadict_squads['Single-hero (лично Кирос) (нейтрал)'] = {
    'Fighter 13 lvl (Кирос «Симарх»)':1,
    }

#----
# Армия Кироса:

#----
# Свита Менона:

metadict_squads['Squad-hero (волшебники Менона) (нейтрал)'] = {
    'Wizard 4 lvl (волшебник Менона)':14,
    'Wizard 12 lvl (Менон Теварин)':1,
    }

metadict_squads['Band-hero (волшебники Менона) (нейтрал)'] = {
    'Wizard 4 lvl (волшебник Менона)':2,
    }

metadict_squads['Single-hero (волшебник Менона) (нейтрал)'] = {
    'Wizard 4 lvl (волшебник Менона)':1,
    }

metadict_squads['Single-hero (лично Менон) (нейтрал)'] = {
    'Wizard 12 lvl (Менон Теварин)':1,
    }

metadict_squads['Single-hero (симулякр Менона) (нейтрал)'] = {
    'Wizard 12 lvl (симулякр Менона)':1,
    }

#----
# Армия Менона:

metadict_squads['Squad-hero (бронзовые гоплиты Менона) (нейтрал)'] = {
    'Warrior 4 lvl (бронзовый гоплит Менона)':15,
    'Warrior 5 lvl (бронзовый гоплит-капитан Менона)':5,
    }

metadict_squads['Company-hero (бронзовые гоплиты Менона) (нейтрал)'] = {
    # Всего у Менона 110 бронзовых гоплитов:
    'Warrior 4 lvl (бронзовый гоплит Менона)':67,
    'Warrior 5 lvl (бронзовый гоплит-капитан Менона)':25,
    }

metadict_squads['Squad-hero (зомби и гоплиты Менона) (нейтрал)'] = {
    'Warrior 4 lvl (бронзовый гоплит Менона)':10,
    'Warrior 5 lvl (бронзовый гоплит-капитан Менона)':4,
    #'Zombie (CR 1/4)':80 + dice_throw('1d12'),
    'Zombie (Danse_Macabre) (CR 1/2)':60,
    }

metadict_squads['Squad-hero (60 зомби Менона) (нейтрал)'] = {
    # Зомби под Danse_Macabre с +5 атаки и +9 урона.
    'Zombie (Danse_Macabre) (CR 1/2)':60,
    'Warrior 4 lvl (бронзовый гоплит Менона)':3,
    'Warrior 5 lvl (бронзовый гоплит-капитан Менона)':1,
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
    'Barbarian 9 lvl (Карагос «Мудрый»)':1,
    }

#----
# Армия Карагоса:

metadict_squads['Company-regular (пираты Карагоса) (нейтрал)'] = {
    'Warrior 1 lvl (пират Карагоса)':70 + dice_throw('1d12'),
    'Warrior 2 lvl (ветеран Карагоса)':20,
    'Warrior 3 lvl (сержант Карагоса)':6,
    'Warrior 4 lvl (лейтенант Карагоса)':2,
    'Warrior 5 lvl (капитан Карагоса)':1,
    }

metadict_squads['Company-veteran (ветераны Карагоса) (нейтрал)'] = {
    # Опытный отряд с двумя капитанами
    'Warrior 2 lvl (ветеран Карагоса)':85 + dice_throw('1d12'),
    'Warrior 3 lvl (сержант Карагоса)':6,
    'Warrior 5 lvl (капитан Карагоса)':2,
    'Warrior 4 lvl (лейтенант Карагоса)':2,
    }

#----
# Свита Акхена Ваджета:

metadict_squads['Squad-hero (варвары Радаманта) (враг)'] = {
    'Barbarian 2 lvl (варвар Радаманта)':9,
    'Barbarian 5 lvl (Радамант «Бдительный»)':1,
    }

#----
# Армия Акхена Ваджета:

metadict_squads['Company-regular (легионеры Акхена) (враг)'] = {
    'Warrior 1 lvl (легионер Акхена)':80 + dice_throw('1d12'),
    'Warrior 2 lvl (ветеран Акхена)':10,
    'Warrior 3 lvl (сержант Акхена)':3,
    'Warrior 5 lvl (капитан Акхена)':1,
    'Warrior 4 lvl (лейтенант Акхена)':1,
    }

#----
# Свита Чары:

metadict_squads['Squad-hero (колдуны Чары) (враг)'] = {
    'Warlock 3 lvl (колдун Чары)':16,
    'Warlock 11 lvl (Чара Атенак)':1,
    }

metadict_squads['Squad-hero (колдун Чары) (враг)'] = {
    'Warlock 3 lvl (колдун Чары)':1,
    }

metadict_squads['Squad-hero (лично Чара) (враг)'] = {
    'Warlock 11 lvl (Чара Атенак)':1,
    }

#----
# Армия Чары:

metadict_squads['Company-regular (мирмидоны Чары) (враг)'] = {
    'Warrior 1 lvl (мирмидон)':180 + dice_throw('1d12'),
    'Warrior 2 lvl (мирмидон-ветеран)':10,
    'Warrior 3 lvl (мирмидон-сержант)':3,
    'Warrior 5 lvl (мирмидон-капитан)':1,
    'Warrior 4 lvl (мирмидон-лейтенант)':1,
    }

metadict_squads['Company-regular (тяжёлые баллисты Чары) (друг)'] = {
    'Warrior 2 lvl (siege engineer-apprentice) (ballista-siege)':10,
    'Warrior 4 lvl (siege engineer-master)':1,
    }

#----
# Армия Ашеры:

metadict_squads['Company-regular (демоны Ашеры) (враг)'] = {
    'Warrior 1 lvl (демон-рядовой)':180 + dice_throw('1d12'),
    'Warrior 2 lvl (демон-ветеран)':10,
    'Warrior 3 lvl (демон-сержант)':3,
    'Warrior 5 lvl (демон-капитан)':1,
    'Warrior 4 lvl (демон-лейтенант)':1,
    }

metadict_squads['Company-regular (карлы Ашеры) (враг)'] = {
    'Commoner 1 lvl (карл)':180 + dice_throw('3d12'),
    'Commoner 1 lvl (карл-ветеран)':4,
    'Warrior 3 lvl (демон-сержант)':1,
    }

#----
# Свита Тинв:

metadict_squads['Squad-hero (кошки Тинв) (друг)'] = {
    # TODO:
    # Её телохранитель Ри всегда рядом.
    # Половина свиты -- мистические ловкачи Ри.
    'Wizard 3 lvl (кошка Тинв)':12,
    'Wizard 9 lvl (Тинв)':1,
    }

metadict_squads['Squad-hero (кошки Тави) (друг)'] = {
    'Wizard 2 lvl (кошка Тави)':10,
    'Wizard 7 lvl (Тави)':1,
    }

#----
# Армия Тинв:

metadict_squads['Company-elite (гвардия Тави) (друг)'] = {
    'Warrior 2 lvl (ветеран Тави)':60,
    'Warrior 3 lvl (сержант Тави)':18,
    'Warrior 4 lvl (лейтенант Тави)':6,
    'Warrior 5 lvl (капитан Тави)':6,
    'Commoner 1 lvl (recruit)':500,
    }

#----
# Свита Крассиуса:

#----
# Армия Крассиуса:

metadict_squads['Company-hero (арбалетчики Тетры) (друг)'] = {
    # в отряде два капитана и +3 лейтенанта
    'Warrior 1 lvl (арбалетчик Тетры)':80 + dice_throw('1d12'),
    'Warrior 2 lvl (арбалетчик-ветеран Тетры)':10,
    'Warrior 3 lvl (арбалетчик-сержант Тетры)':3,
    'Warrior 4 lvl (арбалетчик-лейтенант Тетры)':4,
    'Warrior 5 lvl (арбалетчик-капитан Тетры)':2,
    }

#----
# Свита Кумара

metadict_squads['Squad-hero (монахи Кумара) (друг)'] = {
    # Свита из 13 монахов-теневиков. "Верные ученики".
    'Monk 9 lvl (Кумар «Чугуннорукий»)':1,
    'Monk 3 lvl (монах Кумара)':13,
    }

metadict_squads['Single-hero (лично Кумар) (друг)'] = {
    'Monk 9 lvl (Кумар «Чугуннорукий»)':1,
    }

#----
# Армия Кумара

metadict_squads['Company-militia (пращники Илиона) (друг)'] = {
    # Свинцовые снаряды
    'Commoner 1 lvl (пращник Илиона)':80 + dice_throw('3d12'),
    'Commoner 2 lvl (ветеран пращников Илиона)':5,
    'Warrior 3 lvl (сержант пращников Илиона)':1,
    }

metadict_squads['Company-regular (легионеры Илиона) (друг)'] = {
    # Огненные копья
    'Warrior 1 lvl (легионер Илиона)':80 + dice_throw('1d12'),
    'Warrior 2 lvl (ветеран Илиона)':10,
    'Warrior 3 lvl (сержант Илиона)':3,
    'Warrior 5 lvl (капитан Илиона)':1,
    'Warrior 4 lvl (лейтенант Илиона)':1,
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
    'Commoner 1 lvl (сатир-охотник)':95,
    'Commoner 2 lvl (сатир-ветеран)':5,
    'Warrior 3 lvl (сатир-сержант)':1,
    }

metadict_squads['Company-militia (сатиры Павсания, сына Павсания) (друг)'] = {
    'Commoner 1 lvl (сатир-охотник)':95,
    'Commoner 2 lvl (сатир-ветеран)':5,
    'Warrior 4 lvl (сын Павсания)':1,
    'Warrior 3 lvl (сатир-сержант)':1,
    }

metadict_squads['Company-regular (легионеры мостовика Отто) (друг)'] = {
    # Сам Отто бежал с Фарамом, отряд остался оборонять мост.
    'Warrior 1 lvl (legionary infantry)':80 + dice_throw('1d12'),
    'Warrior 2 lvl (legionary infantry-veteran)':10,
    'Warrior 3 lvl (legionary infantry-corporal)':3,
    'Warrior 4 lvl (legionary infantry-sergeant)':1,
    #'Warrior 5 lvl (legionary infantry-lieutenant)':1,
    }

#----
# Враги (битва за Лемнос):

metadict_squads['Band-hero (колдуны Кара\'Яма) (враг)'] = {
    # Кара'Яма сожрали буреспрайты, отряд разбит и продан в рабство.
    'Warlock 5 lvl (Кара\'Ям)':1,
    'Warlock 1 lvl (колдун Кара\'Яма)':12,
    }

#metadict_squads['Band-hero (колдуны Кема\'Эша) (враг)'] = {
#    'Warlock 5 lvl (Кема\'Эш)':1,
#    'Warlock 1 lvl (колдун Кема\'Эша)':6,
#    }

metadict_squads['Band-hero (следопыты Энзифа) (враг)'] = {
    # Захвачен Гаем Юлием
    'Ranger 5 lvl (Энзиф «Ходи-гора»)':1,
    'Ranger 1 lvl (следопыт Энзифа)':12,
    }

metadict_squads['Band-hero (паладины Магора) (враг)'] = {
    # Побеждён кентурией Марселлия и Патроклом
    'Paladin 5 lvl (Магор «Детоед»)':1,
    'Paladin 1 lvl (паладин Магора)':6,
    }

metadict_squads['Band-hero (снайперы Хана-Вама) (враг)'] = {
    # Взяты в плен Фарамом
    # "Верные ученики" и "Многочисленная свита"
    'Fighter 5 lvl (Хана\'Вам)':1,
    'Fighter 1 lvl (снайпер Хана\'Вама)':12,
    }

metadict_squads['Band-hero (друиды Тик-Бо) (враг)'] = {
    # Сбежали. Сдались Сакатру.
    'Druid 5 lvl (Тик-Бо «Робкий»)':1,
    'Druid 1 lvl (друид Тик-Бо)':6,
    #'Giant Octopus (conjured) (CR 1)':12,
    }

metadict_squads['Company-militia (демоны Кема\'Эша) (враг)'] = {
    # Выбиты Агатой и отрядом Аксиотеи:
    'Commoner 1 lvl (карл)':80,
    'Commoner 1 lvl (карл-ветеран)':4,
    'Warrior 3 lvl (демон Кема\'Эша)':1,
    }

metadict_squads['Company-regular (лучники Энзифа) (враг)'] = {
    # Побеждены Гаем Юлием и сатирами Павсания.
    'Warrior 1 lvl (sqythian bowman)':185,
    'Warrior 2 lvl (sqythian bowman-veteran)':10,
    'Warrior 3 lvl (sqythian bowman-corporal)':3,
    'Warrior 4 lvl (sqythian bowman-sergeant)':1,
    }

metadict_squads['Company-regular (сариссофоры Магора) (враг)'] = {
    # Побеждены Патроклом и кентурией Марселлия
    'Warrior 1 lvl (city pikeman)':75,
    'Warrior 2 lvl (city pikeman-veteran)':20,
    'Warrior 3 lvl (city pikeman-corporal)':6,
    'Warrior 4 lvl (city pikeman-sergeant)':2,
    }

metadict_squads['Company-regular (лучники Хана-Вама) (враг)'] = {
    # Уничтожены Подводной стражей Психеи
    'Warrior 1 lvl (sqythian bowman)':75,
    'Warrior 2 lvl (sqythian bowman-veteran)':10,
    'Warrior 3 lvl (sqythian bowman-corporal)':3,
    'Warrior 4 lvl (sqythian bowman-sergeant)':1,
    'Warrior 5 lvl (sqythian bowman-lieutenant)':1,
    }

metadict_squads['Company-regular (пираты Кара-Яма) (конные) (враг)'] = {
    # Взяты в плен Фарамом
    'Warrior 1 lvl (cavalry archer)':6,
    'Warrior 2 lvl (cavalry archer-veteran)':10,
    'Warrior 3 lvl (cavalry archer-corporal)':3,
    'Warrior 4 lvl (cavalry archer-sergeant)':1,
    }

metadict_squads['Company-regular (пираты Кара-Яма) (пешие) (враг)'] = {
    # Взяты в плен Патроклом в битве за корабли.
    # Лучшие в конном отряде.
    'Warrior 1 lvl (cilician infantry)':70,
    'Warrior 3 lvl (cilician infantry-corporal)':1,
    }

metadict_squads['Company-regular (пираты Кема-Эша) (враг)'] = {
    # Сбежали, пострадали от дактилей, сдались Сакатру.
    'Warrior 1 lvl (cilician infantry)':75,
    'Warrior 2 lvl (cilician infantry-veteran)':10,
    'Warrior 3 lvl (cilician infantry-corporal)':3,
    'Warrior 4 lvl (cilician infantry-sergeant)':1,
    }

metadict_squads['Company-regular (пращники Тик-Бо) (враг)'] = {
    # Сбежали, пострадали от дактилей, сдались Сакатру.
    'Warrior 1 lvl (balear slinger)':75,
    'Warrior 2 lvl (balear slinger-veteran)':10,
    'Warrior 3 lvl (balear slinger-corporal)':3,
    'Warrior 4 lvl (balear slinger-sergeant)':1,
    }

#----
# Армия Нингиримы:

metadict_squads['Company-veteran (гоплиты Нингиримы) (враг)'] = {
    # Опытный отряд.
    'Warrior 1 lvl (гоплит Нингиримы)':46 + dice_throw('1d12'),
    'Warrior 2 lvl (гоплит-ветеран Нингиримы)':46,
    'Warrior 3 lvl (гоплит-сержант Нингиримы)':3,
    'Warrior 5 lvl (гоплит-капитан Нингиримы)':2,
    'Warrior 4 lvl (гоплит-лейтенант Нингиримы)':1,
    'Commoner 1 lvl (recruit)':100,
    }

metadict_squads['Company-veteran (гоплиты Клеомена) (враг)'] = {
    # Опытный отряд.
    'Warrior 2 lvl (гоплит-ветеран Нингиримы)':90,
    'Warrior 3 lvl (гоплит-сержант Нингиримы)':6,
    'Warrior 5 lvl (гоплит-капитан Нингиримы)':2,
    'Warrior 4 lvl (гоплит-лейтенант Нингиримы)':2,
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
    'Commoner 2 lvl (militia slinger-veteran)':5,
    'Warrior 3 lvl (militia slinger-corporal)':1,
    }

metadict_squads['Squad-hero (колдуны Кема\'Эша) (друг)'] = {
    'Warlock 6 lvl (Кема\'Эш «Ловкач»)':1,
    'Warlock 2 lvl (колдун Кема\'Эша)':10,
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
    'Commoner 2 lvl (militia spearman-veteran)':5,
    'Warrior 3 lvl (militia spearman-corporal)':1,
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
    'Bard 2 lvl (бард Тетры)':10,
    'Bard 6 lvl (Тетра Курио)':1,
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
    'Commoner 2 lvl (militia heavy crossbowman-veteran)':5,
    'Warrior 3 lvl (militia heavy crossbowman-corporal)':1,
    }

metadict_squads['Company-militia (арбалетчики Патрокла) (Vened)'] = {
    'Commoner 1 lvl (militia crossbowman)':80 + dice_throw('3d12'),
    'Commoner 2 lvl (militia crossbowman-veteran)':5,
    'Warrior 3 lvl (militia crossbowman-corporal)':1,
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
    'Commoner 2 lvl (militia javeliner-veteran)':5,
    'Warrior 3 lvl (militia javeliner-corporal)':2,
    'Warrior 4 lvl (militia javeliner-sergeant)':1,
    }

metadict_squads['Company-militia (infantry-spearmans)'] = {
    'Commoner 1 lvl (militia spearman)':80 + dice_throw('3d12'),
    'Commoner 2 lvl (militia spearman-veteran)':5,
    'Warrior 3 lvl (militia spearman-corporal)':2,
    'Warrior 4 lvl (militia spearman-sergeant)':1,
    }

metadict_squads['Company-militia (infantry-swordsmans)'] = {
    'Commoner 1 lvl (militia swordsman)':80 + dice_throw('3d12'),
    'Commoner 2 lvl (militia swordsman-veteran)':5,
    'Warrior 3 lvl (militia swordsman-corporal)':2,
    'Warrior 4 lvl (militia swordsman-sergeant)':1,
    }

metadict_squads['Company-militia (skirmisher-slingers)'] = {
    'Commoner 1 lvl (militia slinger)':80 + dice_throw('3d12'),
    'Commoner 2 lvl (militia slinger-veteran)':5,
    'Warrior 3 lvl (militia slinger-corporal)':2,
    'Warrior 4 lvl (militia slinger-sergeant)':1,
    }

metadict_squads['Company-militia (bowmans-hunters)'] = {
    'Commoner 1 lvl (militia bowman)':80 + dice_throw('3d12'),
    'Commoner 2 lvl (militia bowman-veteran)':5,
    'Warrior 3 lvl (militia bowman-corporal)':2,
    'Warrior 4 lvl (militia bowman-sergeant)':1,
    }

metadict_squads['Company-militia (crossbowmans)'] = {
    'Commoner 1 lvl (militia crossbowman)':80 + dice_throw('3d12'),
    'Commoner 2 lvl (militia crossbowman-veteran)':5,
    'Warrior 3 lvl (militia crossbowman-corporal)':2,
    'Warrior 4 lvl (militia crossbowman-sergeant)':1,
    }

metadict_squads['Company-militia (heavy crossbowmans)'] = {
    'Commoner 1 lvl (militia heavy crossbowman)':80 + dice_throw('3d12'),
    'Commoner 2 lvl (militia heavy crossbowman-veteran)':5,
    'Warrior 3 lvl (militia heavy crossbowman-corporal)':2,
    'Warrior 4 lvl (militia heavy crossbowman-sergeant)':1,
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
    'Warrior 2 lvl (achean hoplite-veteran)':10,
    'Warrior 3 lvl (achean hoplite-corporal)':3,
    'Warrior 4 lvl (achean hoplite-sergeant)':1,
    'Warrior 5 lvl (achean hoplite-lieutenant)':1,
    }

metadict_squads['Company-regular (infantry-legionary)'] = {
    # Распределение опыта по уровням:
        # 2 lvl -- 300 * 10 = 3000
        # 3 lvl -- 1200 * 3 = 3600
        # 4 lvl -- 3900 * 1 = 3900
    # Всего около 10 500 опыта (как у героя 5 lvl)
        # 5 lvl -- 10400 * 1 = 10 400
    'Warrior 1 lvl (legionary infantry)':80 + dice_throw('1d12'),
    'Warrior 2 lvl (legionary infantry-veteran)':10,
    'Warrior 3 lvl (legionary infantry-corporal)':3,
    'Warrior 4 lvl (legionary infantry-sergeant)':1,
    'Warrior 5 lvl (legionary infantry-lieutenant)':1,
    }

metadict_squads['Company-regular (infantry-pikemans)'] = {
    'Warrior 1 lvl (city pikeman)':80 + dice_throw('1d12'),
    'Warrior 2 lvl (city pikeman-veteran)':10,
    'Warrior 3 lvl (city pikeman-corporal)':3,
    'Warrior 4 lvl (city pikeman-sergeant)':1,
    'Warrior 5 lvl (city pikeman-lieutenant)':1,
    }

metadict_squads['Company-regular (infantry-thracian)'] = {
    'Warrior 1 lvl (thracian infantry)':80 + dice_throw('1d12'),
    'Warrior 2 lvl (thracian infantry-veteran)':10,
    'Warrior 3 lvl (thracian infantry-corporal)':3,
    'Warrior 4 lvl (thracian infantry-sergeant)':1,
    'Warrior 5 lvl (thracian infantry-lieutenant)':1,
    }

metadict_squads['Company-regular (infantry-cilician)'] = {
    'Warrior 1 lvl (cilician infantry)':80 + dice_throw('1d12'),
    'Warrior 2 lvl (cilician infantry-veteran)':10,
    'Warrior 3 lvl (cilician infantry-corporal)':3,
    'Warrior 4 lvl (cilician infantry-sergeant)':1,
    'Warrior 5 lvl (cilician infantry-lieutenant)':1,
    }

metadict_squads['Company-regular (bowmans-scythian)'] = {
    'Warrior 1 lvl (sqythian bowman)':80 + dice_throw('1d12'),
    'Warrior 2 lvl (sqythian bowman-veteran)':10,
    'Warrior 3 lvl (sqythian bowman-corporal)':3,
    'Warrior 4 lvl (sqythian bowman-sergeant)':1,
    'Warrior 5 lvl (sqythian bowman-lieutenant)':1,
    }

#----
# Регулярная армия (огнестрел):

metadict_squads['Company-regular (line-infantry-musketeers)'] = {
    'Warrior 1 lvl (musketeer line-infantry)':80 + dice_throw('1d12'),
    'Warrior 2 lvl (musketeer line-infantry-veteran)':10,
    'Warrior 3 lvl (musketeer line-infantry-corporal)':3,
    'Warrior 4 lvl (musketeer line-infantry-sergeant)':1,
    'Warrior 5 lvl (musketeer line-infantry-lieutenant)':1,
    }

metadict_squads['Company-regular (line-infantry-grenadiers)'] = {
    'Warrior 1 lvl (grenadier line-infantry)':80 + dice_throw('1d12'),
    'Warrior 2 lvl (grenadier line-infantry-veteran)':10,
    'Warrior 3 lvl (grenadier line-infantry-corporal)':3,
    'Warrior 4 lvl (grenadier line-infantry-sergeant)':1,
    'Warrior 5 lvl (grenadier line-infantry-lieutenant)':1,
    }

metadict_squads['Company-regular (line-infantry-bombardiers)'] = {
    'Warrior 1 lvl (bombardier line-infantry)':80 + dice_throw('1d12'),
    'Warrior 2 lvl (bombardier line-infantry-veteran)':10,
    'Warrior 3 lvl (bombardier line-infantry-corporal)':3,
    'Warrior 4 lvl (bombardier line-infantry-sergeant)':1,
    'Warrior 5 lvl (bombardier line-infantry-lieutenant)':1,
    }

metadict_squads['Company-regular (line-infantry-fusiliers)'] = {
    'Warrior 1 lvl (fusilier line-infantry)':80 + dice_throw('1d12'),
    'Warrior 2 lvl (fusilier line-infantry-veteran)':10,
    'Warrior 3 lvl (fusilier line-infantry-corporal)':3,
    'Warrior 4 lvl (fusilier line-infantry-sergeant)':1,
    'Warrior 5 lvl (fusilier line-infantry-lieutenant)':1,
    }

#----
# Регулярная армия:

#metadict_squads['Company-regular (infantry-polearms)'] = {
#    'Warrior 1 lvl (mercenary heavy-infantry)':80 + dice_throw('1d12'),
#    'Warrior 2 lvl (mercenary heavy-infantry-veteran)':10,
#    'Warrior 3 lvl (mercenary heavy-infantry-corporal)':3,
#    'Warrior 4 lvl (mercenary heavy-infantry-sergeant)':1,
#    'Warrior 5 lvl (mercenary heavy-infantry-lieutenant)':1,
#    }

#metadict_squads['Company-regular (infantry-shekelesh)'] = {
#    'Warrior 1 lvl (shekelesh infantry)':80 + dice_throw('1d12'),
#    'Warrior 2 lvl (shekelesh infantry-veteran)':10,
#    'Warrior 3 lvl (shekelesh infantry-corporal)':3,
#    'Warrior 4 lvl (shekelesh infantry-sergeant)':1,
#    'Warrior 5 lvl (shekelesh infantry-lieutenant)':1,
#    }
#
#metadict_squads['Company-regular (infantry-celtian)'] = {
#    'Warrior 1 lvl (celtian infantry)':80 + dice_throw('1d12'),
#    'Warrior 2 lvl (celtian infantry-veteran)':10,
#    'Warrior 3 lvl (celtian infantry-corporal)':3,
#    'Warrior 4 lvl (celtian infantry-sergeant)':1,
#    'Warrior 5 lvl (celtian infantry-lieutenant)':1,
#    }
#

#metadict_squads['Company-regular (bowmans-persian)'] = {
#    'Warrior 1 lvl (persian bowman)':80 + dice_throw('1d12'),
#    'Warrior 2 lvl (persian bowman-veteran)':10,
#    'Warrior 3 lvl (persian bowman-corporal)':3,
#    'Warrior 4 lvl (persian bowman-sergeant)':1,
#    'Warrior 5 lvl (persian bowman-lieutenant)':1,
#    }

#metadict_squads['Company-regular (slingers-balear)'] = {
#    'Warrior 1 lvl (balear slinger)':80 + dice_throw('1d12'),
#    'Warrior 2 lvl (balear slinger-veteran)':10,
#    'Warrior 3 lvl (balear slinger-corporal)':3,
#    'Warrior 4 lvl (balear slinger-sergeant)':1,
#    'Warrior 5 lvl (balear slinger-lieutenant)':1,
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
#    'Warrior 2 lvl (achean hoplite-veteran)':44,
#    'Warrior 3 lvl (achean hoplite-corporal)':3,
#    'Warrior 4 lvl (achean hoplite-sergeant)':1,
#    'Warrior 5 lvl (achean hoplite-lieutenant)':2,
#    'Commoner 1 lvl (recruit)':100,
#    }
#
#metadict_squads['Company-veteran (infantry-legionary)'] = {
#    # Fighting_Style_Protection
#    'Warrior 1 lvl (legionary infantry)':46 + dice_throw('1d12'),
#    'Warrior 2 lvl (legionary infantry-veteran)':44,
#    'Warrior 3 lvl (legionary infantry-corporal)':3,
#    'Warrior 4 lvl (legionary infantry-sergeant)':1,
#    'Warrior 5 lvl (legionary infantry-lieutenant)':2,
#    'Commoner 1 lvl (recruit)':100,
#    }
#
#metadict_squads['Company-veteran (infantry-pikemans)'] = {
#    # Fighting_Style_Defence
#    'Warrior 1 lvl (city pikeman)':46 + dice_throw('1d12'),
#    'Warrior 2 lvl (city pikeman-veteran)':44,
#    'Warrior 3 lvl (city pikeman-corporal)':3,
#    'Warrior 4 lvl (city pikeman-sergeant)':1,
#    'Warrior 5 lvl (city pikeman-lieutenant)':2,
#    'Commoner 1 lvl (recruit)':100,
#    }
#
#metadict_squads['Company-veteran (infantry-thracian)'] = {
#    # Fighting_Style_Great_Weapon_Fighting
#    'Warrior 1 lvl (thracian infantry)':46 + dice_throw('1d12'),
#    'Warrior 2 lvl (thracian infantry-veteran)':44,
#    'Warrior 3 lvl (thracian infantry-corporal)':3,
#    'Warrior 4 lvl (thracian infantry-sergeant)':1,
#    'Warrior 5 lvl (thracian infantry-lieutenant)':2,
#    'Commoner 1 lvl (recruit)':100,
#    }
#
#metadict_squads['Company-veteran (infantry-cilician)'] = {
#    # Fighting_Style_Two_Weapon_Fighting
#    'Warrior 1 lvl (cilician infantry)':46 + dice_throw('1d12'),
#    'Warrior 2 lvl (cilician infantry-veteran)':44,
#    'Warrior 3 lvl (cilician infantry-corporal)':3,
#    'Warrior 4 lvl (cilician infantry-sergeant)':1,
#    'Warrior 5 lvl (cilician infantry-lieutenant)':2,
#    'Commoner 1 lvl (recruit)':100,
#    }
#
#metadict_squads['Company-veteran (bowmans-scythian)'] = {
#    # Fighting_Style_Archery
#    'Warrior 1 lvl (sqythian bowman)':46 + dice_throw('1d12'),
#    'Warrior 2 lvl (sqythian bowman-veteran)':44,
#    'Warrior 3 lvl (sqythian bowman-corporal)':3,
#    'Warrior 4 lvl (sqythian bowman-sergeant)':1,
#    'Warrior 5 lvl (sqythian bowman-lieutenant)':2,
#    'Commoner 1 lvl (recruit)':100,
#    }

#----
# Ветеранские отряды:

metadict_squads['Company-veteran (infantry-hoplites)'] = {
    # Отряд героя 7 lvl
    # Шесть капитанов и 62 400 exp на отряд.
    # Отборный отряд (сумма параметров 63+) -- 200 рекрутов на 100 солдат
    'Warrior 2 lvl (achean hoplite-veteran)':60,
    'Warrior 3 lvl (achean hoplite-corporal)':18,
    'Warrior 4 lvl (achean hoplite-sergeant)':6,
    'Warrior 5 lvl (achean hoplite-lieutenant)':6,
    'Commoner 1 lvl (recruit)':100,
    }

metadict_squads['Company-veteran (infantry-legionary)'] = {
    'Warrior 2 lvl (legionary infantry-veteran)':60,
    'Warrior 3 lvl (legionary infantry-corporal)':18,
    'Warrior 4 lvl (legionary infantry-sergeant)':6,
    'Warrior 5 lvl (legionary infantry-lieutenant)':6,
    'Commoner 1 lvl (recruit)':100,
    }

metadict_squads['Company-veteran (infantry-pikemans)'] = {
    'Warrior 2 lvl (city pikeman-veteran)':60,
    'Warrior 3 lvl (city pikeman-corporal)':18,
    'Warrior 4 lvl (city pikeman-sergeant)':6,
    'Warrior 5 lvl (city pikeman-lieutenant)':6,
    'Commoner 1 lvl (recruit)':100,
    }

metadict_squads['Company-veteran (infantry-thracian)'] = {
    'Warrior 2 lvl (thracian infantry-veteran)':60,
    'Warrior 3 lvl (thracian infantry-corporal)':18,
    'Warrior 4 lvl (thracian infantry-sergeant)':6,
    'Warrior 5 lvl (thracian infantry-lieutenant)':6,
    'Commoner 1 lvl (recruit)':100,
    }

metadict_squads['Company-veteran (infantry-cilician)'] = {
    'Warrior 2 lvl (cilician infantry-veteran)':60,
    'Warrior 3 lvl (cilician infantry-corporal)':18,
    'Warrior 4 lvl (cilician infantry-sergeant)':6,
    'Warrior 5 lvl (cilician infantry-lieutenant)':6,
    'Commoner 1 lvl (recruit)':100,
    }

metadict_squads['Company-veteran (bowmans-scythian)'] = {
    'Warrior 2 lvl (sqythian bowman-veteran)':60,
    'Warrior 3 lvl (sqythian bowman-corporal)':18,
    'Warrior 4 lvl (sqythian bowman-sergeant)':6,
    'Warrior 5 lvl (sqythian bowman-lieutenant)':6,
    'Commoner 1 lvl (recruit)':100,
    }

metadict_squads['Company-veteran (line-infantry-musketeers)'] = {
    'Warrior 2 lvl (musketeer line-infantry-veteran)':60,
    'Warrior 3 lvl (musketeer line-infantry-corporal)':18,
    'Warrior 4 lvl (musketeer line-infantry-sergeant)':6,
    'Warrior 5 lvl (musketeer line-infantry-lieutenant)':6,
    'Commoner 1 lvl (recruit)':100,
    }

metadict_squads['Company-veteran (line-infantry-fusiliers)'] = {
    'Warrior 2 lvl (fusilier line-infantry-veteran)':60,
    'Warrior 3 lvl (fusilier line-infantry-corporal)':18,
    'Warrior 4 lvl (fusilier line-infantry-sergeant)':6,
    'Warrior 5 lvl (fusilier line-infantry-lieutenant)':6,
    'Commoner 1 lvl (recruit)':100,
    }

metadict_squads['Company-veteran (line-infantry-grenadiers)'] = {
    'Warrior 2 lvl (grenadier line-infantry-veteran)':60,
    'Warrior 3 lvl (grenadier line-infantry-corporal)':18,
    'Warrior 4 lvl (grenadier line-infantry-sergeant)':6,
    'Warrior 5 lvl (grenadier line-infantry-lieutenant)':6,
    'Commoner 1 lvl (recruit)':100,
    }

metadict_squads['Company-veteran (line-infantry-bombardiers)'] = {
    'Warrior 2 lvl (bombardier line-infantry-veteran)':60,
    'Warrior 3 lvl (bombardier line-infantry-corporal)':18,
    'Warrior 4 lvl (bombardier line-infantry-sergeant)':6,
    'Warrior 5 lvl (bombardier line-infantry-lieutenant) (bomba-san)':5,
    'Warrior 5 lvl (bombardier line-infantry-lieutenant) (shaitan-tube)':1,
    'Commoner 1 lvl (recruit)':100,
    }

#----
# Ветеранские отряды (артиллерия):

metadict_squads['Company-veteran (cannoneer artillery-battery) (6-lb Cannons)'] = {
    # Полковая батарея, 8 орудий, 96 бойцов в расчётах.
    'Warrior 1 lvl (cannoneer artillery)':30,
    'Warrior 2 lvl (cannoneer artillery-veteran)':60,
    'Warrior 3 lvl (cannoneer artillery-corporal)':10,
    'Warrior 4 lvl (cannoneer artillery-sergeant) (6lb Cannon)':8,
    'Warrior 5 lvl (cannoneer artillery-lieutenant)':6,
    'Commoner 1 lvl (recruit)':100,
    }

metadict_squads['Company-veteran (cannoneer artillery-battery) (12-lb Mortars)'] = {
    'Warrior 1 lvl (cannoneer artillery)':30,
    'Warrior 2 lvl (cannoneer artillery-veteran)':60,
    'Warrior 3 lvl (cannoneer artillery-corporal)':10,
    'Warrior 4 lvl (cannoneer artillery-sergeant) (12lb Mortar)':8,
    'Warrior 5 lvl (cannoneer artillery-lieutenant)':6,
    'Commoner 1 lvl (recruit)':100,
    }

metadict_squads['Company-veteran (cannoneer artillery-battery) (12-lb Cannons, naval)'] = {
    'Warrior 1 lvl (cannoneer artillery)':30,
    'Warrior 2 lvl (cannoneer artillery-veteran)':60,
    'Warrior 3 lvl (cannoneer artillery-corporal)':10,
    'Warrior 4 lvl (cannoneer artillery-sergeant) (12lb Cannon, naval)':10,
    'Warrior 5 lvl (cannoneer artillery-lieutenant)':6,
    'Commoner 1 lvl (recruit)':100,
    }

metadict_squads['Company-veteran (cannoneer artillery-battery) (24-lb Cannons, naval)'] = {
    'Warrior 1 lvl (cannoneer artillery)':30,
    'Warrior 2 lvl (cannoneer artillery-veteran)':60,
    'Warrior 3 lvl (cannoneer artillery-corporal)':10,
    'Warrior 4 lvl (cannoneer artillery-sergeant) (24lb Cannon, naval)':10,
    'Warrior 5 lvl (cannoneer artillery-lieutenant)':6,
    'Commoner 1 lvl (recruit)':100,
    }

metadict_squads['Company-veteran (cannoneer artillery-battery) (2-lb Falconets)'] = {
    'Warrior 1 lvl (cannoneer artillery)':30,
    'Warrior 2 lvl (cannoneer artillery-veteran)':60,
    'Warrior 3 lvl (cannoneer artillery-corporal)':10,
    'Warrior 4 lvl (cannoneer artillery-sergeant) (2lb Falconet)':8,
    'Warrior 5 lvl (cannoneer artillery-lieutenant)':6,
    'Commoner 1 lvl (recruit)':100,
    }

#----
# Элитные отряды:

metadict_squads['Company-elite (line-infantry-musketeers)'] = {
    # Гвардия героев 11+ lvl
    # 25 капитанов и 260 000 exp на отряд.
    # Отличный отряд (сумма параметров 69+) -- 400 рекрутов на 100 солдат
    'Warrior 4 lvl (musketeer line-infantry-sergeant)':67,
    'Warrior 5 lvl (musketeer line-infantry-lieutenant)':25,
    'Commoner 1 lvl (recruit)':300,
    }

metadict_squads['Company-elite (line-infantry-fusiliers)'] = {
    'Warrior 4 lvl (fusilier line-infantry-sergeant)':67,
    'Warrior 5 lvl (fusilier line-infantry-lieutenant) (Schwartz Mark)':25,
    'Commoner 1 lvl (recruit)':300,
    }

metadict_squads['Company-elite (line-infantry-grenadiers)'] = {
    'Warrior 4 lvl (grenadier line-infantry-sergeant)':67,
    'Warrior 5 lvl (grenadier line-infantry-lieutenant)':25,
    'Commoner 1 lvl (recruit)':300,
    }

metadict_squads['Company-elite (line-infantry-bombardier)'] = {
    'Warrior 4 lvl (bombardier line-infantry-sergeant)':67,
    'Warrior 5 lvl (bombardier line-infantry-lieutenant-variant-bomba-san)':20,
    'Warrior 5 lvl (bombardier line-infantry-lieutenant-variant-shaitan)':5,
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
    'Fighter 5 lvl (legionary horseman-lieutenant)':1,
    #'Fighter 4 lvl (legionary horseman-sergeant)':1,
    #'Fighter 3 lvl (legionary horseman-corporal)':12,
    'Fighter 2 lvl (legionary horseman-veteran)':12,
    #'Fighter 1 lvl (legionary horseman)':12,
    }

metadict_squads['Squad-hero (fighters-samurai)'] = {
    'Fighter 5 lvl (legionary slayer-lieutenant)':1,
    #'Fighter 4 lvl (legionary slayer-sergeant)':1,
    #'Fighter 3 lvl (legionary slayer-champion)':12,
    'Fighter 2 lvl (legionary slayer-flanker)':12,
    #'Fighter 1 lvl (legionary slayer-rookie)':12,
    }

metadict_squads['Squad-hero (fighters-shieldmans)'] = {
    'Fighter 5 lvl (legionary sentinel-lieutenant)':1,
    #'Fighter 4 lvl (legionary sentinel-sergeant)':1,
    #'Fighter 3 lvl (legionary sentinel-mystic)':12,
    'Fighter 2 lvl (legionary sentinel-shieldman)':12,
    #'Fighter 1 lvl (legionary sentinel-battler)':12,
    }

metadict_squads['Squad-hero (rogues)'] = {
    'Rogue 5 lvl (mercenary phantom-lieutenant)':1,
    #'Rogue 4 lvl (mercenary phantom-sergeant)':1,
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
    'Ranger 5 lvl (otherworld wanderer-lieutenant)':1,
    #'Ranger 4 lvl (otherworld wanderer-sergeant)':1,
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
    'Paladin 5 lvl (city sentry-lieutenant)':1,
    #'Paladin 4 lvl (city sentry-sergeant)':1,
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
    #'Fighter 5 lvl (legionary horseman-lieutenant)':1,
    'Fighter 4 lvl (legionary horseman-sergeant)':1,
    #'Fighter 3 lvl (legionary horseman-corporal)':6,
    #'Fighter 2 lvl (legionary horseman-veteran)':6,
    'Fighter 1 lvl (legionary horseman)':6,
    }

metadict_squads['Band-hero (fighters-samurai)'] = {
    #'Fighter 5 lvl (legionary slayer-lieutenant)':1,
    'Fighter 4 lvl (legionary slayer-sergeant)':1,
    #'Fighter 3 lvl (legionary slayer-champion)':6,
    #'Fighter 2 lvl (legionary slayer-flanker)':6,
    'Fighter 1 lvl (legionary slayer-rookie)':6,
    }

metadict_squads['Band-hero (fighters-shieldmans)'] = {
    #'Fighter 5 lvl (legionary sentinel-lieutenant)':1,
    'Fighter 4 lvl (legionary sentinel-sergeant)':1,
    #'Fighter 3 lvl (legionary sentinel-mystic)':6,
    #'Fighter 2 lvl (legionary sentinel-shieldman)':6,
    'Fighter 1 lvl (legionary sentinel-battler)':6,
    }

metadict_squads['Band-hero (rogues)'] = {
    #'Rogue 5 lvl (mercenary phantom-lieutenant)':1,
    'Rogue 4 lvl (mercenary phantom-sergeant)':1,
    #'Rogue 3 lvl (mercenary phantom-deadeye)':6,
    #'Rogue 2 lvl (mercenary phantom-hawkeye)':6,
    'Rogue 1 lvl (mercenary phantom-blackeye)':6,
    }

metadict_squads['Band-hero (rogues-arcane)'] = {
    'Rogue 4 lvl (city cat-runner)':1,
    'Rogue 2 lvl (city cat-meow)':6,
    }

metadict_squads['Band-hero (rangers)'] = {
    #'Ranger 5 lvl (otherworld wanderer-lieutenant)':1,
    'Ranger 4 lvl (otherworld wanderer-sergeant)':1,
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
    #'Paladin 5 lvl (city sentry-lieutenant)':1,
    'Paladin 4 lvl (city sentry-sergeant)':1,
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
    'Fighter 5 lvl (legionary slayer-lieutenant)':1,
    }

metadict_squads['Single-hero (sentinels)'] = {
    'Fighter 5 lvl (legionary sentinel-lieutenant)':1,
    }

metadict_squads['Single-hero (horsemans)'] = {
    'Fighter 5 lvl (legionary horseman-lieutenant)':1,
    }

metadict_squads['Single-hero (rogues)'] = {
    'Rogue 5 lvl (mercenary phantom-lieutenant)':1,
    }

metadict_squads['Single-hero (rangers)'] = {
    'Ranger 5 lvl (otherworld wanderer-lieutenant)':1,
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

metadict_squads['Single-hero (cat)'] = {
    'Rogue 5 lvl (city cat-mastermind)':1,
    }

#-------------------------------------------------------------------------------
# Чёрные флаги Ост-Индии, Black Flags

#----
# Армия союзников:

metadict_squads['Squad-regular (артиллеристы флота) (батарея опендека) (6lb Cannons)'] = {
    'Warrior 1 lvl (артиллерист)':20 + dice_throw('2d10'),
    'Warrior 2 lvl (артиллерист-ветеран) (6lb Cannon)':6,
    'Warrior 4 lvl (артиллерист-сержант)':1,
    }

metadict_squads['Squad-regular (артиллеристы флота) (батарея фальконет) (2lb Falconets)'] = {
    'Warrior 1 lvl (артиллерист)':20 + dice_throw('2d10'),
    'Warrior 2 lvl (артиллерист-ветеран) (2lb Falconet)':6,
    'Warrior 4 lvl (артиллерист-сержант)':1,
    }

metadict_squads['Squad-veteran (абордажники флота)'] = {
    'Warrior 2 lvl (абордажник-ветеран)':25 + dice_throw('2d4'),
    'Warrior 5 lvl (абордажник-лейтенант) (лидер)':1,
    'Commoner 1 lvl (recruit)':35,
    }

metadict_squads['Squad-veteran (абордажники флота) (кошки)'] = {
    'Warrior 2 lvl (абордажник-ветеран) (кошка)':25 + dice_throw('2d4'),
    'Warrior 5 lvl (абордажник-лейтенант) (котяра)':1,
    }

#----
# Армия Эвери:

metadict_squads['Single-hero (лично Эвери) (друг)'] = {
    #'Fighter 13 lvl (Генри Эвери)':1,
    'Fighter 11 lvl (Люсьен де ла Помпаж)':1,
    }

metadict_squads['Company-elite (абордажники Эвери) (друг)'] = {
    # 1 рота гвардии, экипаж Фэнси
    # 6 героев, 6 лейтенантов героев, 6 летёх экипажа = 18 офицеров 5 lvl.
    'Warrior 4 lvl (абордажник Эвери)':52,
    'Warrior 4 lvl (абордажник Эвери) (лидер)':15,
    'Warrior 5 lvl (лейтенант Эвери)':20,
    'Warrior 5 lvl (лейтенант Эвери) (лидер)':5,
    'Commoner 1 lvl (recruit)':300,
    }

metadict_squads['Squad-veteran (артиллеристы Эвери) (батарея гандека) (12lb Cannons)'] = {
    'Warrior 2 lvl (артиллерист-ветеран)':30,
    'Warrior 3 lvl (артиллерист-капрал) (12lb Cannon)':10,
    'Warrior 5 lvl (артиллерист-лейтенант)':2,
    'Commoner 1 lvl (recruit)':50,
    }

metadict_squads['Squad-veteran (артиллеристы Эвери) (батарея опендека) (6lb Cannons)'] = {
    'Warrior 2 lvl (артиллерист-ветеран)':30,
    'Warrior 3 lvl (артиллерист-капрал) (6lb Cannon)':10,
    'Warrior 5 lvl (артиллерист-лейтенант)':2,
    'Commoner 1 lvl (recruit)':50,
    }

metadict_squads['Squad-veteran (артиллеристы Эвери) (батарея фальконет) (2lb Falconets)'] = {
    'Warrior 2 lvl (артиллерист-ветеран)':18,
    'Warrior 4 lvl (артиллерист-сержант) (2lb Falconet)':6,
    'Warrior 5 lvl (артиллерист-лейтенант)':2,
    'Commoner 1 lvl (recruit)':30,
    }

#----
# Армия Салифа:

metadict_squads['Company-militia (паломники с Ганг-и-Савайя) (враг)'] = {
    'Commoner 1 lvl (паломник с Ганг-и-Савайя)':80 + dice_throw('1d12'),
    'Commoner 2 lvl (дворянин с Ганг-и-Савайя)':10 + dice_throw('1d12'),
    'Warrior 3 lvl (охранник с Ганг-и-Савайя)':6,
    'Warrior 4 lvl (охранник-сержант с Ганг-и-Савайя)':1,
    'Warrior 5 lvl (охранник-лейтенант с Ганг-и-Савайя)':1,
    }

metadict_squads['Company-elite (гвардия Салифа) (враг)'] = {
    # 1 рота гвардии.
    'Warrior 4 lvl (гвардеец Салифа)':67,
    'Warrior 5 lvl (лейтенант Салифа)':25,
    'Commoner 1 lvl (recruit)':300,
    }

metadict_squads['Squad-elite (гвардия Салифа) (враг)'] = {
    # 4 отдельный взвода гвардии.
    'Warrior 4 lvl (гвардеец Салифа)':16,
    'Warrior 5 lvl (лейтенант Салифа)':6,
    'Commoner 1 lvl (recruit)':60,
    }

metadict_squads['Band-elite (волшебники Салифа) (враг)'] = {
    'Wizard 4 lvl (волшебник Салифа)':3,
    'Wizard 13 lvl (Салиф)':1,
    }

metadict_squads['Squad-veteran (артиллеристы Салифа) (батарея гандека) (12lb Cannons)'] = {
    'Warrior 2 lvl (артиллерист-ветеран)':30,
    'Warrior 3 lvl (артиллерист-капрал) (12lb Cannon)':10,
    'Warrior 5 lvl (артиллерист-лейтенант)':2,
    'Commoner 1 lvl (recruit)':50,
    }

metadict_squads['Squad-veteran (артиллеристы Салифа) (батарея опендека) (6lb Cannons)'] = {
    'Warrior 2 lvl (артиллерист-ветеран)':30,
    'Warrior 3 lvl (артиллерист-капрал) (6lb Cannon)':10,
    'Warrior 5 lvl (артиллерист-лейтенант)':2,
    'Commoner 1 lvl (recruit)':50,
    }

metadict_squads['Squad-veteran (артиллеристы Салифа) (батарея фальконет) (2lb Falconets)'] = {
    # 4 батареи Ганг-и-Савайя. Одна на носу, одна на корме, по одной с каждого борта.
    'Warrior 2 lvl (артиллерист-ветеран)':30,
    'Warrior 4 lvl (артиллерист-сержант) (2lb Falconet)':10,
    'Warrior 5 lvl (артиллерист-лейтенант)':4,
    'Commoner 1 lvl (recruit)':50,
    }

#----
# Армия Намулиса:

metadict_squads['Company-elite (гвардия Намулиса) (враг)'] = {
    # 1 рота гвардии.
    'Warrior 4 lvl (гвардеец Намулиса)':67,
    'Warrior 5 lvl (лейтенант Намулиса)':25,
    'Commoner 1 lvl (recruit)':300,
    }

metadict_squads['Squad-elite (гвардия Намулиса) (враг)'] = {
    # 4 отдельный взвода гвардии.
    'Warrior 4 lvl (гвардеец Намулиса)':16,
    'Warrior 5 lvl (лейтенант Намулиса)':6,
    'Commoner 1 lvl (recruit)':60,
    }

metadict_squads['Single-hero (лично Намулис) (враг)'] = {
    'Monk 13 lvl (Намулис)':1,
    }

#----
# Сами-по-себе кошки:

metadict_squads['Band-hero (свита Тензы Йозоры) (Shady)'] = {
    'Warrior 3 lvl (Тензина девчонка)':6,
    'Warrior 4 lvl (Тензина девчонка поопытнее)':1,
    'Warrior 5 lvl (Шакти)':1,
    }

metadict_squads['Single-hero (лично Тенза Йозора) (Shady)'] = {
    'Artificier 5 lvl (Shady) (Тенза Йозора)':1,
    }

metadict_squads['Single-hero (лично Януш Кобыла) (Динки)'] = {
    # Сын Стефана Кобылы, конезаводчика с Гангсвэя.
    'Warrior 5 lvl (healer-lieutenant)':1,
    }

#----
# Команда Фэнси:

metadict_squads['Single-hero (лично Питер Янсен) (Katorjnik)'] = {
    'Ranger 5 lvl (Katorjnik) (Питер Янсен)':1,
    }

metadict_squads['Single-hero (лично Тобиас Олдридж) (Волшебник)'] = {
    'Fighter 5 lvl (Волшебник) (Тобиас Олдридж)':1,
    }

metadict_squads['Single-hero (лично Джон Кук) (firesalamander)'] = {
    'Bard 5 lvl (firesalamander) (Джон Кук)':1,
    }

metadict_squads['Band-summon (камикадзе Джона Кука) (firesalamander)'] = {
    'Unseen Servant (30-lb bomb)':6,
    }

metadict_squads['Single-summon (камикадзе Джона Кука) (firesalamander)'] = {
    'Unseen Servant (30-lb bomb)':1,
    }

metadict_squads['Single-hero (лично Тим Серый) (Гримсон)'] = {
    'Artificier 5 lvl (Гримсон) (Тим Серый)':1,
    }
