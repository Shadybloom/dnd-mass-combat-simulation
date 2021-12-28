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

    def set_hitpoints(self, damage = None, heal = None,
            bonus_hitpoints = None, max_hitpoints = None):
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
        if damage and damage > 0:
            self.hitpoints -= damage
        if heal:
            hitpoints_damage = self.hitpoints_max - self.hitpoints
            if heal > hitpoints_damage:
                heal = hitpoints_damage
            self.hitpoints += heal
            self.hitpoints_heal += heal
        if bonus_hitpoints:
            self.bonus_hitpoints = bonus_hitpoints
        # Изменённый максимум хитов, например заклинанием Aid:
        # Бэкап хитов хранится в self.hitpoints_max_backup
        if max_hitpoints:
            self.hitpoints_max = max_hitpoints
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
        if self.class_features.get('Feat_Inspiring_Leader'):
            self.inspiring_leader = True
        if self.proficiency.get('ki_points_max'):
            self.ki_points = self.proficiency['ki_points_max']
        if self.class_features.get('Martial_Archetype_Battlemaster')\
                or self.class_features.get('Feat_Martial_Adept'):
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
        # Все начинают бой под Dodge_Action:
        #self.dodge_action = True
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
        # Скастованные заклинания:
        # Для таймера в clear_spells.
        if not hasattr(self, 'spells_active'):
            self.spells_active = {}
        # Благотворные и вредные эффекты:
        if not hasattr(self, 'buffs'):
            self.buffs = {}
        if not hasattr(self, 'debuffs'):
            self.debuffs = {}
        if not hasattr(self, 'concentration'):
            self.concentration = False
        # Общие для всех параметры:
        self.stable = True
        self.immunity = []
        self.resistance = []
        self.vultenability = []
        self.defeat = False
        self.escape = False
        self.prone = False
        self.kneel = False
        self.stunned = False
        self.paralyzed = False
        self.grappled = False
        self.restrained = False
        self.help_action = False
        self.killer_mark = False
        self.reckless_attack = False
        self.dodge_action = False
        # Убираем окружение:
        self.danger = 0
        self.near_zone = [ ]
        self.near_allies = [ ]
        self.near_enemies = [ ]
        # Долговременные параметры:
        self.petrified = False
        # Эффекты заклинаний:
        self.blink = False
        self.fear = False
        self.fear_source = None
        self.damage_absorbed = None
        # Словарь ранений (disabled)
        if not hasattr(self, 'traumas_dict'):
            self.traumas_dict = {}
        # Словарь трофеев:
        if not hasattr(self, 'trophy_items_dict'):
            self.trophy_items_dict = {}
        # Словарь израсходованного снаряжения:
        if not hasattr(self, 'drop_items_dict'):
            self.drop_items_dict = {}
        # Словарь использованных заклинаний:
        if not hasattr(self, 'drop_spells_dict'):
            self.drop_spells_dict = {}
        # Словарь использованных способностей
        if not hasattr(self, 'drop_actions_dict'):
            self.drop_actions_dict = {}
        # Оружие в руках:
        if not hasattr(self, 'weapon_ready'):
            self.weapon_ready = None
        # Парное оружие в защитной позиции:
        if not hasattr(self, 'shield_ready_dual_wielder'):
            self.shield_ready_dual_wielder = False
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
            self.metadict_recharge = {}
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
        if not hasattr(self, 'death'):
            self.death = False
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
            if self.class_features.get('Martial_Archetype_Battlemaster')\
                    and not hasattr(self, 'superiority_dices')\
                    or self.class_features.get('Feat_Martial_Adept')\
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
        if not self.stunned and not self.paralyzed\
                and not 'sleep' in self.debuffs:
            self.battle_action = True
            self.bonus_action = True
            self.reaction = True
            self.move_action = True
            self.move_pool = self.base_speed
            if self.help_action:
                self.help_action = False
                self.battle_action = False
        # Отключаем манёвры пршлого хода, работавшие за счёт battle_action
        self.disengage_action = False # это защита от провоцированных атак.
        self.dash_action = False # это ускорение до x2 скорости
        self.dodge_action = False # это disadvantage на атаки врагов и преимущество ловксоти
        # Тактика варвара, преимущество и себе, и врагам:
        self.reckless_attack = False
        # Щит возвращается в боевое положение (если в прошлом ходу использовалось двуручное оружие):
        if self.armor['shield_use'] and not self.shield_ready:
            self.set_shield()
        # Оружие Feat_Dual_Wielder в защитное положение:
        if not self.armor['shield_use'] and self.weapon_ready\
                and not self.shield_ready_dual_wielder:
            self.set_shield_dual_wielder()
        # Испуганный бросает спасброски против страха:
        if self.fear:
            self.fear = self.set_fear(self.fear_source, self.fear_difficult)
            #if self.fear:
            #    print('{side_1} {c1} {s} FEAR {fear}'.format(
            #        side_1 = self.ally_side,
            #        c1 = self.place,
            #        s = self.behavior,
            #        fear = self.fear
            #        ))
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
        elif self.grappled or self.restrained:
            self.move_action = False
            self.move_pool = 0
            if self.grappled:
                self.set_grapple_break()
            elif self.restrained:
                self.set_restained_break()
        # Упавший встаёт на ноги (если он не схвачен):
        elif self.prone and not self.grappled:
            self.stand_up()
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
        # Особенности монстров:
        # Перезарядка способности:
        if self.class_features.get('Recharge') and len(self.metadict_recharge) >= 1:
            recharge_throw = dices.dice_throw(self.class_features['Recharge_dice'])
            if recharge_throw in self.class_features['Recharge_numbers']:
                attack_choice = random.choice(list(self.metadict_recharge.keys()))
                attack_dict = self.metadict_recharge.pop(attack_choice)
                attack_dict['ammo'] = 1
                self.attacks[attack_choice] = attack_dict
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
        # TODO: Потихоньку переделывай функции:
        # Channel_Sacred_Weapon
        if self.sacred_weapon:
            if self.sacred_weapon_timer > 0:
                self.sacred_weapon_timer -= 1
            elif self.sacred_weapon_timer == 0:
                self.sacred_weapon = None

    def set_change_form(self, squad):
        """Друид меняет форму
        
        """
        if self.class_features.get('Wild_Shape_Form')\
                and self.class_features['Wild_Shape_Form'] in self.metadict_animals\
                and not self.wild_shape\
                and self.wild_shape_number > 0:
            if self.battle_action or self.bonus_action and self.class_features.get('Combat_Wild_Shape'):
                if self.class_features.get('Combat_Wild_Shape'):
                    self.bonus_action = False
                else:
                    self.battle_action = False
                # Сохраняем ссылку, чтобы восстановить:
                # Сохраняем старую форму, чтобы восстановить:
                squad = self.squad
                battle = self.battle
                metadict_soldiers = self.metadict_soldiers
                self.squad = None
                self.battle = None
                self.metadict_soldiers = None
                self.wild_shape = True
                self.wild_shape_number -= 1
                soldier.recon_near = []
                soldier.near_zone = []
                soldier.near_allies = []
                soldier.near_enemies = []
                old_form = copy.deepcopy(self.__dict__)
                # Создаём новую форму:
                animal_type = self.class_features['Wild_Shape_Form']
                self.levelup(animal_type, regen_spells = False)
                # Берём броню из старой формы, если это возможно:
                self.equipment_weapon = old_form['equipment_weapon']
                self.armor = self.takeoff_armor()
                self.armor.update(self.get_armor())
                # Сохранаяме старую форму:
                self.wild_shape_old_form = old_form
                # Хиты новой формы, это бонусные хиты:
                self.bonus_hitpoints = self.hitpoints
                self.hitpoints = self.wild_shape_old_form['hitpoints']
                self.hitpoints_max = self.wild_shape_old_form['hitpoints_max']
                # Базовая тактика остаётся прежней:
                self.behavior = self.wild_shape_old_form['behavior']
                # Восстанавливаем активные заклинания:
                self.buffs = self.wild_shape_old_form['buffs']
                self.debuffs = self.wild_shape_old_form['debuffs']
                self.spells_active = self.wild_shape_old_form['spells_active']
                # Восстанавливаем ссылки:
                self.squad = squad
                self.battle = battle
                self.metadict_soldiers = metadict_soldiers
                self.spells_generator.mage = self
                # Убираем заклинания:
                self.spells = {}

    def return_old_form(self, metadict_soldiers):
        """Друид возвращает облик человека.
        
        """
        squad = self.squad
        battle = self.battle
        metadict_soldiers = self.metadict_soldiers
        #hitpoints = self.wild_shape_old_form['hitpoints']
        hitpoints = self.hitpoints
        place = self.place
        self.__dict__ = copy.deepcopy(self.wild_shape_old_form)
        # Восстанавливаем ссылки:
        self.squad = squad
        self.battle = battle
        self.metadict_soldiers = metadict_soldiers
        self.spells_generator.mage = self
        self.hitpoints = hitpoints
        self.place = place
        self.wild_shape_old_form = None
        self.wild_shape = False

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

    def try_spellcast(self, spell_name, gen_spell = False, use_spell_slot = True, use_action = True):
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
                if not spell_choice and type(use_spell_slot) == str:
                    spell_choice = (use_spell_slot, spell_name)
                if not spell_choice and not use_spell_slot:
                    spell_choice = ('subspell', spell_name)
        if spell_choice:
            action = self.check_action_to_spellcast(spell_choice)
            if self.__dict__.get(action) or not action or not use_action:
                spell_dict = self.spells_generator.use_spell(spell_choice, gen_spell, use_spell_slot)
                if spell_dict:
                    spell_dict['spell_choice'] = spell_choice
                    self.set_concentration(spell_dict)
                    if use_action:
                        self.use_action_to_spellcast(spell_dict)
                    if use_spell_slot:
                        self.drop_spell(spell_choice)
                        #print(self.rank, self.drop_spells_dict)
                    return spell_dict

    def check_action_to_spellcast(self, spell_choice):
        """Заклинание требует действия. Какого именно?

        """
        spell_dict = self.spells_generator.get_spell_dict(spell_choice)
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
                self.drop_action(('action', 'Spellcast'))
                self.battle_action = False
            elif casting_time == 'bonus_action':
                self.drop_action(('bonus_action', 'Spellcast'))
                self.bonus_action = False
            elif casting_time == 'reaction':
                self.drop_action(('reaction', 'Spellcast'))
                self.reaction = False
            else:
                self.drop_action(('action', 'Spellcast'))
                self.battle_action = False
        else:
            self.drop_action(('action', 'Spellcast'))
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
        if spell_dict.get('ammo'):
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
        if self.class_features.get('Feat_War_Caster'):
            advantage = True
        if self.get_savethrow(difficult, ability, advantage, disadvantage, danger = True)\
                and not autofail:
            return False
        else:
            # Эти теги используются, чтобы снимать баффы с солдат:
            self.concentration['concentration_break'] = True
            self.concentration['concentration_timer'] = 0
            self.concentration['effect_timer'] = 0
            self.concentration = False
            return True

    def set_buff(self, spell_dict):
        """Солдат получает эффект заклинания.
        
        - Он исполняет функцию заклинания на себя.
        """
        effect = spell_dict['effect']
        if effect not in self.buffs:
            spell_dict = self.spells_generator.use_buff(spell_dict['spell_choice'], gen_spell = spell_dict)
            if spell_dict:
                return spell_dict

    def set_debuff(self, spell_dict):
        """Солдат получает эффект заклинания."""
        effect = spell_dict['effect']
        spell_dict = self.spells_generator.use_buff(spell_dict['spell_choice'], gen_spell = spell_dict)
        if spell_dict:
            return spell_dict

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

    def set_patient_defense(self):
        """Защитные приёмы монахов.
        
        Homebrew: Dodge_Action без расхода Ки, подобно cunning_action вора.
        В оригинале: Dodge_Action бонусным действием за счёт Ки, чего хватает только на 2 раунда.
        """
        if self.class_features.get('Patient_Defense'):
            #if hasattr(self, 'ki_points') and self.ki_points > 0 and self.bonus_action == True:
            #    self.ki_points -= 1
            #    self.drop_spell(('ki', 'Patient_Defense'))
            #    self.bonus_action = False
            #    self.dodge_action = True
            if self.bonus_action == True:
                self.drop_action(('bonus_action', 'Dodge_Action_Monk'))
                self.bonus_action = False
                self.dodge_action = True
                return True

    def set_step_of_the_wind_disengage(self):
        """Уклонение монаха."""
        # TODO: использование Ки пока что отключено. Нужно протестировать.
        if self.class_features.get('Step_of_the_Wind'):
            #if hasattr(self, 'ki_points') and self.ki_points > 0 and self.bonus_action == True:
            #    self.ki_points -= 1
            #    self.drop_spell(('ki', 'Step_of_the_Wind'))
            #    self.bonus_action = False
            #    self.disengage_action = True
            if self.bonus_action == True:
                self.drop_action(('bonus_action', 'Disengage_Action_Monk'))
                self.bonus_action = False
                self.disengage_action = True
                return True

    def set_cunning_action_defence(self):
        """Защитные приёмы вора."""
        if self.class_features.get('Cunning_Action'):
            if self.bonus_action == True:
                self.drop_action(('bonus_action', 'Dodge_Action_Rogue'))
                self.bonus_action = False
                self.dodge_action = True
                return True

    def set_cunning_action_disengage(self):
        """Уклонение вора."""
        if self.class_features.get('Cunning_Action'):
            if self.bonus_action == True:
                self.drop_action(('bonus_action', 'Disengage_Action_Rogue'))
                self.bonus_action = False
                self.disengage_action = True
                return True

    def set_cunning_action_dash(self):
        """Ускорение вора."""
        if self.class_features.get('Cunning_Action'):
            if self.bonus_action == True:
                self.drop_action(('bonus_action', 'Dash_Action_Rogue'))
                self.bonus_action = False
                self.dash_action = True
                return True

    def set_two_weapon_fighting(self, attack_choice):
        """Атака вторым оружием за счёт бонусного действия.
        
        - Если боец держал щит, то он его отбрасывает, чтобы атаковать вторым оружием.
        - Навык Fighting_Style_Two_Weapon_Fighting добавляет модификаторы урона к второму оружию.
        """
        attacks_chain_bonus = []
        if self.class_features.get('Fighting_Style_Two_Weapon_Fighting'):
            if not 'two_handed' in self.attacks[attack_choice]['weapon_type']\
                    and self.bonus_action == True:
                attack_list_slice = [key for key in self.attacks\
                        if 'Fighting_Style_Two_Weapon_Fighting' in self.attacks[key]['weapon_skills_use']\
                        and attack_choice[0] in self.attacks[key]['weapon_type']]
                if attack_list_slice:
                    self.unset_shield()
                    self.set_shield_dual_wielder()
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
                self.drop_spell(('ki', 'Flurry_of_Blows'))
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

    def use_stunning_strike(self, enemy_soldier):
        """Монах использует оглушающую атаку.

        - Если противник не оглушён.
        - Если есть на это свободные Ки.
        - Если противник достаточно опасен.
        
        Возвращает сложность спасброска.
        """
        if self.class_features.get('Stunning_Strike')\
                and hasattr(self, 'ki_points')\
                and self.ki_points > 0:
            self.ki_points -= 1
            self.drop_spell(('ki', 'Stunning_Strike'))
            stunned_difficult = 8 + self.proficiency_bonus + self.mods['wisdom']
            stunned = enemy_soldier.set_stunned(stunned_difficult)
            if stunned:
                #print('[+++] {side_1}, {c1} {s} STUNNED >> {side_2} {c2} {e}'.format(
                #    side_1 = self.ally_side,
                #    c1 = self.place,
                #    s = self.behavior,
                #    side_2 = enemy_soldier.ally_side,
                #    c2 = enemy_soldier.place,
                #    e = enemy_soldier.behavior,
                #    ))
                return True

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
        # Сортировка по уровню:
        near_enemies = list(reversed(sorted(near_enemies,key=lambda x: x.level)))
        self.near_enemies = near_enemies

    def set_near_allies(self, dict_recon):
        """Словарь союзников в радиусе 5 футов"""
        near_allies = [ ]
        for char in dict_recon.values():
            if char.side == self.ally_side and not char.uuid == self.uuid:
                near_allies.append(char)
        # Сортировка по уровню:
        near_allies = list(reversed(sorted(near_allies,key=lambda x: x.level)))
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
        #morality_mod = self.mods['charisma'] + self.proficiency_bonus
        self.danger = danger - squad.moral - self.saves['charisma']
        # Некоторые бойцы вовсе не чувствуют опасности. Нежить, например.
        if 'fearless' in self.commands:
            self.danger = 0
            self.escape = False
            return True
        # Герои храбрее обычных бойцов:
        if hasattr(self, 'hero') and self.hero == True:
            self.danger = danger - ((squad.moral + 1) * 6)
        # Варварам в ярости на всё чихать (кроме магии):
        # TODO: просто добавь им команду 'fearless'.
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
            self.drop_action(('reaction', 'Fighting_Style_Protection'))
            self.reaction = False
            return True
        else:
            return False

    def set_reckless_attack(self):
        """Безрассудная атака варавара.
        
        Преимущество к атаке на один ход, помеха к защите от врагов."""
        if self.class_features.get('Reckless_Attack') == True:
            self.drop_action(('feature', 'Reckless_Attack'))
            self.reckless_attack = True
            return True
        else:
            return False

    def set_action_surge(self):
        """Fighter может получить удвоенный ход."""
        # Только показываем, что двойной ход взят:
        if self.class_features.get('Action_Surge'):
            if self.proficiency['Action_Surge'] and self.bonus_action:
                self.drop_spell(('feature', 'Action_Surge'))
                self.proficiency['Action_Surge'] -= 1
                return True
            else:
                return False

    def use_dash_action(self, bonus_action = False):
        """Боец ускоряется.
        
        https://www.dandwiki.com/wiki/5e_SRD:Dash_Action
        """
        if self.bonus_action and self.class_features.get('Cunning_Action'):
            self.set_cunning_action_dash()
        elif bonus_action and self.bonus_action:
            self.drop_action(('bonus_action', 'Dash_Action'))
            self.bonus_action = False
            self.dash_action = True
        elif self.battle_action:
            self.drop_action(('action', 'Dash_Action'))
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
            self.drop_action(('action', 'Disengage_Action'))
            self.battle_action = False
            self.disengage_action = True
            return True

    def use_help_action(self, soldier, enemy_soldier):
        """Боец помогает союзнику
        
        """
        advantage = False
        if self.level < soldier.level or self.level == 1\
                or enemy_soldier.level > soldier.level\
                and self.level <= soldier.level:
        #if self.level < soldier.level or self.level == 1 and enemy_soldier.level > self.level:
            if not self.uuid == soldier.uuid\
                    and 'help' in self.commands\
                    and not self.danger >= self.battle.engage_danger\
                    and not 'dodge' in self.commands\
                    and not self.hero\
                    and not self.help_action:
                self.help_action = True
                advantage = True
                self.drop_action(('action', 'Help_Action_Attack'))
                #print('[+++] {s} {p} {b} HELP_ACTION --> {al_s} {al_p} {al_b} >> {en_s} {en_p} {en_b}'.format(
                #    s = self.ally_side,
                #    p = self.place,
                #    b = self.behavior,
                #    al_s = soldier.ally_side,
                #    al_p = soldier.place,
                #    al_b = soldier.behavior,
                #    en_s = enemy_soldier.ally_side,
                #    en_p = enemy_soldier.place,
                #    en_b = enemy_soldier.behavior))
                return advantage

    def use_reload_action(self):
        """Боец перезаряжает оружие со свойством "reload".
        
        Оружие требует перезарядки действием или бонусным действием.
        - Feat_Crossbow_Expert позволяет не тратя действия перезаряжать арбалеты.
        """
        if len(self.metadict_recharge) >= 1:
            recharge_success = False
            attack_choice = random.choice(list(self.metadict_recharge.keys()))
            # Бросок на вероятность перезарядки. Получилось/нет:
            if 'Recharge_dice' in self.metadict_recharge[attack_choice]:
                recharge_throw = dices.dice_throw(self.metadict_recharge[attack_choice]['Recharge_dice'])
                if recharge_throw in self.metadict_recharge[attack_choice]['Recharge_numbers']:
                    recharge_success = True
                else:
                    recharge_success = False
            # Перезарядка за одно действие:
            else:
                recharge_success = True
            # Опытные стрелки всегда перезаряжают успешно:
            if self.class_features.get('Feat_Firearms_Expert'):
                recharge_success = True
            # Опытные стрелки перезаряжают за счёт бонусного действия:
            if recharge_success and self.class_features.get('Feat_Firearms_Expert') and self.bonus_action:
                self.bonus_action = False
                self.drop_action(('bonus_action', 'Reload_Action_Success'))
                attack_dict = self.metadict_recharge.pop(attack_choice)
                if attack_dict.get('Recharge_magazine') and attack_dict.get('Recharge_magazine_max'):
                    attack_dict['Recharge_magazine'] = attack_dict['Recharge_magazine_max']
                self.attacks[attack_choice] = attack_dict
                return recharge_success
            # Если перезарядка успешна, восстанавливаем атаку:
            elif recharge_success and self.battle_action:
                self.battle_action = False
                self.drop_action(('action', 'Reload_Action_Success'))
                attack_dict = self.metadict_recharge.pop(attack_choice)
                if attack_dict.get('Recharge_magazine') and attack_dict.get('Recharge_magazine_max'):
                    attack_dict['Recharge_magazine'] = attack_dict['Recharge_magazine_max']
                self.attacks[attack_choice] = attack_dict
                return recharge_success
            elif not recharge_success and self.battle_action:
                self.battle_action = False
                self.drop_action(('action', 'Reload_Action_False'))
                return False
            else:
                return False

    def use_dodge_action(self):
        """Боец защищается.
        
        https://www.dandwiki.com/wiki/5e_SRD:Dodge_Action
        """
        dodge = False
        # Защитные приёмы плута и монаха за счёт бонусного действия:
        if self.bonus_action and self.class_features.get('Cunning_Action'):
            dodge = self.set_cunning_action_defence()
        elif self.bonus_action and self.class_features.get('Patient_Defense'):
            dodge = self.set_patient_defense()
        elif self.battle_action:
            self.drop_action(('action', 'Dodge_Action'))
            self.battle_action = False
            self.dodge_action = True
            dodge = True
        # homebrew, Feat_Durable превращает кость хитов в бонусные хиты:
        if dodge and self.class_features.get('Feat_Durable')\
                and self.bonus_hitpoints <= 0\
                and self.hit_dices_use < self.level:
            bonus_hitpoints = dices.dice_throw_advantage(self.hit_dice) + self.mods['constitution']
            if bonus_hitpoints <= self.mods['constitution'] * 2:
                bonus_hitpoints = self.mods['constitution'] * 2
            self.set_hitpoints(bonus_hitpoints = bonus_hitpoints)
            self.hit_dices_use += 1
        if dodge:
            return dodge

    def use_heal(self, use_minor_potion = False, use_action = True, gen_spell = True):
        """Боец лечит себя, если способен."""
        if self.__dict__.get('second_wind'):
            self.use_second_wind()
        elif self.__dict__.get('lay_on_hands'):
            self.use_lay_on_hands()
        elif 'potions' in self.commands:
            self.use_heal_potion(use_minor_potion, use_action, gen_spell)

    def use_heal_potion(self, use_minor_potion = False, use_action = True, gen_spell = True):
        """Боец лечится зельем."""
        spells_list = [
                'Cure_Wounds',
                'Regeneration',
                'Goodberry',
                ]
        if use_minor_potion:
            spells_list = ['Goodberry']
        for spell in spells_list:
            spell_dict = self.use_item(spell, gen_spell, use_action)
            if spell_dict:
                return spell_dict

    def use_second_wind(self):
        """Fighter может очухаться после ранения.
        
        https://www.dandwiki.com/wiki/5e_SRD:Fighter#Second_Wind
        """
        # TODO: можно использовать функцию заклинания Cure_Wounds.
        # Только отправить изменённый словарь.
        if self.class_features.get('Second_Wind'):
            if self.second_wind and self.bonus_action:
                second_wind_heal = dices.dice_throw('1d10') + self.level
                self.set_hitpoints(heal = second_wind_heal)
                self.drop_spell(('feature', 'Second_Wind'))
                self.bonus_action = False
                self.second_wind = False
                #print('{0} {1} {2} heal (second_wind): {3}'.format(
                #    self.ally_side, self.place, self.behavior, second_wind_heal))
                return True
            else:
                return False

    def use_lay_on_hands(self):
        """Паладин способен лечить себя и других:
        
        https://www.dandwiki.com/wiki/5e_SRD:Paladin#Lay_on_Hands
        """
        # TODO: перенеси в заклинания.
        if self.class_features.get('Lay_on_Hands'):
            if self.lay_on_hands and self.battle_action:
                lay_on_hands_heal = self.hitpoints_max - self.hitpoints 
                if lay_on_hands_heal > self.lay_on_hands:
                    lay_on_hands_heal = self.lay_on_hands
                self.drop_spell(('feature', 'Lay_on_Hands'))
                self.set_hitpoints(heal = lay_on_hands_heal)
                self.lay_on_hands = self.lay_on_hands - lay_on_hands_heal
                self.battle_action = False
                #print('{0} {1} {2} heal (lay_on_hands): {3}'.format(
                #    self.ally_side, self.place, self.behavior, lay_on_hands_heal))
                return True
            else:
                return False

    def first_aid(self, injured_ally):
        """Боец лечит раненого союзника зельем, или пытается перевязать.

        """
        self.help_action = True
        self.drop_action(('action', 'Help_Action_First_Aid'))
        injured_ally.use_heal_potion(use_action = False, gen_spell = True)
        if not injured_ally.stable:
            return self.first_aid_bandage(injured_ally)
        else:
            return True

    def first_aid_bandage(self, injured_ally,
            stabilizing_difficul = 10, advantage = False, disadvantage = False):
        """Боец пытается оказать первую помощь раненому.

        https://www.dandwiki.com/wiki/5e_SRD:Dropping_to_0_Hit_Points#Stabilizing_a_Creature
        """
        # TODO: Учти Feat_Healer, что даёт автоматический успех стабилизации. И набор лекаря.
        self.help_action = True
        stabilizing_throw = dices.dice_throw_advantage('1d20', advantage, disadvantage)\
                + self.saves['wisdom']
        if stabilizing_throw < stabilizing_difficul:
            return False
        else:
            injured_ally.stable = True
            return True

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
        if enemy_soldier.size == 'tiny' and self.size in ['medium', 'large', 'huge']\
                or enemy_soldier.size == 'small' and self.size in ['large', 'huge']\
                or enemy_soldier.size == 'medium' and self.size in ['huge']:
            return False
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
            self.restrained = True
            self.move_action = False
            self.move_pool = 0
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
        if self.get_savethrow(difficult, ability, advantage, disadvantage, danger = True):
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
            self.restrained = False
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
            self.stable = True
            return False
        # Тролли и прочие создания с регенерацией стабилизируются сами:
        # Их нельзя убить, уведя хиты в минусовой максимум. Только огнём.
        if self.class_features.get('Regeneration'):
            self.stable = True
            return False
        # Иначе борьба за жизнь, где всё в руках судьбя:
        advantage = False
        disadvantage = False
        # Homebrew: Помеха на спасброски от смерти от зелья с death_rage
        if 'death_rage' in self.buffs:
            disadvantage = True
        else:
            disadvantage = False
        if not self.stable == True and not self.death == True:
            # Играем в рулетку с мрачным жнецом:
            reaper_throw = dices.dice_throw_advantage('1d20', advantage, disadvantage)
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
            #print('{0} {1} {2} {3} hp {4}/{5} throw {6} result {7}:{8} stable {9} dead {10}'.format(
            #    self.ally_side, self.place, self.behavior, self.name,
            #    self.hitpoints, self.hitpoints_max,
            #    reaper_throw, self.death_save_success, self.death_save_loss,
            #    self.stable, self.death))

    def set_disabled(self, advantage = False, disadvantage = False,
            trauma_damage_type = None, death_trauma = False):
        """Тяжёлые раны калечат бойца.
        
        "Длительные травмы" из "Руководства мастера".
        """
        # Герои и офицеры реже получают серьёзные травмы.
        if not self.__dict__.get('mechanism'):
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

    def get_savethrow(self, difficult, ability,
            advantage = None, disadvantage = None, danger = False, bonus = 0):
        """Делаем спасбросок.

        Метка danger значит, что спасбросок опасный, тогда используем способности.
        
        - Учитываем преимущества к броскам характеристик.
        - И помехи к броскам характеристик.
        """
        if not advantage:
            advantage = self.check_savethrow_advantage(ability)
        if not disadvantage:
            disadvantage = self.check_savethrow_disadvantage(ability)
        savethrow_result = dices.dice_throw_advantage('1d20', advantage, disadvantage) + self.saves[ability]
        savethrow_result += self.get_savethrow_bonus(difficult, savethrow_result, ability, danger, bonus)
        if self.check_savethrow_autofail(ability):
            return False
        elif difficult <= savethrow_result:
            return True
        elif difficult > savethrow_result and danger\
                and self.class_features.get('Indomitable')\
                and self.proficiency.get('Indomitable'):
            # TODO: использование Indomitable перенеси в spells.
            self.proficiency['Indomitable'] -= 1
            self.drop_spell(('feature', 'Indomitable'))
            result = self.get_savethrow (difficult, ability, advantage, disadvantage, danger = False)
            return  result
        else:
            return False

    def get_savethrow_bonus(self, difficult, savethrow_result, ability, danger = False, bonus = 0):
        """Бонус к спасброскам от способностей класса.

        """
        if self.class_features.get('Remarkable_Athlete'):
            if ability not in self.dict_class_saves[self.char_class]:
                bonus += round(self.proficiency_bonus / 2)
        # Мастер щитов получает бонус AC щита к спасброскам ловкости:
        if self.class_features.get('Feat_Shield_Master') and ability == 'dexterity'\
                and self.shield_ready:
            bonus += self.armor['armor_class_shield']
        # Заклинание Bless усиливает спасброски:
        if 'bless' in self.buffs:
            bonus += dices.dice_throw_advantage('1d4')
        # Bardic_Inspiration усиливает спасбросок:
        if danger:
            if 'bardic_inspiration' in self.buffs\
                    and savethrow_result < difficult\
                    and not savethrow_result + self.buffs['bardic_inspiration']['inspiration_mod'] < difficult:
                bonus += self.buffs.pop('bardic_inspiration')['inspiration_mod']
        return bonus

    def check_savethrow_autofail(self, ability):
        """Проверка автопровала спасброска.
        
        - Ошеломлённый проваливает спасброски силы и ловкости.
        - Бессознательный проваливает спасброски силы и ловкости.
        - Парализованный проваливает спасброски силы и ловкости.
        - Окаменевший проваливает спасброски силы и ловкости.
        """
        if self.__dict__.get('savethrow_autofail'):
            return True
        elif ability == 'strength' or ability == 'dexterity':
            if 'sleep' in self.debuffs:
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
        elif ability == 'dexterity':
            if self.class_features.get('Danger_Sense'):
                return True
            if self.dodge_action:
                return True
        # Homebrew: преимущества к морали от храбрости командира:
        elif ability == 'charisma':
            if 'brave' in self.commands:
                return True

    def check_savethrow_disadvantage(self, ability):
        """Способности могут дать преимущество на спасбросок."""
        # TODO: уточни, включают ли "проверки характеристик" спасброски.
        # Отравление даёт помеху на проверки характеристик.
        if 'poisoned' in self.debuffs:
            return True
        elif ability == 'dexterity':
            if self.restrained:
                return True
        # Homebrew: помеха к морали из-за негодного командира:
        elif ability == 'charisma':
            if 'coward' in self.commands:
                return True

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

    def move(self, distance = 5, rough = False, terrain = None):
        """Боец двигается. Обычно на 5 футов (один тайл карты).
        
        Возможности:
        - Dash_Action -- двухкратное ускорение.
        """
        # TODO:
        # Добавь правило диагонального перемещения.
        # А заодно и направление движения в стиле север/юг.
        # -------------------------------------------------
        # Прежде чем двигаться встаём:
        if self.prone or self.kneel:
            self.stand_up(terrain)
        # dash_action -- удвоенная скорость.
        if self.dash_action:
            distance = distance / 2
        # Пересечённая местность -- удвоенные потери пула движения:
        if rough:
            self.move_pool -= distance * 2
        # Иначе нормальная скорость:
        else:
            self.move_pool -= distance
        if self.move_pool <= 0:
            self.move_action = False
        return True

    def stand_up(self, terrain = None):
        """Боец пытается встать.
        
        Если стоял на колене (перезарядка оружия) или был сбит с ног.
        """
        if not self.grappled and not self.paralyzed:
            # Упавший встаёт на ноги (если он не схвачен):
            if self.prone and self.move_pool >= 0:
                self.move_pool = self.move_pool / 2
                self.prone = False
                if terrain and 'prone' in terrain:
                    terrain.remove('prone')
            # Стоящий на колене встаёт на ноги:
            if self.kneel and self.move_pool >= 0:
                self.move_pool = self.move_pool - 5
                self.kneel = False
                if terrain and 'kneel' in terrain:
                    terrain.remove('kneel')

    def on_knee(self, terrain = None):
        """Боец встаёт на колено.
        
        Homebrew: поза для перезарядки арбалетов/мушкетов.
        Подобно prone, это даёт помеху к дальним атакам врага.
        Но преимущество к ближним атакам. Так что применять осторожно.
        """
        # Приседаем во время перезарядки, если возможно (это свободное действие):
        if terrain and not 'kneel' in terrain\
                and not self.kneel and not self.prone:
            self.drop_action(('free_action', 'On_Knee'))
            terrain.append('kneel')
            self.kneel = True

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
        # Сортировка врагов по уровню:
        near_enemies = list(reversed(sorted(near_enemies,key=lambda x: x.level)))
        # Выбор первого врага, который сильнейший/слабейший из списка угроз:
        for enemy_type in danger_list:
            for target in near_enemies:
                if target.type == enemy_type:
                    return target    

    def select_attack(self, squad, enemy, enemy_soldier, tile_size = 5, weather = None):
        """Боец выбирает атаку, уже зная врага.
        
        Смотрит по дистанции. Сначала выбирает ближние атаки, после дальние.
        """
        distance = enemy.distance
        enemy_cover = enemy.cover
        # Под водой минимальный радиус атаки для стрелкового/метательного оружия:
        if weather == 'underwater':
            attack_range_choice = 'attack_range'
        else:
            attack_range_choice = 'attack_range_max'
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
            # Если союзники рядом с точкой взрыва гранаты, выбираем другое оружие.
            throw_attack_dict = self.attacks[throw_attack]
            if 'spell_dict' in throw_attack_dict\
                    and throw_attack_dict['spell_dict'].get('zone')\
                    and not throw_attack_dict['spell_dict'].get('safe')\
                    and not len(enemy_soldier.near_enemies) == 0\
                    and 'carefull' in self.commands:
                pass
            # Метатли дротиков работают с максимальной дистанции:
            elif self.behavior == 'archer'\
                    and distance <= round(self.attacks[throw_attack][attack_range_choice] / tile_size):
                return throw_attack
            # Застрельщики с пилумами тоже могут метать издалека по команде:
            elif 'volley' in self.commands\
                    and distance <= round(self.attacks[throw_attack][attack_range_choice] / tile_size):
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
            # Лучники и егеря работают с максимальной дистанции:
            if self.behavior == 'archer'\
                    and distance <= round(self.attacks[ranged_attack][attack_range_choice] / tile_size):
                return ranged_attack
            # Линейная пехота подпускает врага для прицельного залпа, если таков приказ:
            elif 'aim' in self.commands\
                    and distance <= round(self.attacks[ranged_attack]['attack_range'] / tile_size):
                return ranged_attack
            # Все остальные тоже стреляют с предельной дистанции:
            elif self.behavior != 'archer'\
                    and distance <= round(self.attacks[ranged_attack][attack_range_choice] / tile_size):
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
        # Используем Sword_Burst только если врагов больше одного:
        if distance < 2 and 'cantrip' in [attack[0] for attack in self.spells]:
            spell_attack_list = [attack for attack in self.spells if attack[0] == 'cantrip'
                    and attack[1] == self.spells[attack]['spell_of_choice']
                    and self.spells[attack].get('effect',None) == 'burst']
            if spell_attack_list and len(self.near_enemies) > 1:
                for spell_attack in spell_attack_list:
                    if distance <= round(self.spells[spell_attack]['attack_range'] / tile_size):
                        return spell_attack
        # Используем Green_Flame_Blade:
        if distance < 2 and 'cantrip' in [attack[0] for attack in self.spells]:
            spell_attack_list = [attack for attack in self.spells if attack[0] == 'cantrip'
                    and attack[1] == self.spells[attack]['spell_of_choice']
                    and self.spells[attack].get('weapon_attack')]
            if spell_attack_list:
                for spell_attack in spell_attack_list:
                    if distance <= round(self.spells[spell_attack]['attack_range'] / tile_size):
                        return spell_attack

    def attack(self, attack_dict, attack_choice, enemy, metadict_soldiers,
            advantage = False, disadvantage = False):
        """Боец атакует (уже выбранной атакой).
        
        В выводе словарь атаки с числами атаки и урона.
        А также типом повреждений (piercing, slashing, bludgeoning)
        """
        enemy_soldier = metadict_soldiers[enemy.uuid]
        # Берём кость урона, чтобы не изменить её в словаре:
        damage_dice = attack_dict.get('damage_dice', None)
        # Оружие в руки:
        if attack_dict.get('weapon') and attack_dict.get('weapon_use'):
            self.weapon_ready = attack_dict.get('weapon_use')
        # TODO: перенеси в самый конец функции, чтобы работали бесконечные стрелы.
        # Используется боеприпас (стрела, дротик, яд для меча), если указан:
        if attack_dict.get('ammo'):
            self.use_ammo(attack_dict, metadict_soldiers)
        # Нельзя использовать два приёма баттлмастера за одну атаку:
        superiority_use = False
        # Боец с двуручным оружием не может использовать щит:
        # Но только в том раунде, в котором пользовался двуручным оружием.
        # В set_actions щит каждый раз возвращается в боевое положение.
        if attack_dict.get('weapon_type')\
                and 'two_handed' in attack_dict['weapon_type']\
                and self.armor['shield_use']:
            self.unset_shield()
        # Помеха к стрельбе на минимальной/максимальной дальности:
        if attack_dict.get('weapon_type') and attack_choice[0] == 'ranged':
            if not 'Sharpshooter' in attack_dict['weapon_skills_use']\
                    or not 'Firearms_Expert' in attack_dict['weapon_skills_use'] and enemy.distance <= 2:
                if enemy.distance <= 2:
                    disadvantage = True
                elif enemy.distance > round(attack_dict['attack_range'] / self.tile_size):
                    disadvantage = True
        # Homebrew: урон огнестрела уменьшается, если дальность выше предельной:
        # Также исчезает его свойство пробивать доспехи в modify_armor.
        if attack_dict.get('weapon_type') and 'firearm' in attack_dict.get('weapon_type')\
                and enemy.distance * self.tile_size > attack_dict['shoot_range']\
                and attack_choice[0] == 'volley':
            damage_dice = str(1) + damage_dice[1:]
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
                + self.buffs['bardic_inspiration']['inspiration_mod']:
            attack_throw_mod += self.buffs.pop('bardic_inspiration')['inspiration_mod']
        # Precision_Attack мастера боевых искусств:
        if self.class_features.get('Precision_Attack') and not superiority_use:
            superiority_dice_mid = round(int(self.superiority_dice[-1]) / 2)
            if self.superiority_dices\
                and enemy_soldier.armor['armor_class'] > attack_throw_mod\
                and not enemy_soldier.armor['armor_class'] > attack_throw_mod + superiority_dice_mid:
                attack_throw_mod += dices.dice_throw_advantage(self.superiority_dice)
                self.superiority_dices -= 1
                superiority_use = True
                self.drop_spell(('feature', 'Battlemaster_Precision_Attack'))
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
        damage_throw = dices.dice_throw_advantage(damage_dice,
                advantage = damage_throw_advantage, disadvantage = False, max_throw = sharpness)
        # Если атака критическая, бросаем кость урона дважды:
        # Если атака неудачная, то независимо от модификаторов результат нулевой:
        # Атаки по бессознательным вблизи всегда дают критическое попадание.
        if attack_throw >= crit_range\
                or attack_dict['attack_range'] <= 5 and 'sleep' in enemy_soldier.debuffs\
                or attack_dict['attack_range'] <= 5 and enemy_soldier.paralyzed:
            damage_throw = 0
            for throw in range(0, self.crit_multiplier):
                damage_throw += dices.dice_throw_advantage(damage_dice,
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
                        or attack_dict['attack_range'] <= 5 and 'sleep' in enemy_soldier.debuffs:
                    # Критический удар удваивает урон от скрытной атаки:
                    sneak_attack_throw = dices.dice_throw_advantage(self.proficiency['sneak_attack_dice'],
                            advantage = False, disadvantage = False, max_throw = sharpness)
                    damage_throw += sneak_attack_throw
        # Наконец, выводим общий урон:
        damage_throw_mod = damage_throw + attack_dict['damage_mod']
        if damage_throw_mod < 0:
            damage_throw_mod = 0
        # Бонус урона от ярости варвара:
        if self.class_features.get('Rage') and self.rage:
            if attack_choice[0] == 'close' or attack_choice[0] == 'reach':
                damage_throw_mod += self.rage_damage
        # Мастер тяжёлого оружия усиливает удар за счёт точности (если защита врага слаба):
        if attack_dict.get('weapon_skills_use'):
            if 'Feat_Great_Weapon_Master' in attack_dict['weapon_skills_use']:
                if enemy_soldier.armor['armor_class'] <= attack_dict['attack_mod'] + 10\
                        and enemy_soldier.hitpoints > damage_throw_mod\
                        and advantage and not disadvantage\
                        or enemy_soldier.__dict__.get('mechanism')\
                        and enemy_soldier.__dict__.get('ignore_damage')\
                        or 'kill' in self.commands\
                        and not disadvantage:
                    damage_throw_mod += 10
                    attack_throw_mod -=5
            # Снайпер тоже способен усилить урон за счёт точности:
            if 'Sharpshooter' in attack_dict['weapon_skills_use']:
                if enemy_soldier.armor['armor_class'] <= attack_dict['attack_mod'] + 10\
                        and enemy_soldier.hitpoints > damage_throw_mod\
                        and advantage and not disadvantage\
                        or 'kill' in self.commands\
                        and not disadvantage:
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
                self.drop_spell(('feature', 'Battlemaster_Menacing_Attack'))
                #if fear:
                #    print('[+++] {side_1}, {c1} {s} FEAR >> {side_2} {c2} {e}'.format(
                #        side_1 = self.ally_side,
                #        c1 = self.place,
                #        s = self.behavior,
                #        side_2 = enemy_soldier.ally_side,
                #        c2 = enemy_soldier.place,
                #        e = enemy_soldier.behavior,
                #        ))
        attack_result_dict = {
                'damage':damage_throw_mod,
                'attack':attack_throw_mod,
                'damage_throw':damage_throw,
                'attack_throw':attack_throw,
                'attack_crit':attack_crit,
                'attack_loss':attack_loss,
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

    def use_ammo(self, attack_dict, metadict_soldiers):
        """Расходуем боеприпас.

        - Если боеприпас есть в отряде, союзный солдат передаёт его.
        - Если боеприпас закончился, ассциированные с ним атаки убираются.
        """
        # Используем боеприпас:
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
                    # Если боеприпасы закончились, просим у другого бойца:
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
                                    if attack_dict.get('ammo') == 0:
                                        if ammo_type == attack_dict.get('ammo_type')\
                                                or ammo_type == attack_dict.get('weapon_of_choice'):
                                            attack_dict['ammo'] += soldier.equipment_weapon[ammo_type]
                                self.equipment_weapon[ammo_type] += soldier.equipment_weapon[ammo_type]
                                soldier.unset_weapon(attack_dict.get('weapon_of_choice'), ammo_type)
                                soldier.drop_item(ammo_type, transfet_item = True)
                                break
                        else:
                            self.unset_weapon(attack_dict.get('weapon_of_choice'), ammo_type)
                            break
            # Атака убирается из списка доступных, если нужна перезарядка:
            if attack_dict.get('recharge')\
                    or attack_dict.get('weapon_type')\
                    and 'reload' in attack_dict['weapon_type']:
                # Магазинные винтовки:
                if attack_dict.get('Recharge_magazine')\
                        and attack_dict.get('Recharge_magazine') > 0:
                    attack_dict['Recharge_magazine'] -= 1
                else:
                    self.unset_weapon(attack_dict.get('weapon_of_choice'))

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
                if attack_dict.get('recharge')\
                        or attack_dict.get('weapon_type')\
                        and 'reload' in attack_dict['weapon_type']:
                    self.metadict_recharge[attack] = attack_dict
            if ammo_type and ammo_type in self.equipment_weapon:
                self.drop_item(ammo_type, drop_all = True)
            if disarm:
                self.drop_item(weapon_type, drop_all = True)
            # Выбираем лучшее оружие из оставшегося:
            if not len(self.metadict_recharge) >= 1:
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

    def set_shield_dual_wielder(self):
        """Второе оружие в защитное положение.
        
        Feat_Dual_Wielder даёт +1 AC, когда оружие во второй руке.
        """
        if self.class_features.get('Feat_Dual_Wielder')\
                and not self.shield_ready and not self.shield_ready_dual_wielder:
            self.armor['armor_class'] += 1
            self.armor['armor_class_armor_impact'] += 1
            self.armor['armor_class_shield_impact'] += 1
            self.shield_ready_dual_wielder = True
            return True

    def unset_shield(self, disarm = False, dual_wielder = False):
        """Отбрасываем щит на перевязь.
        
        Или отбираем у бойца щит вовсе.
        """
        if self.armor['shield_use']\
                and self.shield_ready == True\
                and self.armor['armor_class_shield'] > 0\
                or self.shield_ready_dual_wielder == True\
                or disarm == True:
            if self.shield_ready:
                self.armor['armor_class'] -= self.armor['armor_class_shield']
                self.armor['armor_class_armor_impact'] -= self.armor['armor_class_shield']
                self.armor['armor_class_shield_impact'] -= self.armor['armor_class_shield']
                self.shield_ready = False
                if disarm:
                    self.drop_item(self.armor['shield_use'])
                    self.armor['shield_use'] = None
                    self.armor['armor_class_shield'] = 0
            if self.shield_ready_dual_wielder and dual_wielder\
                    or self.shield_ready_dual_wielder and disarm:
                self.armor['armor_class'] -= 1
                self.armor['armor_class_armor_impact'] -= 1
                self.armor['armor_class_shield_impact'] -= 1
                self.shield_ready_dual_wielder = False
            return True

    def set_shield_break(self):
        """Пилумы застревают в щитах, мешая их использовать.
    
        Homebrew:
        Каждое попадание пилума в щит, это -1 к его классу защиты.
        Бой сотня на сотню, 12-24 попаданий в щиты, это весомо.
        """
        if self.armor['shield_use']\
                and not self.metadict_items[self.armor['shield_use']].get('unbreakable'):
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

    def drop_spell(self, spell_choice):
        """Теряем слот заклинания. Запоминаем это."""
        spell_slot = spell_choice[0]
        spell_name = spell_choice[-1]
        if spell_slot in self.metadict_class_spells.get((self.char_class,self.level),[]):
            if not spell_choice in self.drop_spells_dict:
                self.drop_spells_dict[spell_choice] = 1
            elif spell_choice in self.drop_spells_dict:
                self.drop_spells_dict[spell_choice] += 1
            return True
        else:
            if not spell_choice in self.drop_spells_dict:
                self.drop_spells_dict[spell_choice] = 1
            elif spell_choice in self.drop_spells_dict:
                self.drop_spells_dict[spell_choice] += 1
            return True

    def drop_action(self, action_choice):
        """Запоминаем, что использовали способность.
        
        """
        # TODO: В этой функции и обнуляй использованные действия.
        if not action_choice in self.drop_actions_dict:
            self.drop_actions_dict[action_choice] = 1
        elif action_choice in self.drop_actions_dict:
            self.drop_actions_dict[action_choice] += 1
        return True

    def use_item(self, spell, gen_spell = True, use_action = True, use_spell_slot = False):
        """Используется руна, свиток, предмет.

        - Хранящий заклинание под ключом 'spell'.
        - При этом базовый словарь заклинание через update пополняется словарём предмета.
        """
        for item, number in self.equipment_weapon.items():
            if number > 0 and 'runes' in self.commands:
                if item == spell and spell == self.metadict_items[item].get('spell'):
                    spell = self.metadict_items[item].get('spell')
                if spell == self.metadict_items[item].get('spell'):
                    item_dict = self.metadict_items[item]
                    if gen_spell and type(gen_spell) == dict:
                        item_dict.update(gen_spell)
                        gen_spell = item_dict
                    elif gen_spell:
                        gen_spell = item_dict
                    spell_dict = self.try_spellcast(spell, gen_spell, use_spell_slot, use_action)
                    if spell_dict:
                        #print('NYA', spell, use_action, gen_spell)
                        self.drop_item(item)
                        return spell_dict

    def drop_item(self, item, number = 1, drop_all = False, transfet_item = False):
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
            if not transfet_item:
                if not item in self.drop_items_dict:
                    self.drop_items_dict[item] = 1
                elif item in self.drop_items_dict:
                    self.drop_items_dict[item] += 1
            return True
        else:
            return False

    def loot_enemy(self, enemy_soldier, use_action = False):
        """Боец грабит поверженного врага.

        Снаряжение врага переносится в трофеи бойца.
        Если грабёж поспешный, то тратится действие и не снимается броня.
        """
        if use_action:
            self.drop_action(('action', 'Help_Action_Loot_Enemy'))
            self.help_action = True
        else:
            self.drop_action(('long_action', 'Loot_Enemy'))
            # Охота. Бойцы разделывают добытую живность (или живность разделывает бойцов):
            if enemy_soldier.char_class == 'Animal'\
                    or self.char_class == 'Animal':
                if enemy_soldier.death or enemy_soldier.disabled:
                    carcass_weight_lb = enemy_soldier.body['weight_lb']
                    meat_weight_lb = round(carcass_weight_lb * 0.5)
                    #meat_dict_base = copy.deepcopy(self.metadict_items['Meat (1 lb)'])
                    #meat_name = (enemy_soldier.rank, 'Meat (1 lb)')
                    meat_name = ' '.join([enemy_soldier.rank, 'meat (lb)'])
                    self.get_trophy(meat_name, meat_weight_lb)
        # Руны и эссенции не попадают в трофеи.
        # Также исключаем созданные магией предметы (вроде Mage_Armor).
        for item, number in enemy_soldier.equipment_weapon.items():
            item_dict = self.metadict_items[item]
            if number > 0\
                    and not item_dict.get('rune') == True\
                    and not item_dict.get('infusion') == True\
                    and not item_dict.get('spell') == True:
                if use_action\
                        and not item_dict.get('armor') == True:
                    self.get_trophy(item, number)
                    enemy_soldier.drop_item(item, number)
                else:
                    self.get_trophy(item, number)
                    enemy_soldier.drop_item(item, number)

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
        """Боец реагирует на атаку."""
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
        armor_dict = self.modify_armor(attack_choice, attack_dict)
        attack_dict['savethrow_bonus_cover'] = armor_dict['savethrow_bonus_cover']
        if attack_dict.get('attack') and not attack_dict.get('direct_hit'):
            if attack_dict['attack_crit'] == True:
                result['hit'] = True
                result['crit'] = True
            elif attack_dict['attack'] >= armor_dict['armor_class']:
                result['hit'] = True
            elif attack_dict['attack'] < armor_dict['armor_class_no_impact']:
                result['miss'] = True
            elif attack_dict['attack'] < armor_dict['armor_class_shield_impact']:
                result['shield_impact'] = True
            elif attack_dict['attack'] < armor_dict['armor_class_armor_impact']:
                result['armor_impact'] = True
            elif attack_dict['attack'] <= 0 or attack_dict['attack_loss']:
                result['clumsy_miss'] = True
        # Волшебные стрелы всегда попадают в цель:
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
            attack_dict = self.take_damage(attack_choice, attack_dict, metadict_soldiers)
        return attack_dict

    def modify_armor_reaction_shield(func):
        """Заклинание "Щит" (Shield) временно повышает AC.

        - Используется из руны/свитка.
        - Либо кастуется из списка заклинаний.
        - Тратит реакцию, что включено в каст заклинания.
        """
        def wrapper(self, attack_choice, attack_dict):
            armor_dict = func(self, attack_choice, attack_dict)
            # Реакцией срабатывает волшебный щит.
            if not 'shield' in self.buffs:
                if attack_dict.get('attack')\
                        and attack_dict['attack'] >= armor_dict['armor_class']\
                        and attack_dict['attack'] < armor_dict['armor_class'] + 5\
                        or attack_choice[-1] == 'Magic_Missile':
                    if 'runes' in self.commands and self.reaction:
                        self.use_item('Shield', gen_spell = True)
                        if not 'shield' in self.buffs\
                                and 'spellcast' in self.commands and self.reaction:
                            self.try_spellcast('Shield', gen_spell = True)
            # Заклинание 'Shield' даёт +5 AC
            # И защищает от волшебных стрел:
            armor_class_before = armor_dict['armor_class']
            if 'shield' in self.buffs:
                armor_dict['armor_class_no_impact'] += 5
                armor_dict['armor_class_shield_impact'] += 5
                armor_dict['armor_class_armor_impact'] += 5
                armor_dict['armor_class'] += 5
                if attack_dict.get('direct_hit'):
                    # Защищает от волшебных стрел:
                    if attack_choice[-1] == 'Magic_Missile':
                        attack_dict['direct_hit'] = False
                    # Защищает от бронебойных пуль, savethrow_all --> armor_class:
                    if 'firearm' in attack_dict.get('weapon_type',[]):
                        attack_dict['direct_hit'] = False
                # Вывод результата:
                # TODO: в отдельную функцию.
                #if attack_dict.get('attack', 0) >= armor_class_before\
                #        and attack_dict.get('attack',0) < (armor_dict['armor_class'])\
                #        and not attack_dict['attack_crit']:
                #    print('[+++] {0} {1} {2} reaction Shield {3}/{4} << {5} atc {6} dmg {7}'.format(
                #        self.ally_side, self.place, self.behavior,
                #        armor_dict['armor_class'], armor_class_before,
                #        attack_choice, attack_dict['attack'], attack_dict['damage']))
            return armor_dict
        return wrapper

    def modify_armor_reaction_def_duel(func):
        """Способность "Оборонительный дуэлянт" Feat_Defensive_Duelist.

        - Добавляет бонус мастерства к AC против единственной атаки.
        - Тратит реакцию.
        """
        def wrapper(self, attack_choice, attack_dict):
            armor_dict = func(self, attack_choice, attack_dict)
            armor_class_before = armor_dict['armor_class']
            # Парирование атаки за счёт реакции:
            # Учитываем реакцию Feat_Defensive_Duelist:
            if attack_choice[0] == 'close' or attack_choice[0] == 'reach':
                if self.class_features.get('Feat_Defensive_Duelist')\
                        and self.reaction == True\
                        and attack_dict['attack'] >= armor_class_before\
                        and attack_dict['attack'] < armor_class_before + self.proficiency_bonus:
                    armor_dict['armor_class_shield_impact'] += self.proficiency_bonus
                    armor_dict['armor_class_armor_impact'] += self.proficiency_bonus
                    armor_dict['armor_class'] += self.proficiency_bonus
                    self.drop_action(('reaction', 'Feat_Defensive_Duelist'))
                    self.reaction = False
                    # Всё работает, вывод можно убрать:
                    #if attack_dict['attack'] < armor_dict['armor_class']\
                    #        and not attack_dict['attack_crit']:
                    #    print('[+++] {0} {1} {2} reaction Def Duel {3}/{4} << {5} atc {6} dmg {7}'.format(
                    #        self.ally_side, self.place, self.behavior,
                    #        armor_dict['armor_class'], armor_class_before,
                    #        attack_choice, attack_dict['attack'], attack_dict['damage']))
            return armor_dict
        return wrapper

    @modify_armor_reaction_def_duel
    @modify_armor_reaction_shield
    def modify_armor(self, attack_choice, attack_dict):
        """Боец реагирует на атаку.
        
        Учитывается прикрытие местности (в долях от площади тела):
        https://www.dandwiki.com/wiki/5e_SRD:Cover
        - 1/2 cover -- +2 AC, +2 DEX sav
        - 3/2 cover -- +5 AC, +5 DEX sav
        """
        # Местность даёт прикрытие (особенно от лучников):
        armor_dict = copy.deepcopy(self.armor)
        cover = attack_dict['enemy_cover']
        armor_dict['savethrow_bonus_cover'] = 0
        if not 'ignore_cover' in attack_dict:
            # 1/2 cover -- +2 AC, +2 DEX sav
            if cover >= 4 and cover < 7:
                armor_dict['armor_class_no_impact'] += 2
                armor_dict['armor_class_shield_impact'] += 2
                armor_dict['armor_class_armor_impact'] += 2
                armor_dict['armor_class'] += 2
                armor_dict['savethrow_bonus_cover'] = 2
            # 3/2 cover -- +5 AC, +5 DEX sav
            elif cover >= 7:
                armor_dict['armor_class_no_impact'] += 5
                armor_dict['armor_class_shield_impact'] += 5
                armor_dict['armor_class_armor_impact'] += 5
                armor_dict['armor_class'] += 5
                armor_dict['savethrow_bonus_cover'] = 5
        # Огнестрел лишается свойства direct_hit на большой дистанции:
        if attack_dict.get('weapon_type') and 'firearm' in attack_dict.get('weapon_type')\
                and attack_dict['enemy_distance'] * self.tile_size > attack_dict['shoot_range']\
                and attack_dict.get('direct_hit'):
            attack_dict['direct_hit'] = False
        # Заклинание "Shield_of_Faith" даёт +2 AC:
        if 'shield_of_faith' in self.buffs:
            armor_dict['armor_class_no_impact'] += 2
            armor_dict['armor_class_shield_impact'] += 2
            armor_dict['armor_class_armor_impact'] += 2
            armor_dict['armor_class'] += 2
        return armor_dict

    def take_damage(self, attack_choice, attack_dict, metadict_soldiers):
        """Боец реагирует на повреждения.
        
        По правилам DnD 5.0:
        - Ранен на 100% хитов -- потеря сознания, борьба за жизнь.
        - Ранен на 200% от макс. числа хитов -- мгновенная смерть.

        Множество модификаторов:
        - Сначала из урона вычитаем/прибавляем целые числа.
        - Учитываем спасбросок, который уменьшает урон вдвое/целиком.
        - Затем делим/умножаем, если есть сопротивляемость/уязвимость.
        - Учитываем бонусные хиты.
        """
        damage = attack_dict['damage']
        # Свойства вооружения врага усиливают урон:
        damage = self.damage_modify_sender(attack_dict, damage)
        # Защитные приёмы и свойства ослабляют урон:
        damage = self.damage_modify_victim(attack_dict, damage)
        # Спасбросок против урона заклинаний:
        if attack_dict.get('savethrow'):
            damage = self.damage_modify_savethrow(attack_dict, damage)
        # Иммунитет, сопротивляемость, уязвимость:
        damage = self.damage_modify_resistance(attack_dict, damage)
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
            # Возвращение друида в обычную форму, если не осталось бонусных хитов:
            if self.wild_shape and self.bonus_hitpoints <= 0:
                self.return_old_form(metadict_soldiers)
        if damage > 0 or attack_dict.get('bonus_hitpoints_damage'):
            # Боец получает урон:
            self.set_hitpoints(damage = damage)
            attack_dict['damage'] = damage
            self.trauma_damage_type = attack_dict['damage_type']
            if self.hitpoints <= 0 and not self.defeat:
                attack_dict['fatal_hit'] = True
            # Спящий просыпается, если ранен:
            if damage and 'sleep' in self.debuffs:
                self.debuffs.pop('sleep')
            # Прерывание концентрации
            if damage and self.concentration:
                spell = self.concentration['spell_choice']
                concentration_break = self.set_concentration_break(difficult = round(damage / 2))
                #if concentration_break:
                #    enemy_soldier = metadict_soldiers[attack_dict['sender_uuid']]
                #    print('[!!!] {side_1}, {c1} {s} DISPELL {spell} >> {side_2} {c2} {e}'.format(
                #        side_1 = enemy_soldier.ally_side,
                #        c1 = enemy_soldier.place,
                #        s = enemy_soldier.behavior,
                #        spell = spell[-1],
                #        side_2 = self.ally_side,
                #        c2 = self.place,
                #        e = self.behavior,
                #        ))
            # Стойкость нежити (зомби не так-то просто убить):
            if self.class_features.get('Undead_Fortitude') and self.hitpoints <= 0\
                    and not attack_dict.get('attack_crit')\
                    and attack_dict['damage_type'] != 'radiant':
                difficult = 5 + damage
                ability = 'constitution'
                if self.get_savethrow(difficult, ability):
                    self.hitpoints = 1
            # Показываем, если командиру достаётся:
            # TODO: перенеси вовне. Сделай декоратором.
            #enemy_soldier = metadict_soldiers[attack_dict['sender_uuid']]
            #if self.level >= 5 and damage > 0:
            #    print('[!!!] {side}, {c1} {s} {w} >>>> {c2} {e}, crit {c} atc {a} dmg {d}'.format(
            #        side = enemy_soldier.ally_side,
            #        s = enemy_soldier.behavior,
            #        e = self.behavior,
            #        c1 = enemy_soldier.place,
            #        c2 = self.place,
            #        w = attack_choice,
            #        c = attack_dict['crit'],
            #        a = attack_dict.get('attack', None),
            #        d = damage,
            #        ))
            return attack_dict
        # Промах, если урон нулевой:
        elif damage <= 0:
            damage = 0
            attack_dict['hit'] = False
            attack_dict['damage'] = damage
            return attack_dict

    def damage_modify_sender(self, attack_dict, damage):
        """Модификаторы к урону от врага.

        - Осадное вооружение = x2 урона зданиям.
        - Под водой огонь наносит 50% урона.
        """
        if 'siege' in attack_dict.get('weapon_type',[]):
            if self.__dict__.get('mechanism'):
                damage *= 2
        if attack_dict.get('damage_halved'):
            damage = round(damage / 2)
        return damage

    def damage_modify_victim(self, attack_dict, damage):
        """Защитные приёмы ослабляют урон.

        - Порог урона крупных объектов
        - Порог урона мастеров тяжёлых доспехов
        - Уклонение плута
        - Отражение стрел монахом
        - Парирование мастера боевых искусств

        Эти модификаторы применяются до сопротивляемости к урону.
        """
        attack_choice = attack_dict['attack_choice']
        # Крупные объекты (стены, корабли) имеют порог урона:
        if self.__dict__.get('ignore_damage'):
            damage -= self.ignore_damage
        # Умелые бойцы получают меньше урона в тяжёлой броне:
        if self.class_features.get('Feat_Heavy_Armor_Master'):
            if attack_dict['damage_type'] == 'bludgeoning'\
                    or attack_dict['damage_type'] == 'piercing'\
                    or attack_dict['damage_type'] == 'slashing':
                damage -= 3
        # TODO: сделай через декораторы, чтобы можно было менять порядок реакции.
        # Уклонение плута срабатывает только против ударов с броском атаки:
        if self.class_features.get('Uncanny_Dodge') and self.reaction\
                and attack_dict.get('attack'):
            damage = round(damage / 2)
            self.reaction = False
        # Отражение/перехват стрел монахом:
        # https://www.dandwiki.com/wiki/5e_SRD:Monk#Deflect_Missiles
        if attack_choice[0] == 'throw' or attack_choice[0] == 'ranged' or attack_choice[0] == 'volley':
            if self.class_features.get('Deflect_Missiles') and self.reaction == True:
                damage_deflect = dices.dice_throw('1d10') + self.mods['dexterity'] + self.level
                damage -= damage_deflect
                self.reaction = False
                #print('[+++] {0} {1} {2} reaction Deflect {3}/{4} << {5} atc {6} dmg {7}'.format(
                #    self.ally_side, self.place, self.behavior,
                #    damage_deflect, attack_dict['damage'],
                #    attack_choice, attack_dict['attack'], attack_dict['damage']))
        # Прирование мастера боевых искусств:
        if attack_choice[0] == 'close' or attack_choice[0] == 'reach':
            if self.class_features.get('Parry') and self.superiority_dices and self.reaction == True:
                damage_deflect = dices.dice_throw(self.superiority_dice) + self.mods['dexterity']
                damage -= damage_deflect
                self.reaction = False
                self.superiority_dices -= 1
                self.drop_spell(('feature', 'Battlemaster_Parry'))
                #print('[+++] {0} {1} {2} reaction Parry {3}/{4} << {5} atc {6} dmg {7}'.format(
                #    self.ally_side, self.place, self.behavior,
                #    damage_deflect, attack_dict['damage'],
                #    attack_choice, attack_dict['attack'], attack_dict['damage']))
        return damage

    def damage_modify_savethrow(self, attack_dict, damage, savethrow_bonus = 0):
        """Спасбросок от урона заклинаний, дыхания дракона, шрапнели и т.п.
        
        - Успешный спасбросок = 50% урона
        - Успешный спасбросок ловкости с Evasion = 0 урона
        - Неудачный спасбросок ловкости с Evasion = 50% урона
        """
        # Если сложность заклинания не указана, тогда она равна атаке (d20 + мод.атаки)
        ability = attack_dict['savethrow_ability']
        difficult = attack_dict.get('spell_save_DC', attack_dict.get('attack'))
        # Бонус укрытия к спасброскам ловкости:
        if ability == 'dexterity' and not attack_dict.get('ignore_cover'):
            savethrow_bonus += attack_dict['savethrow_bonus_cover']
        # Делаем спасбросок:
        if self.get_savethrow(difficult, ability, bonus = savethrow_bonus):
            damage = round(damage / 2)
            if attack_dict.get('savethrow_all'):
                damage = 0
            if ability == 'dexterity' and self.class_features.get('Evasion'):
                damage = 0
            # Мастер щитов может уклониться за счёт реакции:
            if ability == 'dexterity' and self.class_features.get('Feat_Shield_Master'):
                if damage > round(self.hitpoints * 0.2) and self.reaction:
                    self.drop_action(('reaction', 'Feat_Shield_Master_Evasion'))
                    self.reaction = False
                    damage = 0
            if ability == 'dexterity' and self.behavior == 'mount'\
                    and self.__dict__.get('master_uuid')\
                    and self.metadict_soldiers[self.master_uuid].class_features.get('Feat_Mounted_Combatant')\
                    and self.place == self.metadict_soldiers[self.master_uuid].place\
                    and not self.metadict_soldiers[self.master_uuid].defeat:
                damage = 0
        # Увёртливые воры и монахи всё равно уклоняются:
        else:
            if ability == 'dexterity' and self.class_features.get('Evasion'):
                damage = round(damage / 2)
            if ability == 'dexterity' and self.behavior == 'mount'\
                    and self.__dict__.get('master_uuid')\
                    and self.metadict_soldiers[self.master_uuid].class_features.get('Feat_Mounted_Combatant')\
                    and self.place == self.metadict_soldiers[self.master_uuid].place\
                    and not self.metadict_soldiers[self.master_uuid].defeat:
                damage = round(damage / 2)
        return damage

    def damage_modify_resistance(self, attack_dict, damage):
        """Иммунитет, сопротивляемость, уязвимость к урону.

        Иммунитет = 0 урона
        Сопротивляемость = 1/2 урона
        Уязвимость = x2 урона
        
        - Используется заклинание Absorb_Elements, если это возможно.
        - Магическое оружие преодолевает сопротивляемость/иммунитет к обычному оружию.
        """
        # ------------------------------------------------------------
        # TODO: проверки реакции здесь уже не нужны.
        # Проверка на опасный урон должна быть отдельной функцией.
        # ------------------------------------------------------------
        # Пытаемся защититься с помощью руны или заклинания "Поглощение стихий":
        if not attack_dict['damage_type'] in self.resistance:
            if damage >= round(self.hitpoints * 0.2):
                if 'runes' in self.commands and self.reaction:
                    self.use_item(
                            'Absorb_Elements',
                            gen_spell = {'damage_type':attack_dict['damage_type']})
                elif self.reaction:
                    spell_dict = self.try_spellcast(
                            'Absorb_Elements',
                            gen_spell = {'damage_type':attack_dict['damage_type']})
        # Урон от магического оружия преодолевает иммунитет:
        if attack_dict['damage_type'] in self.immunity:
            if attack_dict.get('weapon_type') and 'magic' in attack_dict['weapon_type']:
                damage = damage
            else:
                damage = 0
        # Сопротивляемость к видам урона и её преодоление:
        elif attack_dict['damage_type'] in self.resistance:
            if 'magic' in attack_dict.get('weapon_type',[]):
                damage = damage
            elif attack_dict.get('ignore_resistance') == attack_dict['damage_type']:
                damage = damage
            else:
                damage = round(damage / 2)
        # Уязвимость к видам урона:
        elif attack_dict['damage_type'] in self.vultenability:
            damage = round(damage * 2)
        return damage

# ----
# Опыт за победу

    def set_victory_and_enemy_defeat(self, enemy_soldier):
        """Боец получает опыт за победу.
        
        """
        # Учитывается только первая победа, а не добивание:
        if not enemy_soldier.defeat and not enemy_soldier.fall:
            self.victories += 1
            enemy_soldier.defeats += 1
            self.experience += enemy_soldier.get_experience()
            # Словарь побед (это списки uuid побеждённых врагов):
            key = enemy_soldier.rank
            if not key in self.victories_dict:
                self.victories_dict[key] = [enemy_soldier.uuid,]
            elif key in self.victories_dict:
                self.victories_dict[key].append(enemy_soldier.uuid)
        # TODO: это оформи как wrapper.
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
        # Раненый начинает спасброски от смерти:
        enemy_soldier.stable = False
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
        # У схваченного отбирают всё оружие, чтобы не натворил дел, если вдруг очнётся:
        if enemy_soldier.grappled or not enemy_soldier.near_allies and enemy_soldier.near_enemies:
            self.loot_enemy(enemy_soldier, use_action = True)
        # Оружие и щит выпадают из рук:
        if enemy_soldier.shield_ready:
            enemy_soldier.unset_shield(disarm = True)
        if enemy_soldier.weapon_ready:
            enemy_soldier.unset_weapon(enemy_soldier.weapon_ready, disarm = True)
