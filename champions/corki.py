from champions.champion import Champion


class Corki(Champion):
    def __init__(self):
        super().__init__(
            name = "Corki",
            base_hp = 610,
            scaling_hp = 100,
            base_hp_regeneration = 5.5,
            scaling_hp_regeneration = 0.55,
            base_armor = 30,
            scaling_armor = 4.5,
            base_magic_resist = 30,
            scaling_magic_resist = 1.3,
            base_attack_damage = 52,
            scaling_attack_damage = 2,
            base_movement_speed = 325,
            base_attack_speed = 0.644,
            base_attack_range = 550
        )  