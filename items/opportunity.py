from items.item import Item

class Opportunity(Item):
    def __init__(self):
        super().__init__(
            name = "Opportunity",
            cost = 2700,
            attack_damage = 55, 
            lethality = 18 + 11 # TODO melee vs ranged, also without passive active
        )