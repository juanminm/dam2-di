'''
Created on 28 sept. 2017

@author: juamar
'''
def iterPower(base, exp):
    result = base
    
    if (exp == 0):
        if (base == 0):
            return "Indefinido"
        else:
            return 1
    elif (exp > 0):
        contador = 1
        while contador < exp:
            result *= base
            contador += 1
        
        return result
    else:
        return "No implementado"

# Comprobar base entera positiva con exponente par positivo
print(iterPower(5, 2))

# Comprobar base entera positiva con exponente positivo impar
print(iterPower(5, 3))

# Comprobar base entera positiva con exponente cero
print(iterPower(5, 0))

# Comprobar base entera negativa con exponente positivo
print(iterPower(-5, 2))

# Comprobar base entera negativa con exponente positivo
print(iterPower(-5, 3))

# Comprobar base entera negativa con exponente cero
print(iterPower(-5, 0))

# Comprobar base decimal positiva con exponente par positivo 
print(iterPower(0.5, 2))

# Comprobar base decimal positiva con exponente positivo impar
print(iterPower(0.5, 3))

# Comprobar base decimal positiva con exponente cero
print(iterPower(0.5, 0))

# Comprobar base decimal negativa con exponente par positivo
print(iterPower(-0.5, 2))

# Comprobar base decimal negativa con exponente impar positivo
print(iterPower(-0.5, 3))

# Comprobar base decimal negativa con exponente cero
print(iterPower(-0.5, 0))

# Comprobar base 0 con exponente 0
print(iterPower(0, 0))

# Comprobar cualquier base con exponente negativo
print(iterPower(3, -2))
