class Player:
    def __init__(self, name, init_treasure, init_base_health):
        self.name = name
        self.inv = {
            "wood": 0,
            "brick": 0,
            "iron": 0,
            "treasure": init_treasure,
            "items": []
        }
        self.base = {
            "health": init_base_health,
            "defense": 0,
        }

    def check_inventory(self):
        print(self.inv)

    def inputCoordinate():
    print("Enter the coordinate.")
    x = int(input("Enter X: "))
    y = int(input("Enter y: "))
    return x - 1, y - 1
    
    def dig(self):
        x, y = inputCoordinate()
        coordinate = [x, y]
        coordinateObject = land[x, y]
        coordinateState = coordinateObject.state
        
        while coordinate not in player.playerLand or coordinateState in ["unusable", "dug", "cannon"]:
            x, y = inputCoordinate()
        
        coordinateObject = land[x, y]
        coordinateState = coordinateObject.state
        
        if coordinateState == "empty":
            player.cash += 10 * player.cashMultiplier
            coordinateObject.state = "dug"
        elif coordinateState == "bomb":
            player.health -= 10
            coordinateObject.state = "empty"
            if player.health <= 0:
                print("You died.")

    def build(self):
        x, y = inputCoordinate()
        coordinate = [x, y]
        coordinateObject = land[x, y]
        coordinateState = coordinateObject.state
        
        while coordinate not in player.playerLand or coordinateState in ["unusable", "dug", "cannon"]:
            x, y = inputCoordinate()
        
        coordinateObject = land[x, y]
        coordinateState = coordinate.Object.state

        structure = input()
        while structure not in player.inventory:
            structure = input()

        if structure == "bomb":
            coordinateObject.state = "bomb"
            player.inventory.remove("structure")
        
        
        
    def attack(self):
        x, y = inputCoordinate()
        coordinate = [x, y]
        coordinateObject = land[x, y]
        coordinateState = coordinateObject.state
        
        while coordinateState != "cannon" and coordinate not in player.object:
            x, y = inputCoordinate()
        
        coordinateObject = land[x, y]
        coordinateState = coordinate.Object.state


    def repair(self):
        pass

    def craft_item(self):
        pass

    def trade_request(self):
        pass
