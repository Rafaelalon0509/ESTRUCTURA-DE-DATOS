import tkinter as tk


class EditorTextoFrame(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.historial = []

        self.text_label = tk.Label(self, text="Texto actual")
        self.text_label.pack()

        self.texto_var = tk.StringVar()

        self.texto_actual = tk.Label(self, textvariable = self.texto_var)
        self.texto_actual.pack()

        self.entry_texto = tk.Entry(self)
        self.entry_texto.pack()

        self.boton_agregar = tk.Button(self, text="Agregar texto", command=self.agregar_texto)
        self.boton_agregar.pack()

        self.boton_deshacer = tk.Button(self, text="Deshacer", command=self.deshacer)
        self.boton_deshacer.pack()

        self.pack()

#esta funcion usa la operacion push

def agregar_texto(self):
    texto_nuevo = self.entry_texto.get()#obtener texto del entry
    self.historial.append(texto_nuevo)
    self.entry_texto.delete(0, tk.END) # limpiiar el entry despues de agregar el texto
    self.actualizar_texto()

#esta funcion usa pop
def deshacer(self):
    if self.historial:
        self.historial.pop()
    self.actualizar_texto()


def actualizar_texto(self):
    texto_actual = "".join(self.historial)
    self.texto_var.set(texto_actual)

root = tk.Tk()
editor_franme = EditorTextoFrame(master=root)
editor_franme.mainloop()