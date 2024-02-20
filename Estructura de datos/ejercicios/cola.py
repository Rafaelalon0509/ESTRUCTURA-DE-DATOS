#definicion
#una estructura de datos que almacena de forma lineal y en un orden y con expulsion de primero de entra y primero sale 
#usa el principio fifo

from collections import deque 
cola = deque()

#encolar
cola.append('Rafa')
cola.append('irving')
cola.append('pedro')
cola.append('will')
print(cola)

cola.appendleft('Francisco')
print(cola)


# desencolar
elemento = cola.popleft()
print(elemento)
