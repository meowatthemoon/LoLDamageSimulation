from dataclasses import dataclass

from damage.damage_type import DamageType

@dataclass
class DamageInformation:
    source_name : str
    damage_value : float
    damage_type : DamageType
    is_amplifiable_by_runes : bool
    is_champion_ability : bool
    is_champion_auto_attack : bool
    is_crit : bool
    is_item : bool
    is_rune : bool
    is_single_target : bool
    pre_mitigation : bool