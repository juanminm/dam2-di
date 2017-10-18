def area_triangulo(base, altura):
    """Calcula el area del triangulo usando la base y altura del mismo.

    :param base: la base del triangulo
    :param altura: la altura del triangulo
    :return: el area del trianguo
    """
    return base * altura / 2


def longitud_seg(*segmentos):
    """Suma las longitudes de los segmentos. Si no hay parametros, el resultado será siempre 0.

    :param segmentos: longitud de cada segmento
    :return: suma de los segmentos
    """
    suma = 0

    for valor in segmentos:
        suma += valor

    return suma


print("Llamamos a area_triangulo con los parametros {} y {} y el resultado es {}".format(4, 1, area_triangulo(4, 1)))
print("Llamamos a longitud_seg con los parametros {} y el resultado es {}".format(
    [3, 5, 3.2, 7.3, 6.3], longitud_seg(3, 5, 3.2, 7.3, 6.3)))

print("Llamamos a area_triangulo con los parametros {} y {} y el resultado es {}".format(3, 5, area_triangulo(3, 5)))
print("Llamamos a longitud_seg con los parametros {} y el resultado es {}".format(
    [9, 10.2, 1.345, 6.43, 1.2], longitud_seg(9, 10.2, 1.345, 6.43, 1.2)))

print("Llamamos a area_triangulo con los parametros {} y {} y el resultado es {}".format(9, 16, area_triangulo(9, 16)))
print("Llamamos a longitud_seg con los parametros {} y el resultado es {}".format(
    [], longitud_seg()))
