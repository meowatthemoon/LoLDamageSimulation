from items.item import Item

class Tiamat(Item):
    def __init__(self):
        super().__init__(
            name = "Tiamat",
            cost = 1200,
            attack_damage = 20
        )

    def use_item(self):
        """total_ad_ratio : float = 0.75
        source_total_ad : float = source.get_total_ad()

        pre_mitigation_damage : PreMitigationDamage = PreMitigationDamage(
            value = total_ad_ratio * source_total_ad,
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