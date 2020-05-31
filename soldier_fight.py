#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from soldier_base import *

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
        # Даём боевые действия и пул движения:
        self.battle_action = True
        self.bonus_action = True
        self.reaction = True
        self.move_action = True
        self.move_pool = self.base_speed
        if hasattr(self, 'help_action') and self.help_action: 
            self.help_action = False
        # Общие для всех параметры:
        self.immunity = []
        self.resistance = []
        self.defeat = False
        self.escape = False
        self.prone = False
        self.grappled = False
        self.restained = False
        self.concentration = False
        self.help_action = False
        # Эффекты заклинаний:
        self.fear = False
        self.mockery = False
        self.sleep = False
        self.damage_absorbed = None
        self.bardic_inspiration = None
        # Концентрация на заклинаниях:
        # TODO: да сделай ты универсальную систему!
        # И универсальный таймер концентрации на заклинаниях.
        self.bless = None
        self.bless_timer = 0
        self.thorns = None
        self.thorns_timer = 0
        self.moonbeam = None
        self.moonbeam_timer = 0
        self.call_lightning = None
        self.call_lightning_timer = 0
        # Способности бойца, паладина:
        self.action_surge = False
        self.second_wind = False
        self.lay_on_hands = 0
        self.shield = False
        if not hasattr(self, 'arcane_ward'):
            self.arcane_ward = False
        if not hasattr(self, 'mage_armor'):
            self.mage_armor = False
        if not hasattr(self, 'blur'):
            self.blur = False
        if not hasattr(self, 'sacred_weapon'):
            self.sacred_weapon = False
        if not hasattr(self, 'fall'):
            self.fall = False
        if not hasattr(self, 'disabled'):
            self.disabled = False
        if not hasattr(self, 'captured'):
            self.captured = False
        # Статистика побед и поражений бойца:
        if not hasattr(self, 'victories'):
            self.victories = 0
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
            if self.class_features.get('Champion_Improved_Critical'):
                self.crit_range = 19
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
            if self.proficiency.get('channel_divinity') and not hasattr(self, 'channel_divinity'):
                self.channel_divinity = self.proficiency['channel_divinity']
            # Особенности монстров:
            if self.class_features.get('Wight_Resistance'):
                self.resistance.append('slashing')
                self.resistance.append('piercing')
                self.resistance.append('bludgeoning')
                self.resistance.append('necrotic_energy')
            # Особенности монстров:
            if self.class_features.get('Empyrean_Immunity'):
                self.immunity.append('slashing')
                self.immunity.append('piercing')
                self.immunity.append('bludgeoning')
                self.resistance.append('slashing')
                self.resistance.append('piercing')
                self.resistance.append('bludgeoning')
            if self.class_features.get('Ink_Cloud') and not hasattr(self, 'ink_cloud'):
                self.ink_cloud = True
                self.ink_cloud_radius = 20
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
        # Используем предметы перед боем:
        # TODO: некрасиво сделано. Но в soldier_base переносить не хочется.
        # Вообще, можно считать "Infusion of Claws" оружием и использовать базовый метод.
        #if self.equipment_weapon.get('Infusion of Claws'):
        #    self.equipment_weapon['Infusion of Claws'] -= 1
        #    dict_attack = copy.deepcopy(self.metadict_items['Infusion of Claws'])
        #    dict_attack['attack_range'] = 5
        #    dict_attack['attack_type'] = 'close'
        #    dict_attack.update(self.select_attack_mod(dict_attack))
        #    dict_attack.update(self.attack_modify_features(dict_attack))
        #    self.attacks['close','claws'] = dict_attack
        #    self.attacks.update(self.modify_attacks())
        #    print(self.attacks)
        # Используем заклинания перед боем:
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
                        #print(self.hitpoints_max, self.bonus_hitpoints)
                if spell_dict.get('blur') and not self.blur and not self.concentration:
                    self.spells_generator.use_spell(spell)
                    self.blur = True
                    self.blur_timer = 10
                    break
                if spell_dict.get('effect') is 'sacred_weapon' and not self.sacred_weapon:
                    #self.spells_generator.use_spell(spell)
                    self.sacred_weapon = spell_dict['attack_mod']
                    self.sacred_weapon_timer = spell_dict['effect_timer']
                    self.channel_divinity -= 1
                    break

    def set_actions(self, squad):
        """Доступные действия в 6-секундном раунде боя.
        
        Обновляются в начале каждого раунда:
        https://www.dandwiki.com/wiki/5e_SRD:Combat_Turn
        Move, Action (Ready Action), Bonus Action, Reaction
        """
        # Даём боевые действия и пул движения:
        self.battle_action = True
        self.bonus_action = True
        self.reaction = True
        self.move_action = True
        self.move_pool = self.base_speed
        if self.help_action:
            self.help_action = False
            self.battle_action = False
        # Отключаем манёвры пршлого хода:
        self.dash_action = False # это ускорение до x2 скорости за счёт battle_action.
        self.dodge_action = False # это disadvantage для врагов за счёт battle_action.
        self.reckless_attack = False # тактика варвара, преимущество и себе, и врагам.
        self.shield = False # заклинание 'Shield' волшебника даёт +5 AC на один раунд.
        # Испуганный бросает спасброски против страха:
        if self.fear:
            self.fear = self.set_fear(self.enemy_fear, self.fear_difficult)
            if self.fear:
                print('{side_1} {c1} {s} FEAR {fear}'.format(
                    side_1 = self.ally_side,
                    c1 = self.place,
                    s = self.behavior,
                    fear = self.fear
                    ))
        # Схваченный не может двигаться (но пытается вырваться):
        if self.grappled or self.restained:
            self.move_action = False
            self.move_pool = 0
            if self.grappled:
                self.set_grapple_break()
            elif self.restained:
                self.set_restained_break()
        # Упавший встаёт на ноги (если он не схвачен):
        if self.prone == True and not self.grappled:
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
        # TODO: сделай универсальную систему для заклинаний с концентрацией:
        # Нужен универсальный таймер концентрации.
        # Заклинание Bless:
        if self.bless:
            if self.bless_timer > 0:
                self.bless_timer -= 1
            elif self.bless_timer == 0:
                self.bless = None
        # Заклинание Hail_of_Thorns:
        if self.thorns:
            if self.thorns_timer > 0:
                self.thorns_timer -= 1
            elif self.thorns_timer == 0:
                self.thorns = None
        # Заклинание Moonbeam:
        if self.moonbeam:
            if self.moonbeam_timer > 0:
                self.moonbeam_timer -= 1
            elif self.moonbeam_timer == 0:
                self.moonbeam = None
        # Заклинание Call_Lightning
        if self.call_lightning:
            if self.call_lightning_timer > 0:
                self.call_lightning_timer -= 1
            elif self.call_lightning_timer == 0:
                self.call_lightning = None
        # Заклинание Blur
        if self.blur:
            if self.blur_timer > 0:
                self.blur_timer -= 1
            elif self.blur_timer == 0:
                self.blur = None
        # Channel_Sacred_Weapon
        if self.sacred_weapon:
            if self.sacred_weapon_timer > 0:
                self.sacred_weapon_timer -= 1
            elif self.sacred_weapon_timer == 0:
                self.sacred_weapon = None

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

    def set_thorns(self):
        """Рейнджер превращает лук в гранатомёт.
        
        Скорее в гранату. Hail_of_Thorns срабатывает единожды.
        """
        # TODO: используй soldier.spells_generator.find_spell('Hail_of_Thorns')
        if hasattr(self, 'spells') and self.bonus_action and not self.thorns:
            for spell, spell_dict in self.spells.items():
                if spell_dict.get('effect') and spell_dict['effect'] == 'thorns':
                    self.bonus_action = False
                    spell_dict = dict(self.spells_generator.use_spell(spell))
                    spell_dict['spell_choice'] = spell
                    self.thorns = spell_dict
                    self.thorns_timer = 10
                    break

    def set_bless(self):
        """Жрец благословляет союзников (перед началом боя)"""
        # TODO: используй soldier.spells_generator.find_spell('Bless')
        if hasattr(self, 'spells'):
            for spell, spell_dict in self.spells.items():
                if spell_dict.get('effect') and spell_dict['effect'] == 'bless':
                    spell_dict = dict(self.spells_generator.use_spell(spell))
                    spell_dict['spell_choice'] = spell
                    self.concentration_timer = 10
                    self.concentration = True
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

    def set_cunning_action_defence(self):
        """Защитные приёмы вора."""
        if self.class_features.get('Cunning_Action'):
            if self.bonus_action == True:
                self.bonus_action = False
                self.dodge_action = True

    def set_cunning_action_dash(self):
        """Ускорение вора."""
        if self.class_features.get('Cunning_Action'):
            if self.bonus_action == True:
                self.bonus_action = False
                self.dash_action = True

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
                # После первого применения добавляется ко всем рукопашным атакам:
                if self.class_features.get('Open_Hand_Technique'):
                    self.attacks[attack_choice]['Open_Hand_Technique'] = True
        if self.class_features.get('Martial_Arts'):
            if self.bonus_action == True:
                self.bonus_action = False
                attack_choice = ('close','unarmed')
                attacks_chain_bonus.append(attack_choice)
        return attacks_chain_bonus

    def set_initiative(self):
        """Бросок инициативы делается в начале боя.
        
        Бросаем d20 + модификатор ловкости.
        По этому броску выбираем, в каком порядке ходят бойцы.
        https://www.dandwiki.com/wiki/5e_SRD:Initiative
        """
        initiative = dices.dice_throw('1d20') + self.mods['dexterity']
        if self.class_features.get('Feat_Alert'):
            initiative += 5
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
            if self.danger < 0:
                self.danger += fear_danger
            else:
                self.danger = fear_danger
        # Каждые 10% потерянного здоровья увеличивают опасность:
        if self.hitpoints < self.hitpoints_max\
                and not 'fearless' in squad.commands\
                and not self.equipment_weapon.get('Infusion of Healing'):
            hitpoints_danger = math.floor((1 - self.hitpoints / self.hitpoints_max) * 10)
            self.danger += hitpoints_danger
            # Раненые осьминожки удирают:
            if self.__dict__.get('water_walk') and self.hitpoints < (self.hitpoints_max / 2):
                self.danger = 0
                self.escape = True
            #if 'dodge' in squad.commands and self.hitpoints < (self.hitpoints_max / 2):
            #    self.danger = 0
            #    self.escape = True
        # Каждые 10% потерь союзников также увеличивают угрозу:
        if squad.casualty['casualty_percent'] > 0 and not 'fearless' in squad.commands:
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
            #if hasattr(self, 'spells') and not self.spellslots and 'dodge' in squad.commands:
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
                if mount.escape == True and 'dodge' in squad.commands:
                    self.danger = 1
                    self.escape = True

    def morality_check_escape(self, danger, advantage = False, disadvantage = False):
        """Если опасность высока, боец боится и может сбежать.
        
        Это проверка 10 + уровень_опасности против спасброска харизмы.
        """
        danger_difficul = 10 + danger
        danger_saving_throw = dices.dice_throw_advantage('1d20', advantage, disadvantage)\
                + self.saves['charisma']
        if danger_difficul > danger_saving_throw:
            return True
        else:
            return False

    def set_protection(self, soldier):
        """Боец прикрывает союзника по его просьбе.
        
        Fighting_Style_Protection даёт disadvantage на атаку врага."""
        # Просто указываем, что реакция сработала:
        if self.class_features.get('Fighting_Style_Protection')\
                and self.armor['shield_use'] != None\
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

    def set_second_wind(self):
        """Fighter может очухаться после ранения.
        
        https://www.dandwiki.com/wiki/5e_SRD:Fighter#Second_Wind
        """
        if self.class_features.get('Second_Wind'):
            if self.second_wind and self.bonus_action:
                second_wind_heal = dices.dice_throw('1d10') + self.level
                self.set_hitpoints(heal = second_wind_heal)
                self.bonus_action = False
                self.second_wind = False
                #print('{0} {1} second_wind heal {2}'.format(self.ally_side, self.rank, second_wind_heal))
                return True
            else:
                return False

    def set_lay_of_hands(self):
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
                #print('{0} {1} lay_on_hands heal {2}'.format(self.ally_side, self.rank, lay_on_hands_heal))
                return True
            else:
                return False

    def use_potion_of_healing(self):
        """Боец использует зелье лечения.
        
        Лечение равно костям хитов бойца. Для варвара 5 lvl это 5d12, в среднем 30 hp.
        """
        # TODO: есть мнение, что лечение слишком сильное.
        # Варвар с x3 лечилками восстанавливает аж 90 хитов.
        # Когда паладин с его Lay_on_Hands получает всего 25 хитов.
        if self.equipment_weapon.get('Infusion of Healing'):
            if self.equipment_weapon['Infusion of Healing'] > 0 and self.battle_action:
                self.equipment_weapon['Infusion of Healing'] -= 1
                potion_heal = round(sum([dices.dice_throw(self.hit_dice) for x in range(self.level)]))
                self.set_hitpoints(heal = potion_heal)
                self.battle_action = False
                print('{0} {1} {2} heal (potion): {3}'.format(
                    self.ally_side, self.place, self.behavior, potion_heal))
                return True
            else:
                return False

    def set_sleep(self):
        """Бойца усыпляют заклинанием."""
        # Нужно помнить, что эльфы не спят, и потому ко сну неуязвимы.
        # Мертвяки и конструкты тоже неуязвимы.
        self.sleep = True
        self.prone = True
        self.battle_action = None
        self.bonus_action = None
        self.reaction = None
        self.move_action = None
        self.move_pool = 0
        self.sleep_timer = 10
        # Спящий считается вышедшим из боя:
        #self.fall = True

    def first_aid(self, injured_ally, stabilizing_difficul = 10):
        """Боец пытается оказать первую помощь раненому.
        
        https://www.dandwiki.com/wiki/5e_SRD:Dropping_to_0_Hit_Points#Stabilizing_a_Creature
        """
        self.help_action = True
        stabilizing_throw = dices.dice_throw_advantage('1d20') + self.saves['wisdom']
        if stabilizing_throw >= stabilizing_difficul:
            return True
        else:
            return False

    def set_fall_prone(self, enemy_soldier, advantage = False, disadvantage = False):
        """Бойца пытаются сбить с ног.
        
        Проверка ловкости(+акробатика), или силы(+атлетика):
        https://www.dandwiki.com/wiki/5e_SRD:Conditions#Prone
        https://www.dandwiki.com/wiki/5e_SRD:Movement_and_Position#Being_Prone
        """
        prone_difficul = dices.dice_throw_advantage('1d20', advantage, disadvantage)\
                + enemy_soldier.mods['dexterity'] + enemy_soldier.proficiency_bonus
        if self.saves['strength'] >= self.saves['dexterity']:
            savethrow_adavantage = self.check_savethrow_advantage('strength')
            prone_savethrow = dices.dice_throw_advantage('1d20', savethrow_adavantage)\
                    + self.saves['strength']
        else:
            savethrow_adavantage = self.check_savethrow_advantage('dexterity')
            prone_savethrow = dices.dice_throw_advantage('1d20', savethrow_adavantage)\
                    + self.saves['dexterity']
        if prone_savethrow <= prone_difficul:
            self.prone = True
            return True
        else:
            return False

    def set_restained(self, restained_difficult, advantage = False, disadvantage = False):
        """Бойца пытаются опутать.
        
        Проверка ловкости(+акробатика), или силы(+атлетика):
        https://www.dandwiki.com/wiki/5e_SRD:Conditions#Grappled
        """
        savethrow_adavantage = self.check_savethrow_advantage('strength')
        restained_savethrow = dices.dice_throw_advantage('1d20', savethrow_adavantage)\
                + self.saves['strength']
        if restained_savethrow <= restained_difficult:
            self.restained = True
            self.restained_difficult = restained_difficult
            return True
        else:
            return False

    def set_grappled(self, enemy_soldier, advantage = False, disadvantage = False):
        """Бойца пытаются схватить.
        
        Проверка ловкости(+акробатика), или силы(+атлетика):
        https://www.dandwiki.com/wiki/5e_SRD:Conditions#Grappled
        """
        grapple_difficul = dices.dice_throw_advantage('1d20', advantage, disadvantage)\
                + enemy_soldier.mods['dexterity'] + enemy_soldier.proficiency_bonus
        if self.saves['strength'] >= self.saves['dexterity']:
            savethrow_adavantage = self.check_savethrow_advantage('strength')
            grapple_savethrow = dices.dice_throw_advantage('1d20', savethrow_adavantage)\
                    + self.saves['strength']
        else:
            savethrow_adavantage = self.check_savethrow_advantage('dexterity')
            grapple_savethrow = dices.dice_throw_advantage('1d20', savethrow_adavantage)\
                    + self.saves['dexterity']
        # TODO: здесь должно быть общее состояние "без сознания":
        if self.sleep:
            grapple_savethrow = 0
        if grapple_savethrow <= grapple_difficul:
            self.grappled = True
            self.enemy_grappler = enemy_soldier
            return True
        else:
            return False

    def set_grapple_break(self, advantage = False, disadvantage = False):
        """Боец пытается вырваться из захвата, тратя на это battle_action."""
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
                # Проверка силы(+атлетика) против силы(+атлетика) удерживающего врага:
                grapple_difficul = dices.dice_throw_advantage('1d20', advantage, disadvantage)\
                        + enemy_soldier.mods['strength'] + enemy_soldier.proficiency_bonus
                savethrow_adavantage = self.check_savethrow_advantage('strength')
                grapple_break_throw = dices.dice_throw_advantage('1d20', savethrow_adavantage)\
                        + self.saves['strength']
                if grapple_break_throw >= grapple_difficul:
                    self.grappled = False
                    self.restained = False
                    self.enemy_grappler = None
                    self.battle_action = False
                else:
                    self.battle_action = False

    def set_restained_break(self, advantage = False, disadvantage = False):
        """Боец пытается вырваться из захвата, тратя на это battle_action."""
        restained_difficult = self.restained_difficult
        # Проверка силы(+атлетика) против силы(+атлетика) удерживающего врага:
        savethrow_adavantage = self.check_savethrow_advantage('strength')
        grapple_break_throw = dices.dice_throw_advantage('1d20', savethrow_adavantage)\
                + self.saves['strength']
        if self.sleep:
            grapple_break_throw = 0
        if grapple_break_throw >= restained_difficult:
            self.grappled = False
            self.restained = False
            self.restained_difficult = None
            self.enemy_grappler = None
            self.battle_action = False
        else:
            self.battle_action = False

    def set_disarm_shield(self, enemy_soldier, advantage = False, disadvantage = False):
        """Бойца пытаются лишить щита.
        
        Проверка ловкости(+акробатика), или силы(+атлетика):
        Опциональное правило: Dungeon Master Guide p.271
        """
        disarm_difficul = dices.dice_throw_advantage('1d20', advantage, disadvantage)\
                + enemy_soldier.mods['dexterity'] + enemy_soldier.proficiency_bonus
        if self.saves['strength'] >= self.saves['dexterity']:
            savethrow_adavantage = self.check_savethrow_advantage('strength')
            disarm_savethrow = dices.dice_throw_advantage('1d20', savethrow_adavantage)\
                    + self.saves['strength']
        else:
            savethrow_adavantage = self.check_savethrow_advantage('dexterity')
            disarm_savethrow = dices.dice_throw_advantage('1d20', savethrow_adavantage)\
                    + self.saves['dexterity']
        if self.sleep:
            disarm_savethrow = 0
        if disarm_savethrow <= disarm_difficul:
            return self.unset_shield()
        else:
            return False

    def set_disarm_weapon(self, enemy_soldier, advantage = False, disadvantage = False):
        """Бойца пытаются лишить оружия.
        
        Проверка ловкости(+акробатика), или силы(+атлетика):
        Опциональное правило: Dungeon Master Guide p.271
        """
        disarm_difficul = dices.dice_throw_advantage('1d20', advantage, disadvantage)\
                + enemy_soldier.mods['dexterity'] + enemy_soldier.proficiency_bonus
        if self.saves['strength'] >= self.saves['dexterity']:
            savethrow_adavantage = self.check_savethrow_advantage('strength')
            disarm_savethrow = dices.dice_throw_advantage('1d20', savethrow_adavantage)\
                    + self.saves['strength']
        else:
            savethrow_adavantage = self.check_savethrow_advantage('dexterity')
            disarm_savethrow = dices.dice_throw_advantage('1d20', savethrow_adavantage)\
                    + self.saves['dexterity']
        if self.sleep:
            disarm_savethrow = 0
        if disarm_savethrow <= disarm_difficul:
            # TODO: Тут, получается, разом отбирают всё оружие.
            # ------------------------------------------------------------
            # Но на деле, лишившись копья боец схватил бы меч, а потом кинжал.
            # Используй функцию unset_weapon. Сначала лучшее, weapon_of_choice.
            # ------------------------------------------------------------
            self.attacks = self.takeoff_weapon()
            self.attacks.update(self.modify_attacks())
            return True
        else:
            return False

    def set_fear(self, enemy_soldier, fear_difficult):
        """Бойца пытаются испугать заклинанием cause_fear или чем-то подобным."""
        # 45 срабатываний за бой от 30+ варлоков, впечатляющее заклинание.
        fear_savethrow = dices.dice_throw_advantage('1d20') + self.saves['wisdom']
        if fear_savethrow <= fear_difficult:
            self.fear = True
            self.enemy_fear = enemy_soldier
            self.fear_difficult = fear_difficult
            return True
        else:
            self.fear = False
            self.enemy_fear = None
            self.fear_difficult = None
            return False

    def set_death(self):
        """Тяжелораненые играет в рулетку с мрачным жнецом.
        
        Death Saving Throws:
        https://www.dandwiki.com/wiki/5e_SRD:Dropping_to_0_Hit_Points
        """
        #self.fall = True
        if not hasattr(self, 'death_save_success') or not hasattr(self, 'death_save_loss'):
            self.death_save_loss = 0
            self.death_save_success = 0
            self.disabled = False
            self.stable = False
            self.death = False
        elif not self.stable == True and not self.death == True:
            reaper_throw = dices.dice_throw('1d20')
            # Схваченных не убивают, а только оглушают:
            if self.grappled:
                self.death_save_success = 3
                self.stable = True
                self.captured = True
                return('stable', self.stable)
            # Тяжелейшие ранения, если атака лишь чуть не убила бойца:
            if self.hitpoints <= -(self.hitpoints_max / 2):
                self.disabled = True
                #print('disabled', self.rank, self.hitpoints)
            # Мгновенная смерть, если атака увела хиты в минусовой максимум:
            if self.hitpoints <= -(self.hitpoints_max):
                self.death_save_loss = 3
                self.death = True
            # Иначе борьба за жизнь, где всё в руках судьбя:
            else:
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
                print('{0} {1} {2} {3} hp {4}/{5} throw {6} result {7}:{8} stable {9} dead {10}'.format(
                    self.ally_side, self.place, self.behavior, self.name,
                    self.hitpoints, self.hitpoints_max,
                    reaper_throw, self.death_save_success, self.death_save_loss,
                    self.stable, self.death))

    def check_savethrow_advantage(self, savethrow_type):
        """Способности могут дать преимущество на спасбросок."""
        # Варвары в ярости получают преимущество на спасброски силы:
        if savethrow_type == 'strength':
            if self.class_features.get('Rage') and self.rage:
                return True

# ----

    def move(self, distance = 5, rough = False):
        """Боец двигается. Обычно на 5 футов (один тайл карты).
        
        Возможности:
        - Dash_Action -- двухкратное ускорение.
        """
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
        # ------------------------------------------------------------
        if distance <= 1 and 'close' in [attack[0] for attack in self.attacks]:
            close_attack = [attack for attack in self.attacks if attack[0] == 'close'
                    and attack[1] == self.attacks[attack]['weapon_of_choice']][0]
            return close_attack
        if distance <= 2 and 'reach' in [attack[0] for attack in self.attacks]:
            reach_attack = [attack for attack in self.attacks if attack[0] == 'reach'
                    and attack[1] == self.attacks[attack]['weapon_of_choice']][0]
            return reach_attack
        if distance >= 2 and 'throw' in [attack[0] for attack in self.attacks]:
            throw_attack = [attack for attack in self.attacks if attack[0] == 'throw'
                    and attack[1] == self.attacks[attack]['weapon_of_choice']][0]
            # Метатли дротиков работают с максимальной дистанции:
            if self.behavior == 'archer'\
                    and distance <= round(self.attacks[throw_attack]['attack_range_max'] / tile_size):
                return throw_attack
            # Бойцы ближнего боя подпускают пехоту врага поближе и метают прицельно:
            elif self.behavior != 'archer'\
                    and distance <= round(self.attacks[throw_attack]['attack_range'] / tile_size):
                return throw_attack
        if distance >= 2 and 'ranged' in [attack[0] for attack in self.attacks]:
            ranged_attack = [attack for attack in self.attacks if attack[0] == 'ranged'
                    and attack[1] == self.attacks[attack]['weapon_of_choice']][0]
            if distance <= round(self.attacks[ranged_attack]['attack_range_max'] / tile_size):
                return ranged_attack

    def select_spell(self, squad, enemy, tile_size = 5):
        """Боец выбирает заклинание, начиная с высших уровней."""
        # TODO: проблема дистанции. Некоторые кантрипы удобны в ближнем бою.
        # Сделай метки на заклинаниях ближнего боя и в конце перебирай их.
        distance = enemy.distance
        enemy_cover = enemy.cover
        spellslots_list = reversed(list(self.spellslots.keys()))
        for spell_slot in spellslots_list:
            # Без приказа только заклинания 1 круга:
            if int(spell_slot[0]) < 2 or 'fireball' in squad.commands:
                if distance >= 2 and spell_slot in [attack[0] for attack in self.spells]:
                    spell_attack = [attack for attack in self.spells if attack[0] == spell_slot
                            and attack[1] == self.spells[attack]['spell_of_choice']]
                    if spell_attack:
                        # TODO: лучше используй random.choice
                        spell_attack = spell_attack[0]
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
        # Нельзя использовать два приёма баттлмастера за одну атаку:
        superiority_use = False
        # Боец с двуручным оружием бросает щит (который использовал, чтобы добраться до стрелков)
        # Впрочем, лучники и пикионеры могут использовать щиты с дальней и reach-атакой.
        if attack_dict.get('weapon_type')\
                and attack_choice[0] == 'close'\
                and 'two_handed' in attack_dict['weapon_type']\
                and self.armor['shield_use']:
            self.unset_shield()
        # Стрельба из лука неудобна вблизи, или на сверхдальности:
        if attack_dict['attack_range'] > self.tile_size * 2:
            if enemy.distance > round(attack_dict['attack_range'] / self.tile_size)\
                    or enemy.distance <= 2:
                disadvantage = True
            # Меткие стрелки игнорируют укрытие и помехи по дальности:
            elif self.class_features.get('Feat_Sharpshooter'):
                target_cover = 0
        # Бардовское Vicious_Mockery портит одиночную атаку:
        if self.mockery:
            self.mockery = False
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
        if self.bless:
            attack_throw_mod += self.bless
        # Channel_Sacred_Weapon усиливает атаку (и делает оружие волшебным):
        if self.sacred_weapon:
            attack_throw_mod += self.sacred_weapon
            if attack_dict.get('weapon_type') and not 'magic' in attack_dict['weapon_type']:
                attack_dict['weapon_type'].append('magic')
        # Bardic_Inspiration усиливает атаку:
        if self.bardic_inspiration\
                and enemy_soldier.armor['armor_class'] > attack_throw_mod\
                and not enemy_soldier.armor['armor_class'] > attack_throw_mod + self.bardic_inspiration:
            attack_throw_mod += self.bardic_inspiration
            self.bardic_inspiration = None
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
        damage_throw = dices.dice_throw_advantage(attack_dict['damage_dice'], damage_throw_advantage)
        # Если атака критическая, бросаем кость урона дважды:
        # Если атака неудачная, то независимо от модификаторов результат нулевой:
        # Атаки по бессознательным вблизи всегда дают критическое попадание.
        if attack_throw >= crit_range or attack_dict['attack_range'] <= 5 and enemy_soldier.sleep:
            damage_throw = 0
            for throw in range(0, self.crit_multiplier):
                damage_throw += dices.dice_throw_advantage(attack_dict['damage_dice'],
                        damage_throw_advantage)
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
                sneak_attack_throw = dices.dice_throw_advantage(self.proficiency['sneak_attack_dice'])
                damage_throw += sneak_attack_throw
                if attack_throw >= crit_range\
                        or attack_dict['attack_range'] <= 5 and enemy_soldier.sleep:
                    # Критический удар удваивает урон от скрытной атаки:
                    sneak_attack_throw = dices.dice_throw_advantage(self.proficiency['sneak_attack_dice'])
                    damage_throw += sneak_attack_throw
        # Заклинание Absorb_Elements усиливает атаку за счёт поглощённой энергии:
        if self.damage_absorbed:
            damage_absorbed_throw = dices.dice_throw_advantage(self.damage_absorbed['damage_dice'])
            damage_throw += damage_absorbed_throw
            self.damage_absorbed = None
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
                        and advantage and not disadvantage:
                    damage_throw_mod += 10
                    attack_throw_mod -=5
            # Снайпер тоже способен усилить урон за счёт точности:
            if 'Sharpshooter' in attack_dict['weapon_skills_use']:
                if enemy_soldier.armor['armor_class'] <= attack_dict['attack_mod'] + 10\
                        and enemy_soldier.hitpoints > damage_throw_mod\
                        and advantage and not disadvantage:
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
                fear = enemy_soldier.set_fear(self, 8 + max(self.mods.values()))
                if fear:
                    print('{side_1}, {c1} {s} FEAR >> {side_2} {c2} {e}'.format(
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
        # TODO: в отдельную функцию:
        # Убираем оружие из списка атак, если закончились боеприпасы:
        # Или пополняем боекомплект за счёт союзного бойца (а надо бойца из отряда).
        # Хотя, ополченцы могут тоже пополнять боекомплект легионеров.
        attacks_list = list(self.attacks.keys())
        if attack_dict.get('ammo'):
            attack_dict['ammo'] -= 1
            if attack_dict.get('ammo_type'):
                ammo_type = attack_dict.get('ammo_type')
            else:
                ammo_type = attack_dict.get('weapon_of_choice')
            #print(ammo_type)
            if attack_dict['ammo'] == 0:
                for soldier in metadict_soldiers.values():
                    if ammo_type in soldier.equipment_weapon\
                            and not soldier.defeat\
                            and soldier.uuid != self.uuid\
                            and soldier.ally_side == self.ally_side\
                            and soldier.equipment_weapon[ammo_type] > 0:
                        # Союзник передаёт боеприпасы бойцу:
                        attack_dict['ammo'] += soldier.equipment_weapon[ammo_type]
                        soldier.unset_weapon(attack_dict.get('weapon_of_choice'), ammo_type)
                        break
                else:
                    self.unset_weapon(attack_dict.get('weapon_of_choice'), ammo_type)
        return attack_result_dict

    def unset_weapon(self, weapon_type, ammo_type = None):
        """Убираем оружие, для которого закончились боеприпасы.
        
        Скорость бойца при этом пересчитывается.
        """
        attacks_list = list(self.attacks.keys())
        for attack in attacks_list:
            if attack[-1] == weapon_type:
                self.attacks.pop(attack)
        if ammo_type:
            self.equipment_weapon[ammo_type] = 0
            self.overload = self.calculate_overload()
            self.base_speed = self.overload['base_speed']

    def unset_shield(self):
        """Бросаем щит, если он есть."""
        if self.armor['shield_use']:
            self.armor['armor_class'] -= self.armor['armor_class_shield']
            self.armor['armor_class_armor_impact'] -= self.armor['armor_class_shield']
            self.armor['armor_class_shield_impact'] -= self.armor['armor_class_shield']
            self.armor['armor_class_shield'] = 0
            self.armor['shield_use'] = None
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
            if self.armor['armor_class_shield'] <= 0:
                self.armor['armor_class_shield'] = 0
                shield_type = self.armor['shield_use']
                self.equipment_weapon[shield_type] = 0
                self.overload = self.calculate_overload()
                self.base_speed = self.overload['base_speed']
                self.armor['shield_use'] = None
            #print(self.ally_side, self.place, self.behavior, self.armor)

    def spell_attack(self, attack_dict, enemy, advantage = False, disadvantage = False):
        """Атака заклинанием.
        
        Вроде магической стрелы, которая всегда попадает,
        Или бьющего по местности огненного шара.
        """
        damage_throw = dices.dice_throw_advantage(attack_dict['damage_dice'])
        damage_throw_mod = damage_throw + attack_dict['damage_mod']
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
        savethrow_bonus = 0
        if cover >= 4 and cover < 7:
            armor_class_no_impact += 2
            armor_class_shield_impact += 2
            armor_class_armor_impact += 2
            armor_class += 2
            savethrow_bonus += 2
        elif cover >= 7:
            armor_class_no_impact += 5
            armor_class_shield_impact += 5
            armor_class_armor_impact += 5
            armor_class += 5
            savethrow_bonus += 5
        attack_dict['savethrow_bonus'] = savethrow_bonus
        # TODO: в отдельную функцию:
        # Реакцией срабатывает волшебный щит.
        if self.equipment_weapon.get('Rune of Shielding') and self.reaction == True and not self.shield:
            if attack_dict.get('attack') and attack_dict['attack'] > armor_class\
                    or attack_choice[-1] == 'Magic_Missile':
                self.equipment_weapon['Rune of Shielding'] -= 1
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
        # Учитываем реакцию Feat_Defensive_Duelist:
        if attack_choice[0] == 'close' or attack_choice[0] == 'reach':
            if self.class_features.get('Feat_Defensive_Duelist')\
                    and self.reaction == True\
                    and attack_dict['attack'] > armor_class:
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
                    #success = True
                    #print('[+++] {0} {1} {2} cover {3} reaction Def Duel {4}/{5} AC crit {6}, success {7}, damage {8}'.format(
                    #    self.ally_side, self.place, self.behavior,
                    #    cover, armor_class, armor_dict['armor_class'],
                    #    attack_dict['attack_crit'], success, attack_dict['damage']))
                #else:
                #    success = False
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
        if attack_dict.get('attack'):
            if attack_dict['attack_crit'] == True:
                result['hit'] = True
                result['crit'] = True
                enemy_soldier = metadict_soldiers[attack_dict['sender_uuid']]
            elif attack_dict['attack'] > armor_class:
                result['hit'] = True
            elif attack_dict['attack'] <= armor_class_no_impact:
                result['miss'] = True
            elif attack_dict['attack'] <= armor_class_shield_impact:
                # Homebrew. Пилумы застревают в щитах, мешая их использовать:
                result['shield_impact'] = True
                if attack_dict.get('shield_breaker'):
                    self.set_shield_break()
            elif attack_dict['attack'] <= armor_class_armor_impact:
                result['armor_impact'] = True
            elif attack_dict['attack'] <= 0 or attack_dict['attack_loss']:
                result['clumsy_miss'] = True
        elif attack_dict.get('direct_hit'):
            result['hit'] = True
        # Если атака прошла, переходим к расчёту ранений:
        attack_dict.update(result)
        if attack_dict['hit'] == True:
            attack_dict = self.take_damage(attack_choice, attack_dict, metadict_soldiers)
            # TODO: способность не используется.
            # ------------------------------------------------------------
            # Монахи сначала пытаются сбить с ног. Сбивание, захват, удары.
            # Выбивание реакции тем не менее полезно, если враг щитовик.
            # ------------------------------------------------------------
            # Атака монаха может сбить с ног:
            if 'Open_Hand_Technique' in attack_dict and self.prone == False:
                enemy_soldier = metadict_soldiers[attack_dict['sender_uuid']]
                attack_dict['fall_prone'] = self.set_fall_prone(enemy_soldier)
            # Или лишить реакции:
            elif 'Open_Hand_Technique' in attack_dict and self.prone == True:
                self.reaction = False
        return attack_dict

    def take_damage(self, attack_choice, attack_dict, metadict_soldiers):
        """Боец реагирует на повреждения.
        
        По правилам DnD 5.0:
        - Ранен на 100% хитов -- потеря сознания, борьба за жизнь.
        - Ранен на 200% от макс. числа хитов -- мгновенная смерть.
        """
        enemy_soldier = metadict_soldiers[attack_dict['sender_uuid']]
        damage = attack_dict['damage']
        # Спящий просыпается, если ранен:
        if self.sleep:
            self.sleep_timer = 0
            self.sleep = False
        # Удачный спасбросок может уполовинить урон:
        if attack_dict.get('savethrow'):
            savethrow_ability = attack_dict['savethrow_ability']
            # Помеха врага -- преимущество нам:
            advantage = attack_dict['disadvantage']
            disadvantage = attack_dict['advantage']
            if savethrow_ability == 'dexterity':
                if self.dodge_action or self.class_features.get('Danger_Sense'):
                    advantage = True
                if self.restained:
                    disadvantage = True
            damage_difficul = attack_dict['spell_save_DC']
            damage_savethrow = dices.dice_throw_advantage('1d20', advantage, disadvantage)\
                    + self.saves[savethrow_ability] + attack_dict['savethrow_bonus']
            # Заклинание Bless усиливает спасброски:
            if self.bless:
                damage_savethrow += self.bless
            # Bardic_Inspiration усиливает спасбросок:
            if self.bardic_inspiration\
                    and damage_savethrow < damage_difficul\
                    and not damage_savethrow + self.bardic_inspiration < damage_difficul:
                damage_savethrow += self.bardic_inspiration
                self.bardic_inspiration = None
            if attack_dict.get('ignore_cover'):
                damage_savethrow = dices.dice_throw_advantage('1d20', advantage, disadvantage)\
                        + self.saves[savethrow_ability]
            if damage_savethrow >= damage_difficul:
                damage = round(damage / 2)
                if attack_dict.get('savethrow_all'):
                    attack_dict['hit'] = False
                    damage = 0
            if not damage == 0 and attack_dict.get('effect'):
                if attack_dict['effect'] == 'mockery':
                    self.mockery = True
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
            if self.equipment_weapon.get('Rune of Absorbtion') and self.reaction == True:
                absorb_list = self.metadict_items['Rune of Absorbtion']['absorb_damage_type']
                if attack_dict['damage_type'] in absorb_list:
                    self.reaction = False
                    self.equipment_weapon['Rune of Absorbtion'] -= 1
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
        # Варвары -- настоящие чудовища, плевать они хотели на копья и мечи:
        # TODO: волшебное оружие преодолевает сопротивляемость варваров.
        if attack_dict['damage_type'] in self.resistance:
            if enemy_soldier.class_features.get('Feat_Elemental_Adept') == attack_dict['damage_type']:
                damage = damage
            elif attack_dict.get('weapon_type') and 'magic' in attack_dict['weapon_type']:
                damage = damage
            else:
                damage = round(damage * 0.5)
        if attack_dict['damage_type'] in self.immunity:
            if attack_dict.get('weapon_type') and 'magic' in attack_dict['weapon_type']:
                damage = damage
            else:
                damage = 0
        # Бонусные хиты от Feat_Inspiring_Leader и подобного:
        if self.bonus_hitpoints and self.bonus_hitpoints > 0:
            shield_of_bravery = self.bonus_hitpoints
            self.bonus_hitpoints -= damage
            damage = damage - shield_of_bravery
            if self.bonus_hitpoints < 0:
                self.bonus_hitpoints = 0
        # Отражение/перехват стрел монахом (15-25 срабатываний за бой с лучниками):
        # https://www.dandwiki.com/wiki/5e_SRD:Monk#Deflect_Missiles
        if attack_choice[0] == 'throw' or attack_choice[0] == 'ranged' or attack_choice[0] == 'volley':
            if self.class_features.get('Deflect_Missiles') and self.reaction == True:
                damage_deflect = dices.dice_throw('1d10') + self.mods['dexterity'] + self.level
                damage -= damage_deflect
                self.reaction = False
                print('{0} {1} {2} {3} crit {4} damage {5} reaction deflect -{6}'.format(
                    self.ally_side, self.place, self.behavior,
                    attack_choice, attack_dict['attack_crit'],
                    attack_dict['damage'], damage_deflect))
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
        # Стойкость нежити (зомби не так-то просто убить):
        if self.class_features.get('Undead_Fortitude') and self.hitpoints <= 0\
                and not attack_dict.get('attack_crit')\
                and attack_dict['damage_type'] != 'radiant':
            destruction_difficul = 5 + damage
            destruction_saving_throw = dices.dice_throw_advantage('1d20') + self.saves['constitution']
            if destruction_saving_throw > destruction_difficul:
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
        if self.hitpoints <= 0:
            attack_dict['fatal_hit'] = True
        return attack_dict
