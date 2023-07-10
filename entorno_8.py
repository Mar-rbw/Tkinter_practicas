from tkinter import Tk, Label, Button, Entry, Frame


class MyVentana(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=320, height=170)
        self.master = master
        self.pack()
        self.create_widgets()

    def fnSumar(self):
        n1 = self.txt1.get()
        n2 = self.txt2.get()
        result = float(n1) + float(n2)
        self.txt3.delete(0, "end")
        self.txt3.insert(0, result)

    def create_widgets(self):
        """Para hacer bien la distribución para las columnas suma x + y + height(Seguidamente)
        Para el caso de las filas suma x  + y + widget(Solo requieres calcularlo 1 vez)
        """
        # Primero fila
        self.lbl1 = Label(self, text="Primer número", bg="yellow")
        self.lbl1.place(x=10, y=10, width=100, height=30)

        self.txt1 = Entry(self, bg="pink")
        self.txt1.place(x=120, y=10, width=100, height=30)

        # Segunda fila
        self.lbl2 = Label(self, text="Segundo número", bg="yellow")
        self.lbl2.place(x=10, y=50, width=100, height=30)

        self.txt2 = Entry(self, bg="pink")
        self.txt2.place(x=120, y=50, width=100, height=30)

        self.btn1 = Button(self, text="Sumar", command=self.fnSumar)
        self.btn1.place(x=230, y=10, width=100, height=30)

        # Tercera fila
        self.lbl3 = Label(self, text="Resultado", bg="yellow")
        self.lbl3.place(x=10, y=130, width=100, height=30)

        self.txt3 = Entry(self, bg="pink")
        self.txt3.place(x=120, y=130, width=100, height=30)


""" Para cambiar la resolución a relativo se debe usar
    la siguiente ecuación:
        relx = x / ancho_de_ventana
        rely = y / altura_de_ventana
        
        Ejemeplo:
            El valor de "x" es 400 (ancho de la ventana).
            El valor de "y" es 200 (altura de la ventana).
            
            relx = x / 400
            rely = y / 200
         """
vent = Tk()
vent.wm_title("Suma de numeros")
app = MyVentana(vent)
app.mainloop()
