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

class Resources:

    def __init__(self, name):
        self.name = name

wood = Resources(
    name = "Wood"
)

brick = Resources(
    name = "Brick"
)

iron = Resources(
    name = "Iron"
)

wooden_shovel = Craftables(
    name = "Wooden Shovel"
    requirements = {wood: 3}
    price = 25
)

iron_shovel = Craftables(
    name = "Iron Shovel"
    requirements = {iron: 1, wood: 2}
    price = 50
)

wall = Defence(
    name = "Wall"
    requirements = {brick: 5}
    price = 50
    health = 50
)

armoured_wall = Defence(
    name = "Armoured Wall"
    requirements = {brick: 5, iron: 2}
    price = 100
    health = 100
)

wooden_axe = Weapons(
    name = "Wooden Axe"
    requirements = {wood: 5}
    price = 50
    damage = 10
)

iron_axe = Weapons(
    name = "Iron Axe"
    requirements = {wood: 3, iron: 2}
    price = 100
    damage = 20
)

trap = Weapons(
    name = "Trap"
    requirements = {wood: 3, iron: 3}
    price = 100
)
