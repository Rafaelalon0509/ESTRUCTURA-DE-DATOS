

# nombre_paterno = "" #snake case
# NOMBRE_PATERNO = "" #SCREAMING SNAKE CASE
# nombre_paterno = "" #upper Camel case
# nombrePaterno = "" #lower camel case

# #EJEMPLO MEMORIA ESTATICA

# edad = 18
# nombre = "will"

# lista_estatica = [1,3,5,7,9]

# #EJEMPLO MEMORIA DINAMICA

# lista_dinamica = [2,4,6,8]

# print("hola "+nombre)
# print("secciona un numero: ")
# print(lista_estatica)


# add_lista = int(input("Ingrese numero: "))
# lista_dinamica.append(add_lista)

# print(lista_dinamica)


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

persona1 = Persona("Will", 18)
persona2 = Persona("Pedro", 22)
persona3 = Persona("Rafael", 20)
persona4 = Persona("Irving", 18)
persona5 = Persona("Francisco", 25)

print(persona1.nombre)
print(persona2.nombre)
print(persona3.nombre)
print(persona4.nombre)
print(persona5.nombre)

