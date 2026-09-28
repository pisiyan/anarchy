class Game:
    def __init__(self, players, environment):
        self.players = players
        self.environment = environment
        self.turn = 0
        self.actions = {
            "dig": lambda player: player.dig(),
            "build": lambda player: player.build(),
            "attack": lambda player: player.attack(),
            "repair": lambda player: player.repair(),
            "craft": lambda player: player.craft_item(),
            "trade": lambda player: player.trade_request()
        }
        self.N_TURNS = 3
    def play_turn(self):
        player = self.players[self.turn]
        print(f"It's {player.name}'s turn")
        for i in range(self.N_TURNS):
            print(f"Choose your action: \n - dig\n - build\n - attack\n - repair\n - craft\n - trade")
            action = input()
            while action not in self.actions.keys():
                action = input()
            self.actions[action](player)
            self.update()

    def update(self):
        for player in self.players:
            if player.base["health"] <= 0:
                print(f"{player.name} got cooked.")
                self.players.remove(player)
                self.environment.remove_player(player)

