from champions.champion import Champion


class Ezreal(Champion):
    def __init__(self):
        super().__init__(
            name = "Ezreal",
            base_hp = 600,
            scaling_hp = 102,
            base_hp_regeneration = 4,
            scaling_hp_regeneration = 0.65,
            base_armor = 24,
            scaling_armor = 4.7,
            base_magic_resist = 30,
            scaling_magic_resist = 1.3,
            base_attack_damage = 60,
            scaling_attack_damage = 2.75,
            base_movement_speed = 325,
            base_attack_speed = 0.625,
            base_attack_range = 550
        )  