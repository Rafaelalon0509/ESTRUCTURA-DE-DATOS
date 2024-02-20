from collections import deque

def rotacion_de_empleados(empleados, trunos):

    cola_empleados = deque(empleados)

    for _ in range (trunos):
        empleado_actual = cola_empleados.popleft()
        cola_empleados.append(empleado_actual)
        print("empleado en turno: ",cola_empleados [0])

#ejemplo de uso 
empleados = ["Francisco", "Rafa", "Irving", "Pedro"]
rotacion_de_empleados(empleados, 7) 