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

metadict_squads['Company-test (standard) (greataxes)'] = {
    'Warrior 1 lvl (standard) (Greataxe)':100,
    'Trap (commander)':1,
    }

metadict_squads['Company-test (standard) (disadvantage) (greataxes)'] = {
    'Warrior 1 lvl (standard) (disadvantage) (Greataxe)':100,
    'Trap (commander)':1,
    }

metadict_squads['Company-test (standard) (bless + disadvantage) (greataxes)'] = {
    'Warrior 1 lvl (standard) (bless + disadvantage) (Greataxe)':100,
    'Trap (commander)':1,
    }

metadict_squads['Company-test (standard) (battleaxes)'] = {
    'Warrior 1 lvl (standard) (Battleaxe + Shield)':100,
    'Trap (commander)':1,
    }

metadict_squads['test 12 animals'] = {
    #'Brown Bear (CR 1)':12,
    'Giant Octopus (CR 1)':12,
    #'Empyrean (CR 23)':1,
    }

metadict_squads['test 4 onagers'] = {
    'Warrior 3 lvl (siege engineer-apprentice) (onager-fire)':3,
    'Warrior 4 lvl (siege engineer-master) (onager-fire)':1,
    }

metadict_squads['traps (lightning)'] = {
    'Trap (Glyph of Warding) (Lightning)':1,
    'Trap (commander)':1,
    }

metadict_squads['traps (boulders)'] = {
    'Trap (Boulders)':1,
    'Trap (commander)':1,
    }

metadict_squads['traps (fire)'] = {
    # Восемь бочек алхимичесого огня на корабль
    'Trap (Alchemist\'s Fire)':8,
    'Trap (commander)':1,
    }

metadict_squads['test (ogres)'] = {
    'Ogre (CR 2)':4,
    'Orog (CR 2)':1,
    }

metadict_squads['test enemy (CR 1)'] = {
    'Warrior 3 lvl (враг) (демон Кема\'Эша)':1,
    }

metadict_squads['test party (1 lvl)'] = {
    # Тестовая партия для оценки CR:
    # Воин, клирик, вор и маг:
        # Боец -- лучник с боевым стилем
        # Клерик -- "Воодушевляющий лидер" и командир, колдует "Bless"
        # Рога -- с ножом и арбалетом
        # Волшебник -- с "Волшебной стрелой"
    #'Barbarian 1 lvl (thracian slayer-dogface)':1,
    'Fighter 1 lvl (ArbitraryNickname) (снайпер)':1,
    'Cleric 1 lvl (war cleric)':1,
    'Rogue 1 lvl (city cat-nyamo)':1,
    'Wizard 1 lvl (otherworld mage-disciple)':1,
    }

metadict_squads['Company-dummy (куклы)'] = {
    # Просто чучела на кораблях.
    'Dummy (CR 0)':100,
    'Dummy-officer (CR 0)':4,
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

#----
# Враги (битва за Лемнос):

metadict_squads['Band-hero (колдуны Кара\'Яма) (враг)'] = {
    'Warlock 5 lvl (враг) (Кара\'Ям)':1,
    'Warlock 1 lvl (враг) (колдун Кара\'Яма)':12,
    }

metadict_squads['Band-hero (колдуны Кема\'Эша) (враг)'] = {
    'Warlock 5 lvl (враг) (Кема\'Эш)':1,
    'Warlock 1 lvl (враг) (колдун Кема\'Эша)':6,
    }

metadict_squads['Band-hero (следопыты Энзифа) (враг)'] = {
    'Ranger 5 lvl (враг) (Энзиф «Ходи-гора»)':1,
    'Ranger 1 lvl (враг) (следопыт Энзифа)':12,
    }

metadict_squads['Band-hero (паладины Магора) (враг)'] = {
    'Paladin 5 lvl (враг) (Магор «Детоед»)':1,
    'Paladin 1 lvl (враг) (паладин Магора)':6,
    }

metadict_squads['Band-hero (снайперы Хана-Вама) (враг)'] = {
    # "Верные ученики" и "Многочисленная свита"
    'Fighter 5 lvl (враг) (Хана\'Вам)':1,
    'Fighter 1 lvl (враг) (снайпер Хана\'Вама)':12,
    }

metadict_squads['Band-hero (друиды Тик-Бо) (враг)'] = {
    # Шесть друидов и Тик-Бо на осьминогах, пять осьминогов сопровождают:
    # TODO: Сделай ездовых осьминогов, а пока тпусть так:
    'Druid 5 lvl (враг) (Тик-Бо «Робкий»)':1,
    'Druid 1 lvl (враг) (друид Тик-Бо)':6,
    #'Giant Octopus (conjured) (CR 1)':12,
    }

metadict_squads['Company-militia (демоны Кема\'Эша) (враг)'] = {
    'Commoner 1 lvl (враг) (карл)':80,
    'Commoner 1 lvl (враг) (карл-ветеран)':4,
    'Warrior 3 lvl (враг) (демон Кема\'Эша)':1,
    }

metadict_squads['Company-regular (лучники Энзифа) (враг)'] = {
    'Warrior 1 lvl (sqythian bowman)':185,
    'Warrior 2 lvl (sqythian bowman-corporal)':10,
    'Warrior 3 lvl (sqythian bowman-sergeant)':3,
    'Warrior 4 lvl (sqythian bowman-lieutenant)':1,
    }

metadict_squads['Company-regular (сариссофоры Магора) (враг)'] = {
    'Warrior 1 lvl (city pikeman)':75,
    'Warrior 2 lvl (city pikeman-corporal)':20,
    'Warrior 3 lvl (city pikeman-sergeant)':6,
    'Warrior 4 lvl (city pikeman-lieutenant)':2,
    }

metadict_squads['Company-regular (лучники Хана-Вама) (враг)'] = {
    'Warrior 1 lvl (sqythian bowman)':75,
    'Warrior 2 lvl (sqythian bowman-corporal)':10,
    'Warrior 3 lvl (sqythian bowman-sergeant)':3,
    'Warrior 4 lvl (sqythian bowman-lieutenant)':1,
    'Warrior 5 lvl (sqythian bowman-captain)':1,
    }

metadict_squads['Company-regular (пираты Кара-Яма) (конные) (враг)'] = {
    'Warrior 1 lvl (cavalry archer)':6,
    'Warrior 2 lvl (cavalry archer-corporal)':10,
    'Warrior 3 lvl (cavalry archer-sergeant)':3,
    'Warrior 4 lvl (cavalry archer-lieutenant)':1,
    }

metadict_squads['Company-regular (пращники Тик-Бо) (враг)'] = {
    'Warrior 1 lvl (balear slinger)':75,
    'Warrior 2 lvl (balear slinger-corporal)':10,
    'Warrior 3 lvl (balear slinger-sergeant)':3,
    'Warrior 4 lvl (balear slinger-lieutenant)':1,
    }

metadict_squads['Company-regular (пираты Кема-Эша) (враг)'] = {
    'Warrior 1 lvl (cilician infantry)':75,
    'Warrior 2 lvl (cilician infantry-corporal)':10,
    'Warrior 3 lvl (cilician infantry-sergeant)':3,
    'Warrior 4 lvl (cilician infantry-lieutenant)':1,
    }

#----
# Геройские отряды (армия Гая Юлия):

metadict_squads['Company-militia (гастаты Гая Юлия) (Katorjnik)'] = {
    'Commoner 1 lvl (militia spearman)':95,
    'Commoner 2 lvl (militia spearman-corporal)':5,
    'Warrior 3 lvl (militia spearman-sergeant)':1,
    }

metadict_squads['Company-regular (легионеры Гая Юлия) (Katorjnik)'] = {
    'Warrior 1 lvl (Katorjnik) (манипуларий)':75,
    'Warrior 2 lvl (Katorjnik) (ветеран)':20,
    'Warrior 3 lvl (Katorjnik) (урагос)':6,
    'Warrior 4 lvl (Katorjnik) (опцион)':2,
    #'Warrior 5 lvl (Katorjnik) (центурион)':1,
    }

metadict_squads['Band-hero (преторианцы Гая Юлия) (Katorjnik)'] = {
    'Fighter 5 lvl (Katorjnik) (Гай Юлий)':1,
    'Fighter 1 lvl (Katorjnik) (преторианец)':6,
    }

#----
# Геройские отряды (армия Фарама):

metadict_squads['Company-regular (лучники Фарама) (Mordodrukow)'] = {
    'Warrior 1 lvl (Mordodrukow) (рядовой)':85,
    'Warrior 2 lvl (Mordodrukow) (ветеран)':10,
    'Warrior 3 lvl (Mordodrukow) (сержант)':3,
    'Warrior 4 lvl (Mordodrukow) (лейтенант)':1,
    }

metadict_squads['Band-hero (жрецы Фарама) (Mordodrukow)'] = {
    'Cleric 5 lvl (Mordodrukow) (Фарам «Друг Богов»)':1,
    'Cleric 2 lvl (Mordodrukow) (жрец Зевса) (боевой)':2,
    'Cleric 2 lvl (Mordodrukow) (жрец Зевса) (лекарь)':2,
    #'Fighter 5 lvl (Mordodrukow) (Лонгин)':1,
    'Fighter 2 lvl (Mordodrukow) (темплар Зевса)':2,
    }

metadict_squads['Band-hero (снайпер Лонгин) (Mordodrukow)'] = {
    # Отдельно от команды Фарама:
    'Fighter 5 lvl (Mordodrukow) (Лонгин)':1,
    }

#----
# Геройские отряды (армия Патрокла):

metadict_squads['Band-hero (жрецы Патрокла) (Vened)'] = {
    'Cleric 5 lvl (Vened) (Патрокл «Македонянин»)':1,
    'Cleric 1 lvl (Vened) (жрец домена войны)':10,
    #'Druid 5 lvl (Vened) (Брат Патрокла)':1,
    #'Druid 1 lvl (Vened) (друид Патрокла)':2,
    }

metadict_squads['Band-hero (друиды Патрокла) (Vened)'] = {
    'Druid 5 lvl (Vened) (Брат Патрокла)':1,
    'Druid 1 lvl (Vened) (друид Патрокла)':2,
    }

metadict_squads['Company-regular (онагры Патрокла) (Vened)'] = {
    'Warrior 3 lvl (siege engineer-apprentice) (onager-fire)':7,
    'Warrior 4 lvl (siege engineer-master) (onager-fire)':1,
    }

metadict_squads['Company-militia (скорпионы Патрокла) (Vened)'] = {
    # TODO: переименуй в тяжёлых арбалетчиков для следующего боя.
    # Отряд ополчения с тяжёлыми арбалетами:
    'Commoner 1 lvl (militia heavy crossbowman)':80 + dice_throw('3d12'),
    'Commoner 2 lvl (militia heavy crossbowman-corporal)':5,
    'Warrior 3 lvl (militia heavy crossbowman-sergeant)':1,
    #'Warrior 4 lvl (militia heavy crossbowman-lieutenant)':1,
    }

metadict_squads['Company-regular (сариссофоры Патрокла) (Vened)'] = {
    'Warrior 1 lvl (city pikeman)':85,
    'Warrior 2 lvl (city pikeman-corporal)':10,
    'Warrior 3 lvl (city pikeman-sergeant)':3,
    'Warrior 4 lvl (city pikeman-lieutenant)':1,
    }

#----
# Геройские отряды (армия Протесилая):

metadict_squads['Company-regular (сариссофоры Протесилая) (Тзаангор)'] = {
    'Warrior 1 lvl (Тзаангор) (гипасист)':75,
    'Warrior 2 lvl (Тзаангор) (ветеран)':20,
    'Warrior 3 lvl (Тзаангор) (ур-лодакос)':6,
    'Warrior 4 lvl (Тзаангор) (лодакос)':2,
    }

metadict_squads['Band-hero (паладины Протесилая) (Тзаангор)'] = {
    'Paladin 5 lvl (Тзаангор) (Протесилай II, «Держатель щита»)':1,
    'Paladin 1 lvl (Тзаангор) (паладины)':6,
    }

#----
# Геройские отряды (армия Ианты):

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
    # Ианта отправила лейтенанта в отряд Токсотаев. Стрелками командует сама.
    'Commoner 1 lvl (Vaarsuvius) (токсотай)':95,
    'Commoner 2 lvl (Vaarsuvius) (токсотай-ветеран)':5,
    'Warrior 4 lvl (Vaarsuvius) (стрелок-лейтенант)':1,
    'Warrior 3 lvl (Vaarsuvius) (меткий стрелок-отставник)':1,
    }

metadict_squads['Company-regular (лучники Ианты) (Vaarsuvius)'] = {
    # Ианта отправила лейтенанта в отряд Токсотаев. Стрелками командует сама.
    'Warrior 1 lvl (Vaarsuvius) (стрелок)':85,
    'Warrior 2 lvl (Vaarsuvius) (стрелок-ветеран)':10,
    'Warrior 3 lvl (Vaarsuvius) (меткий стрелок)':3,
    'Druid 5 lvl (Vaarsuvius) (Ианта «Дочь бури»)':1,
    #'Warrior 4 lvl (Vaarsuvius) (стрелок-лейтенант)':1,
    #'Warrior 5 lvl (Vaarsuvius) (стрелок-капитан)':1,
    }

metadict_squads['Company-regular (дочери медведицы Ианты) (Vaarsuvius)'] = {
    'Warrior 1 lvl (Vaarsuvius) (дочерь медведицы)':85,
    'Warrior 2 lvl (Vaarsuvius) (ветеран)':10,
    'Warrior 3 lvl (Vaarsuvius) (сержант)':3,
    'Warrior 5 lvl (Vaarsuvius) (Филлис)':1,
    'Warrior 4 lvl (Vaarsuvius) (первый помощник)':1,
    }

metadict_squads['Squad-hero (друиды Ианты) (Vaarsuvius)'] = {
    # TODO: Добавь отряду "осьминожек" командира Психею:
    # Друидки Ианты:
        # - Хлоя (при Ианте, её дочь)
        # - Иокаста (с Филлис)
        # - Мелина (с Фарамом)
        # - Агата (дочь Атанасии "Бессмертной", погибла на "Кручах")
        # - Психея (с осьминожками на дне)
        # - Психея (глава "Подводной стражи" осьминожек, садист)
        #     - Мелина (в "Подводной страже", любит Ксантию)
        #     - Роксана (в "Подводной страже", не говорит, нет языка)
        #     - Ксантия (в "Подводной страже", любит Мелину)
    #'Druid 5 lvl (Vaarsuvius) (Ианта «Дочь бури»)':1,
    'Druid 2 lvl (Vaarsuvius) (друид Психея)':1,
    'Druid 2 lvl (Vaarsuvius) (друид Артемиды)':7,
    #'Druid 2 lvl (Vaarsuvius) (друид Артемиды)':12,
    }

metadict_squads['Squad-hero (друид Агата) (Vaarsuvius)'] = {
    'Druid 2 lvl (Vaarsuvius) (друид Агата)':1,
    }

#----
# Геройские отряды (армия Артаманаха):

metadict_squads['Band-hero (снайперы Артаманаха) (ArbitraryNickname)'] = {
    'Fighter 5 lvl (ArbitraryNickname) (Артаманах Рыбник)':1,
    'Fighter 1 lvl (ArbitraryNickname) (снайпер)':6,
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
# Рекруты:

metadict_squads['Company-dummy (zombies)'] = {
    'Zombie (CR 1/4)':80 + dice_throw('1d12'),
    'Wight (CR 3)':1,
    }

metadict_squads['Company-dummy (bandits)'] = {
    'Bandit (CR 1/8)':80 + dice_throw('1d12'),
    'Thug (CR 1/2)':4,
    'Veteran (CR 3)':1,
    }

metadict_squads['Company-dummy (sentinels)'] = {
    'Sentinel (CR 1/8)':80 + dice_throw('1d12'),
    'Veteran (CR 3)':1,
    }

metadict_squads['Company-dummy (goblins)'] = {
    'Goblin (CR 1/4)':80 + dice_throw('1d12'),
    'Goblin Boss (CR 1)':3,
    }

metadict_squads['Company-dummy (hobgoblins)'] = {
    'Hobgoblin (CR 1/2)':80 + dice_throw('1d12'),
    'Bugbear (CR 1)':3,
    'Hobgoblin-captain (CR 3)':1,
    }

metadict_squads['Company-dummy (orks)'] = {
    'Ork (CR 1/2)':80 + dice_throw('1d12'),
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

metadict_squads['Company-regular (slingers-balear)'] = {
    'Warrior 1 lvl (balear slinger)':80 + dice_throw('1d12'),
    'Warrior 2 lvl (balear slinger-corporal)':10,
    'Warrior 3 lvl (balear slinger-sergeant)':3,
    'Warrior 4 lvl (balear slinger-lieutenant)':1,
    'Warrior 5 lvl (balear slinger-captain)':1,
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

