from champions.champion import Champion
from damage.damage_type import DamageType
from damage.damage_information import DamageInformation
from runes.rune import Rune

DAMAGE_AMPLIFICATION_PERCENTAGE = 8

class PressTheAttack(Rune):
    def __init__(self):
        super().__init__(name = "Press the Attack")
        self.__active : bool = False
        self.__stack_count : int = 0

    def on_damage(self, pre_mitigation_damage : DamageInformation, source : Champion, target : Champion) -> DamageInformation:
        if pre_mitigation_damage is None:
            return
        
        if self.__active:
            return DamageInformation(
                source_name = self.get_name(),
                damage_value = pre_mitigation_damage.damage_value * (DAMAGE_AMPLIFICATION_PERCENTAGE / 100),
                damage_type = pre_mitigation_damage.damage_type,
                is_amplifiable_by_runes = False,
                is_champion_ability = False,
                is_champion_auto_attack = False,
                is_crit = False,
                is_item = False,
                is_rune = True,
                is_single_target = pre_mitigation_damage.is_single_target,
                pre_mitigation = True
            )
        elif pre_mitigation_damage.is_champion_auto_attack:
            self.__stack_count += 1
            if self.__stack_count == 3:
                self.__active = True
                return DamageInformation(
                    source_name = self.get_name(),
                    damage_value = 40 + 120 / 17 * (source.get_level() - 1),
                    damage_type = DamageType.PhysicalDamage if source.get_bonus_attack_damage() > source.get_bonus_ability_power() else DamageType.MagicalDamage,
                    is_amplifiable_by_runes = True,
                    is_champion_ability = False,
                    is_champion_auto_attack = False,
                    is_crit = False,
                    is_item = False,
                    is_rune = True,
                    is_single_target = pre_mitigation_damage.is_single_target,
                    pre_mitigation = True
                )