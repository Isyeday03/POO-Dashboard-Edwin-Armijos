# interfaz/interfaz_animales.py

import tkinter as tk
from tkinter import ttk, messagebox
from animales import Perro, Gato, Loro

class Interfaz:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Gestión de Animales")
        self.ventana.geometry("400x300")
        self._centrar_ventana()
        self._crear_widgets()

    def _centrar_ventana(self):
        w, h = 400, 300
        sw = self.ventana.winfo_screenwidth()
        sh = self.ventana.winfo_screenheight()
        x = (sw // 2) - (w // 2)
        y = (sh // 2) - (h // 2)
        self.ventana.geometry(f"{w}x{h}+{x}+{y}")

    def _crear_widgets(self):
        tk.Label(self.ventana, text="Nombre:").pack(pady=5)
        self.entry_nombre = tk.Entry(self.ventana)
        self.entry_nombre.pack()

        tk.Label(self.ventana, text="Edad:").pack(pady=5)
        self.entry_edad = tk.Entry(self.ventana)
        self.entry_edad.pack()

        tk.Label(self.ventana, text="Tipo de Animal:").pack(pady=5)
        self.tipo_animal = ttk.Combobox(self.ventana, values=["Perro", "Gato", "Loro"])
        self.tipo_animal.pack()

        self.check_var = tk.BooleanVar()
        self.entry_extra = tk.Entry(self.ventana)
        self.entry_extra.pack(pady=5)
        self.entry_extra.insert(0, "Raza / Color / ¿Habla?")

        tk.Button(self.ventana, text="Crear Animal", command=self.crear_animal).pack(pady=10)

    def crear_animal(self):
        nombre = self.entry_nombre.get()
        try:
            edad = int(self.entry_edad.get())
        except ValueError:
            messagebox.showerror("Error", "Edad inválida.")
            return
        tipo = self.tipo_animal.get().lower()
        extra = self.entry_extra.get().strip()

        if tipo == "perro":
            animal = Perro(nombre, edad, extra)
        elif tipo == "gato":
            animal = Gato(nombre, edad, extra)
        elif tipo == "loro":
            puede_hablar = extra.lower() in ["sí", "si", "true", "1"]
            animal = Loro(nombre, edad, puede_hablar)
        else:
            messagebox.showerror("Error", "Selecciona un tipo válido.")
            return

        messagebox.showinfo("Animal creado", f"{animal.get_nombre()} dice:")
        messagebox.showinfo("Animal creado", f"{animal.get_nombre()} dice:\n{animal.hacer_sonido()}")


    def ejecutar(self):
        self.ventana.mainloop()
