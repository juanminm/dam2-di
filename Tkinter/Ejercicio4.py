from tkinter import *

def click():
    cadena = texto.get("0.0", END)

    A = 0
    T = 0
    G = 0
    C = 0

    for letra in cadena:
        if letra == 'A':
            A += 1
        elif letra == 'T':
            T += 1
        elif letra == 'G':
            G += 1
        elif letra == 'C':
            C += 1

    estado.set("A: " + str(A) + ", T: " + str(T) + ", G: " + str(G) + ", C: "
               + str(C))


if __name__ == '__main__':
    window = Tk()
    estado = StringVar()

    frame = Frame(window)
    frame.pack()

    texto = Text(frame)
    texto.pack()

    button = Button(frame, text="Contar", command=click)
    button.pack()

    info = Label(frame, textvariable=estado, background="#FFFFFF")
    info.pack(fill=X)

    window.mainloop()