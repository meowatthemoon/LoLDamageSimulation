from items.item import Item

class LordDominiksRegards(Item):
    def __init__(self):
        super().__init__(
            name = "Lord Dominik's Regards",
            cost = 3100,
            attack_damage = 35, 
            armor_penetration_percentage = 40,
            crit_chance = 25
        )