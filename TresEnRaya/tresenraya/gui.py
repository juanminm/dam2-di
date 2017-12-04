import tkinter

import tresenraya.managers
import tresenraya.players

game_manager = tresenraya.managers.GameManager()
turn_manager = tresenraya.managers.TurnManager()


class MainWindow:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.resizable(width=False, height=False)
        self.window.minsize(300, 200)
        self.window.title = "Tic Tac Toe"
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        ModeSelectionFrame(self.window);
        self.window.mainloop()


class ModeSelectionFrame:
    def __init__(self, parent):
        self.parent = parent
        self.frame = tkinter.Frame(parent)
        self.frame.pack(fill="none", expand=True)

        self.one_player_button = tkinter.Button(
            self.frame,
            text="One player",
            command=lambda: self.select_mode(True)
        )
        self.one_player_button.pack()

        self.two_players_button = tkinter.Button(
            self.frame,
            text="Two players",
            command=lambda: self.select_mode(False)
        )
        self.two_players_button.pack()

    def select_mode(self, with_cpu):
        if with_cpu:
            game_manager.player1 = tresenraya.players.Human("Player 1")
            game_manager.player2 = tresenraya.players.CPU()
        else:
            game_manager.player1 = tresenraya.players.Human("Player 1")
            game_manager.player2 = tresenraya.players.Human("Player 2")

        change_frame(self.frame, GridSelectionFrame(self.parent))


class GridSelectionFrame:
    def __init__(self, parent):
        self.parent = parent
        self.frame = tkinter.Frame(parent)
        self.frame.pack(fill="none", expand=True)

        self.input_size_label = tkinter.Label(
            self.frame,
            text="Input grid size (empty = 3):"
        )
        self.input_size_label.pack()

        self.size_text = tkinter.Text(self.frame)
        self.size_text.pack()

        self.confirm_grid_size_button = tkinter.Button(
            self.frame,
            text="Confirm",
            command=lambda: self.confirm_grid_size()
        )
        self.confirm_grid_size_button.pack()

    def confirm_grid_size(self):
        size = self.size_text.get("0.0", tkinter.END)

        if size == '\n':
            change_frame(
                self.frame,
                GridFrame(self.parent)
            )
        elif is_int(size):
            game_manager.grid_size = int(size)

            change_frame(
                self.frame,
                GridFrame(self.parent)
            )


class GridFrame:
    def __init__(self, parent):
        self.parent = parent
        self.frame = tkinter.Frame(self.parent)
        self.squares = [[None for i in range(game_manager.grid_size)] for i in
                        range(game_manager.grid_size)]

        self.frame.pack(fill="none", expand=True)

        game_manager.start_game(turn_manager)

        for i in range(game_manager.grid_size):
            for j in range(game_manager.grid_size):
                self.squares[i][j] = Square(self.frame, i, j)


class Square:
    def __init__(self, parent, row, column):
        self.parent = parent
        self.row = row
        self.column = column
        self.marca = tkinter.StringVar()

        self.button = tkinter.Button(
            self.parent,
            textvariable=self.marca,
            command=lambda: make_move(self),
            width=4, height=4
        )

        self.button.grid(row=self.row, column=self.column)


def change_frame(current_frame, next_frame):
    current_frame.destroy()
    next_frame


def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def make_move(square):
    if turn_manager.player == game_manager.player1:
        square.marca.set(game_manager.player1_mark)
        turn_manager.change_turn(game_manager.player2)
    else:
        square.marca.set(game_manager.player2_mark)
        turn_manager.change_turn(game_manager.player1)

    square.button.config(state=tkinter.DISABLED)
    pass
