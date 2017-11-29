import tkinter


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
            command=lambda: change_frame(self.frame, GridSelectionFrame(self.parent))
        )
        self.one_player_button.pack()

        self.two_players_button = tkinter.Button(
            self.frame,
            text="Two players",
            command=lambda: change_frame(self.frame, GridSelectionFrame(self.parent))
        )
        self.two_players_button.pack()


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
            command=self.confirm_grid_size
        )
        self.confirm_grid_size_button.pack()

    def confirm_grid_size(self):
        size = self.size_text.get("0.0", tkinter.END)

        if size == '\n':
            change_frame(self.frame, GridFrame(self.parent))
        elif isinstance(size, int):
            change_frame(self.frame, GridFrame(self.parent, size))



class GridFrame:
    def __init__(self, parent, grid_size=3):
        self.parent = parent
        self.frame = tkinter.Frame(self.parent)
        self.squares = [[None for i in range(grid_size)] for i in
                        range(grid_size)]

        self.frame.pack(fill="none", expand=True)

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


def change_frame(current_frame, next_frame):
    current_frame.destroy()
    next_frame


def makeMove():
    # TODO
    pass
