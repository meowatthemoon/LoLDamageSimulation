from champions.champion import Champion


class TargetDummy(Champion):
    def __init__(self):
        super().__init__(
            name = "Target Dummy",
            base_hp = 1000,
            scaling_hp = 0,
            base_hp_regeneration = 0,
            scaling_hp_regeneration = 0,
            base_armor = 0,
            scaling_armor = 0,
            base_magic_resist = 0,
            scaling_magic_resist = 0,
            base_attack_damage = 0,
            scaling_attack_damage = 0,
            base_movement_speed = 370,
            base_attack_speed = 0,
            base_attack_range = 0
        )  