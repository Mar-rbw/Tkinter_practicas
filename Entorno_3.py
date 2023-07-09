from tkinter import Tk, Label, Button, Entry

vent = Tk()
vent.title("Ejemplo de place")
vent.geometry("400x200")

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


def fnSumar():
    n1 = txt1.get()
    n2 = txt2.get()
    result = float(n1) + float(n2)
    txt3.delete(0, "end")
    txt3.insert(0,result)

""" Para hacer bien la distribución para las columnas suma x + y + height(Seguidamente) 
    Para el caso de las filas suma x  + y + widget(Solo requieres calcularlo 1 vez) """
#Primero fila
lbl1 = Label(vent,text="Primer número", bg="yellow")
lbl1.place(x=10,y=10, width=100, height=30)

txt1 = Entry(vent, bg="pink")
txt1.place( x=120, y=10, width=100, height=30)

#Segunda fila
lbl2 = Label(vent,text="Segundo número", bg="yellow")
lbl2.place(x=10,y=50, width=100, height=30)

txt2 = Entry(vent, bg="pink")
txt2.place(x=120, y=50, width=100, height=30)

btn1 = Button(vent,text="Sumar",command=fnSumar)
btn1.place(x=230, y=10, width=100, height=30)

#Tercera fila
lbl3 = Label(vent,text="Resultado", bg="yellow")
lbl3.place(x=10,y=130, width=100, height=30)

txt3 = Entry(vent, bg="pink")
txt3.place(x=120, y=130, width=100, height=30)

vent.mainloop()