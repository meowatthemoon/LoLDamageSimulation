from champions.champion import Champion


class Yunara(Champion):
    def __init__(self):
        super().__init__(
            name = "Yunara",
            base_hp = 600,
            scaling_hp = 110,
            base_hp_regeneration = 4,
            scaling_hp_regeneration = 0.55,
            base_armor = 25,
            scaling_armor = 4.4,
            base_magic_resist = 30,
            scaling_magic_resist = 1.3,
            base_attack_damage = 56,
            scaling_attack_damage = 2.5,
            base_movement_speed = 325,
            base_attack_speed = 0.65,
            base_attack_range = 575
        )  