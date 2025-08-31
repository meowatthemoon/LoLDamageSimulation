from champions.champion import Champion
from damage.pre_mitigation_damage import PreMitigationDamage
from runes.rune import Rune

DAMAGE_AMPLIFICATION_HP_CUTOFF_PERCENTAGE = 40
DAMAGE_AMPLIFICATION_PERCENTAGE = 8

class CoupDeGrace(Rune):
    def __init__(self):
        super().__init__(name = "Coup de Grace")

    def on_damage(self, pre_mitigation_damage : PreMitigationDamage, source : Champion, target : Champion) -> PreMitigationDamage:
        if pre_mitigation_damage is None:
            return None
        
        if target.get_current_hp() / target.get_total_hp() < DAMAGE_AMPLIFICATION_HP_CUTOFF_PERCENTAGE / 100:
            amplification = DAMAGE_AMPLIFICATION_PERCENTAGE / 100
        else:
            amplification = 0

        return PreMitigationDamage(
            source_name = self.get_name(),
            damage_value = pre_mitigation_damage.damage_value * amplification,
            damage_type = pre_mitigation_damage.damage_type,
            is_amplifiable_by_runes = False,
            is_champion_ability = False,
            is_champion_auto_attack = False,
            is_crit = False,
            is_item = False,
            is_rune = True,
            is_single_target = pre_mitigation_damage.is_single_target
        )
