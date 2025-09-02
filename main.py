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


def main():
    # Source Champion
    rengar = Rengar()
    
    rengar.set_level(level = 18)
    rengar.set_q_rank(rank = 5)
    rengar.set_w_rank(rank = 5)
    rengar.set_e_rank(rank = 5)
    rengar.set_r_rank(rank = 3)

    # Runes
    runes : list[Rune] = [PressTheAttack(), CutDown(), RuneStatAttackDamage(), RuneStatAttackDamage()]
    for rune in runes:
        rune.add_to_champion(champion = rengar)

    # Items
    items : list[Item] = [RavenousHydra(), MortalReminder(), InfinityEdge()]
    for item in items:
        item.add_to_champion(champion = rengar)

    # Target Champion
    dummy = TargetDummy()

    # Simulation
    # Q - Savagery
    damage_sources : list[DamageInformation] = []
    normal_q_pre_mitigation_damage = rengar.press_q(empowered = False)
    damage_sources.append(normal_q_pre_mitigation_damage)
    damage_sources += recursively_apply_runes(pre_mitigation_damage = normal_q_pre_mitigation_damage, source = rengar, target = dummy, runes = runes)
    total_pre = 0
    total_post = 0
    for damage_source in damage_sources:
        total_pre += damage_source.damage_value
        post_mitigation_damage = calculate_post_mitigation_damage(pre_mitigation_damage = damage_source, source = rengar, target = dummy)
        total_post += post_mitigation_damage.damage_value
        result_damage = dummy.take_damage(damage = post_mitigation_damage)
        print(f"{result_damage.source_name} : {result_damage.damage_value} ({result_damage.damage_value / dummy.get_total_hp() * 100})")
    print(f"TOTAL PRE : {total_pre}")
    print(f"TOTAL POST: {total_post}")
    print("-"*20)

    damage_sources : list[DamageInformation] = []
    empowered_q_pre_mitigation_damage = rengar.press_q(empowered = True)
    damage_sources.append(empowered_q_pre_mitigation_damage)
    damage_sources += recursively_apply_runes(pre_mitigation_damage = empowered_q_pre_mitigation_damage, source = rengar, target = dummy, runes = runes)
    total_pre = 0
    total_post = 0
    for damage_source in damage_sources:
        total_pre += damage_source.damage_value
        post_mitigation_damage = calculate_post_mitigation_damage(pre_mitigation_damage = damage_source, source = rengar, target = dummy)
        total_post += post_mitigation_damage.damage_value
        result_damage = dummy.take_damage(damage = post_mitigation_damage)
        print(f"{result_damage.source_name} : {result_damage.damage_value} ({result_damage.damage_value / dummy.get_total_hp() * 100})")
    print(f"TOTAL PRE : {total_pre}")
    print(f"TOTAL POST: {total_post}")
    print("-"*20)

    """
    # W - Battle Roar
    damage_sources : list[DamageInformation] = []
    normal_w_pre_mitigation_damage = rengar.press_w(empowered = False)
    damage_sources.append(normal_w_pre_mitigation_damage)
    damage_sources += recursively_apply_runes(pre_mitigation_damage = normal_w_pre_mitigation_damage, source = rengar, target = dummy, runes = runes)
    total = 0
    for damage_source in damage_sources:
        print(damage_source)
        total += damage_source.damage_value
    print(f"TOTAL : {total}")
    print("-"*20)

    damage_sources : list[DamageInformation] = []
    empowered_w_pre_mitigation_damage = rengar.press_w(empowered = True)
    damage_sources.append(empowered_w_pre_mitigation_damage)
    damage_sources += recursively_apply_runes(pre_mitigation_damage = empowered_w_pre_mitigation_damage, source = rengar, target = dummy, runes = runes)
    total = 0
    for damage_source in damage_sources:
        print(damage_source)
        total += damage_source.damage_value
    print(f"TOTAL : {total}")
    print("-"*20)
    """

    

    """
    # E - Bola Strike
    damage_sources : list[DamageInformation] = []
    normal_e_pre_mitigation_damage = rengar.press_e(empowered = False)
    damage_sources.append(normal_e_pre_mitigation_damage)
    damage_sources += recursively_apply_runes(pre_mitigation_damage = normal_e_pre_mitigation_damage, source = rengar, target = dummy, runes = runes)
    total = 0
    for damage_source in damage_sources:
        print(damage_source)
        total += damage_source.damage_value
    print(f"TOTAL : {total}")
    print("-"*20)

    damage_sources : list[DamageInformation] = []
    empowered_e_pre_mitigation_damage = rengar.press_e(empowered = True)
    damage_sources.append(empowered_e_pre_mitigation_damage)
    damage_sources += recursively_apply_runes(pre_mitigation_damage = empowered_e_pre_mitigation_damage, source = rengar, target = dummy, runes = runes)
    total = 0
    for damage_source in damage_sources:
        print(damage_source)
        total += damage_source.damage_value
    print(f"TOTAL : {total}")
    print("-"*20)
    """

    """
    # R - Thrill of the Hunt
    damage_sources : list[DamageInformation] = []
    auto_attack_pre_mitigation_damage = rengar.auto_attack()
    damage_sources.append(auto_attack_pre_mitigation_damage)
    damage_sources += recursively_apply_runes(pre_mitigation_damage = auto_attack_pre_mitigation_damage, source = rengar, target = dummy, runes = runes)

    normal_r_pre_mitigation_damage = rengar.press_r(ult_bonus = True)
    damage_sources.append(normal_r_pre_mitigation_damage)
    damage_sources += recursively_apply_runes(pre_mitigation_damage = normal_r_pre_mitigation_damage, source = rengar, target = dummy, runes = runes)
    total = 0
    for damage_source in damage_sources:
        print(damage_source)
        total += damage_source.damage_value
    print(f"TOTAL : {total}")
    print("-"*20)
    """

    """
    # 4 Auto Attacks
    for _ in range(4):
        damage_sources : list[DamageInformation] = []
        auto_attack_pre_mitigation_damage = rengar.auto_attack()
        damage_sources.append(auto_attack_pre_mitigation_damage)
        damage_sources += recursively_apply_runes(pre_mitigation_damage = auto_attack_pre_mitigation_damage, source = rengar, target = dummy, runes = runes)

        total = 0
        for damage_source in damage_sources:
            print(damage_source)
            total += damage_source.damage_value
        print(f"TOTAL : {total}")
        print("-"*20)
    """


if __name__ == '__main__':
    main()