#!/usr/bin/env python
# -*- coding: utf-8 -*-

from config_utils import *
from data.LangDatasets import lang_sindar
from data.LangDatasets import lang_human
from data.LangDatasets import lang_english

# Имена солдат для squad_generation.py:
# english, french, german, spanish, italian, chinese
NAMES_LANGUAGE = 'english'
NAMES_DICT = get_json_dict(NAMES_LANGUAGE, '/data/LangDatasets/names')
SURNAMES_DICT = get_json_dict(NAMES_LANGUAGE, '/data/LangDatasets/surnames')
LANGUAGE_DICT_REAL = lang_english.dict_words
# Словарь для генерации имён на синдарине:
# (Раскомментируй, если нужны фентезийные имена)
#LANGUAGE_DICT_FANTASY = {}
#LANGUAGE_DICT_FANTASY.update(lang_sindar.dict_words)
#LANGUAGE_DICT_FANTASY.update(lang_human.dict_words)
