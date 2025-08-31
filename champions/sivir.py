from champions.champion import Champion


class Sivir(Champion):
    def __init__(self):
        super().__init__(
            name = "Sivir",
            base_hp = 600,
            scaling_hp = 104,
            base_hp_regeneration = 3.25,
            scaling_hp_regeneration = 0.55,
            base_armor = 30,
            scaling_armor = 4.45,
            base_magic_resist = 30,
            scaling_magic_resist = 1.3,
            base_attack_damage = 60,
            scaling_attack_damage = 2.5,
            base_movement_speed = 335,
            base_attack_speed = 0.625,
            base_attack_range = 500
        )  