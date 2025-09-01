from champions.champion import Champion
from damage.damage_information import DamageInformation
from runes.rune import Rune

class RuneStatAbilityPower(Rune):
    def __init__(self):
        super().__init__(name = "Rune Stat Ability Power", ability_power = 9)

    def on_damage(self, pre_mitigation_damage : DamageInformation, source : Champion, target : Champion) -> DamageInformation:
        return None