from champions.champion import Champion


class Xayah(Champion):
    def __init__(self):
        super().__init__(
            name = "Xayah",
            base_hp = 630,
            scaling_hp = 107,
            base_hp_regeneration = 3.25,
            scaling_hp_regeneration = 0.75,
            base_armor = 25,
            scaling_armor = 4.2,
            base_magic_resist = 30,
            scaling_magic_resist = 1.3,
            base_attack_damage = 60,
            scaling_attack_damage = 3.5,
            base_movement_speed = 330,
            base_attack_speed = 0.658,
            base_attack_range = 525
        )  