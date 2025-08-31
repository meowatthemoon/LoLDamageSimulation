from champions.champion import Champion


class Ashe(Champion):
    def __init__(self):
        super().__init__(
            name = "Ashe",
            base_hp = 610,
            scaling_hp = 101,
            base_hp_regeneration = 3.5,
            scaling_hp_regeneration = 0.55,
            base_armor = 26,
            scaling_armor = 4.6,
            base_magic_resist = 30,
            scaling_magic_resist = 1.3,
            base_attack_damage = 59,
            scaling_attack_damage = 2.95,
            base_movement_speed = 325,
            base_attack_speed = 0.658,
            base_attack_range = 600
        )  