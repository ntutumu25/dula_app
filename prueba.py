from tkinter import *
import datetime
import mysql.connector


def hora():
    """
    esta funcion permite obtener la hora y la fecha actual del ordenador
    :return: devuelve la fecha y la hora
    """

    fechaHora = datetime.datetime.now()
    #print(fechaHora)
    #print(fechaHora.strftime('%d/%m/%Y %H:%M:%S'))

    return fechaHora.strftime('%d/%m/%Y %H:%M:%S')



def hora1():
    fechaHora = datetime.datetime.now()
    # print(fechaHora)
    # print(fechaHora.strftime('%d/%m/%Y %H:%M:%S'))
    while True:
        return fechaHora.strftime(' %H:%M:%S')

import tkinter as tk


DELAY = 500

def update_cursor():
    if cursor["fg"] == "black":
        cursor.config(fg="#3ADF00")
    else:
        cursor.config(fg="black")
    cursor.after(DELAY, update_cursor)

root = tk.Tk()
root.geometry("300x200")
root.config(bg="black")
tk.Label(
    root, text="C:", fg="#3ADF00", bg="black", font=("Courier", 15)
    ).pack(side=tk.LEFT)
cursor = tk.Label(root, fg="#3ADF00", bg="black", text=" ▌", font=("Courier", 15))
cursor.pack(side=tk.LEFT)
cursor.after(0, update_cursor)

root.mainloop()