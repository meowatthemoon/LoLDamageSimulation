from champions.champion import Champion
from champions.target_dummy import TargetDummy
from champions.rengar import Rengar

from damage.pre_mitigation_damage import PreMitigationDamage
from items.infinity_edge import InfinityEdge
from items.item import Item
from items.mortal_reminder import MortalReminder
from items.ravenous_hydra import RavenousHydra
from runes.press_the_attack import PressTheAttack
from runes.cut_down import CutDown
from runes.rune import Rune
from runes.rune_stat_attack_damage import RuneStatAttackDamage

def recursively_apply_runes(pre_mitigation_damage : PreMitigationDamage, source : Champion, target : Champion, runes : list[Rune]) -> list[PreMitigationDamage]:
    damage_sources : list[PreMitigationDamage] = []
    for rune in runes:    
        if rune.get_name() == pre_mitigation_damage.source_name:
            continue
        
        rune_pre_mitigation_damage = rune.on_damage(pre_mitigation_damage = pre_mitigation_damage, source = source, target = target)

        if rune_pre_mitigation_damage is not None:
            damage_sources.append(rune_pre_mitigation_damage)

            if rune_pre_mitigation_damage.is_amplifiable_by_runes:
                damage_sources += recursively_apply_runes(pre_mitigation_damage = rune_pre_mitigation_damage, source = source, target = target, runes = runes)

    return damage_sources

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
    damage_sources : list[PreMitigationDamage] = []
    normal_q_pre_mitigation_damage = rengar.press_q(empowered = False)
    damage_sources.append(normal_q_pre_mitigation_damage)
    damage_sources += recursively_apply_runes(pre_mitigation_damage = normal_q_pre_mitigation_damage, source = rengar, target = dummy, runes = runes)
    total = 0
    for damage_source in damage_sources:
        print(damage_source)
        total += damage_source.damage_value
    print(f"TOTAL : {total}")
    print("-"*20)

    damage_sources : list[PreMitigationDamage] = []
    empowered_q_pre_mitigation_damage = rengar.press_q(empowered = True)
    damage_sources.append(empowered_q_pre_mitigation_damage)
    damage_sources += recursively_apply_runes(pre_mitigation_damage = empowered_q_pre_mitigation_damage, source = rengar, target = dummy, runes = runes)
    total = 0
    for damage_source in damage_sources:
        print(damage_source)
        total += damage_source.damage_value
    print(f"TOTAL : {total}")
    print("-"*20)

    """
    # W - Battle Roar
    damage_sources : list[PreMitigationDamage] = []
    normal_w_pre_mitigation_damage = rengar.press_w(empowered = False)
    damage_sources.append(normal_w_pre_mitigation_damage)
    damage_sources += recursively_apply_runes(pre_mitigation_damage = normal_w_pre_mitigation_damage, source = rengar, target = dummy, runes = runes)
    total = 0
    for damage_source in damage_sources:
        print(damage_source)
        total += damage_source.damage_value
    print(f"TOTAL : {total}")
    print("-"*20)

    damage_sources : list[PreMitigationDamage] = []
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
    damage_sources : list[PreMitigationDamage] = []
    normal_e_pre_mitigation_damage = rengar.press_e(empowered = False)
    damage_sources.append(normal_e_pre_mitigation_damage)
    damage_sources += recursively_apply_runes(pre_mitigation_damage = normal_e_pre_mitigation_damage, source = rengar, target = dummy, runes = runes)
    total = 0
    for damage_source in damage_sources:
        print(damage_source)
        total += damage_source.damage_value
    print(f"TOTAL : {total}")
    print("-"*20)

    damage_sources : list[PreMitigationDamage] = []
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
    damage_sources : list[PreMitigationDamage] = []
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
        damage_sources : list[PreMitigationDamage] = []
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