nombre_fichero = input("Introduzca el nombre del fichero que se copiará: ")

fichero_original = open(nombre_fichero, mode='r', encoding='utf-8')
fichero_backup = open("bak.txt", mode='w', encoding='utf-8')

for linea in fichero_original:
    fichero_backup.write(linea)

fichero_original.close()
fichero_backup.close()
