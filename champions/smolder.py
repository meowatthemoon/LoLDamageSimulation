from champions.champion import Champion


class Smolder(Champion):
    def __init__(self):
        super().__init__(
            name = "Smolder",
            base_hp = 575,
            scaling_hp = 100,
            base_hp_regeneration = 4.5,
            scaling_hp_regeneration = 0.6,
            base_armor = 26,
            scaling_armor = 4.7,
            base_magic_resist = 30,
            scaling_magic_resist = 1.3,
            base_attack_damage = 60,
            scaling_attack_damage = 2.3,
            base_movement_speed = 330,
            base_attack_speed = 0.638,
            base_attack_range = 550
        )  