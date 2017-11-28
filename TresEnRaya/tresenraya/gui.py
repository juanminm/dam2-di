import tkinter


class MainWindow:
    def __init__(self):
        self.window = tkinter.Tk()
        GridFrame(self.window, 3);
        self.window.mainloop()


class GridFrame:
    def __init__(self, parent, grid_size=3):
        self.parent = parent
        self.frame = tkinter.Frame()
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
            command=lambda : makeMove(),
            width=4, height=4
        )

        self.button.grid(row=self.row, column=self.column)


def makeMove():
    #TODO
    pass
