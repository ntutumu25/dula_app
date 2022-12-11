from tkinter.ttk import *
from tkinter import *
import archivos
import sqlite3
import loguin
import nameBD

def notas():
    """
    esta funcion contiene la venta de busqueda de notas de los alumnos
    :return:
    """

    root = Toplevel()
    root.title("DULA 1.0-NOTAS")
    root.iconbitmap("images/dula.ico")
    root.config(bg = "grey85")
    root.geometry("950x550")


    #------------label root----------------------------------------------------


    logo = PhotoImage(file="images/logoTsei.png")
    labeLogo = Label(root, image=logo)
    labeLogo.pack(side="right", anchor="n")

    Label(root, text = "SECCIÓN DE NOTAS", font=("jokerman", 14), bd=5, relief="groov",
          fg="black", bg="lemonchiffon2").pack(padx = 10, pady = 10)


    #-------------frames root-------------------------------------------------------------

    frame = Frame(root, width = 1000,)
    frame.config(bg = "grey85")
    frame.pack(expand = 0, fill = "both", padx = 10, pady = 5)

    frameTree = Frame(root)
    frameTree.config(bg="grey85")
    frameTree.pack(pady=5)
    #------------variables-----------------------------

    nombreAlumno = StringVar()
    academico = StringVar()



    Label(frame, text = "Nombre completo:", bg = "white",
          font=("comic sans ms", 11), relief = "groove").grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "e")

    Label(frame, text = "Curso:", bg = "white",
          font=("comic sans ms", 11), relief = "groove").grid(row = 0, column = 2, padx = 5, pady = 5, sticky = "e")

    #-------------Entry frames---------------------------------------------------------------

    Entry(frame, width = 34, font=("comic sans ms", 11),
          textvariable = nombreAlumno).grid(row = 0, column = 1, padx = 5, pady = 5, sticky = "w")

    #-----------------botes frames-----------------------------------------------------------------
    Button(frame, text = "Busar", activebackground="#F50743", cursor = "hand2", command = lambda:buscar(),
           font=("comic sans ms", 11)).grid(row = 2, column = 1, padx = 5, pady = 5)


    #--------------Combobox frames------------------------------------------------------------

    combo = Combobox(frame, width = 10, state = "readonly")
    combo.grid(row = 0, column = 3, padx = 5, pady = 5,)
    combo['values'] = ('1°ESBA', '2°ESBA', '3°ESBA', '4°ESBA', '1°BACH', '2°BACH')
    combo.current(0)
    #-------------------treeview-------------------------------------------------------

    treev_scroll = Scrollbar(root)
    treev_scroll.pack(side = RIGHT, fill = Y)




    treev = Treeview(root, yscrollcommand = treev_scroll.set ,
            columns = ('Asignaturas', '1°Trimestre', '2°Trimestre', '3°Trimestre', 'Junio', 'Septiembre'),
                     show = 'headings')
    treev.column('Asignaturas', minwidth = 0, width = 200)
    treev.column('1°Trimestre', minwidth = 0, width = 100)
    treev.column('2°Trimestre', minwidth = 0, width = 100)
    treev.column('3°Trimestre', minwidth = 0, width = 100)
    treev.column('Junio', minwidth = 0, width = 100)
    treev.column('Septiembre', minwidth = 0, width = 100)

    treev.heading('Asignaturas', text = "Asignaturas")
    treev.heading('1°Trimestre', text = "1°Trimestre")
    treev.heading('2°Trimestre', text = "2°Trimestre")
    treev.heading('3°Trimestre', text = "3°Trimestre")
    treev.heading('Junio', text = "Junio")
    treev.heading('Septiembre', text = "Septiembre")
    treev.pack(expand = 1, fill = "both", padx = 10, pady = 7)
    treev_scroll.config(command=treev.yview)


    #-------------boton para cerrar la ventana--------------------------------------
    botonCerrarV = Button(root, text="cerrar la ventana",
                          command=root.destroy, activebackground="#F50743")
    botonCerrarV.config(font=("comic sans ms", 10), bg="salmon3", cursor="hand2")
    botonCerrarV.pack(side="left", anchor="s")






    #--------------funcion de buscar de escritura---------------------------
    def buscar():
        """
        #esta funcion permite mostrar informacion academica del alumno buscado
        :return:
        """
        # ---------------------label academico------------------------------------
        Label(frame, text="AÑO ACADÉMICO", bg="white",
              font=("comic sans ms", 9), relief="groove").grid(row=3, column=0, sticky="se")
        # ----------------------Entry academico------------------------------------
        Entry(frame, width=20, justify="center", textvariable=academico, bg="grey75",
              font=("comic sans ms", 9)).grid(row=3, column=1, sticky="sw")
        # ------------------labels frames------------------------------------------------------

        if combo.get() == "1°ESBA":
            try:
                for letra in treev.get_children():
                    treev.delete(letra)


                connexion = sqlite3.connect(nameBD.nomBD())
                cursor = connexion.cursor()
                cursor.execute(f"select * from primero_esba_uno where nombre = '{nombreAlumno.get().strip().upper()}'")
                stock1 = cursor.fetchall()

                cursor.execute(f"select * from primero_esba_dos where nombre = '{nombreAlumno.get().strip().upper()}'")
                stock2 = cursor.fetchall()

                cursor.execute(f"select * from primero_esba_tres where nombre = '{nombreAlumno.get().strip().upper()}'")
                stock3 = cursor.fetchall()

                cursor.execute(f"select * from primero_esba_junio where nombre = '{nombreAlumno.get().strip().upper()}'")
                stock4 = cursor.fetchall()

                cursor.execute(f"select * from primero_esba_septiembre where nombre = '{nombreAlumno.get().strip().upper()}'")
                stock5 = cursor.fetchall()

                lista = [
                    ("LENGUA ESPAÑOLA", stock1[0][3], stock2[0][3], stock3[0][3], stock4[0][3], stock5[0][3]),
                    ("MATEMÁTICAS", stock1[0][4], stock2[0][4], stock3[0][4], stock4[0][4], stock5[0][4]),
                    ("GEOGRAFÍA", stock1[0][5], stock2[0][5], stock3[0][5], stock4[0][5], stock5[0][5]),
                    ("CIENCIAS NATURALES", stock1[0][6], stock2[0][6], stock3[0][6], stock4[0][6], stock5[0][6]),
                    ("FRANCÉS", stock1[0][7], stock2[0][7], stock3[0][7], stock4[0][7], stock5[0][7]),
                    ("INGLÉS", stock1[0][8], stock2[0][8], stock3[0][8], stock4[0][8], stock5[0][8]),
                    ("RELIGIÓN", stock1[0][9], stock2[0][9], stock3[0][9], stock4[0][9], stock5[0][9]),
                    ("EXPRESIÓN PLÁSTICA", stock1[0][10], stock2[0][10], stock3[0][10], stock4[0][10], stock5[0][10]),
                    ("EDUCACIÓN FÍSICA", stock1[0][11], stock2[0][11], stock3[0][11], stock4[0][11], stock5[0][11]),
                    ("INFORMÁTICA", stock1[0][12], stock2[0][12], stock3[0][12], stock4[0][12], stock5[0][12])
                ]
                academico.set(stock1[0][2])

                i = 0
                try:
                    archivos1 = open("informe/notas.rtf", "w")
                    # archivos1 = open("notas.doc", "a")
                    archivos1.write("(NOMBRE DE LA INSTITUCION)\nJEFATURA DE ESTUDIOS\n")
                    archivos1.write(f"\nNombre y apellidos:  {stock1[0][1]}")
                    archivos1.write("\nCurso: 1°ESBA")
                    archivos1.write(f"\nAño académico: {stock1[0][2]}")
                    archivos1.write("\n\n                         INFORMACIÓN ACADÉMICA")

                    while i < len(lista):
                        j = i + 1
                        archivos1 = open("informe/notas.rtf", "a")
                        archivos1.write("\n\n" + str(j)+"._" + lista[i][0] + ":   " + str(lista[i][1]) + "    "
                                        + str(lista[i][2]) + "    " + str(lista[i][3]) + "    "
                                        + str(lista[i][4]) + "    " + str(lista[i][5]))
                        i += 1
                        archivos1.close()
                    archivos1 = open("informe/notas.rtf", "a")
                    archivos1.write(
                        "\n\n\nNOTA: la información se lee en este orden:\nMateria: 1°trimeste 2°trimestre 3°trimestre junio septiembre")
                    archivos1.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n                         EL JEFE DE ESTUDIOS")
                    archivos1.write(f"\n\n\n\n\n\n\n\n     Fecha y hora de la solicitud: {loguin.hora()}")
                    archivos1.close()
                except PermissionError:
                    for letra in treev.get_children():
                        treev.delete(letra)
                    lista = [
                        ("cierre le archivo word texto.rtf", "ERROR", "ERROR",
                         "ERROR", "ERROR", "ERROR")
                    ]
                    for (a, p, s, t, j, x) in lista:
                        treev.insert("", "end", values=(a, p, s, t, j, x))
                    academico.set("")



                treev.tag_configure("addrow", background = "white")
                treev.tag_configure("evenrow", background="grey75")

                for (a, p, s, t, j,x) in lista:
                    treev.insert("", "end", values = (a, p, s, t, j,x), tags = ("evenrow,"))

                connexion.close()

            except IndexError:
                for letra in treev.get_children():
                    treev.delete(letra)
                lista = [
                    ("ERROR revise el nombre y el curso", "ERROR", "ERROR",
                     "ERROR", "ERROR", "ERROR")
                ]
                for (a, p, s, t, j, x) in lista:
                    treev.insert("", "end", values=(a, p, s, t, j, x))
                academico.set("")







        elif combo.get() == "2°ESBA":

            try:
                for letra in treev.get_children():
                    treev.delete(letra)


                connexion = sqlite3.connect(nameBD.nomBD())
                cursor = connexion.cursor()
                cursor.execute(f"select * from segundo_esba_uno where nombre = '{nombreAlumno.get().strip().upper()}'")
                stock1 = cursor.fetchall()

                cursor.execute(f"select * from segundo_esba_dos where nombre = '{nombreAlumno.get().strip().upper()}'")
                stock2 = cursor.fetchall()

                cursor.execute(f"select * from segundo_esba_tres where nombre = '{nombreAlumno.get().strip().upper()}'")
                stock3 = cursor.fetchall()

                cursor.execute(f"select * from segundo_esba_junio where nombre = '{nombreAlumno.get().strip().upper()}'")
                stock4 = cursor.fetchall()

                cursor.execute(f"select * from segundo_esba_septiembre where nombre = '{nombreAlumno.get().strip().upper()}'")
                stock5 = cursor.fetchall()

                lista = [
                    ("LENGUA ESPAÑOLA", stock1[0][3], stock2[0][3], stock3[0][3], stock4[0][3], stock5[0][3]),
                    ("MATEMÁTICAS", stock1[0][4], stock2[0][4], stock3[0][4], stock4[0][4], stock5[0][4]),
                    ("GEOGRAFÍA", stock1[0][5], stock2[0][5], stock3[0][5], stock4[0][5], stock5[0][5]),
                    ("CIENCIAS NATURALES", stock1[0][6], stock2[0][6], stock3[0][6], stock4[0][6], stock5[0][6]),
                    ("FRANCÉS", stock1[0][7], stock2[0][7], stock3[0][7], stock4[0][7], stock5[0][7]),
                    ("INGLÉS", stock1[0][8], stock2[0][8], stock3[0][8], stock4[0][8], stock5[0][8]),
                    ("RELIGIÓN", stock1[0][9], stock2[0][9], stock3[0][9], stock4[0][9], stock5[0][9]),
                    ("EXPRESIÓN PLÁSTICA", stock1[0][10], stock2[0][10], stock3[0][10], stock4[0][10], stock5[0][10]),
                    ("EDUCACIÓN FÍSICA", stock1[0][11], stock2[0][11], stock3[0][11], stock4[0][11], stock5[0][11]),
                    ("INFORMÁTICA", stock1[0][12], stock2[0][12], stock3[0][12], stock4[0][12], stock5[0][12])
                ]
                academico.set(stock1[0][2])

                i = 0
                try:
                    archivos1 = open("informe/notas.rtf", "w")
                    # archivos1 = open("notas.doc", "a")
                    archivos1.write("(NOMBRE DE LA INSTITUCION)\nJEFATURA DE ESTUDIOS\n")
                    archivos1.write(f"\nNombre y apellidos:  {stock1[0][1]}")
                    archivos1.write("\nCurso: 2°ESBA")
                    archivos1.write(f"\nAño académico: {stock1[0][2]}")
                    archivos1.write("\n\n                         INFORMACIÓN ACADÉMICA")

                    while i < len(lista):
                        j = i + 1
                        archivos1 = open("informe/notas.rtf", "a")
                        archivos1.write("\n\n" +str(j) +"._" + lista[i][0] + ":   " + str(lista[i][1]) + "    "
                                        + str(lista[i][2]) + "    " + str(lista[i][3]) + "    "
                                        + str(lista[i][4]) + "    " + str(lista[i][5]))
                        i += 1
                        archivos1.close()
                    archivos1 = open("informe/notas.rtf", "a")
                    archivos1.write(
                        "\n\n\nNOTA: la información se lee en este orden:\nMateria: 1°trimeste 2°trimestre 3°trimestre junio septiembre")
                    archivos1.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n                         EL JEFE DE ESTUDIOS")
                    archivos1.write(f"\n\n\n\n\n\n     Fecha y hora de la solicitud: {loguin.hora()}")

                    archivos1.close()

                except PermissionError:
                    for letra in treev.get_children():
                        treev.delete(letra)
                    lista = [
                        ("cierre le archivo word texto.rtf", "ERROR", "ERROR",
                         "ERROR", "ERROR", "ERROR")
                    ]
                    for (a, p, s, t, j, x) in lista:
                        treev.insert("", "end", values=(a, p, s, t, j, x))
                    academico.set("")




                for (a, p, s, t, j,x) in lista:
                    treev.insert("", "end", values = (a, p, s, t, j,x))


                connexion.close()

            except IndexError:
                for letra in treev.get_children():
                    treev.delete(letra)
                lista = [
                    ("ERROR revise el nombre y el curso", "ERROR", "ERROR",
                     "ERROR", "ERROR", "ERROR")
                ]
                for (a, p, s, t, j, x) in lista:
                    treev.insert("", "end", values=(a, p, s, t, j, x))
                academico.set("")


        elif combo.get() == "3°ESBA":

            try:
                for letra in treev.get_children():
                    treev.delete(letra)

                connexion = sqlite3.connect(nameBD.nomBD())
                cursor = connexion.cursor()
                cursor.execute(f"select * from tercero_esba_uno where nombre = '{nombreAlumno.get().strip().upper()}'")
                stock1 = cursor.fetchall()

                cursor.execute(f"select * from tercero_esba_dos where nombre = '{nombreAlumno.get().strip().upper()}'")
                stock2 = cursor.fetchall()

                cursor.execute(f"select * from tercero_esba_tres where nombre = '{nombreAlumno.get().strip().upper()}'")
                stock3 = cursor.fetchall()

                cursor.execute(f"select * from tercero_esba_junio where nombre = '{nombreAlumno.get().strip().upper()}'")
                stock4 = cursor.fetchall()

                cursor.execute(f"select * from tercero_esba_septiembre where nombre = '{nombreAlumno.get().strip().upper()}'")
                stock5 = cursor.fetchall()

                lista = [
                    ("LENGUA ESPAÑOLA", stock1[0][3], stock2[0][3], stock3[0][3], stock4[0][3], stock5[0][3]),
                    ("MATEMÁTICAS", stock1[0][4], stock2[0][4], stock3[0][4], stock4[0][4], stock5[0][4]),
                    ("HISTORIA DE ÁFRICA Y GE", stock1[0][5], stock2[0][5], stock3[0][5], stock4[0][5], stock5[0][5]),
                    ("FÍSICA Y QUÍMICA", stock1[0][6], stock2[0][6], stock3[0][6], stock4[0][6], stock5[0][6]),
                    ("BIOLOGÍA Y GEOLOGÍA", stock1[0][7], stock2[0][7], stock3[0][7], stock4[0][7], stock5[0][7]),
                    ("TECNOLOGÍA", stock1[0][8], stock2[0][8], stock3[0][8], stock4[0][8], stock5[0][8]),
                    ("FRANCÉS", stock1[0][9], stock2[0][9], stock3[0][9], stock4[0][9], stock5[0][9]),
                    ("INGLÉS", stock1[0][10], stock2[0][10], stock3[0][10], stock4[0][10], stock5[0][10]),
                    ("RELIGIÓN", stock1[0][11], stock2[0][11], stock3[0][11], stock4[0][11], stock5[0][11]),
                    ("EXPRESIÓN PLÁSTICA", stock1[0][12], stock2[0][12], stock3[0][12], stock4[0][12], stock5[0][12]),
                    ("EDUCACIÓN FÍSICA", stock1[0][13], stock2[0][13], stock3[0][13], stock4[0][13], stock5[0][13]),
                    ("INFORMÁTICA", stock1[0][14], stock2[0][14], stock3[0][14], stock4[0][14], stock5[0][14])
                ]
                academico.set(stock1[0][2])

                i = 0
                try:
                    archivos1 = open("informe/notas.rtf", "w")
                    # archivos1 = open("notas.doc", "a")
                    archivos1.write("(NOMBRE DE LA INSTITUCION)\nJEFATURA DE ESTUDIOS\n")
                    archivos1.write(f"\nNombre y apellidos:  {stock1[0][1]}")
                    archivos1.write("\nCurso: 3°ESBA")
                    archivos1.write(f"\nAño académico: {stock1[0][2]}")
                    archivos1.write("\n\n                         INFORMACIÓN ACADÉMICA")

                    while i < len(lista):
                        j = i + 1
                        archivos1 = open("informe/notas.rtf", "a")
                        archivos1.write("\n\n"+ str(j)+ "._" + lista[i][0] + ":   " + str(lista[i][1]) + "    "
                                        + str(lista[i][2]) + "    " + str(lista[i][3]) + "    "
                                        + str(lista[i][4]) + "    " + str(lista[i][5]))
                        i += 1
                        archivos1.close()
                    archivos1 = open("informe/notas.rtf", "a")
                    archivos1.write(
                        "\n\n\nNOTA: la información se lee en este orden:\nMateria: 1°trimeste 2°trimestre 3°trimestre junio septiembre")
                    archivos1.write("\n\n\n\n\n\n\n\n\n\n                         EL JEFE DE ESTUDIOS")
                    archivos1.write(f"\n\n\n\n\n\n\n        Fecha y hora de la solicitud: {loguin.hora()}")

                    archivos1.close()
                except PermissionError:
                    for letra in treev.get_children():
                        treev.delete(letra)
                    lista = [
                        ("cierre le archivo word texto.rtf", "ERROR", "ERROR",
                         "ERROR", "ERROR", "ERROR")
                    ]
                    for (a, p, s, t, j, x) in lista:
                        treev.insert("", "end", values=(a, p, s, t, j, x))
                    academico.set("")



                for (a, p, s, t, j, x) in lista:
                    treev.insert("", "end", values=(a, p, s, t, j, x))

                connexion.close()

            except IndexError:
                for letra in treev.get_children():
                    treev.delete(letra)
                lista = [
                    ("ERROR revise el nombre y el curso", "ERROR", "ERROR",
                     "ERROR", "ERROR", "ERROR")
                ]
                for (a, p, s, t, j, x) in lista:
                    treev.insert("", "end", values=(a, p, s, t, j, x))
                academico.set("")



        elif combo.get() == "4°ESBA":
            try:
                for letra in treev.get_children():
                    treev.delete(letra)

                connexion = sqlite3.connect(nameBD.nomBD())
                cursor = connexion.cursor()
                cursor.execute(f"select * from cuarto_esba_uno where nombre = '{nombreAlumno.get().strip().upper()}'")
                stock1 = cursor.fetchall()

                cursor.execute(f"select * from cuarto_esba_dos where nombre = '{nombreAlumno.get().strip().upper()}'")
                stock2 = cursor.fetchall()

                cursor.execute(f"select * from cuarto_esba_tres where nombre = '{nombreAlumno.get().strip().upper()}'")
                stock3 = cursor.fetchall()

                cursor.execute(f"select * from cuarto_esba_junio where nombre = '{nombreAlumno.get().strip().upper()}'")
                stock4 = cursor.fetchall()

                cursor.execute(f"select * from cuarto_esba_septiembre where nombre = '{nombreAlumno.get().strip().upper()}'")
                stock5 = cursor.fetchall()

                lista = [
                    ("LENGUA ESPAÑOLA", stock1[0][3], stock2[0][3], stock3[0][3], stock4[0][3], stock5[0][3]),
                    ("MATEMÁTICAS", stock1[0][4], stock2[0][4], stock3[0][4], stock4[0][4], stock5[0][4]),
                    ("HISTORIA UNIVERSAL", stock1[0][5], stock2[0][5], stock3[0][5], stock4[0][5], stock5[0][5]),
                    ("FÍSICA Y QUÍMICA", stock1[0][6], stock2[0][6], stock3[0][6], stock4[0][6], stock5[0][6]),
                    ("BIOLOGÍA Y GEOLOGÍA", stock1[0][7], stock2[0][7], stock3[0][7], stock4[0][7], stock5[0][7]),
                    ("TECNOLOGÍA", stock1[0][8], stock2[0][8], stock3[0][8], stock4[0][8], stock5[0][8]),
                    ("FRANCÉS", stock1[0][9], stock2[0][9], stock3[0][9], stock4[0][9], stock5[0][9]),
                    ("INGLÉS", stock1[0][10], stock2[0][10], stock3[0][10], stock4[0][10], stock5[0][10]),
                    ("RELIGIÓN", stock1[0][11], stock2[0][11], stock3[0][11], stock4[0][11], stock5[0][11]),
                    ("EXPRESIÓN PLÁSTICA", stock1[0][12], stock2[0][12], stock3[0][12], stock4[0][12], stock5[0][12]),
                    ("EDUCACIÓN FÍSICA", stock1[0][13], stock2[0][13], stock3[0][13], stock4[0][13], stock5[0][13]),
                    ("INFORMÁTICA", stock1[0][14], stock2[0][14], stock3[0][14], stock4[0][14], stock5[0][14])
                ]
                academico.set(stock1[0][2])

                i = 0
                try:

                    archivos1 = open("informe/notas.rtf", "w")
                    # archivos1 = open("notas.doc", "a")
                    archivos1.write("(NOMBRE DE LA INSTITUCION)\nJEFATURA DE ESTUDIOS\n")
                    archivos1.write(f"\nNombre y apellidos:  {stock1[0][1]}")
                    archivos1.write("\nCurso: 4°ESBA")
                    archivos1.write(f"\nAño académico: {stock1[0][2]}")
                    archivos1.write("\n\n                         INFORMACIÓN ACADÉMICA")

                    while i < len(lista):
                        j = i + 1
                        archivos1 = open("informe/notas.rtf", "a")
                        archivos1.write("\n\n"+str(j) + "._" + lista[i][0] + ":   " + str(lista[i][1]) + "    "
                                        + str(lista[i][2]) + "    " + str(lista[i][3]) + "    "
                                        + str(lista[i][4]) + "    " + str(lista[i][5]))
                        i += 1
                        archivos1.close()
                    archivos1 = open("informe/notas.rtf", "a")
                    archivos1.write(
                        "\n\n\nNOTA: la información se lee en este orden:\nMateria: 1°trimeste 2°trimestre 3°trimestre junio septiembre")
                    archivos1.write("\n\n\n\n\n\n\n\n                         EL JEFE DE ESTUDIOS")
                    archivos1.write(f"\n\n\n\n\n\n\n\n\n          Fecha y hora de la solicitud: {loguin.hora()}")
                    archivos1.close()

                except PermissionError:
                    for letra in treev.get_children():
                        treev.delete(letra)
                    lista = [
                        ("cierre le archivo word texto.rft", "ERROR", "ERROR",
                         "ERROR", "ERROR", "ERROR")
                    ]
                    for (a, p, s, t, j, x) in lista:
                        treev.insert("", "end", values=(a, p, s, t, j, x))
                    academico.set("")


                for (a, p, s, t, j, x) in lista:
                    treev.insert("", "end", values=(a, p, s, t, j, x))

                connexion.close()

            except IndexError:
                for letra in treev.get_children():
                    treev.delete(letra)
                lista = [
                    ("ERROR revise el nombre y el curso", "ERROR", "ERROR",
                     "ERROR", "ERROR", "ERROR")
                ]
                for (a, p, s, t, j, x) in lista:
                    treev.insert("", "end", values=(a, p, s, t, j, x))
                academico.set("")


        elif combo.get() == "1°BACH":

            try:
                for letra in treev.get_children():
                    treev.delete(letra)

                connexion = sqlite3.connect(nameBD.nomBD())
                cursor = connexion.cursor()
                cursor.execute(f"select * from primero_bach_uno where nombre = '{nombreAlumno.get().strip().upper()}'")
                stock1 = cursor.fetchall()

                cursor.execute(f"select * from primero_bach_dos where nombre = '{nombreAlumno.get().strip().upper()}'")
                stock2 = cursor.fetchall()

                cursor.execute(f"select * from primero_bach_tres where nombre = '{nombreAlumno.get().strip().upper()}'")
                stock3 = cursor.fetchall()

                cursor.execute(f"select * from primero_bach_junio where nombre = '{nombreAlumno.get().strip().upper()}'")
                stock4 = cursor.fetchall()

                cursor.execute(f"select * from primero_bach_septiembre where nombre = '{nombreAlumno.get().strip().upper()}'")
                stock5 = cursor.fetchall()

                lista = [
                    ("LENGUA ESPAÑOLA", stock1[0][3], stock2[0][3], stock3[0][3], stock4[0][3], stock5[0][3]),
                    ("HISTORIA DE ÁFRICA Y GE", stock1[0][4], stock2[0][4], stock3[0][4], stock4[0][4], stock5[0][4]),
                    ("FILOSOFÍA", stock1[0][5], stock2[0][5], stock3[0][5], stock4[0][5], stock5[0][5]),
                    ("CIENCIAS DE LA TIERRA Y M.A", stock1[0][6], stock2[0][6], stock3[0][6], stock4[0][6], stock5[0][6]),
                    ("ECONOMÍA", stock1[0][7], stock2[0][7], stock3[0][7], stock4[0][7], stock5[0][7]),
                    ("RELIGIÓN", stock1[0][8], stock2[0][8], stock3[0][8], stock4[0][8], stock5[0][8]),
                    ("FRANCÉS", stock1[0][9], stock2[0][9], stock3[0][9], stock4[0][9], stock5[0][9]),
                    ("INGLÉS", stock1[0][10], stock2[0][10], stock3[0][10], stock4[0][10], stock5[0][10]),
                    ("EDUCACIÓN FÍSICA", stock1[0][20], stock2[0][20], stock3[0][20], stock4[0][20], stock5[0][20]),
                    ("INFORMÁTICA", stock1[0][21], stock2[0][21], stock3[0][21], stock4[0][21], stock5[0][21]),
                    ("", "", "", "", "", ""),
                    ("MATEMÁTICAS I", stock1[0][11], stock2[0][11], stock3[0][11], stock4[0][11], stock5[0][11]),
                    ("FÍSICA Y QUÍMICA", stock1[0][12], stock2[0][12], stock3[0][12], stock4[0][12], stock5[0][12]),
                    ("BIOLOGÍA", stock1[0][13], stock2[0][13], stock3[0][13], stock4[0][13], stock5[0][13]),
                    ("DIBUJO TÉCNICO I", stock1[0][19], stock2[0][19], stock3[0][19], stock4[0][19], stock5[0][19]),
                    ("", "", "","", "", ""),

                    ("TECNOLOGÍA INDUSTRIAL I", stock1[0][18], stock2[0][18], stock3[0][18], stock4[0][18], stock5[0][18]),
                    ("DIBUJO TÉCNICO I", stock1[0][19], stock2[0][19], stock3[0][19], stock4[0][19], stock5[0][19]),
                    ("", "", "","", "", ""),
                    ("MATEMÁTICAS APLICADAS", stock1[0][14], stock2[0][14], stock3[0][14], stock4[0][14], stock5[0][14]),
                    ("GEOGRAFÍA DE GRANDES ESPACIOS", stock1[0][15], stock2[0][15], stock3[0][15], stock4[0][15], stock5[0][15]),
                    ("LATÍN", stock1[0][16], stock2[0][16], stock3[0][16], stock4[0][16], stock5[0][16]),
                    ("GRIEGO", stock1[0][17], stock2[0][17], stock3[0][17], stock4[0][17], stock5[0][17])



                ]
                academico.set(stock1[0][2])

                i = 0
                try:

                    archivos1 = open("informe/notas.rft", "w")
                    # archivos1 = open("notas.doc", "a")
                    archivos1.write("(NOMBRE DE LA INSTITUCION)\nJEFATURA DE ESTUDIOS\n")
                    archivos1.write(f"\nNombre y apellidos:  {stock1[0][1]}")
                    archivos1.write("\nCurso: 1°BACH")
                    archivos1.write(f"\nAño académico: {stock1[0][2]}")
                    archivos1.write("\n\n                         INFORMACIÓN ACADÉMICA")

                    while i < len(lista):
                        archivos1 = open("informe/notas.rtf", "a")
                        archivos1.write("\n\n" + "-" + lista[i][0] + ":   " + str(lista[i][1]) + "    "
                                        + str(lista[i][2]) + "    " + str(lista[i][3]) + "    "
                                        + str(lista[i][4]) + "    " + str(lista[i][5]))
                        i += 1
                        archivos1.close()
                    archivos1 = open("informe/notas.rtf", "a")
                    archivos1.write(
                        "\n\n\nNOTA: la información se lee en este orden:\nMateria: 1°trimeste 2°trimestre 3°trimestre junio septiembre")
                    archivos1.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                                    "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n                         EL JEFE DE ESTUDIOS")
                    archivos1.write(f"\n\n\n\n\n\n\n\n          Fecha y hora de la solicitud: {loguin.hora()}")

                    archivos1.close()

                except PermissionError:
                    for letra in treev.get_children():
                        treev.delete(letra)
                    lista = [
                        ("cierre le archivo word texto.rtf", "ERROR", "ERROR",
                         "ERROR", "ERROR", "ERROR")
                    ]
                    for (a, p, s, t, j, x) in lista:
                        treev.insert("", "end", values=(a, p, s, t, j, x))
                    academico.set("")


                for (a, p, s, t, j, x) in lista:
                    treev.insert("", "end", values=(a, p, s, t, j, x))

                connexion.close()

            except IndexError:
                for letra in treev.get_children():
                    treev.delete(letra)
                lista = [
                    ("ERROR revise el nombre y el curso", "ERROR ", "ERROR",
                     "ERROR", "ERROR", "ERROR")
                ]
                for (a, p, s, t, j, x) in lista:
                    treev.insert("", "end", values=(a, p, s, t, j, x))
                academico.set("")


        elif combo.get() == "2°BACH":


            try:
                for letra in treev.get_children():
                    treev.delete(letra)

                connexion = sqlite3.connect(nameBD.nomBD())
                cursor = connexion.cursor()
                cursor.execute(f"select * from segundo_bach_uno where nombre = '{nombreAlumno.get().strip().upper()}'")
                stock1 = cursor.fetchall()

                cursor.execute(f"select * from segundo_bach_dos where nombre = '{nombreAlumno.get().strip().upper()}'")
                stock2 = cursor.fetchall()

                cursor.execute(f"select * from segundo_bach_tres where nombre = '{nombreAlumno.get().strip().upper()}'")
                stock3 = cursor.fetchall()

                cursor.execute(f"select * from segundo_bach_junio where nombre = '{nombreAlumno.get().strip().upper()}'")
                stock4 = cursor.fetchall()

                cursor.execute(f"select * from segundo_bach_septiembre where nombre = '{nombreAlumno.get().strip().upper()}'")
                stock5 = cursor.fetchall()

                lista = [
                    ("LENGUA Y LITERATURA", stock1[0][3], stock2[0][3], stock3[0][3], stock4[0][3], stock5[0][3]),
                    ("HISTORIA DEL MUNDO ACTUAL", stock1[0][4], stock2[0][4], stock3[0][4], stock4[0][4], stock5[0][4]),
                    ("HISTORIA DE LA FILOSOFÍA", stock1[0][5], stock2[0][5], stock3[0][5], stock4[0][5], stock5[0][5]),
                    ("CNS", stock1[0][6], stock2[0][6], stock3[0][6], stock4[0][6], stock5[0][6]),
                    ("ECONOMÍA", stock1[0][7], stock2[0][7], stock3[0][7], stock4[0][7], stock5[0][7]),
                    ("RELIGIÓN", stock1[0][8], stock2[0][8], stock3[0][8], stock4[0][8], stock5[0][8]),
                    ("FRANCÉS", stock1[0][9], stock2[0][9], stock3[0][9], stock4[0][9], stock5[0][9]),
                    ("INGLÉS", stock1[0][10], stock2[0][10], stock3[0][10], stock4[0][10], stock5[0][10]),
                    ("INFORMÁTICA", stock1[0][22], stock2[0][22], stock3[0][22], stock4[0][22], stock5[0][22]),
                    ("", "", "", "", "", ""),
                    ("MATEMÁTICAS II", stock1[0][11], stock2[0][11], stock3[0][11], stock4[0][11], stock5[0][11]),
                    ("QUÍMICA", stock1[0][12], stock2[0][12], stock3[0][12], stock4[0][12], stock5[0][12]),
                    ("GEOLOGÍA", stock1[0][13], stock2[0][13], stock3[0][13], stock4[0][13], stock5[0][13]),
                    ("ELECTROTECNIA", stock1[0][14], stock2[0][14], stock3[0][14], stock4[0][14], stock5[0][14]),
                    ("", "", "","", "", ""),

                    ("TECNOLOGÍA INDUSTRIAL II", stock1[0][19], stock2[0][19], stock3[0][19], stock4[0][19], stock5[0][19]),
                    ("DIBUJO TÉCNICO II", stock1[0][20], stock2[0][20], stock3[0][20], stock4[0][20], stock5[0][20]),
                    ("ELECTROTECNIA", stock1[0][14], stock2[0][14], stock3[0][14], stock4[0][14], stock5[0][14]),
                    ("", "", "",
                     "", "", ""),
                    ("MATEMÁTICAS APLICADAS", stock1[0][15], stock2[0][15], stock3[0][15], stock4[0][15], stock5[0][15]),
                    ("HISTORIA DEL ÁRTE", stock1[0][16], stock2[0][16], stock3[0][16], stock4[0][16], stock5[0][16]),
                    ("LATÍN", stock1[0][17], stock2[0][17], stock3[0][17], stock4[0][17], stock5[0][17]),
                    ("GRIEGO", stock1[0][18], stock2[0][18], stock3[0][18], stock4[0][18], stock5[0][18])



                ]
                academico.set(stock1[0][2])
                i = 0
                try:

                    archivos1 = open("informe/notas.rtf", "w")
                    #archivos1 = open("notas.doc", "a")
                    archivos1.write("(NOMBRE DE LA INSTITUCION)\nJEFATURA DE ESTUDIOS\n")
                    archivos1.write(f"\nNombre y apellidos:  {stock1[0][1]}")
                    archivos1.write("\nCurso: 2°BACH")
                    archivos1.write(f"\nAño académico: {stock1[0][2]}")
                    archivos1.write("\n\n                         INFORMACIÓN ACADÉMICA")

                    while i < len(lista):

                        archivos1 = open("informe/notas.rtf", "a")
                        archivos1.write("\n\n"+"-" +lista[i][0]+":   " +str(lista[i][1])+ "    "
                                        +str(lista[i][2])+ "    " +str(lista[i][3])+ "    "
                                        +str(lista[i][4])+  "    " +str(lista[i][5]))
                        i += 1
                        archivos1.close()
                    archivos1 = open("informe/notas.rtf", "a")
                    archivos1.write("\n\n\nNOTA: la información se lee en este orden:\nMateria: 1°trimeste 2°trimestre 3°trimestre junio septiembre")
                    archivos1.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                                    "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n                        EL JEFE DE ESTUDIOS")
                    archivos1.write(f"\n\n\n\n\n\n\n          Fecha y hora de la solicitud: {loguin.hora()}")

                    archivos1.close()


                    for (a, p, s, t, j, x) in lista:
                        treev.insert("", "end", values=(a, p, s, t, j, x))

                    connexion.close()
                except PermissionError:
                    for letra in treev.get_children():
                        treev.delete(letra)
                    lista = [
                        ("cierre le archivo word texto.rft", "ERROR", "ERROR",
                         "ERROR", "ERROR", "ERROR")
                    ]
                    for (a, p, s, t, j, x) in lista:
                        treev.insert("", "end", values=(a, p, s, t, j, x))
                    academico.set("")

            except IndexError:
                for letra in treev.get_children():
                    treev.delete(letra)
                lista = [
                    ("ERROR revise el nombre y el curso", "ERROR", "ERROR",
                     "ERROR", "ERROR", "ERROR")
                ]
                for (a, p, s, t, j, x) in lista:
                    treev.insert("", "end", values=(a, p, s, t, j, x))
                academico.set("")

        else:
            for letra in treev.get_children():
                treev.delete(letra)
            lista = [
                ("ERROR", "ERROR", "ERROR",
                 "ERROR", "ERROR", "ERROR")
            ]
            for (a, p, s, t, j, x) in lista:
                treev.insert("", "end", values=(a, p, s, t, j, x))
            academico.set("")









    root.mainloop()


