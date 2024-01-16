#crear un programa que almacene nombres en un vector 
#capturara datos hasta que el valor ingresado sea "STOP"
#mostrar el vector resultante
#sugerencia : usar metodo while

# Inicializar un vector para almacenar los nombres
nombres = []

# Capturar nombres hasta que se ingrese "STOP"
while True:
    nombre = input("Ingrese un nombre (o escriba 'STOP' para finalizar): ")
    
    # Verificar si se debe detener la captura
    if nombre.upper() == "STOP":
        break
    
    # Agregar el nombre al vector
    nombres.append(nombre)

# Mostrar el vector resultante
print("Nombres ingresados:")
for nombre in nombres:
    print(nombre)