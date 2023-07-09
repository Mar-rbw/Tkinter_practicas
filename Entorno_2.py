from tkinter import *

def miFuncion():
    print("Este mensaje es del boton")

""" Ventana principal de la aplicacion """
root = Tk()
""" El titulo de la aplicacion """
root.title("Hola Mundo")
""" resolucion de la aplicacion """
root.geometry("720x480")


lbl = Label(root,text="Este es un label")
""" posicinar el metodo a la ventana """
lbl.pack()

""" objeto btn de la clase boton y su contructor
COMMAND funciona como un AddEvent  """
btn = Button(root, text="presionar", fg="red", bg="yellow",command=miFuncion)
btn.pack()
""" inicia el ciclo de mensajes, al momento de interactuar con tu aplicacion """
root.mainloop()

