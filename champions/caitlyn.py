from champions.champion import Champion


class Caitlyn(Champion):
    def __init__(self):
        super().__init__(
            name = "Caitlyn",
            base_hp = 580,
            scaling_hp = 107,
            base_hp_regeneration = 3.5,
            scaling_hp_regeneration = 0.55,
            base_armor = 27,
            scaling_armor = 4.7,
            base_magic_resist = 30,
            scaling_magic_resist = 1.3,
            base_attack_damage = 60,
            scaling_attack_damage = 3.8,
            base_movement_speed = 325,
            base_attack_speed = 0.681,
            base_attack_range = 650
        )  