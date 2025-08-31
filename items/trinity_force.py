from items.item import Item

class TrinityForce(Item):
    def __init__(self):
        super().__init__(
            name = "Trinity Force",
            cost = 3333,
            ability_haste = 15, 
            attack_damage = 36, 
            attack_speed = 30,
            hp = 333
        )

    def use_item(self):
        """base_ad_ratio : float = 2
        source_base_ad : float = source.get_base_ad()
        
        pre_mitigation_damage : PreMitigationDamage = PreMitigationDamage(
            value = base_ad_ratio * source_base_ad,
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