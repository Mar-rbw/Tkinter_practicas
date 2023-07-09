from tkinter import Tk, Label, Button, Entry

vent = Tk()
vent.title("Ejemplo de place")
vent.geometry("400x200")

def fnSumar():
    n1 = txt1.get()
    n2 = txt2.get()
    result = float(n1) + float(n2)
    txt3.delete(0, "end")
    txt3.insert(0,result)

lbl1 = Label(vent,text="Primer número", bg="yellow")
txt1 = Entry(vent, bg="pink")
lbl2 = Label(vent,text="Segundo número", bg="yellow")
txt2 = Entry(vent, bg="pink")
btn1 = Button(vent,text="Sumar",command=fnSumar)
lbl3 = Label(vent,text="Resultado", bg="yellow")
txt3 = Entry(vent, bg="cyan")

lbl1.grid(row=0, column=0, padx=6, pady=6, sticky="w", ipady=6)
txt1.grid(row=0, column=1, padx=6, pady=6)
lbl2.grid(row=1, column=0, padx=6, pady=6, sticky="w", ipady=6)
txt2.grid(row=1, column=1, padx=6, pady=6)
btn1.grid(row=1, column=2, padx=6, pady=6, ipady=6, ipadx=10)
lbl3.grid(row=2, column=0, padx=6, pady=6, sticky="w", ipady=6)
txt3.grid(row=2, column=1, padx=6, pady=6)

vent.mainloop()