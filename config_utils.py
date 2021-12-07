#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json

#-------------------------------------------------------------------------
# Функции:

def get_json_dict (search_string, search_dir = None):
    """Поиск json по имени файла.
    
    Обход каталогов рекурсивный, поэтому каталог указывать не обязательно.
    """
    # Абсолютный путь к каталогу программы.
    json_dict = {}
    path = os.path.dirname(os.path.abspath(__file__))
    if search_dir and search_dir != path:
        path = path + search_dir
    # Рекурсивный обход каталогов и поиск файла.
    file_path_list = [f for f in find_files(path) if search_string in f and '.json' in f]
    for file_path in file_path_list:
        with open(file_path) as json_file:
            json_dict.update(json.load(json_file))
    return json_dict

def find_files (directory):
    """Возвращает список путей ко всем файлам каталога, включая подкаталоги."""
    path_f = []
    for d, dirs, files in os.walk(directory):
        for f in files:
                # Формирование адреса:
                path = os.path.join(d,f)
                # Добавление адреса в список:
                path_f.append(path)
    return path_f
