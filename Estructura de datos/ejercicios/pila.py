#definicion
#una estructura de datos que recopila los datos asignados y dependiendo la forma los devulve 
#
#usa el principio lifo 

pila =[] # DEFINIMOS NUESTRA PILA VACIA


#PUSH - operacion para agregar elementos 

pila.append (18)
pila.append (25)
pila.append (56)
 
print(pila)

peek = pila.pop ()
print("el elemento sacado de la pila fue:", peek)


pilaString = []

pilaString.append ('rafa')
pilaString.append ('irving')
pilaString.append ('pedro')
pilaString.append ('francisco')

print(pilaString)
pilaString.pop()
print(pilaString)

cima = pila.pop()
print ("la cima es",cima)
