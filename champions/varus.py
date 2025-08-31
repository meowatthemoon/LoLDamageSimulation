from champions.champion import Champion


class Varus(Champion):
    def __init__(self):
        super().__init__(
            name = "Varus",
            base_hp = 600,
            scaling_hp = 105,
            base_hp_regeneration = 3.5,
            scaling_hp_regeneration = 0.55,
            base_armor = 27,
            scaling_armor = 4.6,
            base_magic_resist = 30,
            scaling_magic_resist = 1.3,
            base_attack_damage = 59,
            scaling_attack_damage = 3.4,
            base_movement_speed = 330,
            base_attack_speed = 0.658,
            base_attack_range = 575
        )  