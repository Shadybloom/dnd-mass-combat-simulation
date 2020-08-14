#!/usr/bin/env python
# -*- coding: utf-8 -*-

import inspect
import random
import copy

class gen_spells():
    """Заклинания представлены как функции.
    
    Параметры меняются в зависимости от способностей мага.
    """

    def __init__(self, soldier):
        # TODO: Так мы передадим заклинаниям параметры мага.
        # ------------------------------------------------------------
        # Создаётся при генерации, в soldier_base.
        # Можно просто передать словарь soldier.__dict__ в self.__dict__.
        # ------------------------------------------------------------
        self.mage = soldier
        # Это лишнее, мы можем просто вызвать self.mage.level:
        #self.mage_level = soldier.level
        #self.mage_class = soldier.char_class
        #self.mods = soldier.mods
        #self.proficiency_bonus = soldier.proficiency_bonus
        self.know_spells = soldier.class_features.get('Spells',[])
        # Нужен список методов класса, можно с примесью опций:
        #self.usable_spells = inspect.getmembers(self, predicate=inspect.ismethod)
        self.usable_spells = ([ method for method in dir(self) if not method.startswith('__')])
        self.spellslots = {}
        # Слоты заклинаний:
        for spell_slot, number in soldier.proficiency.get('spellslots').items():
            if number > 0:
                self.spellslots[spell_slot] = number
        # Feat_Magic_Initiate: добавляет заклинание 1 круга и слот для него:
        if soldier.class_features.get('Feat_Magic_Initiate'):
            if self.spellslots.get('1_lvl'):
                self.spellslots['1_lvl'] +=1
            else:
                self.spellslots['1_lvl'] = 1
        # TODO: В отдельную функцию.
        # ------------------------------------------------------------
        # Нам нужен выбор случайных заклинаний, если в know_spells стоит random.
        # ------------------------------------------------------------
        # Динамическая генерация заклинаний:
        self.spells = {}
        for spell in self.know_spells:
            spell_name = spell[-1]
            spell_level = spell[0]
            if spell_name in self.usable_spells:
                func = getattr(self, spell_name)
                spell_dict = func(spell_level)
                spell_dict['spell_choice'] = spell
                self.spells[spell] = spell_dict
        #print(self.spells)

    def find_spell_attack_mod(self):
        """Модификатор атаки заклинания зависит от класса.
        
        У волшебников это интеллект, у чародеев харизма, у жрецов мудрость.
        """
        # TODO: перенеси это в список, в classes.py
        if self.mage.char_class == 'Wizard'\
                or self.mage.char_class == 'Arcane_Tricker'\
                or self.mage.char_class == 'Eldritch_Knight'\
                or self.mage.char_class == 'Rogue':
            attack_mod = self.mage.mods['intelligence'] + self.mage.proficiency_bonus
        elif self.mage.char_class == 'Sorcerer'\
                or self.mage.char_class == 'Bard'\
                or self.mage.char_class == 'Warlock'\
                or self.mage.char_class == 'Barbarian'\
                or self.mage.char_class == 'Paladin':
            attack_mod = self.mage.mods['charisma'] + self.mage.proficiency_bonus
        elif self.mage.char_class == 'Cleric'\
                or self.mage.char_class == 'Cleric-heavy'\
                or self.mage.char_class == 'Druid'\
                or self.mage.char_class == 'Ranger'\
                or self.mage.char_class == 'Monk':
            attack_mod = self.mage.mods['wisdom'] + self.mage.proficiency_bonus
        elif self.mage.char_class == 'Empyrean':
            attack_mod = self.mage.mods['charisma'] + self.mage.proficiency_bonus
        else:
            # Если класса нет в списке, выбираем маскимальную характеристику:
            mods = self.mage.mods
            mods_list = [mods['intelligence'], mods['wisdom'], mods['charisma']]
            attack_mod = max(mods_list) + self.mage.proficiency_bonus
        # Монстры:
        return attack_mod

    def find_spell(self, spell_name, effect = False):
        """Поиск заклинания из доступных.
        
        Возможен по эффекту заклинания. Тогда spell_name это effect.
        Случайный выбор, если несколько одинаковых заклинаний на разных уровнях.
        """
        if effect:
            spell_list = [spell for spell in self.spells
                    if self.spells[spell].get('effect') == spell_name]
        else:
            spell_list = [spell for spell in self.spells if spell[-1] == spell_name]
        if spell_list:
            spell_choice = random.choice(spell_list)
            return spell_choice

    def use_spell(self, spell_choice, gen_spell = False, use_spell_slot = True):
        """Расходуется ячейка заклинания, очищается словарь self.spells."""
        spell_slot_use = spell_choice[0]
        # Заклинания 0 уровня бесконечные:
        if spell_slot_use == 'cantrip':
            return self.spells[spell_choice]
        # Вызываем заклинание без ячейки, заклинание любое из доступных:
        if not use_spell_slot:
            spell_level = '1_lvl'
            spell_name = spell_choice[-1]
            func = getattr(self, spell_name)
            spell_dict = func(spell_level, gen_spell)
            spell_dict['spell_choice'] = spell_choice
            return spell_dict
        # Используем ячейку заклинания:
        for spell_slot in self.spellslots:
            if spell_slot == spell_slot_use:
                if self.spellslots[spell_slot] > 0 and gen_spell:
                    self.spellslots[spell_slot] -= 1
                    spell_level = spell_slot[0]
                    spell_name = spell_choice[-1]
                    func = getattr(self, spell_name)
                    spell_dict = func(spell_level, gen_spell = True)
                    spell_dict['spell_choice'] = spell_choice
                elif self.spellslots[spell_slot] > 0:
                    self.spellslots[spell_slot] -= 1
                    spell_dict = copy.deepcopy(self.spells[spell_choice])
                if self.spellslots[spell_slot] <= 0:
                    # Убираем закончившиеся ячейки:
                    # Убираем заклинания этого уровня, если ячейки закончились:
                    self.spellslots.pop(spell_slot)
                    spells_to_remove = [spell for spell in self.spells if spell[0] == spell_slot_use]
                    for spell in spells_to_remove:
                        self.spells.pop(spell)
                return spell_dict

#----
# Channel_Divinity

    def Radiance_of_the_Dawn(self, spell_level, gen_spell = False):
        """Сияние рассвета.
        
        """
        # Абсолютно убийственная способность. Сотни обожённых, сотни смертей.
        # Можно защититься баррикадами, которые и без того нередко используются в бою.
        # Как вариант, пусть работает только против волшебных созданий: нежити, демонов, духов и фей.
        # Пока что урон ослаблен 2d10 > 1d10. Зато на 5 lvl урон повышается.
        spell_dict = {
                'effect':'channel',
                'direct_hit':True,
                'savethrow':True,
                'savethrow_ability':'constitution',
                'attacks_number':1,
                'radius':30,
                'attack_range':5,
                'damage_type':'radiant',
                'damage_dice':'1d10',
                'components':['somatic'],
                'casting_time':'action',
                'damage_mod':0,
                'spell_level':spell_level,
                'spell_save_DC':8 + self.find_spell_attack_mod(),
                'spell_of_choice':'Sacred_Flame',
                }
        if self.mage.level >= 5:
            spell_dict['damage_dice'] = '2d10'
        if self.mage.level >= 11:
            spell_dict['damage_dice'] = '3d10'
        if self.mage.level >= 17:
            spell_dict['damage_dice'] = '4d10'
        return spell_dict

    def Divine_Smite(self, spell_level, gen_spell = False):
        """Божественная кара.
        
        """
        # TODO: эта атака усиливается критическим ударом.
        # Кроме того наносит дополнительные 1d8 урона нежити и исчадиям.
        spell_dict = {
                'effect':'smite',
                'direct_hit':True,
                'attacks_number':1,
                'attack_range':5,
                'damage_type':'radiant',
                'damage_dice':'2d8',
                'components':[],
                'casting_time':None,
                'damage_mod':0,
                'spell_level':spell_level,
                'spell_save_DC':8 + self.find_spell_attack_mod(),
                'spell_of_choice':'Sacred_Flame',
                }
        if int(spell_level[0]) > 1:
            dice = int(spell_dict['damage_dice'][0])
            dice += int(spell_level[0]) - 1
            spell_dict['damage_dice'] = str(dice) + spell_dict['damage_dice'][1:]
        return spell_dict

    def Sacred_Weapon(self, spell_level, gen_spell = False):
        """Священное оружие.
        
        Oath_of_Devotion
        """
        spell_dict = {
                'effect':'sacred_weapon',
                'effect_timer':10,
                'subspell':('subspell', 'light'),
                'components':[],
                'casting_time':None,
                'attack_mod':self.mage.mods['charisma'],
                'damage_mod':0,
                'spell_level':spell_level,
                'spell_save_DC':8 + self.find_spell_attack_mod(),
                'spell_of_choice':'Sacred_Flame',
                }
        return spell_dict

    def Dreadful_Aspect(self, spell_level, gen_spell = False):
        """Пугающее присутствие антипаладина.

        Channel_Dreadful_Aspect
        """
        spell_dict = {
                'effect':'fear',
                'attacks_number':1,
                'zone':True,
                'radius':30,
                'attack_range':5,
                'direct_hit':True,
                'savethrow':True,
                'savethrow_all':True,
                'savethrow_ability':'wisdom',
                'components':['verbal'],
                'casting_time':'action',
                'spell_level':spell_level,
                'spell_save_DC':8 + self.find_spell_attack_mod(),
                'spell_of_choice':'Dreadful_Aspect',
                }
        return spell_dict

    def Wrath_of_the_Storm(self, spell_level, gen_spell = False):
        """Контратака жреца

        """
        spell_dict = {
                'direct_hit':True,
                'savethrow':True,
                'savethrow_ability':'dexterity',
                'attacks_number':1,
                'attack_range':5,
                'damage_type':'lightning',
                'damage_dice':'2d8',
                'components':['verbal'],
                'casting_time':'action',
                'damage_mod':0,
                'spell_level':spell_level,
                'spell_save_DC':8 + self.find_spell_attack_mod(),
                'spell_of_choice':'Wrath_of_the_Storm',
                }
        return spell_dict

#----
# Cantrips

    def Eldritch_Blast(self, spell_level, gen_spell = False):
        """Мистический заряд.

        Level: Cantrip
        Casting time: 1 Action
        Range: 120 feet
        Components: V, S
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/eldritch-blast
        """
        spell_dict = {
                'attacks_number':1,
                'attack_range':120,
                'damage_type':'force',
                'damage_dice':'1d10',
                'components':['verbal','somatic'],
                'casting_time':'action',
                'spell_level':spell_level,
                'damage_mod':0,
                'attack_mod':self.find_spell_attack_mod(),
                'spell_save_DC':8 + self.find_spell_attack_mod(),
                # TODO: сделай выбор оптимального заклинания:
                'spell_of_choice':'Eldritch_Blast',
                }
        if self.mage.class_features.get('Invocation_Agonizing_Blast'):
            spell_dict['damage_mod'] = self.mage.mods['charisma']
        if self.mage.class_features.get('Invocation_Eldritch_Spear'):
            spell_dict['attack_range'] += 120
        if self.mage.level >= 5:
            spell_dict['attacks_number'] = 2
        if self.mage.level >= 11:
            spell_dict['attacks_number'] = 3
        if self.mage.level >= 17:
            spell_dict['attacks_number'] = 4
        return spell_dict

    def Fire_Bolt(self, spell_level, gen_spell = False):
        """Огненный снаряд.

        Level: Cantrip
        Casting time: 1 Action
        Range: 120 feet
        Components: V, S
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/fire-bolt
        """
        spell_dict = {
                'attacks_number':1,
                'attack_range':120,
                'damage_type':'fire',
                'damage_dice':'1d10',
                'components':['verbal','somatic'],
                'casting_time':'action',
                'spell_level':spell_level,
                'damage_mod':0,
                'attack_mod':self.find_spell_attack_mod(),
                'spell_save_DC':8 + self.find_spell_attack_mod(),
                'spell_of_choice':'Fire_Bolt',
                }
        if self.mage.level >= 5:
            spell_dict['damage_dice'] = '2d10'
        if self.mage.level >= 11:
            spell_dict['damage_dice'] = '3d10'
        if self.mage.level >= 17:
            spell_dict['damage_dice'] = '4d10'
        return spell_dict

    def Acid_Splash(self, spell_level, gen_spell = False):
        """Брызги кислоты.
        
        Поражает две цели, если не сумеют уклониться.

        Level: Cantrip
        Casting time: 1 Action
        Range: 60 feet
        Components: V, S
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/acid-splash
        """
        # TODO: две разные цели, обе должны быть рядом. Сделай через эффект.
        # Да не, фигня получается, лишнее переусложнение. Пусть будет пока так.
        spell_dict = {
                'direct_hit':True,
                'savethrow':True,
                'savethrow_all':True,
                'savethrow_ability':'dexterity',
                'attacks_number':2,
                'attack_range':60,
                'damage_type':'acid',
                'damage_dice':'1d6',
                'components':['verbal','somatic'],
                'casting_time':'action',
                'spell_level':spell_level,
                'damage_mod':0,
                'attack_mod':self.find_spell_attack_mod(),
                'spell_save_DC':8 + self.find_spell_attack_mod(),
                'spell_of_choice':'Acid_Splash',
                }
        if self.mage.level >= 5:
            spell_dict['damage_dice'] = '2d6'
        if self.mage.level >= 11:
            spell_dict['damage_dice'] = '3d6'
        if self.mage.level >= 17:
            spell_dict['damage_dice'] = '4d6'
        return spell_dict

    def Vicious_Mockery(self, spell_level, gen_spell = False):
        """Злая насмешка

        Level: Cantrip
        Casting time: 1 Action
        Range: 60 feet
        Components: V
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/vicious-mockery
        """
        spell_dict = {
                'effect':'mockery',
                'direct_hit':True,
                'savethrow':True,
                'savethrow_all':True,
                'savethrow_ability':'wisdom',
                'attacks_number':1,
                'attack_range':60,
                'damage_type':'psychic',
                'damage_dice':'1d4',
                'components':['verbal'],
                'casting_time':'action',
                'spell_level':spell_level,
                'damage_mod':0,
                'spell_save_DC':8 + self.find_spell_attack_mod(),
                'spell_of_choice':'Vicious_Mockery',
                }
        if self.mage.level >= 5:
            spell_dict['damage_dice'] = '2d4'
        if self.mage.level >= 11:
            spell_dict['damage_dice'] = '3d4'
        if self.mage.level >= 17:
            spell_dict['damage_dice'] = '4d4'
        return spell_dict

    def Frostbite(self, spell_level, gen_spell = False):
        """Обморожение.

        Level: Cantrip
        Casting time: 1 Action
        Range: 60 feet
        Components: V, S
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/frostbite
        """
        spell_dict = {
                'direct_hit':True,
                'savethrow':True,
                'savethrow_all':True,
                'savethrow_ability':'constitution',
                'attacks_number':1,
                'attack_range':60,
                'effect':'mockery',
                'damage_type':'cold',
                'damage_dice':'1d6',
                'components':['verbal', 'somatic'],
                'casting_time':'action',
                'spell_level':spell_level,
                'damage_mod':0,
                'spell_save_DC':8 + self.find_spell_attack_mod(),
                'spell_of_choice':'Frostbite',
                }
        if self.mage.level >= 5:
            spell_dict['damage_dice'] = '2d6'
        if self.mage.level >= 11:
            spell_dict['damage_dice'] = '3d6'
        if self.mage.level >= 17:
            spell_dict['damage_dice'] = '4d6'
        return spell_dict

    def Sacred_Flame(self, spell_level, gen_spell = False):
        """Священное пламя.

        Level: Cantrip
        Casting time: 1 Action
        Range: 60 feet
        Components: V, S
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/sacred-flame
        """
        spell_dict = {
                'direct_hit':True,
                'ignore_cover':True,
                'savethrow':True,
                'savethrow_all':True,
                'savethrow_ability':'dexterity',
                'attacks_number':1,
                'attack_range':60,
                'damage_type':'radiant',
                'damage_dice':'1d8',
                'components':['verbal','somatic'],
                'casting_time':'action',
                'spell_level':spell_level,
                'damage_mod':0,
                'spell_save_DC':8 + self.find_spell_attack_mod(),
                'spell_of_choice':'Sacred_Flame',
                }
        if self.mage.level >= 5:
            spell_dict['damage_dice'] = '2d8'
        if self.mage.level >= 11:
            spell_dict['damage_dice'] = '3d8'
        if self.mage.level >= 17:
            spell_dict['damage_dice'] = '4d8'
        return spell_dict

    def Sword_Burst(self, spell_level, gen_spell = False):
        """Вихрь клинков мистического рыцаря.

        Level: Cantrip
        Casting time: 1 Action
        Range: 5 feet
        Components: V
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/sword-burst
        """
        spell_dict = {
                'effect':'burst',
                'direct_hit':True,
                'savethrow':True,
                'savethrow_all':True,
                'savethrow_ability':'dexterity',
                'attacks_number':1,
                'radius':5,
                'attack_range':5,
                'damage_type':'force',
                'damage_dice':'1d6',
                'components':['verbal'],
                'casting_time':'action',
                'damage_mod':0,
                'spell_level':spell_level,
                'spell_save_DC':8 + self.find_spell_attack_mod(),
                'spell_of_choice':'Sword_Burst',
                }
        if self.mage.level >= 5:
            spell_dict['damage_dice'] = '2d6'
        if self.mage.level >= 11:
            spell_dict['damage_dice'] = '3d6'
        if self.mage.level >= 17:
            spell_dict['damage_dice'] = '4d6'
        return spell_dict

    def Thunderclap(self, spell_level, gen_spell = False):
        """Громовая атака барда.

        Level: Cantrip
        Casting time: 1 Action
        Range: 5 feet
        Components: S
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/thunderclap
        """
        spell_dict = {
                'effect':'burst',
                'direct_hit':True,
                'savethrow':True,
                'savethrow_all':True,
                'savethrow_ability':'constitution',
                'attacks_number':1,
                'radius':5,
                'attack_range':5,
                'damage_type':'thunder',
                'damage_dice':'1d6',
                'components':['somatic'],
                'casting_time':'action',
                'damage_mod':0,
                'spell_level':spell_level,
                'spell_save_DC':8 + self.find_spell_attack_mod(),
                'spell_of_choice':'Thunderclap',
                }
        if self.mage.level >= 5:
            spell_dict['damage_dice'] = '2d6'
        if self.mage.level >= 11:
            spell_dict['damage_dice'] = '3d6'
        if self.mage.level >= 17:
            spell_dict['damage_dice'] = '4d6'
        return spell_dict

    def Word_of_Radiance(self, spell_level, gen_spell = False):
        """Слово сияния.

        Level: Cantrip
        Casting time: 1 Action
        Range: 5 feet
        Components: V, M (a holy symbol)
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/word-of-radiance
        """
        spell_dict = {
                'effect':'burst',
                'direct_hit':True,
                'savethrow':True,
                'savethrow_all':True,
                'savethrow_ability':'constitution',
                'attacks_number':1,
                'radius':5,
                'attack_range':5,
                'damage_type':'radiant',
                'damage_dice':'1d6',
                'components':['verbal','material'],
                'casting_time':'action',
                'damage_mod':0,
                'spell_level':spell_level,
                'spell_save_DC':8 + self.find_spell_attack_mod(),
                'spell_of_choice':'Word_of_Radiance',
                }
        if self.mage.level >= 5:
            spell_dict['damage_dice'] = '2d6'
        if self.mage.level >= 11:
            spell_dict['damage_dice'] = '3d6'
        if self.mage.level >= 17:
            spell_dict['damage_dice'] = '4d6'
        return spell_dict

    def Create_Bonfire(self, spell_level, gen_spell = False):
        """Сотворение костра.

        Level: Cantrip
        Casting time: 1 Action
        Range: 60 feet
        Components: V, S
        Duration: Concentration, up to 1 minute
        https://www.dnd-spells.com/spell/create-bonfire
        """
        spell_dict = {
                'effect':'bonfire',
                'effect_timer':10,
                'concentration':True,
                'zone_effect':True,
                'zone_danger':True,
                'radius':0,
                'direct_hit':True,
                'savethrow':True,
                'savethrow_all':True,
                'savethrow_ability':'dexterity',
                'attacks_number':1,
                'attack_range':60,
                'damage_type':'fire',
                'damage_dice':'1d8',
                'components':['verbal','somatic'],
                'casting_time':'action',
                'damage_mod':0,
                'spell_level':spell_level,
                'spell_save_DC':8 + self.find_spell_attack_mod(),
                'spell_of_choice':'Create_Bonfire',
                }
        if self.mage.level >= 5:
            spell_dict['damage_dice'] = '2d8'
        if self.mage.level >= 11:
            spell_dict['damage_dice'] = '3d8'
        if self.mage.level >= 17:
            spell_dict['damage_dice'] = '4d8'
        return spell_dict

#----
# Subspells

    def Ice_Knife_Piercing(self, spell_level, gen_spell = False):
        """Главный поражающий элемент заклинания Ice_Knife."""
        # Субзаклинание от Ice_Knife.
        spell_dict = {
                'attacks_number':1,
                'attack_range':60,
                'damage_type':'piercing',
                'damage_dice':'1d10',
                'components':['somatic','material'],
                'casting_time':'action',
                'spell_level':spell_level,
                'damage_mod':0,
                'attack_mod':self.find_spell_attack_mod(),
                'spell_save_DC':8 + self.find_spell_attack_mod(),
                'spell_of_choice':'Ice_Knife_Piercing',
                }
        return spell_dict

    def Ice_Storm_Cold(self, spell_level, gen_spell = False):
        """Град. Повреждения холодом отдельно.
        
        Для каждой отдельной цели.
        """
        spell_dict = {
                'direct_hit':True,
                'savethrow':True,
                'savethrow_ability':'dexterity',
                'attacks_number':1,
                'attack_range':0,
                'damage_type':'cold',
                'damage_dice':'4d6',
                'components':[],
                'casting_time':'free_action',
                'damage_mod':0,
                'spell_level':spell_level,
                'spell_save_DC':8 + self.find_spell_attack_mod(),
                'spell_of_choice':'Magic_Missile',
                }
        return spell_dict

    def Empyrean_Bolt(self, spell_level, gen_spell = False):
        """Дальная атака Эмпирея.

        Он может выбрать тип урона.
        """
        spell_dict = {
                'attacks_number':1,
                'attack_range':600,
                'damage_type':'fire',
                'damage_dice':'7d6',
                'components':['somatic'],
                'casting_time':'action',
                'spell_level':spell_level,
                'damage_mod':0,
                'attack_mod':15,
                'spell_save_DC':23,
                'spell_of_choice':'Empyrean_Bolt',
                }
        return spell_dict

#----
# 1 lvl

    def Healing_Word(self, spell_level, gen_spell = False):
        """Лечащее слово.

        Level: 1
        Casting time: 1 Bonus Action
        Range: 60 feet
        Components: V
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/healing-word
        """
        # Дистанция заклинания увеличена до 120 футов.
        # TODO: в damage_mod получается мод_характеристики + proficiency_bonus.
        # А должно быть только мод_характеристики.
        spell_dict = {
                'direct_hit':True,
                'attacks_number':1,
                'attack_range':120,
                'damage_type':'heal',
                'damage_dice':'1d4',
                'components':['verbal'],
                'casting_time':'bonus_action',
                'spell_level':spell_level,
                'damage_mod':self.find_spell_attack_mod(),
                'spell_save_DC':8 + self.find_spell_attack_mod(),
                'spell_of_choice':'Bane',
                }
        if int(spell_level[0]) > 1:
            dice = int(spell_dict['damage_dice'][0])
            dice += int(spell_level[0]) - 1
            spell_dict['damage_dice'] = str(dice) + spell_dict['damage_dice'][1:]
        if self.mage.class_features.get('Disciple_of_Life'):
            spell_dict['damage_mod'] = 2 + int(spell_level[0])
        return spell_dict

    def Bless(self, spell_level, gen_spell = False):
        """Благословление.

        Level: 1
        Casting time: 1 Action
        Range: 30 feet
        Components: V, S, M (a sprinkling of holy water)
        Duration: Concentration, up to 1 minute
        """
        spell_dict = {
                'concentration':True,
                'effect':'bless',
                'effect_timer':10,
                'direct_hit':True,
                'attacks_number':3,
                'attack_range':30,
                'damage_dice':'1d4',
                'components':['verbal','somatic','material'],
                'casting_time':'action',
                'spell_level':spell_level,
                'spell_save_DC':8 + self.find_spell_attack_mod(),
                'spell_of_choice':'Bane',
                }
        if int(spell_level[0]) > 1:
            spell_dict['attacks_number'] += int(spell_level[0]) - 1
        return spell_dict

    def Shield_of_Faith(self, spell_level, gen_spell = False):
        """Щит веры.


        Level: 1
        Casting time: 1 Bonus Action
        Range: 60 feet
        Components: V, S, M (a small parchment with a bit of holy text written on it)
        Duration: Concentration, up to 10 minutes
        """
        spell_dict = {
                'concentration':True,
                'effect':'shield_of_faith',
                'effect_timer':100,
                'attacks_number':1,
                'attack_range':60,
                'components':['verbal','somatic','material'],
                'casting_time':'bonus_action',
                'spell_level':spell_level,
                'spell_save_DC':8 + self.find_spell_attack_mod(),
                'spell_of_choice':'Bane',
                }
        return spell_dict

    def Fog_Cloud(self, spell_level, gen_spell = False):
        """Туманное облако.

        Level: 1
        Casting time: 1 Action
        Range: 120 feet
        Components: V, S
        Duration: Concentration, up to 1 hour
        https://www.dnd-spells.com/spell/fog-cloud
        """
        spell_dict = {
                'concentration':True,
                'effect':'fog',
                'effect_timer':100,
                'attacks_number':1,
                'radius':20,
                'attack_range':120,
                'components':['verbal','somatic'],
                'casting_time':'action',
                'spell_level':spell_level,
                'spell_save_DC':8 + self.find_spell_attack_mod(),
                'spell_of_choice':'Cause_Fear',
                }
        # Радиус облака растёт на 20 футов за каждый уровень выше первого:
        if int(spell_level[0]) > 1:
            spell_dict['radius'] += 20 * int(spell_level[0])
        return spell_dict

    def Cause_Fear(self, spell_level, gen_spell = False):
        """Вызвать страх.

        Level: 1
        Casting time: 1 Action
        Range: 60 feet
        Components: V
        Duration: Concentration, up to 1 minute
        https://www.dnd-spells.com/spell/cause-fear
        """
        spell_dict = {
                'concentration':True,
                'attacks_number':1,
                'attack_range':60,
                'effect':'fear',
                'effect_timer':10,
                'direct_hit':True,
                'savethrow':True,
                'savethrow_all':True,
                'savethrow_ability':'wisdom',
                'components':['verbal'],
                'casting_time':'action',
                'spell_level':spell_level,
                'spell_save_DC':8 + self.find_spell_attack_mod(),
                'spell_of_choice':'Cause_Fear',
                }
        if int(spell_level[0]) > 1:
            spell_dict['attacks_number'] = int(spell_level[0])
        return spell_dict

    def Hex(self, spell_level, gen_spell = False):
        """Сглаз.

        Level: 1
        Casting time: 1 Bonus Action
        Range: 90 feet
        Components: V, S, M (the petrified eye of a newt)
        Duration: Concentration, up to 1 hour
        https://www.dnd-spells.com/spell/hex
        """
        spell_dict = {
                'concentration':True,
                'effect_timer':600,
                'attacks_number':1,
                'attack_range':90,
                'effect':'hex',
                'direct_hit':True,
                'damage_type':'necrotic_energy',
                'damage_dice':'1d6',
                'components':['verbal','somatic','material'],
                'casting_time':'bonus_action',
                'spell_level':spell_level,
                'spell_save_DC':8 + self.find_spell_attack_mod(),
                'spell_of_choice':'Magic_Missile',
                }
        return spell_dict

    def Sleep(self, spell_level, gen_spell = False):
        """Усыпление.

        Level: 1
        Casting time: 1 Action
        Range: 90 feet
        Components: V, S, M (a pinch of fine sand, rose petals, or a cricket)
        Duration: 1 minute
        https://www.dnd-spells.com/spell/sleep
        """
        spell_dict = {
                'effect':'sleep',
                'effect_timer':100,
                'attacks_number':1,
                'attack_range':90,
                'damage_type':'sleep',
                'damage_dice':'5d8',
                'components':['verbal','somatic','material'],
                'casting_time':'action',
                'spell_level':spell_level,
                'spell_save_DC':8 + self.find_spell_attack_mod(),
                'spell_of_choice':'Sleep',
                }
        # Плюс одна кость усыпления за каждый уровень выше первого:
        if int(spell_level[0]) > 1:
            dice = int(spell_dict['damage_dice'][0])
            dice += int(spell_level[0]) - 1
            spell_dict['damage_dice'] = str(dice) + spell_dict['damage_dice'][1:]
        if self.mage.class_features.get('Metamagic_Distant_Spell'):
            spell_dict['attack_range'] *= 2
        return spell_dict

    def Entangle(self, spell_level, gen_spell = False):
        """Опутывание.

        Level: 1
        Casting time: 1 Action
        Range: 90 feet
        Components: V, S
        Duration: Concentration, up to 1 minute
        https://www.dnd-spells.com/spell/entangle
        """
        # TODO: Чертовски неудобно использовать как зональное заклинание.
        # Пусть лучше будет 10 целей, эффект опутывания и растущие кусты.
        spell_dict = {
                'concentration':True,
                'effect':'entangle',
                'effect_timer':10,
                #'zone':True,
                #'zone_shape':'square',
                #'radius':10,
                'direct_hit':True,
                'savethrow':True,
                'savethrow_all':True,
                'savethrow_ability':'strength',
                'attacks_number':10,
                'attack_range':90,
                'components':['verbal','somatic'],
                'casting_time':'action',
                'spell_level':spell_level,
                'spell_save_DC':8 + self.find_spell_attack_mod(),
                'spell_of_choice':'Entangle',
                }
        return spell_dict

    def Magic_Missile(self, spell_level, gen_spell = False):
        """Волшебная стрела.

        Level: 1
        Casting time: 1 Action
        Range: 120 feet
        Components: V,S
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/magic-missile
        """
        spell_dict = {
                'direct_hit':True,
                'attacks_number':3,
                'attack_range':120,
                'damage_type':'force',
                'damage_dice':'1d4',
                'components':['verbal','somatic'],
                'casting_time':'action',
                'spell_level':spell_level,
                'damage_mod':+1,
                'spell_of_choice':'Magic_Missile',
                }
        # За каждый уровень сверх первого один дополнительный дротик:
        if int(spell_level[0]) > 1:
            spell_dict['attacks_number'] += int(spell_level[0]) - 1
        if self.mage.class_features.get('Metamagic_Distant_Spell'):
            spell_dict['attack_range'] *= 2
        return spell_dict

    def Guiding_Bolt(self, spell_level, gen_spell = False):
        """Направленный снаряд.

        Level: 1
        Casting time: 1 Action
        Range: 120 feet
        Components: V, S
        Duration: 1 round
        https://www.dnd-spells.com/spell/guiding-bolt
        """
        spell_dict = {
                #'direct_hit':True,
                'effect':'guiding_bolt_hit',
                'attacks_number':1,
                'attack_range':120,
                'damage_type':'radiant',
                'damage_dice':'4d6',
                'components':['verbal','somatic'],
                'casting_time':'action',
                'spell_level':spell_level,
                'damage_mod':0,
                'attack_mod':self.find_spell_attack_mod(),
                'spell_save_DC':8 + self.find_spell_attack_mod(),
                'spell_of_choice':'Guiding_Bolt',
                }
        if int(spell_level[0]) > 1:
            dice = int(spell_dict['damage_dice'][0])
            dice += int(spell_level[0]) - 1
            spell_dict['damage_dice'] = str(dice) + spell_dict['damage_dice'][1:]
        if self.mage.class_features.get('Metamagic_Distant_Spell'):
            spell_dict['attack_range'] *= 2
        return spell_dict

    def Burning_Hands(self, spell_level, gen_spell = False):
        """Огненные ладони.

        Level: 1
        Casting time: 1 Action
        Range: Self (15-foot cone)
        Components: V, S
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/burning-hands
        """
        spell_dict = {
                'zone':True,
                'zone_shape':'cone',
                'direct_hit':True,
                'savethrow':True,
                'savethrow_ability':'dexterity',
                'attacks_number':1,
                'attack_range':15,
                'damage_type':'fire',
                'damage_dice':'3d6',
                'components':['verbal','somatic'],
                'casting_time':'action',
                'damage_mod':0,
                'spell_level':spell_level,
                'spell_save_DC':8 + self.find_spell_attack_mod(),
                'spell_of_choice':'Magic_Missile',
                }
        if int(spell_level[0]) > 1:
            dice = int(spell_dict['damage_dice'][0])
            dice += int(spell_level[0]) - 1
            spell_dict['damage_dice'] = str(dice) + spell_dict['damage_dice'][1:]
        return spell_dict

    def Shield(self, spell_level, gen_spell = False):
        """Щит.

        Level: 1
        Casting time: Special
        Range: Self
        Components: V, S
        Duration: 1 round
        https://www.dnd-spells.com/spell/shield
        """
        spell_dict = {
                'effect':'shield',
                'effect_timer':1,
                'attack_range':0,
                'components':['verbal','somatic'],
                'casting_time':'reaction',
                'spell_level':spell_level,
                'spell_of_choice':'Magic_Missile',
                }
        return spell_dict

    def Absorb_Elements(self, spell_level, gen_spell = False):
        """Поглощение стихий.

        Level: 1
        Casting time: Special
        Range: Self
        Components: S
        Duration: 1 round
        https://www.dnd-spells.com/spell/absorb-elements
        """
        # 1d6 урона поглощённого типа можно направить атакой оружием в следующем раунде.
        spell_dict = {
                'effect':'absorb_elements',
                'direct_hit':True,
                'effect_timer':1,
                'attack_range':0,
                'absorb_damage_type':['acid','cold','fire','lightning','thunder'],
                'damage_type':'absorbed',
                'damage_dice':'1d6',
                'components':['somatic'],
                'casting_time':'reaction',
                'damage_mod':0,
                'spell_level':spell_level,
                'spell_of_choice':'Magic_Missile',
                }
        if int(spell_level[0]) > 1:
            dice = int(spell_dict['damage_dice'][0])
            dice += int(spell_level[0]) - 1
            spell_dict['damage_dice'] = str(dice) + spell_dict['damage_dice'][1:]
        return spell_dict

    def Mage_Armor(self, spell_level, gen_spell = False):
        """Доспехи мага.

        Level: 1
        Casting time: 1 Action
        Range: Touch
        Components: V, S, M
        Duration: 8 hours
        https://www.dnd-spells.com/spell/mage-armor
        """
        # TODO: броня берётся из metadict_item.
        spell_dict = {
                'effect':'mage_armor',
                'armor':True,
                'armor_type':'Force',
                'armor_class_armor':13,
                'attack_range':0,
                'components':['verbal','somatic','material'],
                'casting_time':'action',
                'spell_level':spell_level,
                'spell_of_choice':'Magic_Missile',
                }
        if gen_spell:
            soldier = self.mage
            soldier.buffs[spell_dict['effect']] = spell_dict
            soldier.equipment_weapon['Mage_Armor'] = 1
            soldier.armor.update(soldier.get_armor())
            #soldier.mage_armor = spell_dict
            if soldier.class_features.get('Arcane_Ward') and not soldier.bonus_hitpoints:
                soldier.bonus_hitpoints = soldier.level * 2 + soldier.mods['intelligence']
                soldier.arcane_ward = True
        return spell_dict

    def Armor_of_Agathys(self, spell_level, gen_spell = False):
        """Доспех Агатиса.


        Level: 1
        Casting time: 1 Action
        Range: Self
        Components: V, S, M (a cup of water)
        Duration: 1 hour
        https://www.dnd-spells.com/spell/armor-of-agathys
        """
        spell_dict = {
                'effect':'armor_of_agathys',
                'effect_timer':600,
                'direct_hit':True,
                'attack_range':10,
                'damage_type':'cold',
                'damage_dice':'0d0',
                'damage_mod':5,
                'components':['verbal','somatic','material'],
                'casting_time':'free_action',
                'spell_level':spell_level,
                'spell_of_choice':'Magic_Missile',
                }
        if int(spell_level[0]) > 1:
            spell_dict['damage_mod'] *= int(spell_level[0])
        if gen_spell:
            soldier = self.mage
            soldier.bonus_hitpoints = spell_dict['damage_mod']
            soldier.buffs[spell_dict['effect']] = spell_dict
        return spell_dict

    def Ice_Knife(self, spell_level, gen_spell = False):
        """Ледяной кинжал.

        Level: 1
        Casting time: 1 Action
        Range: 60 feet
        Components: S, M
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/ice-knife
        """
        spell_dict = {
                'effect':'ice_knife',
                'subspell':('subspell', 'Ice_Knife_Piercing'),
                'zone':True,
                'direct_hit':True,
                'savethrow':True,
                'savethrow_all':True,
                'savethrow_ability':'dexterity',
                'attacks_number':1,
                'attack_range':60,
                'radius':5,
                'damage_type':'cold',
                'damage_dice':'2d6',
                'components':['somatic','material'],
                'casting_time':'action',
                'damage_mod':0,
                'spell_level':spell_level,
                'spell_save_DC':8 + self.find_spell_attack_mod(),
                'spell_of_choice':'Magic_Missile',
                }
        # Добавляем субзаклинание Ice_Knife_Piercing как основной поражающий элемент:
        if spell_dict.get('subspell'):
            subspell = spell_dict['subspell']
            subspell_name = spell_dict['subspell'][-1]
            subspell_level = spell_dict['subspell'][0]
            if subspell_name in self.usable_spells and not self.spells.get(subspell):
                func = getattr(self, subspell_name)
                self.spells[subspell] = func(subspell_level)
        if int(spell_level[0]) > 1:
            dice = int(spell_dict['damage_dice'][0])
            dice += int(spell_level[0]) - 1
            spell_dict['damage_dice'] = str(dice) + spell_dict['damage_dice'][1:]
        if self.mage.class_features.get('Metamagic_Distant_Spell'):
            spell_dict['attack_range'] *= 2
        return spell_dict

    def Hail_of_Thorns(self, spell_level, gen_spell = False):
        """Град шипов.

        Level: 1
        Casting time: 1 Bonus Action
        Range: Self
        Components: V
        Duration: Concentration, up to 1 minute
        https://www.dnd-spells.com/spell/hail-of-thorns
        """
        spell_dict = {
                'ammo':1,
                'concentration':True,
                'concentration_ready':True,
                'effect':'thorns',
                'effect_timer':10,
                'zone':True,
                'zone_shape':'square',
                'direct_hit':True,
                'savethrow':True,
                'savethrow_ability':'dexterity',
                'attacks_number':1,
                'attack_range':600,
                'radius':5,
                'damage_type':'piercing',
                'damage_dice':'1d10',
                'components':['verbal'],
                'casting_time':'bonus_action',
                'damage_mod':0,
                'spell_level':spell_level,
                'spell_save_DC':8 + self.find_spell_attack_mod(),
                'spell_of_choice':'Magic_Missile',
                }
        if int(spell_level[0]) > 1:
            dice = int(spell_dict['damage_dice'][0])
            dice += int(spell_level[0]) - 1
            spell_dict['damage_dice'] = str(dice) + spell_dict['damage_dice'][1:]
        return spell_dict

    def Arms_of_Hadar(self, spell_level, gen_spell = False):
        """Руки хадара.

        Level: 1
        Casting time: 1 Action
        Range: Self (10-foot radius)
        Components: V, S
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/arms-of-hadar
        """
        # TODO: сделай сбивание реакции.
        spell_dict = {
                'effect':'burst',
                'direct_hit':True,
                'savethrow':True,
                'savethrow_ability':'strength',
                'attacks_number':1,
                'radius':10,
                'attack_range':5,
                'damage_type':'necrotic',
                'damage_dice':'2d6',
                'components':['verbal', 'somatic'],
                'casting_time':'action',
                'damage_mod':0,
                'spell_level':spell_level,
                'spell_save_DC':8 + self.find_spell_attack_mod(),
                'spell_of_choice':'Arms_of_Hadar',
                }
        if int(spell_level[0]) > 1:
            dice = int(spell_dict['damage_dice'][0])
            dice += int(spell_level[0]) - 1
            spell_dict['damage_dice'] = str(dice) + spell_dict['damage_dice'][1:]
        return spell_dict

    def Thunderwave(self, spell_level, gen_spell = False):
        """Волна грома.

        Level: 1
        Casting time: 1 Action
        Range: Self (15-foot cube)
        Components: V, S
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/thunderwave
        """
        # TODO: сделай отталкивание
        spell_dict = {
                'effect':'burst',
                'direct_hit':True,
                'savethrow':True,
                'zone_shape':'square',
                'savethrow_ability':'constitution',
                'attacks_number':1,
                'radius':5,
                'attack_range':5,
                'damage_type':'thunder',
                'damage_dice':'2d8',
                'components':['verbal', 'somatic'],
                'casting_time':'action',
                'damage_mod':0,
                'spell_level':spell_level,
                'spell_save_DC':8 + self.find_spell_attack_mod(),
                'spell_of_choice':'Thunderwave',
                }
        if int(spell_level[0]) > 1:
            dice = int(spell_dict['damage_dice'][0])
            dice += int(spell_level[0]) - 1
            spell_dict['damage_dice'] = str(dice) + spell_dict['damage_dice'][1:]
        return spell_dict

#----
# 2 lvl

    def Scorching_Ray(self, spell_level, gen_spell = False):
        """Палящий луч.

        Level: 2
        Casting time: 1 Action
        Range: 120 feet
        Components: V, S
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/scorching-ray
        """
        spell_dict = {
                #'direct_hit':True,
                'attacks_number':3,
                'attack_range':120,
                'damage_type':'fire',
                'damage_dice':'2d6',
                'components':['verbal','somatic'],
                'casting_time':'action',
                'spell_level':spell_level,
                'damage_mod':0,
                'attack_mod':self.find_spell_attack_mod(),
                'spell_save_DC':8 + self.find_spell_attack_mod(),
                'spell_of_choice':'Scorching_Ray',
                }
        # За каждый уровень сверх первого один дополнительный луч:
        if int(spell_level[0]) > 1:
            spell_dict['attacks_number'] += int(spell_level[0]) - 1
        if self.mage.class_features.get('Metamagic_Distant_Spell'):
            spell_dict['attack_range'] *= 2
        return spell_dict

    def Melfs_Acid_Arrow(self, spell_level, gen_spell = False):
        """Кислотная стрела Мельфа.

        Level: 2
        Casting time: 1 Action
        Range: 90 feet
        Components: V, S, M (powdered rhubarb leaf and an adder’s stomach)
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/melfs-acid-arrow
        """
        # TODO: 2d4 урона в следующий раунд.
        spell_dict = {
                'effect':'acid_arrow',
                'direct_hit':True,
                'savethrow':True,
                'savethrow_ability':'dexterity',
                'attacks_number':1,
                'attack_range':120,
                'damage_type':'acid',
                'damage_dice':'6d4',
                'components':['verbal','somatic','material'],
                'casting_time':'action',
                'spell_level':spell_level,
                'damage_mod':0,
                'attack_mod':self.find_spell_attack_mod(),
                'spell_save_DC':8 + self.find_spell_attack_mod(),
                'spell_of_choice':'Melfs_Acid_Arrow',
                }
        if int(spell_level[0]) > 2:
            dice = int(spell_dict['damage_dice'][0])
            dice += int(spell_level[0]) * 2 - 1
            spell_dict['damage_dice'] = str(dice) + spell_dict['damage_dice'][1:]
        if self.mage.class_features.get('Metamagic_Distant_Spell'):
            spell_dict['attack_range'] *= 2
        return spell_dict

    def Moonbeam(self, spell_level, gen_spell = False):
        """Лунный луч.

        Level: 2
        Casting time: 1 Action
        Range: 120 feet
        Components: V, S, M (several seeds of any moonseed plant and a piece of opalescent feldspar)
        https://www.dnd-spells.com/spell/moonbeam
        """
        spell_dict = {
                'concentration':True,
                'effect':'moonbeam',
                'effect_timer':10,
                'zone':True,
                'zone_shape':'2x2',
                'zone_effect':True,
                'zone_danger':True,
                'direct_hit':True,
                'savethrow':True,
                'savethrow_ability':'dexterity',
                'attacks_number':1,
                'attack_range':120,
                'radius':5,
                'damage_type':'radiant',
                'damage_dice':'2d10',
                'components':['verbal','somatic','material'],
                'casting_time':'action',
                'damage_mod':0,
                'spell_level':spell_level,
                'spell_save_DC':8 + self.find_spell_attack_mod(),
                'spell_of_choice':'Magic_Missile',
                }
        if int(spell_level[0]) > 2:
            dice = int(spell_dict['damage_dice'][0])
            dice += int(spell_level[0]) - 1
            spell_dict['damage_dice'] = str(dice) + spell_dict['damage_dice'][1:]
        return spell_dict

    def Blur(self, spell_level, gen_spell = False):
        """Размытый образ.

        Level: 2
        Casting time: 1 Action
        Range: Self
        Components: V
        Duration: Concentration, up to 1 minute
        https://www.dnd-spells.com/spell/blur
        """
        spell_dict = {
                'concentration':True,
                'effect':'blur',
                'effect_timer':10,
                'attack_range':0,
                'components':['verbal'],
                'casting_time':'action',
                'spell_level':spell_level,
                'spell_of_choice':'Magic_Missile',
                }
        return spell_dict

    def Shatter(self, spell_level, gen_spell = False):
        """Дребезги.

        Level: 2
        Casting time: 1 Action
        Range: 60 feet
        Components: V, S, M (a chip of mica)
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/shatter
        """
        spell_dict = {
                'zone':True,
                'direct_hit':True,
                'savethrow':True,
                'savethrow_ability':'constitution',
                'attacks_number':1,
                'attack_range':60,
                'radius':10,
                'damage_type':'thunder',
                'damage_dice':'3d8',
                'components':['verbal','somatic','material'],
                'casting_time':'action',
                'damage_mod':0,
                'spell_level':spell_level,
                'spell_save_DC':8 + self.find_spell_attack_mod(),
                'spell_of_choice':'Magic_Missile',
                }
        if int(spell_level[0]) > 2:
            dice = int(spell_dict['damage_dice'][0])
            dice += int(spell_level[0]) - 1
            spell_dict['damage_dice'] = str(dice) + spell_dict['damage_dice'][1:]
        if self.mage.class_features.get('Metamagic_Distant_Spell'):
            spell_dict['attack_range'] *= 2
        return spell_dict

    def Darkness(self, spell_level, gen_spell = False):
        """Темнота.
        
        Вокруг предмета, или вокруг точки.

        Level: 2
        Casting time: 1 Action
        Range: 60 feet
        Components: V, M (bat fur and a drop of pitch or piece of coal)
        Duration: Concentration, up to 10 minutes
        https://www.dnd-spells.com/spell/darkness
        """
        spell_dict = {
                # Радиус 20 из-за круглой зоны. Получается 35 футов.
                'concentration':True,
                'effect':'darkness',
                'effect_timer':100,
                'zone_effect':True,
                'zone_self':True,
                'direct_hit':True,
                'attacks_number':1,
                'attack_range':60,
                'radius':20,
                'components':['verbal','material'],
                'casting_time':'action',
                'spell_level':spell_level,
                'spell_save_DC':8 + self.find_spell_attack_mod(),
                'spell_of_choice':'Darkness',
                }
        if self.mage.class_features.get('Metamagic_Distant_Spell'):
            spell_dict['attack_range'] *= 2
        return spell_dict

#----
# 3 lvl

    def Fear(self, spell_level, gen_spell = False):
        """Ужас.

        Level: 3
        Casting time: 1 Action
        Range: Self (30-foot cone)
        Components: V, S, M (a white feather or the heart of a hen)
        Duration: Concentration, up to 1 minute 
        https://www.dnd-spells.com/spell/fear
        """
        spell_dict = {
                'concentration':True,
                'effect':'fear',
                'effect_timer':10,
                'zone':True,
                'zone_shape':'cone',
                'attack_range':30,
                'direct_hit':True,
                'savethrow':True,
                'savethrow_all':True,
                'savethrow_ability':'wisdom',
                'components':['verbal'],
                'casting_time':'action',
                'spell_level':spell_level,
                'spell_save_DC':8 + self.find_spell_attack_mod(),
                'spell_of_choice':'Magic_Missile',
                }
        return spell_dict

    def Call_Lightning(self, spell_level, gen_spell = False):
        """Призыв молнии.

        Level: 3
        Casting time: 1 Action
        Range: 120 feet
        Components: V, S
        Duration: Concentration, up to 10 minutes
        https://www.dnd-spells.com/spell/call-lightning
        """
        # Зона поражения 2x2 клетки, а не 3x3.
        # Молния поражает цели в пределах 5 футов от точки.
        spell_dict = {
                'concentration':True,
                'effect':'call_lightning',
                'effect_timer':100,
                'zone':True,
                'zone_shape':'2x2',
                'direct_hit':True,
                'savethrow':True,
                'savethrow_ability':'dexterity',
                'attacks_number':1,
                'attack_range':120,
                'radius':5,
                'damage_type':'lightning',
                'damage_dice':'3d10',
                'components':['verbal','somatic'],
                'casting_time':'action',
                'damage_mod':0,
                'spell_level':spell_level,
                'spell_save_DC':8 + self.find_spell_attack_mod(),
                'spell_of_choice':'Magic_Missile',
                }
        if int(spell_level[0]) > 3:
            dice = int(spell_dict['damage_dice'][0])
            dice += int(spell_level[0]) - 1
            spell_dict['damage_dice'] = str(dice) + spell_dict['damage_dice'][1:]
        return spell_dict

    def Fireball(self, spell_level, gen_spell = False):
        """Огненный шар.

        Level: 3
        Casting time: 1 Action
        Range: 150 feet
        Components: V,S,M
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/fireball
        """
        spell_dict = {
                'zone':True,
                'direct_hit':True,
                'savethrow':True,
                'savethrow_ability':'dexterity',
                'attacks_number':1,
                'attack_range':150,
                'radius':20,
                'damage_type':'fire',
                'damage_dice':'8d6',
                'components':['verbal','somatic','material'],
                'casting_time':'action',
                'damage_mod':0,
                'spell_level':spell_level,
                'spell_save_DC':8 + self.find_spell_attack_mod(),
                'spell_of_choice':'Magic_Missile',
                }
        if int(spell_level[0]) > 3:
            dice = int(spell_dict['damage_dice'][0])
            dice += int(spell_level[0]) - 1
            spell_dict['damage_dice'] = str(dice) + spell_dict['damage_dice'][1:]
        if self.mage.class_features.get('Metamagic_Distant_Spell'):
            spell_dict['attack_range'] *= 2
        return spell_dict

    def Lightning_Bolt(self, spell_level, gen_spell = False):
        """Удар молнии.

        Level: 3
        Casting time: 1 Action
        Range: Self (100-foot line)
        Components: V, S, M (a bit of fur and a rod of amber, crystal, or glass)
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/lightning-bolt
        """
        # TODO: добавь эффект no_cover. А то следующие цели получают +2, +5 к спасброскам ловкости.
        spell_dict = {
                'zone':True,
                'zone_shape':'ray',
                #'ignore_cover':True,
                'direct_hit':True,
                'savethrow':True,
                'savethrow_ability':'dexterity',
                'attacks_number':1,
                'attack_range':100,
                'damage_type':'lightning',
                'damage_dice':'8d6',
                'components':['verbal','somatic','material'],
                'casting_time':'action',
                'damage_mod':0,
                'spell_level':spell_level,
                'spell_save_DC':8 + self.find_spell_attack_mod(),
                'spell_of_choice':'Magic_Missile',
                }
        if int(spell_level[0]) > 3:
            dice = int(spell_dict['damage_dice'][0])
            dice += int(spell_level[0]) - 1
            spell_dict['damage_dice'] = str(dice) + spell_dict['damage_dice'][1:]
        if self.mage.class_features.get('Metamagic_Distant_Spell'):
            spell_dict['attack_range'] *= 2
        return spell_dict

    def Melf_Minute_Meteors(self, spell_level, gen_spell = False):
        """Мельфовы маленькие метеоры.

        Level: 3
        Casting time: 1 Action
        Range: Self
        Components: V, S, M
        Duration: Concentration, up to 10 minutes
        https://www.dnd-spells.com/spell/melfs-minute-meteors
        """
        spell_dict = {
                'ammo':6,
                'concentration':True,
                'concentration_ready':True,
                'effect':'minute_meteors',
                'effect_timer':100,
                'zone':True,
                'zone_shape':'square',
                'radius':5,
                'direct_hit':True,
                'savethrow':True,
                'savethrow_ability':'dexterity',
                'attacks_number':1,
                'attack_range':120,
                'damage_type':'fire',
                'damage_dice':'2d6',
                'components':['verbal'],
                'casting_time':'bonus_action',
                'damage_mod':0,
                'spell_level':spell_level,
                'spell_save_DC':8 + self.find_spell_attack_mod(),
                'spell_of_choice':'Magic_Missile',
                }
        if int(spell_level[0]) > 3:
            bonus_ammo = 2 * int(spell_level[0]) - 3 * 2
            spell_dict['ammo'] += bonus_ammo
        return spell_dict

    def Counterspell(self, spell_level, gen_spell = False):
        """Контрзаклинание.

        Дальность 300 футов. Нужно видеть врага.

        Level: 3
        Casting time: Special
        Range: 60 feet
        Components: S
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/counterspell
        """
        spell_dict = {
                'effect':'counterspell',
                'attack_range':300,
                'components':['somatic'],
                'casting_time':'reaction',
                'spell_level':spell_level,
                'spell_of_choice':'Magic_Missile',
                }
        return spell_dict

    def Dispel_Magic(self, spell_level, gen_spell = False):
        """Рассеивание магии.
        
        Можно использовать как импровизированный Counterspell
        В этом случае используется подготовленное действие.

        Level: 3
        Casting time: 1 Action
        Range: 120 feet
        Components: V, S
        Duration: Instantaneous
        """
        spell_dict = {
                'effect':'counterspell',
                'attack_range':120,
                'components':['verbal','somatic'],
                'casting_time':'action',
                'spell_level':spell_level,
                'spell_of_choice':'Magic_Missile',
                }
        return spell_dict

    def Crusaders_Mantle(self, spell_level, gen_spell = False):
        """Мантия крестоносца.

        Level: 3
        Casting time: 1 Action
        Range: Self
        Components: V
        Duration: Concentration, up to 1 minute
        https://www.dnd-spells.com/spell/crusaders-mantle
        """
        spell_dict = {
                'safe':True,
                'concentration':True,
                'effect':'crusaders_mantle',
                'effect_timer':10,
                'zone_effect':True,
                'zone_self':True,
                'direct_hit':True,
                'attack_range':0,
                'radius':30,
                'components':['verbal'],
                'damage_type':'radiant',
                'damage_dice':'1d4',
                'casting_time':'action',
                'spell_level':spell_level,
                'damage_mod':0,
                'spell_of_choice':'Magic_Missile',
                }
        return spell_dict


    def Spirit_Guardians(self, spell_level, gen_spell = False):
        """Духовные стражи.

        Level: 3
        Casting time: 1 Action
        Range: Self (15-foot-radius)
        Components: V, S, M (a holy symbol)
        Duration: Concentration, up to 10 minutes
        https://www.dnd-spells.com/spell/spirit-guardians
        """
        spell_dict = {
                'safe':True,
                'concentration':True,
                'effect':'spirit_guardians',
                'effect_timer':100,
                'zone_effect':True,
                'zone_danger':True,
                'zone_self':True,
                'direct_hit':True,
                'savethrow':True,
                'savethrow_ability':'wisdom',
                'attacks_number':1,
                'radius':15,
                'attack_range':0,
                'damage_type':'radiant',
                'damage_dice':'3d8',
                'components':['verbal','somatic','material'],
                'casting_time':'action',
                'damage_mod':0,
                'spell_level':spell_level,
                'spell_save_DC':8 + self.find_spell_attack_mod(),
                'spell_of_choice':'Sacred_Flame',
                }
        if int(spell_level[0]) > 3:
            dice = int(spell_dict['damage_dice'][0])
            dice += int(spell_level[0]) - 1
            spell_dict['damage_dice'] = str(dice) + spell_dict['damage_dice'][1:]
        return spell_dict

#----
# 4 lvl

    def Ice_Storm(self, spell_level, gen_spell = False):
        """Град

        Level: 4
        Casting time: 1 Action
        Range: 300 feet
        Components: V, S, M (a pinch of dust and a few drops of water)
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/ice-storm
        """
        spell_dict = {
                'zone':True,
                'direct_hit':True,
                'savethrow':True,
                'savethrow_ability':'dexterity',
                'subspell':('subspell', 'Ice_Storm_Cold'),
                'attacks_number':1,
                'attack_range':300,
                'radius':20,
                'damage_type':'bludgeoning',
                'damage_dice':'2d8',
                'components':['verbal','somatic','material'],
                'casting_time':'action',
                'damage_mod':0,
                'spell_level':spell_level,
                'spell_save_DC':8 + self.find_spell_attack_mod(),
                'spell_of_choice':'Magic_Missile',
                }
        if spell_dict.get('subspell'):
            subspell = spell_dict['subspell']
            subspell_name = spell_dict['subspell'][-1]
            subspell_level = spell_dict['subspell'][0]
            if subspell_name in self.usable_spells and not self.spells.get(subspell):
                func = getattr(self, subspell_name)
                self.spells[subspell] = func(subspell_level)
        if int(spell_level[0]) > 4:
            dice = int(spell_dict['damage_dice'][0])
            dice += int(spell_level[0]) - 1
            spell_dict['damage_dice'] = str(dice) + spell_dict['damage_dice'][1:]
        if self.mage.class_features.get('Metamagic_Distant_Spell'):
            spell_dict['attack_range'] *= 2
        return spell_dict

#----
# 5 lvl

    def Cone_of_Cold(self, spell_level, gen_spell = False):
        """Конус холода.

        Level: 5
        Casting time: 1 Action
        Range: Self (60-foot cone)
        Components: V, S, M (a small crystal or glass cone)
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/cone-of-cold
        """
        # TODO: effect "icing" -- превращает погибших в ледяные статуи.
        spell_dict = {
                'zone':True,
                'zone_shape':'cone',
                'direct_hit':True,
                'savethrow':True,
                'savethrow_ability':'constitution',
                'attacks_number':1,
                'attack_range':60,
                'damage_type':'cold',
                'damage_dice':'8d8',
                'components':['verbal','somatic','material'],
                'casting_time':'action',
                'damage_mod':0,
                'spell_level':spell_level,
                'spell_save_DC':8 + self.find_spell_attack_mod(),
                'spell_of_choice':'Magic_Missile',
                }
        if int(spell_level[0]) > 5:
            dice = int(spell_dict['damage_dice'][0])
            dice += int(spell_level[0]) - 1
            spell_dict['damage_dice'] = str(dice) + spell_dict['damage_dice'][1:]
        return spell_dict

    def Dawn(self, spell_level, gen_spell = False):
        """Рассвет.

        Level: 5
        Casting time: 1 Action
        Range: 60 feet
        Components: V, S, M (a sunburst pendant worth at least 100 gp)
        Duration: Concentration, up to 1 minute 
        https://www.dnd-spells.com/spell/dawn
        """
        # Первый удар заклинания неожиданный, дальше только смещение луча.
        spell_dict = {
                'ammo':1,
                'concentration':True,
                'concentration_no_ammo':True,
                'effect':'dawn',
                'effect_timer':10,
                'zone':True,
                'zone_effect':True,
                'zone_danger':True,
                'direct_hit':True,
                'savethrow':True,
                'savethrow_ability':'constitution',
                'attacks_number':1,
                'attack_range':60,
                'radius':30,
                'damage_type':'radiant',
                'damage_dice':'4d10',
                'components':['verbal','somatic','material'],
                'casting_time':'action',
                'damage_mod':0,
                'spell_level':spell_level,
                'spell_save_DC':8 + self.find_spell_attack_mod(),
                'spell_of_choice':'Magic_Missile',
                }
        #if int(spell_level[0]) > 5:
        #    dice = int(spell_dict['damage_dice'][0])
        #    dice += int(spell_level[0]) - 1
        #    spell_dict['damage_dice'] = str(dice) + spell_dict['damage_dice'][1:]
        return spell_dict
