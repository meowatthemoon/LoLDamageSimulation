from champions.champion import Champion
from champions.target_dummy import TargetDummy
from champions.rengar import Rengar

from damage.damage_information import DamageInformation
from damage.damage_type import DamageType
from items.infinity_edge import InfinityEdge
from items.item import Item
from items.mortal_reminder import MortalReminder
from items.ravenous_hydra import RavenousHydra
from runes.press_the_attack import PressTheAttack
from runes.cut_down import CutDown
from runes.rune import Rune
from runes.rune_stat_attack_damage import RuneStatAttackDamage

def recursively_apply_runes(pre_mitigation_damage : DamageInformation, source : Champion, target : Champion, runes : list[Rune]) -> list[DamageInformation]:
    damage_sources : list[DamageInformation] = []
    for rune in runes:    
        if rune.get_name() == pre_mitigation_damage.source_name:
            continue
        
        rune_pre_mitigation_damage = rune.on_damage(pre_mitigation_damage = pre_mitigation_damage, source = source, target = target)

        if rune_pre_mitigation_damage is not None:
            damage_sources.append(rune_pre_mitigation_damage)

            if rune_pre_mitigation_damage.is_amplifiable_by_runes:
                damage_sources += recursively_apply_runes(pre_mitigation_damage = rune_pre_mitigation_damage, source = source, target = target, runes = runes)

    return damage_sources


def calculate_post_mitigation_damage(pre_mitigation_damage : DamageInformation, source : Champion, target : Champion) -> DamageInformation:
    if pre_mitigation_damage.damage_type == DamageType.TrueDamage:
        return DamageInformation(
            source_name = pre_mitigation_damage.source_name,
            damage_value = pre_mitigation_damage.damage_value,
            damage_type = pre_mitigation_damage.damage_type,
            is_amplifiable_by_runes = pre_mitigation_damage.is_amplifiable_by_runes,
            is_champion_ability = pre_mitigation_damage.is_champion_ability,
            is_champion_auto_attack = pre_mitigation_damage.is_champion_auto_attack,
            is_crit = pre_mitigation_damage.is_crit,
            is_item = pre_mitigation_damage.is_item,
            is_rune = pre_mitigation_damage.is_rune,
            is_single_target = pre_mitigation_damage.is_single_target,
            pre_mitigation = False
        )
    
    if pre_mitigation_damage.damage_type == DamageType.PhysicalDamage:
        target_resistances = target.get_total_armor()
        target_resistances -= target.get_total_armor_reduction_debuff()
        target_resistances = target_resistances * (1 - source.get_total_armor_penetration_percentage() / 100)
        target_resistances -= source.get_total_lethality()

    elif pre_mitigation_damage.damage_type == DamageType.MagicalDamage:
        target_resistances = target.get_total_magic_resist()
        target_resistances -= target.get_total_magic_resist_reduction_debuff()
        target_resistances = target_resistances * (1 - source.get_total_magic_penetration_percentage() / 100)
        target_resistances -= source.get_total_magic_penetration()

    else:
        raise NotImplementedError("No valid type to calculate post mitigation damage!")
    
    if target_resistances >= 0:
        post_mitigation_damage = pre_mitigation_damage.damage_value * (100 / (100 + target_resistances))
    else:
        post_mitigation_damage = pre_mitigation_damage.damage_value * (2 - (100 / (100 - target_resistances)))

    return DamageInformation(
        source_name = pre_mitigation_damage.source_name,
        damage_value = post_mitigation_damage,
        damage_type = pre_mitigation_damage.damage_type,
        is_amplifiable_by_runes = pre_mitigation_damage.is_amplifiable_by_runes,
        is_champion_ability = pre_mitigation_damage.is_champion_ability,
        is_champion_auto_attack = pre_mitigation_damage.is_champion_auto_attack,
        is_crit = pre_mitigation_damage.is_crit,
        is_item = pre_mitigation_damage.is_item,
        is_rune = pre_mitigation_damage.is_rune,
        is_single_target = pre_mitigation_damage.is_single_target,
        pre_mitigation = False
    )
class Simulation:
    def __init__(
            self, 
            source_champion : Champion, 
            source_champion_level : int, 
            source_champion_q_rank : int,
            source_champion_w_rank : int,
            source_champion_e_rank : int,
            source_champion_r_rank : int,
            source_champion_items : list[Item],
            source_champion_runes : list[Rune],
            target_champion : Champion, 
            target_champion_level : int,
            target_champion_q_rank : int,
            target_champion_w_rank : int,
            target_champion_e_rank : int,
            target_champion_r_rank : int,
            target_champion_items : list[Item] = None,
            target_champion_runes : list[Rune] = None,
        ):

        self.__source_champion : Champion = source_champion
        self.__source_champion.set_level(level = source_champion_level)
        self.__source_champion.set_q_rank(rank = source_champion_q_rank)
        self.__source_champion.set_w_rank(rank = source_champion_w_rank)
        self.__source_champion.set_e_rank(rank = source_champion_e_rank)
        self.__source_champion.set_r_rank(rank = source_champion_r_rank)

        for item in source_champion_items:
            item.add_to_champion(champion = self.__source_champion)

        self.__source_champion_runes : list[Rune] = source_champion_runes
        for rune in source_champion_runes:
            rune.add_to_champion(champion = self.__source_champion)

        self.__target_champion : Champion = target_champion
        self.__target_champion.set_level(level = target_champion_level)
        self.__target_champion.set_q_rank(rank = target_champion_q_rank)
        self.__target_champion.set_w_rank(rank = target_champion_w_rank)
        self.__target_champion.set_e_rank(rank = target_champion_e_rank)
        self.__target_champion.set_r_rank(rank = target_champion_r_rank)

        for item in target_champion_items:
            item.add_to_champion(champion = self.__target_champion)

        for rune in target_champion_runes:
            rune.add_to_champion(champion = self.__target_champion)

    def simulate(self, combo : list, combo_args : list):
        for spell_cast, spell_args in zip(combo, combo_args):
            spell_damage_sources : list[DamageInformation] = []
            spell_pre_mitigation_damage : DamageInformation = spell_cast(*spell_args)
            spell_damage_sources.append(spell_pre_mitigation_damage)
            spell_damage_sources += recursively_apply_runes(
                pre_mitigation_damage = spell_pre_mitigation_damage, 
                source = self.__source_champion, 
                target = self.__target_champion, 
                runes = self.__source_champion_runes
            )

            total_damage_pre_mitigated, total_damage_post_mitigated = 0, 0
            for spell_damage_source in spell_damage_sources:
                total_damage_pre_mitigated += spell_damage_source.damage_value
                post_mitigation_damage = calculate_post_mitigation_damage(
                    pre_mitigation_damage = spell_damage_source, 
                    source = self.__source_champion, 
                    target = self.__target_champion
                )
                total_damage_post_mitigated += post_mitigation_damage.damage_value
                self.__target_champion.take_damage(damage = post_mitigation_damage)

            print(f"{spell_pre_mitigation_damage.source_name}: {int(total_damage_post_mitigated)} ({total_damage_post_mitigated / self.__target_champion.get_total_hp() *100}%)")
        print(f"{self.__target_champion.get_name()} was left with {int(self.__target_champion.get_current_hp())}/{int(self.__target_champion.get_total_hp())} ({self.__target_champion.get_current_hp() / self.__target_champion.get_total_hp() * 100}%)")

if __name__ == '__main__':
    source_champion_class : Champion = Rengar
    target_champion_class : Champion = TargetDummy

    source_champion = source_champion_class()
    target_champion = target_champion_class()
    #main()
    simulation = Simulation(
        source_champion = source_champion, 
        source_champion_level = 18, 
        source_champion_q_rank = 5,
        source_champion_w_rank = 5,
        source_champion_e_rank = 5,
        source_champion_r_rank = 5,
        source_champion_items = [],
        source_champion_runes = [PressTheAttack(), CutDown(), RuneStatAttackDamage(), RuneStatAttackDamage()],
        target_champion = target_champion, 
        target_champion_level = 18,
        target_champion_q_rank = 5,
        target_champion_w_rank = 5,
        target_champion_e_rank = 5,
        target_champion_r_rank = 5,
        target_champion_items = [],
        target_champion_runes = [],
    )

    combo = [
        source_champion_class.press_q,
        source_champion_class.press_w,
        source_champion_class.press_e,
        source_champion_class.auto_attack,
        source_champion_class.press_q,
    ]
    combo_args = [
        (source_champion, False),
        (source_champion, False),
        (source_champion, False),
        (source_champion,),
        (source_champion, True),
    ]

    simulation.simulate(combo = combo, combo_args = combo_args)