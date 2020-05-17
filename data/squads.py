#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dices import *

#-------------------------------------------------------------------------
# Отряды

metadict_squads = {}

#----
# Тестовые

#metadict_squads['test 1000 warriors'] = {
#    'Warrior 1 lvl (legionary infantry)':1000,
#    'Warrior 3 lvl (legionary infantry-sergeant)':3,
#    'Warrior 4 lvl (legionary infantry-lieutenant)':1,
#    'Warrior 5 lvl (legionary infantry-captain)':1,
#    }

metadict_squads['test 100 warriors'] = {
    'Warrior 1 lvl (legionary infantry)':100,
    'Warrior 5 lvl (legionary infantry-captain)':1,
    }

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

#----
# Рекруты:

metadict_squads['Company-dummy (zombies)'] = {
    'Zombie (CR 1/4)':80 + dice_throw('3d12'),
    'Wight (CR 3)':1,
    }

metadict_squads['Company-dummy (bandits)'] = {
    'Bandit (CR 1/8)':80 + dice_throw('3d12'),
    'Thug (CR 1/2)':4,
    'Veteran (CR 3)':1,
    }

metadict_squads['Company-dummy (sentinels)'] = {
    'Sentinel (CR 1/8)':80 + dice_throw('3d12'),
    'Veteran (CR 3)':1,
    }

metadict_squads['Company-dummy (goblins)'] = {
    'Goblin (CR 1/4)':80 + dice_throw('3d12'),
    'Goblin Boss (CR 1)':3,
    }

metadict_squads['Company-dummy (hobgoblins)'] = {
    'Hobgoblin (CR 1/2)':80 + dice_throw('3d12'),
    'Hobgoblin-captain (CR 3)':3,
    }

metadict_squads['Company-dummy (orks)'] = {
    'Ork (CR 1/2)':80 + dice_throw('3d12'),
    'Orog (CR 2)':3,
    'Ork war chief (CR 4)':1,
    }

#----
# Отряды:

#metadict_squads['Squad-dummy (orks)'] = {
#    'Ork (CR 1/2)':12,
#    'Orog (CR 2)':1,
#    }
#
#metadict_squads['Squad-dummy (hobgoblins)'] = {
#    'Hobgoblin (CR 1/2)':12,
#    'Hobgoblin-captain (CR 3)':1,
#    }

#----
# Рекруты:

#metadict_squads['Commander-dummy (wight)'] = {
#    'Wight (CR 3)':1,
#    }
#
#metadict_squads['Commander-dummy (Veteran)'] = {
#    'Veteran (CR 3)':1,
#    }
#
#metadict_squads['Commander-dummy (hobgoblin-captain)'] = {
#    'Hobgoblin-captain (CR 3)':1,
#    }

metadict_squads['Commander-dummy (empyrean)'] = {
    'Empyrean (CR 23)':1,
    }

#----
# Рекруты:

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

metadict_squads['Company-regular (infantry-pikemans)'] = {
    'Warrior 1 lvl (city pikeman)':80 + dice_throw('1d12'),
    'Warrior 2 lvl (city pikeman-corporal)':10,
    'Warrior 3 lvl (city pikeman-sergeant)':3,
    'Warrior 4 lvl (city pikeman-lieutenant)':1,
    'Warrior 5 lvl (city pikeman-captain)':1,
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

metadict_squads['Company-regular (infantry-shekelesh)'] = {
    'Warrior 1 lvl (shekelesh infantry)':80 + dice_throw('1d12'),
    'Warrior 2 lvl (shekelesh infantry-corporal)':10,
    'Warrior 3 lvl (shekelesh infantry-sergeant)':3,
    'Warrior 4 lvl (shekelesh infantry-lieutenant)':1,
    'Warrior 5 lvl (shekelesh infantry-captain)':1,
    }

metadict_squads['Company-regular (infantry-shekelesh-lvl-6)'] = {
    'Warrior 1 lvl (shekelesh infantry)':160 + dice_throw('1d12'),
    'Warrior 2 lvl (shekelesh infantry-corporal)':20,
    'Warrior 3 lvl (shekelesh infantry-sergeant)':6,
    'Warrior 4 lvl (shekelesh infantry-lieutenant)':2,
    'Warrior 5 lvl (shekelesh infantry-captain)':1,
    }

metadict_squads['Company-regular (infantry-shekelesh-lvl-8)'] = {
    'Warrior 2 lvl (shekelesh infantry-corporal)':160,
    'Warrior 3 lvl (shekelesh infantry-sergeant)':10,
    'Warrior 4 lvl (shekelesh infantry-lieutenant)':3,
    'Warrior 5 lvl (shekelesh infantry-captain)':1,
    'Empyrean (CR 23)':1,
    'Warlock 2 lvl (otherworld seeker-adept)':12,
    'Warlock 5 lvl (otherworld seeker-ascendant)':1,
    }

metadict_squads['Company-regular (infantry-celtian)'] = {
    'Warrior 1 lvl (celtian infantry)':80 + dice_throw('1d12'),
    'Warrior 2 lvl (celtian infantry-corporal)':10,
    'Warrior 3 lvl (celtian infantry-sergeant)':3,
    'Warrior 4 lvl (celtian infantry-lieutenant)':1,
    'Warrior 5 lvl (celtian infantry-captain)':1,
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

metadict_squads['Company-regular (infantry-polearms)'] = {
    'Warrior 1 lvl (mercenary heavy-infantry)':80 + dice_throw('1d12'),
    'Warrior 2 lvl (mercenary heavy-infantry-corporal)':10,
    'Warrior 3 lvl (mercenary heavy-infantry-sergeant)':3,
    'Warrior 4 lvl (mercenary heavy-infantry-lieutenant)':1,
    'Warrior 5 lvl (mercenary heavy-infantry-captain)':1,
    }

metadict_squads['Company-regular (bowmans-persian)'] = {
    'Warrior 1 lvl (persian bowman)':80 + dice_throw('1d12'),
    'Warrior 2 lvl (persian bowman-corporal)':10,
    'Warrior 3 lvl (persian bowman-sergeant)':3,
    'Warrior 4 lvl (persian bowman-lieutenant)':1,
    'Warrior 5 lvl (persian bowman-captain)':1,
    }

metadict_squads['Company-regular (bowmans-scythian)'] = {
    'Warrior 1 lvl (sqythian bowman)':80 + dice_throw('1d12'),
    'Warrior 2 lvl (sqythian bowman-corporal)':10,
    'Warrior 3 lvl (sqythian bowman-sergeant)':3,
    'Warrior 4 lvl (sqythian bowman-lieutenant)':1,
    'Warrior 5 lvl (sqythian bowman-captain)':1,
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
    'Rogue 3 lvl (city cat-dodger)':6,
    #'Rogue 4 lvl (city cat-runner)':1,
    'Rogue 5 lvl (city cat-mastermind)':1,
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

#metadict_squads['Commander-hero (barbarians)'] = {
#    'Barbarian 5 lvl (thracian slayer-lord)':1,
#    }
#
#metadict_squads['Commander-hero (samurai)'] = {
#    'Fighter 5 lvl (legionary slayer-captain)':1,
#    }
#
#metadict_squads['Commander-hero (sentinels)'] = {
#    'Fighter 5 lvl (legionary sentinel-captain)':1,
#    }
#
#metadict_squads['Commander-hero (horsemans)'] = {
#    'Fighter 5 lvl (legionary horseman-captain)':1,
#    }
#
#metadict_squads['Commander-hero (rogues)'] = {
#    'Rogue 5 lvl (mercenary phantom-captain)':1,
#    }
#
#metadict_squads['Commander-hero (rangers)'] = {
#    'Ranger 5 lvl (otherworld wanderer-captain)':1,
#    }
#
#metadict_squads['Commander-hero (wizards)'] = {
#    'Wizard 5 lvl (otherworld mage-seer)':1,
#    }
#
#metadict_squads['Commander-hero (druids)'] = {
#    'Druid 5 lvl (otherworld terian-loremaster)':1,
#    }
#
#metadict_squads['Commander-hero (sorcerers)'] = {
#    'Sorcerer 5 lvl (otherworld wildfire-ravager)':1,
#    }
#
#metadict_squads['Commander-hero (warlocks)'] = {
#    'Warlock 5 lvl (otherworld seeker-ascendant)':1,
#    }
#
#metadict_squads['Commander-hero (monks)'] = {
#    'Monk 5 lvl (city windsong-warmonger)':1,
#    }

#----
# Герои (роты):

#metadict_squads['Company-hero (hoplites-sentinels)'] = {
#    'Warrior 1 lvl (achean hoplite)':80 + dice_throw('1d12'),
#    'Warrior 2 lvl (achean hoplite-corporal)':10,
#    'Warrior 3 lvl (achean hoplite-sergeant)':3,
#    'Warrior 4 lvl (achean hoplite-lieutenant)':1,
#    #'Warrior 5 lvl (achean hoplite-captain)':1,
#    #'Cleric 1 lvl (city maatcarian-acolyte)':1,
#    #'Fighter 1 lvl (legionary sentinel-battler)':12,
#    'Fighter 2 lvl (legionary sentinel-shieldman)':12,
#    'Fighter 5 lvl (legionary sentinel-captain)':1,
#    }
#
#metadict_squads['Company-hero (hoplites-bards)'] = {
#    'Warrior 1 lvl (achean hoplite)':80 + dice_throw('1d12'),
#    'Warrior 2 lvl (achean hoplite-corporal)':10,
#    'Warrior 3 lvl (achean hoplite-sergeant)':3,
#    'Warrior 4 lvl (achean hoplite-lieutenant)':1,
#    #'Warrior 5 lvl (achean hoplite-captain)':1,
#    #'Cleric 1 lvl (city maatcarian-acolyte)':1,
#    #'Bard 1 lvl (otherworld singer-follower)':12,
#    'Bard 2 lvl (otherworld singer-stranger)':12,
#    'Bard 5 lvl (otherworld singer-leader)':1,
#    }
#
#metadict_squads['Company-hero (celtian-barbarians)'] = {
#    'Warrior 1 lvl (celtian infantry)':80 + dice_throw('1d12'),
#    'Warrior 2 lvl (celtian infantry-corporal)':10,
#    'Warrior 3 lvl (celtian infantry-sergeant)':3,
#    'Warrior 4 lvl (celtian infantry-lieutenant)':1,
#    #'Warrior 5 lvl (celtian infantry-captain)':1,
#    #'Cleric 1 lvl (city maatcarian-acolyte)':1,
#    #'Barbarian 1 lvl (thracian slayer-dogface)':12,
#    'Barbarian 2 lvl (thracian slayer-slasher)':12,
#    'Barbarian 5 lvl (thracian slayer-lord)':1,
#    }
#
#metadict_squads['Company-hero (legionary-samurai)'] = {
#    'Warrior 1 lvl (legionary infantry)':80 + dice_throw('1d12'),
#    'Warrior 2 lvl (legionary infantry-corporal)':10,
#    'Warrior 3 lvl (legionary infantry-sergeant)':3,
#    'Warrior 4 lvl (legionary infantry-lieutenant)':1,
#    #'Warrior 5 lvl (legionary infantry-captain)':1,
#    #'Cleric 1 lvl (city maatcarian-acolyte)':1,
#    #'Fighter 1 lvl (legionary slayer-rookie)':12,
#    'Fighter 2 lvl (legionary slayer-samurai)':12,
#    'Fighter 5 lvl (legionary slayer-captain)':1,
#    }
#
#metadict_squads['Company-hero (polearms-monks)'] = {
#    'Warrior 1 lvl (mercenary heavy-infantry)':80 + dice_throw('1d12'),
#    'Warrior 2 lvl (mercenary heavy-infantry-corporal)':10,
#    'Warrior 3 lvl (mercenary heavy-infantry-sergeant)':3,
#    'Warrior 4 lvl (mercenary heavy-infantry-lieutenant)':1,
#    #'Warrior 5 lvl (mercenary heavy-infantry-captain)':1,
#    #'Cleric 1 lvl (city maatcarian-acolyte)':1,
#    #'Monk 1 lvl (city windsong-apprentice)':12,
#    'Monk 2 lvl (city windsong-gatekeeper)':12,
#    'Monk 5 lvl (city windsong-warmonger)':1,
#    }
#
#metadict_squads['Company-hero (bowmans-wizards)'] = {
#    'Warrior 1 lvl (persian bowman)':80 + dice_throw('1d12'),
#    'Warrior 2 lvl (persian bowman-corporal)':10,
#    'Warrior 3 lvl (persian bowman-sergeant)':3,
#    'Warrior 4 lvl (persian bowman-lieutenant)':1,
#    #'Warrior 5 lvl (persian bowman-captain)':1,
#    #'Cleric 1 lvl (city maatcarian-acolyte)':1,
#    #'Wizard 1 lvl (otherworld mage-disciple)':12,
#    'Wizard 2 lvl (otherworld mage-weaver)':12,
##    'Wizard 3 lvl (otherworld mage-annalist)':1,
##    'Wizard 4 lvl (otherworld mage-savant)':1,
#    'Wizard 5 lvl (otherworld mage-seer)':1,
#    }
#
#metadict_squads['Company-hero (bowmans-druids)'] = {
#    'Warrior 1 lvl (persian bowman)':80 + dice_throw('1d12'),
#    'Warrior 2 lvl (persian bowman-corporal)':10,
#    'Warrior 3 lvl (persian bowman-sergeant)':3,
#    'Warrior 4 lvl (persian bowman-lieutenant)':1,
#    #'Warrior 5 lvl (persian bowman-captain)':1,
#    #'Cleric 1 lvl (city maatcarian-acolyte)':1,
#    #'Druid 1 lvl (otherworld terian-forester)':12,
#    'Druid 2 lvl (otherworld terian-changer)':12,
#    #'Druid 3 lvl (otherworld terian-wiseman)':1,
#    #'Druid 4 lvl (otherworld terian-wonderman)':1,
#    'Druid 5 lvl (otherworld terian-loremaster)':1,
#    }
#
#metadict_squads['Company-hero (bowmans-rogues)'] = {
#    'Warrior 1 lvl (sqythian bowman)':80 + dice_throw('1d12'),
#    'Warrior 2 lvl (sqythian bowman-corporal)':10,
#    'Warrior 3 lvl (sqythian bowman-sergeant)':3,
#    'Warrior 4 lvl (sqythian bowman-lieutenant)':1,
#    #'Warrior 5 lvl (sqythian bowman-captain)':1,
#    #'Cleric 1 lvl (city maatcarian-acolyte)':1,
##    'Rogue 1 lvl (mercenary phantom-blackeye)':12,
#    'Rogue 2 lvl (mercenary phantom-hawkeye)':12,
##    'Rogue 3 lvl (mercenary phantom-deadeye)':1,
##    'Rogue 4 lvl (mercenary phantom-lieutenant)':1,
#    'Rogue 5 lvl (mercenary phantom-captain)':1,
#    }
#
#metadict_squads['Company-hero (bowmans-rangers)'] = {
#    'Warrior 1 lvl (sqythian bowman)':80 + dice_throw('1d12'),
#    'Warrior 2 lvl (sqythian bowman-corporal)':10,
#    'Warrior 3 lvl (sqythian bowman-sergeant)':3,
#    'Warrior 4 lvl (sqythian bowman-lieutenant)':1,
#    #'Warrior 5 lvl (sqythian bowman-captain)':1,
#    #'Cleric 1 lvl (city maatcarian-acolyte)':1,
#    #'Ranger 1 lvl (otherworld wanderer-scout)':12,
#    'Ranger 2 lvl (otherworld wanderer-marksman)':12,
#    #'Ranger 3 lvl (otherworld wanderer-hunter)':1,
#    #'Ranger 4 lvl (otherworld wanderer-lieutenant)':1,
#    'Ranger 5 lvl (otherworld wanderer-captain)':1,
#    }
#
#metadict_squads['Company-hero (polearms-sorcerers)'] = {
#    'Warrior 1 lvl (mercenary heavy-infantry)':80 + dice_throw('1d12'),
#    'Warrior 2 lvl (mercenary heavy-infantry-corporal)':10,
#    'Warrior 3 lvl (mercenary heavy-infantry-sergeant)':3,
#    'Warrior 4 lvl (mercenary heavy-infantry-lieutenant)':1,
#    #'Warrior 5 lvl (mercenary heavy-infantry-captain)':1,
#    #'Cleric 1 lvl (city maatcarian-acolyte)':1,
#    'Sorcerer 2 lvl (otherworld wildfire-burner)':12,
#    #'Sorcerer 4 lvl (otherworld wildfire-paragon)':1,
#    'Sorcerer 5 lvl (otherworld wildfire-ravager)':1,
#    }
#
#metadict_squads['Company-hero (polearms-warlocks)'] = {
#    'Warrior 1 lvl (mercenary heavy-infantry)':80 + dice_throw('1d12'),
#    'Warrior 2 lvl (mercenary heavy-infantry-corporal)':10,
#    'Warrior 3 lvl (mercenary heavy-infantry-sergeant)':3,
#    'Warrior 4 lvl (mercenary heavy-infantry-lieutenant)':1,
#    #'Warrior 5 lvl (mercenary heavy-infantry-captain)':1,
#    #'Cleric 1 lvl (city maatcarian-acolyte)':1,
#    #'Warlock 1 lvl (otherworld seeker-follower)':12,
#    'Warlock 2 lvl (otherworld seeker-adept)':12,
#    #'Warlock 3 lvl (otherworld seeker-emissary)':1,
#    #'Warlock 4 lvl (otherworld seeker-envoy)':1,
#    'Warlock 5 lvl (otherworld seeker-ascendant)':1,
#    }
#
#metadict_squads['Company-hero (legionary-clerics-light)'] = {
#    'Warrior 1 lvl (legionary infantry)':80 + dice_throw('1d12'),
#    'Warrior 2 lvl (legionary infantry-corporal)':10,
#    'Warrior 3 lvl (legionary infantry-sergeant)':3,
#    'Warrior 4 lvl (legionary infantry-lieutenant)':1,
#    #'Warrior 5 lvl (legionary infantry-captain)':1,
#    #'Cleric 1 lvl (city maatcarian-acolyte)':1,
#    #'Cleric 1 lvl (city luminary-acolyte)':12,
#    'Cleric 2 lvl (city luminary-celebrant)':12,
#    #'Cleric 3 lvl (city luminary-augur)':1,
#    #'Cleric 4 lvl (city luminary-arbiter)':1,
#    'Cleric 5 lvl (city luminary-reviver)':1,
#    }

