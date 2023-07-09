# Aprendiendo Tkinter

primero importamos:
from tkinter import *

def miFuncion():
    print("Este mensaje es del boton")

__Ventana principal de la aplicacion__
root = Tk()
__El titulo de la aplicación__
root.title("Hola Mundo")
__Resolucion de la aplicacion__
root.geometry("720x480")

__Contenido de un Label__
lbl = Label(root,text="Este es un label")

__posicinar el metodo a la ventana__
lbl.pack()

__objeto btn de la clase boton y su contructor__
**COMMAND funciona como un AddEvent**
btn = Button(root, text="presionar",command=miFuncion)
btn.pack()

__inicia el ciclo de mensajes, al momento de interactuar con tu aplicación__
mainloop()

## Configurar widgets Tkinter

Hay 3 formas:

* constructor:
    * miBoton = Button(self,fg="red",bg="blue")

* Método config:
    * miBoton.config(fg = "red", bg = "blue")

* Accediendo a la propiedad(como un diccionario clave/valor)
    * miBoton["fg"] = "red"
    * miBoton["bg"] = "blue"

    nota: fg = cambia el color de la letra y bg = cambia el color del fondo del elemento

**opción 1:**
btn = Button(root, text="presionar", fg="red", bg="yellow",command=miFuncion)
btn.pack()

**opción 2:**
btn = Button(root, text="presionar",command=miFuncion)
btn.config(fg="red", bg="yellow")
btn.pack()

**opción 3:**
btn = Button(root, text="presionar", , bg="yellow",command=miFuncion)
btn["fg"] = "red"
btn["bg"] = "yellow"
btn.pack()

## Extensión .pyw
Normamente los script de Python son almacenados con la extensión.py, para ejecutar este script.

En Windows, Necesitamos abrir una consola de comandos y ejecutar : [name_aplication].py

Pero si cambiamos la extensión a .pyw la aplicación se ejecutara automáticmente al hacer soble clic sobre ella.