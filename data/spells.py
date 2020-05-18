#!/usr/bin/env python
# -*- coding: utf-8 -*-

import inspect
import random

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
                self.spells[spell] = func(spell_level)
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
        if self.mage.char_class == 'Sorcerer'\
                or self.mage.char_class == 'Bard'\
                or self.mage.char_class == 'Warlock'\
                or self.mage.char_class == 'Barbarian'\
                or self.mage.char_class == 'Paladin':
            attack_mod = self.mage.mods['charisma'] + self.mage.proficiency_bonus
        if self.mage.char_class == 'Cleric'\
                or self.mage.char_class == 'Cleric-heavy'\
                or self.mage.char_class == 'Druid'\
                or self.mage.char_class == 'Ranger'\
                or self.mage.char_class == 'Monk':
            attack_mod = self.mage.mods['wisdom'] + self.mage.proficiency_bonus
        # Монстры:
        if self.mage.char_class == 'Empyrean':
            attack_mod = self.mage.mods['charisma'] + self.mage.proficiency_bonus
        return attack_mod

    def find_spell(self, spell_name):
        """Поиск заклинания из доступных.
        
        Случайный выбор, если несколько одинаковых заклинаний на разных уровнях.
        """
        spell_list = [spell for spell in self.spells if spell[-1] == spell_name]
        if spell_list:
            spell_choice = random.choice(spell_list)
            return spell_choice

    def use_spell(self, spell_choice):
        """Расходуется ячейка заклинания, очищается словарь self.spells."""
        spell_slot_use = spell_choice[0]
        # Заклинания 0 уровня бесконечные:
        if spell_slot_use == 'cantrip':
            return self.spells[spell_choice]
        # Используем ячейку заклинания:
        for spell_slot in self.spellslots:
            if spell_slot == spell_slot_use:
                if self.spellslots[spell_slot] > 1:
                    self.spellslots[spell_slot] -= 1
                    return self.spells[spell_choice]
                else:
                    # Убираем закончившиеся ячейки:
                    # Убираем заклинания этого уровня, если ячейки закончились:
                    self.spellslots.pop(spell_slot)
                    spells_to_remove = [spell for spell in self.spells if spell[0] == spell_slot_use]
                    spell_dict = self.spells[spell_choice]
                    for spell in spells_to_remove:
                        self.spells.pop(spell)
                    return spell_dict

#----
# Channel_Divinity

    def Radiance_of_the_Dawn(self, spell_level):
        """Смертоносная вспышка. Жрецы домена света.
        
        """
        # TODO: абсолютно убийственная способность. Сотни обожённых, сотни смертей.
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

    def Divine_Smite(self, spell_level):
        """Смертоносная атака паладина
        
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

    def Sacred_Weapon(self, spell_level):
        """Бонус харизмы к атаке оружия.
        
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

#----
# Cantrips

    def Eldritch_Blast(self, spell_level):
        """Мистический заряд. Главное оружие колдуна.

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

    def Fire_Bolt(self, spell_level):
        """Огненный снаряд. Лучше, чем ничего.

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

    def Acid_Splash(self, spell_level):
        """Поражает две цели, если не сумеют уклониться.

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

    def Vicious_Mockery(self, spell_level):
        """Хитрое заклинание бардов, даёт помеху атаке врага.

        Level: Cantrip
        Casting time: 1 Action
        Range: 60 feet
        Components: V
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/vicious-mockery
        """
        spell_dict = {
                'direct_hit':True,
                'savethrow':True,
                'savethrow_all':True,
                'savethrow_ability':'wisdom',
                'attacks_number':1,
                'attack_range':60,
                'effect':'mockery',
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

    def Frostbite(self, spell_level):
        """Заклинание волшебников, даёт помеху атаке врага.

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

    def Sacred_Flame(self, spell_level):
        """Боевое заклинание жрецов.

        Level: Cantrip
        Casting time: 1 Action
        Range: 60 feet
        Components: V, S
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/sacred-flame
        """
        spell_dict = {
                'direct_hit':True,
                'savethrow':True,
                'savethrow_all':True,
                'savethrow_ability':'dexterity',
                'attacks_number':1,
                'attack_range':60,
                'effect':'ignore_cover',
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

    def Sword_Burst(self, spell_level):
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

    def Thunderclap(self, spell_level):
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

    def Word_of_Radiance(self, spell_level):
        """Чертовски эффективное заклинание жреца. Избирательная атака.

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

    def Create_Bonfire(self, spell_level):
        """Газовая горелка чародея.

        Level: Cantrip
        Casting time: 1 Action
        Range: 60 feet
        Components: V, S
        Duration: Concentration, up to 1 minute
        https://www.dnd-spells.com/spell/create-bonfire
        """
        # TODO: допиливай, нужна метка местности "bonfire"
        spell_dict = {
                'effect':'bonfire',
                'concentration':True,
                'direct_hit':True,
                'savethrow':True,
                'savethrow_all':True,
                'savethrow_ability':'dexterity',
                'attacks_number':1,
                'radius':5,
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

    def Ice_Knife_Piercing(self, spell_level):
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

    def Empyrean_Bolt(self, spell_level):
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

    def Healing_Word(self, spell_level):
        """Спасает жизни.

        Level: 1
        Casting time: 1 Bonus Action
        Range: 60 feet
        Components: V
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/healing-word
        """
        spell_dict = {
                'direct_hit':True,
                'attacks_number':1,
                'attack_range':60,
                'damage_type':'heal',
                'damage_dice':'1d4',
                'components':['verbal'],
                'casting_time':'action',
                'spell_level':spell_level,
                'damage_mod':0,
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

    def Bless(self, spell_level):
        """Отличный бонус к атаке и спасброскам.

        Level: 1
        Casting time: 1 Action
        Range: 30 feet
        Components: V, S, M (a sprinkling of holy water)
        Duration: Concentration, up to 1 minute
        """
        spell_dict = {
                'effect':'bless',
                'effect_timer':10,
                'concentration':True,
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

    def Cause_Fear(self, spell_level):
        """Защитный приём колдунов.

        Level: 1
        Casting time: 1 Action
        Range: 60 feet
        Components: V
        Duration: Concentration, up to 1 minute
        https://www.dnd-spells.com/spell/cause-fear
        """
        spell_dict = {
                'attacks_number':1,
                'attack_range':60,
                'effect':'fear',
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

    def Sleep(self, spell_level):
        """Защитный приём бардов и незлых чародеев.

        Level: 1
        Casting time: 1 Action
        Range: 90 feet
        Components: V, S, M (a pinch of fine sand, rose petals, or a cricket)
        Duration: 1 minute
        https://www.dnd-spells.com/spell/sleep
        """
        spell_dict = {
                'attacks_number':1,
                'attack_range':90,
                'effect':'sleep',
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

    def Entangle(self, spell_level):
        """Задерживает и опутывает цели в зоне 4x4.

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
                'effect':'entangle',
                'concentration':True,
                #'zone':True,
                #'zone_shape':'square',
                #'zone_danger':True,
                'direct_hit':True,
                'savethrow':True,
                'savethrow_all':True,
                'savethrow_ability':'strength',
                'attacks_number':10,
                'attack_range':90,
                # Зона квадратная:
                #'radius':20 / 2,
                'components':['verbal','somatic'],
                'casting_time':'action',
                'spell_level':spell_level,
                'spell_save_DC':8 + self.find_spell_attack_mod(),
                'spell_of_choice':'Entangle',
                }
        return spell_dict

    def Magic_Missile(self, spell_level):
        """Самонаводящееся оружие волшебника.

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

    def Burning_Hands(self, spell_level):
        """Огнемёт.

        Level: 1
        Casting time: 1 Action
        Range: Self (15-foot cone)
        Components: V, S
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/burning-hands
        """
        # TODO: Допили Burning_Hands. Это 15-футовый конус, то есть до 9 целей.
        # А у тебя сейчас квадрат 3x3 на дистанции 10 футов от мага.
        # Чтобы рисовать конусы используй shadowcasting.
        # TODO: во имя баланса зона уменьшена до 2x2 клетов.
        spell_dict = {
                'zone':True,
                'zone_shape':'2x2',
                #'zone_shape':'square',
                'direct_hit':True,
                'savethrow':True,
                'savethrow_ability':'dexterity',
                'attacks_number':1,
                'attack_range':15,
                'radius':5,
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

    def Shield(self, spell_level):
        """Отличная защита на один раунд.

        Level: 1
        Casting time: Special
        Range: Self
        Components: V, S
        Duration: 1 round
        https://www.dnd-spells.com/spell/shield
        """
        spell_dict = {
                'effect':'shield',
                'attack_range':'self',
                'components':['verbal','somatic'],
                'casting_time':'reaction',
                'spell_level':spell_level,
                'spell_of_choice':'Magic_Missile',
                }
        return spell_dict

    def Absorb_Elements(self, spell_level):
        """Сопротивляемость одиночному удару огнешара.

        Level: 1
        Casting time: Special
        Range: Self
        Components: S
        Duration: 1 round
        https://www.dnd-spells.com/spell/absorb-elements
        """
        # 1d6 урона поглощённого типа можно направить атакой оружием в следующем раунде.
        spell_dict = {
                'effect':'absorb',
                'attack_range':'self',
                'absorb_damage_type':['acid','cold','fire','lightning','thunder'],
                'damage_type':'absorbed',
                'damage_dice':'1d6',
                'components':['somatic'],
                'casting_time':'reaction',
                'spell_level':spell_level,
                'spell_of_choice':'Magic_Missile',
                }
        if int(spell_level[0]) > 1:
            dice = int(spell_dict['damage_dice'][0])
            dice += int(spell_level[0]) - 1
            spell_dict['damage_dice'] = str(dice) + spell_dict['damage_dice'][1:]
        return spell_dict

    def Mage_Armor(self, spell_level):
        """Замена лёгкой брони, притом отменная.

        Level: 1
        Casting time: 1 Action
        Range: Touch
        Components: V, S, M
        Duration: 8 hours
        https://www.dnd-spells.com/spell/mage-armor
        """
        # TODO: броня берётся из metadict_item.
        spell_dict = {
                'armor':True,
                'armor_type':'Force',
                'armor_class_armor':13,
                'attack_range':'self',
                'components':['verbal','somatic','material'],
                'casting_time':'action',
                'spell_level':spell_level,
                'spell_of_choice':'Magic_Missile',
                }
        return spell_dict

    def Ice_Knife(self, spell_level):
        """Льдинки отлично работают по плотному строю.

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

    def Hail_of_Thorns(self, spell_level):
        """Превращает рейнджера в гранатомёт.

        Level: 1
        Casting time: 1 Bonus Action
        Range: Self
        Components: V
        Duration: Concentration, up to 1 minute
        https://www.dnd-spells.com/spell/hail-of-thorns
        """
        spell_dict = {
                'effect':'thorns',
                #'zone':True,
                'zone_shape':'square',
                'concentration':True,
                'direct_hit':True,
                'savethrow':True,
                'savethrow_ability':'dexterity',
                'attacks_number':1,
                'attack_range':600,
                'radius':5,
                'damage_type':'piercing',
                'damage_dice':'1d10',
                'components':['verbal'],
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

    def Arms_of_Hadar(self, spell_level):
        """Ранит и лишает врага реакции.

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

#----
# 2 lvl

    def Scorching_Ray(self, spell_level):
        """Бесполезное заклинание. Даже самонаведения нет!

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

    def Melfs_Acid_Arrow(self, spell_level):
        """Так себе. Одиночная цель.

        Level: 2
        Casting time: 1 Action
        Range: 90 feet
        Components: V, S, M (powdered rhubarb leaf and an adder’s stomach)
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/melfs-acid-arrow
        """
        # TODO: 2d4 урона в следующий раунд.
        spell_dict = {
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

    def Moonbeam(self, spell_level):
        """Орбитальный лазер. Работает только ночью и на открытой местности.

        Level: 2
        Casting time: 1 Action
        Range: 120 feet
        Components: V, S, M (several seeds of any moonseed plant and a piece of opalescent feldspar)
        https://www.dnd-spells.com/spell/moonbeam
        """
        spell_dict = {
                'effect':'moonbeam',
                'concentration':True,
                'zone':True,
                'zone_shape':'2x2',
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

    def Blur(self, spell_level):
        """Размытый образ, помеха атаке врагов.

        Level: 2
        Casting time: 1 Action
        Range: Self
        Components: V
        Duration: Concentration, up to 1 minute
        https://www.dnd-spells.com/spell/blur
        """
        spell_dict = {
                'blur':True,
                'attack_range':'self',
                'components':['verbal'],
                'casting_time':'action',
                'spell_level':spell_level,
                'spell_of_choice':'Magic_Missile',
                }
        return spell_dict

    def Shatter(self, spell_level):
        """Взрыв. Поражающих элементов нет, но контузит отлично.

        Level: 2
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

#----
# 3 lvl

    def Fear(self, spell_level):
        """Защитный приём колдунов.

        Level: 3
        Casting time: 1 Action
        Range: Self (30-foot cone)
        Components: V, S, M (a white feather or the heart of a hen)
        Duration: Concentration, up to 1 minute 
        https://www.dnd-spells.com/spell/fear
        """
        # TODO: это атака конусом, а у нас просто выбор 30 целей.
        spell_dict = {
                'attacks_number':30,
                'attack_range':30,
                'effect':'fear',
                'direct_hit':True,
                'savethrow':True,
                'savethrow_all':True,
                'savethrow_ability':'wisdom',
                'components':['verbal'],
                'casting_time':'action',
                'spell_level':spell_level,
                'spell_save_DC':8 + self.find_spell_attack_mod(),
                'spell_of_choice':'Fear',
                }
        return spell_dict

    def Call_Lightning(self, spell_level):
        """Призыв грозовой тучи, молнии с небес.

        Level: 3
        Casting time: 1 Action
        Range: 120 feet
        Components: V, S
        Duration: Concentration, up to 10 minutes
        https://www.dnd-spells.com/spell/call-lightning
        """
        # TODO: зона поражения 2x2 клетки, а не 3x3.
        # Потому что молния поражает цели в пределах 5 футов от точки.
        spell_dict = {
                'effect':'call_lightning',
                'concentration':True,
                'zone':True,
                'zone_shape':'2x2',
                'zone_danger':True,
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

    def Fireball(self, spell_level):
        """Чудовищное оружие. Один удар, один взвод.

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

    def Counterspell(self, spell_level):
        """Защита от огнешаров

        Level: 3
        Casting time: Special
        Range: 60 feet
        Components: S
        Duration: Instantaneous
        https://www.dnd-spells.com/spell/counterspell
        """
        # Нет ограничения по дальности.
        spell_dict = {
                'effect':'counterspell',
                'attack_range':'self',
                'components':['somatic'],
                'casting_time':'reaction',
                'spell_level':spell_level,
                'spell_of_choice':'Magic_Missile',
                }
        return spell_dict
