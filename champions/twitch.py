from champions.champion import Champion


class Twitch(Champion):
    def __init__(self):
        super().__init__(
            name = "Twitch",
            base_hp = 630,
            scaling_hp = 104,
            base_hp_regeneration = 3.75,
            scaling_hp_regeneration = 0.6,
            base_armor = 27,
            scaling_armor = 4.2,
            base_magic_resist = 30,
            scaling_magic_resist = 1.3,
            base_attack_damage = 59,
            scaling_attack_damage = 3.1,
            base_movement_speed = 330,
            base_attack_speed = 0.679,
            base_attack_range = 550
        )  