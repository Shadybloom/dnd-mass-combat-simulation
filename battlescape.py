#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import math
import random
from collections import namedtuple
from collections import OrderedDict
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

import timeit
#import numpy
from skimage import draw

import dices
from data import maps
from squad_generation import *

#-------------------------------------------------------------------------
# Функции:

def distance_measure(firs_point, second_point):
    """Дистанция между двумя точками на плоскости.
    
    bresenham делает то же самое, плюс даёт путь взгляда.
    Но distance_measure быстрее.
    """
    p1 = firs_point
    p2 = second_point
    distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
    return distance

def prolong_ray(source_point, target_point, ray_distance):
    """Возвращает конечную точку отрезка по двум известным точкам.

    - Используется для заклинаний вроде Lightning_Bolt, которые бьют дальше цели.
    
    Как это работает:
    1. Координаты цели относительно кастера: x2 - x1; y2 - y1
    2. Пропорциональное смещение: (x,y) * (дальность_луча/дистанция_до_цели)
    3. Наложение на плоскость: x + x1; y + y1
    """
    x1,y1 = source_point
    x2,y2 = target_point
    # Координаты вектора (цели относительно кастера)
    x = x2 - x1
    y = y2 - y1
    # Вытягиваем вектор, пропорционально смещая его конечную точку.
    target_distance = distance_measure(source_point, target_point)
    proportional_correction = ray_distance / target_distance
    x_new = x * proportional_correction
    y_new = y * proportional_correction
    # Наносим конечную точку вектора на плоскость:
    x_end = x_new + x1
    y_end = y_new + y1
    end_point = (round(x_end), round(y_end))
    return end_point

def find_cone_coordinates(source_point, target_point, ray_distance):
    """Находит координаты конечных точек конуса по исходной точке и дистанции.

    - Конус на плоскости, это равносторонний треугольник.
    """
    # Вектор противонаправлен, от цели к источнику:
    x1,y1 = target_point
    x2,y2 = source_point
    # Координаты вектора:
    x = x2 - x1
    y = y2 - y1
    # Поворачиваем вектор на 90°
    x,y = y,-x
    # Находим длину стороны треугольника и корректируем длину вектора:
    triangle_side = f_triangle(ray_distance, 90, 60)
    vector_lenght = triangle_side / 2
    proportional_correction = vector_lenght / ray_distance
    x_new = x * proportional_correction
    y_new = y * proportional_correction
    # Наносим конечную точку вектора на плоскость:
    x_end = x_new + x1
    y_end = y_new + y1
    end_point = (round(x_end), round(y_end))
    # Находим вторую точку:
    end_point_2 = prolong_ray(end_point, target_point, triangle_side)
    return source_point, end_point, end_point_2

def f_triangle (side_b, angle_a, angle_b):
    """Сторона треугольника по двум углам и другой стороне.

    Теорема синусов:
    # http://www-formula.ru/lengthpartiestriangle
    a = (b * sin(α))/sin(β)
    Где:
    b - известная сторона
    α - угол противолежащий от стороны a и прилежащий к стороне b.
    β - угол противолежащий от стороны b и прилежащий к стороне a.
    """
    # math.sin ждёт угла в радианах, поэтому преобразуем градусы с помощью math.radians
    side_a = abs(side_b * math.sin(math.radians(angle_a))) / math.sin(math.radians(angle_b))
    return side_a

def inside_triangle (triangle_coord_1, triangle_coord_2, triangle_coord_3, point_coord):
    """Проверяем, в треугольнике ли точка.
    
    - Треугольник по трём координатам, find_cone_coordinates
    """
    x1,y1 = triangle_coord_1
    x2,y2 = triangle_coord_2
    x3,y3 = triangle_coord_3
    xp,yp = point_coord
    c1 = (x2-x1)*(yp-y1)-(y2-y1)*(xp-x1)
    c2 = (x3-x2)*(yp-y2)-(y3-y2)*(xp-x2)
    c3 = (x1-x3)*(yp-y3)-(y1-y3)*(xp-x3)
    if (c1<0 and c2<0 and c3<0) or (c1>0 and c2>0 and c3>0):
        return True
    else:
        return False

def inside_circle(point, circle_center, circle_radius):
    '''
    Here is a Python function that checks if a point (x, y)
    is inside the circle centered at (a, b) with radius r.
    http://schoolcoders.com/wiki/Testing_for_point_inside_circle_(Python)
    '''
    # Чуть прибавляем, чтобы захватить границу круга.
    circle_radius += 0.5
    x, y = point
    a, b = circle_center
    r = circle_radius
    return (x - a)*(x - a) + (y - b)*(y - b) < r*r

def sight_line_to_list(soldier_place, enemy_place):
    """Обёртка для bresenham"""
    x0,y0,x1,y1 = soldier_place[0], soldier_place[1], enemy_place[0], enemy_place[1]
    sight_line = list(bresenham(x0,y0, x1,y1))
    return sight_line

def draw_line(x0, y0, x1, y1):
    """Координаты линии с помощью skimage.draw
    
    В выводе список с координатами точек.
    bresenham быстрее в 1.5 раза.
    """
    rr, cc = draw.line(x0, y0, x1, y1)
    #result = [(rr[i], cc[i]) for i in range(0, len(rr))]
    result = list(zip(rr,cc))
    return result

def bresenham(x0, y0, x1, y1):
    """Yield integer coordinates on the line from (x0, y0) to (x1, y1).

    Input coordinates should be integers.

    The result will contain both the start and the end point.

    https://pypi.org/project/bresenham/
    https://github.com/encukou/bresenham
    """
    dx = x1 - x0
    dy = y1 - y0

    xsign = 1 if dx > 0 else -1
    ysign = 1 if dy > 0 else -1

    dx = abs(dx)
    dy = abs(dy)

    if dx > dy:
        xx, xy, yx, yy = xsign, 0, 0, ysign
    else:
        dx, dy = dy, dx
        xx, xy, yx, yy = 0, ysign, xsign, 0

    D = 2*dy - dx
    y = 0

    for x in range(dx + 1):
        yield x0 + x*xx + y*yx, y0 + x*xy + y*yy
        if D >= 0:
            y += 1
            D -= 2*dx
        D += 2*dy

def clear_ansii_string(bad_string):
    """Чистка строки от спецсимволов ANSI sequences"""
    reaesc = re.compile(r'\x1b[^m]*m')
    cler_string = reaesc.sub('', bad_string)
    return cler_string

def nyan_list_creator(bad_list, replace = ' '):
    """Замена повторяющихся элементов в списке.
    
    Если следующий элемент похож на предыдущий,
    Он заменяется на другой. И первый элемент тоже.
    """
    # Создаём матрицу True/False (менять/не_менять):
    replace_matrix = [ bad_list[i]==bad_list[i-1] for i in range(len(bad_list)) ]
    nyan_list = []
    for n, el in enumerate(replace_matrix):
        if not el and bad_list[n] > 0:
            nyan_list.append(str(bad_list[n]))
        else:
            nyan_list.append(replace)
    return nyan_list

def print_ascii_map(ascii_map):
    """Вывод карты с числами строк и столбцов.

    Создан для таких вот ASCII-карт:
    example_map = (
            '...............',
            '.############..',
            '.#.............',
            '.#....@........',
            '...............',
            )
    Цветной вывод в ANSI sequences
    https://en.wikipedia.org/wiki/ANSI_escape_code#8-bit
    """
    # Чтобы измерить длину строки нужно очистить её от меток ANSI:
    length = len(clear_ansii_string(ascii_map[0]))
    # Метки столбцов (максимум 99):
    mark_list = [(x, y) for x in range(10) for y in range(10)]
    mark_list = mark_list[:length]
    string_top, string_bottom = '',''
    list_top = []
    for x in mark_list:
        list_top.append(x[0])
        string_top += str(x[0])
        string_bottom += str(x[1])
    list_top = nyan_list_creator(list_top, replace = ' ')
    string_top = ''.join(list_top)
    # Цветной вывод в ANSI sequences:
    string_top = '\x1b[33m' + '\x1b[48;5;8m' + string_top + '\x1b[0m'
    string_bottom = '\x1b[33m' + '\x1b[1m' + string_bottom + '\x1b[0m'
    print(string_top)
    print(string_bottom)
    # Вывод строк карты, тут всё гораздо проще:
    for y, line in enumerate(ascii_map, 0):
        y = '\x1b[33m' + '\x1b[1m' + str(y) + '\x1b[0m'
        print(line, y)

# ----

class battlescape():
    """Создаёт поле боя из карты в псевдографике.
    
    Ключевые методы:
    - create_battlespace -- создаёт поле боя из ASCII-карты.
    - gen_battlemap -- возвращает текущую карту боя в цветном ASCII.
    - recon -- осмотр определённой зоны (из центра, или со стороны)
    - danger_sense -- оценка опасности зоны (сила своих/сила врагов)
    - find_danger_zones -- находит зоны наибольшей концентрации врага.
    Также есть поиск пути и оценка видимости.
    """
    # Стороны конфликта (по умолчанию):
    ally_side = 'BLUEFOR'
    enemy_side = 'OPFOR'
    battlespace_objects = {
            # Хорошая местность:
            # Названия местности должны быть в начале списка:
            '.':['ground','good_terrain'],
            ',':['grass','good_terrain'],
            # Сложная местность (скорость 50%):
            '%':['bushes','rough_terrain'],
            ':':['hill','height','rough_terrain'],
            ';':['slope','height','rough_terrain'],
            # Защищённая местность (cover 1/2):
            't':['small_tree','cover_terrain'],
            '^':['small_house','roof','cover_terrain'],
            '$':['big_house','height','roof','cover_terrain'],
            '=':['barrikade','cover_terrain'],
            # Недоступная местность (total_cover):
            '#':['dungeon_wall','total_cover_terrain','stop_terrain','zone_border'],
            'T':['big_tree','total_cover_terrain','stop_terrain','zone_border'],
            # Недоступная местность (море, реки, каналы и ямы):
            '|':['wall','stop_terrain','zone_border'],
            '~':['sea','water','stop_terrain', 'zone_border'],
            'P':['pond','water','stop_terrain','zone_border'],
            'R':['river','water','stop_terrain','zone_border'],
            '_':['ditch','stop_terrain','zone_border'],
            'o':['pit','stop_terrain','zone_border'],
            # Ловушки на карте:
            '*':['caltrops','good_terrain'],
            's':['smoke','obscure_terrain','good_terrain'],
            #'d':['darkness','good_terrain',],
            #'f':['fire','stop_terrain','zone_border'],
            # Позиции войск на карте:
            # Это границы зон спавна, каждая принадлежит указанному отряду:
            '-':['horisontal_zone_border','zone_border','good_terrain'],
            #'!':['vertical_zone_border','barrikade','cover_terrain','zone_border'],
            '!':['vertical_zone_border','zone_border','good_terrain'],
            # Это указатели на зону спавна. Указатель должен стоять в границах зоны.
            # Внутри зоны должен быть только один указатель. Иначе отряды смешаются.
            '0':['zone_0','spawn_zone','good_terrain'],
            '1':['zone_1','spawn_zone','good_terrain'],
            '2':['zone_2','spawn_zone','good_terrain'],
            '3':['zone_3','spawn_zone','good_terrain'],
            '4':['zone_4','spawn_zone','good_terrain'],
            '5':['zone_5','spawn_zone','good_terrain'],
            '6':['zone_6','spawn_zone','good_terrain'],
            '7':['zone_7','spawn_zone','good_terrain'],
            '8':['zone_8','spawn_zone','good_terrain'],
            '9':['zone_9','spawn_zone','good_terrain'],
            # Названия бойцов должны быть в конце списка:
            'w':['ground','good_terrain','spawn','warrior'],
            'e':['ground','good_terrain','spawn','elite_warrior'],
            'c':['ground','good_terrain','spawn','commander'],
            'a':['ground','good_terrain','spawn','archer'],
            'M':['ground','good_terrain','spawn','mount'],
            # Укреплённые позиции (лучники на возвышенностях):
            'W':['barrikade','cover_terrain','spawn','warrior'],
            'E':['barrikade','cover_terrain','spawn','elite_warrior'],
            #'C':['barrikade','cover_terrain','spawn','commander'],
            #'A':['barrikade','cover_terrain','spawn','archer'],
            'C':['barrikade','height','cover_terrain','spawn','commander'],
            'A':['barrikade','height','cover_terrain','spawn','archer'],
            }
    # Выбор точек спавна определяется ролью бойца (behavior) в metadict_chars
    spawn_types = (
            'warrior',
            'elite_warrior',
            'commander',
            'archer',
            'mount',
            )
    # Относительная опасность врагов (определяет тактику):
    # ------------------------------------------------------------
    # Боец оценивает, сколько вокруг него союзников и врагов.
    # И после этого решает: атаковать, защищаться, или отступать.
    dict_danger = {
            'commander':3,
            'elite_warrior':2,
            'warrior':1,
            'archer':1,
            'mount':1,
            }
    # Для поиска пути:
    finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
    # Хорошая штука эти namedtuple. Зададим их здесь.
    namedtuple_spawn = namedtuple('spawn',['place','zone','type'])
    namedtuple_target = namedtuple('target',['side','type','place','distance','cover','uuid'])
    namedtuple_visibility = namedtuple('visibility',['distance','cover','visibility'])
    namedtuple_place = namedtuple('place',['place','free','rough','units'])

    def create_battlespace(self, battle_map = None):
        """Рисунок поля боя в координатную плоскость.
        
        - Детали рисунка (деревья, стены) становятся элементами словаря.
        - Создаётся сетка препятствий для алгоритма поиска пути.
        - Пункты спавна переносятся в отдельный список.
        """
        # Работаем:
        self.battle_map = battle_map
        self.battle_map_length = len(self.battle_map[0])
        self.battle_map_height = len(self.battle_map)
        self.dict_battlespace = self.map_to_dict(self.battle_map)
        self.matrix = self.map_to_matrix(self.battle_map, self.dict_battlespace)
        # Размечаем зоны и пункты спавна отдельных солдат:
        self.spawn_zones_dict = self.find_spawn_zones()
        self.set_spawn_zones(self.spawn_zones_dict)
        self.spawn_list = self.find_spawn_points()
        #for place,descript in self.dict_battlespace.items():
        #    print(place,descript)
        #for spawn in self.spawn_list:
        #    print(spawn)

    def map_to_dict(self, battle_map):
        """Создаёт словарь тегов для символов карты.

        Ключевые элементы battlespace_objects:
        1) good/rough/cover/stop_terrain -- для поиска пути.
        2) grass/bushes/tree/wall -- для вывода данных.
        3) spawn/spawn_zone -- начальные позиции сторон.
        4) zone_border -- границы зон спавна.
        5) exit -- точки выхода для беглецов.
        """
        ally_side = self.ally_side
        enemy_side = self.enemy_side
        dict_battlespace = {}
        for y, line in enumerate(battle_map, 0):
            for x, el in enumerate(line, 0):
                # Пиктограммы с карты превращаются в списки тегов (стена, камни, т.д.)
                dict_battlespace[x,y] = list(self.battlespace_objects.get(el,[]))
                # Обозначаем выходы с поля боя (края карты):
                if y == 0 or y == self.battle_map_height - 1\
                        or x == 0 or x == self.battle_map_length - 1:
                    if not 'stop_terrain' in dict_battlespace[x,y]\
                            and not 'zone_border' in dict_battlespace[x,y]:
                        dict_battlespace[x,y].append('exit')
        #for key,value in dict_battlespace.items():
        #    print(key,value)
        return dict_battlespace

    def set_spawn_zones(self, spawn_zones_dict):
        """Размечает зоны на поле боя.
        
        Все незанятые stop_terrain точки в зоне получают метку с номером зоны.
        """
        for zone_name, field in spawn_zones_dict.items():
            for point in field:
                self.dict_battlespace[point].append(zone_name)

    def map_to_matrix(self, battle_map, dict_battlespace, water_walk = False):
        """Создаёт сетку для алгоритма поиска пути.

        Это двухмерный массив с числами, который повторяет карту.

        Числа обозначают сложность пути:
        0 -- недоступная территория (ров, стены)
        1 -- лучшая для пути территория (поле, мостовая)
        2-9 -- неудобная для пути территория (кусты, камни, баррикады)
        Эти же числа используются для расчёта видимости и бонусов укрытия.
        """
        matrix = []
        for y, line in enumerate(battle_map, 0):
            matrix.append([])
            for x, el in enumerate(line, 0):
                # Морские существа плавают:
                if 'water' in dict_battlespace[x,y]\
                        and 'stop_terrain' in dict_battlespace[x,y]\
                        and water_walk:
                    matrix[y].append(1)
                # Ноль, это недоступная территория:
                elif 'stop_terrain' in dict_battlespace[x,y]:
                    matrix[y].append(0)
                # Единица -- оптимум, числа выше -- сложней путь:
                elif 'good_terrain' in dict_battlespace[x,y]:
                    matrix[y].append(1)
                elif 'rough_terrain' in dict_battlespace[x,y]:
                    matrix[y].append(4)
                elif 'cover_terrain' in dict_battlespace[x,y]:
                    matrix[y].append(8)
                # TODO: не хватает реакции на бойцов
                # ------------------------------------------------------------
                # Перебирай dict_battlespace, пока не найдётся type(tuple)
                # Если кортеж найдётся, то считается за stop_terrain.
                # Нет, тогда алгоритм поиска перестанет работать.
                # Просто добавь сложности (заодно это станет помехой обзору).
                # Тогда нужно будет после каждого движения пересоздавать матрицу.
                # Помни! Помеха обзору от людей уже учитывается в calculate_enemy_cover
                # ------------------------------------------------------------
                else:
                    #print(dict_battlespace[x,y])
                    print('ERROR battlespace_objects неизвестный символ, y:{0},x:{1} tile:{2}'.format(y,x,el))
                    matrix[y].append(0)
        #for y, line in enumerate(battle_map, 0):
        #    print(line, y)
        #for el in matrix:
        #    print(el)
        return matrix

    def spawn_zone_names_to_list(self):
        """Создаёт список зон спавна"""
        zone_name_list = []
        for descript in self.battlespace_objects.values():
            if 'spawn_zone' in descript:
                zone_name_list.append(descript[0])
        for number in range(10):
            zone_name = 'zone_0{n}'.format(n = number)
            zone_name_list.append(zone_name)
        for number in range(100):
            zone_name = 'zone_{n}'.format(n = number)
            zone_name_list.append(zone_name)
        zone_name_list = list(sorted(set(zone_name_list)))
        return zone_name_list

    def find_spawn_zones(self):
        """Находит на карте пространства зон спавна.
        
        - Можно указать двузначные зоны (01, 11, 56, т.д.)
        - Обрабатывается только первый указатель зоны. Один указатель -- одна зона.
        - Сначала находим указатель зоны, а затем делаем обход в ширину до границ зоны.
        """
        spawn_zones_dict = {}
        zone_name_list = self.spawn_zone_names_to_list()
        for zone_name in zone_name_list:
            for place, descript in self.dict_battlespace.items():
                if zone_name in descript:
                    next_place = (place[0] + 1, place[-1])
                    # Двузначные зоны спавна (01, 56, т.д.)
                    if not next_place[0] > self.battle_map_length:
                        for zone_name_next in zone_name_list:
                            if zone_name_next in self.dict_battlespace[next_place]:
                                zone_name_combine = zone_name + zone_name_next[-1]
                                zone_field = self.find_points_in_zone(place)
                                spawn_zones_dict[zone_name_combine] = zone_field
                                break
                    # Если номер зоны найден, то поиск прерывается:
                    zone_field = self.find_points_in_zone(place)
                    spawn_zones_dict[zone_name] = zone_field
                    #break
        return spawn_zones_dict

    def find_spawn_points(self):
        """Находит на карте точки спавна наших/врагов.
        
        К каждой точке прилагается тип бойца и указатель зоны спавна.
        """
        spawn_list = []
        zone_name_list = self.spawn_zone_names_to_list()
        for place, value in self.dict_battlespace.items():
            for zone_name in zone_name_list:
                for spawn_type in self.spawn_types:
                    if spawn_type in value and zone_name in value:
                        spawn = self.namedtuple_spawn(place, zone_name, spawn_type)
                        spawn_list.append(spawn)
        return spawn_list

    def calculate_enemy_cover(self, soldier_coordinates, enemy_coordinates, max_obstacle = 10):
        """Оценка видимости врага.
        
        Как это работает:
        - Находим координаты всех квадратов на линии до цели.
        - Суммируем помехи взгляду, что даёт каждый квадрат.
        Возвращает дистанцию, прикрытие, видимость (True/False).

        Логика помех:
        - Цель за стеной -- невидима.
        - Цель за 3x кустами -- невидима.
        - Цель на возвышенности -- заметна, если не за стеной.
        - Цель внизу -- заметна с возвышенности, если не за стеной.

        Используется Bresenham's line algorithm:
        https://en.wikipedia.org/wiki/Bresenham's_line_algorithm
        https://pypi.org/project/bresenham/
        https://github.com/encukou/bresenham
        
        Заметки:
        http://www.roguebasin.com/index.php?title=Line_of_Sight
        http://www.roguebasin.com/index.php?title=Bresenham%27s_Line_Algorithm#Python
        """
        # TODO: отдели помехи взгляду от матрицы поиска пути:
        matrix = self.matrix
        dict_battlespace = self.dict_battlespace
        # Bresenham's line algorithm:
        sight_line = sight_line_to_list(soldier_coordinates, enemy_coordinates)
        # Убираем из линии первый квадрат (там наш боец)
        # Или не убираем, если ищем взглядом своих (в том числе себя)
        if len(sight_line) > 1:
            soldier_point = sight_line.pop(0)
        else:
            soldier_point = sight_line[0]
        enemy_point = sight_line[-1]
        #print(soldier_coordinates, enemy_coordinates)
        #print(soldier_point,enemy_point)
        distance = len(sight_line)
        cover_sum = 0
        visibility = True
        for n, coordinates in enumerate(sight_line):
            x,y = coordinates[0],coordinates[1]
            matrix_point = matrix[y][x]
            # ЗАМЕТКА: видимость
            # ------------------------------------------------------------
            # Стена полностью перекрывает видимость. Прочие преграды относительно.
            # Помехи взгляду суммируются. Каждый пункт cover_sum, это 10% прикрытия.
            # Для простоты данные берём не из dict_battlespace, а из матрицы поиска пути.
            # Люди тоже дают помеху взгляду. Но с помехами местности это не складывается.
            # 5-я шеренга строя на ровной как стол местности уже не видит врагов.
            # ------------------------------------------------------------
            #print(coordinates, dict_battlespace[coordinates], matrix_point)
            # TODO: raycasting извне карты невозможен. Учти нижний-правый угол карты.
            # Это может случиться, когда точка попадания катапульты вне края карты.
            if x < 0 or y < 0:
                visibility = False
                cover_sum = max_obstacle
                break
            # Стены подземелий перегораживают взгляд:
            elif 'total_cover_terrain' in dict_battlespace[coordinates]:
                visibility = False
                cover_sum = max_obstacle
                break
            # Облака дыма/тумана мешают видеть:
            elif 'obscure_terrain' in dict_battlespace[coordinates] and distance > 2:
                visibility = False
                cover_sum = max_obstacle
                break
            elif matrix_point >1:
                cover_sum += matrix_point
            # TODO: оптимизировать
            # ------------------------------------------------------------
            # Это часть функции пожирает 35% времени, что совсем не здорово.
            # После оптимизации find_visible_soldiers вызовов стало гораздо меньше.
            # ------------------------------------------------------------
            elif coordinates != soldier_point and coordinates != enemy_point:
                #print(coordinates, soldier_point, enemy_point)
                if tuple in [type(el) for el in dict_battlespace[coordinates]]:
                    cover_sum += 4
            # Прерываем обход линии взгляда, если видимость нулевая:
            if cover_sum >= max_obstacle:
                cover_sum = max_obstacle
                visibility = False
                # Высоты помогают видеть все ряды врага:
                # 60-футовый холм на дистанции 150-200 футов даёт угол в 17-22 градуса:
                if 'height' in dict_battlespace[soldier_point]\
                        or 'height' in dict_battlespace[enemy_point]:
                    cover_sum = max_obstacle -3
                    visibility = True
                    # Враг может укрыться под крепостной стеной или отвесным склоном:
                    # Это 25-футовая мёртва зона для 25-футовой стены:
                    if 'wall' in dict_battlespace[soldier_point] and distance < 5\
                            or 'wall' in dict_battlespace[enemy_point] and distance < 5:
                        cover_sum = max_obstacle
                        visibility = False
                # Всадник в рядах пехоты заметен. Но прикрытие на 3/4 есть:
                if 'mount_height' in dict_battlespace[soldier_point]\
                        or 'mount_height' in dict_battlespace[enemy_point] and distance < 5:
                    cover_sum = max_obstacle -3
                    visibility = True
                break
        vision_tuple = self.namedtuple_visibility(distance, cover_sum, visibility)
        return vision_tuple

    def find_soldiers_all(self, side = None, scout_place = None):
        """Находит солдат на карте.
        
        Опции:
        - Находит солдат определённой стороны.
        - Измеряет дистанцию от цели до наблюдателя.
        Возвращает словарь, где ключи -- uuid солдат.
        """
        dict_soldiers = {}
        for place, descript in self.dict_battlespace.items():
            for el in descript:
                if type(el) == tuple:
                    soldier_tuple = el
                    soldier_side, soldier_type, soldier_uuid = soldier_tuple
                    soldier_place = place
                    distance = 0
                    if scout_place:
                        distance = round(distance_measure(scout_place, soldier_place))
                    target = self.namedtuple_target(
                            soldier_side, soldier_type, soldier_place,
                            distance, cover = 0, uuid = soldier_uuid)
                    if side == None:
                        dict_soldiers[soldier_uuid] = target
                    elif soldier_side == side:
                        dict_soldiers[soldier_uuid] = target
        # Сортировка целей по дистанции:
        if scout_place:
            dict_soldiers = OrderedDict(sorted(dict_soldiers.items(),key=lambda x: x[1].distance))
        return dict_soldiers

    def refind_soldiers_distance(self, scout_place, dict_soldiers):
        """Сортируем словарь целей по дистанции."""
        for soldier in dict_soldiers.values():
            distance = round(distance_measure(scout_place, soldier.place))
            target = self.namedtuple_target(
                    soldier.side, soldier.type, soldier.place,
                    distance, cover = 0, uuid = soldier.uuid)
            dict_soldiers[soldier.uuid] = target
        dict_soldiers = OrderedDict(sorted(dict_soldiers.items(),key=lambda x: x[1].distance))
        return dict_soldiers

    def find_soldiers_place(self, side = None):
        """Находит координаты врагов/своих.
        
        Возвращает словарь, где ключи -- координаты солдат.
        Если два бойца на одной точке, видит только одного (последнего).
        Это удобно для вывода данных на карту, но плохо для оценки сил.
        """
        dict_soldiers = {}
        for key, value in self.dict_battlespace.items():
            for el in value:
                if type(el) == tuple:
                    soldier_tuple = el
                    if side == None:
                        dict_soldiers[key] = soldier_tuple
                    elif soldier_tuple[0] == side:
                        dict_soldiers[key] = soldier_tuple
        return dict_soldiers

    def find_visible_soldiers(self, soldier_coordinates,
            side = None, dict_recon = None, max_number = 10, max_try = 30):
        """Находит видимых бойцу врагов/своих.

        Как это работает:
        - Создаётся словарь всех целей на карте.
        - Измеряется дистанция до всех целей на карте.
        - Рисуется линия взгляда от бойца к каждой цели.
        Если линия не перекрыта препятствиями, то враг видимый.

        По умолчанию выводит 10 ближайших видимых целей. Максимум попыток поиска -- 30
        Выводит сортированный (по дистанции) словарь, где ключи -- координаты целей.
        Значения: сторона, тип_юнита, кординаты, дистанция, прикрытие (от взгляда), uuid.
        """
        # TODO: оптимизация поиска.
        # ------------------------------------------------------------
        # Функция кое-как оптимизирована, но всё же.
        # Сейчас самое медленное, это find_soldiers_all().
        # Было бы неплохо брать координаты из metadict_soldiers
        # Проблема лишь в том, что это не относится к классу battlescape
        # ------------------------------------------------------------
        # Находим всех врагов на поле боя (70% работы функции):
        # Измерение дистанции до всех целей (30% работы функции)
        #start = timeit.default_timer()
        if not dict_recon:
            dict_recon_raw = self.find_soldiers_all(side, soldier_coordinates)
        else:
            dict_recon_raw = dict_recon
        #stop = timeit.default_timer()
        #print('Function time:', stop - start)
        # TODO: Проблема селекции целей.
        # ------------------------------------------------------------
        # Возможна ситуация, что если боец не видит 10 ближайших врагов,
        # Тогда он не заметит и обстреливающего его с возвышенности лучника.
        # ------------------------------------------------------------
        # Селекция целей по видимости (берём первые 10 видимых целей):
        dict_recon_visible = {}
        found_number = 0
        for n,value in enumerate(dict_recon_raw.values(), 1):
            vision_tuple = self.calculate_enemy_cover(soldier_coordinates, value.place)
            if vision_tuple[-1] == True:
                uuid = value.uuid
                distance = vision_tuple[0]
                cover = vision_tuple[1]
                target = self.namedtuple_target(value.side,value.type,value.place,distance,cover,value.uuid)
                dict_recon_visible[uuid] = target
                found_number += 1
                if found_number >= max_number:
                    break
            # Ограничиваем число попыток (по умолчанию 30)
            if n >= max_try:
                break
        return dict_recon_visible

    def find_path_slow(self, soldier_coordinates, point_coordinate, matrix = None):
        """Находит путь к месту назначения.

        Алгоритм поиска A-star:
        https://github.com/brean/python-pathfinding
        https://ru.wikipedia.org/wiki/Алгоритм_поиска_A*
        """
        if matrix == None:
            matrix = self.matrix
        grid = Grid(matrix = matrix)
        start = grid.node(soldier_coordinates[0],soldier_coordinates[1])
        end = grid.node(point_coordinate[0],point_coordinate[1])
        path, runs = self.finder.find_path(start, end, grid)
        # Удаляем первую точку, там наш солдат:
        if len(path) > 1:
            soldier_point = path.pop(0)
        #print('operations:', runs, 'path length:', len(path))
        #print(grid.grid_str(path=path, start=start, end=end))
        return path

    def find_path_fast(self, soldier_coordinates, point_coordinates):
        """Проверяет, есть ли прямой путь к месту назначения.

        Незачем усложнять, если можно добраться по линии взгляда.
        Между прочим bresenham в 300 раз быстрее, чем AStarFinder.
        """
        sight_line = sight_line_to_list(soldier_coordinates, point_coordinates)
        # Удаляем первую точку, там наш солдат:
        if len(sight_line) > 1:
            soldier_point = sight_line.pop(0)
            for place in sight_line:
                if 'stop_terrain' in self.dict_battlespace[place]:
                    sight_line = None
                    return sight_line
            return sight_line

    def check_place(self, soldier, place):
        """Проверка, не занята ли точка на пути бойца."""
        # TODO: Допили проверку пересечённой местности. Или выведи в move_action.
        unit_tuples = []
        for value in self.dict_battlespace[place]:
            if soldier.__dict__.get('water_walk') and value == 'water':
                free_place = True
                rough_place = False
                break
            elif value == 'stop_terrain':
                free_place = False
                rough_place = True
                break
            elif type(value) == tuple:
                unit_tuples.append(value)
            else:
                free_place = True
                rough_place = False
        if unit_tuples:
            free_place = False
            rough_place = True
        place_tuple = self.namedtuple_place(place, free_place, rough_place, unit_tuples)
        return place_tuple

    #def check_path(self, coordinates):
    #    """Быстрая проверка, не занята ли точка на пути бойца.

    #    Например, другим солдатом, или врагом. Или ямой, стеной.
    #    """
    #    # TODO: перепиливай проверку. Должна возвращать сторону бойца.
    #    # Сделай вывод кортежем.
    #    dict_battlespace = self.dict_battlespace
    #    # Если в списке есть кортеж, значит точка занята другим бойцом:
    #    if tuple in [type(el) for el in self.dict_battlespace[coordinates]]:
    #        return False
    #    elif 'stop_terrain' in self.dict_battlespace[coordinates]:
    #        return False
    #    else:
    #        return True

    def recon(self, zone_center, distance = 1, soldier_coordinates = None, view_all = False):
        """Осмотр квадрата на поле боя. Вывод словаря союзников и врагов.
        
        Как это работает:
        - Боец осматривается из центра зоны (если soldier_coordinates = None)
        - Лучник осматривает зону со стороны (если soldier_coordinates указаны)
        В выводе сортированный по дистанции словарь друзей и врагов.
        """
        dict_battlespace = self.dict_battlespace
        # Зона может быть задана списком координат:
        if len(zone_center) > 2:
            coord_list = zone_center
            zone_center = coord_list[0]
            distance = round(distance_measure(zone_center, coord_list[-1]))
        # Или координатами центра зоны:
        elif type(zone_center) == tuple and len(zone_center) == 2:
            x,y = zone_center[0], zone_center[1]
            # Задаём диапазон координат:
            coord_list = []
            for x1 in range(x - distance, x + distance + 1):
                for y1 in range(y - distance, y + distance + 1):
                    if x1 >= 0 and y1 >= 0\
                            and x1 <= self.battle_map_length\
                            and y1 <= self.battle_map_height:
                        coord_list.append((x1,y1))
        # Проверяя диапазон, находим врагов и своих:
        dict_recon = {}
        for place in coord_list:
            if dict_battlespace.get(place):
                for value in dict_battlespace.get(place):
                    if type(value) == tuple:
                        if soldier_coordinates == False:
                            # Взгляд мастера (дистанция нулевая, помех нет, видны все):
                            vision_tuple = self.namedtuple_visibility(
                                    distance = 0, cover = 0, visibility = True)
                        elif soldier_coordinates != None:
                            # Взгляд на зону со стороны координат (если боец лучник/маг):
                            vision_tuple = self.calculate_enemy_cover(soldier_coordinates, place)
                        else:
                            # Взгляд из центра зоны (если боец в центре):
                            vision_tuple = self.calculate_enemy_cover(zone_center, place)
                        if vision_tuple[-1] == True or view_all:
                            distance = vision_tuple[0]
                            cover = vision_tuple[1]
                            uuid = value[-1]
                            #Сторона, тип_юнита, кординаты, дистанция, прикрытие (от взгляда), uuid.
                            target = self.namedtuple_target(value[0],value[1],place,distance,cover,uuid)
                            dict_recon[uuid] = target
        # Сортировка целей по дистанции:
        dict_recon = OrderedDict(sorted(dict_recon.items(),key=lambda x: x[1].distance))
        return dict_recon

    def danger_sense(self, dict_recon, enemy_side):
        """Оценка угрозы от врагов и поддержки от своих. Страхочуйка.

        Как это работает:
        - У каждого юнита есть свой рейтинг опасности.
        - Элита стоит 2-х простоых бойцов, а командир 3-х бойцов.
        - Из суммарной силы союзников в зоне вычитается сила врагов.
        - Если вывод больше нуля, значит враг в данной зоне сильнее.

        Кто это использует:
        - Простые бойцы (recon на 9 клеток, включая себя)
        - Лучники и маги (чтобы поражать скопления врага)
        - Командиры (оценивая общее соотношение сил на поле боя)
        """
        # ЗАМЕТКА: danger_sense
        # ------------------------------------------------------------
        # Оценка опасности в радиусе 10 футов (5x5 клеток с центром на бойце).
        # Если в этой зоне враги сильнее союзников, боец переходит в оборону.
        # 150-250 срабатываний danger_sense за бой, это весомо. Это спасает жизни.
        # ------------------------------------------------------------
        # Если враг, то добавляем угрозы, если друг, то убавляем:
        dangermeter = 0
        for value in dict_recon.values():
            if value[0] in enemy_side:
                dangermeter += self.dict_danger.get(value[1],0)
            else:
                dangermeter -= self.dict_danger.get(value[1],0)
        return dangermeter

    def point_to_field(self, point, length = 1):
        """Точка в область."""
        coord_list = []
        x, y = point[0], point[1]
        for x1 in range(x - length, x + length + 1):
            for y1 in range(y - length, y + length + 1):
                if x1 >= 0 and y1 >= 0\
                        and x1 < self.battle_map_length\
                        and y1 < self.battle_map_height:
                    coord_list.append((x1,y1))
        return coord_list

    def point_to_field_2x2(self, point):
        """Точка в область."""
        coord_list = []
        x, y = point[0], point[1]
        for x1 in range(x, x + 2):
            for y1 in range(y, y + 2):
                if x1 >= 0 and y1 >= 0\
                        and x1 < self.battle_map_length\
                        and y1 < self.battle_map_height:
                    coord_list.append((x1,y1))
        return coord_list

    def point_to_field_ray(self, source_point, target_point, ray_distance, except_firs_poiint = False):
        """Продолжаем луч до конечной точки.
        
        - Все точки на пути луча возвращаются как зона заклинания.
        """
        end_point = prolong_ray(source_point, target_point, ray_distance)
        ray_field = sight_line_to_list(source_point, end_point)
        # Удаляем первую точку, на которой стоит кастер.
        if except_firs_poiint:
            first_point = ray_field.pop(0)
        return ray_field

    def point_to_field_cone(self, source_point, target_point, ray_distance, except_firs_poiint = False):
        """Атака конусом.
        
        1. Чертим вектор до конца дальности.
        2. Разворачиваем два перпендикулярных вектора из конечной точки, получая координаты их концов.
        3. Получаем координаты концов треугольника.
        4. Строим прямоугольник и находим точки треугольника в нём.
        """
        # TODO: добавь проверку, чтобы source_point и target_point не совпадали.
        # Иногда это случается, когда маг нацеливает конус на врага в своей точке.
        target_point = prolong_ray(source_point, target_point, ray_distance)
        cone_coordinates = find_cone_coordinates(source_point, target_point, ray_distance)
        #print(source_point, target_point, cone_coordinates)
        # Строим прямоугольник, включающий в себя искомый треугольник:
        square_coords = []
        coord_list_x = [cone_coordinates[0][0], cone_coordinates[1][0], cone_coordinates[2][0]]
        coord_list_y = [cone_coordinates[0][1], cone_coordinates[1][1], cone_coordinates[2][1]]
        x_min = min(coord_list_x)
        x_max = max(coord_list_x)
        y_min = min(coord_list_y)
        y_max = max(coord_list_y)
        for y in range(y_min, y_max):
            for x in range(x_min, x_max):
                point = x,y
                square_coords.append(point)
        # Очерчиваем границы треугольника:
        triangle_borders = []
        a = sight_line_to_list(cone_coordinates[0], cone_coordinates[1])
        b = sight_line_to_list(cone_coordinates[0], cone_coordinates[2])
        c = sight_line_to_list(cone_coordinates[1], cone_coordinates[2])
        triangle_borders.extend(a)
        triangle_borders.extend(b)
        triangle_borders.extend(c)
        # Находим координаты всех точек треугольника:
        triangle_coords = []
        for point in square_coords:
            if inside_triangle(cone_coordinates[0], cone_coordinates[1], cone_coordinates[2], point):
                triangle_coords.append(point)
            elif point in triangle_borders:
                triangle_coords.append(point)
        # Удаляем точку, на которой стоит кастер:
        if except_firs_poiint and source_point in triangle_coords:
            source_point = triangle_coords.remove(source_point)
        #print(len(triangle_coords))
        return triangle_coords

    def find_points_in_zone(self, first_point, distance = 100):
        """Поиск всех точек внутри ограниченной зоны.
        
        Рекурсивный обход в ширину:
        Каждая точка поля боя связана с 8 другими точками.
        Мы обходим все точки, которые не stop_terrain и не zone_border.
        Так получаем все точки внутри ограниченной стенами/границами зоны.
        """
        ready_field = []
        checked_points = []
        points_max = len(self.point_to_field(first_point, length = distance))
        field = self.point_to_field(first_point)
        while len(field) > 0 and len(checked_points) < points_max:
            for point in field:
                checked_points.append(point)
                if not point in ready_field\
                        and 'stop_terrain' not in self.dict_battlespace[point]\
                        and 'zone_border' not in self.dict_battlespace[point]:
                    ready_field.append(point)
                    field.extend(self.point_to_field(point))
                    # Чистим зону поиска от дублей:
                    field = list(set(field))
            # Чистим зону поиска от уже проверенных точек:
            checked_points = list(set(checked_points))
            field = list(set(field) - set(checked_points))
            #print(field)
        #print(len(checked_points))
        #print(len(ready_field))
        return ready_field    

    def fireball_points(self, length = 10):
        """Точки оптимального поражания огнешарами.

        Это центры зон 50x50 футов (по умолчанию)
        Маг берёт этот список, затем делает несколько селекций:
        1) По дальности от своей позиции (150 футов -- огнешар)
        2) По видимости со своей позиции (он должен видеть точку поражения)
        3) По числу врагов в зоне и числу своих (через recon и danger_sense)
        И только затем божественный фаерболл отправляется к цели.
        """
        map_lenght = self.battle_map_length
        map_height = self.battle_map_height
        # Находим центры интересующих нас квадартов:
        fireball_points = []
        for x in range(0, map_lenght, round(length / 2)):
            for y in range(0, map_height, round(length / 2)):
                fireball_points.append((x,y))
                #if x != 0 and y != 0:
                #    fireball_points.append((x,y))
        return fireball_points

    def find_danger_zones(self, enemy_side, zone_length = 10, soldier_coordinates = False):
        """Создаёт словарь опасных/безопасных участков карты.
        
        В том числе с точки зрений определённого бойца.
        """
        # Нам нужна половина от длины зоны (поиск из центра):
        recon_radius = round(zone_length / 2)
        dict_danger_zones = {}
        for point in self.fireball_points(zone_length):
            danger = self.danger_sense(
                    self.recon(point, recon_radius, soldier_coordinates), enemy_side)
            if danger > 0:
                dict_danger_zones[point] = danger
        dict_danger_zones = OrderedDict(reversed(sorted(
            dict_danger_zones.items(),key=lambda x: x[1])))
        return dict_danger_zones

    def gen_battlemap(self):
        """Генерация текущей карты боя в формате ASCII.
        
        """
        dict_battlemap = {}
        dict_battlespace = self.dict_battlespace
        # Создаём словарь меток (координаты:символы):
        for key,descript in dict_battlespace.items():
            for symbol,desript_base in self.battlespace_objects.items():
                if descript and descript[0] == desript_base[0]:
                    dict_battlemap[key] = symbol
                    #print(key,symbol,descript)
                    break
                # Если символ неизвестен -- ставим пробел.
                elif not descript:
                    dict_battlemap[key] = ' '
                    break
        #print(dict_battlemap)
        # Дополняем словарь метками бойцов:
        soldiers_dict = self.find_soldiers_place()
        for key,descript in soldiers_dict.items():
            # ЗАМЕТКА: Костыли-костылики
            # ------------------------------------------------------------
            # Здесь мы берём последнюю подходящую метку из словаря battlespace_objects
            # В том случае, если боец под защитой закрытой местности (barrikade)
            # И первую метку, если боец не под защитой (где прерываем цикл через break)
            # ------------------------------------------------------------
            if 'cover_terrain' in self.dict_battlespace[key]:
                for symbol,desript_base in self.battlespace_objects.items():
                    if descript[1] == desript_base[-1]:
                        dict_battlemap[key] = symbol
            else:
                for symbol,desript_base in self.battlespace_objects.items():
                    if descript[1] == desript_base[-1]:
                        dict_battlemap[key] = symbol
                        break
        # Рисуем карту по словарю:
        battlemap_list = []
        battlemap_string = ''
        for key, symbol in dict_battlemap.items():
            if key[0] < self.battle_map_length - 1:
                # Цветные метки бойцов с помощью ANSI:
                symbol_colored = self.color_symbols(key, symbol)
                battlemap_string = battlemap_string + symbol_colored
            else:
                symbol_colored = self.color_symbols(key, symbol)
                battlemap_string = battlemap_string + symbol_colored
                battlemap_list.append(battlemap_string)
                battlemap_string = ''
        # Отображаем карту:
        #print_ascii_map(battlemap_list)
        return battlemap_list

    def color_symbols(self, key, symbol):
        """Цветные символы на карте.
        
        Формат:
        - Миганием делающего ход бойца.
        - Серым фоном защищённые позиции.
        - Подчёркивание -- возвышенности.
        - Особенно ярко -- командиры.
        - Курсивом выделяем раненых.
        - Белым цветом отступающих.

        ANSI sequences
        https://en.wikipedia.org/wiki/ANSI_escape_code#8-bit
        """
        symbol_colored = symbol
        dict_battlespace = self.dict_battlespace
        # Находим бойцов на поле боя (а заодно считаем их на точке):
        soldiers_in_place = 0
        for el in self.dict_battlespace[key]:
            if type(el) == tuple:
                soldiers_in_place += 1
                if el[0] == self.ally_side:
                    symbol_colored = '\x1b[32m' + symbol_colored
                elif el[0] == self.enemy_side:
                    symbol_colored = '\x1b[31m' + symbol_colored
                if el[1] == 'commander':
                    symbol_colored = '\x1b[1m' + symbol_colored
                if 'cover_terrain' in self.dict_battlespace[key]:
                    symbol_colored = '\x1b[48;5;8m' + symbol_colored
                if 'height' in self.dict_battlespace[key]:
                    symbol_colored = '\x1b[48;5;8m' + symbol_colored
                if 'mount_height' in self.dict_battlespace[key]:
                    symbol_colored = '\x1b[48;5;8m' + symbol_colored
                if 'obscure_terrain' in self.dict_battlespace[key]:
                    symbol_colored = '\x1b[48;5;18m' + symbol_colored
                if 'crusaders_mantle' in self.dict_battlespace[key]:
                    symbol_colored = '\x1b[48;5;23m' + symbol_colored
                if 'spirit_guardians' in self.dict_battlespace[key]:
                    symbol_colored = '\x1b[48;5;23m' + symbol_colored
                    #if self.ally_side in el:
                    #    symbol_colored = '\x1b[48;5;22m' + symbol_colored
                    #elif self.enemy_side in el:
                    #    symbol_colored = '\x1b[48;5;52m' + symbol_colored
                if soldiers_in_place > 1:
                    symbol_colored = '\x1b[4m' + symbol_colored
                # TODO: сделай курсив для раненых и белый для отступающих.
                # ------------------------------------------------------------
                # И, если будет угодно, мигание для делающего ход бойца.
                # Или смену его символа на собачку "@".
                # Проблема в том, что у этой функции нет данных по бойцам.
                # ------------------------------------------------------------
            if 'fall_place' in self.dict_battlespace[key]:
                # Если убили своего, выделяем клетку зелёным, а врага красным:
                if self.ally_side in self.dict_battlespace[key]:
                    symbol_colored = '\x1b[48;5;10m' + symbol_colored
                elif self.enemy_side in self.dict_battlespace[key]:
                    symbol_colored = '\x1b[48;5;9m' + symbol_colored
            if 'volley' in self.dict_battlespace[key]\
                    or 'bonfire' in self.dict_battlespace[key]\
                    or 'dawn' in self.dict_battlespace[key]:
                #symbol_colored = '\x1b[48;5;23m' + symbol_colored
                if type(el) == tuple:
                    if el[0] == self.ally_side:
                        symbol_colored = '\x1b[48;5;22m' + symbol_colored
                    elif el[0] == self.enemy_side:
                        symbol_colored = '\x1b[48;5;52m' + symbol_colored
        # Сброс параметров после обработки символа:
        symbol_colored = symbol_colored + '\x1b[0m'
        return symbol_colored
