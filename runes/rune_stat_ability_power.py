from champions.champion import Champion
from damage.pre_mitigation_damage import PreMitigationDamage
from runes.rune import Rune

class RuneStatAbilityPower(Rune):
    def __init__(self):
        super().__init__(name = "Rune Stat Ability Power", ability_power = 9)

    def on_damage(self, pre_mitigation_damage : PreMitigationDamage, source : Champion, target : Champion) -> PreMitigationDamage:
        return None