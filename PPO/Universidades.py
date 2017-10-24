class Miembro:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni


class Profesor(Miembro):
    def __init__(self, nombre, edad, dni, numero_registro):
        Miembro.__init__(self, nombre, edad, dni)
        self.numero_registro = numero_registro


class Estudiante(Miembro):
    def __init__(self, nombre, edad, dni, numero_estudiante):
        Miembro.__init__(self, nombre, edad, dni)
        self.numero_estudiante = numero_estudiante


class Asignatura:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
        self.estudiantes=[]

    def docencia(self, profesor, *estudiantes):
        self.profesor = profesor
        for estudiante in estudiantes:
            self.estudiantes.append(estudiante)

    def lista_estudiantes(self):
        str = ""
        for estudiante in self.estudiantes:
            str += estudiante.nombre + " "

        return str


luis = Profesor("Luis", 50, 34567, 5001)
luisito = Estudiante("Luisito", 20, 56678, 1001)
matematicas = Asignatura("Matemáticas", 5)
matematicas.docencia(luis, luisito)
algebra = Asignatura("Álgebra", 7)
algebra.docencia(luis, luisito)

print("Profesores:")
print("    Nombre: {}. Edad: {}. DNI: {}. Nº Reg.: {}".format(
    luis.nombre, luis.edad, luis.dni, luis.numero_registro
))
print()

print("Estudiantes: ")
print("    Nombre: {}. Edad: {}. DNI: {}. Nº Estudiante: {}".format(
    luisito.nombre, luisito.edad, luisito.dni, luisito.numero_estudiante
))
print()

print("Asignaturas: ")
print("    Nombre: {}. CódAsignat.: {}".format(
    matematicas.nombre, matematicas.codigo
))
print("    Nombre: {}. CódAsignat.: {}".format(
    algebra.nombre, algebra.codigo
))
print()

print("El profesor que da clases de {} es {} y sus alumnos son {}".format(
    matematicas.nombre,
    matematicas.profesor.nombre,
    matematicas.lista_estudiantes()
))