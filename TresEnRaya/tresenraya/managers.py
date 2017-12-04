class GameManager:
    def __init__(self, grid_size=3, player1=None, player2=None):
        self.grid_size = grid_size
        self.player1 = player1
        self.player1_mark = None
        self.player2 = player2
        self.player2_mark = None