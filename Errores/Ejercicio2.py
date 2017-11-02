import random

correcto = False
numero_secreto = random.randint(0, 10)

try:
    numero = int(input("Intenta adivinar el número entre 0 y 10: "))

    while not correcto:

        if numero_secreto == numero:
            correcto = True
            print("¡Adivinaste el número!")
        else:
            numero = int(input("¡Fallaste! Intentalo otra vez: "))

except ValueError:
    print("El valor introducido no es un número")