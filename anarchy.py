class Craftables:

    def __init__(self name, requirements, price):
        self.name = name  
        self.requirements = requirements
        self.price = price

class Defence(Craftables):

    def __init__(self, name, item_requirements, price, health):
        super().__init__(name, item_requirements, price)
        self.health = health

class Weapons(Craftables):

    def __init__(self, name, item_requirements, price, damage, cooldown):
        super().__init__(name, item_requirements, price)
        self.damage = damage
        self.cooldown = cooldown
        
wooden_shovel = Craftables(
    name = "Wooden Shovel"
    requirements = {"Wood": 3}
    price = 25
)

iron_shovel = Craftables(
    name = "Iron Shovel"
    requirements = {"Iron": 1, "Wood": 2}
    price = 50
)

wall = Defence(
    name = "Wall"
    requirements = {"Brick": 5}
    price = 50
    health = 50
)

armoured_wall = Defence(
    name = "Armoured Wall"
    requirements = {"Brick": 5, "Iron": 2}
    price = 100
    health = 100
)

wooden_axe = Weapons(
    name = "Wooden Axe"
    requirements = {"Wood": 5}
    price = 50
    damage = 10
)

iron_axe = Weapons(
    name = "Iron Axe"
    requirements = {"Wood": 3, "Iron": 2}
    price = 100
    damage = 20
)

trap = Weapons(
    name = "Trap"
    requirements = {"Wood": 3, "Iron": 3}
    price = 100
)
