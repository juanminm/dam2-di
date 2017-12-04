import random


class GameManager:
    def __init__(self, grid_size=3, player1=None, player2=None):
        self.grid_size = grid_size
        self.player1 = player1
        self.player1_mark = None
        self.player2 = player2
        self.player2_mark = None

    def start_game(self, turn_manager):
        if random.randint(0, 1) == 0:
            self.player1_mark = "O"
            self.player2_mark = "X"
            turn_manager.player = self.player1
        else:
            self.player1_mark = "X"
            self.player2_mark = "O"
            turn_manager.player = self.player2


class TurnManager:
    def __init__(self):
        self.player = None

    def change_turn(self, player):
        self.player = player