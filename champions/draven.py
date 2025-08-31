from champions.champion import Champion


class Draven(Champion):
    def __init__(self):
        super().__init__(
            name = "Draven",
            base_hp = 675,
            scaling_hp = 104,
            base_hp_regeneration = 3.75,
            scaling_hp_regeneration = 0.7,
            base_armor = 29,
            scaling_armor = 4.4,
            base_magic_resist = 30,
            scaling_magic_resist = 1.3,
            base_attack_damage = 62,
            scaling_attack_damage = 3.6,
            base_movement_speed = 330,
            base_attack_speed = 0.674,
            base_attack_range = 550
        )  