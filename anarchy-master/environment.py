from random import randint
class Environment:
    def __init__(self, columns, rows):
        self.grid = [[self.generate_cell() for i in range(rows)] for i in range(columns)]

    def generate_cell(self):
        return {
            "wood": randint(1, 1000),
            "brick": max(randint(-3, 1)*randint(1, 500), 0),
            "iron": max(randint(-10, 1)*randint(1, 250), 0),
            "bombs": 0,
            "defense": 0
            }
env = Environment(100, 100)
print(env.grid)
    
    
        
