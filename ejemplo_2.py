import tkinter as tk
from tkinter import ttk

class Tab1:
    def __init__(self, tab):
        self.tab = tab
        self.create_widgets()

    def create_widgets(self):
        self.label = ttk.Label(self.tab, text="Proceso 1")
        self.label.pack(pady=20)

        self.button = ttk.Button(self.tab, text="Ejecutar Proceso 1", command=self.run_process_1)
        self.button.pack(pady=10)

    def run_process_1(self):
        self.label.configure(text="Proceso 1 en ejecución...")

        # Lógica del proceso 1
        # ...


class Tab2:
    def __init__(self, tab):
        self.tab = tab
        self.create_widgets()

    def create_widgets(self):
        self.label = ttk.Label(self.tab, text="Proceso 2")
        self.label.pack(pady=20)

        self.button = ttk.Button(self.tab, text="Ejecutar Proceso 2", command=self.run_process_2)
        self.button.pack(pady=10)

    def run_process_2(self):
        self.label.configure(text="Proceso 2 en ejecución...")

        # Lógica del proceso 2
        # ...


# Crear la ventana principal de tkinter
root = tk.Tk()
root.title("Aplicación con Pestañas")

# Crear un objeto Notebook (pestañas)
notebook = ttk.Notebook(root)
notebook.pack(pady=10, fill='both', expand=True)

# Crear las pestañas
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)

# Agregar las pestañas al notebook
notebook.add(tab1, text="Pestaña 1")
notebook.add(tab2, text="Pestaña 2")

# Crear el contenido de cada pestaña
tab1_content = Tab1(tab1)
tab2_content = Tab2(tab2)

# Ejecutar la aplicación
root.mainloop()
