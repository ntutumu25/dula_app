from tkinter.ttk import *
from tkinter import *
import sqlite3
import funciones
from tkinter import messagebox
from tkinter import filedialog
import archivos
import nameBD






def actualizarDatosAum():
    """
    :return: funcion de la ventana de actualiracion de datos del alumno,
    se actualiza la el curso, el nombre del tutor, el telefono del tutor,
    la patalogia de la salud, asi como la direccion y estado del alumno del centro
    """
    root = Toplevel()
    root.title("DULA-ACTUALIZACION DE DATOS")
    root.config(bg = "grey85")
    root.geometry("1020x450")
    root.resizable(0,0)

    botonCerrarV = Button(root, text="cerrar la ventana",
                          command=root.destroy, activebackground="#F50743")
    botonCerrarV.config(font=("comic sans ms", 10), bg="salmon3", cursor="hand2")
    botonCerrarV.pack(side="left", anchor="s")

    logo = PhotoImage(file="images/logoTsei.png")
    labeLogo = Label(root, image=logo)
    labeLogo.pack(side="right", anchor="n")

    #-----------variables-----------------


    opcionRadio2 = IntVar()

    textoEntryNomID = StringVar()


    nombreTutor = StringVar()
    telTutor = StringVar()
    fotoAlum = StringVar()
    fotoAlum.set("images/logoTsei.png")

    direccionAlum = StringVar()
    patologiaAlumno = StringVar()

    condicionAlumn = IntVar()

    # -------------imagenes de la raiz---------------------------------------------

    root.iconbitmap("images/dula.ico")


    # -------------label de la raiz------------------------------------------------------------------


    tituloLabel = Label(root, text="ACTUALIZACIÓN DE DATOS")
    tituloLabel.config(font=("jokerman", 14), bd=5, relief="groov", fg="black", bg="lemonchiffon2")
    tituloLabel.pack()

    """
    datosActualizar = Label(root, text="Selecciona el dato a actualizar del alumno/a:")
    datosActualizar.config(font=("comic sans ms", 12), bd=5, relief="groove", bg="white")
    datosActualizar.place(x = 300, y = 90)

    opcionRegistro = Label(root, text="Selecciona la opción de identificación:")
    opcionRegistro.config(font=("comic sans ms", 12), bd=5, relief="groove", bg="white")
    opcionRegistro.place(x=320, y=190)
    """

    # -----------notebook de ramas pestagna de unoBach----------------------------------

    notebook = Notebook(root, width=500, height=300)
    notebook.pack(expand=1, fill="both", padx=5, pady = 10)

    curso = Frame(notebook)
    curso.config(bg="grey85")
    notebook.add(curso, text="  CURSO  ")

    tutor = Frame(notebook)
    tutor.config(bg="grey85")
    notebook.add(tutor, text="  TUTOR/A  ")

    tutorTel = Frame(notebook)
    tutorTel.config(bg="grey85")
    notebook.add(tutorTel, text="  CONTANCTO DEL TUTOR/A  ")

    foto = Frame(notebook)
    foto.config(bg="grey85")
    notebook.add(foto, text="  FOTO  ")

    direccion = Frame(notebook)
    direccion.config(bg="grey85")
    notebook.add(direccion, text="  DIRECCIÓN  ")

    patologia = Frame(notebook)
    patologia.config(bg="grey85")
    notebook.add(patologia, text="  ESTADO DE SALUD  ")

    estadoAlumno = Frame(notebook)
    estadoAlumno.config(bg="grey85")
    notebook.add(estadoAlumno, text="  ESTADO DEL ALUMNO/A  ")

    # --------freme1 de la raiz-----------------------------------------------------------------------

    frame1 = Frame(root, width=200, height=100)
    frame1.config(bg="grey85")
    #frame1.place(x=125, y=140)

    frame2 = Frame(root, width=200, height=100)
    frame2.config(bg="grey85")
    #frame2.place(x=125, y=240)

    #--------- FRAME CURSO-----------------------------------------------------
    #----------label curso------------------------------
    Label(curso, text="CURSO", bd=5, relief="groove", bg="white",
          font=("comic sans ms", 11)).grid(row=0, columnspan = 4, padx=3, pady=10, )

    Label(curso, text = "Introduzca aqui el identificador:",  bd=5, relief="groove", bg="white",
          font=("comic sans ms", 11)).grid(row=2, column=0, padx=3, pady=3, sticky="e")
    Label(curso, text="Selecciona la opción de identificación:", bd=5, relief="groove", bg="white",
          font=("comic sans ms", 11)).grid(row=1, column=0, padx=3, pady=3, sticky="e")

    Label(curso, text="Curso:", bd=5, relief="groove", bg="white",
          font=("comic sans ms", 11)).grid(row=3, column=0, padx=3, pady=3, sticky="e")
    Label(curso, text="Año académico:", bd=5, relief="groove", bg="white",
          font=("comic sans ms", 11)).grid(row=4, column=0, padx=3, pady=3, sticky="e")

    Label(curso, text="Condición del alumno/a:", bd=5, relief="groove", bg="white",
          font=("comic sans ms", 11)).grid(row=5, column=0, padx=3, pady=3, sticky="e")

    # ------------Entry CURSO------------------------------------------------
    Entry(curso, width=35, textvariable=textoEntryNomID,
          font=("comic sans ms", 11)).grid(row=2, column=1, padx=3, pady=3, columnspan = 2, sticky="w")

    # --------------radioButton TUTOR-----------------------------------------------
    Radiobutton(curso, text="Nombre completo", variable=opcionRadio2, value=1, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2").grid(row=1, column=1, padx=3, pady=3, sticky="w")

    Radiobutton(curso, text="ID", variable=opcionRadio2, value=2, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2", ).grid(row=1, column=2, padx=3, pady=3, sticky="w")

    Radiobutton(curso, text="Curso siguiente", variable=condicionAlumn, value=1, bg="lightgreen",
                font=("comic sans ms", 11), cursor="hand2").grid(row=5, column=1, padx=3, pady=3, sticky="w")

    Radiobutton(curso, text="Repetir curso", variable=condicionAlumn, value=2, bg="palevioletred",
                font=("comic sans ms", 11), cursor="hand2", ).grid(row=5, column=2, padx=3, pady=3, sticky="w")


    #-------------COMBOBOX CURSO------------------------------------------------------------
    comboFecha = Combobox(curso, width=25, state = "readonly")
    comboFecha['values'] = ('2010/2011', '2011/2012', '2012/2013',
                            '2013/2014', '2014/2015', '2015/2016',
                            '2016/2017', '2017/2018', '2018/2019',
                            '2019/2020',
    '2020/2021', '2021/2022', '2022/2023', '2023/2024', '2024/2025', '2025/2026', '2026/2027', '2027/2028', '2028/2029',
    '2029/2030', '2030/2031', '2031/2032', '2032/2033', '2033/2034', '2034/2035', '2035/2036', '2036/2037', '2037/2038',
    '2038/2039', '2039/2040', '2040/2041', '2041/2042', '2042/2043', '2043/2044', '2044/2045', '2045/2046', '2046/2047',
    '2047/2048', '2048/2049', '2049/2050', '2050/2051', '2051/2052', '2052/2053', '2053/2054', '2054/2055', '2055/2056',
    '2056/2057', '2057/2058', '2058/2059', '2059/2060', '2060/2061', '2061/2062', '2062/2063', '2063/2064', '2064/2065',
    '2065/2066', '2066/2067', '2067/2068', '2068/2069', '2069/2070', '2070/2071', '2071/2072', '2072/2073', '2073/2074',
    '2074/2075', '2075/2076', '2076/2077', '2077/2078', '2078/2079', '2079/2080', '2080/2081', '2081/2082', '2082/2083',
    '2083/2084', '2084/2085', '2085/2086', '2086/2087', '2087/2088', '2088/2089', '2089/2090', '2090/2091', '2091/2092',
    '2092/2093', '2093/2094', '2094/2095', '2095/2096', '2096/2097', '2097/2098', '2098/2099', '2099/2100', '2100/2101',
    '2101/2102', '2102/2103', '2103/2104', '2104/2105', '2105/2106', '2106/2107', '2107/2108', '2108/2109', '2109/2110',
    '2110/2111', '2111/2112', '2112/2113', '2113/2114', '2114/2115', '2115/2116', '2116/2117', '2117/2118', '2118/2119',
    '2119/2120')
    comboFecha.grid(row=4, column=1, padx=3, pady=3, sticky="w")
    comboFecha.current(0)

    comboActualizar = Combobox(curso, width=12, state = "readonly")
    comboActualizar['values'] = ("1°ESBA", "2°ESBA", "3°ESBA", "4°ESBA", "1°BACH", "2°BACH")
    comboActualizar.current(0)
    comboActualizar.grid(row=3, column=1, padx=3, pady=3, sticky="w")

    #----------------------BOTONES CURSO-----------------------------
    botonActualizar = Button(curso, text="Actualizar", activebackground="#F50743",
                             command=lambda: curso1())
    botonActualizar.config(font=("comic sans ms", 11), cursor="hand2", relief="sunken", bd=4, bg="grey75")
    botonActualizar.grid(row=6, column=1, padx=3, pady=10, sticky="w")


    # --------- FRAME tutor-----------------------------------------------------
    # ----------label tutor----------------------------------------------------------------
    Label(tutor, text="NOMBRE DEL TUTOR/A", bd=5, relief="groove", bg="white",
          font=("comic sans ms", 11)).grid(row=0, columnspan=4, padx=3, pady=10, )

    Label(tutor, text="Introduzca aqui el identificador:", bd=5, relief="groove", bg="white",
          font=("comic sans ms", 11)).grid(row=2, column=0, padx=3, pady=3, sticky="e")
    Label(tutor, text="Selecciona la opción de identificación:", bd=5, relief="groove", bg="white",
          font=("comic sans ms", 11)).grid(row=1, column=0, padx=3, pady=3, sticky="e")

    Label(tutor, text="Nombre del tutor/a:", bd=5, relief="groove", bg="white",
          font=("comic sans ms", 11)).grid(row=3, column=0, padx=3, pady=3, sticky="e")


    # ------------Entry TUTOR------------------------------------------------
    Entry(tutor, width=35, textvariable=textoEntryNomID,
          font=("comic sans ms", 11)).grid(row=2, column=1, padx=3, pady=3, columnspan=2, sticky="w")

    Entry(tutor, width=35, textvariable=nombreTutor,
          font=("comic sans ms", 11)).grid(row=3, column=1, padx=3, pady=3, columnspan=2, sticky="w")


    # --------------radioButton TUTOR-----------------------------------------------
    Radiobutton(tutor, text="Nombre completo", variable=opcionRadio2, value=1, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2").grid(row=1, column=1, padx=3, pady=3, sticky="w")

    Radiobutton(tutor, text="ID", variable=opcionRadio2, value=2, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2", ).grid(row=1, column=2, padx=3, pady=3, sticky="w")

    # ----------------------BOTONES tutor------------------------------------------------------
    botonActualizar = Button(tutor, text="Actualizar", activebackground="#F50743",
                             command=lambda: nombreT())
    botonActualizar.config(font=("comic sans ms", 11), cursor="hand2", relief="sunken", bd=4, bg="grey75")
    botonActualizar.grid(row=4, column=1, padx=3, pady=3, sticky="w")



    # --------- FRAME tutorTel-----------------------------------------------------
    # ----------label tutor----------------------------------------------------------------
    Label(tutorTel, text="CONTACTO DEL TUTOR/A", bd=5, relief="groove", bg="white",
          font=("comic sans ms", 11)).grid(row=0, columnspan=4, padx=3, pady=10, )

    Label(tutorTel, text="Introduzca aqui el identificador:", bd=5, relief="groove", bg="white",
          font=("comic sans ms", 11)).grid(row=2, column=0, padx=3, pady=3, sticky="e")
    Label(tutorTel, text="Selecciona la opción de identificación:", bd=5, relief="groove", bg="white",
          font=("comic sans ms", 11)).grid(row=1, column=0, padx=3, pady=3, sticky="e")

    Label(tutorTel, text="N° de teléfono del tutor/a:", bd=5, relief="groove", bg="white",
          font=("comic sans ms", 11)).grid(row=3, column=0, padx=3, pady=3, sticky="e")

    # ------------Entry tutorTel------------------------------------------------
    Entry(tutorTel, width=35, textvariable=textoEntryNomID,
          font=("comic sans ms", 11)).grid(row=2, column=1, padx=3, pady=3, columnspan=2, sticky="w")

    Entry(tutorTel, width=35, textvariable=telTutor,
          font=("comic sans ms", 11)).grid(row=3, column=1, padx=3, pady=3, columnspan=2, sticky="w")

    # --------------radioButton tutorTel-----------------------------------------------
    Radiobutton(tutorTel, text="Nombre completo", variable=opcionRadio2, value=1, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2").grid(row=1, column=1, padx=3, pady=3, sticky="w")

    Radiobutton(tutorTel, text="ID", variable=opcionRadio2, value=2, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2", ).grid(row=1, column=2, padx=3, pady=3, sticky="w")

    # ----------------------BOTONES tutorTel------------------------------------------------------
    botonActualizar = Button(tutorTel, text="Actualizar", activebackground="#F50743",
                             command=lambda: telT())
    botonActualizar.config(font=("comic sans ms", 11), cursor="hand2", relief="sunken", bd=4, bg="grey75")
    botonActualizar.grid(row=4, column=1, padx=3, pady=3, sticky="w")



    # --------- FRAME foto-----------------------------------------------------
    # ----------label foto----------------------------------------------------------------
    Label(foto, text="FOTO DEL ALUMNO/A", bd=5, relief="groove", bg="white",
          font=("comic sans ms", 11)).grid(row=0, columnspan=4, padx=3, pady=10,)

    Label(foto, text="Introduzca aqui el identificador:", bd=5, relief="groove", bg="white",
          font=("comic sans ms", 11)).grid(row=2, column=0, padx=3, pady=3, sticky="e")
    Label(foto, text="Selecciona la opción de identificación:", bd=5, relief="groove", bg="white",
          font=("comic sans ms", 11)).grid(row=1, column=0, padx=3, pady=3, sticky="e")





    # ------------Entry foto------------------------------------------------
    Entry(foto, width=35, textvariable=textoEntryNomID,
          font=("comic sans ms", 11)).grid(row=2, column=1, padx=3, pady=3, columnspan=2, sticky="w")

    entryFoto = Entry(foto, width=35, textvariable=fotoAlum,)
    entryFoto.config(font=("comic sans ms", 11), state = "readonly")
    entryFoto.grid(row=3, column=1, padx=3, pady=3, columnspan=2, sticky="w")

    # --------------radioButton foto-----------------------------------------------
    Radiobutton(foto, text="Nombre completo", variable=opcionRadio2, value=1, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2").grid(row=1, column=1, padx=3, pady=3, sticky="w")

    Radiobutton(foto, text="ID", variable=opcionRadio2, value=2, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2", ).grid(row=1, column=2, padx=3, pady=3, sticky="w")

    # ----------------------BOTONES foto------------------------------------------------------
    botonActualizar = Button(foto, text="Actualizar", activebackground="#F50743",
                             command=lambda: fotoA())
    botonActualizar.config(font=("comic sans ms", 11), cursor="hand2", relief="sunken", bd=4, bg="grey75")
    botonActualizar.grid(row=4, column=1, padx=3, pady=3, sticky="w")

    carnet = PhotoImage(file="images/foto.png")
    botonImagen = Button(foto, image=carnet, compound="left", text="foto",
                         command=lambda: abrir())
    botonImagen.config(font=("comic sans ms", 9), cursor="hand2", relief="sunken", bd=3, bg="white")
    botonImagen.grid(row=3, column=0, padx=3, pady=3, sticky="ne")




    # --------- FRAME direccion-----------------------------------------------------
    # ----------label direccion----------------------------------------------------------------
    Label(direccion, text="LUGAR DE RESIDENCIA DEL ALUMNO/A", bd=5, relief="groove", bg="white",
          font=("comic sans ms", 11)).grid(row=0, columnspan=4, padx=3, pady=10, )

    Label(direccion, text="Introduzca aqui el identificador:", bd=5, relief="groove", bg="white",
          font=("comic sans ms", 11)).grid(row=2, column=0, padx=3, pady=3, sticky="e")
    Label(direccion, text="Selecciona la opción de identificación:", bd=5, relief="groove", bg="white",
          font=("comic sans ms", 11)).grid(row=1, column=0, padx=3, pady=3, sticky="e")

    Label(direccion, text="Residencia del alumno/a:", bd=5, relief="groove", bg="white",
          font=("comic sans ms", 11)).grid(row=3, column=0, padx=3, pady=3, sticky="e")

    # ------------Entry direccion------------------------------------------------
    Entry(direccion, width=35, textvariable=textoEntryNomID,
          font=("comic sans ms", 11)).grid(row=2, column=1, padx=3, pady=3, columnspan=2, sticky="w")

    Entry(direccion, width=35, textvariable=direccionAlum,
          font=("comic sans ms", 11)).grid(row=3, column=1, padx=3, pady=3, columnspan=2, sticky="w")

    # --------------radioButton direccion-----------------------------------------------
    Radiobutton(direccion, text="Nombre completo", variable=opcionRadio2, value=1, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2").grid(row=1, column=1, padx=3, pady=3, sticky="w")

    Radiobutton(direccion, text="ID", variable=opcionRadio2, value=2, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2", ).grid(row=1, column=2, padx=3, pady=3, sticky="w")

    # ----------------------BOTONES direccion------------------------------------------------------
    botonActualizar = Button(direccion, text="Actualizar", activebackground="#F50743",
                             command=lambda: direccion1())
    botonActualizar.config(font=("comic sans ms", 11), cursor="hand2", relief="sunken", bd=4, bg="grey75")
    botonActualizar.grid(row=4, column=1, padx=3, pady=3, sticky="w")



    # ----------------FRAME patologia-----------------------------------------------------------------
    # ----------------label patologia----------------------------------------------------------------
    Label(patologia, text="PATOLOGÍA GRAVE DE SALUD", bd=5, relief="groove", bg="white",
          font=("comic sans ms", 11)).grid(row=0, columnspan=4, padx=3, pady=10, )

    Label(patologia, text="Introduzca aqui el identificador:", bd=5, relief="groove", bg="white",
          font=("comic sans ms", 11)).grid(row=2, column=0, padx=3, pady=3, sticky="e")
    Label(patologia, text="Selecciona la opción de identificación:", bd=5, relief="groove", bg="white",
          font=("comic sans ms", 11)).grid(row=1, column=0, padx=3, pady=3, sticky="e")

    Label(patologia, text="Patología grave de salud :", bd=5, relief="groove", bg="white",
          font=("comic sans ms", 11)).grid(row=3, column=0, padx=3, pady=3, sticky="e")

    # ------------Entry patologia------------------------------------------------
    Entry(patologia, width=35, textvariable=textoEntryNomID,
          font=("comic sans ms", 11)).grid(row=2, column=1, padx=3, pady=3, columnspan=2, sticky="w")

    Entry(patologia, width=35, textvariable=patologiaAlumno,
          font=("comic sans ms", 11)).grid(row=3, column=1, padx=3, pady=3, columnspan=2, sticky="w")

    # --------------radioButton patologia-----------------------------------------------
    Radiobutton(patologia, text="Nombre completo", variable=opcionRadio2, value=1, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2").grid(row=1, column=1, padx=3, pady=3, sticky="w")

    Radiobutton(patologia, text="ID", variable=opcionRadio2, value=2, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2", ).grid(row=1, column=2, padx=3, pady=3, sticky="w")

    # ----------------------BOTONES patologia------------------------------------------------------
    botonActualizar = Button(patologia, text="Actualizar", activebackground="#F50743",
                             command=lambda: patologia1())
    botonActualizar.config(font=("comic sans ms", 11), cursor="hand2", relief="sunken", bd=4, bg="grey75")
    botonActualizar.grid(row=4, column=1, padx=3, pady=3, sticky="w")




    # ----------------FRAME estadoAlumno-----------------------------------------------------------------
    # ----------------label estadoAlumno----------------------------------------------------------------
    Label( estadoAlumno, text="ESTADO DEL ALUMNO/A", bd=5, relief="groove", bg="white",
          font=("comic sans ms", 11)).grid(row=0, columnspan=4, padx=3, pady=10, )

    Label(estadoAlumno, text="Introduzca aqui el identificador:", bd=5, relief="groove", bg="white",
          font=("comic sans ms", 11)).grid(row=2, column=0, padx=3, pady=3, sticky="e")
    Label(estadoAlumno, text="Selecciona la opción de identificación:", bd=5, relief="groove", bg="white",
          font=("comic sans ms", 11)).grid(row=1, column=0, padx=3, pady=3, sticky="e")

    Label(estadoAlumno, text="Estado del alumno/a:", bd=5, relief="groove", bg="white",
          font=("comic sans ms", 11)).grid(row=3, column=0, padx=3, pady=3, sticky="e")

    # ------------Entry estadoAlumno------------------------------------------------
    Entry(estadoAlumno, width=35, textvariable=textoEntryNomID,
          font=("comic sans ms", 11)).grid(row=2, column=1, padx=3, pady=3, columnspan=2, sticky="w")


    # --------------radioButton estadoAlumno-----------------------------------------------
    Radiobutton(estadoAlumno, text="Nombre completo", variable=opcionRadio2, value=1, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2").grid(row=1, column=1, padx=3, pady=3, sticky="w")

    Radiobutton(estadoAlumno, text="ID", variable=opcionRadio2, value=2, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2", ).grid(row=1, column=2, padx=3, pady=3, sticky="w")

    #---------------COMBOBOX ESTADO DEL ALUMNO----------------------------------------------------
    comboEstatus = Combobox(estadoAlumno, width=20)
    comboEstatus['values'] = ("MATRICULADO/A", "TRASALADADO/A")
    comboEstatus.current(1)
    comboEstatus.grid(row=3, column=1, padx=3, pady=3, columnspan=2, sticky="w")

    # ----------------------BOTONES estadoAlumno------------------------------------------------------
    botonActualizar = Button(estadoAlumno, text="Actualizar", activebackground="#F50743",
                             command=lambda: estadoAlumno1())
    botonActualizar.config(font=("comic sans ms", 11), cursor="hand2", relief="sunken", bd=4, bg="grey75")
    botonActualizar.grid(row=4, column=1, padx=3, pady=3, sticky="w")








    #------------funciones de actualizacion de datos------------------------------------------------
    def abrir():
        """
        esta funcion permite selecionar una foto en explorador de archivo
        y poner la direccion de la foto en el cuadro de texto de actualizacion
        :return:
        """
        archivo = filedialog.askopenfilename(title="ABRIR")
        if archivo:
            fotoAlum.set(archivo)
        else:
            fotoAlum.set("images/logoTsei.png")



    def ActualNomTutor(a,b):
        """
        esta funcion permite actualirar el nombre del tutor en la base de datos
        :param a: es el valor actualizar
        :param b: es el valor que representa el registro
        :return:
        """
        connexion = sqlite3.connect(nameBD.nomBD())
        cursor = connexion.cursor()
        cursor.execute(f"update alumno set tutor = '{a}' where  nombre_y_apellidos = '{b}' ")
        connexion.commit()

        connexion.close()
        textoEntryNomID.set("")
        nombreTutor.set("")



    def ActualNomTutor1(a, b):
            """
            esta funcion permite actualirar el nombre del tutor en la base de datos
            :param a: es el valor actualizar
            :param b: es el valor que representa el registro
            :return:
            """
            connexion = sqlite3.connect(nameBD.nomBD())
            cursor = connexion.cursor()
            cursor.execute(f"update alumno set tutor = '{a}' where  id = '{b}' ")
            connexion.commit()

            connexion.close()
            textoEntryNomID.set("")

            nombreTutor.set("")









    def ActualTelTutor(a,b):
        """
        esta funcion permite actualirar el telefono del tutor en la base de datos
        :param a: es el valor actualizar
        :param b: es el valor que representa el registro
        :return:
        """
        connexion = sqlite3.connect(nameBD.nomBD())
        cursor = connexion.cursor()
        cursor.execute(f"update alumno set tel_tutor = '{a}' where  nombre_y_apellidos = '{b}' ")
        connexion.commit()

        connexion.close()
        textoEntryNomID.set("")
        telTutor.set("")



    def ActualTelTutor1(a, b):
            """
            esta funcion permite actualirar el telefono del tutor en la base de datos
            :param a: es el valor actualizar
            :param b: es el valor que representa el registro
            :return:
            """
            connexion = sqlite3.connect(nameBD.nomBD())
            cursor = connexion.cursor()
            cursor.execute(f"update alumno set tel_tutor = '{a}' where  id = '{b}' ")
            connexion.commit()

            connexion.close()
            textoEntryNomID.set("")
            telTutor.set("")



    def ActualPatologia(a,b):
        """
        esta funcion permite actualirar la patologia en la base de datos
        :param a: es el valor actualizar
        :param b: es el valor que representa el registro
        :return:
        """
        connexion = sqlite3.connect(nameBD.nomBD())
        cursor = connexion.cursor()
        cursor.execute(f"update alumno set patologia = '{a}' where nombre_y_apellidos = '{b}' ")
        connexion.commit()

        connexion.close()
        textoEntryNomID.set("")
        patologiaAlumno.set("")



    def ActualPatologia1(a, b):
            """
            esta funcion permite actualirar la patologia en la base de datos
            :param a: es el valor actualizar
            :param b: es el valor que representa el registro
            :return:
            """
            connexion = sqlite3.connect(nameBD.nomBD())
            cursor = connexion.cursor()
            cursor.execute(f"update alumno set patologia = '{a}' where id = '{b}' ")
            connexion.commit()

            connexion.close()
            textoEntryNomID.set("")
            patologiaAlumno.set("")



    def ActualCurso(a,b):
        """
        esta funcion permite actualirar curso en la base de datos e insertar la informacion del alumno al curso siguiente
        y eeliminar los antecedes disciplinarios del alumno en cuestion
        :param a: es el valor actualizar
        :param b: es el valor que representa el registro
        :return:
        """
        try:
            connexion = sqlite3.connect(nameBD.nomBD())
            cursor = connexion.cursor()

            #resultado = messagebox.askyesno('DULA 1.0', '¿EL ALUMNO/A VA AL CURSO SIGUIENTE?')
            if condicionAlumn.get() == 1:


                cursor.execute(f"update alumno set curso = '{a}' where nombre_y_apellidos = '{b}' ")
                connexion.commit()

                cursor.execute("select * from disciplina")
                stock = cursor.fetchall()
                i = 0
                while i < len(stock):

                    if i == len(stock) + 1:
                        pass
                        break

                    inforegistro1 = stock[i]
                    i += 1
                    if b == inforegistro1[0].upper():  # parametro l del metodo upper()
                        cursor.execute(f"update disciplina set curso = '{a}' where nombre_y_apellidos = '{b}' ")
                        connexion.commit()

                        cursor.execute(f"update disciplina set numero_de_faltas = 0 where nombre_y_apellidos = '{b}' ")
                        connexion.commit()

                        cursor.execute(f"update disciplina set descripcion = '' where nombre_y_apellidos = '{b}' ")
                        connexion.commit()


                if a.upper() == "1°ESBA":
                    pass

                elif a.upper() == "2°ESBA":
                    cursor.execute(f"select id, nombre_y_apellidos from alumno where nombre_y_apellidos = '{b}'")
                    fecha = cursor.fetchall()
                    nombre = fecha[0][1]
                    id = fecha[0][0]
                    fecha4 = comboFecha.get()

                    cursor.execute(
                        f"insert into segundo_esba_uno values ('{id}', '{nombre}', '{fecha4}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                    cursor.execute(
                        f"insert into segundo_esba_dos values ('{id}', '{nombre}', '{fecha4}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                    cursor.execute(
                        f"insert into segundo_esba_tres values ('{id}', '{nombre}', '{fecha4}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                    cursor.execute(
                        f"insert into segundo_esba_junio values ('{id}', '{nombre}', '{fecha4}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                    cursor.execute(
                        f"insert into segundo_esba_septiembre values ('{id}', '{nombre}', '{fecha4}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()


                elif a.upper() == "3°ESBA":
                    cursor.execute(f"select id, nombre_y_apellidos from alumno where nombre_y_apellidos = '{b}'")
                    fecha = cursor.fetchall()
                    nombre = fecha[0][1]
                    id = fecha[0][0]
                    fecha4 = comboFecha.get()

                    cursor.execute(
                        f"insert into tercero_esba_uno values ('{id}', '{nombre}', '{fecha4}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                    cursor.execute(
                        f"insert into tercero_esba_dos values ('{id}', '{nombre}', '{fecha4}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                    cursor.execute(
                        f"insert into tercero_esba_tres values ('{id}', '{nombre}', '{fecha4}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                    cursor.execute(
                        f"insert into tercero_esba_junio values ('{id}', '{nombre}', '{fecha4}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                    cursor.execute(
                        f"insert into tercero_esba_septiembre values ('{id}', '{nombre}', '{fecha4}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()


                elif a.upper() == "4°ESBA":
                    cursor.execute(f"select id, nombre_y_apellidos from alumno where nombre_y_apellidos = '{b}'")
                    fecha = cursor.fetchall()
                    nombre = fecha[0][1]
                    id = fecha[0][0]
                    fecha4 = comboFecha.get()

                    cursor.execute(
                        f"insert into cuarto_esba_uno values ('{id}', '{nombre}', '{fecha4}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                    cursor.execute(
                        f"insert into cuarto_esba_dos values ('{id}', '{nombre}', '{fecha4}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                    cursor.execute(
                        f"insert into cuarto_esba_tres values ('{id}', '{nombre}', '{fecha4}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                    cursor.execute(
                        f"insert into cuarto_esba_junio values ('{id}', '{nombre}', '{fecha4}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                    cursor.execute(
                        f"insert into cuarto_esba_septiembre values ('{id}', '{nombre}', '{fecha4}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                elif a.upper() == "1°BACH":
                    cursor.execute(f"select id, nombre_y_apellidos from alumno where nombre_y_apellidos = '{b}'")
                    fecha = cursor.fetchall()
                    nombre = fecha[0][1]
                    id = fecha[0][0]
                    fecha4 = comboFecha.get()

                    cursor.execute(
                        f"insert into primero_bach_uno values ('{id}', '{nombre}', '{fecha4}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                    cursor.execute(
                        f"insert into primero_bach_dos values ('{id}', '{nombre}', '{fecha4}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                    cursor.execute(
                        f"insert into primero_bach_tres values ('{id}', '{nombre}', '{fecha4}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                    cursor.execute(
                        f"insert into primero_bach_junio values ('{id}', '{nombre}', '{fecha4}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                    cursor.execute(
                        f"insert into primero_bach_septiembre values ('{id}', '{nombre}', '{fecha4}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()


                elif a.upper() == "2°BACH":
                    cursor.execute(f"select id, nombre_y_apellidos from alumno where nombre_y_apellidos = '{b}'")
                    fecha = cursor.fetchall()
                    nombre = fecha[0][1]
                    id = fecha[0][0]
                    fecha4 = comboFecha.get()

                    cursor.execute(
                        f"insert into segundo_bach_uno values ('{id}', '{nombre}', '{fecha4}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                    cursor.execute(
                        f"insert into segundo_bach_dos values ('{id}', '{nombre}', '{fecha4}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                    cursor.execute(
                        f"insert into segundo_bach_tres values ('{id}', '{nombre}', '{fecha4}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                    cursor.execute(
                        f"insert into segundo_bach_junio values ('{id}', '{nombre}', '{fecha4}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                    cursor.execute(
                        f"insert into segundo_bach_septiembre values ('{id}', '{nombre}', '{fecha4}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                else:
                    pass




            elif condicionAlumn.get() == 2:

                cursor.execute("select * from disciplina")
                stock = cursor.fetchall()
                i = 0
                while i < len(stock):

                    if i == len(stock) + 1:
                        pass
                        break

                    inforegistro1 = stock[i]
                    i += 1
                    if b == inforegistro1[0].upper():  # parametro l del metodo upper()

                        cursor.execute(f"update disciplina set numero_de_faltas = 0 where nombre_y_apellidos = '{b}' ")
                        connexion.commit()

                        cursor.execute(f"update disciplina set descripcion = '' where nombre_y_apellidos = '{b}' ")
                        connexion.commit()

                        cursor.execute(f"update disciplina set curso = '{inforegistro1[1]}' where nombre_y_apellidos = '{b}' ")
                        connexion.commit()


                if a.upper() == "1°ESBA":
                    cursor.execute(f"select id, nombre_y_apellidos from alumno where nombre_y_apellidos = '{b}'")
                    fecha = cursor.fetchall()
                    nombre = fecha[0][1]
                    id = fecha[0][0]
                    fecha4 = comboFecha.get()

                    cursor.execute(f"delete from primero_esba_uno  where nombre = '{b}' ")
                    connexion.commit()

                    cursor.execute(
                        f"insert into primero_esba_uno values ('{id}', '{nombre}', '{fecha4}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()



                    cursor.execute(f"delete from primero_esba_dos  where nombre = '{b}' ")
                    connexion.commit()

                    cursor.execute(
                        f"insert into primero_esba_dos values ('{id}', '{nombre}', '{fecha4}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()



                    cursor.execute(f"delete from primero_esba_tres  where nombre = '{b}' ")
                    connexion.commit()

                    cursor.execute(f"insert into primero_esba_tres values ('{id}', '{nombre}', '{fecha4}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()


                    cursor.execute(f"delete from primero_esba_junio  where nombre = '{b}' ")
                    connexion.commit()

                    cursor.execute(f"insert into primero_esba_junio values ('{id}', '{nombre}', '{fecha4}',"
                                   f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()


                    cursor.execute(f"delete from primero_esba_septiembre  where nombre = '{b}' ")
                    connexion.commit()

                    cursor.execute(f"insert into primero_esba_septiembre values ('{id}', '{nombre}', '{fecha4}',"
                                   f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()


                elif a.upper() == "2°ESBA":
                    cursor.execute(f"select id, nombre_y_apellidos from alumno where nombre_y_apellidos = '{b}'")
                    fecha = cursor.fetchall()
                    nombre = fecha[0][1]
                    id = fecha[0][0]
                    fecha4 = comboFecha.get()

                    cursor.execute(f"delete from segundo_esba_uno  where nombre = '{b}' ")
                    connexion.commit()
                    cursor.execute(f"insert into segundo_esba_uno values ('{id}', '{nombre}', '{fecha4}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                    cursor.execute(f"delete from segundo_esba_dos  where nombre = '{b}' ")
                    connexion.commit()
                    cursor.execute(f"insert into segundo_esba_dos values ('{id}', '{nombre}', '{fecha4}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                    cursor.execute(f"delete from segundo_esba_tres  where nombre = '{b}' ")
                    connexion.commit()
                    cursor.execute(f"insert into segundo_esba_tres values ('{id}', '{nombre}', '{fecha4}',"
                                   f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                    cursor.execute(f"delete from segundo_esba_junio  where nombre = '{b}' ")
                    connexion.commit()
                    cursor.execute(f"insert into segundo_esba_junio values ('{id}', '{nombre}', '{fecha4}',"
                                   f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                    cursor.execute(f"delete from segundo_esba_septiembre  where nombre = '{b}' ")
                    connexion.commit()
                    cursor.execute(f"insert into segundo_esba_septiembre values ('{id}', '{nombre}', '{fecha4}',"
                                   f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()


                elif a.upper() == "3°ESBA":
                    cursor.execute(f"select id, nombre_y_apellidos from alumno where nombre_y_apellidos = '{b}'")
                    fecha = cursor.fetchall()
                    nombre = fecha[0][1]
                    id = fecha[0][0]
                    fecha4 = comboFecha.get()

                    cursor.execute(f"delete from tercero_esba_uno  where nombre = '{b}' ")
                    connexion.commit()
                    cursor.execute(f"insert into tercero_esba_uno values ('{id}', '{nombre}', '{fecha4}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                    cursor.execute(f"delete from tercero_esba_dos  where nombre = '{b}' ")
                    connexion.commit()
                    cursor.execute(f"insert into tercero_esba_dos values ('{id}', '{nombre}', '{fecha4}',"
                                   f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                    cursor.execute(f"delete from tercero_esba_tres  where nombre = '{b}' ")
                    connexion.commit()
                    cursor.execute(f"insert into tercero_esba_tres values ('{id}', '{nombre}', '{fecha4}',"
                                   f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                    cursor.execute(f"delete from tercero_esba_septiembre  where nombre = '{b}' ")
                    connexion.commit()
                    cursor.execute(f"insert into tercero_esba_septiembre values ('{id}', '{nombre}', '{fecha4}',"
                                   f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                    cursor.execute(f"delete from tercero_esba_junio  where nombre = '{b}' ")
                    connexion.commit()
                    cursor.execute(f"insert into tercero_esba_junio values ('{id}', '{nombre}', '{fecha4}',"
                                   f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()



                elif a.upper() == "4°ESBA":
                    cursor.execute(f"select id, nombre_y_apellidos from alumno where nombre_y_apellidos = '{b}'")
                    fecha = cursor.fetchall()
                    nombre = fecha[0][1]
                    id = fecha[0][0]
                    fecha4 = comboFecha.get()

                    cursor.execute(f"delete from cuarto_esba_uno  where nombre = '{b}' ")
                    connexion.commit()
                    cursor.execute(f"insert into cuarto_esba_uno values ('{id}', '{nombre}', '{fecha4}',"
                                   f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                    cursor.execute(f"delete from cuarto_esba_dos  where nombre = '{b}' ")
                    connexion.commit()
                    cursor.execute(f"insert into cuarto_esba_dos values ('{id}', '{nombre}', '{fecha4}',"
                                   f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                    cursor.execute(f"delete from cuarto_esba_tres  where nombre = '{b}' ")
                    connexion.commit()
                    cursor.execute(f"insert into cuarto_esba_tres values ('{id}', '{nombre}', '{fecha4}',"
                                   f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                    cursor.execute(f"delete from cuarto_esba_septiembre  where nombre = '{b}' ")
                    connexion.commit()
                    cursor.execute(f"insert into cuarto_esba_septiembre values ('{id}', '{nombre}', '{fecha4}',"
                                   f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                    cursor.execute(f"delete from cuarto_esba_junio  where nombre = '{b}' ")
                    connexion.commit()
                    cursor.execute(f"insert into cuarto_esba_junio values ('{id}', '{nombre}', '{fecha4}',"
                                   f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()



                elif a.upper() == "1°BACH":
                    cursor.execute(f"select id, nombre_y_apellidos from alumno where nombre_y_apellidos = '{b}'")
                    fecha = cursor.fetchall()
                    nombre = fecha[0][1]
                    id = fecha[0][0]
                    fecha4 = comboFecha.get()

                    cursor.execute(f"delete from primero_bach_uno  where nombre = '{b}' ")
                    connexion.commit()
                    cursor.execute(f"insert into primero_bach_uno values ('{id}', '{nombre}', '{fecha4}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                    cursor.execute(f"delete from primero_bach_dos  where nombre = '{b}' ")
                    connexion.commit()
                    cursor.execute(f"insert into primero_bach_dos values ('{id}', '{nombre}', '{fecha4}',"
                                   f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                    cursor.execute(f"delete from primero_bach_tres  where nombre = '{b}' ")
                    connexion.commit()
                    cursor.execute(f"insert into primero_bach_tres values ('{id}', '{nombre}', '{fecha4}',"
                                   f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                    cursor.execute(f"delete from primero_bach_junio  where nombre = '{b}' ")
                    connexion.commit()
                    cursor.execute(f"insert into primero_bach_junio values ('{id}', '{nombre}', '{fecha4}',"
                                   f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                    cursor.execute(f"delete from primero_bach_septiembre  where nombre = '{b}' ")
                    connexion.commit()
                    cursor.execute(f"insert into primero_bach_septiembre values ('{id}', '{nombre}', '{fecha4}',"
                                   f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()



                elif a.upper() == "2°BACH":
                    cursor.execute(f"select id, nombre_y_apellidos from alumno where nombre_y_apellidos = '{b}'")
                    fecha = cursor.fetchall()
                    nombre = fecha[0][1]
                    id = fecha[0][0]
                    fecha4 = comboFecha.get()

                    cursor.execute(f"delete from segundo_bach_uno  where nombre = '{b}' ")
                    connexion.commit()
                    cursor.execute(f"insert into segundo_bach_uno values ('{id}', '{nombre}', '{fecha4}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                    cursor.execute(f"delete from segundo_bach_dos  where nombre = '{b}' ")
                    connexion.commit()
                    cursor.execute(f"insert into segundo_bach_dos values ('{id}', '{nombre}', '{fecha4}',"
                                   f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                    cursor.execute(f"delete from segundo_bach_tres  where nombre = '{b}' ")
                    connexion.commit()
                    cursor.execute(f"insert into segundo_bach_tres values ('{id}', '{nombre}', '{fecha4}',"
                                   f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                    cursor.execute(f"delete from segundo_bach_junio  where nombre = '{b}' ")
                    connexion.commit()
                    cursor.execute(f"insert into segundo_bach_junio values ('{id}', '{nombre}', '{fecha4}',"
                                   f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                    cursor.execute(f"delete from segundo_bach_septiembre  where nombre = '{b}' ")
                    connexion.commit()
                    cursor.execute(f"insert into segundo_bach_septiembre values ('{id}', '{nombre}', '{fecha4}',"
                                   f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                else:
                    pass

            else:
                pass






            connexion.close()
            textoEntryNomID.set("")

        except IndexError:
            pass




    def ActualCurso1(a, b):
        """
        esta funcion permite actualirar curso en la base de datos atraves del id del alumno
        permite tambien insertar poner el nombre del alumno a la tabla del curso siguiente
        asi aliminar los antecedentes disciplinarios

        :param a: es el valor actualizar
        :param b: es el valor que representa el registro
        :return:
        """
        try:

            connexion = sqlite3.connect(nameBD.nomBD())
            cursor = connexion.cursor()

            #resultado = messagebox.askyesno('DULA 1.0', '¿EL ALUMNO/A VA AL CURSO SIGUIENTE?')
            if condicionAlumn.get() == 1:

                cursor.execute(f"update alumno set curso = '{a}' where id = '{b}' ")
                connexion.commit()

                cursor.execute("select * from disciplina")
                stock = cursor.fetchall()
                i = 0
                while i < len(stock):

                    if i == len(stock) + 1:
                        pass
                        break

                    inforegistro1 = stock[i]
                    i += 1
                    if int(b) == inforegistro1[4]:  # parametro l del metodo upper()
                        cursor.execute(f"update disciplina set curso = '{a}' where id = '{b}' ")
                        connexion.commit()

                        cursor.execute(f"update disciplina set numero_de_faltas = 0 where id = '{b}' ")
                        connexion.commit()

                        cursor.execute(f"update disciplina set descripcion = '' where id = '{b}' ")
                        connexion.commit()

                if a.upper() == "1°ESBA":
                    pass

                elif a.upper() == "2°ESBA":
                        cursor.execute(f"select id, nombre_y_apellidos from alumno where id = '{b}'")
                        fecha = cursor.fetchall()
                        nombre = fecha[0][1]
                        id = fecha[0][0]
                        fecha4 = comboFecha.get()

                        cursor.execute(
                            f"insert into segundo_esba_uno values ('{id}', '{nombre}', '{fecha4}',"
                            f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                        connexion.commit()

                        cursor.execute(
                            f"insert into segundo_esba_dos values ('{id}', '{nombre}', '{fecha4}',"
                            f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                        connexion.commit()

                        cursor.execute(
                            f"insert into segundo_esba_tres values ('{id}', '{nombre}', '{fecha4}',"
                            f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                        connexion.commit()

                        cursor.execute(
                            f"insert into segundo_esba_junio values ('{id}', '{nombre}', '{fecha4}',"
                            f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                        connexion.commit()

                        cursor.execute(
                            f"insert into segundo_esba_septiembre values ('{id}', '{nombre}', '{fecha4}',"
                            f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                        connexion.commit()


                elif a.upper() == "3°ESBA":
                        cursor.execute(f"select id, nombre_y_apellidos from alumno where id = '{b}'")
                        fecha = cursor.fetchall()
                        nombre = fecha[0][1]
                        id = fecha[0][0]
                        fecha4 = comboFecha.get()

                        cursor.execute(
                            f"insert into tercero_esba_uno values ('{id}', '{nombre}', '{fecha4}',"
                            f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                        connexion.commit()

                        cursor.execute(
                            f"insert into tercero_esba_dos values ('{id}', '{nombre}', '{fecha4}',"
                            f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                        connexion.commit()

                        cursor.execute(
                            f"insert into tercero_esba_tres values ('{id}', '{nombre}', '{fecha4}',"
                            f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                        connexion.commit()

                        cursor.execute(
                            f"insert into tercero_esba_junio values ('{id}', '{nombre}', '{fecha4}',"
                            f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                        connexion.commit()

                        cursor.execute(
                            f"insert into tercero_esba_septiembre values ('{id}', '{nombre}', '{fecha4}',"
                            f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                        connexion.commit()


                elif a.upper() == "4°ESBA":
                        cursor.execute(f"select id, nombre_y_apellidos from alumno where id = '{b}'")
                        fecha = cursor.fetchall()
                        nombre = fecha[0][1]
                        id = fecha[0][0]
                        fecha4 = comboFecha.get()
                        cursor.execute(
                            f"insert into cuarto_esba_uno values ('{id}', '{nombre}', '{fecha4}',"
                            f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                        connexion.commit()

                        cursor.execute(
                            f"insert into cuarto_esba_dos values ('{id}', '{nombre}', '{fecha4}',"
                            f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                        connexion.commit()

                        cursor.execute(
                            f"insert into cuarto_esba_tres values ('{id}', '{nombre}', '{fecha4}',"
                            f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                        connexion.commit()

                        cursor.execute(
                            f"insert into cuarto_esba_junio values ('{id}', '{nombre}', '{fecha4}',"
                            f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                        connexion.commit()

                        cursor.execute(
                            f"insert into cuarto_esba_septiembre values ('{id}', '{nombre}', '{fecha4}',"
                            f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                        connexion.commit()

                elif a.upper() == "1°BACH":
                        cursor.execute(f"select id, nombre_y_apellidos from alumno where id = '{b}'")
                        fecha = cursor.fetchall()
                        nombre = fecha[0][1]
                        id = fecha[0][0]
                        fecha4 = comboFecha.get()

                        cursor.execute(
                            f"insert into primero_bach_uno values ('{id}', '{nombre}', '{fecha4}',"
                            f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                        connexion.commit()

                        cursor.execute(
                            f"insert into primero_bach_dos values ('{id}', '{nombre}', '{fecha4}',"
                            f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                        connexion.commit()

                        cursor.execute(
                            f"insert into primero_bach_tres values ('{id}', '{nombre}', '{fecha4}',"
                            f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                        connexion.commit()

                        cursor.execute(
                            f"insert into primero_bach_junio values ('{id}', '{nombre}', '{fecha4}',"
                            f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                        connexion.commit()

                        cursor.execute(
                            f"insert into primero_bach_septiembre values ('{id}', '{nombre}', '{fecha4}',"
                            f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                        connexion.commit()


                elif a.upper() == "2°BACH":
                        cursor.execute(f"select id, nombre_y_apellidos from alumno where id = '{b}'")
                        fecha = cursor.fetchall()
                        nombre = fecha[0][1]
                        id = fecha[0][0]
                        fecha4 = comboFecha.get()

                        cursor.execute(
                            f"insert into segundo_bach_uno values ('{id}', '{nombre}', '{fecha4}',"
                            f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                        connexion.commit()

                        cursor.execute(
                            f"insert into segundo_bach_dos values ('{id}', '{nombre}', '{fecha4}',"
                            f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                        connexion.commit()

                        cursor.execute(
                            f"insert into segundo_bach_tres values ('{id}', '{nombre}', '{fecha4}',"
                            f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                        connexion.commit()

                        cursor.execute(
                            f"insert into segundo_bach_junio values ('{id}', '{nombre}', '{fecha4}',"
                            f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                        connexion.commit()

                        cursor.execute(
                            f"insert into segundo_bach_septiembre values ('{id}', '{nombre}', '{fecha4}',"
                            f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                        connexion.commit()

                else:
                    pass



            elif condicionAlumn.get() == 2:

                cursor.execute(f"update alumno set curso = '{a}' where nombre_y_apellidos = '{b}' ")
                connexion.commit()

                cursor.execute("select * from disciplina")
                stock = cursor.fetchall()
                i = 0
                while i < len(stock):

                    if i == len(stock) + 1:
                        pass
                        break

                    inforegistro1 = stock[i]
                    i += 1
                    if b == inforegistro1[0].upper():  # parametro l del metodo upper()

                        cursor.execute(f"update disciplina set numero_de_faltas = 0 where id = '{b}' ")
                        connexion.commit()

                        cursor.execute(f"update disciplina set descripcion = '' where id = '{b}' ")
                        connexion.commit()

                        cursor.execute(f"update disciplina set curso = '{inforegistro1[1]}' where id = '{b}' ")
                        connexion.commit()


                if a.upper() == "1°ESBA":
                    cursor.execute(f"select id, nombre_y_apellidos from alumno where id = '{b}'")
                    fecha = cursor.fetchall()
                    nombre = fecha[0][1]
                    id = fecha[0][0]
                    fecha4 = comboFecha.get()

                    cursor.execute(f"delete from primero_esba_uno  where id = '{b}' ")
                    connexion.commit()

                    cursor.execute(
                        f"insert into primero_esba_uno values ('{id}', '{nombre}', '{fecha4}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                    cursor.execute(f"delete from primero_esba_dos  where id = '{b}' ")
                    connexion.commit()

                    cursor.execute(
                        f"insert into primero_esba_dos values ('{id}', '{nombre}', '{fecha4}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                    cursor.execute(f"delete from primero_esba_tres  where id = '{b}' ")
                    connexion.commit()

                    cursor.execute(f"insert into primero_esba_tres values ('{id}', '{nombre}', '{fecha4}',"
                                   f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                    cursor.execute(f"delete from primero_esba_junio  where id = '{b}' ")
                    connexion.commit()

                    cursor.execute(f"insert into primero_esba_junio values ('{id}', '{nombre}', '{fecha4}',"
                                   f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                    cursor.execute(f"delete from primero_esba_septiembre  where id = '{b}' ")
                    connexion.commit()

                    cursor.execute(f"insert into primero_esba_septiembre values ('{id}', '{nombre}', '{fecha4}',"
                                   f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()



                elif a.upper() == "2°ESBA":
                    cursor.execute(f"select id, nombre_y_apellidos from alumno where id = '{b}'")
                    fecha = cursor.fetchall()
                    nombre = fecha[0][1]
                    id = fecha[0][0]
                    fecha4 = comboFecha.get()

                    cursor.execute(f"delete from segundo_esba_uno  where id = '{b}' ")
                    connexion.commit()
                    cursor.execute(f"insert into segundo_esba_uno values ('{id}', '{nombre}', '{fecha4}',"
                                   f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                    cursor.execute(f"delete from segundo_esba_dos  where id = '{b}' ")
                    connexion.commit()
                    cursor.execute(f"insert into segundo_esba_dos values ('{id}', '{nombre}', '{fecha4}',"
                                   f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                    cursor.execute(f"delete from segundo_esba_tres  where id = '{b}' ")
                    connexion.commit()
                    cursor.execute(f"insert into segundo_esba_tres values ('{id}', '{nombre}', '{fecha4}',"
                                   f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                    cursor.execute(f"delete from segundo_esba_junio  where id = '{b}' ")
                    connexion.commit()
                    cursor.execute(f"insert into segundo_esba_junio values ('{id}', '{nombre}', '{fecha4}',"
                                   f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                    cursor.execute(f"delete from segundo_esba_septiembre  where id = '{b}' ")
                    connexion.commit()
                    cursor.execute(f"insert into segundo_esba_septiembre values ('{id}', '{nombre}', '{fecha4}',"
                                   f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    connexion.commit()

                elif a.upper() == "3°ESBA":
                        cursor.execute(f"select id, nombre_y_apellidos from alumno where id = '{b}'")
                        fecha = cursor.fetchall()
                        nombre = fecha[0][1]
                        id = fecha[0][0]
                        fecha4 = comboFecha.get()

                        cursor.execute(f"delete from tercero_esba_uno  where id = '{b}' ")
                        connexion.commit()
                        cursor.execute(f"insert into tercero_esba_uno values ('{id}', '{nombre}', '{fecha4}',"
                                       f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                        connexion.commit()

                        cursor.execute(f"delete from tercero_esba_dos  where id = '{b}' ")
                        connexion.commit()
                        cursor.execute(f"insert into tercero_esba_dos values ('{id}', '{nombre}', '{fecha4}',"
                                       f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                        connexion.commit()

                        cursor.execute(f"delete from tercero_esba_tres  where id = '{b}' ")
                        connexion.commit()
                        cursor.execute(f"insert into tercero_esba_tres values ('{id}', '{nombre}', '{fecha4}',"
                                       f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                        connexion.commit()

                        cursor.execute(f"delete from tercero_esba_septiembre  where id = '{b}' ")
                        connexion.commit()
                        cursor.execute(f"insert into tercero_esba_septiembre values ('{id}', '{nombre}', '{fecha4}',"
                                       f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                        connexion.commit()

                        cursor.execute(f"delete from tercero_esba_junio  where id = '{b}' ")
                        connexion.commit()
                        cursor.execute(f"insert into tercero_esba_junio values ('{id}', '{nombre}', '{fecha4}',"
                                       f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                        connexion.commit()



                elif a.upper() == "4°ESBA":
                        cursor.execute(f"select id, nombre_y_apellidos from alumno where id = '{b}'")
                        fecha = cursor.fetchall()
                        nombre = fecha[0][1]
                        id = fecha[0][0]
                        fecha4 = comboFecha.get()

                        cursor.execute(f"delete from cuarto_esba_uno  where id = '{b}' ")
                        connexion.commit()
                        cursor.execute(f"insert into cuarto_esba_uno values ('{id}', '{nombre}', '{fecha4}',"
                                       f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                        connexion.commit()

                        cursor.execute(f"delete from cuarto_esba_dos  where id = '{b}' ")
                        connexion.commit()
                        cursor.execute(f"insert into cuarto_esba_dos values ('{id}', '{nombre}', '{fecha4}',"
                                       f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                        connexion.commit()

                        cursor.execute(f"delete from cuarto_esba_tres  where id = '{b}' ")
                        connexion.commit()
                        cursor.execute(f"insert into cuarto_esba_tres values ('{id}', '{nombre}', '{fecha4}',"
                                       f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                        connexion.commit()

                        cursor.execute(f"delete from cuarto_esba_septiembre  where id = '{b}' ")
                        connexion.commit()
                        cursor.execute(f"insert into cuarto_esba_septiembre values ('{id}', '{nombre}', '{fecha4}',"
                                       f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                        connexion.commit()

                        cursor.execute(f"delete from cuarto_esba_junio  where id = '{b}' ")
                        connexion.commit()
                        cursor.execute(f"insert into cuarto_esba_junio values ('{id}', '{nombre}', '{fecha4}',"
                                       f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                        connexion.commit()



                elif a.upper() == "1°BACH":
                        cursor.execute(f"select id, nombre_y_apellidos from alumno where id = '{b}'")
                        fecha = cursor.fetchall()
                        nombre = fecha[0][1]
                        id = fecha[0][0]
                        fecha4 = comboFecha.get()

                        cursor.execute(f"delete from primero_bach_uno  where id = '{b}' ")
                        connexion.commit()
                        cursor.execute(f"insert into primero_bach_uno values ('{id}', '{nombre}', '{fecha4}',"
                                       f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                        connexion.commit()

                        cursor.execute(f"delete from primero_bach_dos  where id = '{b}' ")
                        connexion.commit()
                        cursor.execute(f"insert into primero_bach_dos values ('{id}', '{nombre}', '{fecha4}',"
                                       f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                        connexion.commit()

                        cursor.execute(f"delete from primero_bach_tres  where id = '{b}' ")
                        connexion.commit()
                        cursor.execute(f"insert into primero_bach_tres values ('{id}', '{nombre}', '{fecha4}',"
                                       f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                        connexion.commit()

                        cursor.execute(f"delete from primero_bach_junio  where id = '{b}' ")
                        connexion.commit()
                        cursor.execute(f"insert into primero_bach_junio values ('{id}', '{nombre}', '{fecha4}',"
                                       f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                        connexion.commit()

                        cursor.execute(f"delete from primero_bach_septiembre  where id = '{b}' ")
                        connexion.commit()
                        cursor.execute(f"insert into primero_bach_septiembre values ('{id}', '{nombre}', '{fecha4}',"
                                       f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                        connexion.commit()



                elif a.upper() == "2°BACH":
                        cursor.execute(f"select id, nombre_y_apellidos from alumno where id = '{b}'")
                        fecha = cursor.fetchall()
                        nombre = fecha[0][1]
                        id = fecha[0][0]
                        fecha4 = comboFecha.get()

                        cursor.execute(f"delete from segundo_bach_uno  where id = '{b}' ")
                        connexion.commit()
                        cursor.execute(f"insert into segundo_bach_uno values ('{id}', '{nombre}', '{fecha4}',"
                                       f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                        connexion.commit()

                        cursor.execute(f"delete from segundo_bach_dos  where id = '{b}' ")
                        connexion.commit()
                        cursor.execute(f"insert into segundo_bach_dos values ('{id}', '{nombre}', '{fecha4}',"
                                       f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                        connexion.commit()

                        cursor.execute(f"delete from segundo_bach_tres  where id = '{b}' ")
                        connexion.commit()
                        cursor.execute(f"insert into segundo_bach_tres values ('{id}', '{nombre}', '{fecha4}',"
                                       f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                        connexion.commit()

                        cursor.execute(f"delete from segundo_bach_junio  where id = '{b}' ")
                        connexion.commit()
                        cursor.execute(f"insert into segundo_bach_junio values ('{id}', '{nombre}', '{fecha4}',"
                                       f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                        connexion.commit()

                        cursor.execute(f"delete from segundo_bach_septiembre  where id = '{b}' ")
                        connexion.commit()
                        cursor.execute(f"insert into segundo_bach_septiembre values ('{id}', '{nombre}', '{fecha4}',"
                                       f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                        connexion.commit()

                else:
                    pass
            else:
                pass



            connexion.close()
            textoEntryNomID.set("")

        except IndexError:
            pass



    def ActualResidencia(a,b):
        """
        esta funcion permite actualirar residencia en la base de datos
        :param a: es el valor actualizar
        :param b: es el valor que representa el registro
        :return:
        """
        connexion = sqlite3.connect(nameBD.nomBD())
        cursor = connexion.cursor()
        cursor.execute(f"update alumno set residencia = '{a}' where nombre_y_apellidos = '{b}' ")
        connexion.commit()

        connexion.close()
        textoEntryNomID.set("")
        direccionAlum.set("")



    def ActualResidencia1(a,b):
        """
        esta funcion permite actualirar residencia en la base de datos
        :param a: es el valor actualizar
        :param b: es el valor que representa el registro
        :return:
        """
        connexion = sqlite3.connect(nameBD.nomBD())
        cursor = connexion.cursor()
        cursor.execute(f"update alumno set residencia = '{a}' where id = '{b}' ")
        connexion.commit()

        connexion.close()
        textoEntryNomID.set("")
        direccionAlum.set("")



    def ActualEstadoAlumno(a,b):
        """
        esta funcion permite actualirar el estado del alumno en el centro en la base de datos
        :param a: es el valor actualizar
        :param b: es el valor que representa el registro
        :return:
        """
        connexion = sqlite3.connect(nameBD.nomBD())
        cursor = connexion.cursor()
        cursor.execute(f"update alumno set estado = '{a}' where nombre_y_apellidos = '{b}' ")
        connexion.commit()

        connexion.close()
        textoEntryNomID.set("")




    def ActualEstadoAlumno1(a,b):
        """
        esta funcion permite actualirar el estado del alumno en el centro en la base de datos
        :param a: es el valor actualizar
        :param b: es el valor que representa el registro
        :return:
        """
        connexion = sqlite3.connect(nameBD.nomBD())
        cursor = connexion.cursor()
        cursor.execute(f"update alumno set estado = '{a}' where id = '{b}' ")
        connexion.commit()

        connexion.close()
        textoEntryNomID.set("")






    def ActualFoto(a, b):
            """
            esta funcion permite actualirar la foto en la base de datos
            :param a: es el valor actualizar
            :param b: es el valor que representa el registro
            :return:
            """
            connexion = sqlite3.connect(nameBD.nomBD())
            cursor = connexion.cursor()
            cursor.execute(f"update alumno set foto = '{a}' where nombre_y_apellidos = '{b}' ")
            connexion.commit()

            connexion.close()
            entryFoto.config(font=("comic sans ms", 11), state="normal")
            textoEntryNomID.set("")
            fotoAlum.set("images/logoTsei.png")
            entryFoto.config(font=("comic sans ms", 11), state="readonly")





    def ActualFoto1(a, b):
            """
            esta funcion permite actualirar la foto en la base de datos
            :param a: es el valor actualizar
            :param b: es el valor que representa el registro
            :return:
            """
            connexion = sqlite3.connect(nameBD.nomBD())
            cursor = connexion.cursor()
            cursor.execute(f"update alumno set foto = '{a}' where id = '{b}' ")
            connexion.commit()

            connexion.close()
            entryFoto.config(font=("comic sans ms", 11), state="normal")
            textoEntryNomID.set("")
            fotoAlum.set("images/logoTsei.png")

            entryFoto.config(font=("comic sans ms", 11), state="readonly")



    #-----------------funciones de selecion nombre o id---------------------------------


    def curso1():
                if opcionRadio2.get() == 1:
                    ActualCurso(comboActualizar.get(), textoEntryNomID.get().strip().upper())
                elif opcionRadio2.get() == 2:
                    ActualCurso1(comboActualizar.get(), textoEntryNomID.get().upper())
                else:
                    pass

    def nombreT():
                if opcionRadio2.get() == 1:
                    ActualNomTutor(nombreTutor.get().upper(), textoEntryNomID.get().strip().upper())
                elif opcionRadio2.get() == 2:
                    ActualNomTutor1(nombreTutor.get().upper(), textoEntryNomID.get().upper())
                else:
                    pass

    def telT():
                if opcionRadio2.get() == 1:
                    ActualTelTutor(telTutor.get().upper(), textoEntryNomID.get().strip().upper())
                elif opcionRadio2.get() == 2:
                    ActualTelTutor1(telTutor.get().upper(), textoEntryNomID.get().upper())
                else:
                    pass

    def patologia1():
                if opcionRadio2.get() == 1:
                    ActualPatologia(patologiaAlumno.get().upper(), textoEntryNomID.get().strip().upper())
                elif opcionRadio2.get() == 2:
                    ActualPatologia1(patologiaAlumno.get().upper(), textoEntryNomID.get().upper())
                else:
                    pass

    def estadoAlumno1():
                if opcionRadio2.get() == 1:
                    ActualEstadoAlumno(comboEstatus.get().upper(), textoEntryNomID.get().strip().upper())
                elif opcionRadio2.get() == 2:
                    ActualEstadoAlumno1(comboEstatus.get().upper(), textoEntryNomID.get().upper())
                else:
                    pass

    def fotoA():
                if opcionRadio2.get() == 1:
                    ActualFoto(fotoAlum.get().upper(), textoEntryNomID.get().strip().upper())
                elif opcionRadio2.get() == 2:
                    ActualFoto1(fotoAlum.get().upper(), textoEntryNomID.get().upper())
                else:
                    entryFoto.config(font=("comic sans ms", 11), state="normal")
                    fotoAlum.set("images/logoTsei.png")
                    entryFoto.config(font=("comic sans ms", 11), state="readonly")

    def direccion1():
                if opcionRadio2.get() == 1:
                    ActualResidencia(direccionAlum.get().upper(), textoEntryNomID.strip().get().upper())
                elif opcionRadio2.get() == 2:
                    ActualResidencia1(direccionAlum.get().upper(), textoEntryNomID.get().upper())
                else:
                    pass


    #---------------funciones de actualizacion del label de confirmacio----------------------




    root.mainloop()