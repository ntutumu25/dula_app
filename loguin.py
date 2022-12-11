from tkinter.ttk import *
from tkinter import *
import ventana_cursos
import sqlite3
import archivos
import datetime
import nameBD
from tkinter import messagebox
from tkinter import filedialog


def loguin():

    root1 = Toplevel()
    root1.title("DULA 1.0 AUTORIZACIÓN")
    root1.resizable(0, 0)

    root1.geometry("700x420")
    root1.config(bg = "grey85")
    #-----------label root------------------------

    logo = PhotoImage(file="images/logoTsei.png")
    labeLogo = Label(root1, image=logo)
    labeLogo.place(x = 540, y = 0)

    root1.iconbitmap("images/dula.ico")


    #--------------botones de cierre de la ventana------------------------------------
    botonCerrarV = Button(root1, text="cerrar la ventana",
                          command=root1.destroy, activebackground="#F50743")
    botonCerrarV.config(font=("comic sans ms", 10), bg="salmon3", cursor="hand2")
    botonCerrarV.pack(side="left", anchor="s")

    #-----------frame root------------------------------
    frameEspace = Frame(root1, width = 10, height = 65)
    frameEspace.config(bg = "grey85")
    frameEspace.pack()

    #----------------label espacio-------------------------------
    Label(frameEspace, text = "CONTROL DE ACCESO", font=("jokerman", 14),
          bd=5, relief="groov", fg="black", bg="lemonchiffon2").grid(row = 0, column = 0, pady = 10, sticky = "w")

    #--------------------------------------------------

    frame = Frame(root1, width = 800)
    frame.config(bg = "grey85")
    frame.pack()


    # -----------notebook de ramas pestagna de unoBach----------------------------------

    notebook = Notebook(frame, width = 850, height = 330)
    notebook.pack()

    sesion = Frame(notebook)
    sesion.config(bg="grey85")
    notebook.add(sesion, text="INICIAR SESIÓN")

    registro = Frame(notebook)
    registro.config(bg="grey85")
    notebook.add(registro, text="REGISTRARSE")


    #-----------LABELS SESION---------------------------------------------------
    #-------------variables--------------------------------------------------
    usuario = StringVar()
    password = StringVar()

    Label(sesion, text = "USUARIO: ", font = ("comic sans ms", 10),
          bg = "grey85").grid(row = 0, column = 0, pady = 3, sticky = "e")

    Label(sesion, text="CONTRASEÑA: ", font=("comic sans ms", 10),
          bg="grey85").grid(row=1, column=0, pady=10, sticky="e")


    #---------------ENTRY SESION-------------------------------------------------
    Entry(sesion, width = 30, font = ("comic sans ms",11), bg = "grey95", textvariable = usuario,
          justify = "center").grid(row=0, column=1, pady=10, sticky="w")

    Entry(sesion, width=30, font = ("comic sans ms",11), show ="*", bg = "grey95", textvariable = password,
          justify = "center").grid(row=1, column=1, pady=10, sticky="w")

    #----------------------BOTONES SESION---------------------------------------------------
    Button(sesion, text = "iniciar sesión", cursor = "hand2",command = lambda:control(),
           font = ("comic sans ms",11)).grid(row=2, column=1, pady=10, )
    #----------------------REGISTRO---------------------------------------------
    #----------------------variables de registro-----------------------------------
    usuarioRegis = StringVar()
    nombreUsuarioRegis = StringVar()
    passwordRegis = StringVar()
    passwordConfirm = StringVar()
    preguntaUnoRegis = StringVar()
    preguntaDosRegis = StringVar()

    #----------------label  registro---------------------------------------------------------------
    Label(registro, text="Nombre y apellidos: ", font=("comic sans ms", 11),
          bg="grey85").grid(row=0, column=0, pady=3, sticky="e")

    Label(registro, text="Nombre de usuario ", font=("comic sans ms", 11),
          bg="grey85").grid(row=1, column=0, pady=3, sticky="e")

    Label(registro, text="Contraseña ", font=("comic sans ms", 11),
          bg="grey85").grid(row=2, column=0, pady=3, sticky="e")

    Label(registro, text="Confirmar contraseña ", font=("comic sans ms", 11),
          bg="grey85").grid(row=3, column=0, pady=3, sticky="e")

    Label(registro, text="¿Cuál es el nombre de tu abuelo materno? ", font=("comic sans ms", 11),
          bg="grey85").grid(row=4, column=0, pady=3, sticky="e")

    Label(registro, text="¿Cuál es tu asignatura favorita? ", font=("comic sans ms", 11),
          bg="grey85").grid(row=5, column=0, pady=3, sticky="e")

    #-----------------ENTRY REGISTRO-------------------------------------------------------
    Entry(registro, width=30, font=("comic sans ms", 11), bg="grey95", textvariable=nombreUsuarioRegis,
          justify="left").grid(row=0, column=1, pady=3, sticky="w")

    Entry(registro, width=30, font=("comic sans ms", 11), bg="grey95", textvariable=usuarioRegis,
          justify="left").grid(row=1, column=1, pady=3, sticky="w")

    Entry(registro, width=30, font=("comic sans ms", 11), show = "*", bg="grey95", textvariable=passwordRegis,
          justify="center").grid(row=2, column=1, pady=3, sticky="w")

    Entry(registro, width=30, font=("comic sans ms", 11), show = "*", bg="grey95", textvariable=passwordConfirm,
          justify="center").grid(row=3, column=1, pady=3, sticky="w")

    Entry(registro, width=30, font=("comic sans ms", 11), bg="grey95", textvariable=preguntaUnoRegis,
          justify="left").grid(row=4, column=1, pady=3, sticky="w")

    Entry(registro, width=30, font=("comic sans ms", 11), bg="grey95", textvariable=preguntaDosRegis,
          justify="left").grid(row=5, column=1, pady=3, sticky="w")

    #---------------------BOTONES registro --------------------------------------------------------------
    Button(registro, text = "Registrar", cursor = "hand2",command = lambda:registrar(),
           font=("comic sans ms", 11)).grid(row=6, column=1, pady=5, sticky="w")






    #---------------funciones de sesion------------------------------------------------------

    def control():
        """
        esta funcion verifica la autecntoficacion de usuario para acceder a la ventana de registro de notas
        tambien escribe la autentificacion en un archivo
        :return:
        """
        try:

            connexion = sqlite3.connect(nameBD.nomBD())  # crear o abrir la conexion con al base de datos
            cursor = connexion.cursor()

            cursor.execute(f"select * from sesion where usuario = '{usuario.get()}'")
            stock = cursor.fetchall()
            global ventanas
            ventanas = stock[0][1]

            if password.get() == stock[0][2]:
                registro = open("system/infoS.txt", "a") # escribir en el archivo el inicio de sesion del usuario

                registro.write( "\n"+stock[0][1] + ", Ha iniciado una sesión  "+str(hora()) )
                registro.close()

                root1.destroy()
                ventana_cursos.cursos()

            else:

                Label(sesion, text="", font=("comic sans ms", 10),
                      bg="grey85").grid(row=3, column=1, pady=10, )


                Label(sesion, text="contraseña o nombre de usuario incorrecto", font=("comic sans ms", 11), fg = "red",
                      bg="grey85").grid(row=3, column=1, pady=10,)
                password.set("")
                usuario.set("")
                Button(sesion, text = "¿Has olvidado la contraseña?",activebackground="#F50743",command = lambda:recuperacionPassword(),
                       font=("comic sans ms", 11)).grid(row=4, column=1, columnspan = 2, pady=5,)

            connexion.close()

        except IndexError:
            Label(sesion, text="", font=("comic sans ms", 10),
                  bg="grey85").grid(row=3, column=1, pady=10, )

            Label(sesion, text="contraseña o nombre de usuario incorrecto", font=("comic sans ms", 11), fg = "red",
                  bg="grey85").grid(row=3, column=1, pady=10, )
            password.set("")
            usuario.set("")
            Button(sesion, text="¿Has olvidado la contraseña?", command = lambda:recuperacionPassword(),
                   cursor = "hand2", activebackground="#F50743", font=("comic sans ms", 11)).grid(row=4, column=1, columnspan=2, pady=5, )



    def registrar():
        """
        esta fucnion registra los datos de un usuario que tentra acceso a la venta de registro de notas
        :return:
        """

        try:

            connexion = sqlite3.connect(nameBD.nomBD())  # crear o abrir la conexion con al base de datos
            cursor = connexion.cursor()

            if nombreUsuarioRegis.get() and usuarioRegis.get() and passwordRegis.get() and preguntaDosRegis.get() and preguntaUnoRegis.get():

                if passwordRegis.get() == passwordConfirm.get():

                    campo1 = usuarioRegis.get().strip()
                    campo2 = nombreUsuarioRegis.get().upper().strip()
                    campo3 = passwordRegis.get().strip()
                    campo4 = preguntaUnoRegis.get().upper().strip()
                    campo5 = preguntaDosRegis.get().upper().strip()

                    avion = [
                        (campo1,  campo2,  campo3, campo4, campo5)
                    ]

                    cursor.executemany("insert into sesion values (?,?,?,?,?)", avion)
                    connexion.commit()

                    registro1 = open("system/registroUsuarios.txt",
                                     "a")  # registrar la informacion del usuarion en el archivo registroUsuarios.txt
                    registro1.write(
                        f"\n{hora()}\nUsuario: {usuarioRegis.get()} \nNombre completo del usuario: {nombreUsuarioRegis.get()}\n")
                    registro1.close()

                    usuarioRegis.set("")
                    nombreUsuarioRegis.set("")
                    passwordConfirm.set("")
                    passwordRegis.set("")
                    preguntaDosRegis.set("")
                    preguntaUnoRegis.set("")

                    Label(registro, text="                                                "
                                         "                      ", font=("comic sans ms", 10),
                          bg="grey85").grid(row=8, column=1, pady=10, columnspan = 2)

                    Label(registro, text="                              Registrado", font=("comic sans ms", 11), fg="green",
                          bg="grey85").grid(row=8, column=0, pady=10, columnspan = 2)

                else:
                    Label(registro, text="                                          ", font=("comic sans ms", 10),
                          bg="grey85").grid(row=8, column=1, pady=10, columnspan = 2)

                    Label(registro, text="             las contraseñas no coinciden", font=("comic sans ms", 11), fg="red",
                          bg="grey85").grid(row=8, column=0, pady=10, columnspan = 2)
                    passwordRegis.set("")
                    passwordConfirm.set("")

            else:
                Label(registro, text="                                                    ", font=("comic sans ms", 10),
                      bg="grey85").grid(row=8, column=1, pady=10, columnspan=2)

                Label(registro, text="                 completa todos los campos", font=("comic sans ms", 11), fg="red",
                      bg="grey85").grid(row=8, column=0, pady=10, columnspan=2)

                usuarioRegis.set("")
                nombreUsuarioRegis.set("")
                passwordConfirm.set("")
                passwordRegis.set("")
                preguntaDosRegis.set("")
                preguntaUnoRegis.set("")

        except sqlite3.IntegrityError:
            Label(registro, text="                                                              ", font=("comic sans ms", 10),
                  bg="grey85").grid(row=8, column=1, pady=10, columnspan=2)

            Label(registro, text=f"{usuarioRegis.get()}, existe ya como nombre de usuario",
                  font=("comic sans ms", 11), fg="red",
                  bg="grey85").grid(row=8, column=0, pady=10, columnspan=2)

    def recuperacionPassword():
        root1.destroy()
        root = Toplevel()
        root.title("DULA 1.0 RECUPARACIÓN DE CREDENCIALES")
        root.resizable(0, 0)

        root.geometry("700x200")
        root.config(bg="grey85")
        # -----------label root------------------------

        logo = PhotoImage(file="images/logoTsei.png")
        labeLogo = Label(root, image=logo)
        labeLogo.place(x=540, y=0)

        root.iconbitmap("images/dula.ico")

        # ----------------label root-------------------------------
        Label(root, text="RECUPERACIÓN DE CREDENCIALES", font=("jokerman", 14),
              bd=5, relief="groov", fg="black", bg="lemonchiffon2").pack()



        # ------------variables entry--------------------------------------
        cuestion1 = StringVar()
        cuestion2 = StringVar()

        motDepass = StringVar()
        motDepassConfirm = StringVar()

        #----------------frame root-------------------------------------------------
        frame = Frame(root, width = 200, height = 150)
        frame.config(bg = "grey85")
        frame.pack(pady = 35)
        #-------------label frame-----------------------------------------------------
        Label(frame, text = "Nombre de usuario", bg = "white",
              font=("comic sans ms", 10),bd=3, relief="groove" ).grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "e")
        #----------Entry frame------------------------------------------------------------------
        #------------variable entry------------------------------------------------
        entryFrame = StringVar()

        entry1 = Entry(frame, textvariable = entryFrame, width = 30)
        entry1.config(font=("comic sans ms", 10))
        entry1.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = "w")

        # -----------------entrys------------------------------------------------------------

        entryCues1 = Entry(frame, width=30, textvariable=cuestion1)
        entryCues1.config(font=("comic sans ms", 10), bg="grey100", justify="left")


        entryCues2 = Entry(frame, width=30, textvariable=cuestion2)
        entryCues2.config(font=("comic sans ms", 10), bg="grey100", justify="left")

        #--------------------BOTON FRAME--------------------------------------------------------------------------

        Button(frame, text = "Validar", cursor = "hand2", activebackground = "red", command = lambda:recup(),
               font=("comic sans ms", 10)).grid(row = 0, column = 2, padx = 5, pady = 5, sticky = "w")

        #------------------funcion de camabio de la contrasegna--------------------------------------

        def recup():
            """
            esta funcion permite que el usuario cambie su mot de passe, a partir del conocimento de su nombre de usuario,
            asi como las preguntas de seguridad
            :return:
            """
            connexion = sqlite3.connect(nameBD.nomBD())  # crear o abrir la conexion con al base de datos
            cursor = connexion.cursor()

            cursor.execute(f"select * from sesion")
            stock = cursor.fetchall()

            i = 0
            while i < len(stock):
                if entryFrame.get().strip() == stock[i][0]:
                    global avionUsua # varibale global del nombe del usuario
                    avionUsua = stock[i][0] # almacenamiento de la variable

                    global preg1  #--variable global para almacenar la pregunta 1
                    preg1 = stock[i][3]

                    global preg2  #--variable global para almacenar la pregunta 2
                    preg2 = stock[i][4]

                    labelInfo = Label(frame, text="")
                    labelInfo.config(font=("comic sans ms", 10), bg="grey85")
                    labelInfo.grid(row = 1, column = 0, padx = 5, pady = 5, columnspan = 3)

                    labelInfo = Label(frame, text=f"TITULAR DE LA CUENTA: {stock[i][1]}")
                    labelInfo.config(font=("comic sans ms", 10), bg="grey85")
                    labelInfo.grid(row=1, column=0, padx=5, pady=5, columnspan=3)
                    #-----------------LOS SIGUIENTES ELEMENTOS DE INDENTIFICACIO-------------------------
                    #----------------labels----------------------------------------------
                    Label(frame, text="¿Cuál es el nombre de tu abuelo materno? ", font=("comic sans ms", 10),
                          bg="grey85").grid(row=2, column=0, padx = 3, pady=3, sticky="e")

                    Label(frame, text="¿Cuál es tu asignatura favorita? ", font=("comic sans ms", 10),
                          bg="grey85").grid(row=3, column=0, padx = 3 , pady=3, sticky="e")
                    #-----------------entrys------------------------------------------------------------


                    entryCues1.grid(row=2, column=1, padx = 3 , pady=3, sticky="w")


                    entryCues2.grid(row=3, column=1, padx=3, pady=3, sticky="w")
                    #--------botones---------------------------------------------
                    Button(frame, text="Verificar", cursor="hand2", activebackground="red", command = lambda:comparar(),
                           font=("comic sans ms", 10)).grid(row=4, column=1, padx=5, pady=5, sticky="w")

                    #---------------------------------------------------------------------------
                    entry1.config(state = "readonly")#--bloqueo del cambo del nombre de usuario
                    root.geometry("700x300")#---aumentar la aventana
                    break

                i += 1
                if i == len(stock):
                    labelInfo = Label(frame, text="")
                    labelInfo.config(font=("comic sans ms", 10), bg="grey85")
                    labelInfo.grid(row=1, column=0, padx=5, pady=5, columnspan=3)

                    labelInfo = Label(frame, text="EL USUARIO NO EXISTE")
                    labelInfo.config(font=("comic sans ms", 10), bg="grey85", fg = "red")
                    labelInfo.grid(row=1, column=0, padx=5, pady=5, columnspan=3)

            connexion.close()




        def comparar():
            """
            esta funcion coprueba si las respuestas de las preguntas de seguridad son correctas
            :return:
            """

            if preg1 == cuestion1.get().strip().upper() and preg2 == cuestion2.get().strip().upper():
                root.geometry("700x450")

                entryCues1.config(state = "readonly")
                entryCues2.config(state="readonly")
                # --------------CONTINUAMOS CON LOS SIGUIENTES ELEMENTOS----------
                #------------labels-------------------------------------------------------------
                Label(frame, text="Nueva contraseña ", font=("comic sans ms", 10),
                          bg="grey85").grid(row=5, column=0, padx=3, pady=3, sticky="e")

                Label(frame, text="Confirmar la contraseña", font=("comic sans ms", 10),
                          bg="grey85").grid(row=6, column=0, padx=3, pady=3, sticky="e")
                #---------------entrys---------------------------------------------

                entryPassword = Entry(frame, width=30,)
                entryPassword.config(font=("comic sans ms", 10), bg="grey100", show = "*",textvariable=motDepass, justify="center")
                entryPassword.grid(row=5, column=1, padx=3, pady=3, sticky="w")

                entryPasswordConfir = Entry(frame, width=30, )
                entryPasswordConfir.config(font=("comic sans ms", 10), bg="grey100", show="*", textvariable=motDepassConfirm,
                                     justify="center")
                entryPasswordConfir.grid(row=6, column=1, padx=3, pady=3, sticky="w")
                #-------------botones-------------------------------------------------------------

                Button(frame, text="Guardar", cursor="hand2", activebackground="red", command = lambda:actualizarMotdepasse(),
                       font=("comic sans ms", 10)).grid(row=7, column=1, padx=5, pady=5, sticky="w")

            else:
                cuestion1.set("RESPUESTA INCORRECTA!!")
                cuestion2.set("RESPUESTA INCORRECTA!!")




        def actualizarMotdepasse():

            if motDepass.get().strip() == motDepassConfirm.get().strip():
                print(avionUsua)
                connexion = sqlite3.connect(nameBD.nomBD())  # crear o abrir la conexion con al base de datos
                cursor = connexion.cursor()

                cursor.execute(f"update sesion set password = '{motDepass.get()}' where  usuario = '{avionUsua}' ")
                connexion.commit()
                connexion.close()

                Label(frame, text="                                          ", font=("comic sans ms", 10),
                      bg="grey85", fg="green").grid(row=8, column=0, padx=3, pady=3, columnspan=3)

                Label(frame, text="éxito en el cambio", font=("comic sans ms", 10),
                      bg="grey85", fg = "green").grid(row=8, column=0, padx=3, pady=3, columnspan = 3)

                motDepassConfirm.set("")
                motDepass.set("")

                # -----BOTON DE CIERRE DE VENTANA----------------------
                botonCerrarV = Button(frame, text="cerrar la ventana",
                                      command=root.destroy, activebackground="#F50743")
                botonCerrarV.config(font=("comic sans ms", 10), bg="salmon3", cursor="hand2")
                botonCerrarV.grid(row=9, column=0, padx=3, pady=3, columnspan=3)




            else:
                Label(frame, text="", font=("comic sans ms", 10),
                      bg="grey85", fg="green").grid(row=8, column=0, padx=3, pady=3, columnspan=3)

                Label(frame, text="las contraseñas no coinciden", font=("comic sans ms", 10),
                      bg="grey85", fg="red").grid(row=8, column=0, padx=3, pady=3, columnspan=3)

                motDepassConfirm.set("")
                motDepass.set("")

                # -----BOTON DE CIERRE DE VENTANA----------------------
                botonCerrarV = Button(frame, text="cerrar la ventana",
                                      command=root.destroy, activebackground="#F50743")
                botonCerrarV.config(font=("comic sans ms", 10), bg="salmon3", cursor="hand2")
                botonCerrarV.grid(row=9, column=0, padx=3, pady=3, columnspan=3)













        root.mainloop()







    root1.mainloop()



def cierreSesion(l):
    """
    esta funcion permite anotar el cierre de sesion de un usuario en el archivo infoS.txt
    :return:
    """



    archivos = open("system/infoS.txt", "a")
    archivos.write(f"\n\n{ventanas} , ha cerrado la sesion {hora()}"
                           f"\n--------------------------------------------------------------"
                       f"-----------------------------------------------------------------------------")
    archivos.close()
    l.destroy()



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


def nombreSesion():
    """
    esta funcion almacena el nombre del usuario en sesion, con el fin de llevarla a la ventana notas
    :return:
    """
    return ventanas



