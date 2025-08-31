from champions.champion import Champion


class Senna(Champion):
    def __init__(self):
        super().__init__(
            name = "Senna",
            base_hp = 530,
            scaling_hp = 89,
            base_hp_regeneration = 3.5,
            scaling_hp_regeneration = 0.55,
            base_armor = 25,
            scaling_armor = 4,
            base_magic_resist = 30,
            scaling_magic_resist = 1.3,
            base_attack_damage = 50,
            scaling_attack_damage = 0,
            base_movement_speed = 330,
            base_attack_speed = 0.625,
            base_attack_range = 600
        )  