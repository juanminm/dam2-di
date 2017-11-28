import tkinter


class MainWindow:
    def __init__(self):
        self.window = tkinter.Tk()
        ModeSelectionFrame(self.window);
        self.window.mainloop()


class ModeSelectionFrame:
    def __init__(self, parent):
        self.parent = parent
        self.frame = tkinter.Frame(parent)
        self.frame.pack()

        self.one_player_button = tkinter.Button(
            self.frame,
            text="One player",
            # command=change_frame(self.frame, GridSelectionFrame(self.parent))
        )
        self.one_player_button.pack()

        self.two_players_button = tkinter.Button(
            self.frame,
            text="Two players",
            # command=change_frame(self.frame, GridSelectionFrame(self.parent))
        )
        self.two_players_button.pack()


class GridFrame:
    def __init__(self, parent, grid_size=3):
        self.parent = parent
        self.frame = tkinter.Frame(self.parent)
        self.squares = [[None for i in range(grid_size)] for i in
                        range(grid_size)]

        self.frame.pack()

        for i in range(grid_size):
            for j in range(grid_size):
                self.squares[i][j] = Cell(self.frame, i, j)


class Cell:
    def __init__(self, parent, row, column):
        self.parent = parent
        self.row = row
        self.column = column

        self.button = tkinter.Button(
            self.parent,
            textvariable=" ",
            command=lambda: makeMove(),
            width=4, height=4
        )

        self.button.grid(row=self.row, column=self.column)


def change_frame(frame, param):
    # TODO
    pass


def makeMove():
    # TODO
    pass
