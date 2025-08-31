from champions.champion import Champion


class KogMaw(Champion):
    def __init__(self):
        super().__init__(
            name = "Kog'Maw",
            base_hp = 635,
            scaling_hp = 99,
            base_hp_regeneration = 3.75,
            scaling_hp_regeneration = 0.55,
            base_armor = 24,
            scaling_armor = 4.45,
            base_magic_resist = 30,
            scaling_magic_resist = 1.3,
            base_attack_damage = 61,
            scaling_attack_damage = 3.1,
            base_movement_speed = 330,
            base_attack_speed = 0.665,
            base_attack_range = 500
        )  