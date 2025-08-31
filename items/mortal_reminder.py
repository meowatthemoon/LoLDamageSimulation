from items.item import Item

class MortalReminder(Item):
    def __init__(self):
        super().__init__(
            name = "Mortal Reminder",
            cost = 3300,
            attack_damage = 35, 
            armor_penetration_percentage = 35,
            crit_chance = 25
        )