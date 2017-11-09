from tkinter import *


def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def convertir():
    result.set(convert_to_celsius(getdouble(entry.get())))


def salir():
    exit(0)


if __name__ == '__main__':
    window = Tk()
    result = DoubleVar()

    frame = Frame(window)
    frame.pack()

    label = Label(frame, text="Temperatura en Fahrenheit: ")
    label.pack()

    entry = Entry(frame)
    entry.pack()

    result_lbl = Label(frame, textvariable=result)
    result_lbl.pack()

    convertir_btn = Button(frame, text="Convertir", command=convertir)
    convertir_btn.pack()

    salir_btn = Button(frame, text="Salir", command=salir)
    salir_btn.pack()

    window.mainloop()