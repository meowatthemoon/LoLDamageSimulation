from champions.champion import Champion


class Kalista(Champion):
    def __init__(self):
        super().__init__(
            name = "Kalista",
            base_hp = 600,
            scaling_hp = 114,
            base_hp_regeneration = 4,
            scaling_hp_regeneration = 0.75,
            base_armor = 24,
            scaling_armor = 5.2,
            base_magic_resist = 30,
            scaling_magic_resist = 1.3,
            base_attack_damage = 59,
            scaling_attack_damage = 3.25,
            base_movement_speed = 330,
            base_attack_speed = 0.694,
            base_attack_range = 525
        )  