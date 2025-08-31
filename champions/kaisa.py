from champions.champion import Champion


class KaiSa(Champion):
    def __init__(self):
        super().__init__(
            name = "Kai'Sa",
            base_hp = 640,
            scaling_hp = 102,
            base_hp_regeneration = 3.5,
            scaling_hp_regeneration = 0.55,
            base_armor = 25,
            scaling_armor = 4.2,
            base_magic_resist = 30,
            scaling_magic_resist = 1.3,
            base_attack_damage = 59,
            scaling_attack_damage = 2.6,
            base_movement_speed = 335,
            base_attack_speed = 0.644,
            base_attack_range = 525
        )  