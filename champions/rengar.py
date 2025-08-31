from champions.champion import Champion
from damage.damage_type import DamageType
from damage.pre_mitigation_damage import PreMitigationDamage

class Rengar(Champion):
    def __init__(self):
        super().__init__(
            name = "Rengar",
            base_attack_damage = 68,
            base_armor = 34,
            base_hp = 590,
            base_hp_regeneration = 6,
            base_magic_resist = 32,
            scaling_attack_damage = 3,
            scaling_armor = 4.2,
            scaling_hp = 104,
            scaling_hp_regeneration = 0.5,
            scaling_magic_resist = 2.05,
            base_movement_speed = 345,
            base_attack_speed = 0.667,
            base_attack_range = 125
        ) 

        self.__q_name : str = "Savagery"    
        self.__w_name : str = "Battle Roar"
        self.__e_name : str = "Bola Strike"
        self.__r_name : str = "Thrill of the Hunt" 

        self.__passive_stacks : int = 0

        print("WARNING: Rengar Constructor has ability names, this should be generalized for all champions in the future!")
        print("WARNING: Rengar Constructor - have to double check base stats!")
        print("WARNING: Rengar missing Q function!")
        print("WARNING: Rengar missing W function!")
        print("WARNING: Rengar missing E function!")
        print("WARNING: Rengar missing R function!")

    def get_passive_stacks(self) -> int:
        return self.__passive_stacks
    
    def set_passive_stacks(self, passive_stacks : int):
        assert 7 > passive_stacks > -1, f"Invalid number for Rengar's passive stacks: {passive_stacks}."
        old_bonus_attack_damage_percentage = self.__passive_stacks ** 2
        new_bonus_attack_damage_percentage = passive_stacks ** 2
        self.__bonus_attack_damage_percentage += new_bonus_attack_damage_percentage - old_bonus_attack_damage_percentage # I dont think we can access this variable so ye may have to change it to just _
        self.__passive_stacks = passive_stacks

    def press_q(self, empowered : bool = False) -> PreMitigationDamage:
        total_attack_damage = self.get_total_attack_damage()

        # Calculate the flat damage (BASE and AD scaling)
        if empowered:
            q_attack_damage_ratio = 1.3
            q_base_damage = 15 + 15 * self.get_level()
            if self.get_level() > 8:
                q_base_damage -= 5 * (self.get_level() - 8)
        else:
            q_attack_damage_ratio = 1 + 3.75 / 100 * (self.get_q_rank() - 1)
            q_base_damage = 30 * self.get_q_rank()
        flat_damage : float = q_base_damage + q_attack_damage_ratio * total_attack_damage

        # Crit scaling (CRIT CHANCE, CRIT DAMAGE and AD scaling)
        has_infinity_edge = self.get_total_crit_amplification() > 75

        crit_scaling = (0.3125 + 0.3 if has_infinity_edge else 0) * self.get_total_crit_chance() + (40 if has_infinity_edge else 0) 
        crit_ratio = crit_scaling / 100
        crit_damage = crit_ratio * total_attack_damage
        
        # Add the sum of both parts
        q_damage = flat_damage + crit_damage

        return PreMitigationDamage(
            source_name = f"{'Empowered 'if empowered else ''}{self.__q_name}",
            damage_value = q_damage,
            damage_type = DamageType.PhysicalDamage,
            is_amplifiable_by_runes = True,
            is_champion_auto_attack = True,
            is_champion_ability = True,
            is_crit = True,
            is_item = False,
            is_rune = False,
            is_single_target = True
        )

    def press_w(self, empowered : bool = False) -> PreMitigationDamage:
        if empowered:
            w_base_damage = 40 + 10 * self.get_level()
            w_ability_power_ratio = 0.8
        else:
            w_base_damage = 20 + 30 * self.get_w_rank()
            w_ability_power_ratio = 0.8

        w_damage : float = w_base_damage + self.get_bonus_ability_power() * w_ability_power_ratio

        return PreMitigationDamage(
            source_name = f"{'Empowered 'if empowered else ''}{self.__w_name}",
            damage_value = w_damage,
            damage_type = DamageType.MagicalDamage,
            is_amplifiable_by_runes = True,
            is_champion_auto_attack = False,
            is_champion_ability = True,
            is_crit = False,
            is_item = False,
            is_rune = False,
            is_single_target = False
        )

    def press_e(self, empowered : bool = False) -> PreMitigationDamage:
        if empowered:
            e_base_damage = 35 + 15 * self.get_level()
        else:
            e_base_damage = 10 + 45 * self.get_e_rank()
        
        e_bonus_attack_damage_ratio = 0.8

        e_damage : float = e_base_damage + self.get_bonus_attack_damage() * e_bonus_attack_damage_ratio

        return PreMitigationDamage(
            source_name = f"{'Empowered 'if empowered else ''}{self.__e_name}",
            damage_value = e_damage,
            damage_type = DamageType.PhysicalDamage,
            is_amplifiable_by_runes = True,
            is_champion_auto_attack = False,
            is_champion_ability = True,
            is_crit = False,
            is_item = False,
            is_rune = False,
            is_single_target = True
        )
    
    def press_r(self, ult_bonus : bool = False) -> PreMitigationDamage:
        ult_damage : float = self.get_total_attack_damage() if ult_bonus else 0

        # TODO Amor Reduction De-buff
        print("WARNING: You haven't implemented Rengar's Ult Amor Reduction De-Buff!")

        return PreMitigationDamage(
            source_name = self.__r_name,
            damage_value = ult_damage,
            damage_type = DamageType.PhysicalDamage,
            is_amplifiable_by_runes = True,
            is_champion_auto_attack = False,
            is_champion_ability = True,
            is_crit = False,
            is_item = False,
            is_rune = False,
            is_single_target = True
        )