from tkinter import *

class MainWindow:
    def __init__(self):
        self.window = Tk()
        Grid(self.window, 3);
        self.window.mainloop()

class Grid:
    def __init__(self, parent, grid_size=3):
        self.parent = parent
        self.squares = [[None for i in range(grid_size)] for i in
                         range(grid_size)]

        for i in range(grid_size):
            for j in range(grid_size):
                self.squares[i][j] = Button(
                    self.parent, textvariable=" ",
                    command=lambda i=i, j=j: self.choose_square(
                        self.choose_square(self.squares[i][j])
                    ),
                    width=4, height=4
                )
                self.squares[i][j].grid(row=i, column=j)
