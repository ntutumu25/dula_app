from tkinter.ttk import *
from tkinter import *
import sqlite3
import loguin
import nameBD


def cursos():

    root = Toplevel()

    root.title("DULA 1.0-REGISTRO DE NOTAS")

    root.geometry("1040x570")
    root.config(bg = "grey85")
    root.resizable(0,0)
    root.iconbitmap("images/dula.ico")

    logo = PhotoImage(file="images/logoTsei.png")
    labeLogo = Label(root, image=logo)
    labeLogo.pack(side="right", anchor="n")
    # -------------------labe de la raiz-----------------------
    tituloLabel = Label(root, text="REGISTRO DE NOTAS")
    tituloLabel.config(font=("jokerman", 14), bd=5, relief="groov", fg="black", bg="lemonchiffon2")
    tituloLabel.pack()

    labelEspacio = Label(root)
    labelEspacio.config(bg = "grey85", height = 2)
    labelEspacio.pack()
    #--------------ENTRY ROOT PARA NOMBRE DEL USUARIO--------------------------------------
    entrySesion = StringVar()
    entrySesion.set(loguin.nombreSesion() + ", DE SESIÓN...")
    entryRoot = Entry(root, textvariable = entrySesion, width = 70)
    entryRoot.config(font = ("comic sans ms", 9), justify = "center", bg = "orange",)
    entryRoot.place(x = 80, y = 50)




    # -----BOTON DE CIERRE DE VENTANA----------------------
    """
    botonCerrarV = Button(root, text="cerrar la ventana",
                          command= loguin.cierreSesion(root), activebackground="#F50743")
    botonCerrarV.config(font=("comic sans ms", 10), bg="salmon3", cursor="hand2")
    botonCerrarV.pack(side="left", anchor="s")
    """
    
    #-----------variables radiosbotton----------------------------------------
    nombreId = IntVar()
    trimestre = IntVar()

    nombreId1 = IntVar()
    trimestre1 = IntVar()

    nombreId2 = IntVar()
    trimestre2 = IntVar()

    nombreId3 = IntVar()
    trimestre3 = IntVar()

    nombreId41 = IntVar()
    trimestre41 = IntVar()

    nombreId42 = IntVar()
    trimestre42 = IntVar()

    nombreId43 = IntVar()
    trimestre43 = IntVar()

    nombreId51 = IntVar()
    trimestre51 = IntVar()

    nombreId52 = IntVar()
    trimestre52 = IntVar()

    nombreId53 = IntVar()
    trimestre53 = IntVar()
    #-----------------------variables de los Entrys--------------------------------------
    nombreEsba1 = StringVar()
    lenguaEsba1 = StringVar()
    matesEsba1 = StringVar()
    geografiaEsba1 = StringVar()
    naturalesEsba1 = StringVar()
    francesEsba1 = StringVar()
    inglesEsba1 = StringVar()
    religionEsba1 = StringVar()
    plasticaEsba1 = StringVar()
    efisicaEsba1 = StringVar()
    informaticaEsba1 = StringVar()

    nombreEsba2 = StringVar()
    lenguaEsba2 = StringVar()
    matesEsba2 = StringVar()
    geografiaEsba2 = StringVar()
    naturalesEsba2 = StringVar()
    francesEsba2 = StringVar()
    inglesEsba2 = StringVar()
    religionEsba2 = StringVar()
    plasticaEsba2 = StringVar()
    efisicaEsba2 = StringVar()
    informaticaEsba2 = StringVar()

    nombreEsba3 = StringVar()
    lenguaEsba3 = StringVar()
    matesEsba3 = StringVar()
    historiaEsba3 = StringVar()
    biologiaygeologiaEsba3 = StringVar()
    francesEsba3 = StringVar()
    inglesEsba3 = StringVar()
    religionEsba3 = StringVar()
    plasticaEsba3 = StringVar()
    efisicaEsba3 = StringVar()
    informaticaEsba3 = StringVar()
    fisicayquimicaEsba3 = StringVar()
    tecnologiaEsba3 = StringVar()

    nombreEsba4 = StringVar()
    lenguaEsba4 = StringVar()
    matesEsba4 = StringVar()
    historiaEsba4 = StringVar()
    biologiaygeologiaEsba4 = StringVar()
    francesEsba4 = StringVar()
    inglesEsba4 = StringVar()
    religionEsba4 = StringVar()
    plasticaEsba4 = StringVar()
    efisicaEsba4 = StringVar()
    informaticaEsba4 = StringVar()
    fisicayquimicaEsba4 = StringVar()
    tecnologiaEsba4 = StringVar()

    nombreBach11 = StringVar()
    lenguaBach11 = StringVar()
    matesBach11 = StringVar()
    historiaBach11 = StringVar()
    fisicayquimicaBach11 = StringVar()
    biologiaBach11 = StringVar()
    economiaBach11 = StringVar()
    francesBach11 = StringVar()
    inglesBach11 = StringVar()
    religionBach11 = StringVar()
    dibujoBach11 = StringVar()
    efisicaBach11 = StringVar()
    informaticaBach11 = StringVar()
    filosofiaBach11 = StringVar()
    cctmBach11 = StringVar()

    nombreBach12 = StringVar()
    lenguaBach12 = StringVar()
    matesBach12 = StringVar()
    historiaBach12 = StringVar()
    tecnologiaBach12 = StringVar()
    biologiaBach12 = StringVar()
    economiaBach12 = StringVar()
    francesBach12 = StringVar()
    inglesBach12 = StringVar()
    religionBach12 = StringVar()
    dibujoBach12 = StringVar()
    efisicaBach12 = StringVar()
    informaticaBach12 = StringVar()
    filosofiaBach12 = StringVar()
    cctmBach12 = StringVar()

    nombreBach13 = StringVar()
    lenguaBach13 = StringVar()
    matesBach13 = StringVar()
    historiaBach13 = StringVar()
    geografiaBach13 = StringVar()
    latinBach13 = StringVar()
    economiaBach13 = StringVar()
    francesBach13 = StringVar()
    inglesBach13 = StringVar()
    religionBach13 = StringVar()
    griegoBach13 = StringVar()
    efisicaBach13 = StringVar()
    informaticaBach13 = StringVar()
    filosofiaBach13 = StringVar()
    cctmBach13 = StringVar()

    nombreBach21 = StringVar()
    lenguaBach21 = StringVar()
    matesBach21 = StringVar()
    historiaBach21 = StringVar()
    quimicaBach21 = StringVar()
    geologiaBach21 = StringVar()
    economiaBach21 = StringVar()
    francesBach21 = StringVar()
    inglesBach21 = StringVar()
    religionBach21 = StringVar()
    electrotecniaBach21 = StringVar()
    efisicaBach21 = StringVar()
    informaticaBach21 = StringVar()
    filosofiaBach21 = StringVar()
    cnsBach21 = StringVar()

    nombreBach22 = StringVar()
    lenguaBach22 = StringVar()
    matesBach22 = StringVar()
    historiaBach22 = StringVar()
    tecnologiaBach22 = StringVar()
    electrotecniaBach22 = StringVar()
    economiaBach22 = StringVar()
    francesBach22 = StringVar()
    inglesBach22 = StringVar()
    religionBach22 = StringVar()
    dibujoBach22 = StringVar()
    efisicaBach22 = StringVar()
    informaticaBach22 = StringVar()
    filosofiaBach22 = StringVar()
    cnsBach22 = StringVar()

    nombreBach23 = StringVar()
    lenguaBach23 = StringVar()
    matesBach23 = StringVar()
    historiaBach23 = StringVar()
    historiaarteBach23 = StringVar()
    latinBach23 = StringVar()
    economiaBach23 = StringVar()
    francesBach23 = StringVar()
    inglesBach23 = StringVar()
    religionBach23 = StringVar()
    griegoBach23 = StringVar()
    efisicaBach23 = StringVar()
    informaticaBach23 = StringVar()
    filosofiaBach23 = StringVar()
    cnsBach23 = StringVar()





    #---------------frames notebook--------------------------------------------------
    frame = Frame(root, width = 10000)
    frame.place(x = 80, y = 80)
    #-------------Notbook----------------------------------------------------------

    notebook = Notebook(frame, width = 900, height = 430)
    notebook.config()
    notebook.grid(row = 0, column = 0)


    #-------------pestagnas de los cursos ----------------------------------------------
    unoEsba = Frame(notebook)
    unoEsba.config(bg = "grey85")
    notebook.add(unoEsba, text = "1°ESBA")

    dosEsba = Frame(notebook)
    dosEsba.config(bg="grey85")
    notebook.add(dosEsba, text="2°ESBA")

    tresEsba = Frame(notebook)
    notebook.add(tresEsba, text="3°ESBA")
    tresEsba.config(bg="grey85")

    cuatroEsba = Frame(notebook)
    notebook.add(cuatroEsba, text="4°ESBA")
    cuatroEsba.config(bg="grey85")

    unoBach = Frame(notebook)
    notebook.add(unoBach, text="1°BACH")
    unoBach.config(bg="grey85")

    dosBach = Frame(notebook)
    notebook.add(dosBach, text="2°BACH")
    dosBach.config(bg="grey85")

    #-----------------pestangna unoEsba--------------------------------------------------------

    nombreIdLabel = Label(unoEsba, text = "Opción de identificación:")
    nombreIdLabel.config(font=("comic sans ms", 11), relief="sunken", bd = 3)
    nombreIdLabel.grid(row = 0, column = 0, padx = 5, pady = 5, sticky="e")

    indicacionLabel = Label(unoEsba, text="Nombre completo o ID:")
    indicacionLabel.config(font=("comic sans ms", 11), relief="sunken", bd=3)
    indicacionLabel.grid(row=1, column=0, padx=5, pady=5, sticky="e")

    trimestreLabel = Label(unoEsba, text="Sesión:")
    trimestreLabel.config(font=("comic sans ms", 11), relief="sunken", bd=3)
    trimestreLabel.grid(row=2, column=0, padx=5, pady=5, sticky="e")

    materiasLabel = Label(unoEsba, text="Asignaturas:")
    materiasLabel.config(font=("comic sans ms", 11), relief="sunken", bd=3)
    materiasLabel.grid(row=3, column=0, padx=5, pady=5, sticky="e")

    lenguaLabel = Label(unoEsba, text="Lengua Española:")
    lenguaLabel.config(font=("comic sans ms", 10), bg = "grey85")
    lenguaLabel.grid(row=3, column=1, padx=2, pady=2, sticky="e")

    matesLabel = Label(unoEsba, text="Matemáticas:")
    matesLabel.config(font=("comic sans ms", 10), bg="grey85")
    matesLabel.grid(row=4, column=1, padx=2, pady=2, sticky="e")

    geogLabel = Label(unoEsba, text="Geografía:")
    geogLabel.config(font=("comic sans ms", 10), bg="grey85")
    geogLabel.grid(row=5, column=1, padx=2, pady=2, sticky="e")

    naturalesLabel = Label(unoEsba, text="CC.Naturales:")
    naturalesLabel.config(font=("comic sans ms", 10), bg="grey85")
    naturalesLabel.grid(row=6, column=1, padx=2, pady=2, sticky="e")

    francesLabel = Label(unoEsba, text="Francés:")
    francesLabel.config(font=("comic sans ms", 10), bg="grey85")
    francesLabel.grid(row=7, column=1, padx=2, pady=2, sticky="e")

    inglesLabel = Label(unoEsba, text="Inglés:")
    inglesLabel.config(font=("comic sans ms", 10), bg="grey85")
    inglesLabel.grid(row=3, column=3, padx=2, pady=2, sticky="e")

    religionLabel = Label(unoEsba, text = "Religión:")
    religionLabel.config(font=("comic sans ms", 10), bg="grey85")
    religionLabel.grid(row=4, column=3, padx=2, pady=2, sticky="e")

    plasticaLabel = Label(unoEsba, text="E.Plástica:")
    plasticaLabel.config(font=("comic sans ms", 10), bg="grey85")
    plasticaLabel.grid(row=5, column=3, padx=2, pady=2, sticky="e")

    educionFisicaLabel = Label(unoEsba, text="E.Física:")
    educionFisicaLabel.config(font=("comic sans ms", 10), bg="grey85")
    educionFisicaLabel.grid(row=6, column=3, padx=2, pady=2, sticky="e")

    inforLabel = Label(unoEsba, text="Informática:")
    inforLabel.config(font=("comic sans ms", 10), bg="grey85")
    inforLabel.grid(row=7, column=3, padx=2, pady=2, sticky="e")




    #------------Entry unoEsba---------------------------------------
    nombreIdEntry = Entry(unoEsba, width = 32, textvariable = nombreEsba1)
    nombreIdEntry.config(font=("comic sans ms", 11))
    nombreIdEntry.grid(row=1, column=1, columnspan = 2, padx=1, pady=1, sticky="w")

    Entry(unoEsba, width=8, font=(9), textvariable = lenguaEsba1).grid(row=3, column=2, padx=2, pady=2, sticky="w")
    Entry(unoEsba, width=8, font=(9), textvariable = matesEsba1).grid(row=4, column=2, padx=2, pady=2, sticky="w")
    Entry(unoEsba, width=8, font=(9), textvariable = geografiaEsba1).grid(row=5, column=2, padx=2, pady=2, sticky="w")
    Entry(unoEsba, width=8, font=(9), textvariable = naturalesEsba1).grid(row=6, column=2, padx=2, pady=2, sticky="w")
    Entry(unoEsba, width=8, font=(9), textvariable = francesEsba1).grid(row=7, column=2, padx=2, pady=2, sticky="w")
    Entry(unoEsba, width=8, font=(9), textvariable = inglesEsba1).grid(row=3, column=4, padx=2, pady=2, sticky="w")
    Entry(unoEsba, width=8, font=(9), textvariable = religionEsba1).grid(row=4, column=4, padx=2, pady=2, sticky="w")
    Entry(unoEsba, width=8, font=(9), textvariable = plasticaEsba1).grid(row=5, column=4, padx=2, pady=2, sticky="w")
    Entry(unoEsba, width=8, font=(9), textvariable = efisicaEsba1).grid(row=6, column=4, padx=2, pady=2, sticky="w")
    Entry(unoEsba, width=8, font=(9), textvariable = informaticaEsba1).grid(row=7, column=4, padx=2, pady=2, sticky="w")

    #-----radiobuton unoEsba---------------------------------------
    Radiobutton(unoEsba, text="Nombre completo", variable=nombreId, value=1, bg = "grey85",
                font=("comic sans ms", 11), cursor="hand2").grid(row=0, column=1, padx=5, pady=5, sticky="w")
    Radiobutton(unoEsba, text="ID", variable=nombreId, value=2, bg = "grey85",
                font=("comic sans ms", 11), cursor="hand2", ).grid(row=0, column=2, padx=5, pady=5, sticky="w")

    Radiobutton(unoEsba, text="1°Trimestre", variable=trimestre, value=1, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2").grid(row=2, column=1, padx=5, pady=5, sticky="w")

    Radiobutton(unoEsba, text="2°Trimestre", variable=trimestre, value=2, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2", ).grid(row=2, column=2, padx=5, pady=5, sticky="w")

    Radiobutton(unoEsba, text="3°Trimestre", variable=trimestre, value=3, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2", ).grid(row=2, column=3, padx=5, pady=5, sticky="w")

    Radiobutton(unoEsba, text="Septiembre", variable=trimestre, value=4, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2", ).grid(row=2, column=4, padx=5, pady=5, sticky="w")

    #------------botones unoEsba----------------------------------------------------------------------------------

    Button(unoEsba, text = "Registrar", cursor="hand2", activebackground="#F50743", command = lambda:unoEsba(),
           font=("comic sans ms", 11)).grid(row=11, column=0, padx=5, pady=5, sticky="e")

    Button(unoEsba, text="Verificar", cursor="hand2", activebackground="#F50743", command = lambda:verifi1(),
           font=("comic sans ms", 11)).grid(row=11, column=1, padx=5, pady=5, sticky="w")



    # -----------------pestangna dosEsba--------------------------------------------------------

    nombreIdLabel = Label(dosEsba, text="Opción de identificación:")
    nombreIdLabel.config(font=("comic sans ms", 11), relief="sunken", bd=3)
    nombreIdLabel.grid(row=0, column=0, padx=5, pady=5, sticky="e")

    indicacionLabel = Label(dosEsba, text="Nombre completo o ID:")
    indicacionLabel.config(font=("comic sans ms", 11), relief="sunken", bd=3)
    indicacionLabel.grid(row=1, column=0, padx=5, pady=5, sticky="e")

    trimestreLabel = Label(dosEsba, text="Sesión:")
    trimestreLabel.config(font=("comic sans ms", 11), relief="sunken", bd=3)
    trimestreLabel.grid(row=2, column=0, padx=5, pady=5, sticky="e")

    materiasLabel = Label(dosEsba, text="Asignaturas:")
    materiasLabel.config(font=("comic sans ms", 11), relief="sunken", bd=3)
    materiasLabel.grid(row=3, column=0, padx=5, pady=5, sticky="e")

    lenguaLabel = Label(dosEsba, text="Lengua Española:")
    lenguaLabel.config(font=("comic sans ms", 10), bg="grey85")
    lenguaLabel.grid(row=3, column=1, padx=2, pady=2, sticky="e")

    matesLabel = Label(dosEsba, text="Matemáticas:")
    matesLabel.config(font=("comic sans ms", 10), bg="grey85")
    matesLabel.grid(row=4, column=1, padx=2, pady=2, sticky="e")

    geogLabel = Label(dosEsba, text="Geografía:")
    geogLabel.config(font=("comic sans ms", 10), bg="grey85")
    geogLabel.grid(row=5, column=1, padx=2, pady=2, sticky="e")

    naturalesLabel = Label(dosEsba, text="CC.Naturales:")
    naturalesLabel.config(font=("comic sans ms", 10), bg="grey85")
    naturalesLabel.grid(row=6, column=1, padx=2, pady=2, sticky="e")

    francesLabel = Label(dosEsba, text="Francés:")
    francesLabel.config(font=("comic sans ms", 10), bg="grey85")
    francesLabel.grid(row=7, column=1, padx=2, pady=2, sticky="e")

    inglesLabel = Label(dosEsba, text="Inglés:")
    inglesLabel.config(font=("comic sans ms", 10), bg="grey85")
    inglesLabel.grid(row=3, column=3, padx=2, pady=2, sticky="e")

    religionLabel = Label(dosEsba, text="Religión:")
    religionLabel.config(font=("comic sans ms", 10), bg="grey85")
    religionLabel.grid(row=4, column=3, padx=2, pady=2, sticky="e")

    plasticaLabel = Label(dosEsba, text="E.Plástica:")
    plasticaLabel.config(font=("comic sans ms", 10), bg="grey85")
    plasticaLabel.grid(row=5, column=3, padx=2, pady=2, sticky="e")

    educionFisicaLabel = Label(dosEsba, text="E.Física:")
    educionFisicaLabel.config(font=("comic sans ms", 10), bg="grey85")
    educionFisicaLabel.grid(row=6, column=3, padx=2, pady=2, sticky="e")

    inforLabel = Label(dosEsba, text="Informática:")
    inforLabel.config(font=("comic sans ms", 10), bg="grey85")
    inforLabel.grid(row=7, column=3, padx=2, pady=2, sticky="e")

    # ------------Entry dosEsba---------------------------------------
    nombreIdEntry = Entry(dosEsba, width=32, textvariable = nombreEsba2)
    nombreIdEntry.config(font=("comic sans ms", 11))
    nombreIdEntry.grid(row=1, column=1, columnspan=2, padx=1, pady=1, sticky="w")

    Entry(dosEsba, width=8, font=(9), textvariable = lenguaEsba2).grid(row=3, column=2, padx=2, pady=2, sticky="w")
    Entry(dosEsba, width=8, font=(9), textvariable = matesEsba2).grid(row=4, column=2, padx=2, pady=2, sticky="w")
    Entry(dosEsba, width=8, font=(9), textvariable = geografiaEsba2).grid(row=5, column=2, padx=2, pady=2, sticky="w")
    Entry(dosEsba, width=8, font=(9), textvariable = naturalesEsba2).grid(row=6, column=2, padx=2, pady=2, sticky="w")
    Entry(dosEsba, width=8, font=(9), textvariable = francesEsba2).grid(row=7, column=2, padx=2, pady=2, sticky="w")
    Entry(dosEsba, width=8, font=(9), textvariable = inglesEsba2).grid(row=3, column=4, padx=2, pady=2, sticky="w")
    Entry(dosEsba, width=8, font=(9), textvariable = religionEsba2).grid(row=4, column=4, padx=2, pady=2, sticky="w")
    Entry(dosEsba, width=8, font=(9), textvariable = plasticaEsba2).grid(row=5, column=4, padx=2, pady=2, sticky="w")
    Entry(dosEsba, width=8, font=(9), textvariable = efisicaEsba2).grid(row=6, column=4, padx=2, pady=2, sticky="w")
    Entry(dosEsba, width=8, font=(9), textvariable = informaticaEsba2).grid(row=7, column=4, padx=2, pady=2, sticky="w")

    # -----radiobuton dosEsba---------------------------------------
    Radiobutton(dosEsba, text="Nombre completo", variable=nombreId1, value=1, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2").grid(row=0, column=1, padx=5, pady=5, sticky="w")
    Radiobutton(dosEsba, text="ID", variable=nombreId1, value=2, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2", ).grid(row=0, column=2, padx=5, pady=5, sticky="w")

    Radiobutton(dosEsba, text="1°Trimestre", variable=trimestre1, value=1, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2").grid(row=2, column=1, padx=5, pady=5, sticky="w")

    Radiobutton(dosEsba, text="2°Trimestre", variable=trimestre1, value=2, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2", ).grid(row=2, column=2, padx=5, pady=5, sticky="w")

    Radiobutton(dosEsba, text="3°Trimestre", variable=trimestre1, value=3, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2", ).grid(row=2, column=3, padx=5, pady=5, sticky="w")

    Radiobutton(dosEsba, text="Septiembre", variable=trimestre1, value=4, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2", ).grid(row=2, column=4, padx=5, pady=5, sticky="w")

    # ------------botones dosEsba----------------------------------------------------------------------------------

    Button(dosEsba, text="Registrar", cursor="hand2", activebackground="#F50743", command = lambda:dosEsba(),
           font=("comic sans ms", 11)).grid(row=11, column=0, padx=5, pady=5, sticky="e")

    Button(dosEsba, text="Verificar", cursor="hand2", activebackground="#F50743", command = lambda:verifi2(),
           font=("comic sans ms", 11)).grid(row=11, column=1, padx=5, pady=5, sticky="w")

    # -----------------pestangna tresEsba--------------------------------------------------------

    nombreIdLabel = Label(tresEsba, text="Opción de identificación:")
    nombreIdLabel.config(font=("comic sans ms", 11), relief="sunken", bd=3)
    nombreIdLabel.grid(row=0, column=0, padx=5, pady=5, sticky="e")

    indicacionLabel = Label(tresEsba, text="Nombre completo o ID:")
    indicacionLabel.config(font=("comic sans ms", 11), relief="sunken", bd=3)
    indicacionLabel.grid(row=1, column=0, padx=5, pady=5, sticky="e")

    trimestreLabel = Label(tresEsba, text="Sesión:")
    trimestreLabel.config(font=("comic sans ms", 11), relief="sunken", bd=3)
    trimestreLabel.grid(row=2, column=0, padx=5, pady=5, sticky="e")

    materiasLabel = Label(tresEsba, text="Asignaturas:")
    materiasLabel.config(font=("comic sans ms", 11), relief="sunken", bd=3)
    materiasLabel.grid(row=3, column=0, padx=5, pady=5, sticky="e")

    lenguaLabel = Label(tresEsba, text="Lengua Española:")
    lenguaLabel.config(font=("comic sans ms", 10), bg="grey85")
    lenguaLabel.grid(row=3, column=1, padx=2, pady=2, sticky="e")

    matesLabel = Label(tresEsba, text="Matemáticas:")
    matesLabel.config(font=("comic sans ms", 10), bg="grey85")
    matesLabel.grid(row=4, column=1, padx=2, pady=2, sticky="e")

    historiaLabel = Label(tresEsba, text="Hªde África y GE:")
    historiaLabel.config(font=("comic sans ms", 10), bg="grey85")
    historiaLabel.grid(row=5, column=1, padx=2, pady=2, sticky="e")

    fygLabel = Label(tresEsba, text="Física y Química:")
    fygLabel.config(font=("comic sans ms", 10), bg="grey85")
    fygLabel.grid(row=6, column=1, padx=2, pady=2, sticky="e")

    bioLabel = Label(tresEsba, text="Biología y Geología:")
    bioLabel.config(font=("comic sans ms", 10), bg="grey85")
    bioLabel.grid(row=7, column=1, padx=2, pady=2, sticky="e")

    tecnologiaLabel = Label(tresEsba, text="Tecnología:")
    tecnologiaLabel.config(font=("comic sans ms", 10), bg="grey85")
    tecnologiaLabel.grid(row=8, column=1, padx=2, pady=2, sticky="e")

    francesLabel = Label(tresEsba, text="Francés:")
    francesLabel.config(font=("comic sans ms", 10), bg="grey85")
    francesLabel.grid(row=9, column=1, padx=2, pady=2, sticky="e")

    inglesLabel = Label(tresEsba, text="Inglés:")
    inglesLabel.config(font=("comic sans ms", 10), bg="grey85")
    inglesLabel.grid(row=3, column=3, padx=2, pady=2, sticky="e")

    religionLabel = Label(tresEsba, text="Religión:")
    religionLabel.config(font=("comic sans ms", 10), bg="grey85")
    religionLabel.grid(row=4, column=3, padx=2, pady=2, sticky="e")

    plasticaLabel = Label(tresEsba, text="E.Plástica:")
    plasticaLabel.config(font=("comic sans ms", 10), bg="grey85")
    plasticaLabel.grid(row=5, column=3, padx=2, pady=2, sticky="e")

    educionFisicaLabel = Label(tresEsba, text="E.Física:")
    educionFisicaLabel.config(font=("comic sans ms", 10), bg="grey85")
    educionFisicaLabel.grid(row=6, column=3, padx=2, pady=2, sticky="e")

    inforLabel = Label(tresEsba, text="Informática:")
    inforLabel.config(font=("comic sans ms", 10), bg="grey85")
    inforLabel.grid(row=7, column=3, padx=2, pady=2, sticky="e")

    # ------------Entry tresEsba---------------------------------------
    nombreIdEntry = Entry(tresEsba, width=32, textvariable = nombreEsba3)
    nombreIdEntry.config(font=("comic sans ms", 11))
    nombreIdEntry.grid(row=1, column=1, columnspan=2, padx=1, pady=1, sticky="w")

    Entry(tresEsba, width=8, font=(9), textvariable = lenguaEsba3).grid(row=3, column=2, padx=2, pady=2, sticky="w") #lengua
    Entry(tresEsba, width=8, font=(9), textvariable = matesEsba3).grid(row=4, column=2, padx=2, pady=2, sticky="w") # matematicas
    Entry(tresEsba, width=8, font=(9), textvariable = historiaEsba3).grid(row=5, column=2, padx=2, pady=2, sticky="w") # historia
    Entry(tresEsba, width=8, font=(9), textvariable = fisicayquimicaEsba3).grid(row=6, column=2, padx=2, pady=2, sticky="w") # fisica y quimica
    Entry(tresEsba, width=8, font=(9), textvariable = biologiaygeologiaEsba3).grid(row=7, column=2, padx=2, pady=2, sticky="w") # Biologia y Geologia
    Entry(tresEsba, width=8, font=(9), textvariable = tecnologiaEsba3).grid(row=8, column=2, padx=2, pady=2, sticky="w") # tecnologia
    Entry(tresEsba, width=8, font=(9), textvariable = francesEsba3).grid(row=9, column=2, padx=2, pady=2, sticky="w") # frances
    Entry(tresEsba, width=8, font=(9), textvariable = inglesEsba3).grid(row=3, column=4, padx=2, pady=2, sticky="w") # ingles
    Entry(tresEsba, width=8, font=(9), textvariable = religionEsba3).grid(row=4, column=4, padx=2, pady=2, sticky="w") # religion
    Entry(tresEsba, width=8, font=(9), textvariable = plasticaEsba3).grid(row=5, column=4, padx=2, pady=2, sticky="w") # E.plastica
    Entry(tresEsba, width=8, font=(9), textvariable = efisicaEsba3).grid(row=6, column=4, padx=2, pady=2, sticky="w") # E.fisica
    Entry(tresEsba, width=8, font=(9), textvariable = informaticaEsba3).grid(row=7, column=4, padx=2, pady=2, sticky="w") # informatica

    # -----radiobuton tresEsba---------------------------------------
    Radiobutton(tresEsba, text="Nombre completo", variable=nombreId2, value=1, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2").grid(row=0, column=1, padx=5, pady=5, sticky="w")
    Radiobutton(tresEsba, text="ID", variable=nombreId2, value=2, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2", ).grid(row=0, column=2, padx=5, pady=5, sticky="w")

    Radiobutton(tresEsba, text="1°Trimestre", variable=trimestre2, value=1, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2").grid(row=2, column=1, padx=5, pady=5, sticky="w")

    Radiobutton(tresEsba, text="2°Trimestre", variable=trimestre2, value=2, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2", ).grid(row=2, column=2, padx=5, pady=5, sticky="w")

    Radiobutton(tresEsba, text="3°Trimestre", variable=trimestre2, value=3, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2", ).grid(row=2, column=3, padx=5, pady=5, sticky="w")

    Radiobutton(tresEsba, text="Septiembre", variable=trimestre2, value=4, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2", ).grid(row=2, column=4, padx=5, pady=5, sticky="w")

    # ------------botones tresEsba----------------------------------------------------------------------------------

    Button(tresEsba, text="Registrar", cursor="hand2", activebackground="#F50743", command = lambda:tresEsba(),
           font=("comic sans ms", 11)).grid(row=11, column=0, padx=5, pady=5, sticky="e")

    Button(tresEsba, text="Verificar", cursor="hand2", activebackground="#F50743", command = lambda:verifi3(),
           font=("comic sans ms", 11)).grid(row=11, column=1, padx=5, pady=5, sticky="w")

    # -----------------pestangna cuatroEsba--------------------------------------------------------

    nombreIdLabel = Label(cuatroEsba, text="Opción de identificación:")
    nombreIdLabel.config(font=("comic sans ms", 11), relief="sunken", bd=3)
    nombreIdLabel.grid(row=0, column=0, padx=5, pady=5, sticky="e")

    indicacionLabel = Label(cuatroEsba, text="Nombre completo o ID:")
    indicacionLabel.config(font=("comic sans ms", 11), relief="sunken", bd=3)
    indicacionLabel.grid(row=1, column=0, padx=5, pady=5, sticky="e")

    trimestreLabel = Label(cuatroEsba, text="Sesión:")
    trimestreLabel.config(font=("comic sans ms", 11), relief="sunken", bd=3)
    trimestreLabel.grid(row=2, column=0, padx=5, pady=5, sticky="e")

    materiasLabel = Label(cuatroEsba, text="Asignaturas:")
    materiasLabel.config(font=("comic sans ms", 11), relief="sunken", bd=3)
    materiasLabel.grid(row=3, column=0, padx=5, pady=5, sticky="e")

    lenguaLabel = Label(cuatroEsba, text="Lengua Española:")
    lenguaLabel.config(font=("comic sans ms", 10), bg="grey85")
    lenguaLabel.grid(row=3, column=1, padx=2, pady=2, sticky="e")

    matesLabel = Label(cuatroEsba, text="Matemáticas:")
    matesLabel.config(font=("comic sans ms", 10), bg="grey85")
    matesLabel.grid(row=4, column=1, padx=2, pady=2, sticky="e")

    historiaLabel = Label(cuatroEsba, text="Historia Universal:")
    historiaLabel.config(font=("comic sans ms", 10), bg="grey85")
    historiaLabel.grid(row=5, column=1, padx=2, pady=2, sticky="e")

    fygLabel = Label(cuatroEsba, text="Física y Química:")
    fygLabel.config(font=("comic sans ms", 10), bg="grey85")
    fygLabel.grid(row=6, column=1, padx=2, pady=2, sticky="e")

    bioLabel = Label(cuatroEsba, text="Biología y Geología:")
    bioLabel.config(font=("comic sans ms", 10), bg="grey85")
    bioLabel.grid(row=7, column=1, padx=2, pady=2, sticky="e")

    tecnologiaLabel = Label(cuatroEsba, text="Tecnología:")
    tecnologiaLabel.config(font=("comic sans ms", 10), bg="grey85")
    tecnologiaLabel.grid(row=8, column=1, padx=2, pady=2, sticky="e")

    francesLabel = Label(cuatroEsba, text="Francés:")
    francesLabel.config(font=("comic sans ms", 10), bg="grey85")
    francesLabel.grid(row=9, column=1, padx=2, pady=2, sticky="e")

    inglesLabel = Label(cuatroEsba, text="Inglés:")
    inglesLabel.config(font=("comic sans ms", 10), bg="grey85")
    inglesLabel.grid(row=3, column=3, padx=2, pady=2, sticky="e")

    religionLabel = Label(cuatroEsba, text="Religión:")
    religionLabel.config(font=("comic sans ms", 10), bg="grey85")
    religionLabel.grid(row=4, column=3, padx=2, pady=2, sticky="e")

    plasticaLabel = Label(cuatroEsba, text="E.Plástica:")
    plasticaLabel.config(font=("comic sans ms", 10), bg="grey85")
    plasticaLabel.grid(row=5, column=3, padx=2, pady=2, sticky="e")

    educionFisicaLabel = Label(cuatroEsba, text="E.Física:")
    educionFisicaLabel.config(font=("comic sans ms", 10), bg="grey85")
    educionFisicaLabel.grid(row=6, column=3, padx=2, pady=2, sticky="e")

    inforLabel = Label(cuatroEsba, text="Informática:")
    inforLabel.config(font=("comic sans ms", 10), bg="grey75")
    inforLabel.grid(row=7, column=3, padx=2, pady=2, sticky="e")

    # ------------Entry cuatroEsba---------------------------------------
    nombreIdEntry = Entry(cuatroEsba, width=32, textvariable = nombreEsba4)
    nombreIdEntry.config(font=("comic sans ms", 11))
    nombreIdEntry.grid(row=1, column=1, columnspan=2, padx=1, pady=1, sticky="w")

    Entry(cuatroEsba, width=8, font=(9), textvariable = lenguaEsba4).grid(row=3, column=2, padx=2, pady=2, sticky="w")  # lengua
    Entry(cuatroEsba, width=8, font=(9), textvariable = matesEsba4).grid(row=4, column=2, padx=2, pady=2, sticky="w")  # matematicas
    Entry(cuatroEsba, width=8, font=(9), textvariable = historiaEsba4).grid(row=5, column=2, padx=2, pady=2, sticky="w")  # historia
    Entry(cuatroEsba, width=8, font=(9), textvariable = fisicayquimicaEsba4).grid(row=6, column=2, padx=2, pady=2, sticky="w")  # fisica y quimica
    Entry(cuatroEsba, width=8, font=(9), textvariable = biologiaygeologiaEsba4).grid(row=7, column=2, padx=2, pady=2, sticky="w")  # Biologia y Geologia
    Entry(cuatroEsba, width=8, font=(9), textvariable = tecnologiaEsba4).grid(row=8, column=2, padx=2, pady=2, sticky="w")  # tecnologia
    Entry(cuatroEsba, width=8, font=(9), textvariable = francesEsba4).grid(row=9, column=2, padx=2, pady=2, sticky="w")  # frances
    Entry(cuatroEsba, width=8, font=(9), textvariable = inglesEsba4).grid(row=3, column=4, padx=2, pady=2, sticky="w")  # ingles
    Entry(cuatroEsba, width=8, font=(9), textvariable = religionEsba4).grid(row=4, column=4, padx=2, pady=2, sticky="w")  # religion
    Entry(cuatroEsba, width=8, font=(9), textvariable = plasticaEsba4).grid(row=5, column=4, padx=2, pady=2, sticky="w")  # E.plastica
    Entry(cuatroEsba, width=8, font=(9), textvariable = efisicaEsba4).grid(row=6, column=4, padx=2, pady=2, sticky="w")  # E.fisica
    Entry(cuatroEsba, width=8, font=(9), textvariable = informaticaEsba4).grid(row=7, column=4, padx=2, pady=2, sticky="w")  # informatica

    # -----radiobuton cuatroEsba---------------------------------------
    Radiobutton(cuatroEsba, text="Nombre completo", variable=nombreId3, value=1, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2").grid(row=0, column=1, padx=5, pady=5, sticky="w")
    Radiobutton(cuatroEsba, text="ID", variable=nombreId3, value=2, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2", ).grid(row=0, column=2, padx=5, pady=5, sticky="w")

    Radiobutton(cuatroEsba, text="1°Trimestre", variable=trimestre3, value=1, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2").grid(row=2, column=1, padx=5, pady=5, sticky="w")

    Radiobutton(cuatroEsba, text="2°Trimestre", variable=trimestre3, value=2, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2", ).grid(row=2, column=2, padx=5, pady=5, sticky="w")

    Radiobutton(cuatroEsba, text="3°Trimestre", variable=trimestre3, value=3, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2", ).grid(row=2, column=3, padx=5, pady=5, sticky="w")

    Radiobutton(cuatroEsba, text="Septiembre", variable=trimestre3, value=4, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2", ).grid(row=2, column=4, padx=5, pady=5, sticky="w")

    # ------------botones cuatroEsba----------------------------------------------------------------------------------

    Button(cuatroEsba, text="Registrar", cursor="hand2", activebackground="#F50743", command = lambda:cuatroEsba(),
           font=("comic sans ms", 11)).grid(row=11, column=0, padx=5, pady=5, sticky="e")

    Button(cuatroEsba, text="Verificar", cursor="hand2", activebackground="#F50743",command = lambda:verifi4(),
           font=("comic sans ms", 11)).grid(row=11, column=1, padx=5, pady=5, sticky="w")


    #-----------pestagnas dosBach------------------------------------------------------------------------

    #-----------notebook de ramas pestagna de dosBach----------------------------------
    notebookRamas2 = Notebook(dosBach, width = 900, height = 800)
    notebookRamas2.place(x = 0, y = 0)

    ciencias2 = Frame(notebookRamas2)
    ciencias2.config(bg="grey85")
    notebookRamas2.add(ciencias2, text="Ciencias")

    tecnologia2 = Frame(notebookRamas2)
    tecnologia2.config(bg="grey85")
    notebookRamas2.add(tecnologia2, text="Tecnología")

    letras2 = Frame(notebookRamas2)
    letras2.config(bg="grey85")
    notebookRamas2.add(letras2, text="Humanidades")

    # -----------------pestangna ciencias2segundo--------------------------------------------------------

    #-------------Label ciencias2segundo-----------------------------------------------------------------
    nombreIdLabel = Label(ciencias2, text="Opción de identificación:")
    nombreIdLabel.config(font=("comic sans ms", 11), relief="sunken", bd=3)
    nombreIdLabel.grid(row=0, column=0, padx=5, pady=5, sticky="e")

    indicacionLabel = Label(ciencias2, text="Nombre completo o ID:")
    indicacionLabel.config(font=("comic sans ms", 11), relief="sunken", bd=3)
    indicacionLabel.grid(row=1, column=0, padx=5, pady=5, sticky="e")

    trimestreLabel = Label(ciencias2, text="Sesión:")
    trimestreLabel.config(font=("comic sans ms", 11), relief="sunken", bd=3)
    trimestreLabel.grid(row=2, column=0, padx=5, pady=5, sticky="e")

    materiasLabel = Label(ciencias2, text="Asignaturas:")
    materiasLabel.config(font=("comic sans ms", 11), relief="sunken", bd=3)
    materiasLabel.grid(row=3, column=0, padx=5, pady=5, sticky="e")

    lenguaLabel = Label(ciencias2, text="Lengua y Literatura:")
    lenguaLabel.config(font=("comic sans ms", 10), bg="grey85")
    lenguaLabel.grid(row=3, column=1, padx=2, pady=2, sticky="e")

    matesLabel = Label(ciencias2, text="MatemáticasII:")
    matesLabel.config(font=("comic sans ms", 10), bg="grey85")
    matesLabel.grid(row=4, column=1, padx=2, pady=2, sticky="e")

    historiaLabel = Label(ciencias2, text="Historia del Mundo Actual:")
    historiaLabel.config(font=("comic sans ms", 10), bg="grey85")
    historiaLabel.grid(row=5, column=1, padx=2, pady=2, sticky="e")

    quimicaLabel = Label(ciencias2, text="Química:")
    quimicaLabel.config(font=("comic sans ms", 10), bg="grey85")
    quimicaLabel.grid(row=6, column=1, padx=2, pady=2, sticky="e")

    geoLabel = Label(ciencias2, text="Geología:")
    geoLabel.config(font=("comic sans ms", 10), bg="grey85")
    geoLabel.grid(row=7, column=1, padx=2, pady=2, sticky="e")

    economiaLabel = Label(ciencias2, text="Economía:")
    economiaLabel.config(font=("comic sans ms", 10), bg="grey85")
    economiaLabel.grid(row=8, column=1, padx=2, pady=2, sticky="e")

    francesLabel = Label(ciencias2, text="Francés:")
    francesLabel.config(font=("comic sans ms", 10), bg="grey85")
    francesLabel.grid(row=9, column=1, padx=2, pady=2, sticky="e")

    inglesLabel = Label(ciencias2, text="Inglés:")
    inglesLabel.config(font=("comic sans ms", 10), bg="grey85")
    inglesLabel.grid(row=3, column=3, padx=2, pady=2, sticky="e")

    religionLabel = Label(ciencias2, text="Religión:")
    religionLabel.config(font=("comic sans ms", 10), bg="grey85")
    religionLabel.grid(row=4, column=3, padx=2, pady=2, sticky="e")

    electrotecniaLabel = Label(ciencias2, text="Electrotecnia:")
    electrotecniaLabel.config(font=("comic sans ms", 10), bg="grey85")
    electrotecniaLabel.grid(row=5, column=3, padx=2, pady=2, sticky="e")

    educionFisicaLabel = Label(ciencias2, text="E.Física:")
    educionFisicaLabel.config(font=("comic sans ms", 10), bg="grey85")
    educionFisicaLabel.grid(row=6, column=3, padx=2, pady=2, sticky="e")

    inforLabel = Label(ciencias2, text="Informática:")
    inforLabel.config(font=("comic sans ms", 10), bg="grey85")
    inforLabel.grid(row=7, column=3, padx=2, pady=2, sticky="e")

    filosofiaLabel = Label(ciencias2, text="H°de la Filosofía:")
    filosofiaLabel.config(font=("comic sans ms", 10), bg="grey85")
    filosofiaLabel.grid(row=8, column=3, padx=2, pady=2, sticky="e")

    cnsLabel = Label(ciencias2, text="CNS:")
    cnsLabel.config(font=("comic sans ms", 10), bg="grey85")
    cnsLabel.grid(row=9, column=3, padx=2, pady=2, sticky="e")

    # ------------Entry ciencias2segundo---------------------------------------
    nombreIdEntry = Entry(ciencias2, width=32, textvariable = nombreBach21)
    nombreIdEntry.config(font=("comic sans ms", 11))
    nombreIdEntry.grid(row=1, column=1, columnspan=2, padx=1, pady=1, sticky="w")

    Entry(ciencias2, width=8, font=(9), textvariable = lenguaBach21).grid(row=3, column=2, padx=2, pady=2, sticky="w")  # lengua
    Entry(ciencias2, width=8, font=(9), textvariable = matesBach21).grid(row=4, column=2, padx=2, pady=2, sticky="w")  # matematicasII
    Entry(ciencias2, width=8, font=(9), textvariable = historiaBach21).grid(row=5, column=2, padx=2, pady=2, sticky="w")  # historia del mundo actual
    Entry(ciencias2, width=8, font=(9), textvariable = quimicaBach21).grid(row=6, column=2, padx=2, pady=2, sticky="w")  # quimica
    Entry(ciencias2, width=8, font=(9), textvariable = geologiaBach21).grid(row=7, column=2, padx=2, pady=2, sticky="w")  # geologia
    Entry(ciencias2, width=8, font=(9), textvariable = economiaBach21).grid(row=8, column=2, padx=2, pady=2, sticky="w")  # Economia
    Entry(ciencias2, width=8, font=(9), textvariable = francesBach21).grid(row=9, column=2, padx=2, pady=2, sticky="w")  # frances
    Entry(ciencias2, width=8, font=(9), textvariable = inglesBach21).grid(row=3, column=4, padx=2, pady=2, sticky="w")  # ingles
    Entry(ciencias2, width=8, font=(9), textvariable = religionBach21).grid(row=4, column=4, padx=2, pady=2, sticky="w")  # religion
    Entry(ciencias2, width=8, font=(9), textvariable = electrotecniaBach21).grid(row=5, column=4, padx=2, pady=2, sticky="w")  # electrotecnia
    Entry(ciencias2, width=8, font=(9), textvariable = efisicaBach21).grid(row=6, column=4, padx=2, pady=2, sticky="w")  # E.fisica
    Entry(ciencias2, width=8, font=(9), textvariable = informaticaBach21).grid(row=7, column=4, padx=2, pady=2, sticky="w")  # informatica
    Entry(ciencias2, width=8, font=(9), textvariable = filosofiaBach21).grid(row=8, column=4, padx=2, pady=2, sticky="w")  # Filosifia
    Entry(ciencias2, width=8, font=(9), textvariable = cnsBach21).grid(row=9, column=4, padx=2, pady=2, sticky="w")  # cns


    # -----radiobuton ciencias2segundo---------------------------------------
    Radiobutton(ciencias2, text="Nombre completo", variable=nombreId51, value=1, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2").grid(row=0, column=1, padx=5, pady=5, sticky="w")
    Radiobutton(ciencias2, text="ID", variable=nombreId51, value=2, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2", ).grid(row=0, column=2, padx=5, pady=5, sticky="w")

    Radiobutton(ciencias2, text="1°Trimestre", variable=trimestre51, value=1, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2").grid(row=2, column=1, padx=5, pady=5, sticky="w")

    Radiobutton(ciencias2, text="2°Trimestre", variable=trimestre51, value=2, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2", ).grid(row=2, column=2, padx=5, pady=5, sticky="w")

    Radiobutton(ciencias2, text="3°Trimestre", variable=trimestre51, value=3, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2", ).grid(row=2, column=3, padx=5, pady=5, sticky="w")

    Radiobutton(ciencias2, text="Septiembre", variable=trimestre51, value=4, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2", ).grid(row=2, column=4, padx=5, pady=5, sticky="w")

    # ------------botones ciencias2segundo----------------------------------------------------------------------------------

    Button(ciencias2, text="Registrar", cursor="hand2", activebackground="#F50743", command = lambda:segundoBachCiencias(),
           font=("comic sans ms", 11)).grid(row=11, column=0, padx=5, pady=5, sticky="e")

    Button(ciencias2, text="Verificar", cursor="hand2", activebackground="#F50743", command = lambda:verifi61(),
           font=("comic sans ms", 11)).grid(row=11, column=1, padx=5, pady=5, sticky="w")

    # -----------------pestangna tecnologia2segundo--------------------------------------------------------

    # -------------Label tecnologia2segundo-----------------------------------------------------------------
    nombreIdLabel = Label(tecnologia2, text="Opción de identificación:")
    nombreIdLabel.config(font=("comic sans ms", 11), relief="sunken", bd=3)
    nombreIdLabel.grid(row=0, column=0, padx=5, pady=5, sticky="e")

    indicacionLabel = Label(tecnologia2, text="Nombre completo o ID:")
    indicacionLabel.config(font=("comic sans ms", 11), relief="sunken", bd=3)
    indicacionLabel.grid(row=1, column=0, padx=5, pady=5, sticky="e")

    trimestreLabel = Label(tecnologia2, text="Sesión:")
    trimestreLabel.config(font=("comic sans ms", 11), relief="sunken", bd=3)
    trimestreLabel.grid(row=2, column=0, padx=5, pady=5, sticky="e")

    materiasLabel = Label(tecnologia2, text="Asignaturas:")
    materiasLabel.config(font=("comic sans ms", 11), relief="sunken", bd=3)
    materiasLabel.grid(row=3, column=0, padx=5, pady=5, sticky="e")

    lenguaLabel = Label(tecnologia2, text="Lengua y Literaturaa:")
    lenguaLabel.config(font=("comic sans ms", 10), bg="grey85")
    lenguaLabel.grid(row=3, column=1, padx=2, pady=2, sticky="e")

    matesLabel = Label(tecnologia2, text="MatemáticasII:")
    matesLabel.config(font=("comic sans ms", 10), bg="grey85")
    matesLabel.grid(row=4, column=1, padx=2, pady=2, sticky="e")

    historiaLabel = Label(tecnologia2, text="Historia del Mundo Actual:")
    historiaLabel.config(font=("comic sans ms", 10), bg="grey85")
    historiaLabel.grid(row=5, column=1, padx=2, pady=2, sticky="e")

    tecnologiaLabel = Label(tecnologia2, text="Tecnología IndustialII:")
    tecnologiaLabel.config(font=("comic sans ms", 10), bg="grey85")
    tecnologiaLabel.grid(row=6, column=1, padx=2, pady=2, sticky="e")

    electrotecniaLabel = Label(tecnologia2, text="Electrotecnia:")
    electrotecniaLabel.config(font=("comic sans ms", 10), bg="grey85")
    electrotecniaLabel.grid(row=7, column=1, padx=2, pady=2, sticky="e")

    economiaLabel = Label(tecnologia2, text="Economía:")
    economiaLabel.config(font=("comic sans ms", 10), bg="grey85")
    economiaLabel.grid(row=8, column=1, padx=2, pady=2, sticky="e")

    francesLabel = Label(tecnologia2, text="Francés:")
    francesLabel.config(font=("comic sans ms", 10), bg="grey85")
    francesLabel.grid(row=9, column=1, padx=2, pady=2, sticky="e")

    inglesLabel = Label(tecnologia2, text="Inglés:")
    inglesLabel.config(font=("comic sans ms", 10), bg="grey85")
    inglesLabel.grid(row=3, column=3, padx=2, pady=2, sticky="e")

    religionLabel = Label(tecnologia2, text="Religión:")
    religionLabel.config(font=("comic sans ms", 10), bg="grey85")
    religionLabel.grid(row=4, column=3, padx=2, pady=2, sticky="e")

    plasticaLabel = Label(tecnologia2, text="Dibujo Técnico II:")
    plasticaLabel.config(font=("comic sans ms", 10), bg="grey85")
    plasticaLabel.grid(row=5, column=3, padx=2, pady=2, sticky="e")

    educionFisicaLabel = Label(tecnologia2, text="E.Física:")
    educionFisicaLabel.config(font=("comic sans ms", 10), bg="grey85")
    educionFisicaLabel.grid(row=6, column=3, padx=2, pady=2, sticky="e")

    inforLabel = Label(tecnologia2, text="Informática:")
    inforLabel.config(font=("comic sans ms", 10), bg="grey85")
    inforLabel.grid(row=7, column=3, padx=2, pady=2, sticky="e")

    filosofiaLabel = Label(tecnologia2, text="H°de la Filosofía:")
    filosofiaLabel.config(font=("comic sans ms", 10), bg="grey85")
    filosofiaLabel.grid(row=8, column=3, padx=2, pady=2, sticky="e")

    cctmLabel = Label(tecnologia2, text="CNS:")
    cctmLabel.config(font=("comic sans ms", 10), bg="grey85")
    cctmLabel.grid(row=9, column=3, padx=2, pady=2, sticky="e")

    # ------------Entry tecnologia2segundo---------------------------------------
    nombreIdEntry = Entry(tecnologia2, width=32, textvariable = nombreBach22)
    nombreIdEntry.config(font=("comic sans ms", 11))
    nombreIdEntry.grid(row=1, column=1, columnspan=2, padx=1, pady=1, sticky="w")

    Entry(tecnologia2, width=8, font=(9), textvariable = lenguaBach22).grid(row=3, column=2, padx=2, pady=2, sticky="w")  # lengua
    Entry(tecnologia2, width=8, font=(9), textvariable = matesBach22).grid(row=4, column=2, padx=2, pady=2, sticky="w")  # matematicasII
    Entry(tecnologia2, width=8, font=(9), textvariable = historiaBach22).grid(row=5, column=2, padx=2, pady=2, sticky="w")  # historia del mundo actual
    Entry(tecnologia2, width=8, font=(9), textvariable = tecnologiaBach22).grid(row=6, column=2, padx=2, pady=2, sticky="w")  # tecnologiaII
    Entry(tecnologia2, width=8, font=(9), textvariable = electrotecniaBach22).grid(row=7, column=2, padx=2, pady=2, sticky="w")  # electrotecnia
    Entry(tecnologia2, width=8, font=(9), textvariable = economiaBach22).grid(row=8, column=2, padx=2, pady=2, sticky="w")  # Economia
    Entry(tecnologia2, width=8, font=(9), textvariable = francesBach22).grid(row=9, column=2, padx=2, pady=2, sticky="w")  # frances
    Entry(tecnologia2, width=8, font=(9), textvariable = inglesBach22).grid(row=3, column=4, padx=2, pady=2, sticky="w")  # ingles
    Entry(tecnologia2, width=8, font=(9), textvariable = religionBach22).grid(row=4, column=4, padx=2, pady=2, sticky="w")  # religion
    Entry(tecnologia2, width=8, font=(9), textvariable = dibujoBach22).grid(row=5, column=4, padx=2, pady=2, sticky="w")  # dibujo tecnico II
    Entry(tecnologia2, width=8, font=(9), textvariable = efisicaBach22).grid(row=6, column=4, padx=2, pady=2, sticky="w")  # E.fisica
    Entry(tecnologia2, width=8, font=(9), textvariable = informaticaBach22).grid(row=7, column=4, padx=2, pady=2, sticky="w")  # informatica
    Entry(tecnologia2, width=8, font=(9), textvariable = filosofiaBach22).grid(row=8, column=4, padx=2, pady=2, sticky="w")  # Filosifia
    Entry(tecnologia2, width=8, font=(9), textvariable = cnsBach22).grid(row=9, column=4, padx=2, pady=2, sticky="w")  # cns

    # -----radiobuton tecnologia2segundo---------------------------------------
    Radiobutton(tecnologia2, text="Nombre completo", variable=nombreId52, value=1, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2").grid(row=0, column=1, padx=5, pady=5, sticky="w")
    Radiobutton(tecnologia2, text="ID", variable=nombreId52, value=2, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2", ).grid(row=0, column=2, padx=5, pady=5, sticky="w")

    Radiobutton(tecnologia2, text="1°Trimestre", variable=trimestre52, value=1, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2").grid(row=2, column=1, padx=5, pady=5, sticky="w")

    Radiobutton(tecnologia2, text="2°Trimestre", variable=trimestre52, value=2, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2", ).grid(row=2, column=2, padx=5, pady=5, sticky="w")

    Radiobutton(tecnologia2, text="3°Trimestre", variable=trimestre52, value=3, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2", ).grid(row=2, column=3, padx=5, pady=5, sticky="w")

    Radiobutton(tecnologia2, text="Septiembre", variable=trimestre52, value=4, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2", ).grid(row=2, column=4, padx=5, pady=5, sticky="w")

    # ------------botones tecnologia2segundo----------------------------------------------------------------------------------

    Button(tecnologia2, text="Registrar", cursor="hand2", activebackground="#F50743", command = lambda:segundoBachTecnologia(),
           font=("comic sans ms", 11)).grid(row=11, column=0, padx=5, pady=5, sticky="e")

    Button(tecnologia2, text="Verificar", cursor="hand2", activebackground="#F50743", command = lambda:verifi62(),
           font=("comic sans ms", 11)).grid(row=11, column=1, padx=5, pady=5, sticky="w")

    # -----------------pestangna letras2segundos--------------------------------------------------------

    # -------------Label letras2segundos-----------------------------------------------------------------
    nombreIdLabel = Label(letras2, text="Opción de identificación:")
    nombreIdLabel.config(font=("comic sans ms", 11), relief="sunken", bd=3)
    nombreIdLabel.grid(row=0, column=0, padx=5, pady=5, sticky="e")

    indicacionLabel = Label(letras2, text="Nombre completo o ID:")
    indicacionLabel.config(font=("comic sans ms", 11), relief="sunken", bd=3)
    indicacionLabel.grid(row=1, column=0, padx=5, pady=5, sticky="e")

    trimestreLabel = Label(letras2, text="Sesión:")
    trimestreLabel.config(font=("comic sans ms", 11), relief="sunken", bd=3)
    trimestreLabel.grid(row=2, column=0, padx=5, pady=5, sticky="e")

    materiasLabel = Label(letras2, text="Asignaturas:")
    materiasLabel.config(font=("comic sans ms", 11), relief="sunken", bd=3)
    materiasLabel.grid(row=3, column=0, padx=5, pady=5, sticky="e")

    lenguaLabel = Label(letras2, text="Lengua y Literatura:")
    lenguaLabel.config(font=("comic sans ms", 10), bg="grey85")
    lenguaLabel.grid(row=3, column=1, padx=2, pady=2, sticky="e")

    matesapLabel = Label(letras2, text="Matemáticas Aplicadas:")
    matesapLabel.config(font=("comic sans ms", 10), bg="grey85")
    matesapLabel.grid(row=4, column=1, padx=2, pady=2, sticky="e")

    historiaLabel = Label(letras2, text="Historia del Mundo Actual:")
    historiaLabel.config(font=("comic sans ms", 10), bg="grey85")
    historiaLabel.grid(row=5, column=1, padx=2, pady=2, sticky="e")

    historiaarteLabel = Label(letras2, text="Historia del Arte:")
    historiaarteLabel.config(font=("comic sans ms", 10), bg="grey85")
    historiaarteLabel.grid(row=6, column=1, padx=2, pady=2, sticky="e")

    latinLabel = Label(letras2, text="Latín:")
    latinLabel.config(font=("comic sans ms", 10), bg="grey85")
    latinLabel.grid(row=7, column=1, padx=2, pady=2, sticky="e")

    economiaLabel = Label(letras2, text="Economía:")
    economiaLabel.config(font=("comic sans ms", 10), bg="grey85")
    economiaLabel.grid(row=8, column=1, padx=2, pady=2, sticky="e")

    francesLabel = Label(letras2, text="Francés:")
    francesLabel.config(font=("comic sans ms", 10), bg="grey85")
    francesLabel.grid(row=9, column=1, padx=2, pady=2, sticky="e")

    inglesLabel = Label(letras2, text="Inglés:")
    inglesLabel.config(font=("comic sans ms", 10), bg="grey85")
    inglesLabel.grid(row=3, column=3, padx=2, pady=2, sticky="e")

    religionLabel = Label(letras2, text="Religión:")
    religionLabel.config(font=("comic sans ms", 10), bg="grey85")
    religionLabel.grid(row=4, column=3, padx=2, pady=2, sticky="e")

    griegoLabel = Label(letras2, text="Griego:")
    griegoLabel.config(font=("comic sans ms", 10), bg="grey85")
    griegoLabel.grid(row=5, column=3, padx=2, pady=2, sticky="e")

    educionFisicaLabel = Label(letras2, text="E.Física:")
    educionFisicaLabel.config(font=("comic sans ms", 10), bg="grey85")
    educionFisicaLabel.grid(row=6, column=3, padx=2, pady=2, sticky="e")

    inforLabel = Label(letras2, text="Informática:")
    inforLabel.config(font=("comic sans ms", 10), bg="grey85")
    inforLabel.grid(row=7, column=3, padx=2, pady=2, sticky="e")

    filosofiaLabel = Label(letras2, text="H°de la Filosofía:")
    filosofiaLabel.config(font=("comic sans ms", 10), bg="grey85")
    filosofiaLabel.grid(row=8, column=3, padx=2, pady=2, sticky="e")

    cnsLabel = Label(letras2, text="CNS:")
    cnsLabel.config(font=("comic sans ms", 10), bg="grey85")
    cnsLabel.grid(row=9, column=3, padx=2, pady=2, sticky="e")

    # ------------Entry letras2segundo---------------------------------------
    nombreIdEntry = Entry(letras2, width=32, textvariable = nombreBach23)
    nombreIdEntry.config(font=("comic sans ms", 11))
    nombreIdEntry.grid(row=1, column=1, columnspan=2, padx=1, pady=1, sticky="w")

    Entry(letras2, width=8, font=(9), textvariable = lenguaBach23).grid(row=3, column=2, padx=2, pady=2, sticky="w")  # lengua
    Entry(letras2, width=8, font=(9), textvariable = matesBach23).grid(row=4, column=2, padx=2, pady=2, sticky="w")  # matematicasI aplicadas
    Entry(letras2, width=8, font=(9), textvariable = historiaBach23).grid(row=5, column=2, padx=2, pady=2, sticky="w")  # historia del mundo actual
    Entry(letras2, width=8, font=(9), textvariable = historiaarteBach23).grid(row=6, column=2, padx=2, pady=2, sticky="w")  # hostoria del arte
    Entry(letras2, width=8, font=(9), textvariable = latinBach23).grid(row=7, column=2, padx=2, pady=2, sticky="w")  # latin
    Entry(letras2, width=8, font=(9), textvariable = economiaBach23).grid(row=8, column=2, padx=2, pady=2, sticky="w")  # Economia
    Entry(letras2, width=8, font=(9), textvariable = francesBach23).grid(row=9, column=2, padx=2, pady=2, sticky="w")  # frances
    Entry(letras2, width=8, font=(9), textvariable = inglesBach23).grid(row=3, column=4, padx=2, pady=2, sticky="w")  # ingles
    Entry(letras2, width=8, font=(9), textvariable = religionBach23).grid(row=4, column=4, padx=2, pady=2, sticky="w")  # religion
    Entry(letras2, width=8, font=(9), textvariable = griegoBach23).grid(row=5, column=4, padx=2, pady=2, sticky="w")  # griego
    Entry(letras2, width=8, font=(9), textvariable = efisicaBach23).grid(row=6, column=4, padx=2, pady=2, sticky="w")  # E.fisica
    Entry(letras2, width=8, font=(9), textvariable = informaticaBach23).grid(row=7, column=4, padx=2, pady=2, sticky="w")  # informatica
    Entry(letras2, width=8, font=(9), textvariable = filosofiaBach23).grid(row=8, column=4, padx=2, pady=2, sticky="w")  # Filosifia
    Entry(letras2, width=8, font=(9), textvariable = cnsBach23).grid(row=9, column=4, padx=2, pady=2, sticky="w")  # cns

    # -----radiobuton letras2segundo---------------------------------------
    Radiobutton(letras2, text="Nombre completo", variable=nombreId53, value=1, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2").grid(row=0, column=1, padx=5, pady=5, sticky="w")
    Radiobutton(letras2, text="ID", variable=nombreId53, value=2, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2", ).grid(row=0, column=2, padx=5, pady=5, sticky="w")

    Radiobutton(letras2, text="1°Trimestre", variable=trimestre53, value=1, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2").grid(row=2, column=1, padx=5, pady=5, sticky="w")

    Radiobutton(letras2, text="2°Trimestre", variable=trimestre53, value=2, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2", ).grid(row=2, column=2, padx=5, pady=5, sticky="w")

    Radiobutton(letras2, text="3°Trimestre", variable=trimestre53, value=3, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2", ).grid(row=2, column=3, padx=5, pady=5, sticky="w")

    Radiobutton(letras2, text="Septiembre", variable=trimestre53, value=4, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2", ).grid(row=2, column=4, padx=5, pady=5, sticky="w")

    # ------------botones letras2segundo----------------------------------------------------------------------------------

    Button(letras2, text="Registrar", cursor="hand2", activebackground="#F50743", command = lambda:segundoBachletras(),
           font=("comic sans ms", 11)).grid(row=11, column=0, padx=5, pady=5, sticky="e")

    Button(letras2, text="Verificar", cursor="hand2", activebackground="#F50743", command = lambda:verifi63(),
           font=("comic sans ms", 11)).grid(row=11, column=1, padx=5, pady=5, sticky="w")





    # -----------pestagnas unoBach------------------------------------------------------------------------

    # -----------notebook de ramas pestagna de unoBach----------------------------------
    notebookRamas1 = Notebook(unoBach, width=900, height=800)
    notebookRamas1.place(x=0, y=0)

    ciencias1 = Frame(notebookRamas1)
    ciencias1.config(bg="grey85")
    notebookRamas1.add(ciencias1, text="Ciencias")

    tecnologia1 = Frame(notebookRamas1)
    tecnologia1.config(bg="grey85")
    notebookRamas1.add(tecnologia1, text="Tecnología")

    letras1 = Frame(notebookRamas1)
    letras1.config(bg="grey85")
    notebookRamas1.add(letras1, text="Humanidades")

    # -----------------pestangna ciencias1Priemero--------------------------------------------------------

    # -------------Label ciencias1primero-----------------------------------------------------------------
    nombreIdLabel = Label(ciencias1, text="Opción de identificación:")
    nombreIdLabel.config(font=("comic sans ms", 11), relief="sunken", bd=3)
    nombreIdLabel.grid(row=0, column=0, padx=5, pady=5, sticky="e")

    indicacionLabel = Label(ciencias1, text="Nombre completo o ID:")
    indicacionLabel.config(font=("comic sans ms", 11), relief="sunken", bd=3)
    indicacionLabel.grid(row=1, column=0, padx=5, pady=5, sticky="e")

    trimestreLabel = Label(ciencias1, text="Sesión:")
    trimestreLabel.config(font=("comic sans ms", 11), relief="sunken", bd=3)
    trimestreLabel.grid(row=2, column=0, padx=5, pady=5, sticky="e")

    materiasLabel = Label(ciencias1, text="Asignaturas:")
    materiasLabel.config(font=("comic sans ms", 11), relief="sunken", bd=3)
    materiasLabel.grid(row=3, column=0, padx=5, pady=5, sticky="e")

    lenguaLabel = Label(ciencias1, text="Lengua Española:")
    lenguaLabel.config(font=("comic sans ms", 10), bg="grey85")
    lenguaLabel.grid(row=3, column=1, padx=2, pady=2, sticky="e")

    matesLabel = Label(ciencias1, text="MatemáticasI:")
    matesLabel.config(font=("comic sans ms", 10), bg="grey85")
    matesLabel.grid(row=4, column=1, padx=2, pady=2, sticky="e")

    historiaLabel = Label(ciencias1, text="Historia de África y GE:")
    historiaLabel.config(font=("comic sans ms", 10), bg="grey85")
    historiaLabel.grid(row=5, column=1, padx=2, pady=2, sticky="e")

    fygLabel = Label(ciencias1, text="Física y Química:")
    fygLabel.config(font=("comic sans ms", 10), bg="grey85")
    fygLabel.grid(row=6, column=1, padx=2, pady=2, sticky="e")

    bioLabel = Label(ciencias1, text="Biología:")
    bioLabel.config(font=("comic sans ms", 10), bg="grey85")
    bioLabel.grid(row=7, column=1, padx=2, pady=2, sticky="e")

    economiaLabel = Label(ciencias1, text="Economía:")
    economiaLabel.config(font=("comic sans ms", 10), bg="grey85")
    economiaLabel.grid(row=8, column=1, padx=2, pady=2, sticky="e")

    francesLabel = Label(ciencias1, text="Francés:")
    francesLabel.config(font=("comic sans ms", 10), bg="grey85")
    francesLabel.grid(row=9, column=1, padx=2, pady=2, sticky="e")

    inglesLabel = Label(ciencias1, text="Inglés:")
    inglesLabel.config(font=("comic sans ms", 10), bg="grey85")
    inglesLabel.grid(row=3, column=3, padx=2, pady=2, sticky="e")

    religionLabel = Label(ciencias1, text="Religión:")
    religionLabel.config(font=("comic sans ms", 10), bg="grey85")
    religionLabel.grid(row=4, column=3, padx=2, pady=2, sticky="e")

    plasticaLabel = Label(ciencias1, text="Dibujo Técnico I:")
    plasticaLabel.config(font=("comic sans ms", 10), bg="grey85")
    plasticaLabel.grid(row=5, column=3, padx=2, pady=2, sticky="e")

    educionFisicaLabel = Label(ciencias1, text="E.Física:")
    educionFisicaLabel.config(font=("comic sans ms", 10), bg="grey85")
    educionFisicaLabel.grid(row=6, column=3, padx=2, pady=2, sticky="e")

    inforLabel = Label(ciencias1, text="Informática:")
    inforLabel.config(font=("comic sans ms", 10), bg="grey85")
    inforLabel.grid(row=7, column=3, padx=2, pady=2, sticky="e")

    filosofiaLabel = Label(ciencias1, text="Filosofía:")
    filosofiaLabel.config(font=("comic sans ms", 10), bg="grey85")
    filosofiaLabel.grid(row=8, column=3, padx=2, pady=2, sticky="e")

    cctmLabel = Label(ciencias1, text="CC.Tierra y M.A:")
    cctmLabel.config(font=("comic sans ms", 10), bg="grey85")
    cctmLabel.grid(row=9, column=3, padx=2, pady=2, sticky="e")

    # ------------Entry ciencias1primero---------------------------------------
    nombreIdEntry = Entry(ciencias1, width=32, textvariable = nombreBach11)
    nombreIdEntry.config(font=("comic sans ms", 11))
    nombreIdEntry.grid(row=1, column=1, columnspan=2, padx=1, pady=1, sticky="w")

    Entry(ciencias1, width=8, font=(9), textvariable = lenguaBach11).grid(row=3, column=2, padx=2, pady=2, sticky="w")  # lengua
    Entry(ciencias1, width=8, font=(9), textvariable = matesBach11).grid(row=4, column=2, padx=2, pady=2, sticky="w")  # matematicasI
    Entry(ciencias1, width=8, font=(9), textvariable = historiaBach11).grid(row=5, column=2, padx=2, pady=2, sticky="w")  # historia de africa
    Entry(ciencias1, width=8, font=(9), textvariable = fisicayquimicaBach11).grid(row=6, column=2, padx=2, pady=2, sticky="w")  # fisica y quimica
    Entry(ciencias1, width=8, font=(9), textvariable = biologiaBach11).grid(row=7, column=2, padx=2, pady=2, sticky="w")  # Biologia
    Entry(ciencias1, width=8, font=(9), textvariable = economiaBach11).grid(row=8, column=2, padx=2, pady=2, sticky="w")  # Economia
    Entry(ciencias1, width=8, font=(9), textvariable = francesBach11).grid(row=9, column=2, padx=2, pady=2, sticky="w")  # frances
    Entry(ciencias1, width=8, font=(9), textvariable = inglesBach11).grid(row=3, column=4, padx=2, pady=2, sticky="w")  # ingles
    Entry(ciencias1, width=8, font=(9), textvariable = religionBach11).grid(row=4, column=4, padx=2, pady=2, sticky="w")  # religion
    Entry(ciencias1, width=8, font=(9), textvariable = dibujoBach11).grid(row=5, column=4, padx=2, pady=2, sticky="w")  # dibujo tecnico
    Entry(ciencias1, width=8, font=(9), textvariable = efisicaBach11).grid(row=6, column=4, padx=2, pady=2, sticky="w")  # E.fisica
    Entry(ciencias1, width=8, font=(9), textvariable = informaticaBach11).grid(row=7, column=4, padx=2, pady=2, sticky="w")  # informatica
    Entry(ciencias1, width=8, font=(9), textvariable = filosofiaBach11).grid(row=8, column=4, padx=2, pady=2, sticky="w")  # Filosifia
    Entry(ciencias1, width=8, font=(9), textvariable = cctmBach11).grid(row=9, column=4, padx=2, pady=2, sticky="w")  # ciencias de la tierre

    # -----radiobuton ciencias1primero---------------------------------------
    Radiobutton(ciencias1, text="Nombre completo", variable=nombreId41, value=1, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2").grid(row=0, column=1, padx=5, pady=5, sticky="w")
    Radiobutton(ciencias1, text="ID", variable=nombreId41, value=2, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2", ).grid(row=0, column=2, padx=5, pady=5, sticky="w")

    Radiobutton(ciencias1, text="1°Trimestre", variable=trimestre41, value=1, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2").grid(row=2, column=1, padx=5, pady=5, sticky="w")

    Radiobutton(ciencias1, text="2°Trimestre", variable=trimestre41, value=2, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2", ).grid(row=2, column=2, padx=5, pady=5, sticky="w")

    Radiobutton(ciencias1, text="3°Trimestre", variable=trimestre41, value=3, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2", ).grid(row=2, column=3, padx=5, pady=5, sticky="w")

    Radiobutton(ciencias1, text="Septiembre", variable=trimestre41, value=4, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2", ).grid(row=2, column=4, padx=5, pady=5, sticky="w")

    # ------------botones ciencias1primero----------------------------------------------------------------------------------

    Button(ciencias1, text="Registrar", cursor="hand2", activebackground="#F50743", command = lambda:primeroBachCiencias(),
           font=("comic sans ms", 11)).grid(row=11, column=0, padx=5, pady=5, sticky="e")

    Button(ciencias1, text="Verificar", cursor="hand2", activebackground="#F50743", command = lambda:verifi51(),
           font=("comic sans ms", 11)).grid(row=11, column=1, padx=5, pady=5, sticky="w")

    # -----------------pestangna tecnologia1Priemero--------------------------------------------------------

    # -------------Label tecnologia1primero-----------------------------------------------------------------
    nombreIdLabel = Label(tecnologia1, text="Opción de identificación:")
    nombreIdLabel.config(font=("comic sans ms", 11), relief="sunken", bd=3)
    nombreIdLabel.grid(row=0, column=0, padx=5, pady=5, sticky="e")

    indicacionLabel = Label(tecnologia1, text="Nombre completo o ID:")
    indicacionLabel.config(font=("comic sans ms", 11), relief="sunken", bd=3)
    indicacionLabel.grid(row=1, column=0, padx=5, pady=5, sticky="e")

    trimestreLabel = Label(tecnologia1, text="Sesión:")
    trimestreLabel.config(font=("comic sans ms", 11), relief="sunken", bd=3)
    trimestreLabel.grid(row=2, column=0, padx=5, pady=5, sticky="e")

    materiasLabel = Label(tecnologia1, text="Asignaturas:")
    materiasLabel.config(font=("comic sans ms", 11), relief="sunken", bd=3)
    materiasLabel.grid(row=3, column=0, padx=5, pady=5, sticky="e")

    lenguaLabel = Label(tecnologia1, text="Lengua Española:")
    lenguaLabel.config(font=("comic sans ms", 10), bg="grey75")
    lenguaLabel.grid(row=3, column=1, padx=2, pady=2, sticky="e")

    matesLabel = Label(tecnologia1, text="MatemáticasI:")
    matesLabel.config(font=("comic sans ms", 10), bg="grey85")
    matesLabel.grid(row=4, column=1, padx=2, pady=2, sticky="e")

    historiaLabel = Label(tecnologia1, text="Historia de África y GE:")
    historiaLabel.config(font=("comic sans ms", 10), bg="grey85")
    historiaLabel.grid(row=5, column=1, padx=2, pady=2, sticky="e")

    tecnologiaLabel = Label(tecnologia1, text="Tecnología IndustialI:")
    tecnologiaLabel.config(font=("comic sans ms", 10), bg="grey85")
    tecnologiaLabel.grid(row=6, column=1, padx=2, pady=2, sticky="e")

    bioLabel = Label(tecnologia1, text="Biología:")
    bioLabel.config(font=("comic sans ms", 10), bg="grey85")
    bioLabel.grid(row=7, column=1, padx=2, pady=2, sticky="e")

    economiaLabel = Label(tecnologia1, text="Economía:")
    economiaLabel.config(font=("comic sans ms", 10), bg="grey85")
    economiaLabel.grid(row=8, column=1, padx=2, pady=2, sticky="e")

    francesLabel = Label(tecnologia1, text="Francés:")
    francesLabel.config(font=("comic sans ms", 10), bg="grey85")
    francesLabel.grid(row=9, column=1, padx=2, pady=2, sticky="e")

    inglesLabel = Label(tecnologia1, text="Inglés:")
    inglesLabel.config(font=("comic sans ms", 10), bg="grey85")
    inglesLabel.grid(row=3, column=3, padx=2, pady=2, sticky="e")

    religionLabel = Label(tecnologia1, text="Religión:")
    religionLabel.config(font=("comic sans ms", 10), bg="grey85")
    religionLabel.grid(row=4, column=3, padx=2, pady=2, sticky="e")

    plasticaLabel = Label(tecnologia1, text="Dibujo Técnico I:")
    plasticaLabel.config(font=("comic sans ms", 10), bg="grey85")
    plasticaLabel.grid(row=5, column=3, padx=2, pady=2, sticky="e")

    educionFisicaLabel = Label(tecnologia1, text="E.grey85:")
    educionFisicaLabel.config(font=("comic sans ms", 10), bg="grey85")
    educionFisicaLabel.grid(row=6, column=3, padx=2, pady=2, sticky="e")

    inforLabel = Label(tecnologia1, text="Informática:")
    inforLabel.config(font=("comic sans ms", 10), bg="grey85")
    inforLabel.grid(row=7, column=3, padx=2, pady=2, sticky="e")

    filosofiaLabel = Label(tecnologia1, text="Filosofía:")
    filosofiaLabel.config(font=("comic sans ms", 10), bg="grey85")
    filosofiaLabel.grid(row=8, column=3, padx=2, pady=2, sticky="e")

    cctmLabel = Label(tecnologia1, text="CC.Tierra y M.A:")
    cctmLabel.config(font=("comic sans ms", 10), bg="grey85")
    cctmLabel.grid(row=9, column=3, padx=2, pady=2, sticky="e")

    # ------------Entry tecnologia1primero---------------------------------------
    nombreIdEntry = Entry(tecnologia1, width=32, textvariable = nombreBach12)
    nombreIdEntry.config(font=("comic sans ms", 11))
    nombreIdEntry.grid(row=1, column=1, columnspan=2, padx=1, pady=1, sticky="w")

    Entry(tecnologia1, width=8, font=(9), textvariable = lenguaBach12).grid(row=3, column=2, padx=2, pady=2, sticky="w")  # lengua
    Entry(tecnologia1, width=8, font=(9), textvariable = matesBach12).grid(row=4, column=2, padx=2, pady=2, sticky="w")  # matematicasI
    Entry(tecnologia1, width=8, font=(9), textvariable = historiaBach12).grid(row=5, column=2, padx=2, pady=2, sticky="w")  # historia de africa
    Entry(tecnologia1, width=8, font=(9), textvariable = tecnologiaBach12).grid(row=6, column=2, padx=2, pady=2, sticky="w")  # tecnologia
    Entry(tecnologia1, width=8, font=(9), textvariable = biologiaBach12).grid(row=7, column=2, padx=2, pady=2, sticky="w")  # Biologia
    Entry(tecnologia1, width=8, font=(9), textvariable = economiaBach12).grid(row=8, column=2, padx=2, pady=2, sticky="w")  # Economia
    Entry(tecnologia1, width=8, font=(9), textvariable = francesBach12).grid(row=9, column=2, padx=2, pady=2, sticky="w")  # frances
    Entry(tecnologia1, width=8, font=(9), textvariable = inglesBach12).grid(row=3, column=4, padx=2, pady=2, sticky="w")  # ingles
    Entry(tecnologia1, width=8, font=(9), textvariable = religionBach12).grid(row=4, column=4, padx=2, pady=2, sticky="w")  # religion
    Entry(tecnologia1, width=8, font=(9), textvariable = dibujoBach12).grid(row=5, column=4, padx=2, pady=2, sticky="w")  # dibujo tecnico I
    Entry(tecnologia1, width=8, font=(9), textvariable = efisicaBach12).grid(row=6, column=4, padx=2, pady=2, sticky="w")  # E.fisica
    Entry(tecnologia1, width=8, font=(9), textvariable = informaticaBach12).grid(row=7, column=4, padx=2, pady=2, sticky="w")  # informatica
    Entry(tecnologia1, width=8, font=(9), textvariable = filosofiaBach12).grid(row=8, column=4, padx=2, pady=2, sticky="w")  # Filosifia
    Entry(tecnologia1, width=8, font=(9), textvariable = cctmBach12).grid(row=9, column=4, padx=2, pady=2, sticky="w")  # ciencias de la tierra

    # -----radiobuton tecnologia1primero---------------------------------------
    Radiobutton(tecnologia1, text="Nombre completo", variable=nombreId42, value=1, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2").grid(row=0, column=1, padx=5, pady=5, sticky="w")
    Radiobutton(tecnologia1, text="ID", variable=nombreId42, value=2, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2", ).grid(row=0, column=2, padx=5, pady=5, sticky="w")

    Radiobutton(tecnologia1, text="1°Trimestre", variable=trimestre42, value=1, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2").grid(row=2, column=1, padx=5, pady=5, sticky="w")

    Radiobutton(tecnologia1, text="2°Trimestre", variable=trimestre42, value=2, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2", ).grid(row=2, column=2, padx=5, pady=5, sticky="w")

    Radiobutton(tecnologia1, text="3°Trimestre", variable=trimestre42, value=3, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2", ).grid(row=2, column=3, padx=5, pady=5, sticky="w")

    Radiobutton(tecnologia1, text="Septiembre", variable=trimestre42, value=4, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2", ).grid(row=2, column=4, padx=5, pady=5, sticky="w")

    # ------------botones tecnologia1primero----------------------------------------------------------------------------------

    Button(tecnologia1, text="Registrar", cursor="hand2", activebackground="#F50743", command = lambda:primeroBachTecnologia(),
           font=("comic sans ms", 11)).grid(row=11, column=0, padx=5, pady=5, sticky="e")

    Button(tecnologia1, text="Verificar", cursor="hand2", activebackground="#F50743", command = lambda:verifi52(),
           font=("comic sans ms", 11)).grid(row=11, column=1, padx=5, pady=5, sticky="w")

    # -----------------pestangna letras1Priemero--------------------------------------------------------

    # -------------Label letras1primero-----------------------------------------------------------------
    nombreIdLabel = Label(letras1, text="Opción de identificación:")
    nombreIdLabel.config(font=("comic sans ms", 11), relief="sunken", bd=3)
    nombreIdLabel.grid(row=0, column=0, padx=5, pady=5, sticky="e")

    indicacionLabel = Label(letras1, text="Nombre completo o ID:")
    indicacionLabel.config(font=("comic sans ms", 11), relief="sunken", bd=3)
    indicacionLabel.grid(row=1, column=0, padx=5, pady=5, sticky="e")

    trimestreLabel = Label(letras1, text="Sesión:")
    trimestreLabel.config(font=("comic sans ms", 11), relief="sunken", bd=3)
    trimestreLabel.grid(row=2, column=0, padx=5, pady=5, sticky="e")

    materiasLabel = Label(letras1, text="Asignaturas:")
    materiasLabel.config(font=("comic sans ms", 11), relief="sunken", bd=3)
    materiasLabel.grid(row=3, column=0, padx=5, pady=5, sticky="e")

    lenguaLabel = Label(letras1, text="Lengua Española:")
    lenguaLabel.config(font=("comic sans ms", 10), bg="grey85")
    lenguaLabel.grid(row=3, column=1, padx=2, pady=2, sticky="e")

    matesapLabel = Label(letras1, text="Matemáticas Aplicadas:")
    matesapLabel.config(font=("comic sans ms", 10), bg="grey85")
    matesapLabel.grid(row=4, column=1, padx=2, pady=2, sticky="e")

    historiaLabel = Label(letras1, text="Historia de África y GE:")
    historiaLabel.config(font=("comic sans ms", 10), bg="grey85")
    historiaLabel.grid(row=5, column=1, padx=2, pady=2, sticky="e")

    geografiagrandesLabel = Label(letras1, text="Geografía de GG.EE:")
    geografiagrandesLabel.config(font=("comic sans ms", 10), bg="grey85")
    geografiagrandesLabel.grid(row=6, column=1, padx=2, pady=2, sticky="e")

    latinLabel = Label(letras1, text="Latín:")
    latinLabel.config(font=("comic sans ms", 10), bg="grey85")
    latinLabel.grid(row=7, column=1, padx=2, pady=2, sticky="e")

    economiaLabel = Label(letras1, text="Economía:")
    economiaLabel.config(font=("comic sans ms", 10), bg="grey85")
    economiaLabel.grid(row=8, column=1, padx=2, pady=2, sticky="e")

    francesLabel = Label(letras1, text="Francés:")
    francesLabel.config(font=("comic sans ms", 10), bg="grey85")
    francesLabel.grid(row=9, column=1, padx=2, pady=2, sticky="e")

    inglesLabel = Label(letras1, text="Inglés:")
    inglesLabel.config(font=("comic sans ms", 10), bg="grey85")
    inglesLabel.grid(row=3, column=3, padx=2, pady=2, sticky="e")

    religionLabel = Label(letras1, text="Religión:")
    religionLabel.config(font=("comic sans ms", 10), bg="grey85")
    religionLabel.grid(row=4, column=3, padx=2, pady=2, sticky="e")

    griegoLabel = Label(letras1, text="Griego:")
    griegoLabel.config(font=("comic sans ms", 10), bg="grey85")
    griegoLabel.grid(row=5, column=3, padx=2, pady=2, sticky="e")

    educionFisicaLabel = Label(letras1, text="E.Física:")
    educionFisicaLabel.config(font=("comic sans ms", 10), bg="grey85")
    educionFisicaLabel.grid(row=6, column=3, padx=2, pady=2, sticky="e")

    inforLabel = Label(letras1, text="Informática:")
    inforLabel.config(font=("comic sans ms", 10), bg="grey85")
    inforLabel.grid(row=7, column=3, padx=2, pady=2, sticky="e")

    filosofiaLabel = Label(letras1, text="Filosofía:")
    filosofiaLabel.config(font=("comic sans ms", 10), bg="grey85")
    filosofiaLabel.grid(row=8, column=3, padx=2, pady=2, sticky="e")

    cctmLabel = Label(letras1, text="CC.Tierra y M.A:")
    cctmLabel.config(font=("comic sans ms", 10), bg="grey85")
    cctmLabel.grid(row=9, column=3, padx=2, pady=2, sticky="e")

    # ------------Entry letras1primero---------------------------------------
    nombreIdEntry = Entry(letras1, width=32, textvariable = nombreBach13)
    nombreIdEntry.config(font=("comic sans ms", 11))
    nombreIdEntry.grid(row=1, column=1, columnspan=2, padx=1, pady=1, sticky="w")

    Entry(letras1, width=8, font=(9), textvariable = lenguaBach13).grid(row=3, column=2, padx=2, pady=2, sticky="w")  # lengua
    Entry(letras1, width=8, font=(9), textvariable = matesBach13).grid(row=4, column=2, padx=2, pady=2, sticky="w")  # matematicasI aplicadas
    Entry(letras1, width=8, font=(9), textvariable = historiaBach13).grid(row=5, column=2, padx=2, pady=2, sticky="w")  # historia de africa
    Entry(letras1, width=8, font=(9), textvariable = geografiaBach13).grid(row=6, column=2, padx=2, pady=2, sticky="w")  # geogragia de grandes epacios
    Entry(letras1, width=8, font=(9), textvariable = latinBach13).grid(row=7, column=2, padx=2, pady=2, sticky="w")  # latin
    Entry(letras1, width=8, font=(9), textvariable = economiaBach13).grid(row=8, column=2, padx=2, pady=2, sticky="w")  # Economia
    Entry(letras1, width=8, font=(9), textvariable = francesBach13).grid(row=9, column=2, padx=2, pady=2, sticky="w")  # frances
    Entry(letras1, width=8, font=(9), textvariable = inglesBach13).grid(row=3, column=4, padx=2, pady=2, sticky="w")  # ingles
    Entry(letras1, width=8, font=(9), textvariable = religionBach13).grid(row=4, column=4, padx=2, pady=2, sticky="w")  # religion
    Entry(letras1, width=8, font=(9), textvariable = griegoBach13).grid(row=5, column=4, padx=2, pady=2, sticky="w")  # griego
    Entry(letras1, width=8, font=(9), textvariable = efisicaBach13).grid(row=6, column=4, padx=2, pady=2, sticky="w")  # E.fisica
    Entry(letras1, width=8, font=(9), textvariable = informaticaBach13).grid(row=7, column=4, padx=2, pady=2, sticky="w")  # informatica
    Entry(letras1, width=8, font=(9), textvariable = filosofiaBach13).grid(row=8, column=4, padx=2, pady=2, sticky="w")  # Filosifia
    Entry(letras1, width=8, font=(9), textvariable = cctmBach13).grid(row=9, column=4, padx=2, pady=2, sticky="w")  # ciencias de la tierre

    # -----radiobuton letras1primero---------------------------------------
    Radiobutton(letras1, text="Nombre completo", variable=nombreId43, value=1, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2").grid(row=0, column=1, padx=5, pady=5, sticky="w")
    Radiobutton(letras1, text="ID", variable=nombreId43, value=2, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2", ).grid(row=0, column=2, padx=5, pady=5, sticky="w")

    Radiobutton(letras1, text="1°Trimestre", variable=trimestre43, value=1, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2").grid(row=2, column=1, padx=5, pady=5, sticky="w")

    Radiobutton(letras1, text="2°Trimestre", variable=trimestre43, value=2, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2", ).grid(row=2, column=2, padx=5, pady=5, sticky="w")

    Radiobutton(letras1, text="3°Trimestre", variable=trimestre43, value=3, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2", ).grid(row=2, column=3, padx=5, pady=5, sticky="w")

    Radiobutton(letras1, text="Septiembre", variable=trimestre43, value=4, bg="grey85",
                font=("comic sans ms", 11), cursor="hand2", ).grid(row=2, column=4, padx=5, pady=5, sticky="w")

    # ------------botones letras1primero----------------------------------------------------------------------------------

    Button(letras1, text="Registrar", cursor="hand2", activebackground="#F50743", command = lambda:primeroBachLetras(),
           font=("comic sans ms", 11)).grid(row=11, column=0, padx=5, pady=5, sticky="e")

    Button(letras1, text="Verificar", cursor="hand2", activebackground="#F50743", command = lambda:verifi53(),
           font=("comic sans ms", 11)).grid(row=11, column=1, padx=5, pady=5, sticky="w")


    #----------funciones de insercion de las notas---------------------------------------------------------------


    def unoEsba():
        """
        esta funcion permite actualizar las tablas de primero de esba atraves del nombre del alumno y el ID
        ValueError
        :return:
        """
        try:
            try:

                connexion = sqlite3.connect(nameBD.nomBD())
                cursor = connexion.cursor()
                if nombreId.get() == 1:
                    if trimestre.get() == 1:
                        if lenguaEsba1.get():
                            cursor.execute(f"update primero_esba_uno set lengua = '{float(lenguaEsba1.get())}' "
                                           f"where  nombre = '{nombreEsba1.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesEsba1.get():
                            cursor.execute(f"update primero_esba_uno set matematicas = '{float(matesEsba1.get())}' "
                                           f"where  nombre = '{nombreEsba1.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if geografiaEsba1.get():
                            cursor.execute(f"update primero_esba_uno set geografia = '{float(geografiaEsba1.get())}' "
                                           f"where  nombre = '{nombreEsba1.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if naturalesEsba1.get():
                            cursor.execute(f"update primero_esba_uno set cn = '{float(naturalesEsba1.get())}' "
                                           f"where  nombre = '{nombreEsba1.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesEsba1.get():
                            cursor.execute(f"update primero_esba_uno set frances = '{float(francesEsba1.get())}' "
                                           f"where  nombre = '{nombreEsba1.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesEsba1.get():
                            cursor.execute(f"update primero_esba_uno set ingles = '{float(inglesEsba1.get())}' "
                                           f"where  nombre = '{nombreEsba1.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionEsba1.get():
                            cursor.execute(f"update primero_esba_uno set religion = '{float(religionEsba1.get())}' "
                                           f"where  nombre = '{nombreEsba1.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if plasticaEsba1.get():
                            cursor.execute(f"update primero_esba_uno set plastica = '{float(plasticaEsba1.get())}' "
                                           f"where  nombre = '{nombreEsba1.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaEsba1.get():
                            cursor.execute(f"update primero_esba_uno set ef = '{float(efisicaEsba1.get())}' "
                                           f"where  nombre = '{nombreEsba1.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaEsba1.get():
                            cursor.execute(f"update primero_esba_uno set informatica = '{float(informaticaEsba1.get())}' "
                                           f"where  nombre = '{nombreEsba1.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass


                    elif trimestre.get() == 2:
                        if lenguaEsba1.get():
                            cursor.execute(f"update primero_esba_dos set lengua = '{float(lenguaEsba1.get())}' "
                                           f"where  nombre = '{nombreEsba1.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesEsba1.get():
                            cursor.execute(f"update primero_esba_dos set matematicas = '{float(matesEsba1.get())}' "
                                           f"where  nombre = '{nombreEsba1.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if geografiaEsba1.get():
                            cursor.execute(f"update primero_esba_dos set geografia = '{float(geografiaEsba1.get())}' "
                                           f"where  nombre = '{nombreEsba1.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if naturalesEsba1.get():
                            cursor.execute(f"update primero_esba_dos set cn = '{float(naturalesEsba1.get())}' "
                                           f"where  nombre = '{nombreEsba1.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesEsba1.get():
                            cursor.execute(f"update primero_esba_dos set frances = '{float(francesEsba1.get())}' "
                                           f"where  nombre = '{nombreEsba1.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesEsba1.get():
                            cursor.execute(f"update primero_esba_dos set ingles = '{float(inglesEsba1.get())}' "
                                           f"where  nombre = '{nombreEsba1.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionEsba1.get():
                            cursor.execute(f"update primero_esba_dos set religion = '{float(religionEsba1.get())}' "
                                           f"where  nombre = '{nombreEsba1.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if plasticaEsba1.get():
                            cursor.execute(f"update primero_esba_dos set plastica = '{float(plasticaEsba1.get())}' "
                                           f"where  nombre = '{nombreEsba1.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaEsba1.get():
                            cursor.execute(f"update primero_esba_dos set ef = '{float(efisicaEsba1.get())}' "
                                           f"where  nombre = '{nombreEsba1.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaEsba1.get():
                            cursor.execute(f"update primero_esba_dos set informatica = '{float(informaticaEsba1.get())}' "
                                           f"where  nombre = '{nombreEsba1.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass


                    elif trimestre.get() == 3:
                        if lenguaEsba1.get():
                            cursor.execute(f"update primero_esba_tres set lengua = '{float(lenguaEsba1.get())}' "
                                           f"where  nombre = '{nombreEsba1.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesEsba1.get():
                            cursor.execute(f"update primero_esba_tres set matematicas = '{float(matesEsba1.get())}' "
                                           f"where  nombre = '{nombreEsba1.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if geografiaEsba1.get():
                            cursor.execute(f"update primero_esba_tres set geografia = '{float(geografiaEsba1.get())}' "
                                           f"where  nombre = '{nombreEsba1.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if naturalesEsba1.get():
                            cursor.execute(f"update primero_esba_tres set cn = '{float(naturalesEsba1.get())}' "
                                           f"where  nombre = '{nombreEsba1.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesEsba1.get():
                            cursor.execute(f"update primero_esba_tres set frances = '{float(francesEsba1.get())}' "
                                           f"where  nombre = '{nombreEsba1.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesEsba1.get():
                            cursor.execute(f"update primero_esba_tres set ingles = '{float(inglesEsba1.get())}' "
                                           f"where  nombre = '{nombreEsba1.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionEsba1.get():
                            cursor.execute(f"update primero_esba_tres set religion = '{float(religionEsba1.get())}' "
                                           f"where  nombre = '{nombreEsba1.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if plasticaEsba1.get():
                            cursor.execute(f"update primero_esba_tres set plastica = '{float(plasticaEsba1.get())}' "
                                           f"where  nombre = '{nombreEsba1.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaEsba1.get():
                            cursor.execute(f"update primero_esba_tres set ef = '{float(efisicaEsba1.get())}' "
                                           f"where  nombre = '{nombreEsba1.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaEsba1.get():
                            cursor.execute(f"update primero_esba_tres set informatica = '{float(informaticaEsba1.get())}' "
                                           f"where  nombre = '{nombreEsba1.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass


                    elif trimestre.get() == 4:
                        if lenguaEsba1.get():
                            cursor.execute(f"update primero_esba_septiembre set lengua = '{float(lenguaEsba1.get())}' "
                                           f"where  nombre = '{nombreEsba1.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesEsba1.get():
                            cursor.execute(f"update primero_esba_septiembre set matematicas = '{float(matesEsba1.get())}' "
                                           f"where  nombre = '{nombreEsba1.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if geografiaEsba1.get():
                            cursor.execute(f"update primero_esba_septiembre set geografia = '{float(geografiaEsba1.get())}' "
                                           f"where  nombre = '{nombreEsba1.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if naturalesEsba1.get():
                            cursor.execute(f"update primero_esba_septiembre set cn = '{float(naturalesEsba1.get())}' "
                                           f"where  nombre = '{nombreEsba1.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesEsba1.get():
                            cursor.execute(f"update primero_esba_septiembre set frances = '{float(francesEsba1.get())}' "
                                           f"where  nombre = '{nombreEsba1.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesEsba1.get():
                            cursor.execute(f"update primero_esba_septiembre set ingles = '{float(inglesEsba1.get())}' "
                                           f"where  nombre = '{nombreEsba1.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionEsba1.get():
                            cursor.execute(f"update primero_esba_septiembre set religion = '{float(religionEsba1.get())}' "
                                           f"where  nombre = '{nombreEsba1.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if plasticaEsba1.get():
                            cursor.execute(f"update primero_esba_septiembre set plastica = '{float(plasticaEsba1.get())}' "
                                           f"where  nombre = '{nombreEsba1.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaEsba1.get():
                            cursor.execute(f"update primero_esba_septiembre set ef = '{float(efisicaEsba1.get())}' "
                                           f"where  nombre = '{nombreEsba1.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaEsba1.get():
                            cursor.execute(f"update primero_esba_septiembre set informatica = '{float(informaticaEsba1.get())}' "
                                           f"where  nombre = '{nombreEsba1.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass


                    #--------actualizar la tabla de junio----------------------------
                    cursor.execute(f"select lengua, matematicas, geografia, cn, frances, ingles, religion,"
                                   f"plastica, ef, informatica from primero_esba_uno where nombre = '{nombreEsba1.get().upper()}'")
                    stock = cursor.fetchall()

                    cursor.execute(f"select lengua, matematicas, geografia, cn, frances, ingles, religion,"
                                   f"plastica, ef, informatica from primero_esba_dos where nombre = '{nombreEsba1.get().upper()}'")
                    stock1 = cursor.fetchall()

                    cursor.execute(f"select lengua, matematicas, geografia, cn, frances, ingles, religion,"
                                   f"plastica, ef, informatica from primero_esba_tres where nombre = '{nombreEsba1.get().upper()}'")
                    stock2 = cursor.fetchall()

                    lengua = (stock[0][0] + stock1[0][0] + stock2[0][0]) / 3
                    matematicas = (stock[0][1] + stock1[0][1] + stock2[0][1]) / 3
                    geografia = (stock[0][2] + stock1[0][1] + stock2[0][1]) / 3
                    cn = (stock[0][3] + stock1[0][3] + stock2[0][3]) / 3
                    frances = (stock[0][4] + stock1[0][4] + stock2[0][4]) / 3
                    ingles = (stock[0][5] + stock1[0][5] + stock2[0][5]) / 3
                    religion = (stock[0][6] + stock1[0][6] + stock2[0][6]) / 3
                    plastica = (stock[0][7] + stock1[0][7] + stock2[0][7]) / 3
                    efisica = (stock[0][8] + stock1[0][8] + stock2[0][8]) / 3
                    informatica = (stock[0][9] + stock1[0][9] + stock2[0][9]) / 3

                    cursor.execute(f"update primero_esba_junio set lengua = '{lengua}' "
                                   f"where  nombre = '{nombreEsba1.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_esba_junio set matematicas = '{matematicas}' "
                                   f"where  nombre = '{nombreEsba1.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_esba_junio set geografia = '{geografia}' "
                                   f"where  nombre = '{nombreEsba1.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_esba_junio set cn = '{cn}' "
                                   f"where  nombre = '{nombreEsba1.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_esba_junio set frances = '{frances}' "
                                   f"where  nombre = '{nombreEsba1.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_esba_junio set ingles = '{ingles}' "
                                   f"where  nombre = '{nombreEsba1.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_esba_junio set religion = '{religion}' "
                                   f"where  nombre = '{nombreEsba1.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_esba_junio set plastica = '{plastica}' "
                                   f"where  nombre = '{nombreEsba1.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_esba_junio set ef = '{efisica}' "
                                   f"where  nombre = '{nombreEsba1.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_esba_junio set informatica = '{informatica}' "
                                   f"where  nombre = '{nombreEsba1.get().upper()}' ")
                    connexion.commit()

                    lenguaEsba1.set("")
                    matesEsba1.set("")
                    geografiaEsba1.set("")
                    naturalesEsba1.set("")
                    francesEsba1.set("")
                    inglesEsba1.set("")
                    religionEsba1.set("")
                    plasticaEsba1.set("")
                    efisicaEsba1.set("")
                    informaticaEsba1.set("")




                elif nombreId.get() == 2:
                    if trimestre.get() == 1:
                        if lenguaEsba1.get():
                            cursor.execute(f"update primero_esba_uno set lengua = '{float(lenguaEsba1.get())}' "
                                           f"where  id = '{int(nombreEsba1.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesEsba1.get():
                            cursor.execute(f"update primero_esba_uno set matematicas = '{float(matesEsba1.get())}' "
                                           f"where  id = '{int(nombreEsba1.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if geografiaEsba1.get():
                            cursor.execute(f"update primero_esba_uno set geografia = '{float(geografiaEsba1.get())}' "
                                           f"where  id = '{int(nombreEsba1.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if naturalesEsba1.get():
                            cursor.execute(f"update primero_esba_uno set cn = '{float(naturalesEsba1.get())}' "
                                           f"where  id = '{int(nombreEsba1.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesEsba1.get():
                            cursor.execute(f"update primero_esba_uno set frances = '{float(francesEsba1.get())}' "
                                           f"where  id = '{int(nombreEsba1.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesEsba1.get():
                            cursor.execute(f"update primero_esba_uno set ingles = '{float(inglesEsba1.get())}' "
                                           f"where  id = '{int(nombreEsba1.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionEsba1.get():
                            cursor.execute(f"update primero_esba_uno set religion = '{float(religionEsba1.get())}' "
                                           f"where  id = '{int(nombreEsba1.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if plasticaEsba1.get():
                            cursor.execute(f"update primero_esba_uno set plastica = '{float(plasticaEsba1.get())}' "
                                           f"where  id = '{int(nombreEsba1.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaEsba1.get():
                            cursor.execute(f"update primero_esba_uno set ef = '{float(efisicaEsba1.get())}' "
                                           f"where  id = '{int(nombreEsba1.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaEsba1.get():
                            cursor.execute(f"update primero_esba_uno set informatica = '{float(informaticaEsba1.get())}' "
                                           f"where  id = '{int(nombreEsba1.get())}' ")
                            connexion.commit()
                        else:
                            pass


                    elif trimestre.get() == 2:
                        if lenguaEsba1.get():
                            cursor.execute(f"update primero_esba_dos set lengua = '{float(lenguaEsba1.get())}' "
                                           f"where  id = '{int(nombreEsba1.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesEsba1.get():
                            cursor.execute(f"update primero_esba_dos set matematicas = '{float(matesEsba1.get())}' "
                                           f"where  id = '{int(nombreEsba1.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if geografiaEsba1.get():
                            cursor.execute(f"update primero_esba_dos set geografia = '{float(geografiaEsba1.get())}' "
                                           f"where  id = '{int(nombreEsba1.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if naturalesEsba1.get():
                            cursor.execute(f"update primero_esba_dos set cn = '{float(naturalesEsba1.get())}' "
                                           f"where  id = '{int(nombreEsba1.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesEsba1.get():
                            cursor.execute(f"update primero_esba_dos set frances = '{float(francesEsba1.get())}' "
                                           f"where  id = '{int(nombreEsba1.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesEsba1.get():
                            cursor.execute(f"update primero_esba_dos set ingles = '{float(inglesEsba1.get())}' "
                                           f"where  id = '{int(nombreEsba1.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionEsba1.get():
                            cursor.execute(f"update primero_esba_dos set religion = '{float(religionEsba1.get())}' "
                                           f"where  id = '{int(nombreEsba1.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if plasticaEsba1.get():
                            cursor.execute(f"update primero_esba_dos set plastica = '{float(plasticaEsba1.get())}' "
                                           f"where  id = '{int(nombreEsba1.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaEsba1.get():
                            cursor.execute(f"update primero_esba_dos set ef = '{float(efisicaEsba1.get())}' "
                                           f"where  id = '{int(nombreEsba1.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaEsba1.get():
                            cursor.execute(f"update primero_esba_dos set informatica = '{float(informaticaEsba1.get())}' "
                                           f"where  id = '{int(nombreEsba1.get())}' ")
                            connexion.commit()
                        else:
                            pass


                    elif trimestre.get() == 3:
                        if lenguaEsba1.get():
                            cursor.execute(f"update primero_esba_tres set lengua = '{float(lenguaEsba1.get())}' "
                                           f"where  id = '{int(nombreEsba1.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesEsba1.get():
                            cursor.execute(f"update primero_esba_tres set matematicas = '{float(matesEsba1.get())}' "
                                           f"where  id = '{int(nombreEsba1.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if geografiaEsba1.get():
                            cursor.execute(f"update primero_esba_tres set geografia = '{float(geografiaEsba1.get())}' "
                                           f"where  id = '{int(nombreEsba1.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if naturalesEsba1.get():
                            cursor.execute(f"update primero_esba_tres set cn = '{float(naturalesEsba1.get())}' "
                                           f"where  id = '{int(nombreEsba1.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesEsba1.get():
                            cursor.execute(f"update primero_esba_tres set frances = '{float(francesEsba1.get())}' "
                                           f"where  id = '{int(nombreEsba1.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesEsba1.get():
                            cursor.execute(f"update primero_esba_tres set ingles = '{float(inglesEsba1.get())}' "
                                           f"where  id = '{int(nombreEsba1.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionEsba1.get():
                            cursor.execute(f"update primero_esba_tres set religion = '{float(religionEsba1.get())}' "
                                           f"where  id = '{int(nombreEsba1.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if plasticaEsba1.get():
                            cursor.execute(f"update primero_esba_tres set plastica = '{float(plasticaEsba1.get())}' "
                                           f"where  id = '{int(nombreEsba1.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaEsba1.get():
                            cursor.execute(f"update primero_esba_tres set ef = '{float(efisicaEsba1.get())}' "
                                           f"where  id = '{int(nombreEsba1.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaEsba1.get():
                            cursor.execute(f"update primero_esba_tres set informatica = '{float(informaticaEsba1.get())}' "
                                           f"where  id = '{int(nombreEsba1.get())}' ")
                            connexion.commit()
                        else:
                            pass


                    elif trimestre.get() == 4:
                        if lenguaEsba1.get():
                            cursor.execute(f"update primero_esba_septiembre set lengua = '{float(lenguaEsba1.get())}' "
                                           f"where  id = '{int(nombreEsba1.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesEsba1.get():
                            cursor.execute(f"update primero_esba_septiembre set matematicas = '{float(matesEsba1.get())}' "
                                           f"where  id = '{int(nombreEsba1.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if geografiaEsba1.get():
                            cursor.execute(f"update primero_esba_septiembre set geografia = '{float(geografiaEsba1.get())}' "
                                           f"where  id = '{int(nombreEsba1.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if naturalesEsba1.get():
                            cursor.execute(f"update primero_esba_septiembre set cn = '{float(naturalesEsba1.get())}' "
                                           f"where  id = '{int(nombreEsba1.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesEsba1.get():
                            cursor.execute(f"update primero_esba_septiembre set frances = '{float(francesEsba1.get())}' "
                                           f"where  id = '{int(nombreEsba1.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesEsba1.get():
                            cursor.execute(f"update primero_esba_septiembre set ingles = '{float(inglesEsba1.get())}' "
                                           f"where  id = '{int(nombreEsba1.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionEsba1.get():
                            cursor.execute(f"update primero_esba_septiembre set religion = '{float(religionEsba1.get())}' "
                                           f"where  id = '{int(nombreEsba1.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if plasticaEsba1.get():
                            cursor.execute(f"update primero_esba_septiembre set plastica = '{float(plasticaEsba1.get())}' "
                                           f"where  id = '{int(nombreEsba1.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaEsba1.get():
                            cursor.execute(f"update primero_esba_septiembre set ef = '{float(efisicaEsba1.get())}' "
                                           f"where  id = '{int(nombreEsba1.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaEsba1.get():
                            cursor.execute(
                                f"update primero_esba_septiembre set informatica = '{float(informaticaEsba1.get())}' "
                                f"where  id = '{int(nombreEsba1.get())}' ")
                            connexion.commit()
                        else:
                            pass

                    cursor.execute(f"select lengua, matematicas, geografia, cn, frances, ingles, religion,"
                                   f"plastica, ef, informatica from primero_esba_uno where id = '{int(nombreEsba1.get())}'")
                    stock = cursor.fetchall()

                    cursor.execute(f"select lengua, matematicas, geografia, cn, frances, ingles, religion,"
                                   f"plastica, ef, informatica from primero_esba_dos where id = '{int(nombreEsba1.get())}'")
                    stock1 = cursor.fetchall()

                    cursor.execute(f"select lengua, matematicas, geografia, cn, frances, ingles, religion,"
                                   f"plastica, ef, informatica from primero_esba_tres where id = '{int(nombreEsba1.get())}'")
                    stock2 = cursor.fetchall()

                    lengua = (stock[0][0] + stock1[0][0] + stock2[0][0]) / 3
                    matematicas = (stock[0][1] + stock1[0][1] + stock2[0][1]) / 3
                    geografia = (stock[0][2] + stock1[0][1] + stock2[0][1]) / 3
                    cn = (stock[0][3] + stock1[0][3] + stock2[0][3]) / 3
                    frances = (stock[0][4] + stock1[0][4] + stock2[0][4]) / 3
                    ingles = (stock[0][5] + stock1[0][5] + stock2[0][5]) / 3
                    religion = (stock[0][6] + stock1[0][6] + stock2[0][6]) / 3
                    plastica = (stock[0][7] + stock1[0][7] + stock2[0][7]) / 3
                    efisica = (stock[0][8] + stock1[0][8] + stock2[0][8]) / 3
                    informatica = (stock[0][9] + stock1[0][9] + stock2[0][9]) / 3

                    cursor.execute(f"update primero_esba_junio set lengua = '{lengua}' "
                                   f"where  id = '{int(nombreEsba1.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_esba_junio set matematicas = '{matematicas}' "
                                   f"where  id = '{int(nombreEsba1.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_esba_junio set geografia = '{geografia}' "
                                   f"where  id = '{int(nombreEsba1.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_esba_junio set cn = '{cn}' "
                                   f"where  id = '{int(nombreEsba1.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_esba_junio set frances = '{frances}' "
                                   f"where  id = '{int(nombreEsba1.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_esba_junio set ingles = '{ingles}' "
                                   f"where  id = '{int(nombreEsba1.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_esba_junio set religion = '{religion}' "
                                   f"where  id = '{int(nombreEsba1.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_esba_junio set plastica = '{plastica}' "
                                   f"where  id = '{int(nombreEsba1.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_esba_junio set ef = '{efisica}' "
                                   f"where  id = '{int(nombreEsba1.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_esba_junio set informatica = '{informatica}' "
                                   f"where  id = '{int(nombreEsba1.get())}' ")
                    connexion.commit()

                    lenguaEsba1.set("")
                    matesEsba1.set("")
                    geografiaEsba1.set("")
                    naturalesEsba1.set("")
                    francesEsba1.set("")
                    inglesEsba1.set("")
                    religionEsba1.set("")
                    plasticaEsba1.set("")
                    efisicaEsba1.set("")
                    informaticaEsba1.set("")

                else:
                    pass
                connexion.close()
            except ValueError:
                pass

        except IndexError:
            pass





    def dosEsba():
        """
        esta funcion permite actualizar las tablas de segundo de esba atraves del nombre del alumno y el ID
        :return:
        """
        try:
            try:


                connexion = sqlite3.connect(nameBD.nomBD())
                cursor = connexion.cursor()
                if nombreId1.get() == 1:
                    if trimestre1.get() == 1:
                        if lenguaEsba2.get():
                            cursor.execute(f"update segundo_esba_uno set lengua = '{float(lenguaEsba2.get())}' "
                                           f"where  nombre = '{nombreEsba2.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesEsba2.get():
                            cursor.execute(f"update segundo_esba_uno set matematicas = '{float(matesEsba2.get())}' "
                                           f"where  nombre = '{nombreEsba2.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if geografiaEsba2.get():
                            cursor.execute(f"update segundo_esba_uno set geografia = '{float(geografiaEsba2.get())}' "
                                           f"where  nombre = '{nombreEsba2.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if naturalesEsba2.get():
                            cursor.execute(f"update segundo_esba_uno set cn = '{float(naturalesEsba2.get())}' "
                                           f"where  nombre = '{nombreEsba2.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesEsba2.get():
                            cursor.execute(f"update segundo_esba_uno set frances = '{float(francesEsba2.get())}' "
                                           f"where  nombre = '{nombreEsba2.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesEsba2.get():
                            cursor.execute(f"update segundo_esba_uno set ingles = '{float(inglesEsba2.get())}' "
                                           f"where  nombre = '{nombreEsba2.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionEsba2.get():
                            cursor.execute(f"update segundo_esba_uno set religion = '{float(religionEsba2.get())}' "
                                           f"where  nombre = '{nombreEsba2.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if plasticaEsba2.get():
                            cursor.execute(f"update segundo_esba_uno set plastica = '{float(plasticaEsba2.get())}' "
                                           f"where  nombre = '{nombreEsba2.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaEsba2.get():
                            cursor.execute(f"update segundo_esba_uno set ef = '{float(efisicaEsba2.get())}' "
                                           f"where  nombre = '{nombreEsba2.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaEsba2.get():
                            cursor.execute(f"update segundo_esba_uno set informatica = '{float(informaticaEsba2.get())}' "
                                           f"where  nombre = '{nombreEsba2.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass


                    elif trimestre1.get() == 2:
                        if lenguaEsba2.get():
                            cursor.execute(f"update segundo_esba_dos set lengua = '{float(lenguaEsba2.get())}' "
                                           f"where  nombre = '{nombreEsba2.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesEsba2.get():
                            cursor.execute(f"update segundo_esba_dos set matematicas = '{float(matesEsba2.get())}' "
                                           f"where  nombre = '{nombreEsba2.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if geografiaEsba2.get():
                            cursor.execute(f"update segundo_esba_dos set geografia = '{float(geografiaEsba2.get())}' "
                                           f"where  nombre = '{nombreEsba2.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if naturalesEsba2.get():
                            cursor.execute(f"update segundo_esba_dos set cn = '{float(naturalesEsba2.get())}' "
                                           f"where  nombre = '{nombreEsba2.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesEsba2.get():
                            cursor.execute(f"update segundo_esba_dos set frances = '{float(francesEsba2.get())}' "
                                           f"where  nombre = '{nombreEsba2.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesEsba2.get():
                            cursor.execute(f"update segundo_esba_dos set ingles = '{float(inglesEsba2.get())}' "
                                           f"where  nombre = '{nombreEsba2.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionEsba2.get():
                            cursor.execute(f"update segundo_esba_dos set religion = '{float(religionEsba2.get())}' "
                                           f"where  nombre = '{nombreEsba2.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if plasticaEsba2.get():
                            cursor.execute(f"update segundo_esba_dos set plastica = '{float(plasticaEsba2.get())}' "
                                           f"where  nombre = '{nombreEsba2.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaEsba2.get():
                            cursor.execute(f"update segundo_esba_dos set ef = '{float(efisicaEsba2.get())}' "
                                           f"where  nombre = '{nombreEsba2.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaEsba2.get():
                            cursor.execute(f"update segundo_esba_dos set informatica = '{float(informaticaEsba2.get())}' "
                                           f"where  nombre = '{nombreEsba2.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass


                    elif trimestre1.get() == 3:
                        if lenguaEsba2.get():
                            cursor.execute(f"update segundo_esba_tres set lengua = '{float(lenguaEsba2.get())}' "
                                           f"where  nombre = '{nombreEsba2.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesEsba2.get():
                            cursor.execute(f"update segundo_esba_tres set matematicas = '{float(matesEsba2.get())}' "
                                           f"where  nombre = '{nombreEsba2.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if geografiaEsba2.get():
                            cursor.execute(f"update segundo_esba_tres set geografia = '{float(geografiaEsba2.get())}' "
                                           f"where  nombre = '{nombreEsba1.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if naturalesEsba2.get():
                            cursor.execute(f"update segundo_esba_tres set cn = '{float(naturalesEsba2.get())}' "
                                           f"where  nombre = '{nombreEsba2.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesEsba2.get():
                            cursor.execute(f"update segundo_esba_tres set frances = '{float(francesEsba2.get())}' "
                                           f"where  nombre = '{nombreEsba2.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesEsba2.get():
                            cursor.execute(f"update segundo_esba_tres set ingles = '{float(inglesEsba2.get())}' "
                                           f"where  nombre = '{nombreEsba2.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionEsba2.get():
                            cursor.execute(f"update segundo_esba_tres set religion = '{float(religionEsba2.get())}' "
                                           f"where  nombre = '{nombreEsba2.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if plasticaEsba2.get():
                            cursor.execute(f"update segundo_esba_tres set plastica = '{float(plasticaEsba2.get())}' "
                                           f"where  nombre = '{nombreEsba2.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaEsba2.get():
                            cursor.execute(f"update segundo_esba_tres set ef = '{float(efisicaEsba2.get())}' "
                                           f"where  nombre = '{nombreEsba2.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaEsba2.get():
                            cursor.execute(f"update segundo_esba_tres set informatica = '{float(informaticaEsba2.get())}' "
                                           f"where  nombre = '{nombreEsba2.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass


                    elif trimestre1.get() == 4:
                        if lenguaEsba2.get():
                            cursor.execute(f"update segundo_esba_septiembre set lengua = '{float(lenguaEsba2.get())}' "
                                           f"where  nombre = '{nombreEsba2.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesEsba2.get():
                            cursor.execute(f"update segundo_esba_septiembre set matematicas = '{float(matesEsba2.get())}' "
                                           f"where  nombre = '{nombreEsba2.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if geografiaEsba2.get():
                            cursor.execute(f"update segundo_esba_septiembre set geografia = '{float(geografiaEsba2.get())}' "
                                           f"where  nombre = '{nombreEsba2.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if naturalesEsba2.get():
                            cursor.execute(f"update segundo_esba_septiembre set cn = '{float(naturalesEsba2.get())}' "
                                           f"where  nombre = '{nombreEsba2.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesEsba2.get():
                            cursor.execute(f"update segundo_esba_septiembre set frances = '{float(francesEsba2.get())}' "
                                           f"where  nombre = '{nombreEsba2.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesEsba2.get():
                            cursor.execute(f"update segundo_esba_septiembre set ingles = '{float(inglesEsba2.get())}' "
                                           f"where  nombre = '{nombreEsba2.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionEsba2.get():
                            cursor.execute(f"update segundo_esba_septiembre set religion = '{float(religionEsba2.get())}' "
                                           f"where  nombre = '{nombreEsba2.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if plasticaEsba2.get():
                            cursor.execute(f"update segundo_esba_septiembre set plastica = '{float(plasticaEsba2.get())}' "
                                           f"where  nombre = '{nombreEsba2.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaEsba2.get():
                            cursor.execute(f"update segundo_esba_septiembre set ef = '{float(efisicaEsba2.get())}' "
                                           f"where  nombre = '{nombreEsba2.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaEsba2.get():
                            cursor.execute(
                                f"update segundo_esba_septiembre set informatica = '{float(informaticaEsba2.get())}' "
                                f"where  nombre = '{nombreEsba2.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                    # --------actualizar la tabla de junio----------------------------
                    cursor.execute(f"select lengua, matematicas, geografia, cn, frances, ingles, religion,"
                                   f"plastica, ef, informatica from segundo_esba_uno where nombre = '{nombreEsba2.get().upper()}'")
                    stock = cursor.fetchall()

                    cursor.execute(f"select lengua, matematicas, geografia, cn, frances, ingles, religion,"
                                   f"plastica, ef, informatica from segundo_esba_dos where nombre = '{nombreEsba2.get().upper()}'")
                    stock1 = cursor.fetchall()

                    cursor.execute(f"select lengua, matematicas, geografia, cn, frances, ingles, religion,"
                                   f"plastica, ef, informatica from segundo_esba_tres where nombre = '{nombreEsba2.get().upper()}'")
                    stock2 = cursor.fetchall()

                    lengua = (stock[0][0] + stock1[0][0] + stock2[0][0]) / 3
                    matematicas = (stock[0][1] + stock1[0][1] + stock2[0][1]) / 3
                    geografia = (stock[0][2] + stock1[0][1] + stock2[0][1]) / 3
                    cn = (stock[0][3] + stock1[0][3] + stock2[0][3]) / 3
                    frances = (stock[0][4] + stock1[0][4] + stock2[0][4]) / 3
                    ingles = (stock[0][5] + stock1[0][5] + stock2[0][5]) / 3
                    religion = (stock[0][6] + stock1[0][6] + stock2[0][6]) / 3
                    plastica = (stock[0][7] + stock1[0][7] + stock2[0][7]) / 3
                    efisica = (stock[0][8] + stock1[0][8] + stock2[0][8]) / 3
                    informatica = (stock[0][9] + stock1[0][9] + stock2[0][9]) / 3

                    cursor.execute(f"update segundo_esba_junio set lengua = '{lengua}' "
                                   f"where  nombre = '{nombreEsba2.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_esba_junio set matematicas = '{matematicas}' "
                                   f"where  nombre = '{nombreEsba2.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_esba_junio set geografia = '{geografia}' "
                                   f"where  nombre = '{nombreEsba2.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_esba_junio set cn = '{cn}' "
                                   f"where  nombre = '{nombreEsba2.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_esba_junio set frances = '{frances}' "
                                   f"where  nombre = '{nombreEsba2.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_esba_junio set ingles = '{ingles}' "
                                   f"where  nombre = '{nombreEsba2.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_esba_junio set religion = '{religion}' "
                                   f"where  nombre = '{nombreEsba2.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_esba_junio set plastica = '{plastica}' "
                                   f"where  nombre = '{nombreEsba2.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_esba_junio set ef = '{efisica}' "
                                   f"where  nombre = '{nombreEsba2.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_esba_junio set informatica = '{informatica}' "
                                   f"where  nombre = '{nombreEsba2.get().upper()}' ")
                    connexion.commit()

                    lenguaEsba2.set("")
                    matesEsba2.set("")
                    geografiaEsba2.set("")
                    naturalesEsba2.set("")
                    francesEsba2.set("")
                    inglesEsba2.set("")
                    religionEsba2.set("")
                    plasticaEsba2.set("")
                    efisicaEsba2.set("")
                    informaticaEsba2.set("")




                elif nombreId1.get() == 2:
                    if trimestre1.get() == 1:
                        if lenguaEsba2.get():
                            cursor.execute(f"update segundo_esba_uno set lengua = '{float(lenguaEsba2.get())}' "
                                           f"where  id = '{int(nombreEsba2.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesEsba2.get():
                            cursor.execute(f"update segundo_esba_uno set matematicas = '{float(matesEsba2.get())}' "
                                           f"where  id = '{int(nombreEsba2.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if geografiaEsba2.get():
                            cursor.execute(f"update segundo_esba_uno set geografia = '{float(geografiaEsba2.get())}' "
                                           f"where  id = '{int(nombreEsba2.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if naturalesEsba2.get():
                            cursor.execute(f"update segundo_esba_uno set cn = '{float(naturalesEsba2.get())}' "
                                           f"where  id = '{int(nombreEsba2.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesEsba2.get():
                            cursor.execute(f"update segundo_esba_uno set frances = '{float(francesEsba2.get())}' "
                                           f"where  id = '{int(nombreEsba2.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesEsba2.get():
                            cursor.execute(f"update segundo_esba_uno set ingles = '{float(inglesEsba2.get())}' "
                                           f"where  id = '{int(nombreEsba2.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionEsba2.get():
                            cursor.execute(f"update segundo_esba_uno set religion = '{float(religionEsba2.get())}' "
                                           f"where  id = '{int(nombreEsba2.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if plasticaEsba2.get():
                            cursor.execute(f"update segundo_esba_uno set plastica = '{float(plasticaEsba2.get())}' "
                                           f"where  id = '{int(nombreEsba2.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaEsba2.get():
                            cursor.execute(f"update segundo_esba_uno set ef = '{float(efisicaEsba2.get())}' "
                                           f"where  id = '{int(nombreEsba2.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaEsba2.get():
                            cursor.execute(f"update segundo_esba_uno set informatica = '{float(informaticaEsba2.get())}' "
                                           f"where  id = '{int(nombreEsba2.get())}' ")
                            connexion.commit()
                        else:
                            pass


                    elif trimestre1.get() == 2:
                        if lenguaEsba2.get():
                            cursor.execute(f"update segundo_esba_dos set lengua = '{float(lenguaEsba2.get())}' "
                                           f"where  id = '{int(nombreEsba2.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesEsba2.get():
                            cursor.execute(f"update segundo_esba_dos set matematicas = '{float(matesEsba2.get())}' "
                                           f"where  id = '{int(nombreEsba2.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if geografiaEsba2.get():
                            cursor.execute(f"update segundo_esba_dos set geografia = '{float(geografiaEsba2.get())}' "
                                           f"where  id = '{int(nombreEsba2.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if naturalesEsba2.get():
                            cursor.execute(f"update segundo_esba_dos set cn = '{float(naturalesEsba2.get())}' "
                                           f"where  id = '{int(nombreEsba2.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesEsba2.get():
                            cursor.execute(f"update segundo_esba_dos set frances = '{float(francesEsba2.get())}' "
                                           f"where  id = '{int(nombreEsba2.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesEsba2.get():
                            cursor.execute(f"update segundo_esba_dos set ingles = '{float(inglesEsba2.get())}' "
                                           f"where  id = '{int(nombreEsba2.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionEsba2.get():
                            cursor.execute(f"update segundo_esba_dos set religion = '{float(religionEsba2.get())}' "
                                           f"where  id = '{int(nombreEsba2.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if plasticaEsba2.get():
                            cursor.execute(f"update segundo_esba_dos set plastica = '{float(plasticaEsba2.get())}' "
                                           f"where  id = '{int(nombreEsba2.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaEsba2.get():
                            cursor.execute(f"update segundo_esba_dos set ef = '{float(efisicaEsba2.get())}' "
                                           f"where  id = '{int(nombreEsba2.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaEsba2.get():
                            cursor.execute(f"update segundo_esba_dos set informatica = '{float(informaticaEsba2.get())}' "
                                           f"where  id = '{int(nombreEsba2.get())}' ")
                            connexion.commit()
                        else:
                            pass


                    elif trimestre1.get() == 3:
                        if lenguaEsba2.get():
                            cursor.execute(f"update segundo_esba_tres set lengua = '{float(lenguaEsba2.get())}' "
                                           f"where  id = '{int(nombreEsba2.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesEsba2.get():
                            cursor.execute(f"update segundo_esba_tres set matematicas = '{float(matesEsba2.get())}' "
                                           f"where  id = '{int(nombreEsba2.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if geografiaEsba2.get():
                            cursor.execute(f"update segundo_esba_tres set geografia = '{float(geografiaEsba2.get())}' "
                                           f"where  id = '{int(nombreEsba2.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if naturalesEsba2.get():
                            cursor.execute(f"update segundo_esba_tres set cn = '{float(naturalesEsba2.get())}' "
                                           f"where  id = '{int(nombreEsba2.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesEsba2.get():
                            cursor.execute(f"update segundo_esba_tres set frances = '{float(francesEsba2.get())}' "
                                           f"where  id = '{int(nombreEsba2.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesEsba2.get():
                            cursor.execute(f"update segundo_esba_tres set ingles = '{float(inglesEsba2.get())}' "
                                           f"where  id = '{int(nombreEsba2.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionEsba2.get():
                            cursor.execute(f"update segundo_esba_tres set religion = '{float(religionEsba2.get())}' "
                                           f"where  id = '{int(nombreEsba2.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if plasticaEsba2.get():
                            cursor.execute(f"update segundo_esba_tres set plastica = '{float(plasticaEsba2.get())}' "
                                           f"where  id = '{int(nombreEsba2.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaEsba2.get():
                            cursor.execute(f"update segundo_esba_tres set ef = '{float(efisicaEsba2.get())}' "
                                           f"where  id = '{int(nombreEsba2.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaEsba2.get():
                            cursor.execute(f"update segundo_esba_tres set informatica = '{float(informaticaEsba2.get())}' "
                                           f"where  id = '{int(nombreEsba2.get())}' ")
                            connexion.commit()
                        else:
                            pass


                    elif trimestre1.get() == 4:
                        if lenguaEsba2.get():
                            cursor.execute(f"update segundo_esba_septiembre set lengua = '{float(lenguaEsba2.get())}' "
                                           f"where  id = '{int(nombreEsba2.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesEsba2.get():
                            cursor.execute(f"update segundo_esba_septiembre set matematicas = '{float(matesEsba2.get())}' "
                                           f"where  id = '{int(nombreEsba2.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if geografiaEsba2.get():
                            cursor.execute(f"update segundo_esba_septiembre set geografia = '{float(geografiaEsba2.get())}' "
                                           f"where  id = '{int(nombreEsba2.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if naturalesEsba2.get():
                            cursor.execute(f"update segundo_esba_septiembre set cn = '{float(naturalesEsba2.get())}' "
                                           f"where  id = '{int(nombreEsba2.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesEsba2.get():
                            cursor.execute(f"update segundo_esba_septiembre set frances = '{float(francesEsba2.get())}' "
                                           f"where  id = '{int(nombreEsba2.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesEsba2.get():
                            cursor.execute(f"update segundo_esba_septiembre set ingles = '{float(inglesEsba2.get())}' "
                                           f"where  id = '{int(nombreEsba2.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionEsba2.get():
                            cursor.execute(f"update segundo_esba_septiembre set religion = '{float(religionEsba2.get())}' "
                                           f"where  id = '{int(nombreEsba2.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if plasticaEsba2.get():
                            cursor.execute(f"update segundo_esba_septiembre set plastica = '{float(plasticaEsba2.get())}' "
                                           f"where  id = '{int(nombreEsba2.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaEsba2.get():
                            cursor.execute(f"update segundo_esba_septiembre set ef = '{float(efisicaEsba2.get())}' "
                                           f"where  id = '{int(nombreEsba2.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaEsba2.get():
                            cursor.execute(
                                f"update segundo_esba_septiembre set informatica = '{float(informaticaEsba2.get())}' "
                                f"where  id = '{int(nombreEsba1.get())}' ")
                            connexion.commit()
                        else:
                            pass

                    cursor.execute(f"select lengua, matematicas, geografia, cn, frances, ingles, religion,"
                                   f"plastica, ef, informatica from segundo_esba_uno where id = '{int(nombreEsba2.get())}'")
                    stock = cursor.fetchall()

                    cursor.execute(f"select lengua, matematicas, geografia, cn, frances, ingles, religion,"
                                   f"plastica, ef, informatica from segundo_esba_dos where id = '{int(nombreEsba2.get())}'")
                    stock1 = cursor.fetchall()

                    cursor.execute(f"select lengua, matematicas, geografia, cn, frances, ingles, religion,"
                                   f"plastica, ef, informatica from segundo_esba_tres where id = '{int(nombreEsba2.get())}'")
                    stock2 = cursor.fetchall()

                    lengua = (stock[0][0] + stock1[0][0] + stock2[0][0]) / 3
                    matematicas = (stock[0][1] + stock1[0][1] + stock2[0][1]) / 3
                    geografia = (stock[0][2] + stock1[0][1] + stock2[0][1]) / 3
                    cn = (stock[0][3] + stock1[0][3] + stock2[0][3]) / 3
                    frances = (stock[0][4] + stock1[0][4] + stock2[0][4]) / 3
                    ingles = (stock[0][5] + stock1[0][5] + stock2[0][5]) / 3
                    religion = (stock[0][6] + stock1[0][6] + stock2[0][6]) / 3
                    plastica = (stock[0][7] + stock1[0][7] + stock2[0][7]) / 3
                    efisica = (stock[0][8] + stock1[0][8] + stock2[0][8]) / 3
                    informatica = (stock[0][9] + stock1[0][9] + stock2[0][9]) / 3

                    cursor.execute(f"update segundo_esba_junio set lengua = '{lengua}' "
                                   f"where  id = '{int(nombreEsba2.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_esba_junio set matematicas = '{matematicas}' "
                                   f"where  id = '{int(nombreEsba2.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_esba_junio set geografia = '{geografia}' "
                                   f"where  id = '{int(nombreEsba2.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_esba_junio set cn = '{cn}' "
                                   f"where  id = '{int(nombreEsba2.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_esba_junio set frances = '{frances}' "
                                   f"where  id = '{int(nombreEsba2.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_esba_junio set ingles = '{ingles}' "
                                   f"where  id = '{int(nombreEsba2.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_esba_junio set religion = '{religion}' "
                                   f"where  id = '{int(nombreEsba2.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_esba_junio set plastica = '{plastica}' "
                                   f"where  id = '{int(nombreEsba2.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_esba_junio set ef = '{efisica}' "
                                   f"where  id = '{int(nombreEsba2.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_esba_junio set informatica = '{informatica}' "
                                   f"where  id = '{int(nombreEsba2.get())}' ")
                    connexion.commit()

                    lenguaEsba2.set("")
                    matesEsba2.set("")
                    geografiaEsba2.set("")
                    naturalesEsba2.set("")
                    francesEsba2.set("")
                    inglesEsba2.set("")
                    religionEsba2.set("")
                    plasticaEsba2.set("")
                    efisicaEsba2.set("")
                    informaticaEsba2.set("")

                else:
                    pass
                connexion.close()

            except ValueError:
                pass

        except IndexError:
            pass


    def tresEsba():
        """
        esta funcion permite actualizar las notas de las tablas de tercero esba atraves del nombre o el id
        :return:
        """
        try:

            try:
                    connexion = sqlite3.connect(nameBD.nomBD())
                    cursor = connexion.cursor()
                    if nombreId2.get() == 1:
                        if trimestre2.get() == 1:
                            if lenguaEsba3.get():
                                cursor.execute(f"update tercero_esba_uno set lengua = '{float(lenguaEsba3.get())}' "
                                               f"where  nombre = '{nombreEsba3.get().upper()}' ")
                                connexion.commit()
                            else:
                                pass

                            if matesEsba3.get():
                                cursor.execute(f"update tercero_esba_uno set matematicas = '{float(matesEsba3.get())}' "
                                               f"where  nombre = '{nombreEsba3.get().upper()}' ")
                                connexion.commit()
                            else:
                                pass

                            if historiaEsba3.get():
                                cursor.execute(f"update tercero_esba_uno set historia = '{float(historiaEsba3.get())}' "
                                               f"where  nombre = '{nombreEsba3.get().upper()}' ")
                                connexion.commit()
                            else:
                                pass

                            if fisicayquimicaEsba3.get():
                                cursor.execute(f"update tercero_esba_uno set fyq = '{float(fisicayquimicaEsba3.get())}' "
                                               f"where  nombre = '{nombreEsba3.get().upper()}' ")
                                connexion.commit()
                            else:
                                pass

                            if biologiaygeologiaEsba3.get():
                                cursor.execute(f"update tercero_esba_uno set byg = '{float(biologiaygeologiaEsba3.get())}' "
                                               f"where  nombre = '{nombreEsba3.get().upper()}' ")
                                connexion.commit()
                            else:
                                pass

                            if francesEsba3.get():
                                cursor.execute(f"update tercero_esba_uno set frances = '{float(francesEsba3.get())}' "
                                               f"where  nombre = '{nombreEsba3.get().upper()}' ")
                                connexion.commit()
                            else:
                                pass

                            if inglesEsba3.get():
                                cursor.execute(f"update tercero_esba_uno set ingles = '{float(inglesEsba3.get())}' "
                                               f"where  nombre = '{nombreEsba3.get().upper()}' ")
                                connexion.commit()
                            else:
                                pass

                            if religionEsba3.get():
                                cursor.execute(f"update tercero_esba_uno set religion = '{float(religionEsba3.get())}' "
                                               f"where  nombre = '{nombreEsba3.get().upper()}' ")
                                connexion.commit()
                            else:
                                pass

                            if plasticaEsba3.get():
                                cursor.execute(f"update tercero_esba_uno set plastica = '{float(plasticaEsba3.get())}' "
                                               f"where  nombre = '{nombreEsba3.get().upper()}' ")
                                connexion.commit()
                            else:
                                pass

                            if efisicaEsba3.get():
                                cursor.execute(f"update tercero_esba_uno set ef = '{float(efisicaEsba3.get())}' "
                                               f"where  nombre = '{nombreEsba3.get().upper()}' ")
                                connexion.commit()
                            else:
                                pass

                            if informaticaEsba3.get():
                                cursor.execute(
                                    f"update tercero_esba_uno set informatica = '{float(informaticaEsba3.get())}' "
                                    f"where  nombre = '{nombreEsba3.get().upper()}' ")
                                connexion.commit()
                            else:
                                pass

                            if tecnologiaEsba3.get():
                                cursor.execute(
                                    f"update tercero_esba_uno set tecnologia = '{float(tecnologiaEsba3.get())}' "
                                    f"where  nombre = '{nombreEsba3.get().upper()}' ")
                                connexion.commit()
                            else:
                                pass



                        elif trimestre2.get() == 2:
                            if lenguaEsba3.get():
                                cursor.execute(f"update tercero_esba_dos set lengua = '{float(lenguaEsba3.get())}' "
                                               f"where  nombre = '{nombreEsba3.get().upper()}' ")
                                connexion.commit()
                            else:
                                pass

                            if matesEsba3.get():
                                cursor.execute(f"update tercero_esba_dos set matematicas = '{float(matesEsba3.get())}' "
                                               f"where  nombre = '{nombreEsba3.get().upper()}' ")
                                connexion.commit()
                            else:
                                pass

                            if historiaEsba3.get():
                                cursor.execute(f"update tercero_esba_dos set historia = '{float(historiaEsba3.get())}' "
                                               f"where  nombre = '{nombreEsba3.get().upper()}' ")
                                connexion.commit()
                            else:
                                pass

                            if fisicayquimicaEsba3.get():
                                cursor.execute(f"update tercero_esba_dos set fyq = '{float(fisicayquimicaEsba3.get())}' "
                                               f"where  nombre = '{nombreEsba3.get().upper()}' ")
                                connexion.commit()
                            else:
                                pass

                            if biologiaygeologiaEsba3.get():
                                cursor.execute(f"update tercero_esba_dos set byg = '{float(biologiaygeologiaEsba3.get())}' "
                                               f"where  nombre = '{nombreEsba3.get().upper()}' ")
                                connexion.commit()
                            else:
                                pass

                            if francesEsba3.get():
                                cursor.execute(f"update tercero_esba_dos set frances = '{float(francesEsba3.get())}' "
                                               f"where  nombre = '{nombreEsba3.get().upper()}' ")
                                connexion.commit()
                            else:
                                pass

                            if inglesEsba3.get():
                                cursor.execute(f"update tercero_esba_dos set ingles = '{float(inglesEsba3.get())}' "
                                               f"where  nombre = '{nombreEsba3.get().upper()}' ")
                                connexion.commit()
                            else:
                                pass

                            if religionEsba3.get():
                                cursor.execute(f"update tercero_esba_dos set religion = '{float(religionEsba3.get())}' "
                                               f"where  nombre = '{nombreEsba3.get().upper()}' ")
                                connexion.commit()
                            else:
                                pass

                            if plasticaEsba3.get():
                                cursor.execute(f"update tercero_esba_dos set plastica = '{float(plasticaEsba3.get())}' "
                                               f"where  nombre = '{nombreEsba3.get().upper()}' ")
                                connexion.commit()
                            else:
                                pass

                            if efisicaEsba3.get():
                                cursor.execute(f"update tercero_esba_dos set ef = '{float(efisicaEsba3.get())}' "
                                               f"where  nombre = '{nombreEsba3.get().upper()}' ")
                                connexion.commit()
                            else:
                                pass

                            if informaticaEsba3.get():
                                cursor.execute(
                                    f"update tercero_esba_dos set informatica = '{float(informaticaEsba3.get())}' "
                                    f"where  nombre = '{nombreEsba3.get().upper()}' ")
                                connexion.commit()
                            else:
                                pass

                            if tecnologiaEsba3.get():
                                cursor.execute(
                                    f"update tercero_esba_dos set tecnologia = '{float(tecnologiaEsba3.get())}' "
                                    f"where  nombre = '{nombreEsba3.get().upper()}' ")
                                connexion.commit()
                            else:
                                pass


                        elif trimestre2.get() == 3:
                            if lenguaEsba3.get():
                                cursor.execute(f"update tercero_esba_tres set lengua = '{float(lenguaEsba3.get())}' "
                                               f"where  nombre = '{nombreEsba3.get().upper()}' ")
                                connexion.commit()
                            else:
                                pass

                            if matesEsba3.get():
                                cursor.execute(f"update tercero_esba_tres set matematicas = '{float(matesEsba3.get())}' "
                                               f"where  nombre = '{nombreEsba3.get().upper()}' ")
                                connexion.commit()
                            else:
                                pass

                            if historiaEsba3.get():
                                cursor.execute(f"update tercero_esba_tres set historia = '{float(historiaEsba3.get())}' "
                                               f"where  nombre = '{nombreEsba3.get().upper()}' ")
                                connexion.commit()
                            else:
                                pass

                            if fisicayquimicaEsba3.get():
                                cursor.execute(f"update tercero_esba_tres set fyq = '{float(fisicayquimicaEsba3.get())}' "
                                               f"where  nombre = '{nombreEsba3.get().upper()}' ")
                                connexion.commit()
                            else:
                                pass

                            if biologiaygeologiaEsba3.get():
                                cursor.execute(f"update tercero_esba_tres set byg = '{float(biologiaygeologiaEsba3.get())}' "
                                               f"where  nombre = '{nombreEsba3.get().upper()}' ")
                                connexion.commit()
                            else:
                                pass

                            if francesEsba3.get():
                                cursor.execute(f"update tercero_esba_tres set frances = '{float(francesEsba3.get())}' "
                                               f"where  nombre = '{nombreEsba3.get().upper()}' ")
                                connexion.commit()
                            else:
                                pass

                            if inglesEsba3.get():
                                cursor.execute(f"update tercero_esba_tres set ingles = '{float(inglesEsba3.get())}' "
                                               f"where  nombre = '{nombreEsba3.get().upper()}' ")
                                connexion.commit()
                            else:
                                pass

                            if religionEsba3.get():
                                cursor.execute(f"update tercero_esba_tres set religion = '{float(religionEsba3.get())}' "
                                               f"where  nombre = '{nombreEsba3.get().upper()}' ")
                                connexion.commit()
                            else:
                                pass

                            if plasticaEsba3.get():
                                cursor.execute(f"update tercero_esba_tres set plastica = '{float(plasticaEsba3.get())}' "
                                               f"where  nombre = '{nombreEsba3.get().upper()}' ")
                                connexion.commit()
                            else:
                                pass

                            if efisicaEsba3.get():
                                cursor.execute(f"update tercero_esba_tres set ef = '{float(efisicaEsba3.get())}' "
                                               f"where  nombre = '{nombreEsba3.get().upper()}' ")
                                connexion.commit()
                            else:
                                pass

                            if informaticaEsba3.get():
                                cursor.execute(
                                    f"update tercero_esba_tres set informatica = '{float(informaticaEsba3.get())}' "
                                    f"where  nombre = '{nombreEsba3.get().upper()}' ")
                                connexion.commit()
                            else:
                                pass

                            if tecnologiaEsba3.get():
                                cursor.execute(
                                    f"update tercero_esba_tres set tecnologia = '{float(tecnologiaEsba3.get())}' "
                                    f"where  nombre = '{nombreEsba3.get().upper()}' ")
                                connexion.commit()
                            else:
                                pass


                        elif trimestre2.get() == 4:
                            if lenguaEsba3.get():
                                cursor.execute(f"update tercero_esba_septiembre set lengua = '{float(lenguaEsba3.get())}' "
                                               f"where  nombre = '{nombreEsba3.get().upper()}' ")
                                connexion.commit()
                            else:
                                pass

                            if matesEsba3.get():
                                cursor.execute(f"update tercero_esba_septiembre set matematicas = '{float(matesEsba3.get())}' "
                                               f"where  nombre = '{nombreEsba3.get().upper()}' ")
                                connexion.commit()
                            else:
                                pass

                            if historiaEsba3.get():
                                cursor.execute(f"update tercero_esba_septiembre set historia = '{float(historiaEsba3.get())}' "
                                               f"where  nombre = '{nombreEsba3.get().upper()}' ")
                                connexion.commit()
                            else:
                                pass

                            if fisicayquimicaEsba3.get():
                                cursor.execute(f"update tercero_esba_septiembre set fyq = '{float(fisicayquimicaEsba3.get())}' "
                                               f"where  nombre = '{nombreEsba3.get().upper()}' ")
                                connexion.commit()
                            else:
                                pass

                            if biologiaygeologiaEsba3.get():
                                cursor.execute(
                                    f"update tercero_esba_septiembre set byg = '{float(biologiaygeologiaEsba3.get())}' "
                                    f"where  nombre = '{nombreEsba3.get().upper()}' ")
                                connexion.commit()
                            else:
                                pass

                            if francesEsba3.get():
                                cursor.execute(f"update tercero_esba_septiembre set frances = '{float(francesEsba3.get())}' "
                                               f"where  nombre = '{nombreEsba3.get().upper()}' ")
                                connexion.commit()
                            else:
                                pass

                            if inglesEsba3.get():
                                cursor.execute(f"update tercero_esba_septiembre set ingles = '{float(inglesEsba3.get())}' "
                                               f"where  nombre = '{nombreEsba3.get().upper()}' ")
                                connexion.commit()
                            else:
                                pass

                            if religionEsba3.get():
                                cursor.execute(f"update tercero_esba_septiembre set religion = '{float(religionEsba3.get())}' "
                                               f"where  nombre = '{nombreEsba3.get().upper()}' ")
                                connexion.commit()
                            else:
                                pass

                            if plasticaEsba3.get():
                                cursor.execute(f"update tercero_esba_septiembre set plastica = '{float(plasticaEsba3.get())}' "
                                               f"where  nombre = '{nombreEsba3.get().upper()}' ")
                                connexion.commit()
                            else:
                                pass

                            if efisicaEsba3.get():
                                cursor.execute(f"update tercero_esba_septiembre set ef = '{float(efisicaEsba3.get())}' "
                                               f"where  nombre = '{nombreEsba3.get().upper()}' ")
                                connexion.commit()
                            else:
                                pass

                            if informaticaEsba3.get():
                                cursor.execute(
                                    f"update tercero_esba_septiembre set informatica = '{float(informaticaEsba3.get())}' "
                                    f"where  nombre = '{nombreEsba3.get().upper()}' ")
                                connexion.commit()
                            else:
                                pass

                            if tecnologiaEsba3.get():
                                cursor.execute(
                                    f"update tercero_esba_septiembre set tecnologia = '{float(tecnologiaEsba3.get())}' "
                                    f"where  nombre = '{nombreEsba3.get().upper()}' ")
                                connexion.commit()
                            else:
                                pass

                        # --------actualizar la tabla de junio----------------------------
                        cursor.execute(f"select lengua, matematicas, historia, fyq, byg, tecnologia, frances, ingles, religion,"
                                       f"plastica, ef, informatica from tercero_esba_uno where nombre = '{nombreEsba3.get().upper()}'")
                        stock = cursor.fetchall()

                        cursor.execute(f"select lengua, matematicas, historia, fyq, byg, tecnologia, frances, ingles, religion,"
                                       f"plastica, ef, informatica from tercero_esba_dos where nombre = '{nombreEsba3.get().upper()}'")
                        stock1 = cursor.fetchall()

                        cursor.execute(f"select lengua, matematicas, historia, fyq, byg, tecnologia, frances, ingles, religion,"
                                       f"plastica, ef, informatica from tercero_esba_tres where nombre = '{nombreEsba3.get().upper()}'")
                        stock2 = cursor.fetchall()

                        lengua = (stock[0][0] + stock1[0][0] + stock2[0][0]) / 3
                        matematicas = (stock[0][1] + stock1[0][1] + stock2[0][1]) / 3
                        historia = (stock[0][2] + stock1[0][1] + stock2[0][1]) / 3
                        fyq = (stock[0][3] + stock1[0][3] + stock2[0][3]) / 3
                        byg = (stock[0][4] + stock1[0][4] + stock2[0][4]) / 3
                        tecnologia = (stock[0][5] + stock1[0][5] + stock2[0][5]) / 3
                        frances = (stock[0][6] + stock1[0][6] + stock2[0][6]) / 3
                        ingles = (stock[0][7] + stock1[0][7] + stock2[0][7]) / 3
                        religion = (stock[0][8] + stock1[0][8] + stock2[0][8]) / 3
                        plastica = (stock[0][9] + stock1[0][9] + stock2[0][9]) / 3
                        ef = (stock[0][10] + stock1[0][10] + stock2[0][10]) / 3
                        informatica = (stock[0][11] + stock1[0][11] + stock2[0][11]) / 3

                        cursor.execute(f"update tercero_esba_junio set lengua = '{lengua}' "
                                       f"where  nombre = '{nombreEsba3.get().upper()}' ")
                        connexion.commit()

                        cursor.execute(f"update tercero_esba_junio set matematicas = '{matematicas}' "
                                       f"where  nombre = '{nombreEsba3.get().upper()}' ")
                        connexion.commit()

                        cursor.execute(f"update tercero_esba_junio set historia = '{historia}' "
                                       f"where  nombre = '{nombreEsba3.get().upper()}' ")
                        connexion.commit()

                        cursor.execute(f"update tercero_esba_junio set fyq = '{fyq}' "
                                       f"where  nombre = '{nombreEsba3.get().upper()}' ")
                        connexion.commit()

                        cursor.execute(f"update tercero_esba_junio set byg = '{byg}' "
                                       f"where  nombre = '{nombreEsba3.get().upper()}' ")
                        connexion.commit()

                        cursor.execute(f"update tercero_esba_junio set tecnologia = '{tecnologia}' "
                                       f"where  nombre = '{nombreEsba3.get().upper()}' ")
                        connexion.commit()

                        cursor.execute(f"update tercero_esba_junio set frances = '{frances}' "
                                       f"where  nombre = '{nombreEsba3.get().upper()}' ")
                        connexion.commit()

                        cursor.execute(f"update tercero_esba_junio set ingles = '{ingles}' "
                                       f"where  nombre = '{nombreEsba3.get().upper()}' ")
                        connexion.commit()

                        cursor.execute(f"update tercero_esba_junio set religion = '{religion}' "
                                       f"where  nombre = '{nombreEsba3.get().upper()}' ")
                        connexion.commit()

                        cursor.execute(f"update tercero_esba_junio set plastica = '{plastica}' "
                                       f"where  nombre = '{nombreEsba3.get().upper()}' ")
                        connexion.commit()

                        cursor.execute(f"update tercero_esba_junio set ef = '{ef}' "
                                       f"where  nombre = '{nombreEsba2.get().upper()}' ")
                        connexion.commit()

                        cursor.execute(f"update tercero_esba_junio set informatica = '{informatica}' "
                                       f"where  nombre = '{nombreEsba3.get().upper()}' ")
                        connexion.commit()

                        lenguaEsba3.set("")
                        matesEsba3.set("")
                        historiaEsba3.set("")
                        fisicayquimicaEsba3.set("")
                        biologiaygeologiaEsba3.set("")
                        tecnologiaEsba3.set("")
                        francesEsba3.set("")
                        inglesEsba3.set("")
                        religionEsba3.set("")
                        plasticaEsba3.set("")
                        efisicaEsba3.set("")
                        informaticaEsba3.set("")




                    elif nombreId2.get() == 2:

                        if trimestre2.get() == 1:
                                if lenguaEsba3.get():
                                    cursor.execute(f"update tercero_esba_uno set lengua = '{float(lenguaEsba3.get())}' "
                                                   f"where  id = '{int(nombreEsba3.get())}' ")
                                    connexion.commit()
                                else:
                                    pass

                                if matesEsba3.get():
                                    cursor.execute(f"update tercero_esba_uno set matematicas = '{float(matesEsba3.get())}' "
                                                   f"where  id = '{int(nombreEsba3.get())}' ")
                                    connexion.commit()
                                else:
                                    pass

                                if historiaEsba3.get():
                                    cursor.execute(f"update tercero_esba_uno set historia = '{float(historiaEsba3.get())}' "
                                                   f"where  id = '{int(nombreEsba3.get())}' ")
                                    connexion.commit()
                                else:
                                    pass

                                if fisicayquimicaEsba3.get():
                                    cursor.execute(
                                        f"update tercero_esba_uno set fyq = '{float(fisicayquimicaEsba3.get())}' "
                                        f"where  id = '{int(nombreEsba3.get())}' ")
                                    connexion.commit()
                                else:
                                    pass

                                if biologiaygeologiaEsba3.get():
                                    cursor.execute(
                                        f"update tercero_esba_uno set byg = '{float(biologiaygeologiaEsba3.get())}' "
                                        f"where  id = '{int(nombreEsba3.get())}' ")
                                    connexion.commit()
                                else:
                                    pass

                                if francesEsba3.get():
                                    cursor.execute(f"update tercero_esba_uno set frances = '{float(francesEsba3.get())}' "
                                                   f"where id = '{int(nombreEsba3.get())}' ")
                                    connexion.commit()
                                else:
                                    pass

                                if inglesEsba3.get():
                                    cursor.execute(f"update tercero_esba_uno set ingles = '{float(inglesEsba3.get())}' "
                                                   f"where  id = '{int(nombreEsba3.get())}' ")
                                    connexion.commit()
                                else:
                                    pass

                                if religionEsba3.get():
                                    cursor.execute(f"update tercero_esba_uno set religion = '{float(religionEsba3.get())}' "
                                                   f"where  id = '{int(nombreEsba3.get())}' ")
                                    connexion.commit()
                                else:
                                    pass

                                if plasticaEsba3.get():
                                    cursor.execute(f"update tercero_esba_uno set plastica = '{float(plasticaEsba3.get())}' "
                                                   f"where id = '{int(nombreEsba3.get())}' ")
                                    connexion.commit()
                                else:
                                    pass

                                if efisicaEsba3.get():
                                    cursor.execute(f"update tercero_esba_uno set ef = '{float(efisicaEsba3.get())}' "
                                                   f"where  id = '{int(nombreEsba3.get())}'")
                                    connexion.commit()
                                else:
                                    pass

                                if informaticaEsba3.get():
                                    cursor.execute(
                                        f"update tercero_esba_uno set informatica = '{float(informaticaEsba3.get())}' "
                                        f"where  id = '{int(nombreEsba3.get())}' ")
                                    connexion.commit()
                                else:
                                    pass

                                if tecnologiaEsba3.get():
                                    cursor.execute(
                                        f"update tercero_esba_uno set tecnologia = '{float(tecnologiaEsba3.get())}' "
                                        f"where  id = '{int(nombreEsba3.get())}' ")
                                    connexion.commit()
                                else:
                                    pass



                        elif trimestre2.get() == 2:
                                if lenguaEsba3.get():
                                    cursor.execute(f"update tercero_esba_dos set lengua = '{float(lenguaEsba3.get())}' "
                                                   f"where  id = '{int(nombreEsba3.get())}' ")
                                    connexion.commit()
                                else:
                                    pass

                                if matesEsba3.get():
                                    cursor.execute(f"update tercero_esba_dos set matematicas = '{float(matesEsba3.get())}' "
                                                   f"where  id = '{int(nombreEsba3.get())}' ")
                                    connexion.commit()
                                else:
                                    pass

                                if historiaEsba3.get():
                                    cursor.execute(f"update tercero_esba_dos set historia = '{float(historiaEsba3.get())}' "
                                                   f"where  id = '{int(nombreEsba3.get())}' ")
                                    connexion.commit()
                                else:
                                    pass

                                if fisicayquimicaEsba3.get():
                                    cursor.execute(
                                        f"update tercero_esba_dos set fyq = '{float(fisicayquimicaEsba3.get())}' "
                                        f"where  id = '{int(nombreEsba3.get())}' ")
                                    connexion.commit()
                                else:
                                    pass

                                if biologiaygeologiaEsba3.get():
                                    cursor.execute(
                                        f"update tercero_esba_dos set byg = '{float(biologiaygeologiaEsba3.get())}' "
                                        f"where  id = '{int(nombreEsba3.get())}' ")
                                    connexion.commit()
                                else:
                                    pass

                                if francesEsba3.get():
                                    cursor.execute(f"update tercero_esba_dos set frances = '{float(francesEsba3.get())}' "
                                                   f"where id = '{int(nombreEsba3.get())}' ")
                                    connexion.commit()
                                else:
                                    pass

                                if inglesEsba3.get():
                                    cursor.execute(f"update tercero_esba_dos set ingles = '{float(inglesEsba3.get())}' "
                                                   f"where  id = '{int(nombreEsba3.get())}' ")
                                    connexion.commit()
                                else:
                                    pass

                                if religionEsba3.get():
                                    cursor.execute(f"update tercero_esba_dos set religion = '{float(religionEsba3.get())}' "
                                                   f"where  id = '{int(nombreEsba3.get())}' ")
                                    connexion.commit()
                                else:
                                    pass

                                if plasticaEsba3.get():
                                    cursor.execute(f"update tercero_esba_dos set plastica = '{float(plasticaEsba3.get())}' "
                                                   f"where id = '{int(nombreEsba3.get())}' ")
                                    connexion.commit()
                                else:
                                    pass

                                if efisicaEsba3.get():
                                    cursor.execute(f"update tercero_esba_dos set ef = '{float(efisicaEsba3.get())}' "
                                                   f"where  id = '{int(nombreEsba3.get())}' ")
                                    connexion.commit()
                                else:
                                    pass

                                if informaticaEsba3.get():
                                    cursor.execute(
                                        f"update tercero_esba_dos set informatica = '{float(informaticaEsba3.get())}' "
                                        f"where  id = '{int(nombreEsba3.get())}' ")
                                    connexion.commit()
                                else:
                                    pass

                                if tecnologiaEsba3.get():
                                    cursor.execute(
                                        f"update tercero_esba_dos set tecnologia = '{float(tecnologiaEsba3.get())}' "
                                        f"where  id = '{int(nombreEsba3.get())}' ")
                                    connexion.commit()
                                else:
                                    pass


                        elif trimestre2.get() == 3:
                                if lenguaEsba3.get():
                                    cursor.execute(f"update tercero_esba_tres set lengua = '{float(lenguaEsba3.get())}' "
                                                   f"where  id = '{int(nombreEsba3.get())}' ")
                                    connexion.commit()
                                else:
                                    pass

                                if matesEsba3.get():
                                    cursor.execute(
                                        f"update tercero_esba_tres set matematicas = '{float(matesEsba3.get())}' "
                                        f"where  id = '{int(nombreEsba3.get())}' ")
                                    connexion.commit()
                                else:
                                    pass

                                if historiaEsba3.get():
                                    cursor.execute(
                                        f"update tercero_esba_tres set historia = '{float(historiaEsba3.get())}' "
                                        f"where  id = '{int(nombreEsba3.get())}' ")
                                    connexion.commit()
                                else:
                                    pass

                                if fisicayquimicaEsba3.get():
                                    cursor.execute(
                                        f"update tercero_esba_tres set fyq = '{float(fisicayquimicaEsba3.get())}' "
                                        f"where  id = '{int(nombreEsba3.get())}' ")
                                    connexion.commit()
                                else:
                                    pass

                                if biologiaygeologiaEsba3.get():
                                    cursor.execute(
                                        f"update tercero_esba_tres set byg = '{float(biologiaygeologiaEsba3.get())}' "
                                        f"where  id = '{int(nombreEsba3.get())}' ")
                                    connexion.commit()
                                else:
                                    pass

                                if francesEsba3.get():
                                    cursor.execute(f"update tercero_esba_tres set frances = '{float(francesEsba3.get())}' "
                                                   f"where  id = '{int(nombreEsba3.get())}' ")
                                    connexion.commit()
                                else:
                                    pass

                                if inglesEsba3.get():
                                    cursor.execute(f"update tercero_esba_tres set ingles = '{float(inglesEsba3.get())}' "
                                                   f"where  id = '{int(nombreEsba3.get())}' ")
                                    connexion.commit()
                                else:
                                    pass

                                if religionEsba3.get():
                                    cursor.execute(
                                        f"update tercero_esba_tres set religion = '{float(religionEsba3.get())}' "
                                        f"where  id = '{int(nombreEsba3.get())}'")
                                    connexion.commit()
                                else:
                                    pass

                                if plasticaEsba3.get():
                                    cursor.execute(
                                        f"update tercero_esba_tres set plastica = '{float(plasticaEsba3.get())}' "
                                        f"where id = '{int(nombreEsba3.get())}' ")
                                    connexion.commit()
                                else:
                                    pass

                                if efisicaEsba3.get():
                                    cursor.execute(f"update tercero_esba_tres set ef = '{float(efisicaEsba3.get())}' "
                                                   f"where  id = '{int(nombreEsba3.get())}' ")
                                    connexion.commit()
                                else:
                                    pass

                                if informaticaEsba3.get():
                                    cursor.execute(
                                        f"update tercero_esba_tres set informatica = '{float(informaticaEsba3.get())}' "
                                        f"where  id = '{int(nombreEsba3.get())}' ")
                                    connexion.commit()
                                else:
                                    pass

                                if tecnologiaEsba3.get():
                                    cursor.execute(
                                        f"update tercero_esba_tres set tecnologia = '{float(tecnologiaEsba3.get())}' "
                                        f"where  id = '{int(nombreEsba3.get())}'")
                                    connexion.commit()
                                else:
                                    pass


                        elif trimestre2.get() == 4:
                                if lenguaEsba3.get():
                                    cursor.execute(
                                        f"update tercero_esba_septiembre set lengua = '{float(lenguaEsba3.get())}' "
                                        f"where  id = '{int(nombreEsba3.get())}' ")
                                    connexion.commit()
                                else:
                                    pass

                                if matesEsba3.get():
                                    cursor.execute(
                                        f"update tercero_esba_septiembre set matematicas = '{float(matesEsba3.get())}' "
                                        f"where  id = '{int(nombreEsba3.get())}' ")
                                    connexion.commit()
                                else:
                                    pass

                                if historiaEsba3.get():
                                    cursor.execute(
                                        f"update tercero_esba_septiembre set historia = '{float(historiaEsba3.get())}' "
                                        f"where  id = '{int(nombreEsba3.get())}' ")
                                    connexion.commit()
                                else:
                                    pass

                                if fisicayquimicaEsba3.get():
                                    cursor.execute(
                                        f"update tercero_esba_septiembre set fyq = '{float(fisicayquimicaEsba3.get())}' "
                                        f"where  id = '{int(nombreEsba3.get())}' ")
                                    connexion.commit()
                                else:
                                    pass

                                if biologiaygeologiaEsba3.get():
                                    cursor.execute(
                                        f"update tercero_esba_septiembre set byg = '{float(biologiaygeologiaEsba3.get())}' "
                                        f"where  id = '{int(nombreEsba3.get())}' ")
                                    connexion.commit()
                                else:
                                    pass

                                if francesEsba3.get():
                                    cursor.execute(
                                        f"update tercero_esba_septiembre set frances = '{float(francesEsba3.get())}' "
                                        f"where  id = '{int(nombreEsba3.get())}' ")
                                    connexion.commit()
                                else:
                                    pass

                                if inglesEsba3.get():
                                    cursor.execute(
                                        f"update tercero_esba_septiembre set ingles = '{float(inglesEsba3.get())}' "
                                        f"where  id = '{int(nombreEsba3.get())}' ")
                                    connexion.commit()
                                else:
                                    pass

                                if religionEsba3.get():
                                    cursor.execute(
                                        f"update tercero_esba_septiembre set religion = '{float(religionEsba3.get())}' "
                                        f"where  id = '{int(nombreEsba3.get())}' ")
                                    connexion.commit()
                                else:
                                    pass

                                if plasticaEsba3.get():
                                    cursor.execute(
                                        f"update tercero_esba_septiembre set plastica = '{float(plasticaEsba3.get())}' "
                                        f"where  id = '{int(nombreEsba3.get())}' ")
                                    connexion.commit()
                                else:
                                    pass

                                if efisicaEsba3.get():
                                    cursor.execute(f"update tercero_esba_septiembre set ef = '{float(efisicaEsba3.get())}' "
                                                   f"where  id = '{int(nombreEsba3.get())}' ")
                                    connexion.commit()
                                else:
                                    pass

                                if informaticaEsba3.get():
                                    cursor.execute(
                                        f"update tercero_esba_septiembre set informatica = '{float(informaticaEsba3.get())}' "
                                        f"where  id = '{int(nombreEsba3.get())}' ")
                                    connexion.commit()
                                else:
                                    pass

                                if tecnologiaEsba3.get():
                                    cursor.execute(
                                        f"update tercero_esba_septiembre set tecnologia = '{float(tecnologiaEsba3.get())}' "
                                        f"where  id = '{int(nombreEsba3.get())}' ")
                                    connexion.commit()
                                else:
                                    pass


                        #-----------actualizar junio----------------------------------

                        cursor.execute(
                            f"select lengua, matematicas, historia, fyq, byg, tecnologia, frances, ingles, religion,"
                            f"plastica, ef, informatica from tercero_esba_uno where id = '{int(nombreEsba3.get())}'")
                        stock = cursor.fetchall()

                        cursor.execute(
                            f"select lengua, matematicas, historia, fyq, byg, tecnologia, frances, ingles, religion,"
                            f"plastica, ef, informatica from tercero_esba_dos where id = '{int(nombreEsba3.get())}'")
                        stock1 = cursor.fetchall()

                        cursor.execute(
                            f"select lengua, matematicas, historia, fyq, byg, tecnologia, frances, ingles, religion,"
                            f"plastica, ef, informatica from tercero_esba_tres where id = '{int(nombreEsba3.get())}'")
                        stock2 = cursor.fetchall()

                        lengua = (stock[0][0] + stock1[0][0] + stock2[0][0]) / 3
                        matematicas = (stock[0][1] + stock1[0][1] + stock2[0][1]) / 3
                        historia = (stock[0][2] + stock1[0][1] + stock2[0][1]) / 3
                        fyq = (stock[0][3] + stock1[0][3] + stock2[0][3]) / 3
                        byg = (stock[0][4] + stock1[0][4] + stock2[0][4]) / 3
                        tecnologia = (stock[0][5] + stock1[0][5] + stock2[0][5]) / 3
                        frances = (stock[0][6] + stock1[0][6] + stock2[0][6]) / 3
                        ingles = (stock[0][7] + stock1[0][7] + stock2[0][7]) / 3
                        religion = (stock[0][8] + stock1[0][8] + stock2[0][8]) / 3
                        plastica = (stock[0][9] + stock1[0][9] + stock2[0][9]) / 3
                        ef = (stock[0][10] + stock1[0][10] + stock2[0][10]) / 3
                        informatica = (stock[0][11] + stock1[0][11] + stock2[0][11]) / 3

                        cursor.execute(f"update tercero_esba_junio set lengua = '{lengua}' "
                                       f"where  id = '{int(nombreEsba3.get())}' ")
                        connexion.commit()

                        cursor.execute(f"update tercero_esba_junio set matematicas = '{matematicas}' "
                                       f"where id = '{int(nombreEsba3.get())}' ")
                        connexion.commit()

                        cursor.execute(f"update tercero_esba_junio set historia = '{historia}' "
                                       f"where id = '{int(nombreEsba3.get())}' ")
                        connexion.commit()

                        cursor.execute(f"update tercero_esba_junio set fyq = '{fyq}' "
                                       f"where  id = '{int(nombreEsba3.get())}' ")
                        connexion.commit()

                        cursor.execute(f"update tercero_esba_junio set byg = '{byg}' "
                                       f"where  id = '{int(nombreEsba3.get())}' ")
                        connexion.commit()

                        cursor.execute(f"update tercero_esba_junio set tecnologia = '{tecnologia}' "
                                       f"where  id = '{int(nombreEsba3.get())}' ")
                        connexion.commit()

                        cursor.execute(f"update tercero_esba_junio set frances = '{frances}' "
                                       f"where  id = '{int(nombreEsba3.get())}' ")
                        connexion.commit()

                        cursor.execute(f"update tercero_esba_junio set ingles = '{ingles}' "
                                       f"where id = '{int(nombreEsba3.get())}' ")
                        connexion.commit()

                        cursor.execute(f"update tercero_esba_junio set religion = '{religion}' "
                                       f"where  id = '{int(nombreEsba3.get())}'")
                        connexion.commit()

                        cursor.execute(f"update tercero_esba_junio set plastica = '{plastica}' "
                                       f"where  id = '{int(nombreEsba3.get())}' ")
                        connexion.commit()

                        cursor.execute(f"update tercero_esba_junio set ef = '{ef}' "
                                       f"where  id = '{int(nombreEsba3.get())}' ")
                        connexion.commit()

                        cursor.execute(f"update tercero_esba_junio set informatica = '{informatica}' "
                                       f"where  id = '{int(nombreEsba3.get())}' ")
                        connexion.commit()

                        lenguaEsba3.set("")
                        matesEsba3.set("")
                        historiaEsba3.set("")
                        fisicayquimicaEsba3.set("")
                        biologiaygeologiaEsba3.set("")
                        tecnologiaEsba3.set("")
                        francesEsba3.set("")
                        inglesEsba3.set("")
                        religionEsba3.set("")
                        plasticaEsba3.set("")
                        efisicaEsba3.set("")
                        informaticaEsba3.set("")

                    else:
                        pass

                    connexion.close()


            except ValueError:
                pass

        except IndexError:
            pass






    def cuatroEsba():
        try:
            try:

                connexion = sqlite3.connect(nameBD.nomBD())
                cursor = connexion.cursor()
                if nombreId3.get() == 1:
                    if trimestre3.get() == 1:
                        if lenguaEsba4.get():
                            cursor.execute(f"update cuarto_esba_uno set lengua = '{float(lenguaEsba4.get())}' "
                                           f"where  nombre = '{nombreEsba4.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesEsba4.get():
                            cursor.execute(f"update cuarto_esba_uno set matematicas = '{float(matesEsba4.get())}' "
                                           f"where  nombre = '{nombreEsba4.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaEsba4.get():
                            cursor.execute(f"update cuarto_esba_uno set historia = '{float(historiaEsba4.get())}' "
                                           f"where  nombre = '{nombreEsba4.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if fisicayquimicaEsba4.get():
                            cursor.execute(f"update cuarto_esba_uno set fyq = '{float(fisicayquimicaEsba4.get())}' "
                                           f"where  nombre = '{nombreEsba4.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if biologiaygeologiaEsba4.get():
                            cursor.execute(f"update cuarto_esba_uno set byg = '{float(biologiaygeologiaEsba4.get())}' "
                                           f"where  nombre = '{nombreEsba4.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesEsba4.get():
                            cursor.execute(f"update cuarto_esba_uno set frances = '{float(francesEsba4.get())}' "
                                           f"where  nombre = '{nombreEsba4.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesEsba4.get():
                            cursor.execute(f"update cuarto_esba_uno set ingles = '{float(inglesEsba4.get())}' "
                                           f"where  nombre = '{nombreEsba4.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionEsba4.get():
                            cursor.execute(f"update cuarto_esba_uno set religion = '{float(religionEsba4.get())}' "
                                           f"where  nombre = '{nombreEsba4.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if plasticaEsba4.get():
                            cursor.execute(f"update cuarto_esba_uno set plastica = '{float(plasticaEsba4.get())}' "
                                           f"where  nombre = '{nombreEsba4.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaEsba4.get():
                            cursor.execute(f"update cuarto_esba_uno set ef = '{float(efisicaEsba4.get())}' "
                                           f"where  nombre = '{nombreEsba4.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaEsba4.get():
                            cursor.execute(
                                f"update cuarto_esba_uno set informatica = '{float(informaticaEsba4.get())}' "
                                f"where  nombre = '{nombreEsba4.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if tecnologiaEsba4.get():
                            cursor.execute(
                                f"update cuarto_esba_uno set tecnologia = '{float(tecnologiaEsba4.get())}' "
                                f"where  nombre = '{nombreEsba4.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass



                    elif trimestre3.get() == 2:
                        if lenguaEsba4.get():
                            cursor.execute(f"update cuarto_esba_dos set lengua = '{float(lenguaEsba4.get())}' "
                                           f"where  nombre = '{nombreEsba4.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesEsba4.get():
                            cursor.execute(f"update cuarto_esba_dos set matematicas = '{float(matesEsba4.get())}' "
                                           f"where  nombre = '{nombreEsba4.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaEsba4.get():
                            cursor.execute(f"update cuarto_esba_dos set historia = '{float(historiaEsba4.get())}' "
                                           f"where  nombre = '{nombreEsba4.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if fisicayquimicaEsba4.get():
                            cursor.execute(f"update cuarto_esba_dos set fyq = '{float(fisicayquimicaEsba4.get())}' "
                                           f"where  nombre = '{nombreEsba4.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if biologiaygeologiaEsba4.get():
                            cursor.execute(f"update cuarto_esba_dos set byg = '{float(biologiaygeologiaEsba4.get())}' "
                                           f"where  nombre = '{nombreEsba4.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesEsba4.get():
                            cursor.execute(f"update cuarto_esba_dos set frances = '{float(francesEsba4.get())}' "
                                           f"where  nombre = '{nombreEsba4.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesEsba4.get():
                            cursor.execute(f"update cuarto_esba_dos set ingles = '{float(inglesEsba4.get())}' "
                                           f"where  nombre = '{nombreEsba4.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionEsba4.get():
                            cursor.execute(f"update cuarto_esba_dos set religion = '{float(religionEsba4.get())}' "
                                           f"where  nombre = '{nombreEsba4.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if plasticaEsba4.get():
                            cursor.execute(f"update cuarto_esba_dos set plastica = '{float(plasticaEsba4.get())}' "
                                           f"where  nombre = '{nombreEsba4.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaEsba4.get():
                            cursor.execute(f"update cuarto_esba_dos set ef = '{float(efisicaEsba4.get())}' "
                                           f"where  nombre = '{nombreEsba4.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaEsba4.get():
                            cursor.execute(
                                f"update cuarto_esba_dos set informatica = '{float(informaticaEsba4.get())}' "
                                f"where  nombre = '{nombreEsba4.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if tecnologiaEsba4.get():
                            cursor.execute(
                                f"update cuarto_esba_dos set tecnologia = '{float(tecnologiaEsba4.get())}' "
                                f"where  nombre = '{nombreEsba4.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass


                    elif trimestre3.get() == 3:
                        if lenguaEsba4.get():
                            cursor.execute(f"update cuarto_esba_tres set lengua = '{float(lenguaEsba4.get())}' "
                                           f"where  nombre = '{nombreEsba4.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesEsba4.get():
                            cursor.execute(f"update cuarto_esba_tres set matematicas = '{float(matesEsba4.get())}' "
                                           f"where  nombre = '{nombreEsba4.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaEsba4.get():
                            cursor.execute(f"update cuarto_esba_tres set historia = '{float(historiaEsba4.get())}' "
                                           f"where  nombre = '{nombreEsba4.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if fisicayquimicaEsba4.get():
                            cursor.execute(f"update cuarto_esba_tres set fyq = '{float(fisicayquimicaEsba4.get())}' "
                                           f"where  nombre = '{nombreEsba4.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if biologiaygeologiaEsba4.get():
                            cursor.execute(f"update cuarto_esba_tres set byg = '{float(biologiaygeologiaEsba4.get())}' "
                                           f"where  nombre = '{nombreEsba4.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesEsba4.get():
                            cursor.execute(f"update cuarto_esba_tres set frances = '{float(francesEsba4.get())}' "
                                           f"where  nombre = '{nombreEsba4.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesEsba4.get():
                            cursor.execute(f"update cuarto_esba_tres set ingles = '{float(inglesEsba4.get())}' "
                                           f"where  nombre = '{nombreEsba4.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionEsba4.get():
                            cursor.execute(f"update cuarto_esba_tres set religion = '{float(religionEsba4.get())}' "
                                           f"where  nombre = '{nombreEsba4.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if plasticaEsba4.get():
                            cursor.execute(f"update cuarto_esba_tres set plastica = '{float(plasticaEsba4.get())}' "
                                           f"where  nombre = '{nombreEsba4.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaEsba4.get():
                            cursor.execute(f"update cuarto_esba_tres set ef = '{float(efisicaEsba4.get())}' "
                                           f"where  nombre = '{nombreEsba4.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaEsba4.get():
                            cursor.execute(
                                f"update cuarto_esba_tres set informatica = '{float(informaticaEsba4.get())}' "
                                f"where  nombre = '{nombreEsba4.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if tecnologiaEsba4.get():
                            cursor.execute(
                                f"update cuarto_esba_tres set tecnologia = '{float(tecnologiaEsba4.get())}' "
                                f"where  nombre = '{nombreEsba4.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass


                    elif trimestre3.get() == 4:
                        if lenguaEsba4.get():
                            cursor.execute(f"update cuarto_esba_septiembre set lengua = '{float(lenguaEsba4.get())}' "
                                           f"where  nombre = '{nombreEsba4.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesEsba4.get():
                            cursor.execute(f"update cuarto_esba_septiembre set matematicas = '{float(matesEsba4.get())}' "
                                           f"where  nombre = '{nombreEsba4.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaEsba4.get():
                            cursor.execute(f"update cuarto_esba_septiembre set historia = '{float(historiaEsba4.get())}' "
                                           f"where  nombre = '{nombreEsba4.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if fisicayquimicaEsba4.get():
                            cursor.execute(f"update cuarto_esba_septiembre set fyq = '{float(fisicayquimicaEsba4.get())}' "
                                           f"where  nombre = '{nombreEsba4.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if biologiaygeologiaEsba4.get():
                            cursor.execute(f"update cuarto_esba_septiembre set byg = '{float(biologiaygeologiaEsba4.get())}' "
                                           f"where  nombre = '{nombreEsba4.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesEsba4.get():
                            cursor.execute(f"update cuarto_esba_septiembre set frances = '{float(francesEsba4.get())}' "
                                           f"where  nombre = '{nombreEsba4.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesEsba4.get():
                            cursor.execute(f"update cuarto_esba_septiembre set ingles = '{float(inglesEsba4.get())}' "
                                           f"where  nombre = '{nombreEsba4.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionEsba4.get():
                            cursor.execute(f"update cuatro_esba_septiembre set religion = '{float(religionEsba4.get())}' "
                                           f"where  nombre = '{nombreEsba4.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if plasticaEsba4.get():
                            cursor.execute(f"update cuarto_esba_septiembre set plastica = '{float(plasticaEsba4.get())}' "
                                           f"where  nombre = '{nombreEsba4.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaEsba4.get():
                            cursor.execute(f"update cuarto_esba_septiembre set ef = '{float(efisicaEsba4.get())}' "
                                           f"where  nombre = '{nombreEsba4.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaEsba4.get():
                            cursor.execute(
                                f"update cuarto_esba_septiembre set informatica = '{float(informaticaEsba4.get())}' "
                                f"where  nombre = '{nombreEsba4.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if tecnologiaEsba4.get():
                            cursor.execute(
                                f"update cuarto_esba_septiembre set tecnologia = '{float(tecnologiaEsba4.get())}' "
                                f"where  nombre = '{nombreEsba4.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                    # --------actualizar la tabla de junio----------------------------
                    cursor.execute(f"select lengua, matematicas, historia, fyq, byg, tecnologia, frances, ingles, religion,"
                                   f"plastica, ef, informatica from cuarto_esba_uno where nombre = '{nombreEsba4.get().upper()}'")
                    stock = cursor.fetchall()

                    cursor.execute(f"select lengua, matematicas, historia, fyq, byg, tecnologia, frances, ingles, religion,"
                                   f"plastica, ef, informatica from cuarto_esba_dos where nombre = '{nombreEsba4.get().upper()}'")
                    stock1 = cursor.fetchall()

                    cursor.execute(f"select lengua, matematicas, historia, fyq, byg, tecnologia, frances, ingles, religion,"
                                   f"plastica, ef, informatica from cuarto_esba_tres where nombre = '{nombreEsba4.get().upper()}'")
                    stock2 = cursor.fetchall()

                    lengua = (stock[0][0] + stock1[0][0] + stock2[0][0]) / 3
                    matematicas = (stock[0][1] + stock1[0][1] + stock2[0][1]) / 3
                    historia = (stock[0][2] + stock1[0][1] + stock2[0][1]) / 3
                    fyq = (stock[0][3] + stock1[0][3] + stock2[0][3]) / 3
                    byg = (stock[0][4] + stock1[0][4] + stock2[0][4]) / 3
                    tecnologia = (stock[0][5] + stock1[0][5] + stock2[0][5]) / 3
                    frances = (stock[0][6] + stock1[0][6] + stock2[0][6]) / 3
                    ingles = (stock[0][7] + stock1[0][7] + stock2[0][7]) / 3
                    religion = (stock[0][8] + stock1[0][8] + stock2[0][8]) / 3
                    plastica = (stock[0][9] + stock1[0][9] + stock2[0][9]) / 3
                    ef = (stock[0][10] + stock1[0][10] + stock2[0][10]) / 3
                    informatica = (stock[0][11] + stock1[0][11] + stock2[0][11]) / 3

                    cursor.execute(f"update cuarto_esba_junio set lengua = '{lengua}' "
                                   f"where  nombre = '{nombreEsba4.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update cuarto_esba_junio set matematicas = '{matematicas}' "
                                   f"where  nombre = '{nombreEsba4.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update cuarto_esba_junio set historia = '{historia}' "
                                   f"where  nombre = '{nombreEsba4.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update cuarto_esba_junio set fyq = '{fyq}' "
                                   f"where  nombre = '{nombreEsba4.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update cuarto_esba_junio set byg = '{byg}' "
                                   f"where  nombre = '{nombreEsba4.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update cuarto_esba_junio set tecnologia = '{tecnologia}' "
                                   f"where  nombre = '{nombreEsba4.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update cuarto_esba_junio set frances = '{frances}' "
                                   f"where  nombre = '{nombreEsba4.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update cuarto_esba_junio set ingles = '{ingles}' "
                                   f"where  nombre = '{nombreEsba4.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update cuarto_esba_junio set religion = '{religion}' "
                                   f"where  nombre = '{nombreEsba4.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update cuarto_esba_junio set plastica = '{plastica}' "
                                   f"where  nombre = '{nombreEsba4.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update cuarto_esba_junio set ef = '{ef}' "
                                   f"where  nombre = '{nombreEsba4.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update cuarto_esba_junio set informatica = '{informatica}' "
                                   f"where  nombre = '{nombreEsba4.get().upper()}' ")
                    connexion.commit()

                    lenguaEsba4.set("")
                    matesEsba4.set("")
                    historiaEsba4.set("")
                    fisicayquimicaEsba4.set("")
                    biologiaygeologiaEsba4.set("")
                    tecnologiaEsba4.set("")
                    francesEsba4.set("")
                    inglesEsba4.set("")
                    religionEsba4.set("")
                    plasticaEsba4.set("")
                    efisicaEsba4.set("")
                    informaticaEsba4.set("")




                elif nombreId3.get() == 2:

                    if trimestre3.get() == 1:
                        if lenguaEsba4.get():
                            cursor.execute(f"update cuarto_esba_uno set lengua = '{float(lenguaEsba4.get())}' "
                                           f"where  id = '{int(nombreEsba4.get().upper())}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesEsba4.get():
                            cursor.execute(f"update cuarto_esba_uno set matematicas = '{float(matesEsba4.get())}' "
                                           f"where   id = '{int(nombreEsba4.get().upper())}'")
                            connexion.commit()
                        else:
                            pass

                        if historiaEsba4.get():
                            cursor.execute(f"update cuarto_esba_uno set historia = '{float(historiaEsba4.get())}' "
                                           f"where   id = '{int(nombreEsba4.get().upper())}' ")
                            connexion.commit()
                        else:
                            pass

                        if fisicayquimicaEsba4.get():
                            cursor.execute(f"update cuarto_esba_uno set fyq = '{float(fisicayquimicaEsba4.get())}' "
                                           f"where   id = '{int(nombreEsba4.get().upper())}' ")
                            connexion.commit()
                        else:
                            pass

                        if biologiaygeologiaEsba4.get():
                            cursor.execute(f"update cuarto_esba_uno set byg = '{float(biologiaygeologiaEsba4.get())}' "
                                           f"where   id = '{int(nombreEsba4.get().upper())}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesEsba4.get():
                            cursor.execute(f"update cuarto_esba_uno set frances = '{float(francesEsba4.get())}' "
                                           f"where   id = '{int(nombreEsba4.get().upper())}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesEsba4.get():
                            cursor.execute(f"update cuarto_esba_uno set ingles = '{float(inglesEsba4.get())}' "
                                           f"where   id = '{int(nombreEsba4.get().upper())}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionEsba4.get():
                            cursor.execute(f"update cuarto_esba_uno set religion = '{float(religionEsba4.get())}' "
                                           f"where   id = '{int(nombreEsba4.get().upper())}' ")
                            connexion.commit()
                        else:
                            pass

                        if plasticaEsba4.get():
                            cursor.execute(f"update cuarto_esba_uno set plastica = '{float(plasticaEsba4.get())}' "
                                           f"where   id = '{int(nombreEsba4.get().upper())}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaEsba4.get():
                            cursor.execute(f"update cuarto_esba_uno set ef = '{float(efisicaEsba4.get())}' "
                                           f"where   id = '{int(nombreEsba4.get().upper())}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaEsba4.get():
                            cursor.execute(
                                f"update cuarto_esba_uno set informatica = '{float(informaticaEsba4.get())}' "
                                f"where   id = '{int(nombreEsba4.get().upper())}' ")
                            connexion.commit()
                        else:
                            pass

                        if tecnologiaEsba4.get():
                            cursor.execute(
                                f"update cuarto_esba_uno set tecnologia = '{float(tecnologiaEsba4.get())}' "
                                f"where   id = '{int(nombreEsba4.get().upper())}' ")
                            connexion.commit()
                        else:
                            pass



                    elif trimestre3.get() == 2:
                        if lenguaEsba4.get():
                            cursor.execute(f"update cuarto_esba_dos set lengua = '{float(lenguaEsba4.get())}' "
                                           f"where   id = '{int(nombreEsba4.get().upper())}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesEsba4.get():
                            cursor.execute(f"update cuarto_esba_dos set matematicas = '{float(matesEsba4.get())}' "
                                           f"where   id = '{int(nombreEsba4.get().upper())}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaEsba4.get():
                            cursor.execute(f"update cuarto_esba_dos set historia = '{float(historiaEsba4.get())}' "
                                           f"where  id = '{int(nombreEsba4.get().upper())}'")
                            connexion.commit()
                        else:
                            pass

                        if fisicayquimicaEsba4.get():
                            cursor.execute(f"update cuarto_esba_dos set fyq = '{float(fisicayquimicaEsba4.get())}' "
                                           f"where   id = '{int(nombreEsba4.get().upper())}' ")
                            connexion.commit()
                        else:
                            pass

                        if biologiaygeologiaEsba4.get():
                            cursor.execute(f"update cuarto_esba_dos set byg = '{float(biologiaygeologiaEsba4.get())}' "
                                           f"where   id = '{int(nombreEsba4.get().upper())}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesEsba4.get():
                            cursor.execute(f"update cuarto_esba_dos set frances = '{float(francesEsba4.get())}' "
                                           f"where   id = '{int(nombreEsba4.get().upper())}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesEsba4.get():
                            cursor.execute(f"update cuarto_esba_dos set ingles = '{float(inglesEsba4.get())}' "
                                           f"where   id = '{int(nombreEsba4.get().upper())}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionEsba4.get():
                            cursor.execute(f"update cuarto_esba_dos set religion = '{float(religionEsba4.get())}' "
                                           f"where   id = '{int(nombreEsba4.get().upper())}' ")
                            connexion.commit()
                        else:
                            pass

                        if plasticaEsba4.get():
                            cursor.execute(f"update cuarto_esba_dos set plastica = '{float(plasticaEsba4.get())}' "
                                           f"where   id = '{int(nombreEsba4.get().upper())}'")
                            connexion.commit()
                        else:
                            pass

                        if efisicaEsba4.get():
                            cursor.execute(f"update cuarto_esba_dos set ef = '{float(efisicaEsba4.get())}' "
                                           f"where   id = '{int(nombreEsba4.get().upper())}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaEsba4.get():
                            cursor.execute(
                                f"update cuarto_esba_dos set informatica = '{float(informaticaEsba4.get())}' "
                                f"where   id = '{int(nombreEsba4.get().upper())}' ")
                            connexion.commit()
                        else:
                            pass

                        if tecnologiaEsba4.get():
                            cursor.execute(
                                f"update cuarto_esba_dos set tecnologia = '{float(tecnologiaEsba4.get())}' "
                                f"where   id = '{int(nombreEsba4.get().upper())}' ")
                            connexion.commit()
                        else:
                            pass


                    elif trimestre3.get() == 3:
                        if lenguaEsba4.get():
                            cursor.execute(f"update cuarto_esba_tres set lengua = '{float(lenguaEsba4.get())}' "
                                           f"where   id = '{int(nombreEsba4.get().upper())}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesEsba4.get():
                            cursor.execute(f"update cuarto_esba_tres set matematicas = '{float(matesEsba4.get())}' "
                                           f"where   id = '{int(nombreEsba4.get().upper())}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaEsba4.get():
                            cursor.execute(f"update cuarto_esba_tres set historia = '{float(historiaEsba4.get())}' "
                                           f"where   id = '{int(nombreEsba4.get().upper())}' ")
                            connexion.commit()
                        else:
                            pass

                        if fisicayquimicaEsba4.get():
                            cursor.execute(f"update cuarto_esba_tres set fyq = '{float(fisicayquimicaEsba4.get())}' "
                                           f"where  id = '{int(nombreEsba4.get().upper())}' ")
                            connexion.commit()
                        else:
                            pass

                        if biologiaygeologiaEsba4.get():
                            cursor.execute(f"update cuarto_esba_tres set byg = '{float(biologiaygeologiaEsba4.get())}' "
                                           f"where  id = '{int(nombreEsba4.get().upper())}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesEsba4.get():
                            cursor.execute(f"update cuarto_esba_tres set frances = '{float(francesEsba4.get())}' "
                                           f"where   id = '{int(nombreEsba4.get().upper())}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesEsba4.get():
                            cursor.execute(f"update cuarto_esba_tres set ingles = '{float(inglesEsba4.get())}' "
                                           f"where   id = '{int(nombreEsba4.get().upper())}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionEsba4.get():
                            cursor.execute(f"update cuarto_esba_tres set religion = '{float(religionEsba4.get())}' "
                                           f"where   id = '{int(nombreEsba4.get().upper())}' ")
                            connexion.commit()
                        else:
                            pass

                        if plasticaEsba4.get():
                            cursor.execute(f"update cuarto_esba_tres set plastica = '{float(plasticaEsba4.get())}' "
                                           f"where   id = '{int(nombreEsba4.get().upper())}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaEsba4.get():
                            cursor.execute(f"update cuarto_esba_tres set ef = '{float(efisicaEsba4.get())}' "
                                           f"where   id = '{int(nombreEsba4.get().upper())}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaEsba4.get():
                            cursor.execute(
                                f"update cuarto_esba_tres set informatica = '{float(informaticaEsba4.get())}' "
                                f"where   id = '{int(nombreEsba4.get().upper())}' ")
                            connexion.commit()
                        else:
                            pass

                        if tecnologiaEsba4.get():
                            cursor.execute(
                                f"update cuarto_esba_tres set tecnologia = '{float(tecnologiaEsba4.get())}' "
                                f"where   id = '{int(nombreEsba4.get().upper())}' ")
                            connexion.commit()
                        else:
                            pass


                    elif trimestre3.get() == 4:
                        if lenguaEsba4.get():
                            cursor.execute(f"update cuarto_esba_septiembre set lengua = '{float(lenguaEsba4.get())}' "
                                           f"where  id = '{int(nombreEsba4.get().upper())}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesEsba4.get():
                            cursor.execute(f"update cuarto_esba_septiembre set matematicas = '{float(matesEsba4.get())}' "
                                           f"where  id = '{int(nombreEsba4.get().upper())}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaEsba4.get():
                            cursor.execute(f"update cuarto_esba_septiembre set historia = '{float(historiaEsba4.get())}' "
                                           f"where   id = '{int(nombreEsba4.get().upper())}' ")
                            connexion.commit()
                        else:
                            pass

                        if fisicayquimicaEsba4.get():
                            cursor.execute(f"update cuarto_esba_septiembre set fyq = '{float(fisicayquimicaEsba4.get())}' "
                                           f"where  id = '{int(nombreEsba4.get().upper())}' ")
                            connexion.commit()
                        else:
                            pass

                        if biologiaygeologiaEsba4.get():
                            cursor.execute(f"update cuarto_esba_septiembre set byg = '{float(biologiaygeologiaEsba4.get())}' "
                                           f"where  id = '{int(nombreEsba4.get().upper())}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesEsba4.get():
                            cursor.execute(f"update cuarto_esba_septiembre set frances = '{float(francesEsba4.get())}' "
                                           f"where  id = '{int(nombreEsba4.get().upper())}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesEsba4.get():
                            cursor.execute(f"update cuarto_esba_septiembre set ingles = '{float(inglesEsba4.get())}' "
                                           f"where   id = '{int(nombreEsba4.get().upper())}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionEsba4.get():
                            cursor.execute(f"update cuarto_esba_septiembre set religion = '{float(religionEsba4.get())}' "
                                           f"where   id = '{int(nombreEsba4.get().upper())}' ")
                            connexion.commit()
                        else:
                            pass

                        if plasticaEsba4.get():
                            cursor.execute(f"update cuarto_esba_septiembre set plastica = '{float(plasticaEsba4.get())}' "
                                           f"where   id = '{int(nombreEsba4.get().upper())}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaEsba4.get():
                            cursor.execute(f"update cuarto_esba_septiembre set ef = '{float(efisicaEsba4.get())}' "
                                           f"where   id = '{int(nombreEsba4.get().upper())}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaEsba4.get():
                            cursor.execute(
                                f"update cuarto_esba_septiembre set informatica = '{float(informaticaEsba4.get())}' "
                                f"where   id = '{int(nombreEsba4.get().upper())}' ")
                            connexion.commit()
                        else:
                            pass

                        if tecnologiaEsba4.get():
                            cursor.execute(
                                f"update cuarto_esba_septiembre set tecnologia = '{float(tecnologiaEsba4.get())}' "
                                f"where   id = '{int(nombreEsba4.get().upper())}' ")
                            connexion.commit()
                        else:
                            pass

                    # --------actualizar la tabla de junio----------------------------
                    cursor.execute(f"select lengua, matematicas, historia, fyq, byg, tecnologia, frances, ingles, religion,"
                                   f"plastica, ef, informatica from cuarto_esba_uno where  id = '{int(nombreEsba4.get().upper())}'")
                    stock = cursor.fetchall()

                    cursor.execute(f"select lengua, matematicas, historia, fyq, byg, tecnologia, frances, ingles, religion,"
                                   f"plastica, ef, informatica from cuarto_esba_dos where  id = '{int(nombreEsba4.get().upper())}'")
                    stock1 = cursor.fetchall()

                    cursor.execute(f"select lengua, matematicas, historia, fyq, byg, tecnologia, frances, ingles, religion,"
                                   f"plastica, ef, informatica from cuarto_esba_tres where  id = '{int(nombreEsba4.get().upper())}'")
                    stock2 = cursor.fetchall()

                    lengua = (stock[0][0] + stock1[0][0] + stock2[0][0]) / 3
                    matematicas = (stock[0][1] + stock1[0][1] + stock2[0][1]) / 3
                    historia = (stock[0][2] + stock1[0][1] + stock2[0][1]) / 3
                    fyq = (stock[0][3] + stock1[0][3] + stock2[0][3]) / 3
                    byg = (stock[0][4] + stock1[0][4] + stock2[0][4]) / 3
                    tecnologia = (stock[0][5] + stock1[0][5] + stock2[0][5]) / 3
                    frances = (stock[0][6] + stock1[0][6] + stock2[0][6]) / 3
                    ingles = (stock[0][7] + stock1[0][7] + stock2[0][7]) / 3
                    religion = (stock[0][8] + stock1[0][8] + stock2[0][8]) / 3
                    plastica = (stock[0][9] + stock1[0][9] + stock2[0][9]) / 3
                    ef = (stock[0][10] + stock1[0][10] + stock2[0][10]) / 3
                    informatica = (stock[0][11] + stock1[0][11] + stock2[0][11]) / 3

                    cursor.execute(f"update cuarto_esba_junio set lengua = '{lengua}' "
                                   f"where   id = '{int(nombreEsba4.get().upper())}' ")
                    connexion.commit()

                    cursor.execute(f"update cuarto_esba_junio set matematicas = '{matematicas}' "
                                   f"where   id = '{int(nombreEsba4.get().upper())}' ")
                    connexion.commit()

                    cursor.execute(f"update cuarto_esba_junio set historia = '{historia}' "
                                   f"where   id = '{int(nombreEsba4.get().upper())}' ")
                    connexion.commit()

                    cursor.execute(f"update cuarto_esba_junio set fyq = '{fyq}' "
                                   f"where   id = '{int(nombreEsba4.get().upper())}' ")
                    connexion.commit()

                    cursor.execute(f"update cuarto_esba_junio set byg = '{byg}' "
                                   f"where   id = '{int(nombreEsba4.get().upper())}' ")
                    connexion.commit()

                    cursor.execute(f"update cuarto_esba_junio set tecnologia = '{tecnologia}' "
                                   f"where   id = '{int(nombreEsba4.get().upper())}' ")
                    connexion.commit()

                    cursor.execute(f"update cuarto_esba_junio set frances = '{frances}' "
                                   f"where   id = '{int(nombreEsba4.get().upper())}' ")
                    connexion.commit()

                    cursor.execute(f"update cuarto_esba_junio set ingles = '{ingles}' "
                                   f"where   id = '{int(nombreEsba4.get().upper())}' ")
                    connexion.commit()

                    cursor.execute(f"update cuarto_esba_junio set religion = '{religion}' "
                                   f"where   id = '{int(nombreEsba4.get().upper())}' ")
                    connexion.commit()

                    cursor.execute(f"update cuarto_esba_junio set plastica = '{plastica}' "
                                   f"where  id = '{int(nombreEsba4.get().upper())}' ")
                    connexion.commit()

                    cursor.execute(f"update cuarto_esba_junio set ef = '{ef}' "
                                   f"where   id = '{int(nombreEsba4.get().upper())}' ")
                    connexion.commit()

                    cursor.execute(f"update cuarto_esba_junio set informatica = '{informatica}' "
                                   f"where  id = '{int(nombreEsba4.get().upper())}' ")
                    connexion.commit()

                    lenguaEsba4.set("")
                    matesEsba4.set("")
                    historiaEsba4.set("")
                    fisicayquimicaEsba4.set("")
                    biologiaygeologiaEsba4.set("")
                    tecnologiaEsba4.set("")
                    francesEsba4.set("")
                    inglesEsba4.set("")
                    religionEsba4.set("")
                    plasticaEsba4.set("")
                    efisicaEsba4.set("")
                    informaticaEsba4.set("")

                else:
                    pass

                connexion.close()

            except ValueError:
                pass
        except IndexError:
            pass




    def primeroBachCiencias():
        try:

            try:


                connexion = sqlite3.connect(nameBD.nomBD())
                cursor = connexion.cursor()
                if nombreId41.get() == 1:
                    if trimestre41.get() == 1:
                        if lenguaBach11.get():
                            cursor.execute(f"update primero_bach_uno set lengua = '{float(lenguaBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesBach11.get():
                            cursor.execute(f"update primero_bach_uno set matematicas = '{float(matesBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaBach11.get():
                            cursor.execute(f"update primero_bach_uno set historia = '{float(historiaBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if fisicayquimicaBach11.get():
                            cursor.execute(f"update primero_bach_uno set fyq = '{float(fisicayquimicaBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if biologiaBach11.get():
                            cursor.execute(f"update primero_bach_uno set biologia = '{float(biologiaBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if economiaBach11.get():
                            cursor.execute(f"update primero_bach_uno set economia = '{float(economiaBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesBach11.get():
                            cursor.execute(f"update primero_bach_uno set frances = '{float(francesBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesBach11.get():
                            cursor.execute(f"update primero_bach_uno set ingles = '{float(inglesBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionBach11.get():
                            cursor.execute(f"update primero_bach_uno set religion = '{float(religionBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if dibujoBach11.get():
                            cursor.execute(f"update primero_bach_uno set dibujo_tecnico = '{float(dibujoBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaBach11.get():
                            cursor.execute(f"update primero_bach_uno set ef = '{float(efisicaBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaBach11.get():
                            cursor.execute(f"update primero_bach_uno set informatica = '{float(informaticaBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if filosofiaBach11.get():
                            cursor.execute(f"update primero_bach_uno set filosofia = '{float(filosofiaBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass


                        if cctmBach11.get():
                            cursor.execute(f"update primero_bach_uno set cctm = '{float(cctmBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass



                    elif trimestre41.get() == 2:
                        if lenguaBach11.get():
                            cursor.execute(f"update primero_bach_dos set lengua = '{float(lenguaBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesBach11.get():
                            cursor.execute(f"update primero_bach_dos set matematicas = '{float(matesBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaBach11.get():
                            cursor.execute(f"update primero_bach_dos set historia = '{float(historiaBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if fisicayquimicaBach11.get():
                            cursor.execute(f"update primero_bach_dos set fyq = '{float(fisicayquimicaBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if biologiaBach11.get():
                            cursor.execute(f"update primero_bach_dos set biologia = '{float(biologiaBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if economiaBach11.get():
                            cursor.execute(f"update primero_bach_dos set economia = '{float(economiaBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesBach11.get():
                            cursor.execute(f"update primero_bach_dos set frances = '{float(francesBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesBach11.get():
                            cursor.execute(f"update primero_bach_dos set ingles = '{float(inglesBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionBach11.get():
                            cursor.execute(f"update primero_bach_dos set religion = '{float(religionBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if dibujoBach11.get():
                            cursor.execute(f"update primero_bach_dos set dibujo_tecnico = '{float(dibujoBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaBach11.get():
                            cursor.execute(f"update primero_bach_dos set ef = '{float(efisicaBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaBach11.get():
                            cursor.execute(f"update primero_bach_dos set informatica = '{float(informaticaBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if filosofiaBach11.get():
                            cursor.execute(f"update primero_bach_dos set filosofia = '{float(filosofiaBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if cctmBach11.get():
                            cursor.execute(f"update primero_bach_dos set cctm = '{float(cctmBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass


                    elif trimestre41.get() == 3:
                        if lenguaBach11.get():
                            cursor.execute(f"update primero_bach_tres set lengua = '{float(lenguaBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesBach11.get():
                            cursor.execute(f"update primero_bach_tres set matematicas = '{float(matesBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaBach11.get():
                            cursor.execute(f"update primero_bach_tres set historia = '{float(historiaBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if fisicayquimicaBach11.get():
                            cursor.execute(f"update primero_bach_tres set fyq = '{float(fisicayquimicaBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if biologiaBach11.get():
                            cursor.execute(f"update primero_bach_tres set biologia = '{float(biologiaBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if economiaBach11.get():
                            cursor.execute(f"update primero_bach_tres set economia = '{float(economiaBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesBach11.get():
                            cursor.execute(f"update primero_bach_tres set frances = '{float(francesBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesBach11.get():
                            cursor.execute(f"update primero_bach_tres set ingles = '{float(inglesBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionBach11.get():
                            cursor.execute(f"update primero_bach_tres set religion = '{float(religionBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if dibujoBach11.get():
                            cursor.execute(f"update primero_bach_tres set dibujo_tecnico = '{float(dibujoBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaBach11.get():
                            cursor.execute(f"update primero_bach_tres set ef = '{float(efisicaBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaBach11.get():
                            cursor.execute(f"update primero_bach_tres set informatica = '{float(informaticaBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if filosofiaBach11.get():
                            cursor.execute(f"update primero_bach_tres set filosofia = '{float(filosofiaBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if cctmBach11.get():
                            cursor.execute(f"update primero_bach_tres set cctm = '{float(cctmBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass


                    elif trimestre41.get() == 4:
                        if lenguaBach11.get():
                            cursor.execute(f"update primero_bach_septiembre set lengua = '{float(lenguaBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesBach11.get():
                            cursor.execute(f"update primero_bach_septiembre set matematicas = '{float(matesBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaBach11.get():
                            cursor.execute(f"update primero_bach_septiembre set historia = '{float(historiaBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if fisicayquimicaBach11.get():
                            cursor.execute(f"update primero_bach_septiembre set fyq = '{float(fisicayquimicaBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if biologiaBach11.get():
                            cursor.execute(f"update primero_bach_septiembre set biologia = '{float(biologiaBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if economiaBach11.get():
                            cursor.execute(f"update primero_bach_septiembre set economia = '{float(economiaBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesBach11.get():
                            cursor.execute(f"update primero_bach_septiembre set frances = '{float(francesBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesBach11.get():
                            cursor.execute(f"update primero_bach_septiembre set ingles = '{float(inglesBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionBach11.get():
                            cursor.execute(f"update primero_bach_septiembre set religion = '{float(religionBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if dibujoBach11.get():
                            cursor.execute(f"update primero_bach_septiembre set dibujo_tecnico = '{float(dibujoBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaBach11.get():
                            cursor.execute(f"update primero_bach_septiembre set ef = '{float(efisicaBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaBach11.get():
                            cursor.execute(f"update primero_bach_septiembre set informatica = '{float(informaticaBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if filosofiaBach11.get():
                            cursor.execute(f"update primero_bach_septiembre set filosofia = '{float(filosofiaBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if cctmBach11.get():
                            cursor.execute(f"update primero_bach_septiembre set cctm = '{float(cctmBach11.get())}' "
                                           f"where  nombre = '{nombreBach11.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                    # --------actualizar la tabla de junio----------------------------
                    cursor.execute(f"select lengua, matematicas, historia, fyq, biologia, economia, frances, ingles, religion,"
                                   f"dibujo_tecnico, ef, informatica, filosofia, cctm from primero_bach_uno where nombre = '{nombreBach11.get().upper()}'")
                    stock = cursor.fetchall()

                    cursor.execute(f"select lengua, matematicas, historia, fyq, biologia, economia, frances, ingles, religion,"
                                   f"dibujo_tecnico, ef, informatica, filosofia, cctm from primero_bach_dos where nombre = '{nombreBach11.get().upper()}'")
                    stock1 = cursor.fetchall()

                    cursor.execute(f"select lengua, matematicas, historia, fyq, biologia, economia, frances, ingles, religion,"
                                   f"dibujo_tecnico, ef, informatica, filosofia, cctm from primero_bach_tres where nombre = '{nombreBach11.get().upper()}'")
                    stock2 = cursor.fetchall()

                    lengua = (stock[0][0] + stock1[0][0] + stock2[0][0]) / 3
                    matematicas = (stock[0][1] + stock1[0][1] + stock2[0][1]) / 3
                    historia = (stock[0][2] + stock1[0][1] + stock2[0][1]) / 3
                    fyq = (stock[0][3] + stock1[0][3] + stock2[0][3]) / 3
                    biologia = (stock[0][4] + stock1[0][4] + stock2[0][4]) / 3
                    economia = (stock[0][5] + stock1[0][5] + stock2[0][5]) / 3
                    frances = (stock[0][6] + stock1[0][6] + stock2[0][6]) / 3
                    ingles = (stock[0][7] + stock1[0][7] + stock2[0][7]) / 3
                    religion = (stock[0][8] + stock1[0][8] + stock2[0][8]) / 3
                    dibujo = (stock[0][9] + stock1[0][9] + stock2[0][9]) / 3
                    ef = (stock[0][10] + stock1[0][10] + stock2[0][10]) / 3
                    informatica = (stock[0][11] + stock1[0][11] + stock2[0][11]) / 3
                    filosofia = (stock[0][12] + stock1[0][12] + stock2[0][12]) / 3
                    cctm = (stock[0][13] + stock1[0][13] + stock2[0][13]) / 3


                    cursor.execute(f"update primero_bach_junio set lengua = '{lengua}' "
                                   f"where  nombre = '{nombreBach11.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set matematicas = '{matematicas}' "
                                   f"where  nombre = '{nombreBach11.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set historia = '{historia}' "
                                   f"where  nombre = '{nombreBach11.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set fyq = '{fyq}' "
                                   f"where  nombre = '{nombreBach11.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set biologia = '{biologia}' "
                                   f"where  nombre = '{nombreBach11.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set economia = '{economia}' "
                                   f"where  nombre = '{nombreBach11.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set frances = '{frances}' "
                                   f"where  nombre = '{nombreBach11.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set ingles = '{ingles}' "
                                   f"where  nombre = '{nombreBach11.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set religion = '{religion}' "
                                   f"where  nombre = '{nombreBach11.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set dibujo_tecnico = '{dibujo}' "
                                   f"where  nombre = '{nombreBach11.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set ef = '{ef}' "
                                   f"where  nombre = '{nombreBach11.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set informatica = '{informatica}' "
                                   f"where  nombre = '{nombreBach11.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set filosofia = '{filosofia}' "
                                   f"where  nombre = '{nombreBach11.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set cctm = '{cctm}' "
                                   f"where  nombre = '{nombreBach11.get().upper()}' ")
                    connexion.commit()

                    lenguaBach11.set("")
                    matesBach11.set("")
                    historiaBach11.set("")
                    fisicayquimicaBach11.set("")
                    biologiaBach11.set("")
                    economiaBach11.set("")
                    francesBach11.set("")
                    inglesBach11.set("")
                    religionBach11.set("")
                    dibujoBach11.set("")
                    efisicaBach11.set("")
                    informaticaBach11.set("")
                    filosofiaBach11.set("")
                    cctmBach11.set("")




                elif nombreId41.get() == 2:

                    if trimestre41.get() == 1:
                        if lenguaBach11.get():
                            cursor.execute(f"update primero_bach_uno set lengua = '{float(lenguaBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesBach11.get():
                            cursor.execute(f"update primero_bach_uno set matematicas = '{float(matesBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaBach11.get():
                            cursor.execute(f"update primero_bach_uno set historia = '{float(historiaBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if fisicayquimicaBach11.get():
                            cursor.execute(f"update primero_bach_uno set fyq = '{float(fisicayquimicaBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if biologiaBach11.get():
                            cursor.execute(f"update primero_bach_uno set biologia = '{float(biologiaBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if economiaBach11.get():
                            cursor.execute(f"update primero_bach_uno set economia = '{float(economiaBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesBach11.get():
                            cursor.execute(f"update primero_bach_uno set frances = '{float(francesBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesBach11.get():
                            cursor.execute(f"update primero_bach_uno set ingles = '{float(inglesBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionBach11.get():
                            cursor.execute(f"update primero_bach_uno set religion = '{float(religionBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if dibujoBach11.get():
                            cursor.execute(f"update primero_bach_uno set dibujo_tecnico = '{float(dibujoBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaBach11.get():
                            cursor.execute(f"update primero_bach_uno set ef = '{float(efisicaBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaBach11.get():
                            cursor.execute(f"update primero_bach_uno set informatica = '{float(informaticaBach11.get())}' "
                                           f"where id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if filosofiaBach11.get():
                            cursor.execute(f"update primero_bach_uno set filosofia = '{float(filosofiaBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if cctmBach11.get():
                            cursor.execute(f"update primero_bach_uno set cctm = '{float(cctmBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass



                    elif trimestre41.get() == 2:
                        if lenguaBach11.get():
                            cursor.execute(f"update primero_bach_dos set lengua = '{float(lenguaBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesBach11.get():
                            cursor.execute(f"update primero_bach_dos set matematicas = '{float(matesBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaBach11.get():
                            cursor.execute(f"update primero_bach_dos set historia = '{float(historiaBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if fisicayquimicaBach11.get():
                            cursor.execute(f"update primero_bach_dos set fyq = '{float(fisicayquimicaBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if biologiaBach11.get():
                            cursor.execute(f"update primero_bach_dos set biologia = '{float(biologiaBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if economiaBach11.get():
                            cursor.execute(f"update primero_bach_dos set economia = '{float(economiaBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesBach11.get():
                            cursor.execute(f"update primero_bach_dos set frances = '{float(francesBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesBach11.get():
                            cursor.execute(f"update primero_bach_dos set ingles = '{float(inglesBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionBach11.get():
                            cursor.execute(f"update primero_bach_dos set religion = '{float(religionBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if dibujoBach11.get():
                            cursor.execute(f"update primero_bach_dos set dibujo_tecnico = '{float(dibujoBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaBach11.get():
                            cursor.execute(f"update primero_bach_dos set ef = '{float(efisicaBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaBach11.get():
                            cursor.execute(f"update primero_bach_dos set informatica = '{float(informaticaBach11.get())}' "
                                           f"where id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if filosofiaBach11.get():
                            cursor.execute(f"update primero_bach_dos set filosofia = '{float(filosofiaBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if cctmBach11.get():
                            cursor.execute(f"update primero_bach_dos set cctm = '{float(cctmBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass


                    elif trimestre41.get() == 3:
                        if lenguaBach11.get():
                            cursor.execute(f"update primero_bach_tres set lengua = '{float(lenguaBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesBach11.get():
                            cursor.execute(f"update primero_bach_tres set matematicas = '{float(matesBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaBach11.get():
                            cursor.execute(f"update primero_bach_tres set historia = '{float(historiaBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if fisicayquimicaBach11.get():
                            cursor.execute(f"update primero_bach_tres set fyq = '{float(fisicayquimicaBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if biologiaBach11.get():
                            cursor.execute(f"update primero_bach_tres set biologia = '{float(biologiaBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if economiaBach11.get():
                            cursor.execute(f"update primero_bach_tres set economia = '{float(economiaBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesBach11.get():
                            cursor.execute(f"update primero_bach_tres set frances = '{float(francesBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesBach11.get():
                            cursor.execute(f"update primero_bach_tres set ingles = '{float(inglesBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionBach11.get():
                            cursor.execute(f"update primero_bach_tres set religion = '{float(religionBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if dibujoBach11.get():
                            cursor.execute(f"update primero_bach_tres set dibujo_tecnico = '{float(dibujoBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaBach11.get():
                            cursor.execute(f"update primero_bach_tres set ef = '{float(efisicaBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaBach11.get():
                            cursor.execute(f"update primero_bach_tres set informatica = '{float(informaticaBach11.get())}' "
                                           f"where id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if filosofiaBach11.get():
                            cursor.execute(f"update primero_bach_tres set filosofia = '{float(filosofiaBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if cctmBach11.get():
                            cursor.execute(f"update primero_bach_tres set cctm = '{float(cctmBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass


                    elif trimestre41.get() == 4:
                        if lenguaBach11.get():
                            cursor.execute(f"update primero_bach_septiembre set lengua = '{float(lenguaBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesBach11.get():
                            cursor.execute(f"update primero_bach_septiembre set matematicas = '{float(matesBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaBach11.get():
                            cursor.execute(f"update primero_bach_septiembre set historia = '{float(historiaBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if fisicayquimicaBach11.get():
                            cursor.execute(f"update primero_bach_septiembre set fyq = '{float(fisicayquimicaBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if biologiaBach11.get():
                            cursor.execute(f"update primero_bach_septiembre set biologia = '{float(biologiaBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if economiaBach11.get():
                            cursor.execute(f"update primero_bach_septiembre set economia = '{float(economiaBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesBach11.get():
                            cursor.execute(f"update primero_bach_septiembre set frances = '{float(francesBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesBach11.get():
                            cursor.execute(f"update primero_bach_septiembre set ingles = '{float(inglesBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionBach11.get():
                            cursor.execute(f"update primero_bach_septiembre set religion = '{float(religionBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if dibujoBach11.get():
                            cursor.execute(f"update primero_bach_septiembre set dibujo_tecnico = '{float(dibujoBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaBach11.get():
                            cursor.execute(f"update primero_bach_septiembre set ef = '{float(efisicaBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaBach11.get():
                            cursor.execute(f"update primero_bach_septiembre set informatica = '{float(informaticaBach11.get())}' "
                                           f"where id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if filosofiaBach11.get():
                            cursor.execute(f"update primero_bach_septiembre set filosofia = '{float(filosofiaBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if cctmBach11.get():
                            cursor.execute(f"update primero_bach_septiembre set cctm = '{float(cctmBach11.get())}' "
                                           f"where  id = '{int(nombreBach11.get())}' ")
                            connexion.commit()
                        else:
                            pass

                    # --------actualizar la tabla de junio----------------------------
                    cursor.execute(
                        f"select lengua, matematicas, historia, fyq, biologia, economia, frances, ingles, religion,"
                        f"dibujo_tecnico, ef, informatica, filosofia, cctm from primero_bach_uno where id = '{int(nombreBach11.get())}'")
                    stock = cursor.fetchall()

                    cursor.execute(
                        f"select lengua, matematicas, historia, fyq, biologia, economia, frances, ingles, religion,"
                        f"dibujo_tecnico, ef, informatica, filosofia, cctm from primero_bach_dos where id = '{int(nombreBach11.get())}'")
                    stock1 = cursor.fetchall()

                    cursor.execute(
                        f"select lengua, matematicas, historia, fyq, biologia, economia, frances, ingles, religion,"
                        f"dibujo_tecnico, ef, informatica, filosofia, cctm from primero_bach_tres where id = '{int(nombreBach11.get())}'")
                    stock2 = cursor.fetchall()

                    lengua = (stock[0][0] + stock1[0][0] + stock2[0][0]) / 3
                    matematicas = (stock[0][1] + stock1[0][1] + stock2[0][1]) / 3
                    historia = (stock[0][2] + stock1[0][1] + stock2[0][1]) / 3
                    fyq = (stock[0][3] + stock1[0][3] + stock2[0][3]) / 3
                    biologia = (stock[0][4] + stock1[0][4] + stock2[0][4]) / 3
                    economia = (stock[0][5] + stock1[0][5] + stock2[0][5]) / 3
                    frances = (stock[0][6] + stock1[0][6] + stock2[0][6]) / 3
                    ingles = (stock[0][7] + stock1[0][7] + stock2[0][7]) / 3
                    religion = (stock[0][8] + stock1[0][8] + stock2[0][8]) / 3
                    dibujo = (stock[0][9] + stock1[0][9] + stock2[0][9]) / 3
                    ef = (stock[0][10] + stock1[0][10] + stock2[0][10]) / 3
                    informatica = (stock[0][11] + stock1[0][11] + stock2[0][11]) / 3
                    filosofia = (stock[0][12] + stock1[0][12] + stock2[0][12]) / 3
                    cctm = (stock[0][13] + stock1[0][13] + stock2[0][13]) / 3

                    cursor.execute(f"update primero_bach_junio set lengua = '{lengua}' "
                                   f"where id = '{int(nombreBach11.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set matematicas = '{matematicas}' "
                                   f"where  id = '{int(nombreBach11.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set historia = '{historia}' "
                                   f"where  id = '{int(nombreBach11.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set fyq = '{fyq}' "
                                   f"where  id = '{int(nombreBach11.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set biologia = '{biologia}' "
                                   f"where id = '{int(nombreBach11.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set economia = '{economia}' "
                                   f"where id = '{int(nombreBach11.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set frances = '{frances}' "
                                   f"where  id = '{int(nombreBach11.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set ingles = '{ingles}' "
                                   f"where  id = '{int(nombreBach11.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set religion = '{religion}' "
                                   f"where  id = '{int(nombreBach11.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set dibujo_tecnico = '{dibujo}' "
                                   f"where  id = '{int(nombreBach11.get())}'")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set ef = '{ef}' "
                                   f"where  id = '{int(nombreBach11.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set informatica = '{informatica}' "
                                   f"where  id = '{int(nombreBach11.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set filosofia = '{filosofia}' "
                                   f"where  id = '{int(nombreBach11.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set cctm = '{cctm}' "
                                   f"where id = '{int(nombreBach11.get())}' ")
                    connexion.commit()

                    lenguaBach11.set("")
                    matesBach11.set("")
                    historiaBach11.set("")
                    fisicayquimicaBach11.set("")
                    biologiaBach11.set("")
                    economiaBach11.set("")
                    francesBach11.set("")
                    inglesBach11.set("")
                    religionBach11.set("")
                    dibujoBach11.set("")
                    efisicaBach11.set("")
                    informaticaBach11.set("")
                    filosofiaBach11.set("")
                    cctmBach11.set("")

                else:
                    pass

                connexion.close()

            except ValueError:
                pass

        except IndexError:
            pass




    def primeroBachTecnologia():
        try:

            try:

                connexion = sqlite3.connect(nameBD.nomBD())
                cursor = connexion.cursor()
                if nombreId42.get() == 1:
                    if trimestre42.get() == 1:
                        if lenguaBach12.get():
                            cursor.execute(f"update primero_bach_uno set lengua = '{float(lenguaBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesBach12.get():
                            cursor.execute(f"update primero_bach_uno set matematicas = '{float(matesBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaBach12.get():
                            cursor.execute(f"update primero_bach_uno set historia = '{float(historiaBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if tecnologiaBach12.get():
                            cursor.execute(f"update primero_bach_uno set tecnologia = '{float(tecnologiaBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if biologiaBach12.get():
                            cursor.execute(f"update primero_bach_uno set biologia = '{float(biologiaBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if economiaBach12.get():
                            cursor.execute(f"update primero_bach_uno set economia = '{float(economiaBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesBach12.get():
                            cursor.execute(f"update primero_bach_uno set frances = '{float(francesBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesBach12.get():
                            cursor.execute(f"update primero_bach_uno set ingles = '{float(inglesBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionBach12.get():
                            cursor.execute(f"update primero_bach_uno set religion = '{float(religionBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if dibujoBach12.get():
                            cursor.execute(f"update primero_bach_uno set dibujo_tecnico = '{float(dibujoBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaBach12.get():
                            cursor.execute(f"update primero_bach_uno set ef = '{float(efisicaBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaBach12.get():
                            cursor.execute(f"update primero_bach_uno set informatica = '{float(informaticaBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if filosofiaBach12.get():
                            cursor.execute(f"update primero_bach_uno set filosofia = '{float(filosofiaBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if cctmBach12.get():
                            cursor.execute(f"update primero_bach_uno set cctm = '{float(cctmBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass



                    elif trimestre42.get() == 2:
                        if lenguaBach12.get():
                            cursor.execute(f"update primero_bach_dos set lengua = '{float(lenguaBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesBach12.get():
                            cursor.execute(f"update primero_bach_dos set matematicas = '{float(matesBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaBach12.get():
                            cursor.execute(f"update primero_bach_dos set historia = '{float(historiaBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if tecnologiaBach12.get():
                            cursor.execute(f"update primero_bach_dos set tecnologia = '{float(tecnologiaBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if biologiaBach12.get():
                            cursor.execute(f"update primero_bach_dos set biologia = '{float(biologiaBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if economiaBach12.get():
                            cursor.execute(f"update primero_bach_dos set economia = '{float(economiaBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesBach12.get():
                            cursor.execute(f"update primero_bach_dos set frances = '{float(francesBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesBach12.get():
                            cursor.execute(f"update primero_bach_dos set ingles = '{float(inglesBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionBach12.get():
                            cursor.execute(f"update primero_bach_dos set religion = '{float(religionBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if dibujoBach12.get():
                            cursor.execute(f"update primero_bach_dos set dibujo_tecnico = '{float(dibujoBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaBach12.get():
                            cursor.execute(f"update primero_bach_dos set ef = '{float(efisicaBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaBach12.get():
                            cursor.execute(f"update primero_bach_dos set informatica = '{float(informaticaBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if filosofiaBach12.get():
                            cursor.execute(f"update primero_bach_dos set filosofia = '{float(filosofiaBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if cctmBach12.get():
                            cursor.execute(f"update primero_bach_dos set cctm = '{float(cctmBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass


                    elif trimestre42.get() == 3:

                        if lenguaBach12.get():
                            cursor.execute(f"update primero_bach_tres set lengua = '{float(lenguaBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesBach12.get():
                            cursor.execute(f"update primero_bach_tres set matematicas = '{float(matesBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaBach12.get():
                            cursor.execute(f"update primero_bach_tres set historia = '{float(historiaBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if tecnologiaBach12.get():
                            cursor.execute(f"update primero_bach_tres set tecnologia = '{float(tecnologiaBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if biologiaBach12.get():
                            cursor.execute(f"update primero_bach_tres set biologia = '{float(biologiaBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if economiaBach12.get():
                            cursor.execute(f"update primero_bach_tres set economia = '{float(economiaBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesBach12.get():
                            cursor.execute(f"update primero_bach_tres set frances = '{float(francesBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesBach12.get():
                            cursor.execute(f"update primero_bach_tres set ingles = '{float(inglesBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionBach12.get():
                            cursor.execute(f"update primero_bach_tres set religion = '{float(religionBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if dibujoBach12.get():
                            cursor.execute(f"update primero_bach_tres set dibujo_tecnico = '{float(dibujoBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaBach12.get():
                            cursor.execute(f"update primero_bach_tres set ef = '{float(efisicaBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaBach12.get():
                            cursor.execute(f"update primero_bach_tres set informatica = '{float(informaticaBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if filosofiaBach12.get():
                            cursor.execute(f"update primero_bach_tres set filosofia = '{float(filosofiaBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if cctmBach12.get():
                            cursor.execute(f"update primero_bach_tres set cctm = '{float(cctmBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass



                    elif trimestre42.get() == 4:
                        if lenguaBach12.get():
                            cursor.execute(f"update primero_bach_septiembre set lengua = '{float(lenguaBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesBach12.get():
                            cursor.execute(f"update primero_bach_septiembre set matematicas = '{float(matesBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaBach12.get():
                            cursor.execute(f"update primero_bach_septiembre set historia = '{float(historiaBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if tecnologiaBach12.get():
                            cursor.execute(f"update primero_bach_septiembre set tecnologia = '{float(tecnologiaBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if biologiaBach12.get():
                            cursor.execute(f"update primero_bach_septiembre set biologia = '{float(biologiaBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if economiaBach12.get():
                            cursor.execute(f"update primero_bach_septiembre set economia = '{float(economiaBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesBach12.get():
                            cursor.execute(f"update primero_bach_septiembre set frances = '{float(francesBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesBach12.get():
                            cursor.execute(f"update primero_bach_septiembre set ingles = '{float(inglesBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionBach12.get():
                            cursor.execute(f"update primero_bach_septiembre set religion = '{float(religionBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if dibujoBach12.get():
                            cursor.execute(f"update primero_bach_septiembre set dibujo_tecnico = '{float(dibujoBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaBach12.get():
                            cursor.execute(f"update primero_bach_septiembre set ef = '{float(efisicaBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaBach12.get():
                            cursor.execute(f"update primero_bach_septiembre set informatica = '{float(informaticaBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if filosofiaBach12.get():
                            cursor.execute(f"update primero_bach_septiembre set filosofia = '{float(filosofiaBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if cctmBach12.get():
                            cursor.execute(f"update primero_bach_septiembre set cctm = '{float(cctmBach12.get())}' "
                                           f"where  nombre = '{nombreBach12.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                    # --------actualizar la tabla de junio----------------------------
                    cursor.execute(
                        f"select lengua, matematicas, historia, tecnologia, biologia, economia, frances, ingles, religion,"
                        f"dibujo_tecnico, ef, informatica, filosofia, cctm from primero_bach_uno where nombre = '{nombreBach12.get().upper()}'")
                    stock = cursor.fetchall()

                    cursor.execute(
                        f"select lengua, matematicas, historia, tecnologia, biologia, economia, frances, ingles, religion,"
                        f"dibujo_tecnico, ef, informatica, filosofia, cctm from primero_bach_dos where nombre = '{nombreBach12.get().upper()}'")
                    stock1 = cursor.fetchall()

                    cursor.execute(
                        f"select lengua, matematicas, historia, tecnologia, biologia, economia, frances, ingles, religion,"
                        f"dibujo_tecnico, ef, informatica, filosofia, cctm from primero_bach_tres where nombre = '{nombreBach12.get().upper()}'")
                    stock2 = cursor.fetchall()

                    lengua = (stock[0][0] + stock1[0][0] + stock2[0][0]) / 3
                    matematicas = (stock[0][1] + stock1[0][1] + stock2[0][1]) / 3
                    historia = (stock[0][2] + stock1[0][1] + stock2[0][1]) / 3
                    tecnologia = (stock[0][3] + stock1[0][3] + stock2[0][3]) / 3
                    biologia = (stock[0][4] + stock1[0][4] + stock2[0][4]) / 3
                    economia = (stock[0][5] + stock1[0][5] + stock2[0][5]) / 3
                    frances = (stock[0][6] + stock1[0][6] + stock2[0][6]) / 3
                    ingles = (stock[0][7] + stock1[0][7] + stock2[0][7]) / 3
                    religion = (stock[0][8] + stock1[0][8] + stock2[0][8]) / 3
                    dibujo = (stock[0][9] + stock1[0][9] + stock2[0][9]) / 3
                    ef = (stock[0][10] + stock1[0][10] + stock2[0][10]) / 3
                    informatica = (stock[0][11] + stock1[0][11] + stock2[0][11]) / 3
                    filosofia = (stock[0][12] + stock1[0][12] + stock2[0][12]) / 3
                    cctm = (stock[0][13] + stock1[0][13] + stock2[0][13]) / 3

                    cursor.execute(f"update primero_bach_junio set lengua = '{lengua}' "
                                   f"where  nombre = '{nombreBach12.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set matematicas = '{matematicas}' "
                                   f"where  nombre = '{nombreBach12.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set historia = '{historia}' "
                                   f"where  nombre = '{nombreBach12.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set tecnologia = '{tecnologia}' "
                                   f"where  nombre = '{nombreBach12.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set biologia = '{biologia}' "
                                   f"where  nombre = '{nombreBach12.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set economia = '{economia}' "
                                   f"where  nombre = '{nombreBach12.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set frances = '{frances}' "
                                   f"where  nombre = '{nombreBach12.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set ingles = '{ingles}' "
                                   f"where  nombre = '{nombreBach12.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set religion = '{religion}' "
                                   f"where  nombre = '{nombreBach12.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set dibujo_tecnico = '{dibujo}' "
                                   f"where  nombre = '{nombreBach12.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set ef = '{ef}' "
                                   f"where  nombre = '{nombreBach12.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set informatica = '{informatica}' "
                                   f"where  nombre = '{nombreBach12.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set filosofia = '{filosofia}' "
                                   f"where  nombre = '{nombreBach12.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set cctm = '{cctm}' "
                                   f"where  nombre = '{nombreBach12.get().upper()}' ")
                    connexion.commit()

                    lenguaBach12.set("")
                    matesBach12.set("")
                    historiaBach12.set("")
                    tecnologiaBach12.set("")
                    biologiaBach12.set("")
                    economiaBach12.set("")
                    francesBach12.set("")
                    inglesBach12.set("")
                    religionBach12.set("")
                    dibujoBach12.set("")
                    efisicaBach12.set("")
                    informaticaBach12.set("")
                    filosofiaBach12.set("")
                    cctmBach12.set("")




                elif nombreId42.get() == 2:

                    if trimestre42.get() == 1:
                        if lenguaBach12.get():
                            cursor.execute(f"update primero_bach_uno set lengua = '{float(lenguaBach12.get())}' "
                                           f"where  id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesBach12.get():
                            cursor.execute(f"update primero_bach_uno set matematicas = '{float(matesBach12.get())}' "
                                           f"where  id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaBach12.get():
                            cursor.execute(f"update primero_bach_uno set historia = '{float(historiaBach12.get())}' "
                                           f"where  id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if tecnologiaBach12.get():
                            cursor.execute(f"update primero_bach_uno set tecnologia = '{float(tecnologiaBach12.get())}' "
                                           f"where  id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if biologiaBach12.get():
                            cursor.execute(f"update primero_bach_uno set biologia = '{float(biologiaBach12.get())}' "
                                           f"where  id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if economiaBach12.get():
                            cursor.execute(f"update primero_bach_uno set economia = '{float(economiaBach12.get())}' "
                                           f"where id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesBach12.get():
                            cursor.execute(f"update primero_bach_uno set frances = '{float(francesBach12.get())}' "
                                           f"where id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesBach12.get():
                            cursor.execute(f"update primero_bach_uno set ingles = '{float(inglesBach12.get())}' "
                                           f"where id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionBach12.get():
                            cursor.execute(f"update primero_bach_uno set religion = '{float(religionBach12.get())}' "
                                           f"where  id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if dibujoBach12.get():
                            cursor.execute(f"update primero_bach_uno set dibujo_tecnico = '{float(dibujoBach12.get())}' "
                                           f"where  id = '{int(nombreBach12.get())}'")
                            connexion.commit()
                        else:
                            pass

                        if efisicaBach12.get():
                            cursor.execute(f"update primero_bach_uno set ef = '{float(efisicaBach12.get())}' "
                                           f"where  id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaBach12.get():
                            cursor.execute(f"update primero_bach_uno set informatica = '{float(informaticaBach12.get())}' "
                                           f"where  id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if filosofiaBach12.get():
                            cursor.execute(f"update primero_bach_uno set filosofia = '{float(filosofiaBach12.get())}' "
                                           f"where  id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if cctmBach12.get():
                            cursor.execute(f"update primero_bach_uno set cctm = '{float(cctmBach12.get())}' "
                                           f"where  id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass



                    elif trimestre42.get() == 2:
                        if lenguaBach12.get():
                            cursor.execute(f"update primero_bach_dos set lengua = '{float(lenguaBach12.get())}' "
                                           f"where  id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesBach12.get():
                            cursor.execute(f"update primero_bach_dos set matematicas = '{float(matesBach12.get())}' "
                                           f"where  id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaBach12.get():
                            cursor.execute(f"update primero_bach_dos set historia = '{float(historiaBach12.get())}' "
                                           f"where  id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if tecnologiaBach12.get():
                            cursor.execute(f"update primero_bach_dos set tecnologia = '{float(tecnologiaBach12.get())}' "
                                           f"where  id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if biologiaBach12.get():
                            cursor.execute(f"update primero_bach_dos set biologia = '{float(biologiaBach12.get())}' "
                                           f"where  id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if economiaBach12.get():
                            cursor.execute(f"update primero_bach_dos set economia = '{float(economiaBach12.get())}' "
                                           f"where id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesBach12.get():
                            cursor.execute(f"update primero_bach_dos set frances = '{float(francesBach12.get())}' "
                                           f"where id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesBach12.get():
                            cursor.execute(f"update primero_bach_dos set ingles = '{float(inglesBach12.get())}' "
                                           f"where id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionBach12.get():
                            cursor.execute(f"update primero_bach_dos set religion = '{float(religionBach12.get())}' "
                                           f"where  id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if dibujoBach12.get():
                            cursor.execute(f"update primero_bach_dos set dibujo_tecnico = '{float(dibujoBach12.get())}' "
                                           f"where  id = '{int(nombreBach12.get())}'")
                            connexion.commit()
                        else:
                            pass

                        if efisicaBach12.get():
                            cursor.execute(f"update primero_bach_dos set ef = '{float(efisicaBach12.get())}' "
                                           f"where  id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaBach12.get():
                            cursor.execute(f"update primero_bach_dos set informatica = '{float(informaticaBach12.get())}' "
                                           f"where  id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if filosofiaBach12.get():
                            cursor.execute(f"update primero_bach_dos set filosofia = '{float(filosofiaBach12.get())}' "
                                           f"where  id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if cctmBach12.get():
                            cursor.execute(f"update primero_bach_dos set cctm = '{float(cctmBach12.get())}' "
                                           f"where  id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass


                    elif trimestre42.get() == 3:

                        if lenguaBach12.get():
                            cursor.execute(f"update primero_bach_tres set lengua = '{float(lenguaBach12.get())}' "
                                           f"where  id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesBach12.get():
                            cursor.execute(f"update primero_bach_tres set matematicas = '{float(matesBach12.get())}' "
                                           f"where  id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaBach12.get():
                            cursor.execute(f"update primero_bach_tres set historia = '{float(historiaBach12.get())}' "
                                           f"where  id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if tecnologiaBach12.get():
                            cursor.execute(f"update primero_bach_tres set tecnologia = '{float(tecnologiaBach12.get())}' "
                                           f"where  id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if biologiaBach12.get():
                            cursor.execute(f"update primero_bach_tres set biologia = '{float(biologiaBach12.get())}' "
                                           f"where  id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if economiaBach12.get():
                            cursor.execute(f"update primero_bach_tres set economia = '{float(economiaBach12.get())}' "
                                           f"where id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesBach12.get():
                            cursor.execute(f"update primero_bach_tres set frances = '{float(francesBach12.get())}' "
                                           f"where id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesBach12.get():
                            cursor.execute(f"update primero_bach_tres set ingles = '{float(inglesBach12.get())}' "
                                           f"where id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionBach12.get():
                            cursor.execute(f"update primero_bach_tres set religion = '{float(religionBach12.get())}' "
                                           f"where  id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if dibujoBach12.get():
                            cursor.execute(f"update primero_bach_tres set dibujo_tecnico = '{float(dibujoBach12.get())}' "
                                           f"where  id = '{int(nombreBach12.get())}'")
                            connexion.commit()
                        else:
                            pass

                        if efisicaBach12.get():
                            cursor.execute(f"update primero_bach_tres set ef = '{float(efisicaBach12.get())}' "
                                           f"where  id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaBach12.get():
                            cursor.execute(f"update primero_bach_tres set informatica = '{float(informaticaBach12.get())}' "
                                           f"where  id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if filosofiaBach12.get():
                            cursor.execute(f"update primero_bach_tres set filosofia = '{float(filosofiaBach12.get())}' "
                                           f"where  id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if cctmBach12.get():
                            cursor.execute(f"update primero_bach_tres set cctm = '{float(cctmBach12.get())}' "
                                           f"where  id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass



                    elif trimestre42.get() == 4:
                        if lenguaBach12.get():
                            cursor.execute(f"update primero_bach_septiembre set lengua = '{float(lenguaBach12.get())}' "
                                           f"where  id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesBach12.get():
                            cursor.execute(f"update primero_bach_septiembre set matematicas = '{float(matesBach12.get())}' "
                                           f"where  id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaBach12.get():
                            cursor.execute(f"update primero_bach_septiembre set historia = '{float(historiaBach12.get())}' "
                                           f"where  id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if tecnologiaBach12.get():
                            cursor.execute(f"update primero_bach_septiembre set tecnologia = '{float(tecnologiaBach12.get())}' "
                                           f"where  id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if biologiaBach12.get():
                            cursor.execute(f"update primero_bach_septiembre set biologia = '{float(biologiaBach12.get())}' "
                                           f"where  id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if economiaBach12.get():
                            cursor.execute(f"update primero_bach_septiembre set economia = '{float(economiaBach12.get())}' "
                                           f"where id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesBach12.get():
                            cursor.execute(f"update primero_bach_septiembre set frances = '{float(francesBach12.get())}' "
                                           f"where id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesBach12.get():
                            cursor.execute(f"update primero_bach_septiembre set ingles = '{float(inglesBach12.get())}' "
                                           f"where id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionBach12.get():
                            cursor.execute(f"update primero_bach_septiembre set religion = '{float(religionBach12.get())}' "
                                           f"where  id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if dibujoBach12.get():
                            cursor.execute(f"update primero_bach_septiembre set dibujo_tecnico = '{float(dibujoBach12.get())}' "
                                           f"where  id = '{int(nombreBach12.get())}'")
                            connexion.commit()
                        else:
                            pass

                        if efisicaBach12.get():
                            cursor.execute(f"update primero_bach_septiembre set ef = '{float(efisicaBach12.get())}' "
                                           f"where  id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaBach12.get():
                            cursor.execute(f"update primero_bach_septiembre set informatica = '{float(informaticaBach12.get())}' "
                                           f"where  id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if filosofiaBach12.get():
                            cursor.execute(f"update primero_bach_septiembre set filosofia = '{float(filosofiaBach12.get())}' "
                                           f"where  id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if cctmBach12.get():
                            cursor.execute(f"update primero_bach_septiembre set cctm = '{float(cctmBach12.get())}' "
                                           f"where  id = '{int(nombreBach12.get())}' ")
                            connexion.commit()
                        else:
                            pass

                    # --------actualizar la tabla de junio----------------------------
                    cursor.execute(
                        f"select lengua, matematicas, historia, tecnologia, biologia, economia, frances, ingles, religion,"
                        f"dibujo_tecnico, ef, informatica, filosofia, cctm from primero_bach_uno where id = '{int(nombreBach12.get())}'")
                    stock = cursor.fetchall()

                    cursor.execute(
                        f"select lengua, matematicas, historia, tecnologia, biologia, economia, frances, ingles, religion,"
                        f"dibujo_tecnico, ef, informatica, filosofia, cctm from primero_bach_dos where id = '{int(nombreBach12.get())}'")
                    stock1 = cursor.fetchall()

                    cursor.execute(
                        f"select lengua, matematicas, historia, tecnologia, biologia, economia, frances, ingles, religion,"
                        f"dibujo_tecnico, ef, informatica, filosofia, cctm from primero_bach_tres where id = '{int(nombreBach12.get())}'")
                    stock2 = cursor.fetchall()

                    lengua = (stock[0][0] + stock1[0][0] + stock2[0][0]) / 3
                    matematicas = (stock[0][1] + stock1[0][1] + stock2[0][1]) / 3
                    historia = (stock[0][2] + stock1[0][1] + stock2[0][1]) / 3
                    tecnologia = (stock[0][3] + stock1[0][3] + stock2[0][3]) / 3
                    biologia = (stock[0][4] + stock1[0][4] + stock2[0][4]) / 3
                    economia = (stock[0][5] + stock1[0][5] + stock2[0][5]) / 3
                    frances = (stock[0][6] + stock1[0][6] + stock2[0][6]) / 3
                    ingles = (stock[0][7] + stock1[0][7] + stock2[0][7]) / 3
                    religion = (stock[0][8] + stock1[0][8] + stock2[0][8]) / 3
                    dibujo = (stock[0][9] + stock1[0][9] + stock2[0][9]) / 3
                    ef = (stock[0][10] + stock1[0][10] + stock2[0][10]) / 3
                    informatica = (stock[0][11] + stock1[0][11] + stock2[0][11]) / 3
                    filosofia = (stock[0][12] + stock1[0][12] + stock2[0][12]) / 3
                    cctm = (stock[0][13] + stock1[0][13] + stock2[0][13]) / 3

                    cursor.execute(f"update primero_bach_junio set lengua = '{lengua}' "
                                   f"where  id = '{int(nombreBach12.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set matematicas = '{matematicas}' "
                                   f"where  id = '{int(nombreBach12.get())}'")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set historia = '{historia}' "
                                   f"where  id = '{int(nombreBach12.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set tecnologia = '{tecnologia}' "
                                   f"where  id = '{int(nombreBach12.get())}'")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set biologia = '{biologia}' "
                                   f"where  id = '{int(nombreBach12.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set economia = '{economia}' "
                                   f"where  id = '{int(nombreBach12.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set frances = '{frances}' "
                                   f"where  id = '{int(nombreBach12.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set ingles = '{ingles}' "
                                   f"where  id = '{int(nombreBach12.get())}'")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set religion = '{religion}' "
                                   f"where  id = '{int(nombreBach12.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set dibujo_tecnico = '{dibujo}' "
                                   f"where  id = '{int(nombreBach12.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set ef = '{ef}' "
                                   f"where  id = '{int(nombreBach12.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set informatica = '{informatica}' "
                                   f"where  id = '{int(nombreBach12.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set filosofia = '{filosofia}' "
                                   f"where  id = '{int(nombreBach12.get())}'")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set cctm = '{cctm}' "
                                   f"where  id = '{int(nombreBach12.get())}' ")
                    connexion.commit()

                    lenguaBach12.set("")
                    matesBach12.set("")
                    historiaBach12.set("")
                    tecnologiaBach12.set("")
                    biologiaBach12.set("")
                    economiaBach12.set("")
                    francesBach12.set("")
                    inglesBach12.set("")
                    religionBach12.set("")
                    dibujoBach12.set("")
                    efisicaBach12.set("")
                    informaticaBach12.set("")
                    filosofiaBach12.set("")
                    cctmBach12.set("")

                else:
                    pass

                connexion.close()

            except ValueError:
                pass

        except IndexError:
            pass



    def primeroBachLetras():
        try:

            try:

                connexion = sqlite3.connect(nameBD.nomBD())
                cursor = connexion.cursor()
                if nombreId43.get() == 1:
                    if trimestre43.get() == 1:
                        if lenguaBach13.get():
                            cursor.execute(f"update primero_bach_uno set lengua = '{float(lenguaBach13.get())}' "
                                           f"where  nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesBach13.get():
                            cursor.execute(f"update primero_bach_uno set mates_aplicadas = '{float(matesBach13.get())}' "
                                           f"where  nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaBach13.get():
                            cursor.execute(f"update primero_bach_uno set historia = '{float(historiaBach13.get())}' "
                                           f"where  nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if geografiaBach13.get():
                            cursor.execute(f"update primero_bach_uno set gge = '{float(geografiaBach13.get())}' "
                                           f"where  nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if latinBach13.get():
                            cursor.execute(f"update primero_bach_uno set latin = '{float(latinBach13.get())}' "
                                           f"where  nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if economiaBach13.get():
                            cursor.execute(f"update primero_bach_uno set economia = '{float(economiaBach13.get())}' "
                                           f"where nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesBach13.get():
                            cursor.execute(f"update primero_bach_uno set frances = '{float(francesBach13.get())}' "
                                           f"where nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesBach13.get():
                            cursor.execute(f"update primero_bach_uno set ingles = '{float(inglesBach13.get())}' "
                                           f"where nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionBach13.get():
                            cursor.execute(f"update primero_bach_uno set religion = '{float(religionBach13.get())}' "
                                           f"where  nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if griegoBach13.get():
                            cursor.execute(f"update primero_bach_uno set griego = '{float(griegoBach13.get())}' "
                                           f"where  nombre = '{nombreBach13.get().upper()}'")
                            connexion.commit()
                        else:
                            pass

                        if efisicaBach13.get():
                            cursor.execute(f"update primero_bach_uno set ef = '{float(efisicaBach13.get())}' "
                                           f"where  nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaBach13.get():
                            cursor.execute(f"update primero_bach_uno set informatica = '{float(informaticaBach13.get())}' "
                                           f"where  nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if filosofiaBach13.get():
                            cursor.execute(f"update primero_bach_uno set filosofia = '{float(filosofiaBach13.get())}' "
                                           f"where  nombre = '{nombreBach13.get().upper()}'")
                            connexion.commit()
                        else:
                            pass

                        if cctmBach13.get():
                            cursor.execute(f"update primero_bach_uno set cctm = '{float(cctmBach13.get())}' "
                                           f"where  nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass



                    elif trimestre43.get() == 2:
                        if lenguaBach13.get():
                            cursor.execute(f"update primero_bach_dos set lengua = '{float(lenguaBach13.get())}' "
                                           f"where nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesBach13.get():
                            cursor.execute(f"update primero_bach_dos set mates_aplicadas = '{float(matesBach13.get())}' "
                                           f"where  nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaBach13.get():
                            cursor.execute(f"update primero_bach_dos set historia = '{float(historiaBach13.get())}' "
                                           f"where  nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if geografiaBach13.get():
                            cursor.execute(f"update primero_bach_dos set gge = '{float(geografiaBach13.get())}' "
                                           f"where  nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if latinBach13.get():
                            cursor.execute(f"update primero_bach_dos set latin = '{float(latinBach13.get())}' "
                                           f"where  nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if economiaBach13.get():
                            cursor.execute(f"update primero_bach_dos set economia = '{float(economiaBach13.get())}' "
                                           f"where nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesBach13.get():
                            cursor.execute(f"update primero_bach_dos set frances = '{float(francesBach13.get())}' "
                                           f"where nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesBach13.get():
                            cursor.execute(f"update primero_bach_dos set ingles = '{float(inglesBach13.get())}' "
                                           f"where nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionBach13.get():
                            cursor.execute(f"update primero_bach_dos set religion = '{float(religionBach13.get())}' "
                                           f"where  nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if griegoBach13.get():
                            cursor.execute(f"update primero_bach_dos set griego = '{float(griegoBach13.get())}' "
                                           f"where nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaBach13.get():
                            cursor.execute(f"update primero_bach_dos set ef = '{float(efisicaBach13.get())}' "
                                           f"where  nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaBach13.get():
                            cursor.execute(f"update primero_bach_dos set informatica = '{float(informaticaBach13.get())}' "
                                           f"where  nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if filosofiaBach13.get():
                            cursor.execute(f"update primero_bach_dos set filosofia = '{float(filosofiaBach13.get())}' "
                                           f"where  nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if cctmBach13.get():
                            cursor.execute(f"update primero_bach_dos set cctm = '{float(cctmBach13.get())}' "
                                           f"where  nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass


                    elif trimestre43.get() == 3:

                        if lenguaBach13.get():
                            cursor.execute(f"update primero_bach_tres set lengua = '{float(lenguaBach13.get())}' "
                                           f"where  nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesBach13.get():
                            cursor.execute(f"update primero_bach_tres set mates_aplicadas = '{float(matesBach13.get())}' "
                                           f"where  nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaBach13.get():
                            cursor.execute(f"update primero_bach_tres set historia = '{float(historiaBach13.get())}' "
                                           f"where  nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if geografiaBach13.get():
                            cursor.execute(f"update primero_bach_tres set gge = '{float(geografiaBach13.get())}' "
                                           f"where nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if latinBach13.get():
                            cursor.execute(f"update primero_bach_tres set latin = '{float(latinBach13.get())}' "
                                           f"where  nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if economiaBach13.get():
                            cursor.execute(f"update primero_bach_tres set economia = '{float(economiaBach13.get())}' "
                                           f"where nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesBach13.get():
                            cursor.execute(f"update primero_bach_tres set frances = '{float(francesBach13.get())}' "
                                           f"where nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesBach13.get():
                            cursor.execute(f"update primero_bach_tres set ingles = '{float(inglesBach13.get())}' "
                                           f"where nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionBach13.get():
                            cursor.execute(f"update primero_bach_tres set religion = '{float(religionBach13.get())}' "
                                           f"where  nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if griegoBach13.get():
                            cursor.execute(f"update primero_bach_tres set griego = '{float(griegoBach13.get())}' "
                                           f"where  nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaBach13.get():
                            cursor.execute(f"update primero_bach_tres set ef = '{float(efisicaBach13.get())}' "
                                           f"where  nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaBach13.get():
                            cursor.execute(f"update primero_bach_tres set informatica = '{float(informaticaBach13.get())}' "
                                           f"where  nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if filosofiaBach13.get():
                            cursor.execute(f"update primero_bach_tres set filosofia = '{float(filosofiaBach13.get())}' "
                                           f"where  nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if cctmBach13.get():
                            cursor.execute(f"update primero_bach_tres set cctm = '{float(cctmBach13.get())}' "
                                           f"where nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass



                    elif trimestre43.get() == 4:
                        if lenguaBach13.get():
                            cursor.execute(f"update primero_bach_septiembre set lengua = '{float(lenguaBach13.get())}' "
                                           f"where  nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesBach13.get():
                            cursor.execute(f"update primero_bach_septiembre set mates_aplicadas = '{float(matesBach13.get())}' "
                                           f"where  nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaBach13.get():
                            cursor.execute(f"update primero_bach_septiembre set historia = '{float(historiaBach13.get())}' "
                                           f"where  nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if geografiaBach13.get():
                            cursor.execute(f"update primero_bach_septiembre set gge = '{float(geografiaBach13.get())}' "
                                           f"where  nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if latinBach13.get():
                            cursor.execute(f"update primero_bach_septiembre set latin = '{float(latinBach13.get())}' "
                                           f"where  nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if economiaBach13.get():
                            cursor.execute(f"update primero_bach_septiembre set economia = '{float(economiaBach13.get())}' "
                                           f"where nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesBach13.get():
                            cursor.execute(f"update primero_bach_septiembre set frances = '{float(francesBach13.get())}' "
                                           f"where nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesBach13.get():
                            cursor.execute(f"update primero_bach_septiembre set ingles = '{float(inglesBach13.get())}' "
                                           f"where nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionBach13.get():
                            cursor.execute(f"update primero_bach_septiembre set religion = '{float(religionBach13.get())}' "
                                           f"where  nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if griegoBach13.get():
                            cursor.execute(f"update primero_bach_septiembre set griego = '{float(griegoBach13.get())}' "
                                           f"where  nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaBach13.get():
                            cursor.execute(f"update primero_bach_septiembre set ef = '{float(efisicaBach13.get())}' "
                                           f"where  nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaBach13.get():
                            cursor.execute(f"update primero_bach_septiembre set informatica = '{float(informaticaBach13.get())}' "
                                           f"where  nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if filosofiaBach13.get():
                            cursor.execute(f"update primero_bach_septiembre set filosofia = '{float(filosofiaBach13.get())}' "
                                           f"where  nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if cctmBach13.get():
                            cursor.execute(f"update primero_bach_septiembre set cctm = '{float(cctmBach13.get())}' "
                                           f"where  nombre = '{nombreBach13.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                    # --------actualizar la tabla de junio----------------------------
                    cursor.execute(
                        f"select lengua, matematicas, historia, gge, latin, economia, frances, ingles, religion,"
                        f"griego, ef, informatica, filosofia, cctm from primero_bach_uno where nombre = '{nombreBach13.get().upper()}' ")
                    stock = cursor.fetchall()

                    cursor.execute(
                        f"select lengua, matematicas, historia, gge, latin, economia, frances, ingles, religion,"
                        f"griego, ef, informatica, filosofia, cctm from primero_bach_dos where nombre = '{nombreBach13.get().upper()}'")
                    stock1 = cursor.fetchall()

                    cursor.execute(
                        f"select lengua, matematicas, historia, gge, latin, economia, frances, ingles, religion,"
                        f"griego, ef, informatica, filosofia, cctm from primero_bach_tres where nombre = '{nombreBach13.get().upper()}' ")
                    stock2 = cursor.fetchall()

                    lengua = (stock[0][0] + stock1[0][0] + stock2[0][0]) / 3
                    matematicas = (stock[0][1] + stock1[0][1] + stock2[0][1]) / 3
                    historia = (stock[0][2] + stock1[0][1] + stock2[0][1]) / 3
                    gge = (stock[0][3] + stock1[0][3] + stock2[0][3]) / 3
                    latin = (stock[0][4] + stock1[0][4] + stock2[0][4]) / 3
                    economia = (stock[0][5] + stock1[0][5] + stock2[0][5]) / 3
                    frances = (stock[0][6] + stock1[0][6] + stock2[0][6]) / 3
                    ingles = (stock[0][7] + stock1[0][7] + stock2[0][7]) / 3
                    religion = (stock[0][8] + stock1[0][8] + stock2[0][8]) / 3
                    griego = (stock[0][9] + stock1[0][9] + stock2[0][9]) / 3
                    ef = (stock[0][10] + stock1[0][10] + stock2[0][10]) / 3
                    informatica = (stock[0][11] + stock1[0][11] + stock2[0][11]) / 3
                    filosofia = (stock[0][12] + stock1[0][12] + stock2[0][12]) / 3
                    cctm = (stock[0][13] + stock1[0][13] + stock2[0][13]) / 3

                    cursor.execute(f"update primero_bach_junio set lengua = '{lengua}' "
                                   f"where  nombre = '{nombreBach13.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set mates_aplicadas = '{matematicas}' "
                                   f"where  nombre = '{nombreBach13.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set historia = '{historia}' "
                                   f"where  nombre = '{nombreBach13.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set gge = '{gge}' "
                                   f"where  nombre = '{nombreBach13.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set latin = '{latin}' "
                                   f"where  nombre = '{nombreBach13.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set economia = '{economia}' "
                                   f"where  nombre = '{nombreBach13.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set frances = '{frances}' "
                                   f"where  nombre = '{nombreBach13.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set ingles = '{ingles}' "
                                   f"where  nombre = '{nombreBach13.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set religion = '{religion}' "
                                   f"where  nombre = '{nombreBach13.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set griego = '{griego}' "
                                   f"where  nombre = '{nombreBach13.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set ef = '{ef}' "
                                   f"where  nombre = '{nombreBach13.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set informatica = '{informatica}' "
                                   f"where  nombre = '{nombreBach13.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set filosofia = '{filosofia}' "
                                   f"where nombre = '{nombreBach13.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set cctm = '{cctm}' "
                                   f"where  nombre = '{nombreBach13.get().upper()}' ")
                    connexion.commit()

                    lenguaBach13.set("")
                    matesBach13.set("")
                    historiaBach13.set("")
                    geografiaBach13.set("")
                    latinBach13.set("")
                    economiaBach13.set("")
                    francesBach13.set("")
                    inglesBach13.set("")
                    religionBach13.set("")
                    griegoBach13.set("")
                    efisicaBach13.set("")
                    informaticaBach13.set("")
                    filosofiaBach13.set("")
                    cctmBach13.set("")




                elif nombreId43.get() == 2:

                    if trimestre43.get() == 1:
                        if lenguaBach13.get():
                            cursor.execute(f"update primero_bach_uno set lengua = '{float(lenguaBach13.get())}' "
                                           f"where  id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesBach13.get():
                            cursor.execute(f"update primero_bach_uno set mates_aplicadas = '{float(matesBach13.get())}' "
                                           f"where  id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaBach13.get():
                            cursor.execute(f"update primero_bach_uno set historia = '{float(historiaBach13.get())}' "
                                           f"where  id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if geografiaBach13.get():
                            cursor.execute(f"update primero_bach_uno set gge = '{float(geografiaBach13.get())}' "
                                           f"where  id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if latinBach13.get():
                            cursor.execute(f"update primero_bach_uno set latin = '{float(latinBach13.get())}' "
                                           f"where  id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if economiaBach13.get():
                            cursor.execute(f"update primero_bach_uno set economia = '{float(economiaBach13.get())}' "
                                           f"where id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesBach13.get():
                            cursor.execute(f"update primero_bach_uno set frances = '{float(francesBach13.get())}' "
                                           f"where id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesBach13.get():
                            cursor.execute(f"update primero_bach_uno set ingles = '{float(inglesBach13.get())}' "
                                           f"where id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionBach13.get():
                            cursor.execute(f"update primero_bach_uno set religion = '{float(religionBach13.get())}' "
                                           f"where  id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if griegoBach13.get():
                            cursor.execute(f"update primero_bach_uno set griego = '{float(griegoBach13.get())}' "
                                           f"where  id = '{int(nombreBach13.get())}'")
                            connexion.commit()
                        else:
                            pass

                        if efisicaBach13.get():
                            cursor.execute(f"update primero_bach_uno set ef = '{float(efisicaBach13.get())}' "
                                           f"where  id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaBach13.get():
                            cursor.execute(f"update primero_bach_uno set informatica = '{float(informaticaBach13.get())}' "
                                           f"where  id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if filosofiaBach13.get():
                            cursor.execute(f"update primero_bach_uno set filosofia = '{float(filosofiaBach13.get())}' "
                                           f"where  id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if cctmBach13.get():
                            cursor.execute(f"update primero_bach_uno set cctm = '{float(cctmBach13.get())}' "
                                           f"where  id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass



                    elif trimestre43.get() == 2:
                        if lenguaBach13.get():
                            cursor.execute(f"update primero_bach_dos set lengua = '{float(lenguaBach13.get())}' "
                                           f"where  id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesBach13.get():
                            cursor.execute(f"update primero_bach_dos set mates_aplicadas = '{float(matesBach13.get())}' "
                                           f"where  id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaBach13.get():
                            cursor.execute(f"update primero_bach_dos set historia = '{float(historiaBach13.get())}' "
                                           f"where  id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if geografiaBach13.get():
                            cursor.execute(f"update primero_bach_dos set gge = '{float(geografiaBach13.get())}' "
                                           f"where  id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if latinBach13.get():
                            cursor.execute(f"update primero_bach_dos set latin = '{float(latinBach13.get())}' "
                                           f"where  id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if economiaBach13.get():
                            cursor.execute(f"update primero_bach_dos set economia = '{float(economiaBach13.get())}' "
                                           f"where id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesBach13.get():
                            cursor.execute(f"update primero_bach_dos set frances = '{float(francesBach13.get())}' "
                                           f"where id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesBach13.get():
                            cursor.execute(f"update primero_bach_dos set ingles = '{float(inglesBach13.get())}' "
                                           f"where id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionBach13.get():
                            cursor.execute(f"update primero_bach_dos set religion = '{float(religionBach13.get())}' "
                                           f"where  id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if griegoBach13.get():
                            cursor.execute(f"update primero_bach_dos set griego = '{float(griegoBach13.get())}' "
                                           f"where  id = '{int(nombreBach13.get())}'")
                            connexion.commit()
                        else:
                            pass

                        if efisicaBach13.get():
                            cursor.execute(f"update primero_bach_dos set ef = '{float(efisicaBach13.get())}' "
                                           f"where  id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaBach13.get():
                            cursor.execute(f"update primero_bach_dos set informatica = '{float(informaticaBach13.get())}' "
                                           f"where  id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if filosofiaBach13.get():
                            cursor.execute(f"update primero_bach_dos set filosofia = '{float(filosofiaBach13.get())}' "
                                           f"where  id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if cctmBach13.get():
                            cursor.execute(f"update primero_bach_dos set cctm = '{float(cctmBach13.get())}' "
                                           f"where  id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass


                    elif trimestre43.get() == 3:

                        if lenguaBach13.get():
                            cursor.execute(f"update primero_bach_tres set lengua = '{float(lenguaBach13.get())}' "
                                           f"where  id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesBach13.get():
                            cursor.execute(f"update primero_bach_tres set mates_aplicadas = '{float(matesBach13.get())}' "
                                           f"where  id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaBach13.get():
                            cursor.execute(f"update primero_bach_tres set historia = '{float(historiaBach13.get())}' "
                                           f"where  id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if geografiaBach13.get():
                            cursor.execute(f"update primero_bach_tres set gge = '{float(geografiaBach13.get())}' "
                                           f"where  id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if latinBach13.get():
                            cursor.execute(f"update primero_bach_tres set latin = '{float(latinBach13.get())}' "
                                           f"where  id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if economiaBach13.get():
                            cursor.execute(f"update primero_bach_tres set economia = '{float(economiaBach13.get())}' "
                                           f"where id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesBach13.get():
                            cursor.execute(f"update primero_bach_tres set frances = '{float(francesBach13.get())}' "
                                           f"where id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesBach13.get():
                            cursor.execute(f"update primero_bach_tres set ingles = '{float(inglesBach13.get())}' "
                                           f"where id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionBach13.get():
                            cursor.execute(f"update primero_bach_tres set religion = '{float(religionBach13.get())}' "
                                           f"where  id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if griegoBach13.get():
                            cursor.execute(f"update primero_bach_tres set griego = '{float(griegoBach13.get())}' "
                                           f"where  id = '{int(nombreBach13.get())}'")
                            connexion.commit()
                        else:
                            pass

                        if efisicaBach13.get():
                            cursor.execute(f"update primero_bach_tres set ef = '{float(efisicaBach13.get())}' "
                                           f"where  id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaBach13.get():
                            cursor.execute(f"update primero_bach_tres set informatica = '{float(informaticaBach13.get())}' "
                                           f"where  id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if filosofiaBach13.get():
                            cursor.execute(f"update primero_bach_tres set filosofia = '{float(filosofiaBach13.get())}' "
                                           f"where  id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if cctmBach13.get():
                            cursor.execute(f"update primero_bach_tres set cctm = '{float(cctmBach13.get())}' "
                                           f"where  id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass



                    elif trimestre43.get() == 4:
                        if lenguaBach13.get():
                            cursor.execute(f"update primero_bach_septiembre set lengua = '{float(lenguaBach13.get())}' "
                                           f"where  id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesBach13.get():
                            cursor.execute(f"update primero_bach_septiembre set mates_aplicadas = '{float(matesBach13.get())}' "
                                           f"where  id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaBach13.get():
                            cursor.execute(f"update primero_bach_septiembre set historia = '{float(historiaBach13.get())}' "
                                           f"where  id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if geografiaBach13.get():
                            cursor.execute(f"update primero_bach_septiembre set gge = '{float(geografiaBach13.get())}' "
                                           f"where  id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if latinBach13.get():
                            cursor.execute(f"update primero_bach_septiembre set latin = '{float(latinBach13.get())}' "
                                           f"where  id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if economiaBach13.get():
                            cursor.execute(f"update primero_bach_septiembre set economia = '{float(economiaBach13.get())}' "
                                           f"where id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesBach13.get():
                            cursor.execute(f"update primero_bach_septiembre set frances = '{float(francesBach13.get())}' "
                                           f"where id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesBach13.get():
                            cursor.execute(f"update primero_bach_septiembre set ingles = '{float(inglesBach13.get())}' "
                                           f"where id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionBach13.get():
                            cursor.execute(f"update primero_bach_septiembre set religion = '{float(religionBach13.get())}' "
                                           f"where  id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if griegoBach13.get():
                            cursor.execute(f"update primero_bach_septiembre set griego = '{float(griegoBach13.get())}' "
                                           f"where  id = '{int(nombreBach13.get())}'")
                            connexion.commit()
                        else:
                            pass

                        if efisicaBach13.get():
                            cursor.execute(f"update primero_bach_septiembre set ef = '{float(efisicaBach13.get())}' "
                                           f"where  id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaBach13.get():
                            cursor.execute(f"update primero_bach_septiembre set informatica = '{float(informaticaBach13.get())}' "
                                           f"where  id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if filosofiaBach13.get():
                            cursor.execute(f"update primero_bach_septiembre set filosofia = '{float(filosofiaBach13.get())}' "
                                           f"where  id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if cctmBach13.get():
                            cursor.execute(f"update primero_bach_septiembre set cctm = '{float(cctmBach13.get())}' "
                                           f"where  id = '{int(nombreBach13.get())}' ")
                            connexion.commit()
                        else:
                            pass

                    # --------actualizar la tabla de junio----------------------------
                    cursor.execute(
                        f"select lengua, matematicas, historia, gge, latin, economia, frances, ingles, religion,"
                        f"griego, ef, informatica, filosofia, cctm from primero_bach_uno where id = '{int(nombreBach13.get())}'")
                    stock = cursor.fetchall()

                    cursor.execute(
                        f"select lengua, matematicas, historia, gge, latin, economia, frances, ingles, religion,"
                        f"griego, ef, informatica, filosofia, cctm from primero_bach_dos where id = '{int(nombreBach13.get())}' ")
                    stock1 = cursor.fetchall()

                    cursor.execute(
                        f"select lengua, matematicas, historia, gge, latin, economia, frances, ingles, religion,"
                        f"griego, ef, informatica, filosofia, cctm from primero_bach_tres where id = '{int(nombreBach13.get())}'")
                    stock2 = cursor.fetchall()

                    lengua = (stock[0][0] + stock1[0][0] + stock2[0][0]) / 3
                    matematicas = (stock[0][1] + stock1[0][1] + stock2[0][1]) / 3
                    historia = (stock[0][2] + stock1[0][1] + stock2[0][1]) / 3
                    gge = (stock[0][3] + stock1[0][3] + stock2[0][3]) / 3
                    latin = (stock[0][4] + stock1[0][4] + stock2[0][4]) / 3
                    economia = (stock[0][5] + stock1[0][5] + stock2[0][5]) / 3
                    frances = (stock[0][6] + stock1[0][6] + stock2[0][6]) / 3
                    ingles = (stock[0][7] + stock1[0][7] + stock2[0][7]) / 3
                    religion = (stock[0][8] + stock1[0][8] + stock2[0][8]) / 3
                    griego = (stock[0][9] + stock1[0][9] + stock2[0][9]) / 3
                    ef = (stock[0][10] + stock1[0][10] + stock2[0][10]) / 3
                    informatica = (stock[0][11] + stock1[0][11] + stock2[0][11]) / 3
                    filosofia = (stock[0][12] + stock1[0][12] + stock2[0][12]) / 3
                    cctm = (stock[0][13] + stock1[0][13] + stock2[0][13]) / 3

                    cursor.execute(f"update primero_bach_junio set lengua = '{lengua}' "
                                   f"where  id = '{int(nombreBach12.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set mates_aplicadas = '{matematicas}' "
                                   f"where  id = '{int(nombreBach12.get())}'")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set historia = '{historia}' "
                                   f"where  id = '{int(nombreBach12.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set gge = '{gge}' "
                                   f"where  id = '{int(nombreBach12.get())}'")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set latin = '{latin}' "
                                   f"where  id = '{int(nombreBach12.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set economia = '{economia}' "
                                   f"where  id = '{int(nombreBach12.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set frances = '{frances}' "
                                   f"where  id = '{int(nombreBach12.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set ingles = '{ingles}' "
                                   f"where  id = '{int(nombreBach12.get())}'")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set religion = '{religion}' "
                                   f"where  id = '{int(nombreBach12.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set griego = '{griego}' "
                                   f"where  id = '{int(nombreBach12.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set ef = '{ef}' "
                                   f"where  id = '{int(nombreBach12.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set informatica = '{informatica}' "
                                   f"where  id = '{int(nombreBach12.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set filosofia = '{filosofia}' "
                                   f"where  id = '{int(nombreBach12.get())}'")
                    connexion.commit()

                    cursor.execute(f"update primero_bach_junio set cctm = '{cctm}' "
                                   f"where  id = '{int(nombreBach12.get())}' ")
                    connexion.commit()

                    lenguaBach13.set("")
                    matesBach13.set("")
                    historiaBach13.set("")
                    geografiaBach13.set("")
                    latinBach13.set("")
                    economiaBach13.set("")
                    francesBach13.set("")
                    inglesBach13.set("")
                    religionBach13.set("")
                    griegoBach13.set("")
                    efisicaBach13.set("")
                    informaticaBach13.set("")
                    filosofiaBach13.set("")
                    cctmBach13.set("")

                else:
                    pass

                connexion.close()

            except ValueError:
                pass

        except IndexError:
            pass



    def segundoBachCiencias():

        try:


            try:


                connexion = sqlite3.connect(nameBD.nomBD())
                cursor = connexion.cursor()
                if nombreId51.get() == 1:
                    if trimestre51.get() == 1:
                        if lenguaBach21.get():
                            cursor.execute(f"update segundo_bach_uno set lengua = '{float(lenguaBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesBach21.get():
                            cursor.execute(f"update segundo_bach_uno set matematicas = '{float(matesBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaBach21.get():
                            cursor.execute(f"update segundo_bach_uno set historia = '{float(historiaBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if quimicaBach21.get():
                            cursor.execute(f"update segundo_bach_uno set quimica = '{float(quimicaBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if geologiaBach21.get():
                            cursor.execute(f"update segundo_bach_uno set geologia = '{float(geologiaBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if economiaBach21.get():
                            cursor.execute(f"update segundo_bach_uno set economia = '{float(economiaBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesBach21.get():
                            cursor.execute(f"update segundo_bach_uno set frances = '{float(francesBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesBach21.get():
                            cursor.execute(f"update segundo_bach_uno set ingles = '{float(inglesBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionBach21.get():
                            cursor.execute(f"update segundo_bach_uno set religion = '{float(religionBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if electrotecniaBach21.get():
                            cursor.execute(f"update segundo_bach_uno set electrotecnia = '{float(electrotecniaBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaBach21.get():
                            cursor.execute(f"update segundo_bach_uno set ef = '{float(efisicaBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaBach21.get():
                            cursor.execute(f"update segundo_bach_uno set informatica = '{float(informaticaBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if filosofiaBach21.get():
                            cursor.execute(f"update segundo_bach_uno set filosofia = '{float(filosofiaBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass


                        if cnsBach21.get():
                            cursor.execute(f"update segundo_bach_uno set cns = '{float(cnsBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass



                    elif trimestre51.get() == 2:
                        if lenguaBach21.get():
                            cursor.execute(f"update segundo_bach_dos set lengua = '{float(lenguaBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesBach21.get():
                            cursor.execute(f"update segundo_bach_dos set matematicas = '{float(matesBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaBach21.get():
                            cursor.execute(f"update segundo_bach_dos set historia = '{float(historiaBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if quimicaBach21.get():
                            cursor.execute(f"update segundo_bach_dos set quimica = '{float(quimicaBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if geologiaBach21.get():
                            cursor.execute(f"update segundo_bach_dos set geologia = '{float(geologiaBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if economiaBach21.get():
                            cursor.execute(f"update segundo_bach_dos set economia = '{float(economiaBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesBach21.get():
                            cursor.execute(f"update segundo_bach_dos set frances = '{float(francesBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesBach21.get():
                            cursor.execute(f"update segundo_bach_dos set ingles = '{float(inglesBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionBach21.get():
                            cursor.execute(f"update segundo_bach_dos set religion = '{float(religionBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if electrotecniaBach21.get():
                            cursor.execute(f"update segundo_bach_dos set electrotecnia = '{float(electrotecniaBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaBach21.get():
                            cursor.execute(f"update segundo_bach_dos set ef = '{float(efisicaBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaBach21.get():
                            cursor.execute(f"update segundo_bach_dos set informatica = '{float(informaticaBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if filosofiaBach21.get():
                            cursor.execute(f"update segundo_bach_dos set filosofia = '{float(filosofiaBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass


                        if cnsBach21.get():
                            cursor.execute(f"update segundo_bach_dos set cns = '{float(cnsBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass


                    elif trimestre51.get() == 3:
                        if lenguaBach21.get():
                            cursor.execute(f"update segundo_bach_tres set lengua = '{float(lenguaBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesBach21.get():
                            cursor.execute(f"update segundo_bach_tres set matematicas = '{float(matesBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaBach21.get():
                            cursor.execute(f"update segundo_bach_tres set historia = '{float(historiaBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if quimicaBach21.get():
                            cursor.execute(f"update segundo_bach_tres set quimica = '{float(quimicaBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if geologiaBach21.get():
                            cursor.execute(f"update segundo_bach_tres set geologia = '{float(geologiaBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if economiaBach21.get():
                            cursor.execute(f"update segundo_bach_tres set economia = '{float(economiaBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesBach21.get():
                            cursor.execute(f"update segundo_bach_tres set frances = '{float(francesBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesBach21.get():
                            cursor.execute(f"update segundo_bach_tres set ingles = '{float(inglesBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionBach21.get():
                            cursor.execute(f"update segundo_bach_tres set religion = '{float(religionBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if electrotecniaBach21.get():
                            cursor.execute(f"update segundo_bach_tres set electrotecnia = '{float(electrotecniaBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaBach21.get():
                            cursor.execute(f"update segundo_bach_tres set ef = '{float(efisicaBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaBach21.get():
                            cursor.execute(f"update segundo_bach_tres set informatica = '{float(informaticaBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if filosofiaBach21.get():
                            cursor.execute(f"update segundo_bach_tres set filosofia = '{float(filosofiaBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass


                        if cnsBach21.get():
                            cursor.execute(f"update segundo_bach_tres set cns = '{float(cnsBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass


                    elif trimestre51.get() == 4:
                        if lenguaBach21.get():
                            cursor.execute(f"update segundo_bach_septiembre set lengua = '{float(lenguaBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesBach21.get():
                            cursor.execute(f"update segundo_bach_septiembre set matematicas = '{float(matesBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaBach21.get():
                            cursor.execute(f"update segundo_bach_septiembre set historia = '{float(historiaBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if quimicaBach21.get():
                            cursor.execute(f"update segundo_bach_septiembre set quimica = '{float(quimicaBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if geologiaBach21.get():
                            cursor.execute(f"update segundo_bach_septiembre set geologia = '{float(geologiaBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if economiaBach21.get():
                            cursor.execute(f"update segundo_bach_septiembre set economia = '{float(economiaBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesBach21.get():
                            cursor.execute(f"update segundo_bach_septiembre set frances = '{float(francesBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesBach21.get():
                            cursor.execute(f"update segundo_bach_septiembre set ingles = '{float(inglesBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionBach21.get():
                            cursor.execute(f"update segundo_bach_septiembre set religion = '{float(religionBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if electrotecniaBach21.get():
                            cursor.execute(f"update segundo_bach_septiembre set electrotecnia = '{float(electrotecniaBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaBach21.get():
                            cursor.execute(f"update segundo_bach_septiembre set ef = '{float(efisicaBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaBach21.get():
                            cursor.execute(f"update segundo_bach_septiembre set informatica = '{float(informaticaBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if filosofiaBach21.get():
                            cursor.execute(f"update segundo_bach_septiembre set filosofia = '{float(filosofiaBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass


                        if cnsBach21.get():
                            cursor.execute(f"update segundo_bach_septiembre set cns = '{float(cnsBach21.get())}' "
                                           f"where  nombre = '{nombreBach21.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass


                    # --------actualizar la tabla de junio----------------------------

                    cursor.execute(f"select lengua, matematicas, historia, quimica, geologia, economia, frances, ingles, religion,"
                                   f"electrotecnia, ef, informatica, filosofia, cns from segundo_bach_uno where nombre = '{nombreBach21.get().upper()}' ")
                    stock = cursor.fetchall()

                    cursor.execute(f"select lengua, matematicas, historia, quimica, geologia, economia, frances, ingles, religion,"
                                   f"electrotecnia, ef, informatica, filosofia, cns from segundo_bach_dos where nombre = '{nombreBach21.get().upper()}' ")
                    stock1 = cursor.fetchall()

                    cursor.execute(f"select lengua, matematicas, historia, quimica, geologia, economia, frances, ingles, religion,"
                                   f"electrotecnia, ef, informatica, filosofia, cns from segundo_bach_tres where nombre = '{nombreBach21.get().upper()}'")
                    stock2 = cursor.fetchall()

                    lengua = (stock[0][0] + stock1[0][0] + stock2[0][0]) / 3
                    matematicas = (stock[0][1] + stock1[0][1] + stock2[0][1]) / 3
                    historia = (stock[0][2] + stock1[0][1] + stock2[0][1]) / 3
                    quimica = (stock[0][3] + stock1[0][3] + stock2[0][3]) / 3
                    geologia = (stock[0][4] + stock1[0][4] + stock2[0][4]) / 3
                    economia = (stock[0][5] + stock1[0][5] + stock2[0][5]) / 3
                    frances = (stock[0][6] + stock1[0][6] + stock2[0][6]) / 3
                    ingles = (stock[0][7] + stock1[0][7] + stock2[0][7]) / 3
                    religion = (stock[0][8] + stock1[0][8] + stock2[0][8]) / 3
                    electrotecnia = (stock[0][9] + stock1[0][9] + stock2[0][9]) / 3
                    ef = (stock[0][10] + stock1[0][10] + stock2[0][10]) / 3
                    informatica = (stock[0][11] + stock1[0][11] + stock2[0][11]) / 3
                    filosofia = (stock[0][12] + stock1[0][12] + stock2[0][12]) / 3
                    cns = (stock[0][13] + stock1[0][13] + stock2[0][13]) / 3


                    cursor.execute(f"update segundo_bach_junio set lengua = '{lengua}' "
                                   f"where  nombre = '{nombreBach21.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set matematicas = '{matematicas}' "
                                   f"where  nombre = '{nombreBach21.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set historia = '{historia}' "
                                   f"where  nombre = '{nombreBach21.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set quimica = '{quimica}' "
                                   f"where  nombre = '{nombreBach21.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set geologia = '{geologia}' "
                                   f"where  nombre = '{nombreBach21.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set economia = '{economia}' "
                                   f"where  nombre = '{nombreBach21.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set frances = '{frances}' "
                                   f"where  nombre = '{nombreBach21.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set ingles = '{ingles}' "
                                   f"where  nombre = '{nombreBach21.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set religion = '{religion}' "
                                   f"where  nombre = '{nombreBach21.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set electrotecnia = '{electrotecnia}' "
                                   f"where  nombre = '{nombreBach21.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set ef = '{ef}' "
                                   f"where  nombre = '{nombreBach21.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set informatica = '{informatica}' "
                                   f"where  nombre = '{nombreBach21.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set filosofia = '{filosofia}' "
                                   f"where  nombre = '{nombreBach21.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set cns = '{cns}' "
                                   f"where  nombre = '{nombreBach21.get().upper()}' ")
                    connexion.commit()


                    lenguaBach21.set("")
                    matesBach21.set("")
                    historiaBach21.set("")
                    quimicaBach21.set("")
                    geologiaBach21.set("")
                    economiaBach21.set("")
                    francesBach21.set("")
                    inglesBach21.set("")
                    religionBach21.set("")
                    electrotecniaBach21.set("")
                    efisicaBach21.set("")
                    informaticaBach21.set("")
                    filosofiaBach21.set("")
                    cnsBach21.set("")




                elif nombreId51.get() == 2:

                    if trimestre51.get() == 1:
                        if lenguaBach21.get():
                            cursor.execute(f"update segundo_bach_uno set lengua = '{float(lenguaBach21.get())}' "
                                           f"where  id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesBach21.get():
                            cursor.execute(f"update segundo_bach_uno set matematicas = '{float(matesBach21.get())}' "
                                           f"where  id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaBach21.get():
                            cursor.execute(f"update segundo_bach_uno set historia = '{float(historiaBach21.get())}' "
                                           f"where  id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if quimicaBach21.get():
                            cursor.execute(f"update segundo_bach_uno set quimica = '{float(quimicaBach21.get())}' "
                                           f"where  id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if geologiaBach21.get():
                            cursor.execute(f"update segundo_bach_uno set geologia = '{float(geologiaBach21.get())}' "
                                           f"where  id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if economiaBach21.get():
                            cursor.execute(f"update segundo_bach_uno set economia = '{float(economiaBach21.get())}' "
                                           f"where  id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesBach21.get():
                            cursor.execute(f"update segundo_bach_uno set frances = '{float(francesBach21.get())}' "
                                           f"where  id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesBach21.get():
                            cursor.execute(f"update segundo_bach_uno set ingles = '{float(inglesBach21.get())}' "
                                           f"where  id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionBach21.get():
                            cursor.execute(f"update segundo_bach_uno set religion = '{float(religionBach21.get())}' "
                                           f"where  id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if electrotecniaBach21.get():
                            cursor.execute(f"update segundo_bach_uno set electrotecnia = '{float(electrotecniaBach21.get())}' "
                                           f"where  id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaBach21.get():
                            cursor.execute(f"update segundo_bach_uno set ef = '{float(efisicaBach21.get())}' "
                                           f"where  id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaBach21.get():
                            cursor.execute(f"update segundo_bach_uno set informatica = '{float(informaticaBach21.get())}' "
                                           f"where  id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if filosofiaBach21.get():
                            cursor.execute(f"update segundo_bach_uno set filosofia = '{float(filosofiaBach21.get())}' "
                                           f"where id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass


                        if cnsBach21.get():
                            cursor.execute(f"update segundo_bach_uno set cns = '{float(cnsBach21.get())}' "
                                           f"where id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass



                    elif trimestre51.get() == 2:
                        if lenguaBach21.get():
                            cursor.execute(f"update segundo_bach_dos set lengua = '{float(lenguaBach21.get())}' "
                                           f"where id = '{int(nombreBach21.get())}'")
                            connexion.commit()
                        else:
                            pass

                        if matesBach21.get():
                            cursor.execute(f"update segundo_bach_dos set matematicas = '{float(matesBach21.get())}' "
                                           f"where  id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaBach21.get():
                            cursor.execute(f"update segundo_bach_dos set historia = '{float(historiaBach21.get())}' "
                                           f"where  id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if quimicaBach21.get():
                            cursor.execute(f"update segundo_bach_dos set quimica = '{float(quimicaBach21.get())}' "
                                           f"where  id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if geologiaBach21.get():
                            cursor.execute(f"update segundo_bach_dos set geologia = '{float(geologiaBach21.get())}' "
                                           f"where id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if economiaBach21.get():
                            cursor.execute(f"update segundo_bach_dos set economia = '{float(economiaBach21.get())}' "
                                           f"where  id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesBach21.get():
                            cursor.execute(f"update segundo_bach_dos set frances = '{float(francesBach21.get())}' "
                                           f"where  id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesBach21.get():
                            cursor.execute(f"update segundo_bach_dos set ingles = '{float(inglesBach21.get())}' "
                                           f"where  id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionBach21.get():
                            cursor.execute(f"update segundo_bach_dos set religion = '{float(religionBach21.get())}' "
                                           f"where  id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if electrotecniaBach21.get():
                            cursor.execute(f"update segundo_bach_dos set electrotecnia = '{float(electrotecniaBach21.get())}' "
                                           f"where  id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaBach21.get():
                            cursor.execute(f"update segundo_bach_dos set ef = '{float(efisicaBach21.get())}' "
                                           f"where  id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaBach21.get():
                            cursor.execute(f"update segundo_bach_dos set informatica = '{float(informaticaBach21.get())}' "
                                           f"where  id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if filosofiaBach21.get():
                            cursor.execute(f"update segundo_bach_dos set filosofia = '{float(filosofiaBach21.get())}' "
                                           f"where  id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass


                        if cnsBach21.get():
                            cursor.execute(f"update segundo_bach_dos set cns = '{float(cnsBach21.get())}' "
                                           f"where  id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass


                    elif trimestre51.get() == 3:
                        if lenguaBach21.get():
                            cursor.execute(f"update segundo_bach_tres set lengua = '{float(lenguaBach21.get())}' "
                                           f"where  id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesBach21.get():
                            cursor.execute(f"update segundo_bach_tres set matematicas = '{float(matesBach21.get())}' "
                                           f"where id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaBach21.get():
                            cursor.execute(f"update segundo_bach_tres set historia = '{float(historiaBach21.get())}' "
                                           f"where  id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if quimicaBach21.get():
                            cursor.execute(f"update segundo_bach_tres set quimica = '{float(quimicaBach21.get())}' "
                                           f"where id = '{int(nombreBach21.get())}'")
                            connexion.commit()
                        else:
                            pass

                        if geologiaBach21.get():
                            cursor.execute(f"update segundo_bach_tres set geologia = '{float(geologiaBach21.get())}' "
                                           f"where id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if economiaBach21.get():
                            cursor.execute(f"update segundo_bach_tres set economia = '{float(economiaBach21.get())}' "
                                           f"where id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesBach21.get():
                            cursor.execute(f"update segundo_bach_tres set frances = '{float(francesBach21.get())}' "
                                           f"where  id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesBach21.get():
                            cursor.execute(f"update segundo_bach_tres set ingles = '{float(inglesBach21.get())}' "
                                           f"where  id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionBach21.get():
                            cursor.execute(f"update segundo_bach_tres set religion = '{float(religionBach21.get())}' "
                                           f"where  id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if electrotecniaBach21.get():
                            cursor.execute(f"update segundo_bach_tres set electrotecnia = '{float(electrotecniaBach21.get())}' "
                                           f"where  id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaBach21.get():
                            cursor.execute(f"update segundo_bach_tres set ef = '{float(efisicaBach21.get())}' "
                                           f"where  id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaBach21.get():
                            cursor.execute(f"update segundo_bach_tres set informatica = '{float(informaticaBach21.get())}' "
                                           f"where  id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if filosofiaBach21.get():
                            cursor.execute(f"update segundo_bach_tres set filosofia = '{float(filosofiaBach21.get())}' "
                                           f"where  id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass


                        if cnsBach21.get():
                            cursor.execute(f"update segundo_bach_tres set cns = '{float(cnsBach21.get())}' "
                                           f"where  id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass


                    elif trimestre51.get() == 4:
                        if lenguaBach21.get():
                            cursor.execute(f"update segundo_bach_septiembre set lengua = '{float(lenguaBach21.get())}' "
                                           f"where  id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesBach21.get():
                            cursor.execute(f"update segundo_bach_septiembre set matematicas = '{float(matesBach21.get())}' "
                                           f"where  id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaBach21.get():
                            cursor.execute(f"update segundo_bach_septiembre set historia = '{float(historiaBach21.get())}' "
                                           f"where  id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if quimicaBach21.get():
                            cursor.execute(f"update segundo_bach_septiembre set quimica = '{float(quimicaBach21.get())}' "
                                           f"where  id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if geologiaBach21.get():
                            cursor.execute(f"update segundo_bach_septiembre set geologia = '{float(geologiaBach21.get())}' "
                                           f"where id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if economiaBach21.get():
                            cursor.execute(f"update segundo_bach_septiembre set economia = '{float(economiaBach21.get())}' "
                                           f"where  id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesBach21.get():
                            cursor.execute(f"update segundo_bach_septiembre set frances = '{float(francesBach21.get())}' "
                                           f"where  id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesBach21.get():
                            cursor.execute(f"update segundo_bach_septiembre set ingles = '{float(inglesBach21.get())}' "
                                           f"where  id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionBach21.get():
                            cursor.execute(f"update segundo_bach_septiembre set religion = '{float(religionBach21.get())}' "
                                           f"where  id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if electrotecniaBach21.get():
                            cursor.execute(f"update segundo_bach_septiembre set electrotecnia = '{float(electrotecniaBach21.get())}' "
                                           f"where id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaBach21.get():
                            cursor.execute(f"update segundo_bach_septiembre set ef = '{float(efisicaBach21.get())}' "
                                           f"where  id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaBach21.get():
                            cursor.execute(f"update segundo_bach_septiembre set informatica = '{float(informaticaBach21.get())}' "
                                           f"where  id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if filosofiaBach21.get():
                            cursor.execute(f"update segundo_bach_septiembre set filosofia = '{float(filosofiaBach21.get())}' "
                                           f"where  id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass


                        if cnsBach21.get():
                            cursor.execute(f"update segundo_bach_septiembre set cns = '{float(cnsBach21.get())}' "
                                           f"where  id = '{int(nombreBach21.get())}' ")
                            connexion.commit()
                        else:
                            pass

                    # --------actualizar la tabla de junio----------------------------
                    cursor.execute(f"select lengua, matematicas, historia, quimica, geologia, economia, frances, ingles, religion,"
                                   f"electrotecnia, ef, informatica, filosofia, cns from segundo_bach_uno where id = '{int(nombreBach21.get())}' ")
                    stock = cursor.fetchall()

                    cursor.execute(f"select lengua, matematicas, historia, quimica, geologia, economia, frances, ingles, religion,"
                                   f"electrotecnia, ef, informatica, filosofia, cns from segundo_bach_dos where id = '{int(nombreBach21.get())}' ")
                    stock1 = cursor.fetchall()

                    cursor.execute(f"select lengua, matematicas, historia, quimica, geologia, economia, frances, ingles, religion,"
                                   f"electrotecnia, ef, informatica, filosofia, cns from segundo_bach_tres where id = '{int(nombreBach21.get())}' ")
                    stock2 = cursor.fetchall()

                    lengua = (stock[0][0] + stock1[0][0] + stock2[0][0]) / 3
                    matematicas = (stock[0][1] + stock1[0][1] + stock2[0][1]) / 3
                    historia = (stock[0][2] + stock1[0][1] + stock2[0][1]) / 3
                    quimica = (stock[0][3] + stock1[0][3] + stock2[0][3]) / 3
                    geologia = (stock[0][4] + stock1[0][4] + stock2[0][4]) / 3
                    economia = (stock[0][5] + stock1[0][5] + stock2[0][5]) / 3
                    frances = (stock[0][6] + stock1[0][6] + stock2[0][6]) / 3
                    ingles = (stock[0][7] + stock1[0][7] + stock2[0][7]) / 3
                    religion = (stock[0][8] + stock1[0][8] + stock2[0][8]) / 3
                    electrotecnia = (stock[0][9] + stock1[0][9] + stock2[0][9]) / 3
                    ef = (stock[0][10] + stock1[0][10] + stock2[0][10]) / 3
                    informatica = (stock[0][11] + stock1[0][11] + stock2[0][11]) / 3
                    filosofia = (stock[0][12] + stock1[0][12] + stock2[0][12]) / 3
                    cns = (stock[0][13] + stock1[0][13] + stock2[0][13]) / 3


                    cursor.execute(f"update segundo_bach_junio set lengua = '{lengua}' "
                                   f"where  id = '{int(nombreBach21.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set matematicas = '{matematicas}' "
                                   f"where  id = '{int(nombreBach21.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set historia = '{historia}' "
                                   f"where  id = '{int(nombreBach21.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set quimica = '{quimica}' "
                                   f"where id = '{int(nombreBach21.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set geologia = '{geologia}' "
                                   f"where  id = '{int(nombreBach21.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set economia = '{economia}' "
                                   f"where id = '{int(nombreBach21.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set frances = '{frances}' "
                                   f"where  id = '{int(nombreBach21.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set ingles = '{ingles}' "
                                   f"where id = '{int(nombreBach21.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set religion = '{religion}' "
                                   f"where  id = '{int(nombreBach21.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set electrotecnia = '{electrotecnia}' "
                                   f"where  id = '{int(nombreBach21.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set ef = '{ef}' "
                                   f"where  id = '{int(nombreBach21.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set informatica = '{informatica}' "
                                   f"where  id = '{int(nombreBach21.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set filosofia = '{filosofia}' "
                                   f"where id = '{int(nombreBach21.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set cns = '{cns}' "
                                   f"where id = '{int(nombreBach21.get())}' ")
                    connexion.commit()

                    lenguaBach21.set("")
                    matesBach21.set("")
                    historiaBach21.set("")
                    quimicaBach21.set("")
                    geologiaBach21.set("")
                    economiaBach21.set("")
                    francesBach21.set("")
                    inglesBach21.set("")
                    religionBach21.set("")
                    electrotecniaBach21.set("")
                    efisicaBach21.set("")
                    informaticaBach21.set("")
                    filosofiaBach21.set("")
                    cnsBach21.set("")

                else:
                    pass

                connexion.close()

            except ValueError:
                pass

        except IndexError:
            pass


    def segundoBachTecnologia():
        try:

            try:


                connexion = sqlite3.connect(nameBD.nomBD())
                cursor = connexion.cursor()
                if nombreId52.get() == 1:
                    if trimestre52.get() == 1:
                        if lenguaBach22.get():
                            cursor.execute(f"update segundo_bach_uno set lengua = '{float(lenguaBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesBach22.get():
                            cursor.execute(f"update segundo_bach_uno set matematicas = '{float(matesBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaBach22.get():
                            cursor.execute(f"update segundo_bach_uno set historia = '{float(historiaBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if tecnologiaBach22.get():
                            cursor.execute(f"update segundo_bach_uno set tecnologia = '{float(tecnologiaBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if electrotecniaBach22.get():
                            cursor.execute(f"update segundo_bach_uno set electrotecnia = '{float(electrotecniaBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if economiaBach22.get():
                            cursor.execute(f"update segundo_bach_uno set economia = '{float(economiaBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesBach22.get():
                            cursor.execute(f"update segundo_bach_uno set frances = '{float(francesBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesBach22.get():
                            cursor.execute(f"update segundo_bach_uno set ingles = '{float(inglesBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionBach22.get():
                            cursor.execute(f"update segundo_bach_uno set religion = '{float(religionBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if dibujoBach22.get():
                            cursor.execute(f"update segundo_bach_uno set dibujo_tecnico = '{float(dibujoBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaBach22.get():
                            cursor.execute(f"update segundo_bach_uno set ef = '{float(efisicaBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaBach22.get():
                            cursor.execute(f"update segundo_bach_uno set informatica = '{float(informaticaBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if filosofiaBach22.get():
                            cursor.execute(f"update segundo_bach_uno set filosofia = '{float(filosofiaBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass


                        if cnsBach22.get():
                            cursor.execute(f"update segundo_bach_uno set cns = '{float(cnsBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass



                    elif trimestre52.get() == 2:
                        if lenguaBach22.get():
                            cursor.execute(f"update segundo_bach_dos set lengua = '{float(lenguaBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesBach22.get():
                            cursor.execute(f"update segundo_bach_dos set matematicas = '{float(matesBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaBach22.get():
                            cursor.execute(f"update segundo_bach_dos set historia = '{float(historiaBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if tecnologiaBach22.get():
                            cursor.execute(f"update segundo_bach_dos set tecnologia = '{float(tecnologiaBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if electrotecniaBach22.get():
                            cursor.execute(f"update segundo_bach_dos set electrotecnia = '{float(electrotecniaBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if economiaBach22.get():
                            cursor.execute(f"update segundo_bach_dos set economia = '{float(economiaBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesBach22.get():
                            cursor.execute(f"update segundo_bach_dos set frances = '{float(francesBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesBach22.get():
                            cursor.execute(f"update segundo_bach_dos set ingles = '{float(inglesBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionBach22.get():
                            cursor.execute(f"update segundo_bach_dos set religion = '{float(religionBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if dibujoBach22.get():
                            cursor.execute(f"update segundo_bach_dos set dibujo_tecnico = '{float(dibujoBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaBach22.get():
                            cursor.execute(f"update segundo_bach_dos set ef = '{float(efisicaBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaBach22.get():
                            cursor.execute(f"update segundo_bach_dos set informatica = '{float(informaticaBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if filosofiaBach22.get():
                            cursor.execute(f"update segundo_bach_dos set filosofia = '{float(filosofiaBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass


                        if cnsBach22.get():
                            cursor.execute(f"update segundo_bach_dos set cns = '{float(cnsBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass


                    elif trimestre52.get() == 3:
                        if lenguaBach22.get():
                            cursor.execute(f"update segundo_bach_tres set lengua = '{float(lenguaBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesBach22.get():
                            cursor.execute(f"update segundo_bach_tres set matematicas = '{float(matesBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaBach22.get():
                            cursor.execute(f"update segundo_bach_tres set historia = '{float(historiaBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if tecnologiaBach22.get():
                            cursor.execute(f"update segundo_bach_tres set tecnologia = '{float(tecnologiaBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if electrotecniaBach22.get():
                            cursor.execute(f"update segundo_bach_tres set electrotecnia = '{float(electrotecniaBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if economiaBach22.get():
                            cursor.execute(f"update segundo_bach_tres set economia = '{float(economiaBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesBach22.get():
                            cursor.execute(f"update segundo_bach_tres set frances = '{float(francesBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesBach22.get():
                            cursor.execute(f"update segundo_bach_tres set ingles = '{float(inglesBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionBach22.get():
                            cursor.execute(f"update segundo_bach_tres set religion = '{float(religionBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if dibujoBach22.get():
                            cursor.execute(f"update segundo_bach_tres set dibujo_tecnico = '{float(dibujoBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaBach22.get():
                            cursor.execute(f"update segundo_bach_tres set ef = '{float(efisicaBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaBach22.get():
                            cursor.execute(f"update segundo_bach_tres set informatica = '{float(informaticaBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if filosofiaBach22.get():
                            cursor.execute(f"update segundo_bach_tres set filosofia = '{float(filosofiaBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass


                        if cnsBach22.get():
                            cursor.execute(f"update segundo_bach_tres set cns = '{float(cnsBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass


                    elif trimestre52.get() == 4:
                        if lenguaBach22.get():
                            cursor.execute(f"update segundo_bach_septiembre set lengua = '{float(lenguaBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesBach22.get():
                            cursor.execute(f"update segundo_bach_septiembre set matematicas = '{float(matesBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaBach22.get():
                            cursor.execute(f"update segundo_bach_septiembre set historia = '{float(historiaBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if tecnologiaBach22.get():
                            cursor.execute(f"update segundo_bach_septiembre set tecnologia = '{float(tecnologiaBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if electrotecniaBach22.get():
                            cursor.execute(f"update segundo_bach_septiembre set electrotecnia = '{float(electrotecniaBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if economiaBach22.get():
                            cursor.execute(f"update segundo_bach_septiembre set economia = '{float(economiaBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesBach22.get():
                            cursor.execute(f"update segundo_bach_septiembre set frances = '{float(francesBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesBach22.get():
                            cursor.execute(f"update segundo_bach_septiembre set ingles = '{float(inglesBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionBach22.get():
                            cursor.execute(f"update segundo_bach_septiembre set religion = '{float(religionBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if dibujoBach22.get():
                            cursor.execute(f"update segundo_bach_septiembre set dibujo_tecnico = '{float(dibujoBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaBach22.get():
                            cursor.execute(f"update segundo_bach_septiembre set ef = '{float(efisicaBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaBach22.get():
                            cursor.execute(f"update segundo_bach_septiembre set informatica = '{float(informaticaBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if filosofiaBach22.get():
                            cursor.execute(f"update segundo_bach_septiembre set filosofia = '{float(filosofiaBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass


                        if cnsBach22.get():
                            cursor.execute(f"update segundo_bach_septiembre set cns = '{float(cnsBach22.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                    # --------actualizar la tabla de junio----------------------------
                    cursor.execute(
                                f"select lengua, matematicas, historia, tecnologia, electrotecnia, economia, frances, ingles, religion,"
                                f"dibujo_tecnico, ef, informatica, filosofia, cns from segundo_bach_uno where nombre = '{nombreBach22.get().upper()}' ")
                    stock = cursor.fetchall()

                    cursor.execute(
                                f"select lengua, matematicas, historia, tecnologia, electrotecnia, economia, frances, ingles, religion,"
                                f"dibujo_tecnico, ef, informatica, filosofia, cns from segundo_bach_dos where nombre = '{nombreBach22.get().upper()}' ")
                    stock1 = cursor.fetchall()

                    cursor.execute(
                                f"select lengua, matematicas, historia, tecnologia, electrotecnia, economia, frances, ingles, religion,"
                                f"dibujo_tecnico, ef, informatica, filosofia, cns from segundo_bach_tres where nombre = '{nombreBach22.get().upper()}' ")
                    stock2 = cursor.fetchall()

                    lengua = (stock[0][0] + stock1[0][0] + stock2[0][0]) / 3
                    matematicas = (stock[0][1] + stock1[0][1] + stock2[0][1]) / 3
                    historia = (stock[0][2] + stock1[0][1] + stock2[0][1]) / 3
                    tecnologia = (stock[0][3] + stock1[0][3] + stock2[0][3]) / 3
                    electrotecnia = (stock[0][4] + stock1[0][4] + stock2[0][4]) / 3
                    economia = (stock[0][5] + stock1[0][5] + stock2[0][5]) / 3
                    frances = (stock[0][6] + stock1[0][6] + stock2[0][6]) / 3
                    ingles = (stock[0][7] + stock1[0][7] + stock2[0][7]) / 3
                    religion = (stock[0][8] + stock1[0][8] + stock2[0][8]) / 3
                    dibujo = (stock[0][9] + stock1[0][9] + stock2[0][9]) / 3
                    ef = (stock[0][10] + stock1[0][10] + stock2[0][10]) / 3
                    informatica = (stock[0][11] + stock1[0][11] + stock2[0][11]) / 3
                    filosofia = (stock[0][12] + stock1[0][12] + stock2[0][12]) / 3
                    cns = (stock[0][13] + stock1[0][13] + stock2[0][13]) / 3

                    cursor.execute(f"update segundo_bach_junio set lengua = '{lengua}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set matematicas = '{matematicas}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set historia = '{historia}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set tecnologia = '{tecnologia}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set electrotecnia = '{electrotecnia}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set economia = '{economia}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set frances = '{frances}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set ingles = '{ingles}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set religion = '{religion}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set dibujo_tecnico = '{dibujo}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set ef = '{ef}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set informatica = '{informatica}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set filosofia = '{filosofia}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set cns = '{cns}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                    connexion.commit()

                    lenguaBach22.set("")
                    matesBach22.set("")
                    historiaBach22.set("")
                    tecnologiaBach22.set("")
                    electrotecniaBach22.set("")
                    economiaBach22.set("")
                    francesBach22.set("")
                    inglesBach22.set("")
                    religionBach22.set("")
                    dibujoBach22.set("")
                    efisicaBach22.set("")
                    informaticaBach22.set("")
                    filosofiaBach22.set("")
                    cnsBach22.set("")






                elif nombreId52.get() == 2:

                    if trimestre52.get() == 1:
                        if lenguaBach22.get():
                            cursor.execute(f"update segundo_bach_uno set lengua = '{float(lenguaBach22.get())}' "
                                           f"where  id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesBach22.get():
                            cursor.execute(f"update segundo_bach_uno set matematicas = '{float(matesBach22.get())}' "
                                           f"where  id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaBach22.get():
                            cursor.execute(f"update segundo_bach_uno set historia = '{float(historiaBach22.get())}' "
                                           f"where  id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if tecnologiaBach22.get():
                            cursor.execute(f"update segundo_bach_uno set tecnologia = '{float(tecnologiaBach22.get())}' "
                                           f"where  id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if electrotecniaBach22.get():
                            cursor.execute(f"update segundo_bach_uno set electrotecnia = '{float(electrotecniaBach22.get())}' "
                                           f"where  id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if economiaBach22.get():
                            cursor.execute(f"update segundo_bach_uno set economia = '{float(economiaBach22.get())}' "
                                           f"where  id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesBach22.get():
                            cursor.execute(f"update segundo_bach_uno set frances = '{float(francesBach22.get())}' "
                                           f"where  id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesBach22.get():
                            cursor.execute(f"update segundo_bach_uno set ingles = '{float(inglesBach22.get())}' "
                                           f"where  id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionBach22.get():
                            cursor.execute(f"update segundo_bach_uno set religion = '{float(religionBach22.get())}' "
                                           f"where id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if dibujoBach22.get():
                            cursor.execute(f"update segundo_bach_uno set dibujo_tecnico = '{float(dibujoBach22.get())}' "
                                           f"where  id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaBach22.get():
                            cursor.execute(f"update segundo_bach_uno set ef = '{float(efisicaBach22.get())}' "
                                           f"where  id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaBach22.get():
                            cursor.execute(f"update segundo_bach_uno set informatica = '{float(informaticaBach22.get())}' "
                                           f"where  id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if filosofiaBach22.get():
                            cursor.execute(f"update segundo_bach_uno set filosofia = '{float(filosofiaBach22.get())}' "
                                           f"where  id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass


                        if cnsBach22.get():
                            cursor.execute(f"update segundo_bach_uno set cns = '{float(cnsBach22.get())}' "
                                           f"where  id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass



                    elif trimestre52.get() == 2:
                        if lenguaBach22.get():
                            cursor.execute(f"update segundo_bach_dos set lengua = '{float(lenguaBach22.get())}' "
                                           f"where id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesBach22.get():
                            cursor.execute(f"update segundo_bach_dos set matematicas = '{float(matesBach22.get())}' "
                                           f"where  id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaBach22.get():
                            cursor.execute(f"update segundo_bach_dos set historia = '{float(historiaBach22.get())}' "
                                           f"where  id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if tecnologiaBach22.get():
                            cursor.execute(f"update segundo_bach_dos set tecnologia = '{float(tecnologiaBach22.get())}' "
                                           f"where id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if electrotecniaBach22.get():
                            cursor.execute(f"update segundo_bach_dos set electrotecnia = '{float(electrotecniaBach22.get())}' "
                                           f"where id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if economiaBach22.get():
                            cursor.execute(f"update segundo_bach_dos set economia = '{float(economiaBach22.get())}' "
                                           f"where id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesBach22.get():
                            cursor.execute(f"update segundo_bach_dos set frances = '{float(francesBach22.get())}' "
                                           f"where  id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesBach22.get():
                            cursor.execute(f"update segundo_bach_dos set ingles = '{float(inglesBach22.get())}' "
                                           f"where  id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionBach22.get():
                            cursor.execute(f"update segundo_bach_dos set religion = '{float(religionBach22.get())}' "
                                           f"where  id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if dibujoBach22.get():
                            cursor.execute(f"update segundo_bach_dos set dibujo_tecnico = '{float(dibujoBach22.get())}' "
                                           f"where  id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaBach22.get():
                            cursor.execute(f"update segundo_bach_dos set ef = '{float(efisicaBach22.get())}' "
                                           f"where  id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaBach22.get():
                            cursor.execute(f"update segundo_bach_dos set informatica = '{float(informaticaBach22.get())}' "
                                           f"where id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if filosofiaBach22.get():
                            cursor.execute(f"update segundo_bach_dos set filosofia = '{float(filosofiaBach22.get())}' "
                                           f"where  id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass


                        if cnsBach22.get():
                            cursor.execute(f"update segundo_bach_dos set cns = '{float(cnsBach22.get())}' "
                                           f"where  id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass


                    elif trimestre52.get() == 3:
                        if lenguaBach22.get():
                            cursor.execute(f"update segundo_bach_tres set lengua = '{float(lenguaBach22.get())}' "
                                           f"where  id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesBach22.get():
                            cursor.execute(f"update segundo_bach_tres set matematicas = '{float(matesBach22.get())}' "
                                           f"where  id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaBach22.get():
                            cursor.execute(f"update segundo_bach_tres set historia = '{float(historiaBach22.get())}' "
                                           f"where id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if tecnologiaBach22.get():
                            cursor.execute(f"update segundo_bach_tres set tecnologia = '{float(tecnologiaBach22.get())}' "
                                           f"where  id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if electrotecniaBach22.get():
                            cursor.execute(f"update segundo_bach_tres set electrotecnia = '{float(electrotecniaBach22.get())}' "
                                           f"where  id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if economiaBach22.get():
                            cursor.execute(f"update segundo_bach_tres set economia = '{float(economiaBach22.get())}' "
                                           f"where  id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesBach22.get():
                            cursor.execute(f"update segundo_bach_tres set frances = '{float(francesBach22.get())}' "
                                           f"where  id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesBach22.get():
                            cursor.execute(f"update segundo_bach_tres set ingles = '{float(inglesBach22.get())}' "
                                           f"where  id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionBach22.get():
                            cursor.execute(f"update segundo_bach_tres set religion = '{float(religionBach22.get())}' "
                                           f"where  id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if dibujoBach22.get():
                            cursor.execute(f"update segundo_bach_tres set dibujo_tecnico = '{float(dibujoBach22.get())}' "
                                           f"where  id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaBach22.get():
                            cursor.execute(f"update segundo_bach_tres set ef = '{float(efisicaBach22.get())}' "
                                           f"where id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaBach22.get():
                            cursor.execute(f"update segundo_bach_tres set informatica = '{float(informaticaBach22.get())}' "
                                           f"where  id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if filosofiaBach22.get():
                            cursor.execute(f"update segundo_bach_tres set filosofia = '{float(filosofiaBach22.get())}' "
                                           f"where  id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass


                        if cnsBach22.get():
                            cursor.execute(f"update segundo_bach_tres set cns = '{float(cnsBach22.get())}' "
                                           f"where  id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass


                    elif trimestre52.get() == 4:
                        if lenguaBach22.get():
                            cursor.execute(f"update segundo_bach_septiembre set lengua = '{float(lenguaBach22.get())}' "
                                           f"where  id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesBach22.get():
                            cursor.execute(f"update segundo_bach_septiembre set matematicas = '{float(matesBach22.get())}' "
                                           f"where  id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaBach22.get():
                            cursor.execute(f"update segundo_bach_septiembre set historia = '{float(historiaBach22.get())}' "
                                           f"where  id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if tecnologiaBach22.get():
                            cursor.execute(f"update segundo_bach_septiembre set tecnologia = '{float(tecnologiaBach22.get())}' "
                                           f"where  id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if electrotecniaBach22.get():
                            cursor.execute(f"update segundo_bach_septiembre set electrotecnia = '{float(electrotecniaBach22.get())}' "
                                           f"where id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if economiaBach22.get():
                            cursor.execute(f"update segundo_bach_septiembre set economia = '{float(economiaBach22.get())}' "
                                           f"where  id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesBach22.get():
                            cursor.execute(f"update segundo_bach_septiembre set frances = '{float(francesBach22.get())}' "
                                           f"where  id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesBach22.get():
                            cursor.execute(f"update segundo_bach_septiembre set ingles = '{float(inglesBach22.get())}' "
                                           f"where  id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionBach22.get():
                            cursor.execute(f"update segundo_bach_septiembre set religion = '{float(religionBach22.get())}' "
                                           f"where  id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if dibujoBach22.get():
                            cursor.execute(f"update segundo_bach_septiembre set dibujo_tecnico = '{float(dibujoBach22.get())}' "
                                           f"where id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaBach22.get():
                            cursor.execute(f"update segundo_bach_septiembre set ef = '{float(efisicaBach22.get())}' "
                                           f"where  id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaBach22.get():
                            cursor.execute(f"update segundo_bach_septiembre set informatica = '{float(informaticaBach22.get())}' "
                                           f"where  id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if filosofiaBach22.get():
                            cursor.execute(f"update segundo_bach_septiembre set filosofia = '{float(filosofiaBach22.get())}' "
                                           f"where  id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass


                        if cnsBach22.get():
                            cursor.execute(f"update segundo_bach_septiembre set cns = '{float(cnsBach22.get())}' "
                                           f"where  id = '{int(nombreBach22.get())}' ")
                            connexion.commit()
                        else:
                            pass


                    # --------actualizar la tabla de junio----------------------------
                    cursor.execute(f"select lengua, matematicas, historia, tecnologia, electrotecnia, economia, frances, ingles, religion,"
                                   f"dibujo_tecnico, ef, informatica, filosofia, cns from segundo_bach_uno where id = '{int(nombreBach22.get())}' ")
                    stock = cursor.fetchall()

                    cursor.execute(f"select lengua, matematicas, historia, tecnologia, electrotecnia, economia, frances, ingles, religion,"
                                   f"dibujo_tecnico, ef, informatica, filosofia, cns from segundo_bach_dos where id = '{int(nombreBach22.get())}' ")
                    stock1 = cursor.fetchall()

                    cursor.execute(f"select lengua, matematicas, historia, tecnologia, electrotecnia, economia, frances, ingles, religion,"
                                   f"dibujo_tecnico, ef, informatica, filosofia, cns from segundo_bach_tres where id = '{int(nombreBach22.get())}' ")
                    stock2 = cursor.fetchall()

                    lengua = (stock[0][0] + stock1[0][0] + stock2[0][0]) / 3
                    matematicas = (stock[0][1] + stock1[0][1] + stock2[0][1]) / 3
                    historia = (stock[0][2] + stock1[0][1] + stock2[0][1]) / 3
                    tecnologia = (stock[0][3] + stock1[0][3] + stock2[0][3]) / 3
                    electrotecnia = (stock[0][4] + stock1[0][4] + stock2[0][4]) / 3
                    economia = (stock[0][5] + stock1[0][5] + stock2[0][5]) / 3
                    frances = (stock[0][6] + stock1[0][6] + stock2[0][6]) / 3
                    ingles = (stock[0][7] + stock1[0][7] + stock2[0][7]) / 3
                    religion = (stock[0][8] + stock1[0][8] + stock2[0][8]) / 3
                    dibujo = (stock[0][9] + stock1[0][9] + stock2[0][9]) / 3
                    ef = (stock[0][10] + stock1[0][10] + stock2[0][10]) / 3
                    informatica = (stock[0][11] + stock1[0][11] + stock2[0][11]) / 3
                    filosofia = (stock[0][12] + stock1[0][12] + stock2[0][12]) / 3
                    cns = (stock[0][13] + stock1[0][13] + stock2[0][13]) / 3


                    cursor.execute(f"update segundo_bach_junio set lengua = '{lengua}' "
                                   f"where  id = '{int(nombreBach22.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set matematicas = '{matematicas}' "
                                   f"where  id = '{int(nombreBach22.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set historia = '{historia}' "
                                   f"where  id = '{int(nombreBach22.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set tecnologia = '{tecnologia}' "
                                   f"where  id = '{int(nombreBach22.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set electrotecnia = '{electrotecnia}' "
                                   f"where  id = '{int(nombreBach22.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set economia = '{economia}' "
                                   f"where  id = '{int(nombreBach22.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set frances = '{frances}' "
                                   f"where  id = '{int(nombreBach22.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set ingles = '{ingles}' "
                                   f"where id = '{int(nombreBach22.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set religion = '{religion}' "
                                   f"where  id = '{int(nombreBach22.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set dibujo_tecnico = '{dibujo}' "
                                   f"where id = '{int(nombreBach22.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set ef = '{ef}' "
                                   f"where  id = '{int(nombreBach22.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set informatica = '{informatica}' "
                                   f"where  id = '{int(nombreBach22.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set filosofia = '{filosofia}' "
                                   f"where id = '{int(nombreBach22.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set cns = '{cns}' "
                                   f"where id = '{int(nombreBach22.get())}' ")
                    connexion.commit()

                    lenguaBach22.set("")
                    matesBach22.set("")
                    historiaBach22.set("")
                    tecnologiaBach22.set("")
                    electrotecniaBach22.set("")
                    economiaBach22.set("")
                    francesBach22.set("")
                    inglesBach22.set("")
                    religionBach22.set("")
                    dibujoBach22.set("")
                    efisicaBach22.set("")
                    informaticaBach22.set("")
                    filosofiaBach22.set("")
                    cnsBach22.set("")

                else:
                    pass

                connexion.close()

            except ValueError:
                pass

        except IndexError:
            pass


    def segundoBachletras():
        try:

            try:


                connexion = sqlite3.connect(nameBD.nomBD())
                cursor = connexion.cursor()
                if nombreId53.get() == 1:
                    if trimestre53.get() == 1:
                        if lenguaBach23.get():
                            cursor.execute(f"update segundo_bach_uno set lengua = '{float(lenguaBach23.get())}' "
                                           f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesBach23.get():
                            cursor.execute(f"update segundo_bach_uno set mates_aplicadas = '{float(matesBach23.get())}' "
                                           f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaBach23.get():
                            cursor.execute(f"update segundo_bach_uno set historia = '{float(historiaBach23.get())}' "
                                           f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaarteBach23.get():
                            cursor.execute(f"update segundo_bach_uno set historia_arte = '{float(historiaarteBach23.get())}' "
                                           f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass


                        if latinBach23.get():
                            cursor.execute(f"update segundo_bach_uno set latin = '{float(latinBach23.get())}' "
                                           f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass


                        if economiaBach23.get():
                            cursor.execute(f"update segundo_bach_uno set economia = '{float(economiaBach23.get())}' "
                                           f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesBach23.get():
                            cursor.execute(f"update segundo_bach_uno set frances = '{float(francesBach23.get())}' "
                                           f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesBach23.get():
                            cursor.execute(f"update segundo_bach_uno set ingles = '{float(inglesBach23.get())}' "
                                           f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionBach23.get():
                            cursor.execute(f"update segundo_bach_uno set religion = '{float(religionBach23.get())}' "
                                           f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if griegoBach23.get():
                            cursor.execute(f"update segundo_bach_uno set griego = '{float(griegoBach23.get())}' "
                                           f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaBach23.get():
                            cursor.execute(f"update segundo_bach_uno set ef = '{float(efisicaBach23.get())}' "
                                           f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaBach23.get():
                            cursor.execute(f"update segundo_bach_uno set informatica = '{float(informaticaBach23.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if filosofiaBach23.get():
                            cursor.execute(f"update segundo_bach_uno set filosofia = '{float(filosofiaBach23.get())}' "
                                           f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass


                        if cnsBach23.get():
                            cursor.execute(f"update segundo_bach_uno set cns = '{float(cnsBach23.get())}' "
                                           f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass



                    elif trimestre53.get() == 2:
                        if lenguaBach23.get():
                            cursor.execute(f"update segundo_bach_dos set lengua = '{float(lenguaBach23.get())}' "
                                           f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesBach23.get():
                            cursor.execute(f"update segundo_bach_dos set mates_aplicadas = '{float(matesBach23.get())}' "
                                           f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaBach23.get():
                            cursor.execute(f"update segundo_bach_dos set historia = '{float(historiaBach23.get())}' "
                                           f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaarteBach23.get():
                            cursor.execute(
                                f"update segundo_bach_dos set historia_arte = '{float(historiaarteBach23.get())}' "
                                f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if latinBach23.get():
                            cursor.execute(f"update segundo_bach_dos set latin = '{float(latinBach23.get())}' "
                                           f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if economiaBach23.get():
                            cursor.execute(f"update segundo_bach_dos set economia = '{float(economiaBach23.get())}' "
                                           f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesBach23.get():
                            cursor.execute(f"update segundo_bach_dos set frances = '{float(francesBach23.get())}' "
                                           f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesBach23.get():
                            cursor.execute(f"update segundo_bach_dos set ingles = '{float(inglesBach23.get())}' "
                                           f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionBach23.get():
                            cursor.execute(f"update segundo_bach_dos set religion = '{float(religionBach23.get())}' "
                                           f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if griegoBach23.get():
                            cursor.execute(f"update segundo_bach_dos set griego = '{float(griegoBach23.get())}' "
                                           f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaBach23.get():
                            cursor.execute(f"update segundo_bach_dos set ef = '{float(efisicaBach23.get())}' "
                                           f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaBach23.get():
                            cursor.execute(f"update segundo_bach_dos set informatica = '{float(informaticaBach23.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if filosofiaBach23.get():
                            cursor.execute(f"update segundo_bach_dos set filosofia = '{float(filosofiaBach23.get())}' "
                                           f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if cnsBach23.get():
                            cursor.execute(f"update segundo_bach_dos set cns = '{float(cnsBach23.get())}' "
                                           f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass


                    elif trimestre53.get() == 3:
                        if lenguaBach23.get():
                            cursor.execute(f"update segundo_bach_tres set lengua = '{float(lenguaBach23.get())}' "
                                           f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesBach23.get():
                            cursor.execute(f"update segundo_bach_tres set mates_aplicadas = '{float(matesBach23.get())}' "
                                           f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaBach23.get():
                            cursor.execute(f"update segundo_bach_tres set historia = '{float(historiaBach23.get())}' "
                                           f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaarteBach23.get():
                            cursor.execute(
                                f"update segundo_bach_tres set historia_arte = '{float(historiaarteBach23.get())}' "
                                f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if latinBach23.get():
                            cursor.execute(f"update segundo_bach_tres set latin = '{float(latinBach23.get())}' "
                                           f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if economiaBach23.get():
                            cursor.execute(f"update segundo_bach_tres set economia = '{float(economiaBach23.get())}' "
                                           f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesBach23.get():
                            cursor.execute(f"update segundo_bach_tres set frances = '{float(francesBach23.get())}' "
                                           f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesBach23.get():
                            cursor.execute(f"update segundo_bach_tres set ingles = '{float(inglesBach23.get())}' "
                                           f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionBach23.get():
                            cursor.execute(f"update segundo_bach_tres set religion = '{float(religionBach23.get())}' "
                                           f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if griegoBach23.get():
                            cursor.execute(f"update segundo_bach_tres set griego = '{float(griegoBach23.get())}' "
                                           f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaBach23.get():
                            cursor.execute(f"update segundo_bach_tres set ef = '{float(efisicaBach23.get())}' "
                                           f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaBach23.get():
                            cursor.execute(f"update segundo_bach_tres set informatica = '{float(informaticaBach23.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if filosofiaBach23.get():
                            cursor.execute(f"update segundo_bach_tres set filosofia = '{float(filosofiaBach23.get())}' "
                                           f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if cnsBach23.get():
                            cursor.execute(f"update segundo_bach_tres set cns = '{float(cnsBach23.get())}' "
                                           f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass


                    elif trimestre53.get() == 4:
                        if lenguaBach23.get():
                            cursor.execute(f"update segundo_bach_septiembre set lengua = '{float(lenguaBach23.get())}' "
                                           f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesBach23.get():
                            cursor.execute(f"update segundo_bach_septiembre set mates_aplicadas = '{float(matesBach23.get())}' "
                                           f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaBach23.get():
                            cursor.execute(f"update segundo_bach_septiembre set historia = '{float(historiaBach23.get())}' "
                                           f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaarteBach23.get():
                            cursor.execute(
                                f"update segundo_bach_septiembre set historia_arte = '{float(historiaarteBach23.get())}' "
                                f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if latinBach23.get():
                            cursor.execute(f"update segundo_bach_septiembre set latin = '{float(latinBach23.get())}' "
                                           f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if economiaBach23.get():
                            cursor.execute(f"update segundo_bach_septiembre set economia = '{float(economiaBach23.get())}' "
                                           f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesBach23.get():
                            cursor.execute(f"update segundo_bach_septiembre set frances = '{float(francesBach23.get())}' "
                                           f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesBach23.get():
                            cursor.execute(f"update segundo_bach_septiembre set ingles = '{float(inglesBach23.get())}' "
                                           f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionBach23.get():
                            cursor.execute(f"update segundo_bach_septiembre set religion = '{float(religionBach23.get())}' "
                                           f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if griegoBach23.get():
                            cursor.execute(f"update segundo_bach_septiembre set griego = '{float(griegoBach23.get())}' "
                                           f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaBach23.get():
                            cursor.execute(f"update segundo_bach_septiembre set ef = '{float(efisicaBach23.get())}' "
                                           f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaBach23.get():
                            cursor.execute(f"update segundo_bach_septiembre set informatica = '{float(informaticaBach23.get())}' "
                                           f"where  nombre = '{nombreBach22.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if filosofiaBach23.get():
                            cursor.execute(f"update segundo_bach_septiembre set filosofia = '{float(filosofiaBach23.get())}' "
                                           f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                        if cnsBach23.get():
                            cursor.execute(f"update segundo_bach_septiembre set cns = '{float(cnsBach23.get())}' "
                                           f"where  nombre = '{nombreBach23.get().upper()}' ")
                            connexion.commit()
                        else:
                            pass

                    # --------actualizar la tabla de junio----------------------------
                    cursor.execute(f"select lengua, mates_aplicadas, historia, historia_arte, latin, economia, frances, ingles, religion,"
                                   f"griego, ef, informatica, filosofia, cns from segundo_bach_uno where nombre = '{nombreBach23.get().upper()}' ")
                    stock = cursor.fetchall()

                    cursor.execute(f"select lengua, mates_aplicadas, historia, historia_arte, latin, economia, frances, ingles, religion,"
                                   f"griego, ef, informatica, filosofia, cns from segundo_bach_uno where nombre = '{nombreBach23.get().upper()}' ")
                    stock1 = cursor.fetchall()

                    cursor.execute(f"select lengua, mates_aplicadas, historia, historia_arte, latin, economia, frances, ingles, religion,"
                                   f"griego, ef, informatica, filosofia, cns from segundo_bach_uno where nombre = '{nombreBach23.get().upper()}' ")
                    stock2 = cursor.fetchall()

                    lengua = (stock[0][0] + stock1[0][0] + stock2[0][0]) / 3
                    matematicas = (stock[0][1] + stock1[0][1] + stock2[0][1]) / 3
                    historia = (stock[0][2] + stock1[0][1] + stock2[0][1]) / 3
                    historia_arte = (stock[0][3] + stock1[0][3] + stock2[0][3]) / 3
                    latin = (stock[0][4] + stock1[0][4] + stock2[0][4]) / 3
                    economia = (stock[0][5] + stock1[0][5] + stock2[0][5]) / 3
                    frances = (stock[0][6] + stock1[0][6] + stock2[0][6]) / 3
                    ingles = (stock[0][7] + stock1[0][7] + stock2[0][7]) / 3
                    religion = (stock[0][8] + stock1[0][8] + stock2[0][8]) / 3
                    griego = (stock[0][9] + stock1[0][9] + stock2[0][9]) / 3
                    ef = (stock[0][10] + stock1[0][10] + stock2[0][10]) / 3
                    informatica = (stock[0][11] + stock1[0][11] + stock2[0][11]) / 3
                    filosofia = (stock[0][12] + stock1[0][12] + stock2[0][12]) / 3
                    cns = (stock[0][13] + stock1[0][13] + stock2[0][13]) / 3


                    cursor.execute(f"update segundo_bach_junio set lengua = '{lengua}' "
                                   f"where  nombre = '{nombreBach23.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set mates_aplicadas = '{matematicas}' "
                                   f"where  nombre = '{nombreBach23.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set historia = '{historia}' "
                                   f"where  nombre = '{nombreBach23.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set historia_arte = '{historia_arte}' "
                                   f"where  nombre = '{nombreBach23.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set latin = '{latin}' "
                                   f"where  nombre = '{nombreBach23.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set economia = '{economia}' "
                                   f"where  nombre = '{nombreBach23.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set frances = '{frances}' "
                                   f"where  nombre = '{nombreBach23.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set ingles = '{ingles}' "
                                   f"where  nombre = '{nombreBach23.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set religion = '{religion}' "
                                   f"where  nombre = '{nombreBach23.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set griego = '{griego}' "
                                   f"where  nombre = '{nombreBach23.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set ef = '{ef}' "
                                   f"where  nombre = '{nombreBach23.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set informatica = '{informatica}' "
                                   f"where  nombre = '{nombreBach23.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set filosofia = '{filosofia}' "
                                   f"where  nombre = '{nombreBach23.get().upper()}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set cns = '{cns}' "
                                   f"where  nombre = '{nombreBach23.get().upper()}' ")
                    connexion.commit()

                    lenguaBach23.set("")
                    matesBach23.set("")
                    historiaBach23.set("")
                    historiaarteBach23.set("")
                    latinBach23.set("")
                    economiaBach23.set("")
                    francesBach23.set("")
                    inglesBach23.set("")
                    religionBach23.set("")
                    griegoBach23.set("")
                    efisicaBach23.set("")
                    informaticaBach23.set("")
                    filosofiaBach23.set("")
                    cnsBach23.set("")




                elif nombreId53.get() == 2:

                    if trimestre53.get() == 1:
                        if lenguaBach23.get():
                            cursor.execute(f"update segundo_bach_uno set lengua = '{float(lenguaBach23.get())}' "
                                           f"where  id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesBach23.get():
                            cursor.execute(f"update segundo_bach_uno set mates_aplicadas = '{float(matesBach23.get())}' "
                                           f"where  id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaBach23.get():
                            cursor.execute(f"update segundo_bach_uno set historia = '{float(historiaBach23.get())}' "
                                           f"where  id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaarteBach23.get():
                            cursor.execute(
                                f"update segundo_bach_uno set historia_arte = '{float(historiaarteBach23.get())}' "
                                f"where  id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if latinBach23.get():
                            cursor.execute(f"update segundo_bach_uno set latin = '{float(latinBach23.get())}' "
                                           f"where id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if economiaBach23.get():
                            cursor.execute(f"update segundo_bach_uno set economia = '{float(economiaBach23.get())}' "
                                           f"where  id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesBach23.get():
                            cursor.execute(f"update segundo_bach_uno set frances = '{float(francesBach23.get())}' "
                                           f"where id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesBach23.get():
                            cursor.execute(f"update segundo_bach_uno set ingles = '{float(inglesBach23.get())}' "
                                           f"where  id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionBach23.get():
                            cursor.execute(f"update segundo_bach_uno set religion = '{float(religionBach23.get())}' "
                                           f"where  id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if griegoBach23.get():
                            cursor.execute(f"update segundo_bach_uno set griego = '{float(griegoBach23.get())}' "
                                           f"where  id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaBach23.get():
                            cursor.execute(f"update segundo_bach_uno set ef = '{float(efisicaBach23.get())}' "
                                           f"where  id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaBach23.get():
                            cursor.execute(f"update segundo_bach_uno set informatica = '{float(informaticaBach23.get())}' "
                                           f"where  id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if filosofiaBach23.get():
                            cursor.execute(f"update segundo_bach_uno set filosofia = '{float(filosofiaBach23.get())}' "
                                           f"where id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if cnsBach23.get():
                            cursor.execute(f"update segundo_bach_uno set cns = '{float(cnsBach23.get())}' "
                                           f"where  id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass



                    elif trimestre53.get() == 2:
                        if lenguaBach23.get():
                            cursor.execute(f"update segundo_bach_dos set lengua = '{float(lenguaBach23.get())}' "
                                           f"where  id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesBach23.get():
                            cursor.execute(f"update segundo_bach_dos set mates_aplicadas = '{float(matesBach23.get())}' "
                                           f"where  id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaBach23.get():
                            cursor.execute(f"update segundo_bach_dos set historia = '{float(historiaBach23.get())}' "
                                           f"where  id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaarteBach23.get():
                            cursor.execute(
                                f"update segundo_bach_dos set historia_arte = '{float(historiaarteBach23.get())}' "
                                f"where  id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if latinBach23.get():
                            cursor.execute(f"update segundo_bach_dos set latin = '{float(latinBach23.get())}' "
                                           f"where  id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if economiaBach23.get():
                            cursor.execute(f"update segundo_bach_dos set economia = '{float(economiaBach23.get())}' "
                                           f"where  id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesBach23.get():
                            cursor.execute(f"update segundo_bach_dos set frances = '{float(francesBach23.get())}' "
                                           f"where  id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesBach23.get():
                            cursor.execute(f"update segundo_bach_dos set ingles = '{float(inglesBach23.get())}' "
                                           f"where  id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionBach23.get():
                            cursor.execute(f"update segundo_bach_dos set religion = '{float(religionBach23.get())}' "
                                           f"where  id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if griegoBach23.get():
                            cursor.execute(f"update segundo_bach_dos set griego = '{float(griegoBach23.get())}' "
                                           f"where id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaBach23.get():
                            cursor.execute(f"update segundo_bach_dos set ef = '{float(efisicaBach23.get())}' "
                                           f"where  id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaBach23.get():
                            cursor.execute(f"update segundo_bach_dos set informatica = '{float(informaticaBach23.get())}' "
                                           f"where  id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if filosofiaBach23.get():
                            cursor.execute(f"update segundo_bach_dos set filosofia = '{float(filosofiaBach23.get())}' "
                                           f"where id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if cnsBach23.get():
                            cursor.execute(f"update segundo_bach_dos set cns = '{float(cnsBach23.get())}' "
                                           f"where  id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass


                    elif trimestre53.get() == 3:
                        if lenguaBach23.get():
                            cursor.execute(f"update segundo_bach_tres set lengua = '{float(lenguaBach23.get())}' "
                                           f"where id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesBach23.get():
                            cursor.execute(f"update segundo_bach_tres set mates_aplicadas = '{float(matesBach23.get())}' "
                                           f"where  id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaBach23.get():
                            cursor.execute(f"update segundo_bach_tres set historia = '{float(historiaBach23.get())}' "
                                           f"where id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaarteBach23.get():
                            cursor.execute(
                                f"update segundo_bach_tres set historia_arte = '{float(historiaarteBach23.get())}' "
                                f"where  id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if latinBach23.get():
                            cursor.execute(f"update segundo_bach_tres set latin = '{float(latinBach23.get())}' "
                                           f"where  id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if economiaBach23.get():
                            cursor.execute(f"update segundo_bach_tres set economia = '{float(economiaBach23.get())}' "
                                           f"where id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesBach23.get():
                            cursor.execute(f"update segundo_bach_tres set frances = '{float(francesBach23.get())}' "
                                           f"where  id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesBach23.get():
                            cursor.execute(f"update segundo_bach_tres set ingles = '{float(inglesBach23.get())}' "
                                           f"where id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionBach23.get():
                            cursor.execute(f"update segundo_bach_tres set religion = '{float(religionBach23.get())}' "
                                           f"where  id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if griegoBach23.get():
                            cursor.execute(f"update segundo_bach_tres set griego = '{float(griegoBach23.get())}' "
                                           f"where  id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaBach23.get():
                            cursor.execute(f"update segundo_bach_tres set ef = '{float(efisicaBach23.get())}' "
                                           f"where  id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaBach23.get():
                            cursor.execute(f"update segundo_bach_tres set informatica = '{float(informaticaBach23.get())}' "
                                           f"where id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if filosofiaBach23.get():
                            cursor.execute(f"update segundo_bach_tres set filosofia = '{float(filosofiaBach23.get())}' "
                                           f"where  id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if cnsBach23.get():
                            cursor.execute(f"update segundo_bach_tres set cns = '{float(cnsBach23.get())}' "
                                           f"where id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass


                    elif trimestre53.get() == 4:
                        if lenguaBach23.get():
                            cursor.execute(f"update segundo_bach_septiembre set lengua = '{float(lenguaBach23.get())}' "
                                           f"where  id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if matesBach23.get():
                            cursor.execute(
                                f"update segundo_bach_septiembre set mates_aplicadas = '{float(matesBach23.get())}' "
                                f"where  id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaBach23.get():
                            cursor.execute(f"update segundo_bach_septiembre set historia = '{float(historiaBach23.get())}' "
                                           f"where  id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if historiaarteBach23.get():
                            cursor.execute(
                                f"update segundo_bach_septiembre set historia_arte = '{float(historiaarteBach23.get())}' "
                                f"where  id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if latinBach23.get():
                            cursor.execute(f"update segundo_bach_septiembre set latin = '{float(latinBach23.get())}' "
                                           f"where  id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if economiaBach23.get():
                            cursor.execute(f"update segundo_bach_septiembre set economia = '{float(economiaBach23.get())}' "
                                           f"where  id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if francesBach23.get():
                            cursor.execute(f"update segundo_bach_septiembre set frances = '{float(francesBach23.get())}' "
                                           f"where  id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if inglesBach23.get():
                            cursor.execute(f"update segundo_bach_septiembre set ingles = '{float(inglesBach23.get())}' "
                                           f"where  id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if religionBach23.get():
                            cursor.execute(f"update segundo_bach_septiembre set religion = '{float(religionBach23.get())}' "
                                           f"where  id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if griegoBach23.get():
                            cursor.execute(f"update segundo_bach_septiembre set griego = '{float(griegoBach23.get())}' "
                                           f"where  id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if efisicaBach23.get():
                            cursor.execute(f"update segundo_bach_septiembre set ef = '{float(efisicaBach23.get())}' "
                                           f"where  id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if informaticaBach23.get():
                            cursor.execute(
                                f"update segundo_bach_septiembre set informatica = '{float(informaticaBach23.get())}' "
                                f"where  id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if filosofiaBach23.get():
                            cursor.execute(
                                f"update segundo_bach_septiembre set filosofia = '{float(filosofiaBach23.get())}' "
                                f"where  id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                        if cnsBach23.get():
                            cursor.execute(f"update segundo_bach_septiembre set cns = '{float(cnsBach23.get())}' "
                                           f"where  id = '{int(nombreBach23.get())}' ")
                            connexion.commit()
                        else:
                            pass

                    # --------actualizar la tabla de junio----------------------------
                    cursor.execute(
                        f"select lengua, mates_aplicadas, historia, historia_arte, latin, economia, frances, ingles, religion,"
                        f"griego, ef, informatica, filosofia, cns from segundo_bach_uno where id = '{int(nombreBach23.get())}' ")
                    stock = cursor.fetchall()

                    cursor.execute(
                        f"select lengua, mates_aplicadas, historia, historia_arte, latin, economia, frances, ingles, religion,"
                        f"griego, ef, informatica, filosofia, cns from segundo_bach_uno where id = '{int(nombreBach23.get())}' ")
                    stock1 = cursor.fetchall()

                    cursor.execute(
                        f"select lengua, mates_aplicadas, historia, historia_arte, latin, economia, frances, ingles, religion,"
                        f"griego, ef, informatica, filosofia, cns from segundo_bach_uno where id = '{int(nombreBach23.get())}' ")
                    stock2 = cursor.fetchall()

                    lengua = (stock[0][0] + stock1[0][0] + stock2[0][0]) / 3
                    matematicas = (stock[0][1] + stock1[0][1] + stock2[0][1]) / 3
                    historia = (stock[0][2] + stock1[0][1] + stock2[0][1]) / 3
                    historia_arte = (stock[0][3] + stock1[0][3] + stock2[0][3]) / 3
                    latin = (stock[0][4] + stock1[0][4] + stock2[0][4]) / 3
                    economia = (stock[0][5] + stock1[0][5] + stock2[0][5]) / 3
                    frances = (stock[0][6] + stock1[0][6] + stock2[0][6]) / 3
                    ingles = (stock[0][7] + stock1[0][7] + stock2[0][7]) / 3
                    religion = (stock[0][8] + stock1[0][8] + stock2[0][8]) / 3
                    griego = (stock[0][9] + stock1[0][9] + stock2[0][9]) / 3
                    ef = (stock[0][10] + stock1[0][10] + stock2[0][10]) / 3
                    informatica = (stock[0][11] + stock1[0][11] + stock2[0][11]) / 3
                    filosofia = (stock[0][12] + stock1[0][12] + stock2[0][12]) / 3
                    cns = (stock[0][13] + stock1[0][13] + stock2[0][13]) / 3

                    cursor.execute(f"update segundo_bach_junio set lengua = '{lengua}' "
                                   f"where  id = '{int(nombreBach23.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set mates_aplicadas = '{matematicas}' "
                                   f"where  id = '{int(nombreBach23.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set historia = '{historia}' "
                                   f"where  id = '{int(nombreBach23.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set historia_arte = '{historia_arte}' "
                                   f"where  id = '{int(nombreBach23.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set latin = '{latin}' "
                                   f"where id = '{int(nombreBach23.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set economia = '{economia}' "
                                   f"where  id = '{int(nombreBach23.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set frances = '{frances}' "
                                   f"where id = '{int(nombreBach23.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set ingles = '{ingles}' "
                                   f"where  id = '{int(nombreBach23.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set religion = '{religion}' "
                                   f"where id = '{int(nombreBach23.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set griego = '{griego}' "
                                   f"where  id = '{int(nombreBach23.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set ef = '{ef}' "
                                   f"where  id = '{int(nombreBach23.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set informatica = '{informatica}' "
                                   f"where  id = '{int(nombreBach23.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set filosofia = '{filosofia}' "
                                   f"where  id = '{int(nombreBach23.get())}' ")
                    connexion.commit()

                    cursor.execute(f"update segundo_bach_junio set cns = '{cns}' "
                                   f"where  id = '{int(nombreBach23.get())}' ")
                    connexion.commit()

                    lenguaBach23.set("")
                    matesBach23.set("")
                    historiaBach23.set("")
                    historiaarteBach23.set("")
                    latinBach23.set("")
                    economiaBach23.set("")
                    francesBach23.set("")
                    inglesBach23.set("")
                    religionBach23.set("")
                    griegoBach23.set("")
                    efisicaBach23.set("")
                    informaticaBach23.set("")
                    filosofiaBach23.set("")
                    cnsBach23.set("")

                else:
                    pass

                connexion.close()

            except ValueError:
                pass

        except IndexError:
            pass


    #-------------------------funciones de verificacion de notas-------------------------------------

    def verifi1():
        if nombreId.get() == 1:
            def verificacionUno():
                """
                esta funcion permite ver las notas de un alumno de primero esba

                :return: nada
                """
                root = Toplevel()
                root.resizable(0, 0)
                root.title("DULA 1.0-NOTAS DE 1°ESBA")
                root.config(bg="grey75")
                root.geometry("509x450")
                root.iconbitmap("dula.ico")

                # ----------frames root ---------------------------------------
                frame = Frame(root)
                frame.config(bg="grey75")
                frame.pack()
                # -------------botones frames------------------------------------
                Button(frame, text="1°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: primero(), font=("comic sans ms", 10)).grid(row=0, column=0)
                Button(frame, text="2°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: segundo(), font=("comic sans ms", 10)).grid(row=0, column=1, padx=5, pady=5)
                Button(frame, text="3°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: tercero(), font=("comic sans ms", 10)).grid(row=0, column=2, padx=5, pady=5)
                Button(frame, text="Septiembre", cursor="hand2", activebackground="#F50743",
                       command=lambda: septiembre(), font=("comic sans ms", 10)).grid(row=0, column=3, padx=5, pady=5)

                # -----------frames root------------------------*
                frameText = Frame(root)
                frameText.pack()

                # ---------la cja de TEXTO-----------------------------
                textoInfo = Text(frameText, width=60, height=20, )
                textoInfo.config(bg="grey85", font=("comic sans ms", 10))
                textoInfo.grid(row=0, column=0, padx=5, pady=5)

                # ----------scrollbar---------------
                scrollVertical = Scrollbar(frameText, command=textoInfo.yview)
                scrollVertical.grid(row=0, column=1, sticky="wns", )
                textoInfo.config(yscrollcommand=scrollVertical.set)

                # -----BOTON DE CIERRE DE VENTANA----------------------
                botonCerrarV = Button(root, text="cerrar la ventana",
                                      command=root.destroy, activebackground="#F50743")
                botonCerrarV.config(font=("comic sans ms", 10), bg="salmon3", cursor="hand2")
                botonCerrarV.pack(side="left", anchor="s")

                # --------------------funciones de botones------------------------------------
                def primero():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from primero_esba_uno where nombre = '{nombreEsba1.get().upper()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL PRIMER TRIMESTRE*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nMATEMÁTICAS: " + str(stock[0][4])
                                         + "\n\nGEOGRAFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIAS NATURALES: " + str(stock[0][6])
                                         + "\n\nFRANCÉS: " + str(stock[0][7])
                                         + "\n\nINGLÉS: " + str(stock[0][8])
                                         + "\n\nRELIGIÓN: " + str(stock[0][9])
                                         + "\n\nEXPRESIÓN PLÁSTICA: " + str(stock[0][10])
                                         + "\n\nEDUCACIÓN FÍSICA: " + str(stock[0][11])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][12])
                                         )
                        connexion.close()
                    except IndexError:
                        pass

                def segundo():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from primero_esba_dos where nombre = '{nombreEsba1.get().upper()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL SEGUNDO TRIMESTRE*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nMATEMÁTICAS: " + str(stock[0][4])
                                         + "\n\nGEOGRAFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIAS NATURALES: " + str(stock[0][6])
                                         + "\n\nFRANCÉS: " + str(stock[0][7])
                                         + "\n\nINGLÉS: " + str(stock[0][8])
                                         + "\n\nRELIGIÓN: " + str(stock[0][9])
                                         + "\n\nEXPRESIÓN PLÁSTICA: " + str(stock[0][10])
                                         + "\n\nEDUCACIÓN FÍSICA: " + str(stock[0][11])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][12])
                                         )
                        connexion.close()



                    except IndexError:
                        pass

                def tercero():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from primero_esba_tres where nombre = '{nombreEsba1.get().upper()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0,
                                         "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL TERCER TRIMESTRE*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nMATEMÁTICAS: " + str(stock[0][4])
                                         + "\n\nGEOGRAFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIAS NATURALES: " + str(stock[0][6])
                                         + "\n\nFRANCÉS: " + str(stock[0][7])
                                         + "\n\nINGLÉS: " + str(stock[0][8])
                                         + "\n\nRELIGIÓN: " + str(stock[0][9])
                                         + "\n\nEXPRESIÓN PLÁSTICA: " + str(stock[0][10])
                                         + "\n\nEDUCACIÓN FÍSICA: " + str(stock[0][11])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][12])
                                         )
                        connexion.close()

                    except IndexError:
                        pass

                def septiembre():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(
                            f"select * from primero_esba_septiembre where nombre = '{nombreEsba1.get().upper()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0,
                                         "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL EXTRAORDINARIO*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nMATEMÁTICAS: " + str(stock[0][4])
                                         + "\n\nGEOGRAFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIAS NATURALES: " + str(stock[0][6])
                                         + "\n\nFRANCÉS: " + str(stock[0][7])
                                         + "\n\nINGLÉS: " + str(stock[0][8])
                                         + "\n\nRELIGIÓN: " + str(stock[0][9])
                                         + "\n\nEXPRESIÓN PLÁSTICA: " + str(stock[0][10])
                                         + "\n\nEDUCACIÓN FÍSICA: " + str(stock[0][11])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][12])
                                         )
                        connexion.close()

                    except IndexError:
                        pass

                root.mainloop()

            verificacionUno()

        elif nombreId.get() == 2:
            def verificacionUno1():
                """
                esta funcion permite ver las notas de un alumno de primero esba

                :return: nada
                """
                root = Toplevel()
                root.resizable(0, 0)
                root.title("DULA 1.0-NOTAS DE 1°ESBA")
                root.config(bg="grey75")
                root.geometry("509x450")
                root.iconbitmap("images/dula.ico")

                # ----------frames root ---------------------------------------
                frame = Frame(root)
                frame.config(bg="grey75")
                frame.pack()
                # -------------botones frames------------------------------------
                Button(frame, text="1°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: primero(), font=("comic sans ms", 10)).grid(row=0, column=0)
                Button(frame, text="2°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: segundo(), font=("comic sans ms", 10)).grid(row=0, column=1, padx=5, pady=5)
                Button(frame, text="3°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: tercero(), font=("comic sans ms", 10)).grid(row=0, column=2, padx=5, pady=5)
                Button(frame, text="Septiembre", cursor="hand2", activebackground="#F50743",
                       command=lambda: septiembre(), font=("comic sans ms", 10)).grid(row=0, column=3, padx=5, pady=5)

                # -----------frames root------------------------*
                frameText = Frame(root)
                frameText.pack()

                # ---------la cja de TEXTO-----------------------------
                textoInfo = Text(frameText, width=60, height=20, )
                textoInfo.config(bg="grey85", font=("comic sans ms", 10))
                textoInfo.grid(row=0, column=0, padx=5, pady=5)

                # ----------scrollbar---------------
                scrollVertical = Scrollbar(frameText, command=textoInfo.yview)
                scrollVertical.grid(row=0, column=1, sticky="wns", )
                textoInfo.config(yscrollcommand=scrollVertical.set)

                # -----BOTON DE CIERRE DE VENTANA----------------------
                botonCerrarV = Button(root, text="cerrar la ventana",
                                      command=root.destroy, activebackground="#F50743")
                botonCerrarV.config(font=("comic sans ms", 10), bg="salmon3", cursor="hand2")
                botonCerrarV.pack(side="left", anchor="s")

                # --------------------funciones de botones------------------------------------
                def primero():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from primero_esba_uno where id = '{nombreEsba1.get()}' ")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL PRIMER TRIMESTRE*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nMATEMÁTICAS: " + str(stock[0][4])
                                         + "\n\nGEOGRAFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIAS NATURALES: " + str(stock[0][6])
                                         + "\n\nFRANCÉS: " + str(stock[0][7])
                                         + "\n\nINGLÉS: " + str(stock[0][8])
                                         + "\n\nRELIGIÓN: " + str(stock[0][9])
                                         + "\n\nEXPRESIÓN PLÁSTICA: " + str(stock[0][10])
                                         + "\n\nEDUCACIÓN FÍSICA: " + str(stock[0][11])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][12])
                                         )
                        connexion.close()
                    except IndexError:
                        pass

                def segundo():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from primero_esba_dos where id = '{nombreEsba1.get()}' ")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL SEGUNDO TRIMESTRE*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nMATEMÁTICAS: " + str(stock[0][4])
                                         + "\n\nGEOGRAFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIAS NATURALES: " + str(stock[0][6])
                                         + "\n\nFRANCÉS: " + str(stock[0][7])
                                         + "\n\nINGLÉS: " + str(stock[0][8])
                                         + "\n\nRELIGIÓN: " + str(stock[0][9])
                                         + "\n\nEXPRESIÓN PLÁSTICA: " + str(stock[0][10])
                                         + "\n\nEDUCACIÓN FÍSICA: " + str(stock[0][11])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][12])
                                         )
                        connexion.close()



                    except IndexError:
                        pass

                def tercero():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from primero_esba_tres where id = '{nombreEsba1.get()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0,
                                         "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL TERCER TRIMESTRE*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nMATEMÁTICAS: " + str(stock[0][4])
                                         + "\n\nGEOGRAFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIAS NATURALES: " + str(stock[0][6])
                                         + "\n\nFRANCÉS: " + str(stock[0][7])
                                         + "\n\nINGLÉS: " + str(stock[0][8])
                                         + "\n\nRELIGIÓN: " + str(stock[0][9])
                                         + "\n\nEXPRESIÓN PLÁSTICA: " + str(stock[0][10])
                                         + "\n\nEDUCACIÓN FÍSICA: " + str(stock[0][11])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][12])
                                         )
                        connexion.close()

                    except IndexError:
                        pass

                def septiembre():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(
                            f"select * from primero_esba_septiembre where id = '{nombreEsba1.get()}' ")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0,
                                         "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL EXTRAORDINARIO*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nMATEMÁTICAS: " + str(stock[0][4])
                                         + "\n\nGEOGRAFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIAS NATURALES: " + str(stock[0][6])
                                         + "\n\nFRANCÉS: " + str(stock[0][7])
                                         + "\n\nINGLÉS: " + str(stock[0][8])
                                         + "\n\nRELIGIÓN: " + str(stock[0][9])
                                         + "\n\nEXPRESIÓN PLÁSTICA: " + str(stock[0][10])
                                         + "\n\nEDUCACIÓN FÍSICA: " + str(stock[0][11])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][12])
                                         )
                        connexion.close()

                    except IndexError:
                        pass

                root.mainloop()

            verificacionUno1()

        else:
            pass


    def verifi2():
        if nombreId1.get() == 1:
            def verificacionDos():

                """
                esta funcion permite ver las notas de un alumno de segundo esba

                :return: nada
                """
                root = Toplevel()
                root.config(bg="grey75")
                root.resizable(0, 0)
                root.title("DULA 1.0-NOTAS DE 2°ESBA")
                root.geometry("509x450")
                root.iconbitmap("dula.ico")

                # ----------frames root ---------------------------------------
                frame = Frame(root)
                frame.config(bg="grey75")
                frame.pack()
                # -------------botones frames------------------------------------
                Button(frame, text="1°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: primero(), font=("comic sans ms", 10)).grid(row=0, column=0)
                Button(frame, text="2°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: segundo(), font=("comic sans ms", 10)).grid(row=0, column=1, padx=5, pady=5)
                Button(frame, text="3°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: tercero(), font=("comic sans ms", 10)).grid(row=0, column=2, padx=5, pady=5)
                Button(frame, text="Septiembre", cursor="hand2", activebackground="#F50743",
                       command=lambda: septiembre(), font=("comic sans ms", 10)).grid(row=0, column=3, padx=5, pady=5)

                # -----------frames root------------------------*
                frameText = Frame(root)
                frameText.pack()

                # ---------la cja de TEXTO-----------------------------
                textoInfo = Text(frameText, width=60, height=20, )
                textoInfo.config(bg="grey85", font=("comic sans ms", 10))
                textoInfo.grid(row=0, column=0, padx=5, pady=5)

                # ----------scrollbar---------------
                scrollVertical = Scrollbar(frameText, command=textoInfo.yview)
                scrollVertical.grid(row=0, column=1, sticky="wns", )
                textoInfo.config(yscrollcommand=scrollVertical.set)

                # -----BOTON DE CIERRE DE VENTANA----------------------
                botonCerrarV = Button(root, text="cerrar la ventana",
                                      command=root.destroy, activebackground="#F50743")
                botonCerrarV.config(font=("comic sans ms", 10), bg="salmon3", cursor="hand2")
                botonCerrarV.pack(side="left", anchor="s")

                # --------------------funciones de botones------------------------------------
                def primero():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from segundo_esba_uno where nombre = '{nombreEsba2.get().upper()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL PRIMER TRIMESTRE*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nMATEMÁTICAS: " + str(stock[0][4])
                                         + "\n\nGEOGRAFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIAS NATURALES: " + str(stock[0][6])
                                         + "\n\nFRANCÉS: " + str(stock[0][7])
                                         + "\n\nINGLÉS: " + str(stock[0][8])
                                         + "\n\nRELIGIÓN: " + str(stock[0][9])
                                         + "\n\nEXPRESIÓN PLÁSTICA: " + str(stock[0][10])
                                         + "\n\nEDUCACIÓN FÍSICA: " + str(stock[0][11])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][12])
                                         )
                        connexion.close()
                    except IndexError:
                        pass

                def segundo():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from segundo_esba_dos where nombre = '{nombreEsba2.get().upper()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL SEGUNDO TRIMESTRE*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nMATEMÁTICAS: " + str(stock[0][4])
                                         + "\n\nGEOGRAFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIAS NATURALES: " + str(stock[0][6])
                                         + "\n\nFRANCÉS: " + str(stock[0][7])
                                         + "\n\nINGLÉS: " + str(stock[0][8])
                                         + "\n\nRELIGIÓN: " + str(stock[0][9])
                                         + "\n\nEXPRESIÓN PLÁSTICA: " + str(stock[0][10])
                                         + "\n\nEDUCACIÓN FÍSICA: " + str(stock[0][11])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][12])
                                         )
                        connexion.close()



                    except IndexError:
                        pass

                def tercero():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from segundo_esba_tres where nombre = '{nombreEsba2.get().upper()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0,
                                         "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL TERCER TRIMESTRE*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nMATEMÁTICAS: " + str(stock[0][4])
                                         + "\n\nGEOGRAFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIAS NATURALES: " + str(stock[0][6])
                                         + "\n\nFRANCÉS: " + str(stock[0][7])
                                         + "\n\nINGLÉS: " + str(stock[0][8])
                                         + "\n\nRELIGIÓN: " + str(stock[0][9])
                                         + "\n\nEXPRESIÓN PLÁSTICA: " + str(stock[0][10])
                                         + "\n\nEDUCACIÓN FÍSICA: " + str(stock[0][11])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][12])
                                         )
                        connexion.close()

                    except IndexError:
                        pass

                def septiembre():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(
                            f"select * from segundo_esba_septiembre where nombre = '{nombreEsba2.get().upper()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0,
                                         "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL EXTRAORDINARIO*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nMATEMÁTICAS: " + str(stock[0][4])
                                         + "\n\nGEOGRAFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIAS NATURALES: " + str(stock[0][6])
                                         + "\n\nFRANCÉS: " + str(stock[0][7])
                                         + "\n\nINGLÉS: " + str(stock[0][8])
                                         + "\n\nRELIGIÓN: " + str(stock[0][9])
                                         + "\n\nEXPRESIÓN PLÁSTICA: " + str(stock[0][10])
                                         + "\n\nEDUCACIÓN FÍSICA: " + str(stock[0][11])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][12])
                                         )
                        connexion.close()

                    except IndexError:
                        pass

                root.mainloop()

            verificacionDos()

        elif nombreId1.get() == 2:
            def verificacionDos1():

                """
                esta funcion permite ver las notas de un alumno de segundo esba

                :return: nada
                """
                root = Toplevel()
                root.config(bg="grey75")
                root.resizable(0, 0)
                root.title("DULA 1.0-NOTAS DE 2°ESBA")
                root.geometry("509x450")
                root.iconbitmap("dula.ico")

                # ----------frames root ---------------------------------------
                frame = Frame(root)
                frame.config(bg="grey75")
                frame.pack()
                # -------------botones frames------------------------------------
                Button(frame, text="1°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: primero(), font=("comic sans ms", 10)).grid(row=0, column=0)
                Button(frame, text="2°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: segundo(), font=("comic sans ms", 10)).grid(row=0, column=1, padx=5, pady=5)
                Button(frame, text="3°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: tercero(), font=("comic sans ms", 10)).grid(row=0, column=2, padx=5, pady=5)
                Button(frame, text="Septiembre", cursor="hand2", activebackground="#F50743",
                       command=lambda: septiembre(), font=("comic sans ms", 10)).grid(row=0, column=3, padx=5, pady=5)

                # -----------frames root------------------------*
                frameText = Frame(root)
                frameText.pack()

                # ---------la cja de TEXTO-----------------------------
                textoInfo = Text(frameText, width=60, height=20, )
                textoInfo.config(bg="grey85", font=("comic sans ms", 10))
                textoInfo.grid(row=0, column=0, padx=5, pady=5)

                # ----------scrollbar---------------
                scrollVertical = Scrollbar(frameText, command=textoInfo.yview)
                scrollVertical.grid(row=0, column=1, sticky="wns", )
                textoInfo.config(yscrollcommand=scrollVertical.set)

                # -----BOTON DE CIERRE DE VENTANA----------------------
                botonCerrarV = Button(root, text="cerrar la ventana",
                                      command=root.destroy, activebackground="#F50743")
                botonCerrarV.config(font=("comic sans ms", 10), bg="salmon3", cursor="hand2")
                botonCerrarV.pack(side="left", anchor="s")

                # --------------------funciones de botones------------------------------------
                def primero():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from segundo_esba_uno where id = '{nombreEsba2.get()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL PRIMER TRIMESTRE*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nMATEMÁTICAS: " + str(stock[0][4])
                                         + "\n\nGEOGRAFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIAS NATURALES: " + str(stock[0][6])
                                         + "\n\nFRANCÉS: " + str(stock[0][7])
                                         + "\n\nINGLÉS: " + str(stock[0][8])
                                         + "\n\nRELIGIÓN: " + str(stock[0][9])
                                         + "\n\nEXPRESIÓN PLÁSTICA: " + str(stock[0][10])
                                         + "\n\nEDUCACIÓN FÍSICA: " + str(stock[0][11])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][12])
                                         )
                        connexion.close()
                    except IndexError:
                        pass

                def segundo():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from segundo_esba_dos where id = '{nombreEsba2.get()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL SEGUNDO TRIMESTRE*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nMATEMÁTICAS: " + str(stock[0][4])
                                         + "\n\nGEOGRAFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIAS NATURALES: " + str(stock[0][6])
                                         + "\n\nFRANCÉS: " + str(stock[0][7])
                                         + "\n\nINGLÉS: " + str(stock[0][8])
                                         + "\n\nRELIGIÓN: " + str(stock[0][9])
                                         + "\n\nEXPRESIÓN PLÁSTICA: " + str(stock[0][10])
                                         + "\n\nEDUCACIÓN FÍSICA: " + str(stock[0][11])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][12])
                                         )
                        connexion.close()



                    except IndexError:
                        pass

                def tercero():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from segundo_esba_tres where id = '{nombreEsba2.get()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0,
                                         "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL TERCER TRIMESTRE*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nMATEMÁTICAS: " + str(stock[0][4])
                                         + "\n\nGEOGRAFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIAS NATURALES: " + str(stock[0][6])
                                         + "\n\nFRANCÉS: " + str(stock[0][7])
                                         + "\n\nINGLÉS: " + str(stock[0][8])
                                         + "\n\nRELIGIÓN: " + str(stock[0][9])
                                         + "\n\nEXPRESIÓN PLÁSTICA: " + str(stock[0][10])
                                         + "\n\nEDUCACIÓN FÍSICA: " + str(stock[0][11])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][12])
                                         )
                        connexion.close()

                    except IndexError:
                        pass

                def septiembre():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(
                            f"select * from segundo_esba_septiembre where id = '{nombreEsba2.get()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0,
                                         "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL EXTRAORDINARIO*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nMATEMÁTICAS: " + str(stock[0][4])
                                         + "\n\nGEOGRAFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIAS NATURALES: " + str(stock[0][6])
                                         + "\n\nFRANCÉS: " + str(stock[0][7])
                                         + "\n\nINGLÉS: " + str(stock[0][8])
                                         + "\n\nRELIGIÓN: " + str(stock[0][9])
                                         + "\n\nEXPRESIÓN PLÁSTICA: " + str(stock[0][10])
                                         + "\n\nEDUCACIÓN FÍSICA: " + str(stock[0][11])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][12])
                                         )
                        connexion.close()

                    except IndexError:
                        pass

                root.mainloop()

            verificacionDos1()


        else:
            pass



    def verifi3():
        if nombreId2.get() == 1:
            def verificacionTres():
                """
                esta funcion permite ver las notas de un alumno de TERCERO esba

                :return: nada
                """
                root = Toplevel()
                root.resizable(0, 0)
                root.title("DULA 1.0-NOTAS DE 3°ESBA")
                root.config(bg="grey75")
                root.geometry("509x450")
                root.iconbitmap("dula.ico")

                # ----------frames root ---------------------------------------
                frame = Frame(root)
                frame.config(bg="grey75")
                frame.pack()
                # -------------botones frames------------------------------------
                Button(frame, text="1°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: primero(), font=("comic sans ms", 10)).grid(row=0, column=0)
                Button(frame, text="2°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: segundo(), font=("comic sans ms", 10)).grid(row=0, column=1, padx=5, pady=5)
                Button(frame, text="3°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: tercero(), font=("comic sans ms", 10)).grid(row=0, column=2, padx=5, pady=5)
                Button(frame, text="Septiembre", cursor="hand2", activebackground="#F50743",
                       command=lambda: septiembre(), font=("comic sans ms", 10)).grid(row=0, column=3, padx=5, pady=5)

                # -----------frames root------------------------*
                frameText = Frame(root)
                frameText.pack()

                # ---------la cja de TEXTO-----------------------------
                textoInfo = Text(frameText, width=60, height=20, )
                textoInfo.config(bg="grey85", font=("comic sans ms", 10))
                textoInfo.grid(row=0, column=0, padx=5, pady=5)

                # ----------scrollbar---------------
                scrollVertical = Scrollbar(frameText, command=textoInfo.yview)
                scrollVertical.grid(row=0, column=1, sticky="wns", )
                textoInfo.config(yscrollcommand=scrollVertical.set)

                # -----BOTON DE CIERRE DE VENTANA----------------------
                botonCerrarV = Button(root, text="cerrar la ventana",
                                      command=root.destroy, activebackground="#F50743")
                botonCerrarV.config(font=("comic sans ms", 10), bg="salmon3", cursor="hand2")
                botonCerrarV.pack(side="left", anchor="s")

                # --------------------funciones de botones------------------------------------
                def primero():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from tercero_esba_uno where nombre = '{nombreEsba3.get().upper()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL PRIMER TRIMESTRE*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nMATEMÁTICAS: " + str(stock[0][4])
                                         + "\n\nHISTORIA DE ÁFRICA Y GE: " + str(stock[0][5])
                                         + "\n\nFÍSICA Y QUÍMICA: " + str(stock[0][6])
                                         + "\n\nBIOLOGÍA Y GEOLOGÍA: " + str(stock[0][7])
                                         + "\n\nTECNOLOGÍA: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nRELIGIÓN: " + str(stock[0][11])
                                         + "\n\nEXPRESIÓN PLÁSTICA: " + str(stock[0][12])
                                         + "\n\nEDUCACIÓN FÍSICA: " + str(stock[0][13])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][14])
                                         )
                        connexion.close()
                    except IndexError:
                        pass

                def segundo():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from tercero_esba_dos where nombre = '{nombreEsba3.get().upper()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL SEGUNDO TRIMESTRE*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nMATEMÁTICAS: " + str(stock[0][4])
                                         + "\n\nHISTORIA DE ÁFRICA Y GE: " + str(stock[0][5])
                                         + "\n\nFÍSICA Y QUÍMICA: " + str(stock[0][6])
                                         + "\n\nBIOLOGÍA Y GEOLOGÍA: " + str(stock[0][7])
                                         + "\n\nTECNOLOGÍA: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nRELIGIÓN: " + str(stock[0][11])
                                         + "\n\nEXPRESIÓN PLÁSTICA: " + str(stock[0][12])
                                         + "\n\nEDUCACIÓN FÍSICA: " + str(stock[0][13])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][14])
                                         )
                        connexion.close()



                    except IndexError:
                        pass

                def tercero():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from tercero_esba_tres where nombre = '{nombreEsba3.get().upper()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL TERCER TRIMESTRE*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nMATEMÁTICAS: " + str(stock[0][4])
                                         + "\n\nHISTORIA DE ÁFRICA Y GE: " + str(stock[0][5])
                                         + "\n\nFÍSICA Y QUÍMICA: " + str(stock[0][6])
                                         + "\n\nBIOLOGÍA Y GEOLOGÍA: " + str(stock[0][7])
                                         + "\n\nTECNOLOGÍA: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nRELIGIÓN: " + str(stock[0][11])
                                         + "\n\nEXPRESIÓN PLÁSTICA: " + str(stock[0][12])
                                         + "\n\nEDUCACIÓN FÍSICA: " + str(stock[0][13])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][14])
                                         )
                        connexion.close()

                    except IndexError:
                        pass

                def septiembre():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(
                            f"select * from tercero_esba_septiembre where nombre = '{nombreEsba3.get().upper()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL EXTRAORDINARIO*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nMATEMÁTICAS: " + str(stock[0][4])
                                         + "\n\nHISTORIA DE ÁFRICA Y GE: " + str(stock[0][5])
                                         + "\n\nFÍSICA Y QUÍMICA: " + str(stock[0][6])
                                         + "\n\nBIOLOGÍA Y GEOLOGÍA: " + str(stock[0][7])
                                         + "\n\nTECNOLOGÍA: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nRELIGIÓN: " + str(stock[0][11])
                                         + "\n\nEXPRESIÓN PLÁSTICA: " + str(stock[0][12])
                                         + "\n\nEDUCACIÓN FÍSICA: " + str(stock[0][13])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][14])
                                         )
                        connexion.close()

                    except IndexError:
                        pass

                root.mainloop()
            verificacionTres()

        elif nombreId2.get() == 2:
            def verificacionTres1():
                """
                esta funcion permite ver las notas de un alumno de TERCERO esba

                :return: nada
                """
                root = Toplevel()
                root.resizable(0, 0)
                root.title("DULA 1.0-NOTAS DE 3°ESBA")
                root.config(bg="grey75")
                root.geometry("509x450")
                root.iconbitmap("dula.ico")

                # ----------frames root ---------------------------------------
                frame = Frame(root)
                frame.config(bg="grey75")
                frame.pack()
                # -------------botones frames------------------------------------
                Button(frame, text="1°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: primero(), font=("comic sans ms", 10)).grid(row=0, column=0)
                Button(frame, text="2°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: segundo(), font=("comic sans ms", 10)).grid(row=0, column=1, padx=5, pady=5)
                Button(frame, text="3°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: tercero(), font=("comic sans ms", 10)).grid(row=0, column=2, padx=5, pady=5)
                Button(frame, text="Septiembre", cursor="hand2", activebackground="#F50743",
                       command=lambda: septiembre(), font=("comic sans ms", 10)).grid(row=0, column=3, padx=5, pady=5)

                # -----------frames root------------------------*
                frameText = Frame(root)
                frameText.pack()

                # ---------la cja de TEXTO-----------------------------
                textoInfo = Text(frameText, width=60, height=20, )
                textoInfo.config(bg="grey85", font=("comic sans ms", 10))
                textoInfo.grid(row=0, column=0, padx=5, pady=5)

                # ----------scrollbar---------------
                scrollVertical = Scrollbar(frameText, command=textoInfo.yview)
                scrollVertical.grid(row=0, column=1, sticky="wns", )
                textoInfo.config(yscrollcommand=scrollVertical.set)

                # -----BOTON DE CIERRE DE VENTANA----------------------
                botonCerrarV = Button(root, text="cerrar la ventana",
                                      command=root.destroy, activebackground="#F50743")
                botonCerrarV.config(font=("comic sans ms", 10), bg="salmon3", cursor="hand2")
                botonCerrarV.pack(side="left", anchor="s")

                # --------------------funciones de botones------------------------------------
                def primero():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from tercero_esba_uno where id = '{nombreEsba3.get()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL PRIMER TRIMESTRE*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nMATEMÁTICAS: " + str(stock[0][4])
                                         + "\n\nHISTORIA DE ÁFRICA Y GE: " + str(stock[0][5])
                                         + "\n\nFÍSICA Y QUÍMICA: " + str(stock[0][6])
                                         + "\n\nBIOLOGÍA Y GEOLOGÍA: " + str(stock[0][7])
                                         + "\n\nTECNOLOGÍA: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nRELIGIÓN: " + str(stock[0][11])
                                         + "\n\nEXPRESIÓN PLÁSTICA: " + str(stock[0][12])
                                         + "\n\nEDUCACIÓN FÍSICA: " + str(stock[0][13])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][14])
                                         )
                        connexion.close()
                    except IndexError:
                        pass

                def segundo():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from tercero_esba_dos where id = '{nombreEsba3.get()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL SEGUNDO TRIMESTRE*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nMATEMÁTICAS: " + str(stock[0][4])
                                         + "\n\nHISTORIA DE ÁFRICA Y GE: " + str(stock[0][5])
                                         + "\n\nFÍSICA Y QUÍMICA: " + str(stock[0][6])
                                         + "\n\nBIOLOGÍA Y GEOLOGÍA: " + str(stock[0][7])
                                         + "\n\nTECNOLOGÍA: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nRELIGIÓN: " + str(stock[0][11])
                                         + "\n\nEXPRESIÓN PLÁSTICA: " + str(stock[0][12])
                                         + "\n\nEDUCACIÓN FÍSICA: " + str(stock[0][13])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][14])
                                         )
                        connexion.close()



                    except IndexError:
                        pass

                def tercero():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from tercero_esba_tres where id = '{nombreEsba3.get()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL TERCER TRIMESTRE*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nMATEMÁTICAS: " + str(stock[0][4])
                                         + "\n\nHISTORIA DE ÁFRICA Y GE: " + str(stock[0][5])
                                         + "\n\nFÍSICA Y QUÍMICA: " + str(stock[0][6])
                                         + "\n\nBIOLOGÍA Y GEOLOGÍA: " + str(stock[0][7])
                                         + "\n\nTECNOLOGÍA: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nRELIGIÓN: " + str(stock[0][11])
                                         + "\n\nEXPRESIÓN PLÁSTICA: " + str(stock[0][12])
                                         + "\n\nEDUCACIÓN FÍSICA: " + str(stock[0][13])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][14])
                                         )
                        connexion.close()

                    except IndexError:
                        pass

                def septiembre():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(
                            f"select * from tercero_esba_septiembre where id = '{nombreEsba3.get()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL EXTRAORDINARIO*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nMATEMÁTICAS: " + str(stock[0][4])
                                         + "\n\nHISTORIA DE ÁFRICA Y GE: " + str(stock[0][5])
                                         + "\n\nFÍSICA Y QUÍMICA: " + str(stock[0][6])
                                         + "\n\nBIOLOGÍA Y GEOLOGÍA: " + str(stock[0][7])
                                         + "\n\nTECNOLOGÍA: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nRELIGIÓN: " + str(stock[0][11])
                                         + "\n\nEXPRESIÓN PLÁSTICA: " + str(stock[0][12])
                                         + "\n\nEDUCACIÓN FÍSICA: " + str(stock[0][13])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][14])
                                         )
                        connexion.close()

                    except IndexError:
                        pass

                root.mainloop()

            verificacionTres1()



        else:
            pass


    def verifi4():

        if nombreId3.get() == 1:
            def verificacionCuarto():

                """
                esta funcion permite ver las notas de un alumno de cuarto esba

                :return: nada
                """
                root = Toplevel()
                root.resizable(0, 0)
                root.title("DULA 1.0-NOTAS DE 4°ESBA")
                root.config(bg="grey75")
                root.geometry("509x450")
                root.iconbitmap("dula.ico")

                # ----------frames root ---------------------------------------
                frame = Frame(root)
                frame.config(bg="grey75")
                frame.pack()
                # -------------botones frames------------------------------------
                Button(frame, text="1°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: primero(), font=("comic sans ms", 10)).grid(row=0, column=0)
                Button(frame, text="2°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: segundo(), font=("comic sans ms", 10)).grid(row=0, column=1, padx=5, pady=5)
                Button(frame, text="3°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: tercero(), font=("comic sans ms", 10)).grid(row=0, column=2, padx=5, pady=5)
                Button(frame, text="Septiembre", cursor="hand2", activebackground="#F50743",
                       command=lambda: septiembre(), font=("comic sans ms", 10)).grid(row=0, column=3, padx=5, pady=5)

                # -----------frames root------------------------*
                frameText = Frame(root)
                frameText.pack()

                # ---------la cja de TEXTO-----------------------------
                textoInfo = Text(frameText, width=60, height=20, )
                textoInfo.config(bg="grey85", font=("comic sans ms", 10))
                textoInfo.grid(row=0, column=0, padx=5, pady=5)

                # ----------scrollbar---------------
                scrollVertical = Scrollbar(frameText, command=textoInfo.yview)
                scrollVertical.grid(row=0, column=1, sticky="wns", )
                textoInfo.config(yscrollcommand=scrollVertical.set)

                # -----BOTON DE CIERRE DE VENTANA----------------------
                botonCerrarV = Button(root, text="cerrar la ventana",
                                      command=root.destroy, activebackground="#F50743")
                botonCerrarV.config(font=("comic sans ms", 10), bg="salmon3", cursor="hand2")
                botonCerrarV.pack(side="left", anchor="s")

                # --------------------funciones de botones------------------------------------
                def primero():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from cuarto_esba_uno where nombre = '{nombreEsba4.get().upper()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL PRIMER TRIMESTRE*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nMATEMÁTICAS: " + str(stock[0][4])
                                         + "\n\nHISTORIA UNIVERSAL: " + str(stock[0][5])
                                         + "\n\nFÍSICA Y QUÍMICA: " + str(stock[0][6])
                                         + "\n\nBIOLOGÍA Y GEOLOGÍA: " + str(stock[0][7])
                                         + "\n\nTECNOLOGÍA: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nRELIGIÓN: " + str(stock[0][11])
                                         + "\n\nEXPRESIÓN PLÁSTICA: " + str(stock[0][12])
                                         + "\n\nEDUCACIÓN FÍSICA: " + str(stock[0][13])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][14])
                                         )
                        connexion.close()
                    except IndexError:
                        pass

                def segundo():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from cuarto_esba_dos where nombre = '{nombreEsba4.get().upper()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL SEGUNDO TRIMESTRE*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nMATEMÁTICAS: " + str(stock[0][4])
                                         + "\n\nHISTORIA UNIVERSAL: " + str(stock[0][5])
                                         + "\n\nFÍSICA Y QUÍMICA: " + str(stock[0][6])
                                         + "\n\nBIOLOGÍA Y GEOLOGÍA: " + str(stock[0][7])
                                         + "\n\nTECNOLOGÍA: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nRELIGIÓN: " + str(stock[0][11])
                                         + "\n\nEXPRESIÓN PLÁSTICA: " + str(stock[0][12])
                                         + "\n\nEDUCACIÓN FÍSICA: " + str(stock[0][13])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][14])
                                         )
                        connexion.close()



                    except IndexError:
                        pass

                def tercero():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from cuarto_esba_tres where nombre = '{nombreEsba4.get().upper()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL TERCER TRIMESTRE*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nMATEMÁTICAS: " + str(stock[0][4])
                                         + "\n\nHISTORIA UNIVERSAL: " + str(stock[0][5])
                                         + "\n\nFÍSICA Y QUÍMICA: " + str(stock[0][6])
                                         + "\n\nBIOLOGÍA Y GEOLOGÍA: " + str(stock[0][7])
                                         + "\n\nTECNOLOGÍA: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nRELIGIÓN: " + str(stock[0][11])
                                         + "\n\nEXPRESIÓN PLÁSTICA: " + str(stock[0][12])
                                         + "\n\nEDUCACIÓN FÍSICA: " + str(stock[0][13])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][14])
                                         )
                        connexion.close()

                    except IndexError:
                        pass

                def septiembre():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(
                            f"select * from cuarto_esba_septiembre where nombre = '{nombreEsba4.get().upper()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL EXTRAORDINARIO*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nMATEMÁTICAS: " + str(stock[0][4])
                                         + "\n\nHISTORIA UNIVERSAL: " + str(stock[0][5])
                                         + "\n\nFÍSICA Y QUÍMICA: " + str(stock[0][6])
                                         + "\n\nBIOLOGÍA Y GEOLOGÍA: " + str(stock[0][7])
                                         + "\n\nTECNOLOGÍA: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nRELIGIÓN: " + str(stock[0][11])
                                         + "\n\nEXPRESIÓN PLÁSTICA: " + str(stock[0][12])
                                         + "\n\nEDUCACIÓN FÍSICA: " + str(stock[0][13])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][14])
                                         )
                        connexion.close()

                    except IndexError:
                        pass

                root.mainloop()

            verificacionCuarto()


        elif nombreId3.get() == 2:
            def verificacionCuarto1():

                """
                esta funcion permite ver las notas de un alumno de cuarto esba

                :return: nada
                """
                root = Toplevel()
                root.resizable(0, 0)
                root.title("DULA 1.0-NOTAS DE 4°ESBA")
                root.config(bg="grey75")
                root.geometry("509x450")
                root.iconbitmap("dula.ico")

                # ----------frames root ---------------------------------------
                frame = Frame(root)
                frame.config(bg="grey75")
                frame.pack()
                # -------------botones frames------------------------------------
                Button(frame, text="1°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: primero(), font=("comic sans ms", 10)).grid(row=0, column=0)
                Button(frame, text="2°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: segundo(), font=("comic sans ms", 10)).grid(row=0, column=1, padx=5, pady=5)
                Button(frame, text="3°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: tercero(), font=("comic sans ms", 10)).grid(row=0, column=2, padx=5, pady=5)
                Button(frame, text="Septiembre", cursor="hand2", activebackground="#F50743",
                       command=lambda: septiembre(), font=("comic sans ms", 10)).grid(row=0, column=3, padx=5, pady=5)

                # -----------frames root------------------------*
                frameText = Frame(root)
                frameText.pack()

                # ---------la cja de TEXTO-----------------------------
                textoInfo = Text(frameText, width=60, height=20, )
                textoInfo.config(bg="grey85", font=("comic sans ms", 10))
                textoInfo.grid(row=0, column=0, padx=5, pady=5)

                # ----------scrollbar---------------
                scrollVertical = Scrollbar(frameText, command=textoInfo.yview)
                scrollVertical.grid(row=0, column=1, sticky="wns", )
                textoInfo.config(yscrollcommand=scrollVertical.set)

                # -----BOTON DE CIERRE DE VENTANA----------------------
                botonCerrarV = Button(root, text="cerrar la ventana",
                                      command=root.destroy, activebackground="#F50743")
                botonCerrarV.config(font=("comic sans ms", 10), bg="salmon3", cursor="hand2")
                botonCerrarV.pack(side="left", anchor="s")

                # --------------------funciones de botones------------------------------------
                def primero():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from cuarto_esba_uno where id = '{nombreEsba4.get()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL PRIMER TRIMESTRE*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nMATEMÁTICAS: " + str(stock[0][4])
                                         + "\n\nHISTORIA UNIVERSAL: " + str(stock[0][5])
                                         + "\n\nFÍSICA Y QUÍMICA: " + str(stock[0][6])
                                         + "\n\nBIOLOGÍA Y GEOLOGÍA: " + str(stock[0][7])
                                         + "\n\nTECNOLOGÍA: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nRELIGIÓN: " + str(stock[0][11])
                                         + "\n\nEXPRESIÓN PLÁSTICA: " + str(stock[0][12])
                                         + "\n\nEDUCACIÓN FÍSICA: " + str(stock[0][13])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][14])
                                         )
                        connexion.close()
                    except IndexError:
                        pass

                def segundo():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from cuarto_esba_dos where id = '{nombreEsba4.get()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL SEGUNDO TRIMESTRE*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nMATEMÁTICAS: " + str(stock[0][4])
                                         + "\n\nHISTORIA UNIVERSAL: " + str(stock[0][5])
                                         + "\n\nFÍSICA Y QUÍMICA: " + str(stock[0][6])
                                         + "\n\nBIOLOGÍA Y GEOLOGÍA: " + str(stock[0][7])
                                         + "\n\nTECNOLOGÍA: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nRELIGIÓN: " + str(stock[0][11])
                                         + "\n\nEXPRESIÓN PLÁSTICA: " + str(stock[0][12])
                                         + "\n\nEDUCACIÓN FÍSICA: " + str(stock[0][13])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][14])
                                         )
                        connexion.close()



                    except IndexError:
                        pass

                def tercero():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from cuarto_esba_tres where  id = '{nombreEsba4.get()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL TERCER TRIMESTRE*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nMATEMÁTICAS: " + str(stock[0][4])
                                         + "\n\nHISTORIA UNIVERSAL: " + str(stock[0][5])
                                         + "\n\nFÍSICA Y QUÍMICA: " + str(stock[0][6])
                                         + "\n\nBIOLOGÍA Y GEOLOGÍA: " + str(stock[0][7])
                                         + "\n\nTECNOLOGÍA: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nRELIGIÓN: " + str(stock[0][11])
                                         + "\n\nEXPRESIÓN PLÁSTICA: " + str(stock[0][12])
                                         + "\n\nEDUCACIÓN FÍSICA: " + str(stock[0][13])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][14])
                                         )
                        connexion.close()

                    except IndexError:
                        pass

                def septiembre():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(
                            f"select * from cuarto_esba_septiembre where id = '{nombreEsba4.get()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL EXTRAORDINARIO*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nMATEMÁTICAS: " + str(stock[0][4])
                                         + "\n\nHISTORIA UNIVERSAL: " + str(stock[0][5])
                                         + "\n\nFÍSICA Y QUÍMICA: " + str(stock[0][6])
                                         + "\n\nBIOLOGÍA Y GEOLOGÍA: " + str(stock[0][7])
                                         + "\n\nTECNOLOGÍA: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nRELIGIÓN: " + str(stock[0][11])
                                         + "\n\nEXPRESIÓN PLÁSTICA: " + str(stock[0][12])
                                         + "\n\nEDUCACIÓN FÍSICA: " + str(stock[0][13])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][14])
                                         )
                        connexion.close()

                    except IndexError:
                        pass

                root.mainloop()

            verificacionCuarto1()
        else:
            pass



    def verifi51():
        if nombreId41.get() == 1:
            def verificacionBach11():

                """
                esta funcion permite ver las notas de un alumno de primero bach ciencias

                :return: nada
                """
                root = Toplevel()
                root.resizable(0, 0)
                root.title("DULA 1.0-NOTAS DE 1°BACH CIENCIAS")
                root.config(bg="grey75")
                root.geometry("509x450")
                root.iconbitmap("dula.ico")

                # ----------frames root ---------------------------------------
                frame = Frame(root)
                frame.config(bg="grey75")
                frame.pack()
                # -------------botones frames------------------------------------
                Button(frame, text="1°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: primero(), font=("comic sans ms", 10)).grid(row=0, column=0)
                Button(frame, text="2°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: segundo(), font=("comic sans ms", 10)).grid(row=0, column=1, padx=5, pady=5)
                Button(frame, text="3°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: tercero(), font=("comic sans ms", 10)).grid(row=0, column=2, padx=5, pady=5)
                Button(frame, text="Septiembre", cursor="hand2", activebackground="#F50743",
                       command=lambda: septiembre(), font=("comic sans ms", 10)).grid(row=0, column=3, padx=5, pady=5)

                # -----------frames root------------------------*
                frameText = Frame(root)
                frameText.pack()

                # ---------la cja de TEXTO-----------------------------
                textoInfo = Text(frameText, width=60, height=20, )
                textoInfo.config(bg="grey85", font=("comic sans ms", 10))
                textoInfo.grid(row=0, column=0, padx=5, pady=5)

                # ----------scrollbar---------------
                scrollVertical = Scrollbar(frameText, command=textoInfo.yview)
                scrollVertical.grid(row=0, column=1, sticky="wns", )
                textoInfo.config(yscrollcommand=scrollVertical.set)

                # -----BOTON DE CIERRE DE VENTANA----------------------
                botonCerrarV = Button(root, text="cerrar la ventana",
                                      command=root.destroy, activebackground="#F50743")
                botonCerrarV.config(font=("comic sans ms", 10), bg="salmon3", cursor="hand2")
                botonCerrarV.pack(side="left", anchor="s")

                # --------------------funciones de botones------------------------------------
                def primero():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from primero_bach_uno where nombre = '{nombreBach11.get().upper()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL PRIMER TRIMESTRE*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nHISTORIA DE ÁFRICA Y GE: " + str(stock[0][4])
                                         + "\n\nFILOSOFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIAS DE LA TIERRA Y M.A: " + str(stock[0][6])
                                         + "\n\nECONOMÍA: " + str(stock[0][7])
                                         + "\n\nRELIGIÓN: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nMATEMÁTICAS I: " + str(stock[0][11])
                                         + "\n\nFÍSICA Y QUÍMICA: " + str(stock[0][12])
                                         + "\n\nBIOLOGÍA: " + str(stock[0][13])
                                         + "\n\nDIBUJO TÉCNICO: " + str(stock[0][19])
                                         + "\n\nEDUCACÍON FÍSICA: " + str(stock[0][20])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][21])
                                         )
                        connexion.close()
                    except IndexError:
                        pass

                def segundo():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from primero_bach_dos where nombre = '{nombreBach11.get().upper()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL SEGUNDO TRIMESTRE*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nHISTORIA DE ÁFRICA Y GE: " + str(stock[0][4])
                                         + "\n\nFILOSOFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIAS DE LA TIERRA Y M.A: " + str(stock[0][6])
                                         + "\n\nECONOMÍA: " + str(stock[0][7])
                                         + "\n\nRELIGIÓN: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nMATEMÁTICAS I: " + str(stock[0][11])
                                         + "\n\nFÍSICA Y QUÍMICA: " + str(stock[0][12])
                                         + "\n\nBIOLOGÍA: " + str(stock[0][13])
                                         + "\n\nDIBUJO TÉCNICO: " + str(stock[0][19])
                                         + "\n\nEDUCACÍON FÍSICA: " + str(stock[0][20])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][21])
                                         )
                        connexion.close()



                    except IndexError:
                        pass

                def tercero():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from primero_bach_tres where nombre = '{nombreBach11.get().upper()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL TERCER TRIMESTRE*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nHISTORIA DE ÁFRICA Y GE: " + str(stock[0][4])
                                         + "\n\nFILOSOFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIAS DE LA TIERRA Y M.A: " + str(stock[0][6])
                                         + "\n\nECONOMÍA: " + str(stock[0][7])
                                         + "\n\nRELIGIÓN: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nMATEMÁTICAS I: " + str(stock[0][11])
                                         + "\n\nFÍSICA Y QUÍMICA: " + str(stock[0][12])
                                         + "\n\nBIOLOGÍA: " + str(stock[0][13])
                                         + "\n\nDIBUJO TÉCNICO: " + str(stock[0][19])
                                         + "\n\nEDUCACÍON FÍSICA: " + str(stock[0][20])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][21])
                                         )
                        connexion.close()

                    except IndexError:
                        pass

                def septiembre():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(
                            f"select * from primero_bach_septiembre where nombre = '{nombreBach11.get().upper()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL EXTRAORDINARIO*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nHISTORIA DE ÁFRICA Y GE: " + str(stock[0][4])
                                         + "\n\nFILOSOFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIAS DE LA TIERRA Y M.A: " + str(stock[0][6])
                                         + "\n\nECONOMÍA: " + str(stock[0][7])
                                         + "\n\nRELIGIÓN: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nMATEMÁTICAS I: " + str(stock[0][11])
                                         + "\n\nFÍSICA Y QUÍMICA: " + str(stock[0][12])
                                         + "\n\nBIOLOGÍA: " + str(stock[0][13])
                                         + "\n\nDIBUJO TÉCNICO: " + str(stock[0][19])
                                         + "\n\nEDUCACÍON FÍSICA: " + str(stock[0][20])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][21])
                                         )
                        connexion.close()

                    except IndexError:
                        pass

                root.mainloop()

            verificacionBach11()

        elif nombreId41.get() == 2:
            def verificacionBach11x():

                """
                esta funcion permite ver las notas de un alumno de primero bach ciencias

                :return: nada
                """
                root = Toplevel()
                root.resizable(0, 0)
                root.title("DULA 1.0-NOTAS DE 1°BACH CIENCIAS")
                root.config(bg="grey75")
                root.geometry("509x450")
                root.iconbitmap("dula.ico")

                # ----------frames root ---------------------------------------
                frame = Frame(root)
                frame.config(bg="grey75")
                frame.pack()
                # -------------botones frames------------------------------------
                Button(frame, text="1°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: primero(), font=("comic sans ms", 10)).grid(row=0, column=0)
                Button(frame, text="2°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: segundo(), font=("comic sans ms", 10)).grid(row=0, column=1, padx=5, pady=5)
                Button(frame, text="3°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: tercero(), font=("comic sans ms", 10)).grid(row=0, column=2, padx=5, pady=5)
                Button(frame, text="Septiembre", cursor="hand2", activebackground="#F50743",
                       command=lambda: septiembre(), font=("comic sans ms", 10)).grid(row=0, column=3, padx=5, pady=5)

                # -----------frames root------------------------*
                frameText = Frame(root)
                frameText.pack()

                # ---------la cja de TEXTO-----------------------------
                textoInfo = Text(frameText, width=60, height=20, )
                textoInfo.config(bg="grey85", font=("comic sans ms", 10))
                textoInfo.grid(row=0, column=0, padx=5, pady=5)

                # ----------scrollbar---------------
                scrollVertical = Scrollbar(frameText, command=textoInfo.yview)
                scrollVertical.grid(row=0, column=1, sticky="wns", )
                textoInfo.config(yscrollcommand=scrollVertical.set)

                # -----BOTON DE CIERRE DE VENTANA----------------------
                botonCerrarV = Button(root, text="cerrar la ventana",
                                      command=root.destroy, activebackground="#F50743")
                botonCerrarV.config(font=("comic sans ms", 10), bg="salmon3", cursor="hand2")
                botonCerrarV.pack(side="left", anchor="s")

                # --------------------funciones de botones------------------------------------
                def primero():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from primero_bach_uno where id = '{nombreBach11.get()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL PRIMER TRIMESTRE*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nHISTORIA DE ÁFRICA Y GE: " + str(stock[0][4])
                                         + "\n\nFILOSOFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIAS DE LA TIERRA Y M.A: " + str(stock[0][6])
                                         + "\n\nECONOMÍA: " + str(stock[0][7])
                                         + "\n\nRELIGIÓN: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nMATEMÁTICAS I: " + str(stock[0][11])
                                         + "\n\nFÍSICA Y QUÍMICA: " + str(stock[0][12])
                                         + "\n\nBIOLOGÍA: " + str(stock[0][13])
                                         + "\n\nDIBUJO TÉCNICO: " + str(stock[0][19])
                                         + "\n\nEDUCACÍON FÍSICA: " + str(stock[0][20])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][21])
                                         )
                        connexion.close()
                    except IndexError:
                        pass

                def segundo():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from primero_bach_dos where id = '{nombreBach11.get()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL SEGUNDO TRIMESTRE*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nHISTORIA DE ÁFRICA Y GE: " + str(stock[0][4])
                                         + "\n\nFILOSOFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIAS DE LA TIERRA Y M.A: " + str(stock[0][6])
                                         + "\n\nECONOMÍA: " + str(stock[0][7])
                                         + "\n\nRELIGIÓN: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nMATEMÁTICAS I: " + str(stock[0][11])
                                         + "\n\nFÍSICA Y QUÍMICA: " + str(stock[0][12])
                                         + "\n\nBIOLOGÍA: " + str(stock[0][13])
                                         + "\n\nDIBUJO TÉCNICO: " + str(stock[0][19])
                                         + "\n\nEDUCACÍON FÍSICA: " + str(stock[0][20])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][21])
                                         )
                        connexion.close()



                    except IndexError:
                        pass

                def tercero():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from primero_bach_tres where id = '{nombreBach11.get()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL TERCER TRIMESTRE*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nHISTORIA DE ÁFRICA Y GE: " + str(stock[0][4])
                                         + "\n\nFILOSOFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIAS DE LA TIERRA Y M.A: " + str(stock[0][6])
                                         + "\n\nECONOMÍA: " + str(stock[0][7])
                                         + "\n\nRELIGIÓN: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nMATEMÁTICAS I: " + str(stock[0][11])
                                         + "\n\nFÍSICA Y QUÍMICA: " + str(stock[0][12])
                                         + "\n\nBIOLOGÍA: " + str(stock[0][13])
                                         + "\n\nDIBUJO TÉCNICO: " + str(stock[0][19])
                                         + "\n\nEDUCACÍON FÍSICA: " + str(stock[0][20])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][21])
                                         )
                        connexion.close()

                    except IndexError:
                        pass

                def septiembre():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(
                            f"select * from primero_bach_septiembre where id = '{nombreBach11.get()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL EXTRAORDINARIO*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nHISTORIA DE ÁFRICA Y GE: " + str(stock[0][4])
                                         + "\n\nFILOSOFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIAS DE LA TIERRA Y M.A: " + str(stock[0][6])
                                         + "\n\nECONOMÍA: " + str(stock[0][7])
                                         + "\n\nRELIGIÓN: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nMATEMÁTICAS I: " + str(stock[0][11])
                                         + "\n\nFÍSICA Y QUÍMICA: " + str(stock[0][12])
                                         + "\n\nBIOLOGÍA: " + str(stock[0][13])
                                         + "\n\nDIBUJO TÉCNICO: " + str(stock[0][19])
                                         + "\n\nEDUCACÍON FÍSICA: " + str(stock[0][20])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][21])
                                         )
                        connexion.close()

                    except IndexError:
                        pass

                root.mainloop()

            verificacionBach11x()
        else:
            pass


    def verifi52():
        if nombreId42.get() == 1:
            def verificacionBach12():

                """
                esta funcion permite ver las notas de un alumno de primero bach tecnologias

                :return: nada
                """
                root = Toplevel()
                root.resizable(0, 0)
                root.title("DULA 1.0-NOTAS DE 1°BACH TECNOLOGIA")
                root.config(bg="grey75")
                root.geometry("509x450")
                root.iconbitmap("dula.ico")

                # ----------frames root ---------------------------------------
                frame = Frame(root)
                frame.config(bg="grey75")
                frame.pack()
                # -------------botones frames------------------------------------
                Button(frame, text="1°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: primero(), font=("comic sans ms", 10)).grid(row=0, column=0)
                Button(frame, text="2°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: segundo(), font=("comic sans ms", 10)).grid(row=0, column=1, padx=5, pady=5)
                Button(frame, text="3°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: tercero(), font=("comic sans ms", 10)).grid(row=0, column=2, padx=5, pady=5)
                Button(frame, text="Septiembre", cursor="hand2", activebackground="#F50743",
                       command=lambda: septiembre(), font=("comic sans ms", 10)).grid(row=0, column=3, padx=5, pady=5)

                # -----------frames root------------------------*
                frameText = Frame(root)
                frameText.pack()

                # ---------la cja de TEXTO-----------------------------
                textoInfo = Text(frameText, width=60, height=20, )
                textoInfo.config(bg="grey85", font=("comic sans ms", 10))
                textoInfo.grid(row=0, column=0, padx=5, pady=5)

                # ----------scrollbar---------------
                scrollVertical = Scrollbar(frameText, command=textoInfo.yview)
                scrollVertical.grid(row=0, column=1, sticky="wns", )
                textoInfo.config(yscrollcommand=scrollVertical.set)

                # -----BOTON DE CIERRE DE VENTANA----------------------
                botonCerrarV = Button(root, text="cerrar la ventana",
                                      command=root.destroy, activebackground="#F50743")
                botonCerrarV.config(font=("comic sans ms", 10), bg="salmon3", cursor="hand2")
                botonCerrarV.pack(side="left", anchor="s")

                # --------------------funciones de botones------------------------------------
                def primero():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from primero_bach_uno where nombre = '{nombreBach12.get().upper()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL PRIMER TRIMESTRE*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nHISTORIA DE ÁFRICA Y GE: " + str(stock[0][4])
                                         + "\n\nFILOSOFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIAS DE LA TIERRA Y M.A: " + str(stock[0][6])
                                         + "\n\nECONOMÍA: " + str(stock[0][7])
                                         + "\n\nRELIGIÓN: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nMATEMÁTICAS I: " + str(stock[0][11])
                                         + "\n\nTECNOLOGÍA: " + str(stock[0][18])
                                         + "\n\nBIOLOGÍA: " + str(stock[0][13])
                                         + "\n\nDIBUJO TÉCNICO: " + str(stock[0][19])
                                         + "\n\nEDUCACÍON FÍSICA: " + str(stock[0][20])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][21])
                                         )
                        connexion.close()
                    except IndexError:
                        pass

                def segundo():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from primero_bach_dos where nombre = '{nombreBach12.get().upper()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL SEGUNDO TRIMESTRE*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nHISTORIA DE ÁFRICA Y GE: " + str(stock[0][4])
                                         + "\n\nFILOSOFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIAS DE LA TIERRA Y M.A: " + str(stock[0][6])
                                         + "\n\nECONOMÍA: " + str(stock[0][7])
                                         + "\n\nRELIGIÓN: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nMATEMÁTICAS I: " + str(stock[0][11])
                                         + "\n\nTECNOLOGÍA: " + str(stock[0][18])
                                         + "\n\nBIOLOGÍA: " + str(stock[0][13])
                                         + "\n\nDIBUJO TÉCNICO: " + str(stock[0][19])
                                         + "\n\nEDUCACÍON FÍSICA: " + str(stock[0][20])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][21])
                                         )
                        connexion.close()



                    except IndexError:
                        pass

                def tercero():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from primero_bach_tres where nombre = '{nombreBach12.get().upper()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL TERCER TRIMESTRE*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nHISTORIA DE ÁFRICA Y GE: " + str(stock[0][4])
                                         + "\n\nFILOSOFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIAS DE LA TIERRA Y M.A: " + str(stock[0][6])
                                         + "\n\nECONOMÍA: " + str(stock[0][7])
                                         + "\n\nRELIGIÓN: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nMATEMÁTICAS I: " + str(stock[0][11])
                                         + "\n\nTECNOLOGÍA: " + str(stock[0][18])
                                         + "\n\nBIOLOGÍA: " + str(stock[0][13])
                                         + "\n\nDIBUJO TÉCNICO: " + str(stock[0][19])
                                         + "\n\nEDUCACÍON FÍSICA: " + str(stock[0][20])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][21])
                                         )
                        connexion.close()

                    except IndexError:
                        pass

                def septiembre():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(
                            f"select * from primero_bach_septiembre where nombre = '{nombreBach12.get().upper()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL EXTRAORDINARIO*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nHISTORIA DE ÁFRICA Y GE: " + str(stock[0][4])
                                         + "\n\nFILOSOFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIAS DE LA TIERRA Y M.A: " + str(stock[0][6])
                                         + "\n\nECONOMÍA: " + str(stock[0][7])
                                         + "\n\nRELIGIÓN: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nMATEMÁTICAS I: " + str(stock[0][11])
                                         + "\n\nTECNOLOGÍA: " + str(stock[0][18])
                                         + "\n\nBIOLOGÍA: " + str(stock[0][13])
                                         + "\n\nDIBUJO TÉCNICO: " + str(stock[0][19])
                                         + "\n\nEDUCACÍON FÍSICA: " + str(stock[0][20])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][21])
                                         )
                        connexion.close()

                    except IndexError:
                        pass

                root.mainloop()

            verificacionBach12()

        elif nombreId42.get() == 2:
            def verificacionBach12x():

                """
                esta funcion permite ver las notas de un alumno de primero bach tecnologias

                :return: nada
                """
                root = Toplevel()
                root.resizable(0, 0)
                root.title("DULA 1.0-NOTAS DE 1°BACH TECNOLOGIA")
                root.config(bg="grey75")
                root.geometry("509x450")
                root.iconbitmap("dula.ico")

                # ----------frames root ---------------------------------------
                frame = Frame(root)
                frame.config(bg="grey75")
                frame.pack()
                # -------------botones frames------------------------------------
                Button(frame, text="1°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: primero(), font=("comic sans ms", 10)).grid(row=0, column=0)
                Button(frame, text="2°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: segundo(), font=("comic sans ms", 10)).grid(row=0, column=1, padx=5, pady=5)
                Button(frame, text="3°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: tercero(), font=("comic sans ms", 10)).grid(row=0, column=2, padx=5, pady=5)
                Button(frame, text="Septiembre", cursor="hand2", activebackground="#F50743",
                       command=lambda: septiembre(), font=("comic sans ms", 10)).grid(row=0, column=3, padx=5, pady=5)

                # -----------frames root------------------------*
                frameText = Frame(root)
                frameText.pack()

                # ---------la cja de TEXTO-----------------------------
                textoInfo = Text(frameText, width=60, height=20, )
                textoInfo.config(bg="grey85", font=("comic sans ms", 10))
                textoInfo.grid(row=0, column=0, padx=5, pady=5)

                # ----------scrollbar---------------
                scrollVertical = Scrollbar(frameText, command=textoInfo.yview)
                scrollVertical.grid(row=0, column=1, sticky="wns", )
                textoInfo.config(yscrollcommand=scrollVertical.set)

                # -----BOTON DE CIERRE DE VENTANA----------------------
                botonCerrarV = Button(root, text="cerrar la ventana",
                                      command=root.destroy, activebackground="#F50743")
                botonCerrarV.config(font=("comic sans ms", 10), bg="salmon3", cursor="hand2")
                botonCerrarV.pack(side="left", anchor="s")

                # --------------------funciones de botones------------------------------------
                def primero():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from primero_bach_uno where id = '{nombreBach12.get()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL PRIMER TRIMESTRE*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nHISTORIA DE ÁFRICA Y GE: " + str(stock[0][4])
                                         + "\n\nFILOSOFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIAS DE LA TIERRA Y M.A: " + str(stock[0][6])
                                         + "\n\nECONOMÍA: " + str(stock[0][7])
                                         + "\n\nRELIGIÓN: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nMATEMÁTICAS I: " + str(stock[0][11])
                                         + "\n\nTECNOLOGÍA: " + str(stock[0][18])
                                         + "\n\nBIOLOGÍA: " + str(stock[0][13])
                                         + "\n\nDIBUJO TÉCNICO: " + str(stock[0][19])
                                         + "\n\nEDUCACÍON FÍSICA: " + str(stock[0][20])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][21])
                                         )
                        connexion.close()
                    except IndexError:
                        pass

                def segundo():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from primero_bach_dos where id = '{nombreBach12.get()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL SEGUNDO TRIMESTRE*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nHISTORIA DE ÁFRICA Y GE: " + str(stock[0][4])
                                         + "\n\nFILOSOFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIAS DE LA TIERRA Y M.A: " + str(stock[0][6])
                                         + "\n\nECONOMÍA: " + str(stock[0][7])
                                         + "\n\nRELIGIÓN: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nMATEMÁTICAS I: " + str(stock[0][11])
                                         + "\n\nTECNOLOGÍA: " + str(stock[0][18])
                                         + "\n\nBIOLOGÍA: " + str(stock[0][13])
                                         + "\n\nDIBUJO TÉCNICO: " + str(stock[0][19])
                                         + "\n\nEDUCACÍON FÍSICA: " + str(stock[0][20])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][21])
                                         )
                        connexion.close()



                    except IndexError:
                        pass

                def tercero():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from primero_bach_tres where id = '{nombreBach12.get()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL TERCER TRIMESTRE*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nHISTORIA DE ÁFRICA Y GE: " + str(stock[0][4])
                                         + "\n\nFILOSOFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIAS DE LA TIERRA Y M.A: " + str(stock[0][6])
                                         + "\n\nECONOMÍA: " + str(stock[0][7])
                                         + "\n\nRELIGIÓN: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nMATEMÁTICAS I: " + str(stock[0][11])
                                         + "\n\nTECNOLOGÍA: " + str(stock[0][18])
                                         + "\n\nBIOLOGÍA: " + str(stock[0][13])
                                         + "\n\nDIBUJO TÉCNICO: " + str(stock[0][19])
                                         + "\n\nEDUCACÍON FÍSICA: " + str(stock[0][20])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][21])
                                         )
                        connexion.close()

                    except IndexError:
                        pass

                def septiembre():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(
                            f"select * from primero_bach_septiembre where id = '{nombreBach12.get()}' ")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL EXTRAORDINARIO*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nHISTORIA DE ÁFRICA Y GE: " + str(stock[0][4])
                                         + "\n\nFILOSOFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIAS DE LA TIERRA Y M.A: " + str(stock[0][6])
                                         + "\n\nECONOMÍA: " + str(stock[0][7])
                                         + "\n\nRELIGIÓN: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nMATEMÁTICAS I: " + str(stock[0][11])
                                         + "\n\nTECNOLOGÍA: " + str(stock[0][18])
                                         + "\n\nBIOLOGÍA: " + str(stock[0][13])
                                         + "\n\nDIBUJO TÉCNICO: " + str(stock[0][19])
                                         + "\n\nEDUCACÍON FÍSICA: " + str(stock[0][20])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][21])
                                         )
                        connexion.close()

                    except IndexError:
                        pass

                root.mainloop()

            verificacionBach12x()

        else:
            pass




    def verifi53():
        if nombreId43.get() == 1:
            def verificacionBach13():
                """
                esta funcion permite ver las notas de un alumno de primero bach HUMANIDADES

                :return: nada
                """
                root = Toplevel()
                root.resizable(0, 0)
                root.title("DULA 1.0-NOTAS DE 1°BACH HUMANIDADES")
                root.config(bg="grey75")
                root.geometry("509x450")
                root.iconbitmap("dula.ico")

                # ----------frames root ---------------------------------------
                frame = Frame(root)
                frame.config(bg="grey75")
                frame.pack()
                # -------------botones frames------------------------------------
                Button(frame, text="1°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: primero(), font=("comic sans ms", 10)).grid(row=0, column=0)
                Button(frame, text="2°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: segundo(), font=("comic sans ms", 10)).grid(row=0, column=1, padx=5, pady=5)
                Button(frame, text="3°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: tercero(), font=("comic sans ms", 10)).grid(row=0, column=2, padx=5, pady=5)
                Button(frame, text="Septiembre", cursor="hand2", activebackground="#F50743",
                       command=lambda: septiembre(), font=("comic sans ms", 10)).grid(row=0, column=3, padx=5, pady=5)

                # -----------frames root------------------------*
                frameText = Frame(root)
                frameText.pack()

                # ---------la cja de TEXTO-----------------------------
                textoInfo = Text(frameText, width=60, height=20, )
                textoInfo.config(bg="grey85", font=("comic sans ms", 10))
                textoInfo.grid(row=0, column=0, padx=5, pady=5)

                # ----------scrollbar---------------
                scrollVertical = Scrollbar(frameText, command=textoInfo.yview)
                scrollVertical.grid(row=0, column=1, sticky="wns", )
                textoInfo.config(yscrollcommand=scrollVertical.set)

                # -----BOTON DE CIERRE DE VENTANA----------------------
                botonCerrarV = Button(root, text="cerrar la ventana",
                                      command=root.destroy, activebackground="#F50743")
                botonCerrarV.config(font=("comic sans ms", 10), bg="salmon3", cursor="hand2")
                botonCerrarV.pack(side="left", anchor="s")

                # --------------------funciones de botones------------------------------------
                def primero():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from primero_bach_uno where nombre = '{nombreBach13.get().upper()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL PRIMER TRIMESTRE*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nHISTORIA DE ÁFRICA Y GE: " + str(stock[0][4])
                                         + "\n\nFILOSOFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIAS DE LA TIERRA Y M.A: " + str(stock[0][6])
                                         + "\n\nECONOMÍA: " + str(stock[0][7])
                                         + "\n\nRELIGIÓN: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nMATEMÁTICAS APLICADAS: " + str(stock[0][14])
                                         + "\n\nGEOGRAFÍA DE GRANDES ESPACIOS: " + str(stock[0][15])
                                         + "\n\nLATÍN: " + str(stock[0][16])
                                         + "\n\nGRIEGO: " + str(stock[0][17])
                                         + "\n\nEDUCACÍON FÍSICA: " + str(stock[0][20])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][21])
                                         )
                        connexion.close()
                    except IndexError:
                        pass

                def segundo():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from primero_bach_dos where nombre = '{nombreBach13.get().upper()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL SEGUNDO TRIMESTRE*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nHISTORIA DE ÁFRICA Y GE: " + str(stock[0][4])
                                         + "\n\nFILOSOFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIAS DE LA TIERRA Y M.A: " + str(stock[0][6])
                                         + "\n\nECONOMÍA: " + str(stock[0][7])
                                         + "\n\nRELIGIÓN: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nMATEMÁTICAS APLICADAS: " + str(stock[0][14])
                                         + "\n\nGEOGRAFÍA DE GRANDES ESPACIOS: " + str(stock[0][15])
                                         + "\n\nLATÍN: " + str(stock[0][16])
                                         + "\n\nGRIEGO: " + str(stock[0][17])
                                         + "\n\nEDUCACÍON FÍSICA: " + str(stock[0][20])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][21])
                                         )
                        connexion.close()



                    except IndexError:
                        pass

                def tercero():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from primero_bach_tres where nombre = '{nombreBach13.get().upper()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL TERCER TRIMESTRE*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nHISTORIA DE ÁFRICA Y GE: " + str(stock[0][4])
                                         + "\n\nFILOSOFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIAS DE LA TIERRA Y M.A: " + str(stock[0][6])
                                         + "\n\nECONOMÍA: " + str(stock[0][7])
                                         + "\n\nRELIGIÓN: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nMATEMÁTICAS APLICADAS: " + str(stock[0][14])
                                         + "\n\nGEOGRAFÍA DE GRANDES ESPACIOS: " + str(stock[0][15])
                                         + "\n\nLATÍN: " + str(stock[0][16])
                                         + "\n\nGRIEGO: " + str(stock[0][17])
                                         + "\n\nEDUCACÍON FÍSICA: " + str(stock[0][20])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][21])
                                         )
                        connexion.close()

                    except IndexError:
                        pass

                def septiembre():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(
                            f"select * from primero_bach_septiembre where nombre = '{nombreBach13.get().upper()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL EXTRAORDINARIO*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nHISTORIA DE ÁFRICA Y GE: " + str(stock[0][4])
                                         + "\n\nFILOSOFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIAS DE LA TIERRA Y M.A: " + str(stock[0][6])
                                         + "\n\nECONOMÍA: " + str(stock[0][7])
                                         + "\n\nRELIGIÓN: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nMATEMÁTICAS APLICADAS: " + str(stock[0][14])
                                         + "\n\nGEOGRAFÍA DE GRANDES ESPACIOS: " + str(stock[0][15])
                                         + "\n\nLATÍN: " + str(stock[0][16])
                                         + "\n\nGRIEGO: " + str(stock[0][17])
                                         + "\n\nEDUCACÍON FÍSICA: " + str(stock[0][20])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][21])
                                         )
                        connexion.close()

                    except IndexError:
                        pass

                root.mainloop()

            verificacionBach13()

        elif nombreId43.get() == 2:
            def verificacionBach13x():
                """
                esta funcion permite ver las notas de un alumno de primero bach HUMANIDADES

                :return: nada
                """
                root = Toplevel()
                root.resizable(0, 0)
                root.title("DULA 1.0-NOTAS DE 1°BACH HUMANIDADES")
                root.config(bg="grey75")
                root.geometry("509x450")
                root.iconbitmap("dula.ico")

                # ----------frames root ---------------------------------------
                frame = Frame(root)
                frame.config(bg="grey75")
                frame.pack()
                # -------------botones frames------------------------------------
                Button(frame, text="1°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: primero(), font=("comic sans ms", 10)).grid(row=0, column=0)
                Button(frame, text="2°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: segundo(), font=("comic sans ms", 10)).grid(row=0, column=1, padx=5, pady=5)
                Button(frame, text="3°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: tercero(), font=("comic sans ms", 10)).grid(row=0, column=2, padx=5, pady=5)
                Button(frame, text="Septiembre", cursor="hand2", activebackground="#F50743",
                       command=lambda: septiembre(), font=("comic sans ms", 10)).grid(row=0, column=3, padx=5, pady=5)

                # -----------frames root------------------------*
                frameText = Frame(root)
                frameText.pack()

                # ---------la cja de TEXTO-----------------------------
                textoInfo = Text(frameText, width=60, height=20, )
                textoInfo.config(bg="grey85", font=("comic sans ms", 10))
                textoInfo.grid(row=0, column=0, padx=5, pady=5)

                # ----------scrollbar---------------
                scrollVertical = Scrollbar(frameText, command=textoInfo.yview)
                scrollVertical.grid(row=0, column=1, sticky="wns", )
                textoInfo.config(yscrollcommand=scrollVertical.set)

                # -----BOTON DE CIERRE DE VENTANA----------------------
                botonCerrarV = Button(root, text="cerrar la ventana",
                                      command=root.destroy, activebackground="#F50743")
                botonCerrarV.config(font=("comic sans ms", 10), bg="salmon3", cursor="hand2")
                botonCerrarV.pack(side="left", anchor="s")

                # --------------------funciones de botones------------------------------------
                def primero():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from primero_bach_uno where id = '{nombreBach13.get()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL PRIMER TRIMESTRE*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nHISTORIA DE ÁFRICA Y GE: " + str(stock[0][4])
                                         + "\n\nFILOSOFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIAS DE LA TIERRA Y M.A: " + str(stock[0][6])
                                         + "\n\nECONOMÍA: " + str(stock[0][7])
                                         + "\n\nRELIGIÓN: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nMATEMÁTICAS APLICADAS: " + str(stock[0][14])
                                         + "\n\nGEOGRAFÍA DE GRANDES ESPACIOS: " + str(stock[0][15])
                                         + "\n\nLATÍN: " + str(stock[0][16])
                                         + "\n\nGRIEGO: " + str(stock[0][17])
                                         + "\n\nEDUCACÍON FÍSICA: " + str(stock[0][20])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][21])
                                         )
                        connexion.close()
                    except IndexError:
                        pass

                def segundo():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from primero_bach_dos where id = '{nombreBach13.get()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL SEGUNDO TRIMESTRE*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nHISTORIA DE ÁFRICA Y GE: " + str(stock[0][4])
                                         + "\n\nFILOSOFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIAS DE LA TIERRA Y M.A: " + str(stock[0][6])
                                         + "\n\nECONOMÍA: " + str(stock[0][7])
                                         + "\n\nRELIGIÓN: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nMATEMÁTICAS APLICADAS: " + str(stock[0][14])
                                         + "\n\nGEOGRAFÍA DE GRANDES ESPACIOS: " + str(stock[0][15])
                                         + "\n\nLATÍN: " + str(stock[0][16])
                                         + "\n\nGRIEGO: " + str(stock[0][17])
                                         + "\n\nEDUCACÍON FÍSICA: " + str(stock[0][20])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][21])
                                         )
                        connexion.close()



                    except IndexError:
                        pass

                def tercero():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from primero_bach_tres where id = '{nombreBach13.get()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL TERCER TRIMESTRE*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nHISTORIA DE ÁFRICA Y GE: " + str(stock[0][4])
                                         + "\n\nFILOSOFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIAS DE LA TIERRA Y M.A: " + str(stock[0][6])
                                         + "\n\nECONOMÍA: " + str(stock[0][7])
                                         + "\n\nRELIGIÓN: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nMATEMÁTICAS APLICADAS: " + str(stock[0][14])
                                         + "\n\nGEOGRAFÍA DE GRANDES ESPACIOS: " + str(stock[0][15])
                                         + "\n\nLATÍN: " + str(stock[0][16])
                                         + "\n\nGRIEGO: " + str(stock[0][17])
                                         + "\n\nEDUCACÍON FÍSICA: " + str(stock[0][20])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][21])
                                         )
                        connexion.close()

                    except IndexError:
                        pass

                def septiembre():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(
                            f"select * from primero_bach_septiembre where id = '{nombreBach13.get()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL EXTRAORDINARIO*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nHISTORIA DE ÁFRICA Y GE: " + str(stock[0][4])
                                         + "\n\nFILOSOFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIAS DE LA TIERRA Y M.A: " + str(stock[0][6])
                                         + "\n\nECONOMÍA: " + str(stock[0][7])
                                         + "\n\nRELIGIÓN: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nMATEMÁTICAS APLICADAS: " + str(stock[0][14])
                                         + "\n\nGEOGRAFÍA DE GRANDES ESPACIOS: " + str(stock[0][15])
                                         + "\n\nLATÍN: " + str(stock[0][16])
                                         + "\n\nGRIEGO: " + str(stock[0][17])
                                         + "\n\nEDUCACÍON FÍSICA: " + str(stock[0][20])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][21])
                                         )
                        connexion.close()

                    except IndexError:
                        pass

                root.mainloop()

            verificacionBach13x()
        else:
            pass




    def verifi61():

        if nombreId51.get() == 1:
            def verificacionBach21():

                """
                esta funcion permite ver las notas de un alumno de segundo bach bach ciencias

                :return: nada
                """
                root = Toplevel()
                root.resizable(0, 0)
                root.title("DULA 1.0-NOTAS DE 2°BACH CIENCIAS")
                root.config(bg="grey75")
                root.geometry("509x450")
                root.iconbitmap("dula.ico")

                # ----------frames root ---------------------------------------
                frame = Frame(root)
                frame.config(bg="grey75")
                frame.pack()
                # -------------botones frames------------------------------------
                Button(frame, text="1°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: primero(), font=("comic sans ms", 10)).grid(row=0, column=0)
                Button(frame, text="2°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: segundo(), font=("comic sans ms", 10)).grid(row=0, column=1, padx=5, pady=5)
                Button(frame, text="3°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: tercero(), font=("comic sans ms", 10)).grid(row=0, column=2, padx=5, pady=5)
                Button(frame, text="Septiembre", cursor="hand2", activebackground="#F50743",
                       command=lambda: septiembre(), font=("comic sans ms", 10)).grid(row=0, column=3, padx=5, pady=5)

                # -----------frames root------------------------*
                frameText = Frame(root)
                frameText.pack()

                # ---------la cja de TEXTO-----------------------------
                textoInfo = Text(frameText, width=60, height=20, )
                textoInfo.config(bg="grey85", font=("comic sans ms", 10))
                textoInfo.grid(row=0, column=0, padx=5, pady=5)

                # ----------scrollbar---------------
                scrollVertical = Scrollbar(frameText, command=textoInfo.yview)
                scrollVertical.grid(row=0, column=1, sticky="wns", )
                textoInfo.config(yscrollcommand=scrollVertical.set)

                # -----BOTON DE CIERRE DE VENTANA----------------------
                botonCerrarV = Button(root, text="cerrar la ventana",
                                      command=root.destroy, activebackground="#F50743")
                botonCerrarV.config(font=("comic sans ms", 10), bg="salmon3", cursor="hand2")
                botonCerrarV.pack(side="left", anchor="s")

                # --------------------funciones de botones------------------------------------
                def primero():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from segundo_bach_uno where nombre = '{nombreBach21.get().upper()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL PRIMER TRIMESTRE*******************"
                                         + "\n\nLENGUA Y LITERATURA: " + str(stock[0][3])
                                         + "\n\nHISTORIA DEL MUNDO ACTUAL: " + str(stock[0][4])
                                         + "\n\nHISTORIA DE LA FILOSOFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIA DE LA NATURALEZA Y SALUD " + str(stock[0][6])
                                         + "\n\nECONOMÍA: " + str(stock[0][7])
                                         + "\n\nRELIGIÓN: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nMATEMÁTICAS II: " + str(stock[0][11])
                                         + "\n\nQUÍMICA: " + str(stock[0][12])
                                         + "\n\nGEOLOGÍA: " + str(stock[0][13])
                                         + "\n\nELECTROTECNIA: " + str(stock[0][14])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][22])
                                         )
                        connexion.close()
                    except IndexError:
                        pass

                def segundo():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from segundo_bach_dos where nombre = '{nombreBach21.get().upper()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL SEGUNDO TRIMESTRE*******************"
                                         + "\n\nLENGUA Y LITERATURA: " + str(stock[0][3])
                                         + "\n\nHISTORIA DEL MUNDO ACTUAL: " + str(stock[0][4])
                                         + "\n\nHISTORIA DE LA FILOSOFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIA DE LA NATURALEZA Y SALUD " + str(stock[0][6])
                                         + "\n\nECONOMÍA: " + str(stock[0][7])
                                         + "\n\nRELIGIÓN: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nMATEMÁTICAS II: " + str(stock[0][11])
                                         + "\n\nQUÍMICA: " + str(stock[0][12])
                                         + "\n\nGEOLOGÍA: " + str(stock[0][13])
                                         + "\n\nELECTROTECNIA: " + str(stock[0][14])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][22])
                                         )
                        connexion.close()



                    except IndexError:
                        pass

                def tercero():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from segundo_bach_tres where nombre = '{nombreBach21.get().upper()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL TERCER TRIMESTRE*******************"
                                         + "\n\nLENGUA Y LITERATURA: " + str(stock[0][3])
                                         + "\n\nHISTORIA DEL MUNDO ACTUAL: " + str(stock[0][4])
                                         + "\n\nHISTORIA DE LA FILOSOFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIA DE LA NATURALEZA Y SALUD " + str(stock[0][6])
                                         + "\n\nECONOMÍA: " + str(stock[0][7])
                                         + "\n\nRELIGIÓN: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nMATEMÁTICAS II: " + str(stock[0][11])
                                         + "\n\nQUÍMICA: " + str(stock[0][12])
                                         + "\n\nGEOLOGÍA: " + str(stock[0][13])
                                         + "\n\nELECTROTECNIA: " + str(stock[0][14])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][22])
                                         )
                        connexion.close()

                    except IndexError:
                        pass

                def septiembre():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(
                            f"select * from segundo_bach_septiembre where nombre = '{nombreBach21.get().upper()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL EXTRAORDINARIO*******************"
                                         + "\n\nLENGUA Y LITERATURA: " + str(stock[0][3])
                                         + "\n\nHISTORIA DEL MUNDO ACTUAL: " + str(stock[0][4])
                                         + "\n\nHISTORIA DE LA FILOSOFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIA DE LA NATURALEZA Y SALUD " + str(stock[0][6])
                                         + "\n\nECONOMÍA: " + str(stock[0][7])
                                         + "\n\nRELIGIÓN: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nMATEMÁTICAS II: " + str(stock[0][11])
                                         + "\n\nQUÍMICA: " + str(stock[0][12])
                                         + "\n\nGEOLOGÍA: " + str(stock[0][13])
                                         + "\n\nELECTROTECNIA: " + str(stock[0][14])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][22])
                                         )
                        connexion.close()

                    except IndexError:
                        pass

                root.mainloop()

            verificacionBach21()

        elif nombreId51.get() == 2:
            def verificacionBach21x():

                """
                esta funcion permite ver las notas de un alumno de segundo bach bach ciencias

                :return: nada
                """
                root = Toplevel()
                root.resizable(0, 0)
                root.title("DULA 1.0-NOTAS DE 2°BACH CIENCIAS")
                root.config(bg="grey75")
                root.geometry("509x450")
                root.iconbitmap("dula.ico")

                # ----------frames root ---------------------------------------
                frame = Frame(root)
                frame.config(bg="grey75")
                frame.pack()
                # -------------botones frames------------------------------------
                Button(frame, text="1°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: primero(), font=("comic sans ms", 10)).grid(row=0, column=0)
                Button(frame, text="2°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: segundo(), font=("comic sans ms", 10)).grid(row=0, column=1, padx=5, pady=5)
                Button(frame, text="3°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: tercero(), font=("comic sans ms", 10)).grid(row=0, column=2, padx=5, pady=5)
                Button(frame, text="Septiembre", cursor="hand2", activebackground="#F50743",
                       command=lambda: septiembre(), font=("comic sans ms", 10)).grid(row=0, column=3, padx=5, pady=5)

                # -----------frames root------------------------*
                frameText = Frame(root)
                frameText.pack()

                # ---------la cja de TEXTO-----------------------------
                textoInfo = Text(frameText, width=60, height=20, )
                textoInfo.config(bg="grey85", font=("comic sans ms", 10))
                textoInfo.grid(row=0, column=0, padx=5, pady=5)

                # ----------scrollbar---------------
                scrollVertical = Scrollbar(frameText, command=textoInfo.yview)
                scrollVertical.grid(row=0, column=1, sticky="wns", )
                textoInfo.config(yscrollcommand=scrollVertical.set)

                # -----BOTON DE CIERRE DE VENTANA----------------------
                botonCerrarV = Button(root, text="cerrar la ventana",
                                      command=root.destroy, activebackground="#F50743")
                botonCerrarV.config(font=("comic sans ms", 10), bg="salmon3", cursor="hand2")
                botonCerrarV.pack(side="left", anchor="s")

                # --------------------funciones de botones------------------------------------
                def primero():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from segundo_bach_uno where id = '{nombreBach21.get()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL PRIMER TRIMESTRE*******************"
                                         + "\n\nLENGUA Y LITERATURA: " + str(stock[0][3])
                                         + "\n\nHISTORIA DEL MUNDO ACTUAL: " + str(stock[0][4])
                                         + "\n\nHISTORIA DE LA FILOSOFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIA DE LA NATURALEZA Y SALUD: " + str(stock[0][6])
                                         + "\n\nECONOMÍA: " + str(stock[0][7])
                                         + "\n\nRELIGIÓN: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nMATEMÁTICAS II: " + str(stock[0][11])
                                         + "\n\nQUÍMICA: " + str(stock[0][12])
                                         + "\n\nGEOLOGÍA: " + str(stock[0][13])
                                         + "\n\nELECTROTECNIA: " + str(stock[0][14])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][22])
                                         )
                        connexion.close()
                    except IndexError:
                        pass

                def segundo():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from segundo_bach_dos where id = '{nombreBach21.get()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL SEGUNDO TRIMESTRE*******************"
                                         + "\n\nLENGUA Y LITERATURA: " + str(stock[0][3])
                                         + "\n\nHISTORIA DEL MUNDO ACTUAL: " + str(stock[0][4])
                                         + "\n\nHISTORIA DE LA FILOSOFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIA DE LA NATURALEZA Y SALUD: " + str(stock[0][6])
                                         + "\n\nECONOMÍA: " + str(stock[0][7])
                                         + "\n\nRELIGIÓN: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nMATEMÁTICAS II: " + str(stock[0][11])
                                         + "\n\nQUÍMICA: " + str(stock[0][12])
                                         + "\n\nGEOLOGÍA: " + str(stock[0][13])
                                         + "\n\nELECTROTECNIA: " + str(stock[0][14])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][22])
                                         )
                        connexion.close()



                    except IndexError:
                        pass

                def tercero():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from segundo_bach_tres where id = '{nombreBach21.get()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL TERCER TRIMESTRE*******************"
                                         + "\n\nLENGUA Y LITERATURA: " + str(stock[0][3])
                                         + "\n\nHISTORIA DEL MUNDO ACTUAL: " + str(stock[0][4])
                                         + "\n\nHISTORIA DE LA FILOSOFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIA DE LA NATURALEZA Y SALUD: " + str(stock[0][6])
                                         + "\n\nECONOMÍA: " + str(stock[0][7])
                                         + "\n\nRELIGIÓN: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nMATEMÁTICAS II: " + str(stock[0][11])
                                         + "\n\nQUÍMICA: " + str(stock[0][12])
                                         + "\n\nGEOLOGÍA: " + str(stock[0][13])
                                         + "\n\nELECTROTECNIA: " + str(stock[0][14])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][22])
                                         )
                        connexion.close()

                    except IndexError:
                        pass

                def septiembre():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(
                            f"select * from segundo_bach_septiembre where id = '{nombreBach21.get()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL EXTRAORDINARIO*******************"
                                         + "\n\nLENGUA Y LITERATURA: " + str(stock[0][3])
                                         + "\n\nHISTORIA DEL MUNDO ACTUAL: " + str(stock[0][4])
                                         + "\n\nHISTORIA DE LA FILOSOFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIA DE LA NATURALEZA Y SALUD: " + str(stock[0][6])
                                         + "\n\nECONOMÍA: " + str(stock[0][7])
                                         + "\n\nRELIGIÓN: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nMATEMÁTICAS II: " + str(stock[0][11])
                                         + "\n\nQUÍMICA: " + str(stock[0][12])
                                         + "\n\nGEOLOGÍA: " + str(stock[0][13])
                                         + "\n\nELECTROTECNIA: " + str(stock[0][14])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][22])
                                         )
                        connexion.close()

                    except IndexError:
                        pass

                root.mainloop()

            verificacionBach21x()
        else:
            pass


    def verifi62():
        if nombreId52.get() == 1:
            def verificacionBach22():

                """
                esta funcion permite ver las notas de un alumno de SEGUNDO bach tecnologias

                :return: nada
                """
                root = Toplevel()
                root.resizable(0, 0)
                root.title("DULA 1.0-NOTAS DE 2°BACH TECNOLOGIA")
                root.config(bg="grey75")
                root.geometry("509x450")
                root.iconbitmap("dula.ico")

                # ----------frames root ---------------------------------------
                frame = Frame(root)
                frame.config(bg="grey75")
                frame.pack()
                # -------------botones frames------------------------------------
                Button(frame, text="1°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: primero(), font=("comic sans ms", 10)).grid(row=0, column=0)
                Button(frame, text="2°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: segundo(), font=("comic sans ms", 10)).grid(row=0, column=1, padx=5, pady=5)
                Button(frame, text="3°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: tercero(), font=("comic sans ms", 10)).grid(row=0, column=2, padx=5, pady=5)
                Button(frame, text="Septiembre", cursor="hand2", activebackground="#F50743",
                       command=lambda: septiembre(), font=("comic sans ms", 10)).grid(row=0, column=3, padx=5, pady=5)

                # -----------frames root------------------------*
                frameText = Frame(root)
                frameText.pack()

                # ---------la cja de TEXTO-----------------------------
                textoInfo = Text(frameText, width=60, height=20, )
                textoInfo.config(bg="grey85", font=("comic sans ms", 10))
                textoInfo.grid(row=0, column=0, padx=5, pady=5)

                # ----------scrollbar---------------
                scrollVertical = Scrollbar(frameText, command=textoInfo.yview)
                scrollVertical.grid(row=0, column=1, sticky="wns", )
                textoInfo.config(yscrollcommand=scrollVertical.set)

                # -----BOTON DE CIERRE DE VENTANA----------------------
                botonCerrarV = Button(root, text="cerrar la ventana",
                                      command=root.destroy, activebackground="#F50743")
                botonCerrarV.config(font=("comic sans ms", 10), bg="salmon3", cursor="hand2")
                botonCerrarV.pack(side="left", anchor="s")

                # --------------------funciones de botones------------------------------------
                def primero():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from segundo_bach_uno where nombre = '{nombreBach22.get().upper()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL PRIMER TRIMESTRE*******************"
                                         + "\n\nLENGUA Y LITERATURA: " + str(stock[0][3])
                                         + "\n\nHISTORIA DEL MUNDO ACTUAL: " + str(stock[0][4])
                                         + "\n\nHISTORIA DE LA FILOSOFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIA DE LA NATURALEZA Y SALUD: " + str(stock[0][6])
                                         + "\n\nECONOMÍA: " + str(stock[0][7])
                                         + "\n\nRELIGIÓN: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nMATEMÁTICAS II: " + str(stock[0][11])
                                         + "\n\nTECNOLOGÍA INDUSTRIAL II: " + str(stock[0][19])
                                         + "\n\nDIBUJO TECNICO II: " + str(stock[0][20])
                                         + "\n\nELECTROTECNIA: " + str(stock[0][14])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][22])
                                         )
                        connexion.close()
                    except IndexError:
                        pass

                def segundo():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from segundo_bach_dos where nombre = '{nombreBach22.get().upper()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL SEGUNDO TRIMESTRE*******************"
                                         + "\n\nLENGUA Y LITERATURA: " + str(stock[0][3])
                                         + "\n\nHISTORIA DEL MUNDO ACTUAL: " + str(stock[0][4])
                                         + "\n\nHISTORIA DE LA FILOSOFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIA DE LA NATURALEZA Y SALUD: " + str(stock[0][6])
                                         + "\n\nECONOMÍA: " + str(stock[0][7])
                                         + "\n\nRELIGIÓN: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nMATEMÁTICAS II: " + str(stock[0][11])
                                         + "\n\nTECNOLOGÍA INDUSTRIAL II: " + str(stock[0][19])
                                         + "\n\nDIBUJO TECNICO II: " + str(stock[0][20])
                                         + "\n\nELECTROTECNIA: " + str(stock[0][14])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][22])
                                         )
                        connexion.close()



                    except IndexError:
                        pass

                def tercero():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from segundo_bach_tres where nombre = '{nombreBach22.get().upper()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL TERCER TRIMESTRE*******************"
                                         + "\n\nLENGUA Y LITERATURA: " + str(stock[0][3])
                                         + "\n\nHISTORIA DEL MUNDO ACTUAL: " + str(stock[0][4])
                                         + "\n\nHISTORIA DE LA FILOSOFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIA DE LA NATURALEZA Y SALUD: " + str(stock[0][6])
                                         + "\n\nECONOMÍA: " + str(stock[0][7])
                                         + "\n\nRELIGIÓN: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nMATEMÁTICAS II: " + str(stock[0][11])
                                         + "\n\nTECNOLOGÍA INDUSTRIAL II: " + str(stock[0][19])
                                         + "\n\nDIBUJO TECNICO II: " + str(stock[0][20])
                                         + "\n\nELECTROTECNIA: " + str(stock[0][14])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][22])
                                         )
                        connexion.close()

                    except IndexError:
                        pass

                def septiembre():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(
                            f"select * from segundo_bach_septiembre where nombre = '{nombreBach22.get().upper()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL EXTRAORDINARIO*******************"
                                         + "\n\nLENGUA Y LITERATURA: " + str(stock[0][3])
                                         + "\n\nHISTORIA DEL MUNDO ACTUAL: " + str(stock[0][4])
                                         + "\n\nHISTORIA DE LA FILOSOFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIA DE LA NATURALEZA Y SALUD: " + str(stock[0][6])
                                         + "\n\nECONOMÍA: " + str(stock[0][7])
                                         + "\n\nRELIGIÓN: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nMATEMÁTICAS II: " + str(stock[0][11])
                                         + "\n\nTECNOLOGÍA INDUSTRIAL II: " + str(stock[0][19])
                                         + "\n\nDIBUJO TECNICO II: " + str(stock[0][20])
                                         + "\n\nELECTROTECNIA: " + str(stock[0][14])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][22])
                                         )
                        connexion.close()

                    except IndexError:
                        pass

                root.mainloop()

            verificacionBach22()

        elif nombreId52.get() == 2:
            def verificacionBach22x():

                """
                esta funcion permite ver las notas de un alumno de SEGUNDO bach tecnologias

                :return: nada
                """
                root = Toplevel()
                root.resizable(0, 0)
                root.title("DULA 1.0-NOTAS DE 2°BACH TECNOLOGIA")
                root.config(bg="grey75")
                root.geometry("509x450")
                root.iconbitmap("dula.ico")

                # ----------frames root ---------------------------------------
                frame = Frame(root)
                frame.config(bg="grey75")
                frame.pack()
                # -------------botones frames------------------------------------
                Button(frame, text="1°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: primero(), font=("comic sans ms", 10)).grid(row=0, column=0)
                Button(frame, text="2°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: segundo(), font=("comic sans ms", 10)).grid(row=0, column=1, padx=5, pady=5)
                Button(frame, text="3°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: tercero(), font=("comic sans ms", 10)).grid(row=0, column=2, padx=5, pady=5)
                Button(frame, text="Septiembre", cursor="hand2", activebackground="#F50743",
                       command=lambda: septiembre(), font=("comic sans ms", 10)).grid(row=0, column=3, padx=5, pady=5)

                # -----------frames root------------------------*
                frameText = Frame(root)
                frameText.pack()

                # ---------la cja de TEXTO-----------------------------
                textoInfo = Text(frameText, width=60, height=20, )
                textoInfo.config(bg="grey85", font=("comic sans ms", 10))
                textoInfo.grid(row=0, column=0, padx=5, pady=5)

                # ----------scrollbar---------------
                scrollVertical = Scrollbar(frameText, command=textoInfo.yview)
                scrollVertical.grid(row=0, column=1, sticky="wns", )
                textoInfo.config(yscrollcommand=scrollVertical.set)

                # -----BOTON DE CIERRE DE VENTANA----------------------
                botonCerrarV = Button(root, text="cerrar la ventana",
                                      command=root.destroy, activebackground="#F50743")
                botonCerrarV.config(font=("comic sans ms", 10), bg="salmon3", cursor="hand2")
                botonCerrarV.pack(side="left", anchor="s")

                # --------------------funciones de botones------------------------------------
                def primero():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from segundo_bach_uno where id = '{nombreBach22.get()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL PRIMER TRIMESTRE*******************"
                                         + "\n\nLENGUA Y LITERATURA: " + str(stock[0][3])
                                         + "\n\nHISTORIA DEL MUNDO ACTUAL: " + str(stock[0][4])
                                         + "\n\nHISTORIA DE LA FILOSOFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIA DE LA NATURALEZA Y SALUD: " + str(stock[0][6])
                                         + "\n\nECONOMÍA: " + str(stock[0][7])
                                         + "\n\nRELIGIÓN: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nMATEMÁTICAS II: " + str(stock[0][11])
                                         + "\n\nTECNOLOGÍA INDUSTRIAL II: " + str(stock[0][19])
                                         + "\n\nDIBUJO TECNICO II: " + str(stock[0][20])
                                         + "\n\nELECTROTECNIA: " + str(stock[0][14])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][22])
                                         )
                        connexion.close()
                    except IndexError:
                        pass

                def segundo():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from segundo_bach_dos where id = '{nombreBach22.get()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL SEGUNDO TRIMESTRE*******************"
                                         + "\n\nLENGUA Y LITERATURA: " + str(stock[0][3])
                                         + "\n\nHISTORIA DEL MUNDO ACTUAL: " + str(stock[0][4])
                                         + "\n\nHISTORIA DE LA FILOSOFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIA DE LA NATURALEZA Y SALUD: " + str(stock[0][6])
                                         + "\n\nECONOMÍA: " + str(stock[0][7])
                                         + "\n\nRELIGIÓN: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nMATEMÁTICAS II: " + str(stock[0][11])
                                         + "\n\nTECNOLOGÍA INDUSTRIAL II: " + str(stock[0][19])
                                         + "\n\nDIBUJO TECNICO II: " + str(stock[0][20])
                                         + "\n\nELECTROTECNIA: " + str(stock[0][14])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][22])
                                         )
                        connexion.close()



                    except IndexError:
                        pass

                def tercero():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from segundo_bach_tres where id = '{nombreBach22.get()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL TERCER TRIMESTRE*******************"
                                         + "\n\nLENGUA Y LITERATURA: " + str(stock[0][3])
                                         + "\n\nHISTORIA DEL MUNDO ACTUAL: " + str(stock[0][4])
                                         + "\n\nHISTORIA DE LA FILOSOFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIA DE LA NATURALEZA Y SALUD: " + str(stock[0][6])
                                         + "\n\nECONOMÍA: " + str(stock[0][7])
                                         + "\n\nRELIGIÓN: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nMATEMÁTICAS II: " + str(stock[0][11])
                                         + "\n\nTECNOLOGÍA INDUSTRIAL II: " + str(stock[0][19])
                                         + "\n\nDIBUJO TECNICO II: " + str(stock[0][20])
                                         + "\n\nELECTROTECNIA: " + str(stock[0][14])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][22])
                                         )
                        connexion.close()

                    except IndexError:
                        pass

                def septiembre():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from segundo_bach_septiembre where id = '{nombreBach22.get()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL EXTRAORDINARIO*******************"
                                         + "\n\nLENGUA Y LITERATURA: " + str(stock[0][3])
                                         + "\n\nHISTORIA DEL MUNDO ACTUAL: " + str(stock[0][4])
                                         + "\n\nHISTORIA DE LA FILOSOFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIA DE LA NATURALEZA Y SALUD: " + str(stock[0][6])
                                         + "\n\nECONOMÍA: " + str(stock[0][7])
                                         + "\n\nRELIGIÓN: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nMATEMÁTICAS II: " + str(stock[0][11])
                                         + "\n\nTECNOLOGÍA INDUSTRIAL II: " + str(stock[0][19])
                                         + "\n\nDIBUJO TECNICO II: " + str(stock[0][20])
                                         + "\n\nELECTROTECNIA: " + str(stock[0][14])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][22])
                                         )
                        connexion.close()

                    except IndexError:
                        pass

                root.mainloop()

            verificacionBach22x()
        else:
            pass


    def verifi63():
        if nombreId53.get() == 1:
            def verificacionBach23():
                """
                esta funcion permite ver las notas de un alumno de segundo bach HUMANIDADES

                :return: nada
                """
                root = Toplevel()
                root.resizable(0, 0)
                root.title("DULA 1.0-NOTAS DE 2°BACH HUMANIDADES")
                root.config(bg="grey75")
                root.geometry("509x450")
                root.iconbitmap("dula.ico")

                # ----------frames root ---------------------------------------
                frame = Frame(root)
                frame.config(bg="grey75")
                frame.pack()
                # -------------botones frames------------------------------------
                Button(frame, text="1°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: primero(), font=("comic sans ms", 10)).grid(row=0, column=0)
                Button(frame, text="2°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: segundo(), font=("comic sans ms", 10)).grid(row=0, column=1, padx=5, pady=5)
                Button(frame, text="3°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: tercero(), font=("comic sans ms", 10)).grid(row=0, column=2, padx=5, pady=5)
                Button(frame, text="Septiembre", cursor="hand2", activebackground="#F50743",
                       command=lambda: septiembre(), font=("comic sans ms", 10)).grid(row=0, column=3, padx=5, pady=5)

                # -----------frames root------------------------*
                frameText = Frame(root)
                frameText.pack()

                # ---------la cja de TEXTO-----------------------------
                textoInfo = Text(frameText, width=60, height=20, )
                textoInfo.config(bg="grey85", font=("comic sans ms", 10))
                textoInfo.grid(row=0, column=0, padx=5, pady=5)

                # ----------scrollbar---------------
                scrollVertical = Scrollbar(frameText, command=textoInfo.yview)
                scrollVertical.grid(row=0, column=1, sticky="wns", )
                textoInfo.config(yscrollcommand=scrollVertical.set)

                # -----BOTON DE CIERRE DE VENTANA----------------------
                botonCerrarV = Button(root, text="cerrar la ventana",
                                      command=root.destroy, activebackground="#F50743")
                botonCerrarV.config(font=("comic sans ms", 10), bg="salmon3", cursor="hand2")
                botonCerrarV.pack(side="left", anchor="s")

                # --------------------funciones de botones------------------------------------
                def primero():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from segundo_bach_uno where nombre = '{nombreBach23.get().upper()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL PRIMER TRIMESTRE*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nHISTORIA DEL MUNDO ACTUAL: " + str(stock[0][4])
                                         + "\n\nHISTORIA DE LA FILOSOFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIAS DE LA NATURALEZA Y SALUD: " + str(stock[0][6])
                                         + "\n\nECONOMÍA: " + str(stock[0][7])
                                         + "\n\nRELIGIÓN: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nMATEMÁTICAS APLICADAS: " + str(stock[0][15])
                                         + "\n\n:HISTORIA DEL ARTE:" + str(stock[0][16])
                                         + "\n\nLATÍN: " + str(stock[0][17])
                                         + "\n\nGRIEGO: " + str(stock[0][18])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][22])
                                         )
                        connexion.close()
                    except IndexError:
                        pass

                def segundo():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from segundo_bach_dos where nombre = '{nombreBach23.get().upper()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL SEGUNDO TRIMESTRE*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nHISTORIA DEL MUNDO ACTUAL: " + str(stock[0][4])
                                         + "\n\nHISTORIA DE LA FILOSOFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIAS DE LA NATURALEZA Y SALUD: " + str(stock[0][6])
                                         + "\n\nECONOMÍA: " + str(stock[0][7])
                                         + "\n\nRELIGIÓN: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nMATEMÁTICAS APLICADAS: " + str(stock[0][15])
                                         + "\n\n:HISTORIA DEL ARTE:" + str(stock[0][16])
                                         + "\n\nLATÍN: " + str(stock[0][17])
                                         + "\n\nGRIEGO: " + str(stock[0][18])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][22])
                                         )
                        connexion.close()



                    except IndexError:
                        pass

                def tercero():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from segundo_bach_tres where nombre = '{nombreBach23.get().upper()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL PRIMER TRIMESTRE*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nHISTORIA DEL MUNDO ACTUAL: " + str(stock[0][4])
                                         + "\n\nHISTORIA DE LA FILOSOFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIAS DE LA NATURALEZA Y SALUD: " + str(stock[0][6])
                                         + "\n\nECONOMÍA: " + str(stock[0][7])
                                         + "\n\nRELIGIÓN: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nMATEMÁTICAS APLICADAS: " + str(stock[0][15])
                                         + "\n\n:HISTORIA DEL ARTE:" + str(stock[0][16])
                                         + "\n\nLATÍN: " + str(stock[0][17])
                                         + "\n\nGRIEGO: " + str(stock[0][18])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][22])
                                         )
                        connexion.close()

                    except IndexError:
                        pass

                def septiembre():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(
                            f"select * from segundo_bach_septiembre where nombre = '{nombreBach23.get().upper()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL EXTRAORDINARIO*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nHISTORIA DEL MUNDO ACTUAL: " + str(stock[0][4])
                                         + "\n\nHISTORIA DE LA FILOSOFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIAS DE LA NATURALEZA Y SALUD: " + str(stock[0][6])
                                         + "\n\nECONOMÍA: " + str(stock[0][7])
                                         + "\n\nRELIGIÓN: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nMATEMÁTICAS APLICADAS: " + str(stock[0][15])
                                         + "\n\n:HISTORIA DEL ARTE:" + str(stock[0][16])
                                         + "\n\nLATÍN: " + str(stock[0][17])
                                         + "\n\nGRIEGO: " + str(stock[0][18])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][22])
                                         )
                        connexion.close()

                    except IndexError:
                        pass

                root.mainloop()

            verificacionBach23()

        elif nombreId53.get() == 2:
            def verificacionBach23x():
                """
                esta funcion permite ver las notas de un alumno de segundo bach HUMANIDADES

                :return: nada
                """
                root = Toplevel()
                root.resizable(0, 0)
                root.title("DULA 1.0-NOTAS DE 2°BACH HUMANIDADES")
                root.config(bg="grey75")
                root.geometry("509x450")
                root.iconbitmap("dula.ico")

                # ----------frames root ---------------------------------------
                frame = Frame(root)
                frame.config(bg="grey75")
                frame.pack()
                # -------------botones frames------------------------------------
                Button(frame, text="1°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: primero(), font=("comic sans ms", 10)).grid(row=0, column=0)
                Button(frame, text="2°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: segundo(), font=("comic sans ms", 10)).grid(row=0, column=1, padx=5, pady=5)
                Button(frame, text="3°Trimestre", cursor="hand2", activebackground="#F50743",
                       command=lambda: tercero(), font=("comic sans ms", 10)).grid(row=0, column=2, padx=5, pady=5)
                Button(frame, text="Septiembre", cursor="hand2", activebackground="#F50743",
                       command=lambda: septiembre(), font=("comic sans ms", 10)).grid(row=0, column=3, padx=5, pady=5)

                # -----------frames root------------------------*
                frameText = Frame(root)
                frameText.pack()

                # ---------la cja de TEXTO-----------------------------
                textoInfo = Text(frameText, width=60, height=20, )
                textoInfo.config(bg="grey85", font=("comic sans ms", 10))
                textoInfo.grid(row=0, column=0, padx=5, pady=5)

                # ----------scrollbar---------------
                scrollVertical = Scrollbar(frameText, command=textoInfo.yview)
                scrollVertical.grid(row=0, column=1, sticky="wns", )
                textoInfo.config(yscrollcommand=scrollVertical.set)

                # -----BOTON DE CIERRE DE VENTANA----------------------
                botonCerrarV = Button(root, text="cerrar la ventana",
                                      command=root.destroy, activebackground="#F50743")
                botonCerrarV.config(font=("comic sans ms", 10), bg="salmon3", cursor="hand2")
                botonCerrarV.pack(side="left", anchor="s")

                # --------------------funciones de botones------------------------------------
                def primero():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from segundo_bach_uno where id = '{nombreBach23.get()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL PRIMER TRIMESTRE*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nHISTORIA DEL MUNDO ACTUAL: " + str(stock[0][4])
                                         + "\n\nHISTORIA DE LA FILOSOFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIAS DE LA NATURALEZA Y SALUD: " + str(stock[0][6])
                                         + "\n\nECONOMÍA: " + str(stock[0][7])
                                         + "\n\nRELIGIÓN: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nMATEMÁTICAS APLICADAS: " + str(stock[0][15])
                                         + "\n\n:HISTORIA DEL ARTE:" + str(stock[0][16])
                                         + "\n\nLATÍN: " + str(stock[0][17])
                                         + "\n\nGRIEGO: " + str(stock[0][18])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][22])
                                         )
                        connexion.close()
                    except IndexError:
                        pass

                def segundo():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from segundo_bach_dos where id = '{nombreBach23.get()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL SEGUNDO TRIMESTRE*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nHISTORIA DEL MUNDO ACTUAL: " + str(stock[0][4])
                                         + "\n\nHISTORIA DE LA FILOSOFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIAS DE LA NATURALEZA Y SALUD: " + str(stock[0][6])
                                         + "\n\nECONOMÍA: " + str(stock[0][7])
                                         + "\n\nRELIGIÓN: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nMATEMÁTICAS APLICADAS: " + str(stock[0][15])
                                         + "\n\n:HISTORIA DEL ARTE:" + str(stock[0][16])
                                         + "\n\nLATÍN: " + str(stock[0][17])
                                         + "\n\nGRIEGO: " + str(stock[0][18])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][22])
                                         )
                        connexion.close()



                    except IndexError:
                        pass

                def tercero():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(f"select * from segundo_bach_tres where id = '{nombreBach23.get()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL PRIMER TRIMESTRE*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nHISTORIA DEL MUNDO ACTUAL: " + str(stock[0][4])
                                         + "\n\nHISTORIA DE LA FILOSOFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIAS DE LA NATURALEZA Y SALUD: " + str(stock[0][6])
                                         + "\n\nECONOMÍA: " + str(stock[0][7])
                                         + "\n\nRELIGIÓN: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nMATEMÁTICAS APLICADAS: " + str(stock[0][15])
                                         + "\n\n:HISTORIA DEL ARTE:" + str(stock[0][16])
                                         + "\n\nLATÍN: " + str(stock[0][17])
                                         + "\n\nGRIEGO: " + str(stock[0][18])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][22])
                                         )
                        connexion.close()

                    except IndexError:
                        pass

                def septiembre():
                    try:
                        textoInfo.delete(1.0, END)
                        connexion = sqlite3.connect(nameBD.nomBD())
                        cursor = connexion.cursor()
                        cursor.execute(
                            f"select * from segundo_bach_septiembre where id = '{nombreBach23.get()}'")
                        stock = cursor.fetchall()

                        textoInfo.config(fg="black")
                        textoInfo.insert(1.0, "ALUMNO/A: " + stock[0][1]
                                         + "\nAÑO ACADÉMICO: " + stock[0][2]
                                         + "\n*****************NOTAS DEL EXTRAORDINARIO*******************"
                                         + "\n\nLENGUA ESPAÑOLA: " + str(stock[0][3])
                                         + "\n\nHISTORIA DEL MUNDO ACTUAL: " + str(stock[0][4])
                                         + "\n\nHISTORIA DE LA FILOSOFÍA: " + str(stock[0][5])
                                         + "\n\nCIENCIAS DE LA NATURALEZA Y SALUD: " + str(stock[0][6])
                                         + "\n\nECONOMÍA: " + str(stock[0][7])
                                         + "\n\nRELIGIÓN: " + str(stock[0][8])
                                         + "\n\nFRANCÉS: " + str(stock[0][9])
                                         + "\n\nINGLÉS: " + str(stock[0][10])
                                         + "\n\nMATEMÁTICAS APLICADAS: " + str(stock[0][15])
                                         + "\n\n:HISTORIA DEL ARTE:" + str(stock[0][16])
                                         + "\n\nLATÍN: " + str(stock[0][17])
                                         + "\n\nGRIEGO: " + str(stock[0][18])
                                         + "\n\nINFORMÁTICA: " + str(stock[0][22])
                                         )
                        connexion.close()

                    except IndexError:
                        pass

                root.mainloop()

            verificacionBach23x()
        else:
            pass




    #------------------funcion de cierre de ventana---------------------------
    


    root.protocol("WM_DELETE_WINDOW", lambda:loguin.cierreSesion(root))
    root.mainloop()
