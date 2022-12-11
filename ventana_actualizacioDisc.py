from tkinter import *
import sqlite3
import datetime
import avanzado
import nameBD


def actulDisci():
    """
    esta funcion contiene la ventana de actualizacion de datos disciplinarios de un alumno
    :return:
    """

    root = Toplevel()

    root.title("DULA-ACTUALIZAR INFO DISCIPLINARIA")
    root.geometry("700x390")
    root.config(bg = "grey85")
    root.resizable(0,0)
    root.iconbitmap("images/dula.ico")



    # -------------imagenes de la raiz---------------------------------------------


    logo = PhotoImage(file="images/logoTsei.png")
    labeLogo = Label(root, image=logo)
    labeLogo.pack(side="right", anchor="n")
    # -----BOTON DE CIERRE DE VENTANA----------------------
    botonCerrarV = Button(root, text="cerrar la ventana",
                          command=root.destroy, activebackground="#F50743")
    botonCerrarV.config(font=("comic sans ms", 10), bg="salmon3", cursor="hand2")
    botonCerrarV.pack(side="left", anchor="s")
    #----------variables----------------------------------------------------------
    textoNombre = StringVar()

    # -------------label de la raiz------------------------------------------------------------------

    tituloLabel = Label(root, text="ACTUALIZACIÓN DE DATOS")
    tituloLabel.config(font=("jokerman", 14), bd=5, relief="groov", fg="black", bg="lemonchiffon2")
    tituloLabel.pack()
    #---------------------frame1---------------------------------------------------------------------
    frame1 =Frame(root,)
    frame1.config(width = 50, height = 20, bg = "grey85")
    frame1.place(x = 60, y = 87)
    #------------label frame1--------------------------------------------------------------------
    label1F1 = Label(frame1, text = "INFORMACIÓN DEL AÑO EN CURSO")
    label1F1.config(font=("comic sans ms", 10), bd=5, relief="groove", bg="antique white")
    label1F1.grid(row = 0, column = 0, padx = 5, pady = 5)

    label2F1 = Label(frame1, text = "Nombre completo")
    label2F1.config(font=("comic sans ms", 10), relief = "groove", bg = "white")
    label2F1.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "e")

    label3F1 = Label(frame1, text="Descripción de la falta:")
    label3F1.config(font=("comic sans ms", 10), relief="groove", bg="white")
    label3F1.grid(row=2, column=0, padx=5, pady=5, sticky="ne")

    #--------Entry frame1-------------------------------------
    entry1F1 = Entry(frame1, textvariable = textoNombre, width = 36)
    entry1F1.config(font=("comic sans ms", 10))
    entry1F1.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = "w")

    # --------------Text frame1-----------------------------
    textDescrip = Text(frame1, width=36, height=6)
    textDescrip.config(font=("comic sans ms", 12))
    textDescrip.grid(row=2, column=1, padx=5, pady=5, sticky="w")
    #-------------boton frame1-------------------------------------
    botonActua = Button(frame1, text = "Actualizar", activebackground="#F50743",
                        command = lambda:actuInfo())
    botonActua.config(font=("comic sans ms", 10), bg="white", cursor="hand2", relief = "sunken", bd = 4)
    botonActua.grid(row = 3, column = 1, padx = 5, pady = 5, columnspan = 2)

    #------------funciones--------------------------------------------------
    def actuInfo():
        """
        esta funcion permite actualizar las informaciones tales como, el numero de faltas, la descripcion de la falta
        :return:
        """
        try:
            connexion = sqlite3.connect(nameBD.nomBD())
            cursor = connexion.cursor()
            fechaHora = datetime.datetime.now()

            cursor.execute(f"select numero_de_faltas, descripcion from disciplina where nombre_y_apellidos = '{textoNombre.get().strip().upper()}'")
            stock = cursor.fetchall()
            stock1 = stock[0][0] + 1
            stock2 = stock[0][1] + "\n"
            stock3 = fechaHora.strftime('%d/%m/%Y ') + "\n"

            cursor.execute(f"update disciplina set descripcion = '{stock2+ stock3  +textDescrip.get(1.0, END)}'"
                           f" where nombre_y_apellidos = '{textoNombre.get().strip().upper()}' ")
            connexion.commit()

            cursor.execute(f"update disciplina set numero_de_faltas = '{stock1}' where nombre_y_apellidos = '{textoNombre.get().strip().upper()}' ")
            connexion.commit()
            connexion.close()

            textDescrip.delete(1.0, END)
            textoNombre.set("")



        except IndexError:
            pass

























    root.mainloop()