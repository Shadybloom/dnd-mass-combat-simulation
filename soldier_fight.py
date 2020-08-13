#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from soldier_base import *
from data import traumas

#-------------------------------------------------------------------------
# Функции:

def find_dice_medial(dice):
    """Средний бросок кости в формате навроде 1d6, 2d6, 1d12.
    
    """
    dice_list = dice.split('d')
    medial_number = math.floor(int(dice_list[0]) * (int(dice_list[1]) / 2))
    return medial_number

#-------------------------------------------------------------------------
# Классы:

class soldier_in_battle(soldier):
    """Описание класса.
    
    Действия и реакции для солдат. Изменяемые параметры.
    """
    # Диапазон критической атаки (стандартный)
    crit_range = 20
    crit_multiplier = 2
    loss_range = 1
    # На 5 уровне бойцы получают дополнительную атаку.
    attacks_number = 1
    # Размер тайла -- 5 футов (1.5 метра):
    tile_size = 5
    dict_danger = {
            'commander':3,
            'elite_warrior':2,
            'warrior':1,
            'archer':1,
            'mount':1,
            }
    # Опыт от показателя опасности:
    challenge_rating_experience_dict = {
            '-':0,
            '0':10,
            '1/8':25,
            '1/4':50,
            '1/2':100,
            '1':200,
            '2':450,
            '3':700,
            '4':1100,
            '5':1800,
            '6':2300,
            '7':2900,
            '8':3900,
            '9':5000,
            '10':5900,
            '11':7200,
            '12':8400,
            '13':10000,
            '14':11500,
            '15':13000,
            '16':15000,
            '17':18000,
            '18':20000,
            '19':22000,
            '20':25000,
            '21':33000,
            '22':41000,
            '23':50000,
            '24':62000,
            '25':75000,
            '26':90000,
            '27':105000,
            '28':120000,
            '29':135000,
            '30':155000,
            }

    def set_hitpoints(self, damage = None, heal = None, bonus_hitpoints = None):
        """Контроль хитпоинтов в начале и в ходе боя.
        
        Варианты:
        - Боец получает урон/лечение (или отдых).
        - Боец ранен в прошлом бою (берётся из БД)
        - Боец воодушевлён командиром (Feat_Inspiring_Leader)
        - Боец начинает бой со своим нормальным максимумом хитов.
        """
        # Если хитпоинты не указаны, значит персонаж совсем зелёный и у него максимум хитов.
        if not hasattr(self, 'hitpoints'):
            self.hitpoints = self.hitpoints_max
            self.bonus_hitpoints = 0
        if not hasattr(self, 'hitpoints_heal'):
            self.hitpoints_heal = 0
        if damage:
            self.hitpoints -= damage
        if heal:
            hitpoints_damage = self.hitpoints_max - self.hitpoints
            if heal > hitpoints_damage:
                heal = hitpoints_damage
            self.hitpoints += heal
            self.hitpoints_heal += heal
        if bonus_hitpoints:
            self.bonus_hitpoints = bonus_hitpoints
        return self.hitpoints

    def set_short_rest_rearm(self):
        """Солдаты обновляют вооружение, боекомплект.

        - Берётся экипировка из шаблона.
        - Пересчитывается вес снаряжения.
        - Восстананавливается список атак (стрелы/дротики могли кончиться)
        - Восстанавливается защита (щиты могли поломать пилумами)
        """
        self.equipment_weapon = copy.deepcopy(self.metadict_chars[self.rank]['equipment_weapon'])
        self.overload = self.calculate_overload()
        self.base_speed = self.overload['base_speed']
        self.armor = self.takeoff_armor()
        self.armor.update(self.get_armor())
        self.attacks = self.takeoff_weapon()
        self.attacks.update(self.get_weapon())
        self.attacks.update(self.modify_attacks())
        self.attacks.update(self.modify_attacks_weapon_of_choice())
        pass

    def set_short_rest_heal(self):
        """Короткий отдых (1 час). Позволяет подлечиться.

        - Раненые лечатся на "hit_dice + constitution_mod"
        https://www.dandwiki.com/wiki/5e_SRD:Short_Rest
        """
        # Лечение за счёт использования кости хитов:
        for n in enumerate(range(0, self.level)):
            if self.hitpoints < self.hitpoints_max and self.hit_dices_use < self.level:
                rest_heal = dices.dice_throw_advantage(self.hit_dice) + self.mods['constitution']
                self.set_hitpoints(heal = rest_heal)
                self.hit_dices_use += 1

    def set_short_rest_restoration(self):
        """Короткий отдых (1 час). Восстанавливает способности.

        https://www.dandwiki.com/wiki/5e_SRD:Short_Rest
        """
        # TODO: допиливай, здесь много всего.
            # - Концентрация прерывается.
            # - Эффекты заклинаний прекращаются.
        # Восстанавливаются после короткого отдыха (short_rest):
        if self.class_features.get('Second_Wind'):
            self.second_wind = True
        if self.class_features.get('Action_Surge'):
            self.action_surge = True
        if self.class_features.get('Feat_Inspiring_Leader'):
            self.inspiring_leader = True
        if self.proficiency.get('ki_points_max'):
            self.ki_points = self.proficiency['ki_points_max']
        if self.class_features.get('Martial_Archetype_Battlemaster'):
            self.superiority_dices = self.proficiency['superiority_dices']
        # Восстанавливаются заклинания колдуна:
        if self.char_class == 'Warlock':
            self.spells_generator = spells.gen_spells(self)
            self.spellslots = self.spells_generator.spellslots
            self.spells = self.spells_generator.spells
        # После отдыха можно повторить перевязку.
        self.treated = False

    def set_actions_base(self, squad):
        """Расставляем переменные, используемые в бою.
        
        До начала боя, если боец со свежими силами.
        """
        # Отменяем подготовленное действие:
        self.ready_action = False
        # Даём боевые действия и пул движения:
        self.battle_action = True
        self.bonus_action = True
        self.reaction = True
        self.move_action = True
        self.move_pool = self.base_speed
        if hasattr(self, 'help_action') and self.help_action: 
            self.help_action = False
        # Индивидуальные команды солдату:
        self.commands = []
        # Благотворные и вредные эффекты:
        self.buffs = {}
        self.debuffs = {}
        # Общие для всех параметры:
        self.immunity = []
        self.resistance = []
        self.vultenability = []
        self.defeat = False
        self.escape = False
        self.prone = False
        self.poisoned = False
        self.stunned = False
        self.paralyzed = False
        self.grappled = False
        self.restained = False
        self.concentration = False
        self.help_action = False
        self.killer_mark = False
        # Долговременные параметры:
        self.petrified = False
        # Эффекты заклинаний:
        self.fear = False
        self.fear_source = None
        self.sleep = False
        self.damage_absorbed = None
        self.guiding_bolt_hit = False
        self.mockery_hit = False
        self.hex = False
        # Способности бойца, паладина:
        self.action_surge = False
        self.shield = False
        # Словарь ранений (disabled)
        if not hasattr(self, 'trophy_items_dict'):
            self.traumas_dict = {}
        # Словарь трофеев:
        if not hasattr(self, 'trophy_items_dict'):
            self.trophy_items_dict = {}
        # Словарь израсходованного снаряжения:
        if not hasattr(self, 'drop_items_dict'):
            self.drop_items_dict = {}
        # Оружие в руках:
        if not hasattr(self, 'weapon_ready'):
            self.weapon_ready = None
        # Щит в боевое положение:
        if not hasattr(self, 'shield_ready'):
            if self.armor['shield_use']:
                self.shield_ready = True
            else:
                self.shield_ready = False
        # Правим изменившиеся параметры в человеческой форме друида:
        if self.__dict__.get('wild_shape_old_form'):
            self.wild_shape_old_form['ally_side'] = self.ally_side
            self.wild_shape_old_form['enemy_side'] = self.enemy_side
            self.wild_shape_old_form['initiative'] = self.initiative
            self.wild_shape_old_form['place'] = self.place
            self.wild_shape_old_form['place_in_order'] = self.place_in_order
        if not hasattr(self, 'recharge'):
            self.recharge_dict = None
        if not hasattr(self, 'wild_shape'):
            self.wild_shape = False
        if not hasattr(self, 'water_walk'):
            self.water_walk = False
        if not hasattr(self, 'air_walk'):
            self.air_walk = False
        if not hasattr(self, 'wild_shape_old_form'):
            self.wild_shape_old_form = None
        if not hasattr(self, 'arcane_ward'):
            self.arcane_ward = False
        if not hasattr(self, 'mage_armor'):
            self.mage_armor = False
        if not hasattr(self, 'heroism'):
            self.heroism = False
        if not hasattr(self, 'blur'):
            self.blur = False
        if not hasattr(self, 'sacred_weapon'):
            self.sacred_weapon = False
        if not hasattr(self, 'destructive_wrath'):
            self.destructive_wrath = False
        # Павшие, покалеченые, захваченые в плен:
        if not hasattr(self, 'fall'):
            self.fall = False
        if not hasattr(self, 'death'):
            self.death = False
        if not hasattr(self, 'disabled'):
            self.disabled = False
        if not hasattr(self, 'trauma_damage_type'):
            self.trauma_damage_type = None
        if not hasattr(self, 'captured'):
            self.captured = False
        # Опыт и трофеи бойца:
        if not hasattr(self, 'experience'):
            self.experience = 0
        # Статистика побед и поражений бойца:
        if not hasattr(self, 'victories'):
            self.victories = 0
        if not hasattr(self, 'victories_dict'):
            self.victories_dict = {}
        if not hasattr(self, 'defeats'):
            self.defeats = 0
        # В составе отряда могут быть "мёртвые души":
        if not hasattr(self, 'death') or not hasattr(self, 'stable'):
            self.death = False
            self.stable = False
        # Бонусные хиты от Feat_Inspiring_Leader:
        if not hasattr(self, 'bonus_hitpoints'):
            self.bonus_hitpoints = 0
        # Использованные для лечения на отдыхе кости хитов:
        if not hasattr(self, 'hit_dices_use'):
            self.hit_dices_use = 0
        # Перевязка от лекаря с Feat_Healer:
        if not hasattr(self, 'treated'):
            self.treated = False
        # Учитываем доступные приёмы:
        if self.class_features:
            if self.class_features.get('Extra_Attack'):
                self.attacks_number = 2
                if type(self.class_features['Extra_Attack']) == int:
                    self.attacks_number = 1 + self.class_features['Extra_Attack']
                elif self.proficiency.get('Extra_Attack'):
                    self.attacks_number = 1 + self.proficiency['Extra_Attack']
            if self.class_features.get('Champion_Improved_Critical'):
                self.crit_range = 19
            if self.class_features.get('Brutal_Critical') and not self.crit_multiplier > 2:
                self.crit_multiplier += self.proficiency['brutal_critical']
            # Восстанавливаются после короткого отдыха (short_rest):
            if self.class_features.get('Second_Wind') and not hasattr(self, 'second_wind'):
                self.second_wind = True
            if self.class_features.get('Action_Surge') and not hasattr(self, 'action_surge'):
                self.action_surge = True
            if self.class_features.get('Martial_Archetype_Battlemaster')\
                    and not hasattr(self, 'superiority_dices'):
                self.superiority_dice = self.proficiency['superiority_dice']
                self.superiority_dices = self.proficiency['superiority_dices']
            if self.class_features.get('Feat_Inspiring_Leader') and not hasattr(self, 'inspiring_leader'):
                self.inspiring_leader = True
            if self.proficiency.get('ki_points_max') and not hasattr(self, 'ki_points'):
                self.ki_points = self.proficiency['ki_points_max']
            if self.proficiency.get('wild_shape') and not hasattr(self, 'wild_shape_number'):
                self.wild_shape_number = self.proficiency['wild_shape']
            # Восстанавливаются после долгого отдыха (long_rest):
            if self.class_features.get('Lay_on_Hands') and not hasattr(self, 'lay_on_hands'):
                self.lay_on_hands = self.level * 5
            if self.class_features.get('Bardic_Inspiration') and not hasattr(self, 'inspiring_bard_number'):
                self.inspiring_bard_number = self.mods['charisma']
                self.inspiring_bard_dice = self.proficiency['bardic_inspiration']
            if self.proficiency.get('rages_max') and not hasattr(self, 'rages'):
                self.rages = self.proficiency['rages_max']
            if self.class_features.get('Rage'):
                self.rage_timer = 0
            if self.class_features.get('Font_of_Magic') and not hasattr(self, 'sorcery_points'):
                self.sorcery_points = self.proficiency.get('sorcery_points',0)
            if self.class_features.get('Warding_Flare') and not hasattr(self, 'warding_flare'):
                self.warding_flare = self.mods['wisdom']
            if self.class_features.get('War_Priest') and not hasattr(self, 'war_priest'):
                self.war_priest = self.mods['wisdom']
            if self.proficiency.get('channel_divinity') and not hasattr(self, 'channel_divinity'):
                self.channel_divinity = self.proficiency['channel_divinity']
            if self.class_features.get('Ink_Cloud') and not hasattr(self, 'ink_cloud'):
                self.ink_cloud = True
                self.ink_cloud_radius = 20
            # Иммунитет:
            if self.class_features.get('immunity'):
                self.immunity.extend(self.class_features.get('immunity',[]))
            # Сопротивляемость:
            if self.class_features.get('resistance'):
                self.resistance.extend(self.class_features.get('resistance',[]))
            # Уязвимости:
            if self.class_features.get('vultenability'):
                self.vultenability.extend(self.class_features.get('vultenability',[]))
        # Используем доступные приёмы:
        if self.class_features:
            # Font_of_Magic даёт 2 sorcery_points на 2 lvl чародея, можно вложить в лишний слот 1 lvl.
            if self.class_features.get('Font_of_Magic_Spellslot_1_lvl'):
                if self.proficiency.get('sorcery_points',0) >= 2:
                    if self.spellslots.get('1_lvl'):
                        self.spellslots['1_lvl'] += 1
                        self.sorcery_points -= 2
                    else:
                        self.spellslots['1_lvl'] = 1
                        self.sorcery_points -= 2
            # Shadow_Arts позволяет монаху-теневику колдовать за счёт Ки:
            if self.class_features.get('Shadow_Arts') and self.spells:
                if self.ki_points >= 2 and not self.spellslots.get('2_lvl'):
                    self.spellslots['2_lvl'] = 1
                    self.ki_points -= 2
        # Используем заклинания перед боем:
        # TODO: перенеси это в set_squad_buffs
        if hasattr(self, 'spells'):
            for spell, spell_dict in self.spells.items():
                if spell_dict.get('armor') and not self.armor['armor_use']:
                    self.spells_generator.use_spell(spell)
                    self.equipment_weapon['Mage_Armor'] = 1
                    self.armor.update(self.get_armor())
                    self.mage_armor = True
                    if self.class_features.get('Arcane_Ward') and not self.bonus_hitpoints:
                        self.bonus_hitpoints = self.level * 2 + self.mods['intelligence']
                        self.arcane_ward = True

    def set_actions(self, squad):
        """Доступные действия в 6-секундном раунде боя.
        
        Обновляются в начале каждого раунда:
        https://www.dandwiki.com/wiki/5e_SRD:Combat_Turn
        Move, Action (Ready Action), Bonus Action, Reaction
        """
        # Отменяем подготовленное действие:
        self.ready_action = False
        # Индивидуальные команды обновляются каждый ход:
        self.commands = []
        # Боец может оказаться в бою раненым:
        if self.hitpoints <= 0:
            self.fall = True
        else:
            self.fall = False
        # Даём боевые действия и пул движения:
        if not self.stunned and not self.paralyzed and not self.sleep:
            self.battle_action = True
            self.bonus_action = True
            self.reaction = True
            self.move_action = True
            self.move_pool = self.base_speed
            if  self.equipment_weapon.get('Infusion of Longstrider'):
                self.move_pool +10
            if self.help_action:
                self.help_action = False
                self.battle_action = False
        # Отключаем манёвры пршлого хода, работавшие за счёт battle_action
        self.disengage_action = False # это защита от провоцированных атак.
        self.dash_action = False # это ускорение до x2 скорости
        self.dodge_action = False # это disadvantage на атаки врагов и преимущество ловксоти
        # Тактика варвара, преимущество и себе, и врагам:
        self.reckless_attack = False
        # Заклинание "Shield" волшебника:
        self.shield = False
        # Щит возвращается в боевое положение (если в прошлом ходу использовалось двуручное оружие):
        if self.armor['shield_use'] and not self.shield_ready:
            self.set_shield()
        # Испуганный бросает спасброски против страха:
        if self.fear:
            self.fear = self.set_fear(self.fear_source, self.fear_difficult)
            if self.fear:
                print('{side_1} {c1} {s} FEAR {fear}'.format(
                    side_1 = self.ally_side,
                    c1 = self.place,
                    s = self.behavior,
                    fear = self.fear
                    ))
        # Отравленный отходит от яда (делая спасброски):
        if self.poisoned:
            if self.get_savethrow(self.poison_difficult, 'constitution'):
                self.poisoned = False
                self.poison_difficult = None
            elif self.poison_timer > 0:
                self.poison_timer -= 1
            elif self.poison_timer == 0:
                self.poisoned = False
                self.poison_difficult = None
        # Ошеломлённый пытается очухаться:
        if self.stunned:
            if self.stunned_timer > 0:
                self.stunned_timer -= 1
            elif self.stunned_timer == 0:
                self.stunned = False
                self.stunned_difficult = None
        # Парализованный сопротивляется:
        if self.paralyzed:
            if self.get_savethrow(self.paralyzed_difficult, 'constitution'):
                self.paralyzed = False
                self.paralyzed_timer = None
                self.paralyzed_difficult = None
            elif self.paralyzed_timer > 0:
                self.paralyzed_timer -= 1
            elif self.paralyzed_timer == 0:
                self.paralyzed = False
                self.paralyzed_difficult = None
        # Схваченный не может двигаться (но пытается вырваться):
        elif self.grappled or self.restained:
            self.move_action = False
            self.move_pool = 0
            if self.grappled:
                self.set_grapple_break()
            elif self.restained:
                self.set_restained_break()
        # Упавший встаёт на ноги (если он не схвачен):
        elif self.prone == True and not self.grappled:
            self.move_pool = self.move_pool / 2
            self.prone = False
        # Даём всадникам скорость их коней (но только если они в одной точке):
        if hasattr(self, 'mount_uuid') and self.mount_uuid in squad.metadict_soldiers:
            mount = squad.metadict_soldiers[self.mount_uuid]
            if hasattr(mount, 'place') and mount.place == self.place:
                # TODO: дай коняшкам нормальный dash_action.
                # Кони используют dash_action, поэтому удваиваем скорость:
                self.move_pool = mount.base_speed * 2
        # Забираем у лошадок право свободно бегать, пока ими управляет всадник:
        if hasattr(self, 'master_uuid') and self.master_uuid in squad.metadict_soldiers:
            master = squad.metadict_soldiers[self.master_uuid]
            if hasattr(self, 'place') and self.place == master.place:
                self.move_pool = 0
                # По правилами DnD 5 управляемое ездовое животное не может атаковать:
                self.battle_action = False
                self.dodge_action = True
        # Убираем окружение:
        self.danger = 0
        self.near_zone = [ ]
        self.near_allies = [ ]
        self.near_enemies = [ ]
        # Возвращение друида в обычную форму, если не осталось бонусных хитов:
        if self.wild_shape and self.bonus_hitpoints <= 0:
            self.return_old_form()
        # Бесстрашные бойцы бесстрашны:
        if self.__dict__.get('fearless_AI')\
                or self.__dict__.get('heroism'):
            self.fearless = True
            self.commands.append('fearless')
        # Используем предметы перед боем:
        # TODO: получается, что будут использоваться каждый раунд, если их несколько.
        if hasattr(squad, 'commands') and 'potions' in squad.commands:
            if not self.bonus_hitpoints:
                if self.equipment_weapon.get('Infusion of Heroism')\
                        or self.equipment_weapon.get('Potion of Bravery'):
                    self.use_potion_of_heroism()
        # Особенности монстров:
        # Перезарядка способности:
        if self.class_features.get('Recharge') and self.recharge_dict:
            recharge_throw = dices.dice_throw(self.class_features['Recharge_dice'])
            if recharge_throw in self.class_features['Recharge_numbers']:
                attack_choice = self.recharge_dict['recharge']
                self.attacks[attack_choice] = self.recharge_dict
                self.recharge_dict = None
        # Регенерация троллей и демонов:
        if self.class_features.get('Regeneration')\
                and self.hitpoints < self.hitpoints_max:
            self.set_hitpoints(heal = self.class_features['Regeneration'])
        # TODO: упрости проверку до if self.rage:
        # Работа способностей, ограниченных по времени:
        if self.class_features.get('Rage'):
            if self.rage_timer > 0:
                self.rage_timer -= 1
            elif self.rage_timer == 0:
                self.rage_damage = 0
                self.resistance = []
                self.frenzy = False
                self.rage = False
        if self.heroism:
            if self.heroism_timer > 0:
                self.heroism_timer -= 1
                if self.bonus_hitpoints < self.level:
                    self.bonus_hitpoints = self.level
            elif self.heroism_timer == 0:
                self.heroism = None
        # Сброс заклинаний:
        # TODO: это лишнее. Делай через buffs.
        self.blur = False
        # Универсальный таймер концентрации.
        if self.concentration:
            if self.concentration['concentration_timer'] == 0:
                self.set_concentration_break(autofail = True)
            elif self.concentration['concentration_timer'] > 0:
                self.concentration['concentration_timer'] -= 1
                spell_dict = self.concentration
                if spell_dict.get('effect') == 'blur':
                    self.blur = True
        # TODO: Потихоньку переделывай функции:
        # Channel_Sacred_Weapon
        if self.sacred_weapon:
            if self.sacred_weapon_timer > 0:
                self.sacred_weapon_timer -= 1
            elif self.sacred_weapon_timer == 0:
                self.sacred_weapon = None

    def set_change_form(self):
        """Друид меняет форму
        
        """
        if self.class_features.get('Wild_Shape_Form')\
                and self.class_features['Wild_Shape_Form'] in self.metadict_animals\
                and not self.wild_shape:
            if self.battle_action or self.bonus_action and self.class_features.get('Combat_Wild_Shape'):
                if self.class_features.get('Combat_Wild_Shape'):
                    self.bonus_action = False
                else:
                    self.battle_action = False
                # Сохраняем старую форму, чтобы восстановить:
                animal_type = self.class_features['Wild_Shape_Form']
                self.wild_shape_old_form = copy.deepcopy(self.__dict__)
                # Меняем форму:
                self.rank = animal_type
                self.__dict__.update(copy.deepcopy(self.metadict_animals[animal_type]))
                self.body = self.gen_height_and_weight()
                self.size = self.body['size']
                self.proficiency = self.find_class_proficiency()
                self.proficiency_bonus = self.proficiency['proficiency_bonus']
                self.overload = self.calculate_overload()
                self.base_speed = self.overload['base_speed']
                self.mods = self.calculate_mods()
                self.saves = self.calculate_saves()
                self.armor = self.takeoff_armor()
                self.armor.update(self.get_armor())
                self.attacks = self.takeoff_weapon()
                self.attacks.update(self.get_weapon())
                self.attacks.update(self.modify_attacks())
                self.attacks.update(self.modify_attacks_weapon_of_choice())
                # Хиты изменённой формы, это бонусные хиты:
                self.bonus_hitpoints = self.calculate_hitpoints()
                self.behavior = self.wild_shape_old_form['behavior']
                self.wild_shape = True
                self.wild_shape_number -= 1

    def return_old_form(self):
        """Друид возвращает облик человека.
        
        """
        self.wild_shape = False
        self.wild_shape_old_form['hitpoints'] = self.hitpoints
        self.__dict__.update(copy.deepcopy(self.wild_shape_old_form))

    def set_rage(self):
        """Варвар злится.
        
        Что это даёт:
        - Сопротивляемость к урону обычного оружия.
        - Дополнительный урон, что зависит от уровня варвара.

        Ярость длится минуту (10 раундов), и только пока варвар атакует врага:
        https://www.dandwiki.com/wiki/5e_SRD:Barbarian#Rage
        https://www.dandwiki.com/wiki/5e_SRD:Damage_Resistance
        """
        if self.class_features.get('Rage'):
            if self.rages > 0 and self.rage_timer == 0 and self.bonus_action:
                self.rage = True
                self.bonus_action = False
                self.resistance.append('slashing')
                self.resistance.append('piercing')
                self.resistance.append('bludgeoning')
                self.rage_damage = self.proficiency['rage_damage']
                self.rage_timer = 10
                self.rages -= 1

    def try_spellcast(self, spell_name):
        """Маг кастует заклинание, если это возможно.
        
        Сначала поиск по названиям заклинаний, затем по их эффектам.
        Возвращает словарь заклинание. Он же в кидается в self.concentration
        """
        spell_choice = None
        if spell_name in self.spells:
            spell_choice = spell_name
        if not spell_choice:
            spell_choice = self.spells_generator.find_spell(spell_name)
            if not spell_choice:
                spell_effect = spell_name
                spell_choice = self.spells_generator.find_spell(spell_effect, effect = True)
        if spell_choice:
            action = self.check_action_to_spellcast(self.spells[spell_choice])
            if self.__dict__.get(action):
                spell_dict = self.spells_generator.use_spell(spell_choice)
                spell_dict['spell_choice'] = spell_choice
                self.use_action_to_spellcast(spell_dict)
                self.set_concentration(spell_dict)
                return spell_dict
            else:
                return False
        else:
            return False

    def check_action_to_spellcast(self, spell_dict):
        """Заклинание требует действия. Какого именно?

        """
        actions_list = ['battle_action', 'bonus_action', 'reaction']
        if spell_dict.get('casting_time') in actions_list:
            return spell_dict['casting_time']
        elif spell_dict.get('casting_time') == 'action':
            return 'battle_action'
        else:
            return False

    def use_action_to_spellcast(self, spell_dict):
        """Каст заклинания тратит действие.
        
        - Действие
        - Бонусное действие
        - Реакция
        """
        if spell_dict.get('casting_time'):
            casting_time = spell_dict['casting_time']
            if casting_time == 'action':
                self.battle_action = False
            elif casting_time == 'bonus_action':
                self.bonus_action = False
            elif casting_time == 'reaction':
                self.reaction = False
            else:
                self.battle_action = False
        else:
            self.battle_action = False

    def set_concentration(self, spell_dict):
        """Концентрация на заклинании"""
        if spell_dict.get('concentration'):
            self.concentration = spell_dict
            if spell_dict.get('concentration_timer'):
                pass
            elif spell_dict.get('effect_timer'):
                spell_dict['concentration_timer'] = spell_dict['effect_timer']
            else:
                # Даём минуту концентрации, если время не указано:
                spell_dict['concentration_timer'] = 10
            return True
        else:
            return False

    def use_spell_ammo(self, spell_dict):
        """Расходуется боекомплект заклинания.

        Например:
        - Melf_Minute_Meteors даёт 6 метеоров

        Концентрация прерывается, если закончился боекомплект.
        """
        if spell_dict.get('ammo') > 0:
            spell_dict['ammo'] -=1
            return True
        if spell_dict.get('ammo') <= 0:
            if self.concentration\
                    and self.concentration.get('spell_choice')\
                    and spell_dict.get('spell_choice') == self.concentration['spell_choice']\
                    and not spell_dict.get('concentration_no_ammo'):
                self.set_concentration_break(autofail = True)
            return False

    def set_concentration_break(self, difficult = 10,
            advantage = False, disadvantage = False, autofail = False):
        """Бойцу пытаются сбить концентрацию.

        - Спасбросок телосложения СЛ 10 или половина от урона.
        - Недееспособность тоже лишает концентрации.

        Здесь указана сама сложность спасброска, а не урон.
        """
        ability = 'constitution'
        if difficult < 10:
            difficult = 10
        if self.get_savethrow(difficult, ability, advantage, disadvantage) and not autofail:
            return False
        else:
            # Этот тег используется, чтобы снимать баффы с солдат.
            self.concentration['concentration_break'] = True
            self.concentration = False
            return True

    def set_buff(self, spell_dict):
        """Солдат получает эффект заклинания.
        
        """
        effect = spell_dict['effect']
        if effect not in self.buffs:
            self.buffs[effect] = spell_dict
            return True
        else:
            self.buffs[effect] = spell_dict
            return True

    def set_frenzy(self, attack_choice):
        """Берсерк бесится.
        
        Что это даёт:
        - Бонусная атака каждый раунд ценой истощения после ярости.
        https://www.dandwiki.com/wiki/5e_SRD:Barbarian#Path_of_the_Berserker
        """
        attacks_chain_bonus = []
        if self.class_features.get('Berserker_Frenzy'):
            if not self.frenzy and self.rage_timer > 0 and self.bonus_action:
                self.frenzy = True
                self.bonus_action = False
            elif self.frenzy and self.bonus_action:
                self.bonus_action = False
                attacks_chain_bonus.append(attack_choice)
        return attacks_chain_bonus

    def set_patient_defence(self):
        """Защитные приёмы монахов.
        
        Homebrew: Dodge_Action без расхода Ки, подобно cunning_action вора.
        В оригинале: Dodge_Action бонусным действием за счёт Ки, чего хватает только на 2 раунда.
        """
        if self.class_features.get('Patient_Defense'):
            #if hasattr(self, 'ki_points') and self.ki_points > 0 and self.bonus_action == True:
            #    self.ki_points -= 1
            #    self.bonus_action = False
            #    self.dodge_action = True
            if self.bonus_action == True:
                self.bonus_action = False
                self.dodge_action = True
                return True

    def set_step_of_the_wind_disengage(self):
        """Уклонение монаха."""
        if self.class_features.get('Step_of_the_Wind'):
            #if hasattr(self, 'ki_points') and self.ki_points > 0 and self.bonus_action == True:
            #    self.ki_points -= 1
            #    self.bonus_action = False
            #    self.disengage_action = True
            if self.bonus_action == True:
                self.bonus_action = False
                self.disengage_action = True
                return True

    def set_cunning_action_defence(self):
        """Защитные приёмы вора."""
        if self.class_features.get('Cunning_Action'):
            if self.bonus_action == True:
                self.bonus_action = False
                self.dodge_action = True
                return True

    def set_cunning_action_disengage(self):
        """Уклонение вора."""
        if self.class_features.get('Cunning_Action'):
            if self.bonus_action == True:
                self.bonus_action = False
                self.disengage_action = True
                return True

    def set_cunning_action_dash(self):
        """Ускорение вора."""
        if self.class_features.get('Cunning_Action'):
            if self.bonus_action == True:
                self.bonus_action = False
                self.dash_action = True
                return True

    def set_two_weapon_fighting(self, attack_choice):
        """Атака вторым оружием за счёт бонусного действия.
        
        - Если боец держал щит, то он его отбрасывает, чтобы атаковать вторым оружием.
        - Навык Fighting_Style_Two_Weapon_Fighting добавляет модификаторы урона к второму оружию.
        """
        attacks_chain_bonus = []
        if self.class_features.get('Fighting_Style_Two_Weapon_Fighting')\
                and not 'two_handed' in self.attacks[attack_choice]['weapon_type']\
                and self.bonus_action == True:
            attack_list_slice = [key for key in self.attacks\
                    if 'Fighting_Style_Two_Weapon_Fighting' in self.attacks[key]['weapon_skills_use']\
                    and attack_choice[0] in self.attacks[key]['weapon_type']]
            if attack_list_slice:
                self.unset_shield()
                self.bonus_action = False
                attacks_chain_bonus.append(attack_list_slice[-1])
        return attacks_chain_bonus

    def set_martial_arts(self):
        """Боевые приёмы монахов.
        
        Flurry_of_Blows делает монаха крайне опасным бойцом ближнего боя.
        Homebrew. Монах может использовать сбивание/хватание/разоружение вместо любой атаки.
        Три атаки. Первой/второй сбивает с ног, третьей хватает. И всё, враг небоеспособен.
        https://www.dandwiki.com/wiki/5e_SRD:Monk#Martial_Arts
        """
        attacks_chain_bonus = []
        if self.class_features.get('Flurry_of_Blows'):
            if hasattr(self, 'ki_points') and self.ki_points > 0 and self.bonus_action == True:
                self.ki_points -= 1
                self.bonus_action = False
                attack_choice = ('close','unarmed')
                attacks_chain_bonus.append(attack_choice)
                attacks_chain_bonus.append(attack_choice)
                # TODO: исправить
                # После первого применения добавляется ко всем рукопашным атакам:
                if self.class_features.get('Open_Hand_Technique'):
                    self.attacks[attack_choice]['Open_Hand_Technique'] = True
        if self.class_features.get('Martial_Arts'):
            if self.bonus_action == True:
                self.bonus_action = False
                attack_choice = ('close','unarmed')
                attacks_chain_bonus.append(attack_choice)
        return attacks_chain_bonus

    def set_stunnign_strike(self, enemy_soldier, attack_dict):
        """Монах использует оглушающую атаку.

        - Если противник не оглушён.
        - Если есть на это свободные Ки.
        - Если противник достаточно опасен.
        
        Возвращает сложность спасброска.
        """
        if self.class_features.get('Stunning_Strike')\
                and enemy_soldier.behavior == 'commander'\
                and not enemy_soldier.stunned:
            if hasattr(self, 'ki_points') and self.ki_points > 0:
                self.ki_points -= 1
                stunned_difficult = 8 + self.proficiency_bonus + self.mods['wisdom']
                return stunned_difficult

    def set_initiative(self, advantage = False, disadvantage = False):
        """Бросок инициативы делается в начале боя.
        
        Бросаем d20 + модификатор ловкости.
        По этому броску выбираем, в каком порядке ходят бойцы.
        https://www.dandwiki.com/wiki/5e_SRD:Initiative
        """
        if self.class_features.get('Feral_Instinct'):
            advantage = True
        initiative = dices.dice_throw_advantage('1d20', advantage, disadvantage) + self.mods['dexterity']
        if self.class_features.get('Feat_Alert'):
            initiative += 5
        # Homebrew: талант "Идеальное взаимодействие".
        if self.__dict__.get('squad_advantage'):
            initiative += 10
        self.initiative = initiative

    def set_coordinates(self, place):
        """Боец получает свои координаты на карте."""
        self.place = place

    def get_coordinates(self):
        """Боец возвращает свои координаты, если есть."""
        if hasattr(self, 'place'):
            return self.place
        else:
            return None

    def set_ally_side(self, ally_side):
        """Указываем своих."""
        self.ally_side = ally_side

    def set_enemy_side(self, enemy_side):
        """Указываем врага."""
        self.enemy_side = enemy_side

    def set_near_enemies(self, dict_recon):
        """Словарь врагов в радиусе 5 футов."""
        near_enemies = [ ]
        for char in dict_recon.values():
            if char.side == self.enemy_side:
                near_enemies.append(char)
        self.near_enemies = near_enemies

    def set_near_allies(self, dict_recon):
        """Словарь врагов в радиусе 5 футов"""
        near_allies = [ ]
        for char in dict_recon.values():
            if char.side == self.ally_side:
                near_allies.append(char)
        self.near_allies = near_allies

    def set_place_in_order(self, place_in_order):
        """Место в строю относительно командира."""
        self.place_in_order = place_in_order

    def set_danger(self, danger, squad):
        """Опасность окружения, плюс влияние морали и ранений.
        
        Предпосылки:
        - Боец каждый раунд запоминает окружение (3x3 клетки) с помощью recon_action.
        - И численно оценивает соотношение сил своих/врагов с помощью danger_sense.
        - Опасность выше нуля -- преимущество врагов, надо защищаться/отступать.
        - Опасность ниже нуля -- преимущество своих, атаковать можно.
        Каждая единица морали сравнима с одним товарищем за спиной каждого бойца.

        Здесь же коррекция оценки по состоянию здоровья и морали:
        - Потеря 10% хитов -- +1 к опасности.
        - Потеря 10% союзников -- +1 к опсности.
        """
        # TODO: перенеси все escape в morality_check_escape.
        self.danger = danger - squad.moral
        # Некоторые бойцы вовсе не чувствуют опасности. Нежить, например.
        if hasattr(self, 'fearless') and self.fearless == True:
            self.danger = 0
            self.escape = False
            return True
        if hasattr(self, 'hero') and self.hero == True:
            self.danger = danger - ((squad.moral + 1) * 6)
            # Варварам в ярости на всё чихать (кроме магии):
            if hasattr(self, 'rage') and self.rage and not self.fear:
                self.danger = 0
                self.escape = False
                return True
        # Страх может быть вызван магией:
        if self.fear:
            fear_danger = self.fear_difficult - 10
            if self.danger > 0:
                self.danger += fear_danger
            else:
                self.danger = fear_danger
        # Каждые 10% потерянного здоровья увеличивают опасность:
        if self.hitpoints < self.hitpoints_max\
                and not 'fearless' in self.commands\
                and not self.equipment_weapon.get('Infusion of Healing'):
            hitpoints_danger = math.floor((1 - self.hitpoints / self.hitpoints_max) * 10)
            self.danger += hitpoints_danger
            # Раненые осьминожки удирают:
            if self.__dict__.get('water_walk') and self.hitpoints < (self.hitpoints_max / 2):
                self.danger = 0
                self.escape = True
            #if 'dodge' in self.commands and self.hitpoints < (self.hitpoints_max / 2):
            #    self.danger = 0
            #    self.escape = True
        # Каждые 10% потерь союзников также увеличивают угрозу:
        if squad.casualty['casualty_percent'] > 0 and not 'fearless' in self.commands:
            casualty_danger = round(squad.casualty['casualty_percent'] / 10)
            self.danger += casualty_danger
        if self.behavior == 'archer':
            # Если у лучника нет дальних атак, значит боеприпасы закончились и время делать ноги:
            #for attack in self.attacks.keys():
            #    if attack[0] == 'ranged' or attack[0] == 'throw' or hasattr(self, 'spells'):
            #        break
            #else:
            #    self.danger = 1
            #    self.escape = True
            # Это же относится к магам, у которых закончились слоты заклинаний:
            #if hasattr(self, 'spells') and not self.spellslots and 'dodge' in self.commands:
            #    self.danger = 1
            #    self.escape = True
            # Если враг рядом, лучники тоже отступают (хотя могут и просто держать дистанцию).
            # Не используется, работает команда disengage.
            #if self.near_enemies:
            #    self.danger = 1
            #    self.escape = True
            # Конные лучники отступают, если ранен конь:
            if hasattr(self, 'mount_uuid') and self.mount_uuid in squad.metadict_soldiers:
                mount = squad.metadict_soldiers[self.mount_uuid]
                if mount.escape == True and 'dodge' in self.commands:
                    self.danger = 1
                    self.escape = True

    def set_protection(self, soldier):
        """Боец прикрывает союзника по его просьбе.
        
        Fighting_Style_Protection даёт disadvantage на атаку врага."""
        # Просто указываем, что реакция сработала:
        if self.class_features.get('Fighting_Style_Protection')\
                and self.armor['shield_use'] != None\
                and self.shield_ready\
                and self.reaction:
            self.reaction = False
            return True
        else:
            return False

    def set_reckless_attack(self):
        """Безрассудная атака варавара.
        
        Преимущество к атаке на один ход, помеха к защите от врагов."""
        if self.class_features.get('Reckless_Attack') == True:
            self.reckless_attack = True
            return True
        else:
            return False

    def set_action_surge(self):
        """Fighter может получить удвоенный ход."""
        # Только показываем, что двойной ход взят:
        if self.class_features.get('Action_Surge'):
            if self.action_surge and self.bonus_action:
                self.bonus_action = False
                self.action_surge = False
                return True
            else:
                return False

    def use_dash_action(self, bonus_action = False):
        """Боец ускоряется.
        
        https://www.dandwiki.com/wiki/5e_SRD:Dash_Action
        """
        if self.bonus_action and self.class_features.get('Cunning_Action'):
            self.set_cunning_action_dash()
        elif self.bonus_action and bonus_action:
            self.bonus_action = False
            self.dash_action = True
        elif self.battle_action:
            self.battle_action = False
            self.dash_action = True

    def use_disengage_action(self):
        """Боец уклоняется от провоцированных атак на движение.

        https://www.dandwiki.com/wiki/5e_SRD:Disengage_Action
        """
        if self.bonus_action and self.class_features.get('Cunning_Action'):
            return self.set_cunning_action_disengage()
        elif self.bonus_action and self.class_features.get('Step_of_the_Wind'):
            return self.set_step_of_the_wind_disengage()
        elif self.battle_action:
            self.battle_action = False
            self.dodge_action = True
            return True

    def use_dodge_action(self):
        """Боец защищается.
        
        https://www.dandwiki.com/wiki/5e_SRD:Dodge_Action
        """
        if self.bonus_action and self.class_features.get('Cunning_Action'):
            return self.set_cunning_action_defence()
        elif self.bonus_action and self.class_features.get('Patient_Defense'):
            return self.set_patient_defence()
        elif self.battle_action:
            self.battle_action = False
            self.dodge_action = True
            return True

    def use_heal(self, use_minor_potion = False):
        """Боец лечит себя, если способен."""
        if self.__dict__.get('second_wind'):
            self.use_second_wind()
        elif self.__dict__.get('lay_on_hands'):
            self.use_lay_on_hands()
        elif 'potions' in self.commands:
            self.use_heal_potion(use_minor_potion)

    def use_second_wind(self):
        """Fighter может очухаться после ранения.
        
        https://www.dandwiki.com/wiki/5e_SRD:Fighter#Second_Wind
        """
        if self.class_features.get('Second_Wind'):
            if self.second_wind and self.bonus_action:
                second_wind_heal = dices.dice_throw('1d10') + self.level
                self.set_hitpoints(heal = second_wind_heal)
                self.bonus_action = False
                self.second_wind = False
                print('{0} {1} {2} heal (second_wind): {3}'.format(
                    self.ally_side, self.place, self.behavior, second_wind_heal))
                return True
            else:
                return False

    def use_lay_on_hands(self):
        """Паладин способен лечить себя и других:
        
        https://www.dandwiki.com/wiki/5e_SRD:Paladin#Lay_on_Hands
        """
        if self.class_features.get('Lay_on_Hands'):
            if self.lay_on_hands and self.battle_action:
                lay_on_hands_heal = self.hitpoints_max - self.hitpoints 
                if lay_on_hands_heal > self.lay_on_hands:
                    lay_on_hands_heal = self.lay_on_hands
                self.set_hitpoints(heal = lay_on_hands_heal)
                self.lay_on_hands = self.lay_on_hands - lay_on_hands_heal
                self.battle_action = False
                print('{0} {1} {2} heal (lay_on_hands): {3}'.format(
                    self.ally_side, self.place, self.behavior, lay_on_hands_heal))
                return True
            else:
                return False

    def use_heal_potion(self, use_battle_action = True, use_minor_potion = False):
        """Боец использует зелье лечения.
        
        Лечение равно костям хитов бойца. Для варвара 5 lvl это 5d12, в среднем 30 hp.
        """
        # TODO: есть мнение, что лечение эссенцией слишком сильное.
        # Варвар с x3 лечилками восстанавливает аж 90 хитов.
        # Когда паладин с его Lay_on_Hands получает всего 25 хитов.
        # TODO: У солдата с плюсовыми хитпоинтами должен исчезать статус defeat
        if self.battle_action or use_battle_action == False:
            if self.equipment_weapon.get('Infusion of Healing', 0) > 0 and not use_minor_potion:
                self.drop_item('Infusion of Healing')
                potion_heal = round(sum([dices.dice_throw(self.hit_dice) for x in range(self.level)]))
                self.set_hitpoints(heal = potion_heal)
                self.battle_action = False
                print('{0} {1} {2} heal (potion): {3}'.format(
                    self.ally_side, self.place, self.behavior, potion_heal))
                return True
            elif self.equipment_weapon.get('Goodberry', 0) > 0:
                self.drop_item('Goodberry')
                potion_heal = 1
                self.set_hitpoints(heal = potion_heal)
                self.battle_action = False
                print('{0} {1} {2} heal (potion): {3}'.format(
                    self.ally_side, self.place, self.behavior, potion_heal))
                return True
            elif self.equipment_weapon.get('Infusion of Regeneration', 0) > 0:
                spell_dict = self.metadict_items['Infusion of Regeneration']
                potion_heal = spell_dict['healing_mod']
                self.set_hitpoints(heal = potion_heal)
                self.battle_action = False
                #print('{0} {1} {2} heal (regen): {3}'.format(
                #    self.ally_side, self.place, self.behavior, potion_heal))
                return True
            elif self.class_features.get('Regeneration_Minor'):
                potion_heal = self.class_features['Regeneration_Minor']
                self.set_hitpoints(heal = potion_heal)
                self.battle_action = False
                #print('{0} {1} {2} heal (potion): {3}'.format(
                #    self.ally_side, self.place, self.behavior, potion_heal))
                return True
            else:
                return False

    def use_potion_of_heroism(self, use_battle_action = True):
        """Боец использует зелье героизма.
        
        Homebrew: даёт +1 hp/уровень в течении минуты.
        """
        if self.battle_action or use_battle_action == False:
            if self.equipment_weapon.get('Infusion of Heroism', 0) > 0:
                self.drop_item('Infusion of Heroism')
                self.heroism_timer = 10
                self.heroism = True
                if self.bonus_hitpoints < self.level:
                    self.bonus_hitpoints = self.level
                return True
            elif self.equipment_weapon.get('Potion of Bravery', 0) > 0:
                self.drop_item('Potion of Bravery')
                spell_dict = self.metadict_items['Potion of Bravery']
                bonus_hitpoints = dices.dice_throw(spell_dict['healing_dice'])
                poisoned = self.set_poisoned(spell_dict['spell_save_DC'], spell_dict['effect_timer'])
                if poisoned:
                    print('[+++] {side_1}, {c1} {s} POISONED << Potion of Bravery'.format(
                        side_1 = self.ally_side,
                        c1 = self.place,
                        s = self.behavior,
                        ))
                if self.bonus_hitpoints < bonus_hitpoints:
                    self.bonus_hitpoints = bonus_hitpoints
                return True
            else:
                return False

    def first_aid(self, injured_ally, stabilizing_difficul = 10, advantage = False, disadvantage = False):
        """Боец пытается оказать первую помощь раненому.
        
        https://www.dandwiki.com/wiki/5e_SRD:Dropping_to_0_Hit_Points#Stabilizing_a_Creature
        - Добряника обнуляет сложность стабилизации, потому что стабилизирует даже +1 hp.
        """
        # TODO: лучше сделай поиск предмета по эффекту "healing".
        # potion_heal бери из словаря Goodberry.
        self.help_action = True
        if injured_ally.equipment_weapon.get('Goodberry', 0) > 0:
            injured_ally.drop_item('Goodberry')
            potion_heal = 1
            injured_ally.set_hitpoints(heal = potion_heal)
            stabilizing_difficul = 0
            print('{0} {1} {2} (help_action) >> {3}, {4}, {5} heal (potion): {6}'.format(
                self.ally_side, self.place, self.behavior,
                injured_ally.ally_side, injured_ally.place, injured_ally.behavior,
                potion_heal))
        # TODO: Учти Feat_Healer, что даёт автоматический успех стабилизации. И набор лекаря.
        stabilizing_throw = dices.dice_throw_advantage('1d20', advantage, disadvantage)\
                + self.saves['wisdom']
        if stabilizing_throw >= stabilizing_difficul:
            return True
        else:
            return False

    def first_aid_spell(self, injured_ally, spell_choice, vision_tuple):
        """Лекарь использует заклинание лечения.
        
        - Лекарь должен видеть раненого.
        - Раненый должен быть на дистанции заклинания.
        """
        distance_max = round(self.spells[spell_choice].get('attack_range', 0) / self.tile_size)
        casting_action = self.spells[spell_choice].get('casting_time', None)
        # casting_action должно иметь значение "battle_action" или "bonus_action":
        if casting_action and self.__dict__.get(casting_action)\
                and vision_tuple.distance <= distance_max:
            self.__dict__[casting_action] = False
            spell_dict = self.spells_generator.use_spell(spell_choice)
            heal = dices.dice_throw_advantage(spell_dict['damage_dice']) + spell_dict['damage_mod']
            injured_ally.set_hitpoints(heal)
            print('{0} {1} {2} (help_action) >> {3}, {4}, {5} heal (spell): {6}'.format(
                self.ally_side, self.place, self.behavior,
                injured_ally.ally_side, injured_ally.place, injured_ally.behavior,
                heal))
            return True
        else:
            return False

# ----
# Спасброски

    def set_fall_prone(self, enemy_soldier, advantage = False, disadvantage = False, difficult = False):
        """Бойца пытаются сбить с ног.
        
        Проверка Ловкости (акробатика), или Силы (атлетика):
        https://www.dandwiki.com/wiki/5e_SRD:Conditions#Prone
        https://www.dandwiki.com/wiki/5e_SRD:Movement_and_Position#Being_Prone
        """
        # TODO: должно быть владение навыком атлетика.
        # Сделай таблицы навыков в classes.
        if not difficult:
            if enemy_soldier.mods['strength'] >= enemy_soldier.mods['dexterity']:
                difficult = dices.dice_throw_advantage('1d20', advantage, disadvantage)\
                        + enemy_soldier.mods['strength'] + enemy_soldier.proficiency_bonus
            else:
                difficult = dices.dice_throw_advantage('1d20', advantage, disadvantage)\
                        + enemy_soldier.mods['dexterity'] + enemy_soldier.proficiency_bonus
        if self.saves['strength'] >= self.saves['dexterity']:
            ability = 'strength'
        else:
            ability = 'dexterity'
        if self.get_savethrow(difficult, ability, advantage, disadvantage):
            return False
        else:
            self.prone = True
            return True

    def set_restained(self, difficult, advantage = False, disadvantage = False):
        """Бойца пытаются опутать.
        
        Проверка ловкости (Акробатика), или силы (Атлетика):
        https://www.dandwiki.com/wiki/5e_SRD:Conditions#Grappled
        """
        if self.saves['strength'] >= self.saves['dexterity']:
            ability = 'strength'
        else:
            ability = 'dexterity'
        if self.get_savethrow(difficult, ability, advantage, disadvantage):
            return False
        else:
            self.restained_difficult = difficult
            self.restained = True
            self.move_action = False
            self.move_pool = 0
            return True

    def set_poisoned(self, difficult, timer = 10, advantage = False, disadvantage = False):
        """Бойца пытаются отравить

        - Помеха на броски атаки
        - Помеха на проверки характеристик
        
        Спасбросок телосложения.
        https://www.dandwiki.com/wiki/5e_SRD:Conditions#Poisoned
        """
        ability = 'constitution'
        if self.get_savethrow(difficult, ability, advantage, disadvantage):
            return False
        else:
            self.poison_difficult = difficult
            self.poison_timer = timer
            self.poisoned = True
            return True

    def set_stunned(self, difficult, timer = 1, advantage = False, disadvantage = False):
        """Бойца пытаются оглушить.
        
        - Ошеломлённое существо недееспособно (не может совершать действия и реакции)
        - Проваливает все спасброски силы и ловкости
        - Броски атаки по существу с преимуществом

        Спасбросок телосложения:
        # https://www.dandwiki.com/wiki/5e_SRD:Conditions#Stunned
        # https://www.dandwiki.com/wiki/5e_SRD:Conditions#Incapacitated
        """
        ability = 'constitution'
        if self.get_savethrow(difficult, ability, advantage, disadvantage):
            return False
        else:
            self.stunned_difficult = difficult
            self.stunned_timer = timer
            self.stunned = True
            return True

    def set_paralyzed(self, difficult, timer = 10, advantage = False, disadvantage = False):
        """Бойца пытаются парализовать.
        
        - Ошеломлённое существо недееспособно (не может совершать действия и реакции)
        - Проваливает все спасброски силы и ловкости
        - Броски атаки по существу с преимуществом
        - Все попадания критические с 5 футов.

        Спасбросок телосложения:
        # https://www.dandwiki.com/wiki/5e_SRD:Conditions#Paralyzed
        # https://www.dandwiki.com/wiki/5e_SRD:Conditions#Incapacitated
        """
        ability = 'constitution'
        if self.get_savethrow(difficult, ability, advantage, disadvantage):
            return False
        else:
            self.paralyzed_difficult = difficult
            self.paralyzed_timer = timer
            self.paralyzed = True
            return True

    def set_sleep(self, difficult = 100, timer = 10, advantage = False, disadvantage = False):
        """Бойца пытаются усыпить.
        
        - Заклинание "Sleep" срабатывает без спасброска.
        - Яд позволяет сделать спасбросок телосложения.

        https://www.dandwiki.com/wiki/5e_SRD:Conditions#Unconscious
        """
        # TODO: Мертвяки и конструкты неуязвимы к усыплению. Эльфы тоже.
        ability = 'constitution'
        if self.get_savethrow(difficult, ability, advantage, disadvantage):
            return False
        else:
            self.sleep = True
            self.prone = True
            self.battle_action = None
            self.bonus_action = None
            self.reaction = None
            self.move_action = None
            self.move_pool = 0
            self.sleep_timer = timer
            return True

    def set_grappled(self, enemy_soldier, advantage = False, disadvantage = False, difficult = False):
        """Бойца пытаются схватить.
        
        Проверка Ловкости (акробатика), или Силы (атлетика):
        https://www.dandwiki.com/wiki/5e_SRD:Conditions#Grappled
        """
        if not difficult:
            if enemy_soldier.mods['strength'] >= enemy_soldier.mods['dexterity']:
                difficult = dices.dice_throw_advantage('1d20', advantage, disadvantage)\
                        + enemy_soldier.mods['strength'] + enemy_soldier.proficiency_bonus
            else:
                difficult = dices.dice_throw_advantage('1d20', advantage, disadvantage)\
                        + enemy_soldier.mods['dexterity'] + enemy_soldier.proficiency_bonus
        if self.saves['strength'] >= self.saves['dexterity']:
            ability = 'strength'
        else:
            ability = 'dexterity'
        if self.get_savethrow(difficult, ability, advantage, disadvantage):
            return False
        else:
            self.enemy_grappler = enemy_soldier
            self.grappled = True
            self.move_action = False
            self.move_pool = 0
            return True

    def set_grapple_break(self, advantage = False, disadvantage = False):
        """Боец пытается вырваться из захвата, тратя на это battle_action.
        
        Проверка Силы (атлетика) или Ловкости (акробатика) против Силы (атлетика) удерживающего врага:
        """
        enemy_soldier = self.enemy_grappler
        # Если схватившего нет рядом, значит захват уже сорвался:
        if not self.near_enemies:
            self.grappled = False
            self.enemy_grappler = None
        elif self.near_enemies:
            enemy_uuids = [enemy.uuid for enemy in self.near_enemies]
            if not self.enemy_grappler.uuid in enemy_uuids:
                self.grappled = False
                self.enemy_grappler = None
            else:
                difficult = dices.dice_throw_advantage('1d20', advantage, disadvantage)\
                        + enemy_soldier.mods['strength'] + enemy_soldier.proficiency_bonus
                if self.saves['strength'] >= self.saves['dexterity']:
                    ability = 'strength'
                else:
                    ability = 'dexterity'
                if not self.get_savethrow(difficult, ability, advantage, disadvantage):
                    self.battle_action = False
                    return False
                else:
                    self.battle_action = False
                    self.enemy_grappler = None
                    self.grappled = False
                    return True

    def set_restained_break(self, advantage = False, disadvantage = False, difficult = False):
        """Боец пытается вырваться из захвата, тратя на это battle_action.

        - Чаще всего это сложность заклинания "Опутывание", щупальц осьминога и т.д.
        
        Проверка Силы (атлетика) или Ловкости (акробатика) против СЛ.
        """
        if not difficult:
            difficult = self.restained_difficult
        if self.saves['strength'] >= self.saves['dexterity']:
            ability = 'strength'
        else:
            ability = 'dexterity'
        if not self.get_savethrow(difficult, ability, advantage, disadvantage):
            self.battle_action = False
            return False
        else:
            self.battle_action = False
            self.restained_difficult = None
            self.enemy_grappler = None
            self.restained = False
            return True

    def set_disarm_shield(self, enemy_soldier, advantage = False, disadvantage = False, difficult = False):
        """Бойца пытаются лишить щита.
        
        Проверка Ловкости (акробатика), или Силы (атлетика):
        Опциональное правило: Dungeon Master Guide p.271
        """
        if not difficult:
            if enemy_soldier.mods['strength'] >= enemy_soldier.mods['dexterity']:
                difficult = dices.dice_throw_advantage('1d20', advantage, disadvantage)\
                        + enemy_soldier.mods['strength'] + enemy_soldier.proficiency_bonus
            else:
                difficult = dices.dice_throw_advantage('1d20', advantage, disadvantage)\
                        + enemy_soldier.mods['dexterity'] + enemy_soldier.proficiency_bonus
        if self.saves['strength'] >= self.saves['dexterity']:
            ability = 'strength'
        else:
            ability = 'dexterity'
        if self.get_savethrow(difficult, ability, advantage, disadvantage):
            return False
        else:
            enemy_soldier.get_trophy(
                    self.armor['shield_use'],
                    self.equipment_weapon[self.armor['shield_use']],
                    )
            self.unset_shield(disarm = True)
            return True

    def set_disarm_weapon(self, enemy_soldier, advantage = False,
            disadvantage = False, difficult = False, close = False):
        """Бойца пытаются лишить оружия.
        
        Проверка Ловкости (акробатика), или Силы (атлетика):
        Опциональное правило: Dungeon Master Guide p.271
        """
        # TODO: По правилам обезоруживание, это бросок атаки оружием.
        if not difficult:
            if enemy_soldier.mods['strength'] >= enemy_soldier.mods['dexterity']:
                difficult = dices.dice_throw_advantage('1d20', advantage, disadvantage)\
                        + enemy_soldier.mods['strength'] + enemy_soldier.proficiency_bonus
            else:
                difficult = dices.dice_throw_advantage('1d20', advantage, disadvantage)\
                        + enemy_soldier.mods['dexterity'] + enemy_soldier.proficiency_bonus
        if self.saves['strength'] >= self.saves['dexterity']:
            ability = 'strength'
        else:
            ability = 'dexterity'
        if self.get_savethrow(difficult, ability, advantage, disadvantage):
            return False
        else:
            if self.weapon_ready:
                weapon = self.weapon_ready
                enemy_soldier.get_trophy(weapon, self.equipment_weapon[weapon])
                self.unset_weapon(weapon, disarm = True)
            else:
                weapon_list = self.get_weapon_list(close)
                weapon = random.choice(weapon_list)
                enemy_soldier.get_trophy(weapon, self.equipment_weapon[weapon])
                self.unset_weapon(weapon, disarm = True)
            if not self.get_weapon_list(close):
                return True

    def morality_check_escape(self, danger, advantage = False, disadvantage = False):
        """Если опасность высока, боец боится и может сбежать.
        
        Это проверка 10 + уровень_опасности против спасброска харизмы.
        """
        difficult = 10 + danger
        ability = 'charisma'
        if self.get_savethrow(difficult, ability, advantage, disadvantage):
            return False
        else:
            return True

    def set_fear(self, enemy_soldier, difficult, advantage = False, disadvantage = False):
        """Бойца пытаются испугать.
        
        - Заклинание "Fear" или "Cause_Fear"
        - Menacing_Attack мастера боевых искусств.

        Спасбросок мудрости.
        https://www.dandwiki.com/wiki/5e_SRD:Conditions#Frightened
        """
        ability = 'wisdom'
        if self.get_savethrow(difficult, ability, advantage, disadvantage):
            self.fear_difficult = None
            self.fear_source = None
            self.fear = False
            return False
        else:
            self.fear_difficult = difficult
            self.fear_source = enemy_soldier
            self.fear = True
            return True

    def set_death(self):
        """Тяжелораненые играет в рулетку с мрачным жнецом.
        
        Death Saving Throws:
        https://www.dandwiki.com/wiki/5e_SRD:Dropping_to_0_Hit_Points
        """
        if not hasattr(self, 'death_save_success')\
                and not hasattr(self, 'death_save_loss'):
            self.death_save_loss = 0
            self.death_save_success = 0
        # Возвращение друида в обычную форму, если выбыл:
        if self.wild_shape:
            self.return_old_form()
        # Схваченного легко убить, или взять в плен:
        if self.grappled and self.enemy_grappler\
                and not 'kill' in self.enemy_grappler.commands:
            self.death_save_success = 3
            self.stable = True
            self.captured = True
            return False
        # Мгновенная смерть, если атака увела хиты в минусовой максимум:
        if self.hitpoints <= -(self.hitpoints_max):
            self.death_save_loss = 3
            self.killer_mark = False
            self.set_disabled(death_trauma = True)
            self.death = True
            return True
        # Тяжелейшие ранения, если атака лишь чуть не убила бойца:
        elif self.hitpoints <= -(self.hitpoints_max / 2):
            self.set_disabled()
        # Механизмы не бросают спасброски:
        if self.__dict__.get('mechanism') and not self.death:
            #self.death_save_success = 3
            #self.stable = True
            return False
        # Тролли и прочие создания с регенерацией стабилизируются сами:
        # Их нельзя убить, уведя хиты в минусовой максимум. Только огнём.
        if self.class_features.get('Regeneration'):
            self.death_save_success = 3
            self.stable = True
            return False
        # Иначе борьба за жизнь, где всё в руках судьбя:
        if not self.stable == True and not self.death == True:
            # Играем в рулетку с мрачным жнецом:
            reaper_throw = dices.dice_throw('1d20')
            if reaper_throw == 20:
                self.death_save_success += 2
            elif reaper_throw >= 10:
                self.death_save_success += 1
            elif reaper_throw == 1:
                self.death_save_loss += 2
            else:
                self.death_save_loss += 1
            if self.death_save_success >= 3:
                self.stable = True
            elif self.death_save_loss >= 3:
                self.death = True
        if self.stable:
            self.killer_mark = False
        if self.death:
            self.killer_mark = False
            print('{0} {1} {2} {3} hp {4}/{5} throw {6} result {7}:{8} stable {9} dead {10}'.format(
                self.ally_side, self.place, self.behavior, self.name,
                self.hitpoints, self.hitpoints_max,
                reaper_throw, self.death_save_success, self.death_save_loss,
                self.stable, self.death))

    def set_disabled(self, advantage = False, disadvantage = False,
            trauma_damage_type = None, death_trauma = False):
        """Тяжёлые раны калечат бойца.
        
        "Длительные травмы" из "Руководства мастера".
        """
        # Герои и офицеры реже получают серьёзные травмы.
        if self.hero or self.level >= 3:
            advantage = True
        if death_trauma:
            disadvantage = True
        if self.trauma_damage_type:
            trauma_damage_type = self.trauma_damage_type
        trauma_throw = dices.dice_throw_advantage('1d20', advantage, disadvantage)
        if trauma_damage_type in ['slashing','piercing','bludgeoning','thunder']:
            dict_traumas = dict(traumas.dict_traumas_base)
        elif trauma_damage_type in ['fire','lightning','radiant','acid']:
            dict_traumas = dict(traumas.dict_traumas_fire)
        elif trauma_damage_type in ['cold','necrotic','necrotic_energy']:
            dict_traumas = dict(traumas.dict_traumas_cold)
        elif trauma_damage_type in ['poison']:
            dict_traumas = dict(traumas.dict_traumas_necrotic)
        else:
            dict_traumas = dict(traumas.dict_traumas_base)
        # Только травмы 1-10 лишают бойца боеспособности.
        if trauma_throw <= 10:
            self.disabled = True
        trauma = dict_traumas[trauma_throw]
        if not trauma in self.traumas_dict:
            self.traumas_dict[trauma] = 1
        elif trauma in self.traumas_dict:
            self.traumas_dict[trauma] += 1

# ----
# Универсальная проверка спасброска.

    def get_savethrow(self, difficult, ability, advantage = None, disadvantage = None):
        """Делаем спасбросок.
        
        - Учитываем преимущества к броскам характеристик.
        - И помехи к броскам характеристик.
        """
        if not advantage == None:
            advantage = self.check_savethrow_advantage(ability)
        if not disadvantage == None:
            disadvantage = self.check_savethrow_disadvantage(ability)
        savethrow_result = dices.dice_throw_advantage('1d20', advantage, disadvantage) + self.saves[ability]
        savethrow_result += self.get_savethrow_bonus(ability)
        if self.check_savethrow_autofail(ability):
            return False
        elif difficult <= savethrow_result:
            return True
        else:
            return False

    def get_savethrow_bonus(self, ability):
        """Бонус к спасброскам от способностей класса.

        """
        savethrow_bonus = 0
        if self.class_features.get('Remarkable_Athlete'):
            if ability not in self.dict_class_saves[self.char_class]:
                savethrow_bonus = round(self.proficiency_bonus / 2)
        return savethrow_bonus

    def check_savethrow_autofail(self, ability):
        """Проверка автопровала спасброска.
        
        - Ошеломлённый проваливает спасброски силы и ловкости.
        - Бессознательный проваливает спасброски силы и ловкости.
        - Парализованный проваливает спасброски силы и ловкости.
        - Окаменевший проваливает спасброски силы и ловкости.
        """
        if ability == 'strength' or ability == 'dexterity':
            if self.sleep:
                return True
            elif self.stunned:
                return True
            elif self.paralyzed:
                return True
            elif self.petrified:
                return True
            else:
                return False
        else:
            return False

    def check_savethrow_advantage(self, ability):
        """Способности могут дать преимущество на спасбросок."""
        # Варвары в ярости получают преимущество на спасброски силы:
        if ability == 'strength':
            if self.class_features.get('Rage') and self.rage:
                return True
        # Homebrew: преимущества к морали от храбрости командира:
        elif ability == 'charisma':
            if 'brave' in self.commands:
                return True
        else:
            return False

    def check_savethrow_disadvantage(self, ability):
        """Способности могут дать преимущество на спасбросок."""
        # TODO: уточни, включают ли "проверки характеристик" спасброски.
        # Отравление даёт помеху на проверки характеристик.
        if self.poisoned:
            return True
        else:
            return False

# ----
# Вывод данных

    def get_weapon_list(self, close = False):
        """Список оружия из атак бойца.
        
        """
        weapon_list = []
        for attack_choice, attack_dict in self.attacks.items():
            if attack_dict.get('weapon_use'):
                if close and 'close' in attack_dict.get('weapon_type',[]):
                    weapon_list.append(attack_dict['weapon_use'])
                elif not close:
                    weapon_list.append(attack_dict['weapon_use'])
        weapon_list = list(set(weapon_list))
        return weapon_list

    def get_experience(self):
        """Опыт за победу над этим бойцом.
        
        1) Опыт от паказателя опасности, challenge_rating, CR
        2) Опыт за уровень > 5 lvl
        3) Опыт за уровень <= 5 lvl
        """
        # Опыт от показателя опасности:
        if self.__dict__.get('challenge_rating')\
                and self.challenge_rating in self.challenge_rating_experience_dict:
            experience = self.challenge_rating_experience_dict[self.challenge_rating]
        # Если уровень > 5, то уровень и есть показатель опасности:
        elif self.level > 5:
            experience = self.challenge_rating_experience_dict[str(self.level)]
        # Для простых солдат считается сложнее:
        else:
            # Опыт за уровень врага:
            # 1 lvl: 25*2^(1-1) = 25 exp; 5 lvl: 25*2^(5-1) = 400 exp
            experience = 25 * 2 ** (self.level - 1)
            if self.hero:
                experience *= 2
            elif self.char_class == 'Commoner':
                experience /= 2.5
        experience = round(experience)
        return experience

# ----
# Движения и атака:

    def move(self, distance = 5, rough = False):
        """Боец двигается. Обычно на 5 футов (один тайл карты).
        
        Возможности:
        - Dash_Action -- двухкратное ускорение.
        """
        # TODO: добавь правило диагонального перемещения.
        # А заодно и направление движения в стиле север/юг.
        # dash_action -- удвоенная скорость.
        if self.dash_action:
            distance = distance / 2
        if rough:
            # Пересечённая местность -- удвоенные потери пуля движения:
            self.move_pool -= distance * 2
        else:
            self.move_pool -= distance
        if self.move_pool <= 0:
            self.move_action = False
        return True

    def select_enemy(self, near_enemies, select_strongest = False, select_weaker = False):
        """Выбираем слабейшего/сильнейшего врага из списка целей.
        
        Лучшая тактика в текущих условиях боя -- выбивать слабейших.
        """
        if 'select_weaker' in self.commands:
            select_weaker = True
        elif 'select_strongest' in self.commands:
            select_strongest = True
        # На входе может быть как список, так и словарь:
        if type(near_enemies) == dict:
            near_enemies = near_enemies.values()
        # Список типов противников, отсортированный по уровню угрозы:
        if select_weaker == True:
            danger_list = reversed(list(self.dict_danger.keys()))
        elif select_strongest == True:
            danger_list = list(self.dict_danger.keys())
        else:
            danger_list = (list(self.dict_danger.keys()))
            random.shuffle(danger_list)
        # Выбор первого врага, который сильнейший/слабейший из списка угроз:
        for enemy_type in danger_list:
            for target in near_enemies:
                if target.type == enemy_type:
                    return target    

    def select_attack(self, squad, enemy, tile_size = 5):
        """Боец выбирает атаку, уже зная врага.
        
        Смотрит по дистанции. Сначала выбирает ближние атаки, после дальние.
        """
        distance = enemy.distance
        enemy_cover = enemy.cover
        # ЗАМЕТКА: хитрый выбор атаки.
        # ------------------------------------------------------------
        # У бойца может быть куча разных атак (рукопашная, копьём, мечом)
        # Но выбирает он ту, в которой оружие дороже, или навыков к нему больше.
        # А если лучшей атаки нет (оружие потерялось), то какую-нибудь другую из подходящих.
        # ------------------------------------------------------------
        if distance <= 1 and 'close' in [attack[0] for attack in self.attacks]:
            close_attack_list = [attack for attack in self.attacks if attack[0] == 'close'
                    and attack[1] == self.attacks[attack]['weapon_of_choice']]
            if 'unarmed' in self.commands:
                close_attack_list = [attack for attack in self.attacks if attack[0] == 'close'
                        and attack[1] == 'unarmed']
            if close_attack_list:
                close_attack = random.choice(close_attack_list)
                return close_attack
            else:
                close_attack_list = [attack for attack in self.attacks if attack[0] == 'close']
                close_attack = random.choice(close_attack_list)
                return close_attack
        if distance <= 2 and 'reach' in [attack[0] for attack in self.attacks]:
            reach_attack_list = [attack for attack in self.attacks if attack[0] == 'reach'
                    and attack[1] == self.attacks[attack]['weapon_of_choice']]
            if reach_attack_list:
                reach_attack = random.choice(reach_attack_list)
                return reach_attack
            else:
                reach_attack_list = [attack for attack in self.attacks if attack[0] == 'reach']
                reach_attack = random.choice(reach_attack_list)
                return reach_attack
        if distance >= 2 and 'throw' in [attack[0] for attack in self.attacks]:
            throw_attack_list = [attack for attack in self.attacks if attack[0] == 'throw'
                    and attack[1] == self.attacks[attack]['weapon_of_choice']]
            if throw_attack_list:
                throw_attack = random.choice(throw_attack_list)
            else:
                throw_attack_list = [attack for attack in self.attacks if attack[0] == 'throw']
                throw_attack = random.choice(throw_attack_list)
            # Метатли дротиков работают с максимальной дистанции:
            if self.behavior == 'archer'\
                    and distance <= round(self.attacks[throw_attack]['attack_range_max'] / tile_size):
                return throw_attack
            # Застрельщики с пилумами тоже могут метать издалека по команде:
            elif 'volley' in self.commands\
                    and distance <= round(self.attacks[throw_attack]['attack_range_max'] / tile_size):
                return throw_attack
            # Бойцы ближнего боя подпускают пехоту врага поближе и метают прицельно:
            elif self.behavior != 'archer'\
                    and distance <= round(self.attacks[throw_attack]['attack_range'] / tile_size):
                return throw_attack
        if distance >= 2 and 'ranged' in [attack[0] for attack in self.attacks]:
            ranged_attack_list = [attack for attack in self.attacks if attack[0] == 'ranged'
                    and attack[1] == self.attacks[attack]['weapon_of_choice']]
            if ranged_attack_list:
                ranged_attack = random.choice(ranged_attack_list)
            else:
                ranged_attack_list = [attack for attack in self.attacks if attack[0] == 'ranged']
                ranged_attack = random.choice(ranged_attack_list)
            if distance <= round(self.attacks[ranged_attack]['attack_range_max'] / tile_size):
                return ranged_attack

    def select_spell(self, squad, enemy, tile_size = 5):
        """Боец выбирает заклинание, начиная с высших уровней."""
        distance = enemy.distance
        enemy_cover = enemy.cover
        spellslots_list = reversed(list(self.spellslots.keys()))
        for spell_slot in spellslots_list:
            # Без приказа только заклинания 1 круга:
            if int(spell_slot[0]) < 2 or 'fireball' in self.commands:
                if distance >= 2 and spell_slot in [attack[0] for attack in self.spells]:
                    spell_attack_list = [attack for attack in self.spells if attack[0] == spell_slot
                            and attack[1] == self.spells[attack]['spell_of_choice']]
                    if spell_attack_list:
                        spell_attack = random.choice(spell_attack_list)
                        if distance <= round(self.spells[spell_attack]['attack_range'] / tile_size):
                            #print(spell_attack, self.rank, self.spellslots)
                            return spell_attack
                if distance <= 2 and spell_slot in [attack[0] for attack in self.spells]:
                    spell_attack_list = [attack for attack in self.spells if attack[0] == spell_slot
                            and attack[1] == self.spells[attack]['spell_of_choice']
                            and self.spells[attack].get('effect',None) == 'burst']
                    if spell_attack_list:
                        spell_attack = spell_attack_list[0]
                        if distance <= round(self.spells[spell_attack]['attack_range'] / tile_size):
                            return spell_attack
        if distance >= 2 and 'cantrip' in [attack[0] for attack in self.spells]:
            spell_attack_list = [attack for attack in self.spells if attack[0] == 'cantrip'
                    and attack[1] == self.spells[attack]['spell_of_choice']
                    and not self.spells[attack].get('effect',None) == 'burst']
            if spell_attack_list:
                for spell_attack in spell_attack_list:
                    if distance <= round(self.spells[spell_attack]['attack_range'] / tile_size):
                        return spell_attack
        if distance < 2 and 'cantrip' in [attack[0] for attack in self.spells]:
            spell_attack_list = [attack for attack in self.spells if attack[0] == 'cantrip'
                    and attack[1] == self.spells[attack]['spell_of_choice']
                    and self.spells[attack].get('effect',None) == 'burst']
            # Используем Sword_Burst только если врагов больше одного:
            if spell_attack_list and len(self.near_enemies) > 1:
                for spell_attack in spell_attack_list:
                    if distance <= round(self.spells[spell_attack]['attack_range'] / tile_size):
                        return spell_attack

    def attack(self, attack_dict, attack_choice, enemy, metadict_soldiers,
            advantage = False, disadvantage = False):
        """Боец атакует (уже выбранной атакой).
        
        В выводе словарь атаки с числами атаки и урона.
        А также типом повреждений (piercing, slashing, bludgeoning)
        """
        target_cover = enemy.cover
        enemy_soldier = metadict_soldiers[enemy.uuid]
        # Используется боеприпас (стрела, дротик, яд для меча), если указан:
        if attack_dict.get('ammo'):
            self.use_ammo(attack_dict, metadict_soldiers)
        # Оружие в руки:
        if attack_dict.get('weapon') and attack_dict.get('weapon_use'):
            self.weapon_ready = attack_dict.get('weapon_use')
        # Нельзя использовать два приёма баттлмастера за одну атаку:
        superiority_use = False
        # Боец с двуручным оружием не может использовать щит:
        # Но только в том раунде, в котором пользовался двуручным оружием.
        # В set_actions щит каждый раз возвращается в боевое положение.
        if attack_dict.get('weapon_type')\
                and 'two_handed' in attack_dict['weapon_type']\
                and self.armor['shield_use']:
            self.unset_shield()
        # Стрельба из лука/арбалета неудобна вблизи,
        # Или на сверхдальности (для всех, кроме снайперов):
        if attack_dict.get('weapon_type')\
                and attack_choice[0] == 'ranged':
            if attack_dict['attack_range'] > self.tile_size * 2:
                if enemy.distance <= 2:
                    disadvantage = True
                elif enemy.distance > round(attack_dict['attack_range'] / self.tile_size)\
                        and not self.class_features.get('Feat_Sharpshooter'):
                    disadvantage = True
            # Меткие стрелки игнорируют укрытие и помехи по дальности:
            if self.class_features.get('Feat_Sharpshooter'):
                target_cover = 0
        # Бардовское Vicious_Mockery портит одиночную атаку:
        if self.mockery_hit:
            self.mockery_hit = False
            disadvantage = True
        # Диапазон критического урона может увеличить Champion_Improved_Critical:
        crit_range = self.crit_range
        loss_range = self.loss_range
        attack_throw = dices.dice_throw_advantage(
                dice_string = '1d20',
                disadvantage = disadvantage,
                advantage = advantage,
                )
        attack_throw_mod = attack_throw + attack_dict['attack_mod']
        # Заклинание Bless усиливает атаку:
        if 'bless' in self.buffs:
            attack_throw_mod += dices.dice_throw_advantage('1d4')
        # Channel_Sacred_Weapon усиливает атаку (и делает оружие волшебным):
        if self.sacred_weapon:
            attack_throw_mod += self.sacred_weapon
            if attack_dict.get('weapon_type') and not 'magic' in attack_dict['weapon_type']:
                attack_dict['weapon_type'].append('magic')
        # Bardic_Inspiration усиливает атаку:
        if 'bardic_inspiration' in self.buffs\
                and enemy_soldier.armor['armor_class'] > attack_throw_mod\
                and not enemy_soldier.armor['armor_class'] > attack_throw_mod\
                + self.buffs['bardic_inspiration']:
            attack_throw_mod += self.buffs.pop('bardic_inspiration',0)
        # Precision_Attack мастера боевых искусств:
        if self.class_features.get('Precision_Attack') and not superiority_use:
            superiority_dice_mid = round(int(self.superiority_dice[-1]) / 2)
            if self.superiority_dices\
                and enemy_soldier.armor['armor_class'] > attack_throw_mod\
                and not enemy_soldier.armor['armor_class'] > attack_throw_mod + superiority_dice_mid:
                attack_throw_mod += dices.dice_throw_advantage(self.superiority_dice)
                self.superiority_dices -= 1
                superiority_use = True
        # Great_Weapon_Fighting даёт преимущество по урону (в среднем +2 для диапазона 2d6):
        if attack_dict.get('weapon_skills_use')\
                and 'Fighting_Style_Great_Weapon_Fighting' in attack_dict['weapon_skills_use']:
            damage_throw_advantage = True
        else:
            damage_throw_advantage = False
        if attack_dict.get('weapon_type')\
                and 'sharpness' in attack_dict.get('weapon_type')\
                and enemy_soldier.__dict__.get('mechanism'):
            sharpness = True
        else:
            sharpness = False
        damage_throw = dices.dice_throw_advantage(attack_dict['damage_dice'],
                advantage = damage_throw_advantage, disadvantage = False, max_throw = sharpness)
        # Если атака критическая, бросаем кость урона дважды:
        # Если атака неудачная, то независимо от модификаторов результат нулевой:
        # Атаки по бессознательным вблизи всегда дают критическое попадание.
        if attack_throw >= crit_range\
                or attack_dict['attack_range'] <= 5 and enemy_soldier.sleep\
                or attack_dict['attack_range'] <= 5 and enemy_soldier.paralyzed:
            damage_throw = 0
            for throw in range(0, self.crit_multiplier):
                damage_throw += dices.dice_throw_advantage(attack_dict['damage_dice'],
                        advantage = damage_throw_advantage, disadvantage = False, max_throw = sharpness)
            attack_crit = True
            attack_loss = False
        elif attack_throw <= loss_range:
            attack_loss = True
            attack_crit = False
            attack_throw_mod = 0
        else:
            attack_loss = False
            attack_crit = False
        # Скрытная атака вора срабатывает только если нет помехи:
        # Также требуется преимущество, или товарищ рядом с врагом.
        # TODO: добавь Assassinate, атаку с преимуществом в первый ход боя.
        if self.class_features.get('Sneak_Attack') and not disadvantage:
            if advantage or len(enemy_soldier.near_enemies) > 1:
                sneak_attack_throw = dices.dice_throw_advantage(self.proficiency['sneak_attack_dice'],
                        advantage = False, disadvantage = False, max_throw = sharpness)
                damage_throw += sneak_attack_throw
                if attack_throw >= crit_range\
                        or attack_dict['attack_range'] <= 5 and enemy_soldier.sleep:
                    # Критический удар удваивает урон от скрытной атаки:
                    sneak_attack_throw = dices.dice_throw_advantage(self.proficiency['sneak_attack_dice'],
                            advantage = False, disadvantage = False, max_throw = sharpness)
                    damage_throw += sneak_attack_throw
        # Наконец, выводим общий урон:
        damage_throw_mod = damage_throw + attack_dict['damage_mod']
        if damage_throw_mod < 0:
            damage_throw_mod = 0
        # Бонус урона от ярости варвара:
        if hasattr(self, 'rage') and self.rage == True:
            if attack_choice[0] == 'close' or attack_choice[0] == 'reach':
                damage_throw_mod += self.rage_damage
        # Мастер тяжёлого оружия усиливает удар за счёт точности (если защита врага слаба):
        if attack_dict.get('weapon_skills_use'):
            if 'Feat_Great_Weapon_Master' in attack_dict['weapon_skills_use']:
                if enemy_soldier.armor['armor_class'] <= attack_dict['attack_mod'] + 10\
                        and enemy_soldier.hitpoints > damage_throw_mod\
                        and advantage and not disadvantage\
                        or enemy_soldier.__dict__.get('mechanism')\
                        and enemy_soldier.__dict__.get('ignore_damage'):
                    damage_throw_mod += 10
                    attack_throw_mod -=5
            # Снайпер тоже способен усилить урон за счёт точности:
            if 'Sharpshooter' in attack_dict['weapon_skills_use']:
                if enemy_soldier.armor['armor_class'] <= attack_dict['attack_mod'] + 10\
                        and enemy_soldier.hitpoints > damage_throw_mod\
                        and advantage and not disadvantage\
                        or 'kill' in self.commands:
                    damage_throw_mod += 10
                    attack_throw_mod -=5
        # Menacing_Attack мастера боевых искусств может испугать противника:
        # TODO: испугать можно тольпо при попадании. А здесь попадание не гарантировано.
        if self.class_features.get('Menacing_Attack') and not superiority_use:
            if self.superiority_dices and not enemy_soldier.fear\
                    and enemy_soldier.armor['armor_class'] < attack_throw_mod:
                damage_throw_mod += dices.dice_throw_advantage(self.superiority_dice)
                self.superiority_dices -= 1
                superiority_use = True
                fear_difficult = 8 + max(self.mods.values()) + self.proficiency_bonus
                fear = enemy_soldier.set_fear(self, fear_difficult)
                if fear:
                    print('[+++] {side_1}, {c1} {s} FEAR >> {side_2} {c2} {e}'.format(
                        side_1 = self.ally_side,
                        c1 = self.place,
                        s = self.behavior,
                        side_2 = enemy_soldier.ally_side,
                        c2 = enemy_soldier.place,
                        e = enemy_soldier.behavior,
                        ))
        attack_result_dict = {
                'damage':damage_throw_mod,
                'attack':attack_throw_mod,
                'damage_throw':damage_throw,
                'attack_throw':attack_throw,
                'attack_crit':attack_crit,
                'attack_loss':attack_loss,
                'advantage':advantage,
                'disadvantage':disadvantage,
                'enemy_cover':target_cover,
                'enemy_distance':enemy.distance,
                'victim_side':enemy.side,
                'victim_type':enemy.type,
                'victim_uuid':enemy.uuid,
                'sender_uuid':self.uuid,
                }
        attack_result_dict.update(attack_dict)
        return attack_result_dict

    def use_ammo(self, attack_dict, metadict_soldiers):
        """Расходуем боеприпас.

        - Если боеприпас есть в отряде, союзный солдат передаёт его.
        - Если боеприпас закончился, ассциированные с ним атаки убираются.
        """
        if attack_dict.get('ammo'):
            if attack_dict.get('ammo_type') and isinstance(attack_dict.get('ammo_type'), str):
                ammo_type = attack_dict.get('ammo_type')
            else:
                ammo_type = attack_dict.get('weapon_of_choice')
            if ammo_type in self.equipment_weapon:
                self.drop_item(ammo_type)
            for attack_choice, attack_dict in self.attacks.items():
                if ammo_type and ammo_type == attack_dict.get('ammo_type')\
                        or ammo_type == attack_dict.get('weapon_of_choice')\
                        and attack_dict.get('ammo'):
                    attack_dict['ammo'] -= 1
                    if attack_dict['ammo'] == 0:
                        for soldier in metadict_soldiers.values():
                            if ammo_type in soldier.equipment_weapon\
                                    and not soldier.defeat\
                                    and not soldier.near_enemies\
                                    and not soldier.help_action\
                                    and soldier.uuid != self.uuid\
                                    and soldier.ally_side == self.ally_side\
                                    and soldier.equipment_weapon[ammo_type] > 0:
                                # Союзник передаёт боеприпасы бойцу:
                                soldier.help_action = True
                                for attack_choice, attack_dict in self.attacks.items():
                                    if ammo_type == attack_dict.get('ammo_type')\
                                            or ammo_type == attack_dict.get('weapon_of_choice'):
                                        attack_dict['ammo'] += soldier.equipment_weapon[ammo_type]
                                soldier.unset_weapon(attack_dict.get('weapon_of_choice'), ammo_type)
                                break
                        else:
                            self.unset_weapon(attack_dict.get('weapon_of_choice'), ammo_type)
                            break

    def unset_weapon(self, weapon_type, ammo_type = None, disarm = False):
        """Убираем оружие, для которого закончились боеприпасы.
        
        Скорость бойца при этом пересчитывается.
        """
        unset_list = []
        for attack_choice, attack_dict in self.attacks.items():
            if not disarm:
                if attack_choice[-1] == weapon_type\
                        or attack_dict.get('ammo_type') == ammo_type:
                    unset_list.append(attack_choice)
            elif disarm:
                if attack_dict.get('weapon') == True\
                        and attack_dict.get('weapon_use')\
                        and attack_dict['weapon_use'] == weapon_type:
                    unset_list.append(attack_choice)
        if unset_list and len(unset_list) > 0:
            unset_list = list(set(unset_list))
            for attack in unset_list:
                attack_dict = self.attacks.pop(attack)
                if attack_dict.get('recharge'):
                    self.recharge_dict = attack_dict
                    self.recharge_dict['recharge'] = attack
                    self.recharge_dict['ammo'] = 1
            if ammo_type and ammo_type in self.equipment_weapon:
                self.drop_item(ammo_type, drop_all = True)
            if disarm:
                self.drop_item(weapon_type, drop_all = True)
            # Выбираем лучшее оружие из оставшегося:
            if not self.recharge_dict:
                self.attacks.update(self.modify_attacks_weapon_of_choice())

    def set_shield(self):
        """Щит в боевое положение.
        
        Во время стрельбы из лука и ходов с атаками двуручным оружием он висит на перевязи.
        """
        if self.armor['shield_use']\
                and self.shield_ready == False\
                and self.armor['armor_class_shield'] > 0:
            self.armor['armor_class'] += self.armor['armor_class_shield']
            self.armor['armor_class_armor_impact'] += self.armor['armor_class_shield']
            self.armor['armor_class_shield_impact'] += self.armor['armor_class_shield']
            self.shield_ready = True
            return True

    def unset_shield(self, disarm = False):
        """Отбрасываем щит на перевязь.
        
        Или отбираем у бойца щит вовсе.
        """
        if self.armor['shield_use']\
                and self.shield_ready == True\
                and self.armor['armor_class_shield'] > 0\
                or disarm == True:
            self.armor['armor_class'] -= self.armor['armor_class_shield']
            self.armor['armor_class_armor_impact'] -= self.armor['armor_class_shield']
            self.armor['armor_class_shield_impact'] -= self.armor['armor_class_shield']
            self.shield_ready = False
            if disarm:
                self.drop_item(self.armor['shield_use'])
                self.armor['shield_use'] = None
                self.armor['armor_class_shield'] = 0
            return True

    def set_shield_break(self):
        """Пилумы застревают в щитах, мешая их использовать.
    
        Homebrew:
        Каждое попадание пилума в щит, это -1 к его классу защиты.
        Бой сотня на сотню, 12-24 попаданий в щиты, это весомо.
        """
        if self.armor['shield_use']:
            self.armor['armor_class'] -= 1
            self.armor['armor_class_armor_impact'] -= 1
            self.armor['armor_class_shield_impact'] -= 1
            self.armor['armor_class_shield'] -= 1
            self.armor_class_shield = self.armor['armor_class_shield']
            if self.armor['armor_class_shield'] <= 0:
                self.armor_class_shield = 0
                self.armor['armor_class_shield'] = 0
                shield_type = self.armor['shield_use']
                self.armor['shield_use'] = None
                self.drop_item(shield_type)
            #print(self.ally_side, self.place, self.behavior, self.armor)

    def drop_item(self, item, number = 1, drop_all = False):
        """Теряем предмет. Запоминаем потерю.
        
        - Пересчитывается скорость и нагрузка.
        """
        if item in self.equipment_weapon\
                and self.equipment_weapon[item] > 0:
            if drop_all:
                number = self.equipment_weapon[item]
            self.equipment_weapon[item] -= number
            self.overload = self.calculate_overload()
            self.base_speed = self.overload['base_speed']
            # Запоминаем израсходованный предмет:
            if not item in self.drop_items_dict:
                self.drop_items_dict[item] = 1
            elif item in self.drop_items_dict:
                self.drop_items_dict[item] += 1
            return True
        else:
            return False

    def get_trophy(self, item, number = 1):
        """Словарь трофеев пополняется предметом.
        
        - Боекомплект пополняется за счёт поверженого врага.
        """
        if item in self.equipment_weapon\
                and self.equipment_weapon[item]\
                < self.metadict_chars[self.rank]['equipment_weapon'].get(item, 0):
            # Пополняется боекомплект:
            self.equipment_weapon[item] += number
            self.overload = self.calculate_overload()
            self.base_speed = self.overload['base_speed']
            # Обновляются атаки:
            self.attacks = self.takeoff_weapon()
            self.attacks.update(self.get_weapon())
            self.attacks.update(self.modify_attacks())
            self.attacks.update(self.modify_attacks_weapon_of_choice())
        else:
            # Забираем предмет как трофей:
            if not item in self.trophy_items_dict:
                self.trophy_items_dict[item] = number
            elif item in self.trophy_items_dict:
                self.trophy_items_dict[item] += number

    def spell_attack(self, attack_dict, enemy, metadict_soldiers, advantage = False, disadvantage = False):
        """Атака заклинанием.
        
        Вроде магической стрелы, которая всегда попадает,
        Или бьющего по местности огненного шара.
        """
        # У заклинаний тоже заканчиваются заряды:
        if attack_dict.get('ammo'):
            self.use_ammo(attack_dict, metadict_soldiers)
        damage_throw = dices.dice_throw_advantage(attack_dict['damage_dice'])
        damage_throw_mod = damage_throw + attack_dict.get('damage_mod',0)
        attack_result_dict = {
                'damage':damage_throw_mod,
                'damage_throw':damage_throw,
                'advantage':advantage,
                'disadvantage':disadvantage,
                'enemy_cover':enemy.cover,
                'enemy_distance':enemy.distance,
                'victim_side':enemy.side,
                'victim_type':enemy.type,
                'victim_uuid':enemy.uuid,
                'sender_uuid':self.uuid,
                }
        attack_result_dict.update(attack_dict)
        return attack_result_dict

    def take_attack(self, attack_choice, attack_dict, metadict_soldiers):
        """Боец реагирует на атаку.
        
        Возможности (все требуют действия-реакции):
        1) Protection от союзника (установить флажок заранее)
        2) Defensive_Duelist
        3) Перехват стрел монахом

        Также учитывается прикрытие местности (в долях от площади тела):
        https://www.dandwiki.com/wiki/5e_SRD:Cover
        1/2 cover -- +2 AC, +2 DEX sav
        3/2 cover -- +5 AC, +5 DEX sav
        """
        armor_dict = self.armor
        cover = attack_dict['enemy_cover']
        result = {
                'attack_choice':attack_choice,
                'clumsy_miss':False,
                'miss':False,
                'shield_impact':False,
                'armor_impact':False,
                'hit':False,
                'fatal_hit':False,
                'crit':False,
                }
        armor_class_no_impact = armor_dict['armor_class_no_impact']
        armor_class_shield_impact = armor_dict['armor_class_shield_impact']
        armor_class_armor_impact = armor_dict['armor_class_armor_impact']
        armor_class = armor_dict['armor_class']
        # Местность даёт прикрытие (особенно от лучников):
        # Кусты дают прикрытие на 1/2 +2 AC, баррикады на 3/4 +5 AC.
        savethrow_bonus_cover = 0
        if cover >= 4 and cover < 7:
            armor_class_no_impact += 2
            armor_class_shield_impact += 2
            armor_class_armor_impact += 2
            armor_class += 2
            savethrow_bonus_cover += 2
        elif cover >= 7:
            armor_class_no_impact += 5
            armor_class_shield_impact += 5
            armor_class_armor_impact += 5
            armor_class += 5
            savethrow_bonus_cover += 5
        attack_dict['savethrow_bonus_cover'] = savethrow_bonus_cover
        # Заклинание "Shield_of_Faith" даёт прекрасные +2 к AC.
        if 'shield_of_faith' in self.buffs:
            armor_class_no_impact += 2
            armor_class_shield_impact += 2
            armor_class_armor_impact += 2
            armor_class += 2
        # TODO: в отдельную функцию:
        # Учитываем реакцию Feat_Defensive_Duelist:
        if attack_choice[0] == 'close' or attack_choice[0] == 'reach':
            if self.class_features.get('Feat_Defensive_Duelist')\
                    and self.reaction == True\
                    and attack_dict['attack'] > armor_class\
                    and attack_dict['attack'] < armor_class + self.proficiency_bonus:
                armor_class_shield_impact += self.proficiency_bonus
                armor_class_armor_impact += self.proficiency_bonus
                armor_class += self.proficiency_bonus
                self.reaction = False
                # Всё работает, вывод можно убрать:
                if attack_dict['attack'] <= armor_class and not attack_dict['attack_crit']:
                    print('[+++] {0} {1} {2} reaction Def Duel {3}/{4} << {5}, atc {6} dmg {7}'.format(
                        self.ally_side, self.place, self.behavior,
                        armor_class, armor_dict['armor_class'],
                        attack_choice, attack_dict['attack'], attack_dict['damage']))
        # TODO: в отдельную функцию:
        # Реакцией срабатывает волшебный щит.
        if 'runes' in self.commands\
                and self.equipment_weapon.get('Rune of Shielding')\
                and self.reaction == True\
                and not self.shield:
            if attack_dict.get('attack') and attack_dict['attack'] > armor_class\
                    or attack_choice[-1] == 'Magic_Missile':
                self.drop_item('Rune of Shielding')
                self.reaction = False
                self.shield = True
        elif hasattr(self, 'spells') and self.reaction == True and not self.shield:
            if attack_dict.get('attack') and attack_dict['attack'] > armor_class\
                    or attack_choice[-1] == 'Magic_Missile':
                for spell, spell_dict in self.spells.items():
                    if spell_dict.get('effect') and spell_dict['effect'] == 'shield':
                        spell_dict = self.spells_generator.use_spell(spell)
                        # Магическая защита восстанавливается или создаётся:
                        if self.class_features.get('Arcane_Ward'):
                            if self.arcane_ward and not self.bonus_hitpoints:
                                self.bonus_hitpoints = int(spell_dict['spell_level'][0]) * 2
                            elif not self.arcane_ward:
                                self.bonus_hitpoints = self.level * 2 + self.mods['intelligence']
                        self.reaction = False
                        self.shield = True
                        break
        # Заклинание 'Shield' даёт впечатляющие +5 к AC на один раунд и защищает от волшебных стрел.
        if self.shield:
            armor_class_no_impact += 5
            armor_class_shield_impact += 5
            armor_class_armor_impact += 5
            armor_class += 5
            if attack_choice[-1] == 'Magic_Missile':
                attack_dict['direct_hit'] = False
            # Вывод результата:
            if attack_dict.get('attack', 0) <= armor_class\
                    and attack_dict.get('attack',0) > (armor_class - 5)\
                    and not attack_dict['attack_crit']:
                print('[+++] {0} {1} {2} reaction Shield {3}/{4} << {5}, atc {6} dmg {7}'.format(
                    self.ally_side, self.place, self.behavior,
                    armor_class, armor_dict['armor_class'],
                    attack_choice, attack_dict['attack'], attack_dict['damage']))
        # TODO: в отдельную функцию:
        # Лошадка может попросить защиты у хозяина с Feat_Mounted_Combatant:
        if attack_dict.get('attack'):
            if self.behavior == 'mount' and self.hitpoints < self.hitpoints_max / 4\
                    and hasattr(self, 'master_uuid') and self.master_uuid in metadict_soldiers:
                master = metadict_soldiers[self.master_uuid]
                near_allies_uuid = [ally[-1] for ally in self.near_allies]
                if master.uuid in near_allies_uuid\
                        and master.class_features.get('Feat_Mounted_Combatant')\
                        and master.hitpoints > master.hitpoints_max / 2:
                    attack_result = master.take_attack(
                            attack_choice, attack_dict, metadict_soldiers)
                    return attack_result
        if attack_dict.get('attack') and not attack_dict.get('direct_hit'):
            if attack_dict['attack_crit'] == True:
                result['hit'] = True
                result['crit'] = True
            elif attack_dict['attack'] >= armor_class:
                result['hit'] = True
            elif attack_dict['attack'] < armor_class_no_impact:
                result['miss'] = True
            elif attack_dict['attack'] < armor_class_shield_impact:
                result['shield_impact'] = True
            elif attack_dict['attack'] < armor_class_armor_impact:
                result['armor_impact'] = True
            elif attack_dict['attack'] <= 0 or attack_dict['attack_loss']:
                result['clumsy_miss'] = True
        elif attack_dict.get('direct_hit'):
            result['hit'] = True
        # Пилумы застревают в щитах:
        if result['shield_impact'] and armor_dict.get('shield_use'):
            if attack_dict.get('shield_breaker'):
                self.set_shield_break()
            if attack_dict.get('shield_breaker_absolute'):
                self.set_shield_break()
                self.set_shield_break()
        # Если атака прошла, переходим к расчёту ранений:
        attack_dict.update(result)
        if attack_dict['hit']:
            enemy_soldier = metadict_soldiers[attack_dict['sender_uuid']]
            if enemy_soldier.class_features.get('Stunning_Strike'):
                # enemy_soldier -- атакующий монах; 'self' -- получающий удар боец.
                stunned_difficult = enemy_soldier.set_stunnign_strike(self, attack_dict)
                stunned = False
                if stunned_difficult:
                    stunned = self.set_stunned(stunned_difficult)
                    if stunned:
                        print('[+++] {side_1}, {c1} {s} STUNNED >> {side_2} {c2} {e}'.format(
                            side_1 = enemy_soldier.ally_side,
                            c1 = enemy_soldier.place,
                            s = enemy_soldier.behavior,
                            side_2 = self.ally_side,
                            c2 = self.place,
                            e = self.behavior,
                            ))
            # TODO: способность не используется из-за предпочтения захватов.
            # ------------------------------------------------------------
            # Монахи сначала пытаются сбить с ног. Сбивание, захват, удары.
            # Выбивание реакции тем не менее полезно, если враг щитовик.
            # ------------------------------------------------------------
            # Атака монаха может сбить с ног:
            elif 'Open_Hand_Technique' in attack_dict and self.prone == False:
                attack_dict['fall_prone'] = self.set_fall_prone(enemy_soldier)
            # Или лишить реакции:
            elif 'Open_Hand_Technique' in attack_dict and self.prone == True:
                self.reaction = False
            attack_dict = self.take_damage(attack_choice, attack_dict, metadict_soldiers)
        return attack_dict

    def take_damage(self, attack_choice, attack_dict, metadict_soldiers):
        """Боец реагирует на повреждения.
        
        По правилам DnD 5.0:
        - Ранен на 100% хитов -- потеря сознания, борьба за жизнь.
        - Ранен на 200% от макс. числа хитов -- мгновенная смерть.
        """
        enemy_soldier = metadict_soldiers[attack_dict['sender_uuid']]
        damage = attack_dict['damage']
        # Урон предметам от осадных монстров удваивается:
        if attack_dict.get('weapon_type') and 'siege' in attack_dict['weapon_type']\
                and self.__dict__.get('mechanism'):
            damage *= 2
        # Удачный спасбросок может уполовинить урон:
        if attack_dict.get('savethrow') and not self.__dict__.get('savethrow_autofall'):
            savethrow_ability = attack_dict['savethrow_ability']
            # Помеха врага -- преимущество нам:
            advantage = attack_dict['disadvantage']
            disadvantage = attack_dict['advantage']
            if savethrow_ability == 'dexterity':
                if self.dodge_action or self.class_features.get('Danger_Sense'):
                    advantage = True
                if self.restained:
                    disadvantage = True
            damage_difficul = attack_dict.get('spell_save_DC', attack_dict.get('attack_throw'))
            damage_savethrow = dices.dice_throw_advantage('1d20', advantage, disadvantage)\
                    + self.saves[savethrow_ability]
            # Заклинание Sacred_Flame игнорирует бонус укрытия к спасброскам ловкости:
            if savethrow_ability == 'dexterity' and not attack_dict.get('ignore_cover'):
                damage_savethrow += attack_dict['savethrow_bonus_cover']
            # Заклинание Bless усиливает спасброски:
            if 'bless' in self.buffs:
                damage_savethrow += dices.dice_throw_advantage('1d4')
            # Bardic_Inspiration усиливает спасбросок:
            if 'bardic_inspiration' in self.buffs\
                    and damage_savethrow < damage_difficul\
                    and not damage_savethrow + self.buffs['bardic_inspiration'] < damage_difficul:
                damage_savethrow += self.buffs.pop('bardic_inspiration',0)
            if damage_savethrow >= damage_difficul\
                    and not self.stunned and not self.sleep:
                damage = round(damage / 2)
                if attack_dict.get('savethrow_all'):
                    attack_dict['hit'] = False
                    damage = 0
                elif self.class_features.get('Evasion'):
                    attack_dict['hit'] = False
                    damage = 0
            # Увёртливые воры и монахи всё равно уклоняются:
            elif damage_savethrow < damage_difficul\
                    and self.class_features.get('Evasion'):
                damage = round(damage / 2)
        # Крупные объекты (стены, корабли) имеют порог урона:
        if self.__dict__.get('ignore_damage'):
            damage -= self.ignore_damage
        # Умелые бойцы получают меньше урона в тяжёлой броне:
        if self.class_features.get('Feat_Heavy_Armor_Master'):
            if attack_dict['damage_type'] == 'bludgeoning'\
                    or attack_dict['damage_type'] == 'piercing'\
                    or attack_dict['damage_type'] == 'slashing':
                damage -= 3
        # Плуты ослабляют атаки за счёт реакции (это срабатывает до сопротивляемости урону):
        # Uncanny_Dodge срабатывает только против ударов с броском атаки:
        elif self.class_features.get('Uncanny_Dodge') and self.reaction and attack_dict.get('attack'):
            damage = round(damage * 0.5)
        # Homebrew, руна с Absorb_Elements:
        if not attack_dict['damage_type'] in self.resistance:
            if 'runes' in self.commands\
                    and self.equipment_weapon.get('Rune of Absorbtion')\
                    and self.reaction == True:
                absorb_list = self.metadict_items['Rune of Absorbtion']['absorb_damage_type']
                if attack_dict['damage_type'] in absorb_list:
                    self.reaction = False
                    self.drop_item('Rune of Absorbtion')
                    spell_dict = dict(self.metadict_items['Rune of Absorbtion'])
                    spell_dict['damage_type'] = attack_dict['damage_type']
                    self.resistance.append(attack_dict['damage_type'])
                    self.damage_absorbed = spell_dict
            # Заклинание Absorb_Elements спасает жизни (особенно рейнджерам):
            elif hasattr(self, 'spells') and self.reaction == True:
                for spell, spell_dict in self.spells.items():
                    if spell_dict.get('effect') and spell_dict['effect'] == 'absorb'\
                            and attack_dict['damage_type'] in spell_dict['absorb_damage_type']:
                        self.reaction = False
                        spell_dict = dict(self.spells_generator.use_spell(spell))
                        spell_dict['damage_type'] = attack_dict['damage_type']
                        self.resistance.append(attack_dict['damage_type'])
                        self.damage_absorbed = spell_dict
                        #print(self.resistance, damage, self.hitpoints_max)
                        break
        # Иммунитет к видам урона.
        # Урон от магического оружия преодолевает иммунитет.
        if attack_dict['damage_type'] in self.immunity:
            if attack_dict.get('weapon_type') and 'magic' in attack_dict['weapon_type']:
                damage = damage
            else:
                damage = 0
        # Сопротивляемость к видам урона.
        # Урон от магического оружия преодолевает сопротивляемость.
        elif attack_dict['damage_type'] in self.resistance:
            if enemy_soldier.class_features.get('Feat_Elemental_Adept') == attack_dict['damage_type']:
                damage = damage
            elif attack_dict.get('weapon_type') and 'magic' in attack_dict['weapon_type']:
                damage = damage
            else:
                damage = round(damage * 0.5)
        # Уязвимость к видам урона:
        elif attack_dict['damage_type'] in self.vultenability:
            damage = round(damage * 2)
        # Бонусные хиты от Feat_Inspiring_Leader и подобного:
        if self.bonus_hitpoints and self.bonus_hitpoints > 0:
            shield_of_bravery = self.bonus_hitpoints
            self.bonus_hitpoints -= damage
            damage = damage - shield_of_bravery
            if self.bonus_hitpoints < 0:
                self.bonus_hitpoints = 0
            if damage < 0:
                attack_dict['bonus_hitpoints_damage'] = damage + shield_of_bravery
            else:
                attack_dict['bonus_hitpoints_damage'] = shield_of_bravery
        # Отражение/перехват стрел монахом (15-25 срабатываний за бой с лучниками):
        # https://www.dandwiki.com/wiki/5e_SRD:Monk#Deflect_Missiles
        if attack_choice[0] == 'throw' or attack_choice[0] == 'ranged' or attack_choice[0] == 'volley':
            if self.class_features.get('Deflect_Missiles') and self.reaction == True:
                damage_deflect = dices.dice_throw('1d10') + self.mods['dexterity'] + self.level
                damage -= damage_deflect
                self.reaction = False
                print('[+++] {0} {1} {2} reaction Deflect {3}/{4} << {5} atc {6} dmg {7}'.format(
                    self.ally_side, self.place, self.behavior,
                    damage, attack_dict['damage'],
                    attack_choice, attack_dict['attack'], attack_dict['damage']))
        # Прирование мастера боевых искусств:
        if attack_choice[0] == 'close' or attack_choice[0] == 'reach':
            if self.class_features.get('Parry') and self.superiority_dices and self.reaction == True:
                damage_deflect = dices.dice_throw(self.superiority_dice)\
                        + self.mods['dexterity']
                damage -= damage_deflect
                self.reaction = False
                print('{0} {1} {2} {3} crit {4} damage {5} reaction parry -{6}'.format(
                    self.ally_side, self.place, self.behavior,
                    attack_choice, attack_dict['attack_crit'],
                    attack_dict['damage'], damage_deflect))
        # Скажем "нет" лечебным атакам:
        if damage < 0:
            damage = 0
        self.set_hitpoints(damage = damage)
        attack_dict['damage'] = damage
        # Спящий просыпается, если ранен:
        if damage and self.sleep:
            self.sleep_timer = 0
            self.sleep = False
        # Стойкость нежити (зомби не так-то просто убить):
        if self.class_features.get('Undead_Fortitude') and self.hitpoints <= 0\
                and not attack_dict.get('attack_crit')\
                and attack_dict['damage_type'] != 'radiant':
            destruction_difficul = 5 + damage
            destruction_saving_throw = dices.dice_throw_advantage('1d20') + self.saves['constitution']
            if destruction_saving_throw >= destruction_difficul:
                self.hitpoints = 1
        # Показываем, если командиру достаётся:
        if self.level >= 5:
            print('[!!!] {side}, {c1} {s} {w} >>>> {c2} {e}, crit {c} dmg {d}'.format(
                side = enemy_soldier.ally_side,
                s = enemy_soldier.behavior,
                e = self.behavior,
                c1 = enemy_soldier.place,
                c2 = self.place,
                w = attack_choice,
                c = attack_dict['crit'],
                d = damage,
                ))
            #print('{0} {1} {2} injured {3} crit {4} dmg {5} hp {6}/{7}'.format(
            #    self.ally_side, self.place, self.rank,
            #    attack_choice, attack_dict['attack_crit'],
            #    attack_dict['damage'], self.hitpoints, self.hitpoints_max))
        if damage > 0:
            self.trauma_damage_type = attack_dict['damage_type']
            if self.concentration:
                self.set_concentration_break(difficult = round(damage / 2))
        if self.hitpoints <= 0 and damage > 0 and not self.defeat:
            attack_dict['fatal_hit'] = True
        return attack_dict

# ----
# Опыт за победу

    def set_victory_and_enemy_defeat(self, enemy_soldier):
        """Боец получает опыт за победу.
        
        - Колдун с Dark_One\'s_Blessing получает бонусные хиты:
        """
        # TODO: добавь трофеи бойца.
        # ------------------------------------------------------------
        # Вражеское снаряжение, если враг схвачен или убит.
        # Или если враг не имеет рядом союзников, способных его вытащить.
        # ------------------------------------------------------------
        # Учитывается только первая победа, а не добивание:
        if not enemy_soldier.defeat and not enemy_soldier.fall:
            self.victories += 1
            enemy_soldier.defeats += 1
            self.experience += enemy_soldier.get_experience()
            # Список побед:
            key = enemy_soldier.rank
            if not key in self.victories_dict:
                self.victories_dict[key] = 1
            elif key in self.victories_dict:
                self.victories_dict[key] += 1
        # Колдун с Dark_One\'s_Blessing получает бонусные хиты:
        if self.class_features.get('Dark_One\'s_Blessing'):
            bonus_hitpoints_bless = self.mods['charisma'] + self.level
            if bonus_hitpoints_bless > self.bonus_hitpoints:
                self.set_hitpoints(bonus_hitpoints = bonus_hitpoints_bless)
                #print('{0} {1} temp_hp {2}'.format(
                #    self.ally_side, self.rank, bonus_hitpoints_bless))
        # Противник падает:
        enemy_soldier.defeat = True
        enemy_soldier.prone = True
        enemy_soldier.fall = True
        # Противник лишается действий и реакции:
        # TODO: Создай для этого функцию set_incapacitated
        # Не забудь, что неподвижный теряет dodge_action, если имел.
        # https://www.dandwiki.com/wiki/5e_SRD:Conditions#Incapacitated
        enemy_soldier.ready_action = False
        enemy_soldier.battle_action = False
        enemy_soldier.bonus_action = False
        enemy_soldier.reaction = False
        # Противник теряет концентрацию:
        if enemy_soldier.concentration:
            enemy_soldier.set_concentration_break(autofail = True)
        # У схваченного трофеят всё снаряжение:
        if enemy_soldier.grappled or not enemy_soldier.near_allies and enemy_soldier.near_enemies:
            for item, number in enemy_soldier.equipment_weapon.items():
                if number > 0:
                    self.get_trophy(item, number)
                    enemy_soldier.drop_item(item, number)
        # Оружие и щит выпадают из рук:
        if enemy_soldier.shield_ready:
            enemy_soldier.unset_shield(disarm = True)
        if enemy_soldier.weapon_ready:
            enemy_soldier.unset_weapon(enemy_soldier.weapon_ready, disarm = True)
