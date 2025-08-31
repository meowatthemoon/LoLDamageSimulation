from items.item import Item

class Collector(Item):
    def __init__(self):
        super().__init__( 
            name = "Collector",
            cost = 3000,
            attack_damage = 50, 
            crit_chance = 25,
            lethality = 10
        )

    def use_item(self):
        """value = target.get_current_hp() if target.get_current_hp() / target.get_total_hp() < 0.05 else 0
        pre_mitigation_damage = PreMitigationDamage(
            value = value,
            damage_type = DamageType.TrueDamage,
            damage_source = DamageSource.Item,
            is_single_target = True,
            user_lethality = 0,
            user_magic_penetration = 0,
            user_percentage_armor_penetration = 0,
            user_percentage_magic_penetration = 0
        )
        return target.take_damage(pre_mitigation_damage = pre_mitigation_damage)"""
        raise NotImplementedError