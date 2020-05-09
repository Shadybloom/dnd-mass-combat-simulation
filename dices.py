#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Скрипт бросает игральные кости и выдаёт результат.
# Один бросок шестигранной кости:
# dices 1d6
# Четыре броска восьмигранной кости:
# dices 4d8
# Тысяча бросков тридцатигранной кости:
# dices 1000d30

import random
import argparse
from collections import OrderedDict

#-------------------------------------------------------------------------
# Опции:

# Стандартная кость:
DICE = 20
# Число бросков стандартной кости:
DICE_THROWS = 1

#-------------------------------------------------------------------------
# Аргументы командной строки:

def create_parser():
    """Список доступных параметров скрипта."""
    parser = argparse.ArgumentParser()
    parser.add_argument('dice_string',
                        action='store', type=str, nargs='*', default='',
                        help='Кость D&D, например 2d6 (по умолчанию 1d20)'
                        )
    return parser

#-------------------------------------------------------------------------
# Функции:

def dice_range (n1, n2, throws=1):
    """Возвращает рандомное число в диапазоне."""
    d_sum = 0
    while throws > 0:
        # randint: n1 <= d <= n2
        d = random.randint(n1, n2)
        throws -= 1
        d_sum += d
    return d_sum

def dice_throw (dice_string='1d20'):
    """Бросает любую кость в формате D&D.
    
    Например, dice_string(throw='3d6')
    """
    # Дробим строку по разделителю 'd' на два элемента.
    throws_dice_list = (dice_string.split('d'))
    #print(throws_dice_list)
    # Сначала число бросков, затем число граней кости.
    throws = int(throws_dice_list[0])
    dice = int(throws_dice_list[1])
    output = dice_range(1, dice, throws)
    return output

def throw_d2(throws=1):
    # Функции ниже для внешних вызовов.
    # Сам скрипт использут только dice_range
    """Бросаем двухгранную кость (монетку)."""
    d = dice_range(1, 2, throws)
    return d

def throw_d3(throws=1):
    d = dice_range(1, 3, throws)
    return d

def throw_d4(throws=1):
    """Бросаем четырёхгранную кость."""
    d = dice_range(1, 4, throws)
    return d

def throw_d6(throws=1):
    """Бросаем шестигранную кость."""
    d = dice_range(1, 6, throws)
    return d

def throw_d8(throws=1):
    """Бросаем восьмигранную кость."""
    d = dice_range(1, 8, throws)
    return d

def throw_d10(throws=1):
    """Бросаем десятигранную кость."""
    d = dice_range(1, 10, throws)
    return d

def throw_d12(throws=1):
    """Бросаем двенацтигранную кость."""
    d = dice_range(1, 12, throws)
    return d

def throw_d20(throws=1):
    """Бросаем двадцатигранную кость."""
    d = dice_range(1, 20, throws)
    return d

def throw_d100(throws=1):
    """Бросаем стогранную кость (проценты)."""
    d = dice_range(1, 100, throws)
    return d

def dice_throw_advantage (dice_string = '1d20', advantage=False, disadvantage=False):
    """Бросаем кость с учётом преимуществ/помех.
    
    Учитываются помехи/преимущества из правил D&D 5
    """
    throw_first = dice_throw(dice_string)
    throw_second = dice_throw(dice_string)
    if advantage == True and disadvantage == True:
        # Если есть и помеха, и преимущество, делается обычный бросок:
        # https://www.dandwiki.com/wiki/5e_SRD:Advantage_and_Disadvantage
        throw = throw_first
    elif advantage == True:
        # Преимущество позволяет выбрать лучший бросок:
        throw = max(throw_first, throw_second)
    elif disadvantage == True:
        # Помеха заставляет взять худший:
        throw = min(throw_first, throw_second)
    else:
        throw = throw_first
    return throw

def d20_check(modifiers = 0, difficulty = 0,
        advantage=False, disadvantage=False,
        take10=False, take20=False):
    """Бросаем d20 с модификаторами против сложности задачи. В выводе резултат и бросок
    
    1) Учитываются помехи/преимущества из правил D&D 5
    2) Возможна повседневная подстановка 10 или 20 вместо броска d20.
    """
    throw_first = throw_d20()
    throw_second = throw_d20()
    if advantage == True and disadvantage == True:
        # Если есть и помеха, и преимущество, делается обычный бросок:
        # https://www.dandwiki.com/wiki/5e_SRD:Advantage_and_Disadvantage
        throw = throw_first
    elif advantage == True:
        # Преимущество позволяет выбрать лучший бросок:
        throw = max(throw_first, throw_second)
    elif disadvantage == True:
        # Помеха заставляет взять худший:
        throw = min(throw_first, throw_second)
    else:
        throw = throw_first
    # В повседневных делах d20 = 10. При уйме времени/возможностей на попытки d20 = 20
    if take10 == True:
        throw = 10
    elif take20 == True:
        throw = 20
    # Возвращаем резульатат и сам бросок (может выпасть 1, или 20, что многое меняет).
    result = throw + modifiers - difficulty
    return result, throw

def dice_throw_number (dice_string = '1d20', advantage=False, disadvantage=False, number=10000, mod=0):
    """Бросаем кучу костей, добавляем модификатор и выводим распределение.
    
    Учитываются помехи/преимущества из правил D&D 5
    """
    throws = 0
    dict_throws = {}
    while throws < number:
        throws +=1
        throw_first = dice_throw(dice_string)
        throw_second = dice_throw(dice_string)
        if advantage == True and disadvantage == True:
            # Если есть и помеха, и преимущество, делается обычный бросок:
            # https://www.dandwiki.com/wiki/5e_SRD:Advantage_and_Disadvantage
            throw = throw_first
        elif advantage == True:
            # Преимущество позволяет выбрать лучший бросок:
            throw = max(throw_first, throw_second)
        elif disadvantage == True:
            # Помеха заставляет взять худший:
            throw = min(throw_first, throw_second)
        else:
            throw = throw_first
        throw_mod = throw + mod
        if throw_mod not in dict_throws:
            dict_throws[throw_mod] = 1
        elif throw_mod in dict_throws:
            dict_throws[throw_mod] += 1
    dict_percent = {}
    for key, el in dict_throws.items():
        dict_percent[key] = round((el / number * 100), 1)
    dict_percent = OrderedDict(reversed(sorted(dict_percent.items(),key=lambda x: x)))
    return dict_percent

#-------------------------------------------------------------------------
# Тело программы:

if __name__ == '__main__':
    # Создаётся список аргументов скрипта:
    parser = create_parser()
    namespace = parser.parse_args()
    # Бросаем кость из поля ввода:
    if namespace.dice_string:
        result = dice_throw(dice_string=namespace.dice_string[0])
    else:
        throws = DICE_THROWS
        dice = DICE
        result = dice_range(1, dice, throws)
    print(result)

    # Средняя численность племени:
    #numbers_list = []
    #for n in range (0,1000):
    #    #tribe_number = dice_throw('2d12') * 100 + 200
    #    tribe_number = dice_throw('5d12') * 100 + 200
    #    #tribe_number = dice_throw('9d12') * 100 + 200
    #    #tribe_number = dice_throw('15d12') * 100 + 200
    #    numbers_list.append(tribe_number)
    #medial_number = sum(numbers_list) / len(numbers_list)
    #print(medial_number, max(numbers_list), min(numbers_list))
