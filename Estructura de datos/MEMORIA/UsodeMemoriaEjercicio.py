class Tarea:
    tareas = []  

    def __init__(self, nombre, fecha_inicial, fecha_limite):
        self.nombre = nombre
        self.fecha_inicial = fecha_inicial
        self.fecha_limite = fecha_limite
        Tarea.tareas.append(self)  

    def mostrar_tareas(self):
        print("Lista de tareas:")
        for tarea in Tarea.tareas:
            print(f"Nombre: {tarea.nombre}, Fecha inicial: {tarea.fecha_inicial}, Fecha límite: {tarea.fecha_limite}")


tarea1 = Tarea("Ir al mercado", "19/01/2024", "19/01/2024")
tarea2 = Tarea("Vacaciones", "19/01/2024", "15/02/2024")
tarea3 = Tarea("Trabajo", "17/01/2024", "19/01/2024")
tarea4 = Tarea("Exposiciones", "19/01/2024", "22/01/2024")


tarea1.mostrar_tareas()


    

