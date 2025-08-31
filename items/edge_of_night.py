from items.item import Item

class EdgeOfNight(Item):
    def __init__(self):
        super().__init__(
            name = "Edge of Night",
            cost = 3000,
            attack_damage = 50, 
            hp = 250,
            lethality = 15
        )