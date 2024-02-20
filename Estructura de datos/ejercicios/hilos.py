import threading
import time
import random

# Función que será ejecutada por cada hilo
def descarga_juegos(juego):
    tiempo_descarga = random.randint(1, 5)
    print(f"descargando juego {juego}. Tiempo estimado: {tiempo_descarga} segundos.")
    time.sleep(tiempo_descarga)
    print(f"{juego} descargado exitosamente en {tiempo_descarga} segundos.")

juegos_a_descargar = ["minecraft", "codm", "gears 3", "fortnite", "resident evil"]

hilos = []
for juegos in juegos_a_descargar:
    hilo = threading.Thread(target=descarga_juegos, args= (juegos,))
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()


print("Todos las descargas han terminado.")