from champions.champion import Champion
from damage.pre_mitigation_damage import PreMitigationDamage
from runes.rune import Rune

class RuneStatAttackDamage(Rune):
    def __init__(self):
        super().__init__(name = "Rune Stat Attack Damage", attack_damage = 5.4)

    def on_damage(self, pre_mitigation_damage : PreMitigationDamage, source : Champion, target : Champion) -> PreMitigationDamage:
        return None