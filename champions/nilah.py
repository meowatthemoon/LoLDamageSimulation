from champions.champion import Champion


class Nilah(Champion):
    def __init__(self):
        super().__init__(
            name = "Nilah",
            base_hp = 570,
            scaling_hp = 101,
            base_hp_regeneration = 6,
            scaling_hp_regeneration = 0.9,
            base_armor = 27,
            scaling_armor = 4.5,
            base_magic_resist = 32,
            scaling_magic_resist = 2.05,
            base_attack_damage = 58,
            scaling_attack_damage = 2,
            base_movement_speed = 340,
            base_attack_speed = 0.697,
            base_attack_range = 225
        )  