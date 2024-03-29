from tkinter import Button, Frame, Tk

root = Tk()
root.title("Ejemplo de Frames")
root.geometry("200x70")

frame1 = Frame(root, bg="blue")
frame1.pack(expand=True, fill="both")

frame2 = Frame(root, bg="yellow")
frame2.pack(expand=True, fill="both")
frame2.config(cursor="heart")

redbutton = Button(frame1, text="Red", fg="red")
greenbutton = Button(frame1, text="Brown", fg="brown")
bluebutton = Button(frame1, text="Blue", fg="blue")

redbutton.place(relx=.05, rely=.05, relwidth=.25, relheight=.9)
greenbutton.place(relx=.35, rely=.05, relwidth=.25, relheight=.9)
bluebutton.place(relx=.65, rely=.05, relwidth=.25, relheight=.9)


blackbutton = Button(frame2, text="Black", fg="black")
blackbutton.pack()

root.mainloop()
