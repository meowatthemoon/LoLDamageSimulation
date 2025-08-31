from champions.champion import Champion


class Lucian(Champion):
    def __init__(self):
        super().__init__(
            name = "Lucian",
            base_hp = 641,
            scaling_hp = 100,
            base_hp_regeneration = 3.75,
            scaling_hp_regeneration = 0.65,
            base_armor = 28,
            scaling_armor = 4.2,
            base_magic_resist = 30,
            scaling_magic_resist = 1.3,
            base_attack_damage = 60,
            scaling_attack_damage = 2.9,
            base_movement_speed = 335,
            base_attack_speed = 0.638,
            base_attack_range = 500
        )  