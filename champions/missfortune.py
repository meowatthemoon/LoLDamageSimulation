from champions.champion import Champion


class MissFortune(Champion):
    def __init__(self):
        super().__init__(
            name = "Miss Fortune",
            base_hp = 640,
            scaling_hp = 103,
            base_hp_regeneration = 3.75,
            scaling_hp_regeneration = 0.65,
            base_armor = 28,
            scaling_armor = 4.2,
            base_magic_resist = 30,
            scaling_magic_resist = 1.3,
            base_attack_damage = 53,
            scaling_attack_damage = 2.4,
            base_movement_speed = 325,
            base_attack_speed = 0.656,
            base_attack_range = 550
        )  