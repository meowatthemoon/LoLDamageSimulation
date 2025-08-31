from champions.champion import Champion


class Jinx(Champion):
    def __init__(self):
        super().__init__(
            name = "Jinx",
            base_hp = 630,
            scaling_hp = 105,
            base_hp_regeneration = 3.75,
            scaling_hp_regeneration = 0.55,
            base_armor = 26,
            scaling_armor = 4.7,
            base_magic_resist = 30,
            scaling_magic_resist = 1.3,
            base_attack_damage = 59,
            scaling_attack_damage = 2.9,
            base_movement_speed = 325,
            base_attack_speed = 0.625,
            base_attack_range = 525
        )  