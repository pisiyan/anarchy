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

    def dig(self):
        pass

    def build(self):
        pass

    def attack(self):
        pass

    def repair(self):
        pass

    def craft_item(self):
        pass

    def trade_request(self):
        pass
