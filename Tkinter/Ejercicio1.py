import tkinter


def click():
    exit(0)

if __name__ == '__main__':
    window = tkinter.Tk()
    frame = tkinter.Frame(window)
    frame.pack()

    button = tkinter.Button(frame, text='Adiós', command=click)
    button.pack()

    window.mainloop()