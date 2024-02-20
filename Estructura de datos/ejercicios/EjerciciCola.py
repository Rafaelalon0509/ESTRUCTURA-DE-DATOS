from collections import deque 


class SistemaGestionTareas:
    def __init__(self):
        self.tareas_pendientes = deque 

     
    def agregar_tarea(self, tarea):
        self.tareas_pendientes.append(tarea)  
        print(self.tareas_pendientes) 

    def procesar_tareas(self):
        while self.tareas_pendientes:
            tarea = self.tareas_pendientes.popleft()
            print("procesando tarea: ", tarea)

#ejemplo de uso 
sistema = SistemaGestionTareas()
sistema.agregar_tarea("desayunar")
sistema.agregar_tarea("bañarse")
sistema.agregar_tarea("tender cama")
sistema.procesar_tareas()
