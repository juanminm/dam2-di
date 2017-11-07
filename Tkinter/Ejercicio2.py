import tkinter

def click():
    contador.set(contador.get() + 1)

if __name__ == '__main__':
    window = tkinter.Tk()

    contador = tkinter.IntVar()
    contador.set(0)

    frame = tkinter.Frame(window)
    frame.pack()

    button = tkinter.Button(frame, textvariable=contador, command=click)
    button.pack()

    window.mainloop()