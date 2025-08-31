from items.item import Item

class InfinityEdge(Item):
    def __init__(self):
        super().__init__(
            name = "Infinity Edge",
            cost = 3450,
            attack_damage = 65, 
            crit_amplification = 40, 
            crit_chance = 25
        )