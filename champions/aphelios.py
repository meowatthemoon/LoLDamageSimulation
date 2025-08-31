from champions.champion import Champion


class Aphelios(Champion):
    def __init__(self):
        super().__init__(
            name = "Aphelios",
            base_hp = 600,
            scaling_hp = 102,
            base_hp_regeneration = 3.25,
            scaling_hp_regeneration = 0.55,
            base_armor = 26,
            scaling_armor = 4.2,
            base_magic_resist = 30,
            scaling_magic_resist = 1.3,
            base_attack_damage = 55,
            scaling_attack_damage = 2.3,
            base_movement_speed = 325,
            base_attack_speed = 0.64,
            base_attack_range = 550
        )  