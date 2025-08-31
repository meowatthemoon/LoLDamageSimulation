from champions.champion import Champion


class Vayne(Champion):
    def __init__(self):
        super().__init__(
            name = "Vayne",
            base_hp = 550,
            scaling_hp = 103,
            base_hp_regeneration = 3.5,
            scaling_hp_regeneration = 0.55,
            base_armor = 23,
            scaling_armor = 4.6,
            base_magic_resist = 30,
            scaling_magic_resist = 1.3,
            base_attack_damage = 60,
            scaling_attack_damage = 2.35,
            base_movement_speed = 330,
            base_attack_speed = 0.658,
            base_attack_range = 550
        )  