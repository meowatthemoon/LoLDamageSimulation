from champions.champion import Champion


class Tristana(Champion):
    def __init__(self):
        super().__init__(
            name = "Tristana",
            base_hp = 640,
            scaling_hp = 102,
            base_hp_regeneration = 4,
            scaling_hp_regeneration = 0.5,
            base_armor = 30,
            scaling_armor = 4,
            base_magic_resist = 28,
            scaling_magic_resist = 1.3,
            base_attack_damage = 60,
            scaling_attack_damage = 2.5,
            base_movement_speed = 325,
            base_attack_speed = 0.694,
            base_attack_range = 550
        )  