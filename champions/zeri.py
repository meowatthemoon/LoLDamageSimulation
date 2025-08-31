from champions.champion import Champion


class Zeri(Champion):
    def __init__(self):
        super().__init__(
            name = "Zeri",
            base_hp = 600,
            scaling_hp = 110,
            base_hp_regeneration = 3.25,
            scaling_hp_regeneration = 0.7,
            base_armor = 24,
            scaling_armor = 4.2,
            base_magic_resist = 30,
            scaling_magic_resist = 1.3,
            base_attack_damage = 56,
            scaling_attack_damage = 2,
            base_movement_speed = 330,
            base_attack_speed = 0.658,
            base_attack_range = 500
        )  