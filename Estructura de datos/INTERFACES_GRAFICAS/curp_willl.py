import tkinter as tk
from datetime import datetime

def calcular_curp():
    
    nombre = entry_nombre.get().upper()
    apellido_paterno = entry_apellido_paterno.get().upper()
    apellido_materno = entry_apellido_materno.get().upper()
    fecha_nacimiento = entry_fecha_nacimiento.get()

   
    curp = apellido_paterno[:2] + apellido_materno[0] + nombre[0] + fecha_nacimiento[2:4] + fecha_nacimiento[5:7] + fecha_nacimiento[8:]

    resultado.config(text=f"Se ha generado la CURP: {curp}")

ventana = tk.Tk()
ventana.title("Calculadora de CURP")

tk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=10, pady=10)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1, padx=10, pady=10)

tk.Label(ventana, text="Apellido Paterno:").grid(row=1, column=0, padx=10, pady=10)
entry_apellido_paterno = tk.Entry(ventana)
entry_apellido_paterno.grid(row=1, column=1, padx=10, pady=10)

tk.Label(ventana, text="Apellido Materno:").grid(row=2, column=0, padx=10, pady=10)
entry_apellido_materno = tk.Entry(ventana)
entry_apellido_materno.grid(row=2, column=1, padx=10, pady=10)

tk.Label(ventana, text="Fecha de Nacimiento (YYYY-MM-DD):").grid(row=3, column=0, padx=10, pady=10)
entry_fecha_nacimiento = tk.Entry(ventana)
entry_fecha_nacimiento.grid(row=3, column=1, padx=10, pady=10)

btn_calcular = tk.Button(ventana, text="Calcular CURP", command=calcular_curp)
btn_calcular.grid(row=4, column=0, columnspan=2, pady=10)

resultado = tk.Label(ventana, text="")
resultado.grid(row=5, column=0, columnspan=2, pady=10)

ventana.mainloop()