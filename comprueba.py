from tkinter import *
import sqlite3
import datetime

"""
print(datetime.date(2018, 3, 4))
valor = datetime.date(2018, 3, 4)

for letra in valor:
    print(letra)
"""

def ventana():

    root = Tk()
    root.config(bg = "yellow")
    root.geometry("200x100")


    boton = Button(root, text = "cambiar")
    boton.pack()
    valor = StringVar()

    entry = Entry(root, textvariable = valor)
    entry.pack()

    label = Label(root, text = "")
    label.place(x = 100, y = 200)

    def update():
        label.config(text = f"{valor.get()}", bg = "yellow", font = ("chiller", 14))
        label.after(500, update)
    update()

    root.mainloop()

ventana()

