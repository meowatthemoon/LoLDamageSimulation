from random import uniform

from damage.damage_type import DamageType
from damage.damage_information import DamageInformation

class Champion:
    def __init__(
            self, 
            name : str,
            base_attack_damage : int,
            base_attack_range : int,
            base_attack_speed : float,
            base_armor : int, 
            base_hp : int, 
            base_hp_regeneration : int, 
            base_magic_resist : int, 
            base_movement_speed : int,
            scaling_attack_damage : float,
            scaling_armor : float,
            scaling_hp : float,
            scaling_hp_regeneration : float,
            scaling_magic_resist : float,
            base_crit_amplification : int = 75
    ):
        # Champion Information
        self.__name : str = name

        # Base Stats
        self.__base_attack_damage : float = base_attack_damage
        self.__base_attack_range : int = base_attack_range
        self.__base_attack_speed : float = base_attack_speed
        self.__base_armor : int = base_armor
        self.__base_crit_amplification : int = base_crit_amplification
        self.__base_hp : int = base_hp
        self.__base_hp_regeneration : float = base_hp_regeneration
        self.__base_magic_resist : int = base_magic_resist
        self.__base_movement_speed : int = base_movement_speed

        # Scaling Stats
        self.__scaling_attack_damage : float = scaling_attack_damage
        self.__scaling_armor : float = scaling_armor
        self.__scaling_hp : float = scaling_hp
        self.__scaling_hp_regeneration : float = scaling_hp_regeneration
        self.__scaling_magic_resist : float = scaling_magic_resist

        # Bonus Stats
        self.__bonus_ability_haste : int = 0
        self.__bonus_ability_power : int = 0
        self.__bonus_ability_power_percentage : int = 0
        self.__bonus_attack_damage : int = 0
        self.__bonus_attack_damage_percentage : int = 0
        self.__bonus_attack_speed : int = 0
        self.__bonus_armor_penetration_percentage : int = 0
        self.__bonus_armor : int = 0
        self.__bonus_crit_amplification : int = 0
        self.__bonus_crit_chance : int = 0
        self.__bonus_hp : int = 0
        self.__bonus_hp_regeneration_percentage : int = 0
        self.__bonus_lethality : int = 0
        self.__bonus_life_steal : int = 0
        self.__bonus_magic_penetration : int = 0
        self.__bonus_magic_penetration_percentage : int = 0
        self.__bonus_magic_resist : int = 0
        self.__bonus_movement_speed : int = 0

        # De-buffs
        self.__total_armor_reduction_debuff : int = 0
        self.__total_magic_resist_reduction_debuff : int = 0

        # Champion Variables
        self.__level : int = 0
        self.__q_rank : int = 0
        self.__w_rank : int = 0
        self.__e_rank : int = 0
        self.__r_rank : int = 0
        self.__current_hp : float = self.get_total_hp()

    def add_bonus_ability_haste(self, bonus_ability_haste : int):
        self.__bonus_ability_haste += bonus_ability_haste

    def add_bonus_ability_power(self, bonus_ability_power : int):
        self.__bonus_ability_power += bonus_ability_power

    def add_bonus_ability_power_percentage(self, bonus_ability_power_percentage : int):
        self.__bonus_ability_power_percentage += bonus_ability_power_percentage

    def add_bonus_attack_damage(self, bonus_attack_damage : int):
        self.__bonus_attack_damage += bonus_attack_damage

    def add_bonus_attack_damage_percentage(self, bonus_attack_damage_percentage : int):
        self.__bonus_attack_damage_percentage += bonus_attack_damage_percentage

    def add_bonus_attack_speed(self, bonus_attack_speed : int):
        self.__bonus_attack_speed += bonus_attack_speed

    def add_bonus_armor(self, bonus_armor : int):
        self.__bonus_armor += bonus_armor

    def add_bonus_armor_penetration_percentage(self, bonus_armor_penetration_percentage : int):
        self.__bonus_armor_penetration_percentage += bonus_armor_penetration_percentage

    def add_bonus_crit_chance(self, bonus_crit_chance : int):
        self.__bonus_crit_chance += bonus_crit_chance

    def add_bonus_crit_amplification(self, bonus_crit_amplification : int):
        self.__bonus_crit_amplification += bonus_crit_amplification

    def add_bonus_hp(self, bonus_hp : int):
        self.__bonus_hp += bonus_hp
        self.__current_hp += bonus_hp

    def add_bonus_hp_regeneration_percentage(self, bonus_hp_regeneration_percentage : int):
        self.__bonus_hp_regeneration_percentage += bonus_hp_regeneration_percentage

    def add_bonus_lethality(self, bonus_lethality : int):
        self.__bonus_lethality += bonus_lethality

    def add_bonus_life_steal(self, bonus_life_steal : int):
        self.__bonus_life_steal += bonus_life_steal

    def add_bonus_magic_penetration(self, bonus_magic_penetration : int):
        self.__bonus_magic_penetration += bonus_magic_penetration

    def add_bonus_magic_penetration_percentage(self, bonus_magic_penetration_percentage : int):
        self.__bonus_magic_penetration_percentage += bonus_magic_penetration_percentage

    def add_bonus_magic_resist(self, bonus_magic_resist : int):
        self.__bonus_magic_resist += bonus_magic_resist

    def add_bonus_movement_speed(self, bonus_movement_speed : int):
        self.__bonus_movement_speed += bonus_movement_speed

    def auto_attack(self, ensure_crit : bool = False, median_crit : bool = False) -> DamageInformation:
        attack_damage : float = self.get_total_attack_damage()

        # Crit Amplification
        crit_damage_amplification : float = 0
        crit_chance : float = self.get_total_crit_chance()
        is_crit : bool = False
        if crit_chance > 0:
            crit_amplification : int = self.get_total_crit_amplification()

            if ensure_crit:
                crit_damage_amplification = crit_amplification / 100
                is_crit = True
            elif median_crit:
                crit_damage_amplification = crit_amplification / 100 * crit_chance / 100
                is_crit = True
            elif uniform(0, 1) < crit_chance / 100:
                crit_damage_amplification = crit_amplification / 100
                is_crit = True
                
        attack_damage += attack_damage * crit_damage_amplification

        return DamageInformation(
            source_name = "Auto Attack",
            damage_value = attack_damage,
            damage_type = DamageType.PhysicalDamage,
            is_amplifiable_by_runes = True,
            is_champion_ability = False,
            is_champion_auto_attack = True,
            is_crit = is_crit,
            is_item = False,
            is_rune = False,
            is_single_target = True
        )
    
    def get_current_hp(self) -> float:
        return self.__current_hp
    
    def get_level(self) -> int:
        return self.__level

    def get_name(self) -> str:
        return self.__name
    
    def get_base_armor(self) -> float:
        return self.__calculate_base_stat(base_stat = self.__base_armor, scaling_stat = self.__scaling_armor)

    def get_base_attack_damage(self) -> float:
        return self.__calculate_base_stat(base_stat = self.__base_attack_damage, scaling_stat = self.__scaling_attack_damage)
    
    def get_base_crit_amplification(self) -> float:
        return self.__base_crit_amplification
    
    def get_base_hp(self) -> float:
        return self.__calculate_base_stat(base_stat = self.__base_hp, scaling_stat = self.__scaling_hp)
    
    def get_base_magic_resist(self) -> float:
        return self.__calculate_base_stat(base_stat = self.__base_magic_resist, scaling_stat = self.__scaling_magic_resist)
    
    def get_bonus_armor(self) -> float:
        return self.__bonus_armor

    def get_bonus_attack_damage(self) -> float:
        bonus_attack_damage_ratio : float = self.__bonus_attack_damage_percentage / 100

        return self.__bonus_attack_damage * (1 + bonus_attack_damage_ratio)
    
    def get_bonus_ability_power(self) -> float:
        bonus_ability_power_ratio : float = self.__bonus_ability_power_percentage / 100

        return self.__bonus_ability_power * (1 + bonus_ability_power_ratio)
    
    def get_bonus_crit_amplification(self):
        return self.__bonus_crit_amplification

    def get_bonus_hp(self) -> float:
        return self.__bonus_hp
    
    def get_bonus_magic_resist(self) -> float:
        return self.__bonus_magic_resist

    def get_total_armor(self) -> float:
        return self.get_base_armor() + self.get_bonus_armor()

    def get_total_armor_penetration_percentage(self) -> float:
        return self.__bonus_armor_penetration_percentage
    
    def get_total_armor_reduction_debuff(self) -> float:
        return self.__total_armor_reduction_debuff

    def get_total_attack_damage(self) -> float:
        return self.get_base_attack_damage() + self.get_bonus_attack_damage()
    
    def get_total_crit_amplification(self) -> int:
        return self.get_base_crit_amplification() + self.get_bonus_crit_amplification()

    def get_total_crit_chance(self) -> float:
        return self.__bonus_crit_chance
    
    def get_total_lethality(self) -> float:
        return self.__bonus_lethality
    
    def get_total_hp(self) -> float:
        return self.get_base_hp() + self.get_bonus_hp()
    
    def get_total_magic_penetration(self) -> float:
        return self.__bonus_magic_penetration
    
    def get_total_magic_penetration_percentage(self) -> float:
        return self.__bonus_magic_penetration_percentage
    
    def get_total_magic_resist(self) -> float:
        return self.get_base_magic_resist() + self.get_bonus_magic_resist()
    
    def get_total_magic_resist_reduction_debuff(self) -> float:
        return self.__total_magic_resist_reduction_debuff
    
    def get_q_rank(self):
        return self.__q_rank

    def get_w_rank(self):
        return self.__w_rank

    def get_e_rank(self):
        return self.__e_rank

    def get_r_rank(self):
        return self.__r_rank

    def set_level(self, level : int):
        self.__level : int = level

    def set_q_rank(self, rank : int):
        self.__q_rank : int = rank

    def set_w_rank(self, rank : int):
        self.__w_rank : int = rank

    def set_e_rank(self, rank : int):
        self.__e_rank : int = rank

    def set_r_rank(self, rank : int):
        self.__r_rank : int = rank

    def take_damage(self, damage : DamageInformation) -> DamageInformation:
        assert not damage.pre_mitigation, "Received pre-mitigated damage."
        damage_taken = damage.damage_value if self.get_current_hp() >= damage.damage_value  else self.get_current_hp()
        self.__current_hp -= damage_taken
        return DamageInformation(
            source_name = damage.source_name,
            damage_type = damage.damage_type,
            damage_value = damage_taken,
            is_amplifiable_by_runes = damage.is_amplifiable_by_runes,
            is_champion_ability = damage.is_champion_ability,
            is_champion_auto_attack = damage.is_champion_auto_attack,
            is_crit = damage.is_crit,
            is_item = damage.is_item,
            is_rune = damage.is_rune,
            is_single_target = damage.is_single_target,
            pre_mitigation = False
        )

    def __calculate_base_stat(self, base_stat : float, scaling_stat):
        return base_stat + scaling_stat * (self.__level - 1) * (0.7025 + 0.0175 * (self.__level - 1))
    
    