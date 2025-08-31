from champions.champion import Champion
from damage.pre_mitigation_damage import PreMitigationDamage


class Rune:
    def __init__(
            self,
            name : str,
            ability_haste : int = 0,
            ability_power : int = 0,
            ability_power_percentage : int = 0,
            attack_damage : int = 0,
            attack_damage_percentage : int = 0,
            attack_speed : int = 0,
            armor : int = 0,
            armor_penetration_percentage : int = 0,
            crit_chance : int = 0,
            crit_amplification : int = 0,
            hp : int = 0,
            hp_regeneration_percentage : int = 0,
            lethality : int = 0,
            life_steal : int = 0,
            magic_penetration : int = 0,
            magic_penetration_percentage : int = 0,
            magic_resist : int = 0,
            movement_speed : int = 0            
            ):
        
        # Rune Information
        self.__name : str = name

        # Rune Stats
        self.__ability_haste : int = ability_haste
        self.__ability_power : int = ability_power
        self.__ability_power_percentage : int = ability_power_percentage
        self.__attack_damage : int = attack_damage
        self.__attack_damage_percentage : int = attack_damage_percentage
        self.__attack_speed : int = attack_speed
        self.__armor : int = armor
        self.__armor_penetration_percentage : int = armor_penetration_percentage
        self.__crit_chance : int = crit_chance
        self.__crit_amplification : int = crit_amplification
        self.__hp : int = hp
        self.__hp_regeneration_percentage : int = hp_regeneration_percentage
        self.__lethality : int = lethality
        self.__life_steal : int = life_steal
        self.__magic_penetration : int = magic_penetration
        self.__magic_penetration_percentage : int = magic_penetration_percentage
        self.__magic_resist : int = magic_resist
        self.__movement_speed : int = movement_speed  

    def add_to_champion(self, champion : Champion):
        champion.add_bonus_ability_haste(bonus_ability_haste = self.__ability_haste)
        champion.add_bonus_ability_power(bonus_ability_power = self.__ability_power)
        champion.add_bonus_ability_power_percentage(bonus_ability_power_percentage = self.__ability_power_percentage)
        champion.add_bonus_attack_damage(bonus_attack_damage = self.__attack_damage)
        champion.add_bonus_attack_damage_percentage(bonus_attack_damage_percentage = self.__attack_damage_percentage)
        champion.add_bonus_attack_speed(bonus_attack_speed = self.__attack_speed)
        champion.add_bonus_armor(bonus_armor = self.__armor)
        champion.add_bonus_armor_penetration_percentage(bonus_armor_penetration_percentage = self.__armor_penetration_percentage)
        champion.add_bonus_crit_chance(bonus_crit_chance = self.__crit_chance)
        champion.add_bonus_crit_amplification(bonus_crit_amplification = self.__crit_amplification)
        champion.add_bonus_hp(bonus_hp = self.__hp)
        champion.add_bonus_hp_regeneration_percentage(bonus_hp_regeneration_percentage = self.__hp_regeneration_percentage)
        champion.add_bonus_lethality(bonus_lethality = self.__lethality)
        champion.add_bonus_life_steal(bonus_life_steal = self.__life_steal)
        champion.add_bonus_magic_penetration(bonus_magic_penetration = self.__magic_penetration)
        champion.add_bonus_magic_penetration_percentage(bonus_magic_penetration_percentage = self.__magic_penetration_percentage)
        champion.add_bonus_magic_resist(bonus_magic_resist = self.__magic_resist)
        champion.add_bonus_movement_speed(bonus_movement_speed = self.__movement_speed)

    def get_ability_haste(self) -> int:
        return self.__ability_haste
    
    def get_ability_power(self) -> int:
        return self.__ability_power
    
    def get_ability_power_percentage(self) -> float:
        return self.__ability_power_percentage

    def get_attack_damage(self) -> int:
        return self.__attack_damage
    
    def get_attack_damage_percentage(self) -> float:
        return self.__attack_damage_percentage
    
    def get_attack_speed(self) -> int:
        return self.__attack_speed
    
    def get_armor(self) -> int:
        return self.__armor
    
    def get_armor_penetration_percentage(self) -> int:
        return self.__armor_penetration_percentage
    
    def get_crit_amplification(self) -> int:
        return self.__crit_amplification

    def get_crit_chance(self) -> int:
        return self.__crit_chance
    
    def get_hp(self) -> int:
        return self.__hp
    
    def get_hp_regeneration_percentage(self) -> int:
        return self.__hp_regeneration_percentage
    
    def get_lethality(self) -> int:
        return self.__lethality
    
    def get_life_steal(self) -> int:
        return self.__life_steal
    
    def get_magic_penetration(self) -> int:
        return self.__magic_penetration
    
    def get_magic_penetration_percentage(self) -> int:
        return self.__magic_penetration_percentage
    
    def get_magic_resist(self) -> int:
        return self.__magic_resist
    
    def get_movement_speed(self) -> int:
        return self.__movement_speed
    
    def get_name(self) -> str:
        return self.__name

    def on_damage(self, pre_mitigation_damage : PreMitigationDamage, source : Champion, target : Champion) -> PreMitigationDamage:
        raise NotImplementedError