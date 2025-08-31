from champions.champion import Champion


class Samira(Champion):
    def __init__(self):
        super().__init__(
            name = "Samira",
            base_hp = 630,
            scaling_hp = 108,
            base_hp_regeneration = 3.25,
            scaling_hp_regeneration = 0.55,
            base_armor = 26,
            scaling_armor = 4.7,
            base_magic_resist = 30,
            scaling_magic_resist = 1.3,
            base_attack_damage = 57,
            scaling_attack_damage = 3,
            base_movement_speed = 335,
            base_attack_speed = 0.658,
            base_attack_range = 500
        )  