from items.item import Item

class Eclipse(Item):
    def __init__(self):
        super().__init__(
            name = "Eclipse",
            cost = 2900,
            ability_haste = 15, 
            attack_damage = 60
        )

    def use_item(self):
        """total_hp_ratio : float = 0.6
        target_total_hp : float = target.get_total_hp()
        pre_mitigation_damage : PreMitigationDamage = PreMitigationDamage(
            value = total_hp_ratio * target_total_hp,
            damage_type = DamageType.PhysicalDamage,
            damage_source = DamageSource.Item,
            is_single_target = False,
            user_lethality = source.get_total_lethality(),
            user_percentage_armor_penetration = source.get_total_percentage_armor_penetration(),
            user_magic_penetration = 0,
            user_percentage_magic_penetration = 0
        )
        return target.take_damage(pre_mitigation_damage = pre_mitigation_damage)"""
        raise NotImplementedError