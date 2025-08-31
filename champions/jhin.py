from champions.champion import Champion


class Jhin(Champion):
    def __init__(self):
        super().__init__(
            name = "Jhin",
            base_hp = 655,
            scaling_hp = 107,
            base_hp_regeneration = 3.75,
            scaling_hp_regeneration = 0.55,
            base_armor = 24,
            scaling_armor = 4.7,
            base_magic_resist = 30,
            scaling_magic_resist = 1.3,
            base_attack_damage = 59,
            scaling_attack_damage = 4.4,
            base_movement_speed = 330,
            base_attack_speed = 0.625,
            base_attack_range = 550
        )  