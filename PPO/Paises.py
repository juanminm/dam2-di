class Pais:
    def __init__(self, nombre, poblacion, area):
        self.nombre = nombre
        self.poblacion = poblacion
        self.area = area

    def mas_grande_que(self, otro_pais):
        if self.area > otro_pais.area:
            return True
        else:
            return False

    def densidad_poblacion(self):
        return self.poblacion / self.area

espanya = Pais("España", 46770000, 504645)
francia = Pais("Francia", 66030000, 640679)

# En este bloque uso una sintaxis de if parecida a una operación ternaria de Java (ex: a > b ? a : b). En el primer caso
# devolverá la cadena "" si espanya.mas_grande_que(francia) devuelve True; en caso contrario, la cadena devuelta es
# "no ".
print("{} {}es mas grande que {}".format(espanya.nombre,
                                         "" if espanya.mas_grande_que(francia) else "no ",
                                         francia.nombre))

print("La densidad de población de {} es {}".format(espanya.nombre, espanya.densidad_poblacion()))
print("La densidad de población de {} es {}".format(francia.nombre, francia.densidad_poblacion()))