from tkinter.ttk import *
from tkinter import *

from tkinter import messagebox
import sqlite3
import interface  # este modulo contiene las ventanas dee los ultimos registros de la ventana registro y disciplina
import funciones  #este modulo contiene la funcion de mostrar la foto de un alumno
import ventanas_actualizacion # este contiene la ventana de actualizacion de los datos de un alumno
import ventana_actualizacioDisc # este modudlo contiene la ventana de actualizacion de informacion disciplinaria
from tkinter import filedialog # este modulo permite abrir un archivo en windows explorer
import archivos # este modulo contiene la funcion de corregir los errores de espacio introducido por el usuario
import datetime # este modulo permite extraer fecha y hora de la maquina
import nameBD
#from  tkinter import filedialog

def registro():
    raiz = Toplevel()

    raiz.title("DULA 1.0-REGISTRO DE ALUMNOS")
    raiz.resizable(0,0)
    raiz.config(bg="grey85")
    raiz.geometry("1080x580")

    logo = PhotoImage(file="images/logoTsei.png")
    labeLogo = Label(raiz, image=logo)
    labeLogo.pack(side="right", anchor="n")
    # -------------------labe de la raiz-----------------------
    tituloLabel = Label(raiz, text="REGISTRO DE ALUMNOS")
    tituloLabel.config(font=("jokerman", 14), bd=5, relief="groov", fg="black", bg="lemonchiffon2")
    tituloLabel.pack()

    # ---------imagen----------------------------



    raiz.iconbitmap("images/dula.ico")
    #---------entry raiz-------------------
    attencion = StringVar()

    entryAtt = Entry(raiz, width = 47, textvariable = attencion)

    entryAtt.place(x = 460, y = 520)
    entryAtt.config(bg="grey85", font=("comic sans ms", 11), fg="red", justify="center", state = "readonly")



    #-------------variables de los Entry de la ventana datos del alumno--------------------------
    textoNombre = StringVar()
    textoApellido = StringVar()
    textoResidencia = StringVar()
    textoCurso = StringVar()
    textoSalud = StringVar()
    textoDateN = StringVar()
    textoDateN.set("00/00/0000")
    textoTutor = StringVar()
    textoTelTutor = StringVar()
    textoEstado = StringVar()
    textoFoto = StringVar()
    opcionRadiobutton = IntVar()
    opcionRadiobuttonCurso = IntVar()
    textoAcademico = StringVar()
    textoFoto.set("images/logoTsei.png") # la foto por defecto en el Entry foto

    #----------frames-------------------------------------
    frameRoot = Frame(raiz, width = "300", height = "10")
    frameRoot.config(bg = "grey85")
    frameRoot.place(x = 3, y = 80)
    #--------------frame curso------------------------------------
    frame1 = Frame(raiz,width = "300", height = "50")
    frame1.config(bg = "grey85")
    frame1.place(x = 210, y = 320)
    #-----------------radio baton frame cursos--------------------------

    # --------------------combobox fechas------------------------------------------
    comboDia = Combobox(frameRoot, width=5, state="readonly")
    comboDia['values'] = ('01', '02', '03', '04', '05', '06', '07', '08', '09',
                          '10', '11', '12', '13', '14', '15', '16', '17', '18',
                          '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31')
    comboDia.current(0)
    comboDia.place(x=214, y=125)

    comboMes = Combobox(frameRoot, width=5, state="readonly")
    comboMes['values'] = ('01', '02', '03', '04', '05', '06', '07', '08', '09',
                          '10', '11', '12')
    comboMes.current(0)
    comboMes.place(x=295, y=125)

    comboYear = Combobox(frameRoot, width=5, state="readonly")
    comboYear['values'] = ('1990', '1991', '1992', '1993', '1994',
                           '1995', '1996', '1997', '1998', '1999',
                           '2000', '2001', '2002', '2003', '2004',
                           '2005', '2006', '2007', '2008', '2009',
                           '2010', '2011', '2012', '2013', '2014',
                           '2015', '2016', '2017', '2018', '2019',
                           '2020', '2021', '2022', '2023', '2024',
                           '2025', '2026', '2027', '2028', '2029',
                           '2030', '2031', '2032', '2033', '2034',
                           '2035', '2036', '2037', '2038', '2039',
                           '2040', '2041', '2042', '2043', '2044', '2045',
                           '2046', '2047', '2048', '2049', '2050',
                           '2051', '2052', '2053', '2054', '2055',
                           '2056', '2057', '2058', '2059', '2060',
                           '2061', '2062', '2063', '2064', '2065',
                           '2066', '2067', '2068', '2069', '2070', '2071', '2072', '2073',
                           '2074', '2075', '2076', '2077', '2078', '2079', '2080', '2081',
                           '2082', '2083', '2084', '2085', '2086', '2087', '2088', '2089',
                           '2090', '2091', '2092', '2093', '2094', '2095', '2096', '2097',
                           '2098', '2099', '2100', '2101', '2102', '2103', '2104', '2105',
                           '2106', '2107', '2108', '2109', '2110', '2111', '2112', '2113',
                           '2114', '2115', '2116', '2117', '2118', '2119', '2120', '2121',
                           '2122', '2123', '2124', '2125', '2126', '2127', '2128', '2129',
                           '2130', '2131', '2132', '2133', '2134', '2135', '2136', '2137', '2138', '2139')
    comboYear.current(10)
    comboYear.place(x=376, y=125)
    # -----------------radio baton frame cursos--------------------------
    """
    Radiobutton(frame1, text="Presc1", variable=opcionRadiobuttonCurso, value=1,
                font=("comic sans ms", 9), cursor="hand2").grid(row=0, column=0, padx=5, pady=3, sticky="wn")

    Radiobutton(frame1, text="Presc2", variable=opcionRadiobuttonCurso, value=2,
                font=("comic sans ms", 9), cursor="hand2").grid(row=0, column=1, padx=5, pady=3, sticky="wn")

    Radiobutton(frame1, text="1°Pep", variable=opcionRadiobuttonCurso, value=3,
                font=("comic sans ms", 9), cursor="hand2").grid(row=0, column=2, padx=5, pady=3, sticky="wn")

    Radiobutton(frame1, text="2°Pep", variable=opcionRadiobuttonCurso, value=4,
                font=("comic sans ms", 9), cursor="hand2").grid(row=0, column=3, padx=5, pady=3, sticky="wn")

    Radiobutton(frame1, text="3°Pep", variable=opcionRadiobuttonCurso, value=5,
                font=("comic sans ms", 9), cursor="hand2").grid(row=1, column=0, padx=5, pady=3, sticky="wn")

    Radiobutton(frame1, text="4°Pep", variable=opcionRadiobuttonCurso, value=6,
                font=("comic sans ms", 9), cursor="hand2").grid(row=1, column=1, padx=5, pady=3, sticky="wn")

    Radiobutton(frame1, text="5°Pep", variable=opcionRadiobuttonCurso, value=7,
                font=("comic sans ms", 9), cursor="hand2").grid(row=1, column=2, padx=5, pady=3, sticky="wn")

    Radiobutton(frame1, text="6°Pep", variable=opcionRadiobuttonCurso, value=8,
                font=("comic sans ms", 9), cursor="hand2").grid(row=1, column=3, padx=5, pady=3, sticky="wn")
    """
    Radiobutton(frame1, text="1°Esba", variable=opcionRadiobuttonCurso, value=9,
                font=("comic sans ms", 9), cursor="hand2").grid(row=2, column=0, padx=5, pady=3, sticky="wn")

    Radiobutton(frame1, text="2°Esba", variable=opcionRadiobuttonCurso, value=10,
                font=("comic sans ms", 9), cursor="hand2").grid(row=2, column=1, padx=5, pady=3, sticky="wn")

    Radiobutton(frame1, text="3°Esba", variable=opcionRadiobuttonCurso, value=11,
                font=("comic sans ms", 9), cursor="hand2").grid(row=2, column=2, padx=5, pady=3, sticky="wn")

    Radiobutton(frame1, text="4°Esba", variable=opcionRadiobuttonCurso, value=12,
                font=("comic sans ms", 9), cursor="hand2").grid(row=2, column=3, padx=5, pady=3, sticky="wn")

    Radiobutton(frame1, text="1°Bach", variable=opcionRadiobuttonCurso, value=13,
                font=("comic sans ms", 9), cursor="hand2").grid(row=3, column=0, padx=5, pady=3, sticky="wn")

    Radiobutton(frame1, text="2°Bach", variable=opcionRadiobuttonCurso, value=14,
                font=("comic sans ms", 9), cursor="hand2").grid(row=3, column=1, padx=5, pady=3, sticky="wn")





    #frameRoot.pack(side = "top", anchor = "w")
    #--------------funcion para seleccionar el curso---------------
    def cursoSelec():
        if opcionRadiobuttonCurso.get() == 1:
            return "Presc1"
        elif opcionRadiobuttonCurso.get() == 2:
            return "Presc2"
        elif opcionRadiobuttonCurso.get() == 3:
            return "1°Pep"
        elif opcionRadiobuttonCurso.get() == 4:
            return "2°Pep"
        elif opcionRadiobuttonCurso.get() == 5:
            return "3°Pep"
        elif opcionRadiobuttonCurso.get() == 6:
            return "4°Pep"
        elif opcionRadiobuttonCurso.get() == 7:
            return "5°Pep"
        elif opcionRadiobuttonCurso.get() == 8:
            return "6°Pep"
        elif opcionRadiobuttonCurso.get() == 9:
            return "1°Esba"
        elif opcionRadiobuttonCurso.get() == 10:
            return "2°Esba"
        elif opcionRadiobuttonCurso.get() == 11:
            return "3°Esba"
        elif opcionRadiobuttonCurso.get() == 12:
            return "4°Esba"
        elif opcionRadiobuttonCurso.get() == 13:
            return "1°Bach"
        elif opcionRadiobuttonCurso.get() == 14:
            return "2°Bach"
        else:
            return ""



    #--------------funciones de texto--------------------


    def MostrarText():
        try:

            #esta funcion permite registra la informacion personal de un nuevo a lumno

           if textoNombre.get() and textoApellido.get() and textoTutor.get():
                fichaAlumno = open("informe/inscripcion.doc", "w")


                textoAcademico = comboFecha.get()

                miConexion = sqlite3.connect(nameBD.nomBD())  # crear o abrir la conexion con al base de datos
                cursor = miConexion.cursor()

                nombreApellido = textoNombre.get().strip().upper()+" "+textoApellido.get().strip().upper()
                dateN = comboDia.get()+"/"+comboMes.get()+"/"+comboYear.get()
                generos = genero().upper()
                tutor = textoTutor.get().upper()
                telTutor = textoTelTutor.get().upper()
                curso = cursoSelec()
                residencia = textoResidencia.get().upper()
                salud = textoSalud.get().upper()
                imagen = textoFoto.get()
                estadoA = "MATRICULADO/A"

                avion = [
                    (nombreApellido, dateN, generos, curso, tutor, telTutor, residencia, salud, estadoA, imagen)
                ]

                # insercion de datos en la tabla
                cursor.executemany("insert into alumno values (null,?,?,?,?,?,?,?,?,?,?)", avion)
                miConexion.commit()  # validation de la insertion de datos

                if cursoSelec() == "1°Esba":
                    cursor.execute(f"select id from alumno where nombre_y_apellidos = '{nombreApellido}'")
                    stock = cursor.fetchall()
                    stock1 = stock[0][0]
                    cursor.execute(f"insert into primero_esba_uno values ('{stock1}', '{nombreApellido}', '{textoAcademico}',"
                                   f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    miConexion.commit()

                    cursor.execute(f"insert into primero_esba_dos values ('{stock1}', '{nombreApellido}', '{textoAcademico}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    miConexion.commit()

                    cursor.execute(
                        f"insert into primero_esba_tres values ('{stock1}', '{nombreApellido}', '{textoAcademico}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    miConexion.commit()

                    cursor.execute(
                        f"insert into primero_esba_junio values ('{stock1}', '{nombreApellido}', '{textoAcademico}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    miConexion.commit()

                    cursor.execute(
                        f"insert into primero_esba_septiembre values ('{stock1}', '{nombreApellido}', '{textoAcademico}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    miConexion.commit()

                elif cursoSelec() == "2°Esba":
                    cursor.execute(f"select id from alumno where nombre_y_apellidos = '{nombreApellido}'")
                    stock = cursor.fetchall()
                    stock1 = stock[0][0]
                    cursor.execute(f"insert into segundo_esba_uno values ('{stock1}', '{nombreApellido}', '{textoAcademico}',"
                                   f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    miConexion.commit()

                    cursor.execute(f"insert into segundo_esba_dos values ('{stock1}', '{nombreApellido}', '{textoAcademico}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    miConexion.commit()

                    cursor.execute(f"insert into segundo_esba_tres values ('{stock1}', '{nombreApellido}', '{textoAcademico}',"
                                   f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    miConexion.commit()

                    cursor.execute(f"insert into segundo_esba_junio values ('{stock1}', '{nombreApellido}', '{textoAcademico}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    miConexion.commit()

                    cursor.execute(f"insert into segundo_esba_septiembre values ('{stock1}', '{nombreApellido}', '{textoAcademico}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    miConexion.commit()

                elif cursoSelec() == "3°Esba":
                    cursor.execute(f"select id from alumno where nombre_y_apellidos = '{nombreApellido}'")
                    stock = cursor.fetchall()
                    stock1 = stock[0][0]
                    cursor.execute(f"insert into tercero_esba_uno values ('{stock1}', '{nombreApellido}', '{textoAcademico}',"
                                   f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    miConexion.commit()

                    cursor.execute(
                        f"insert into tercero_esba_dos values ('{stock1}', '{nombreApellido}', '{textoAcademico}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    miConexion.commit()

                    cursor.execute(
                        f"insert into tercero_esba_tres values ('{stock1}', '{nombreApellido}', '{textoAcademico}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    miConexion.commit()

                    cursor.execute(
                        f"insert into tercero_esba_junio values ('{stock1}', '{nombreApellido}', '{textoAcademico}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    miConexion.commit()

                    cursor.execute(
                        f"insert into tercero_esba_septiembre values ('{stock1}', '{nombreApellido}', '{textoAcademico}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    miConexion.commit()

                elif cursoSelec() == "4°Esba":
                    cursor.execute(f"select id from alumno where nombre_y_apellidos = '{nombreApellido}'")
                    stock = cursor.fetchall()
                    stock1 = stock[0][0]
                    cursor.execute(f"insert into cuarto_esba_uno values ('{stock1}', '{nombreApellido}', '{textoAcademico}',"
                                   f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    miConexion.commit()

                    cursor.execute(
                        f"insert into cuarto_esba_dos values ('{stock1}', '{nombreApellido}', '{textoAcademico}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    miConexion.commit()

                    cursor.execute(
                        f"insert into cuarto_esba_tres values ('{stock1}', '{nombreApellido}', '{textoAcademico}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    miConexion.commit()

                    cursor.execute(
                        f"insert into cuarto_esba_junio values ('{stock1}', '{nombreApellido}', '{textoAcademico}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    miConexion.commit()

                    cursor.execute(
                        f"insert into cuarto_esba_septiembre values ('{stock1}', '{nombreApellido}', '{textoAcademico}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    miConexion.commit()

                elif cursoSelec() == "1°Bach":
                    cursor.execute(f"select id from alumno where nombre_y_apellidos = '{nombreApellido}'")
                    stock = cursor.fetchall()
                    stock1 = stock[0][0]
                    cursor.execute(f"insert into primero_bach_uno values ('{stock1}', '{nombreApellido}', '{textoAcademico}',"
                                   f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    miConexion.commit()

                    cursor.execute(
                        f"insert into primero_bach_dos values ('{stock1}', '{nombreApellido}', '{textoAcademico}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    miConexion.commit()

                    cursor.execute(
                        f"insert into primero_bach_tres values ('{stock1}', '{nombreApellido}', '{textoAcademico}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    miConexion.commit()

                    cursor.execute(
                        f"insert into primero_bach_junio values ('{stock1}', '{nombreApellido}', '{textoAcademico}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    miConexion.commit()

                    cursor.execute(
                        f"insert into primero_bach_septiembre values ('{stock1}', '{nombreApellido}', '{textoAcademico}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    miConexion.commit()

                elif cursoSelec() == "2°Bach":
                    cursor.execute(f"select id from alumno where nombre_y_apellidos = '{nombreApellido}'")
                    stock = cursor.fetchall()
                    stock1 = stock[0][0]
                    cursor.execute(f"insert into segundo_bach_uno values ('{stock1}', '{nombreApellido}', '{textoAcademico}',"
                                   f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    miConexion.commit()

                    cursor.execute(
                        f"insert into segundo_bach_dos values ('{stock1}', '{nombreApellido}', '{textoAcademico}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    miConexion.commit()

                    cursor.execute(
                        f"insert into segundo_bach_tres values ('{stock1}', '{nombreApellido}', '{textoAcademico}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    miConexion.commit()

                    cursor.execute(
                        f"insert into segundo_bach_junio values ('{stock1}', '{nombreApellido}', '{textoAcademico}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    miConexion.commit()

                    cursor.execute(
                        f"insert into segundo_bach_septiembre values ('{stock1}', '{nombreApellido}', '{textoAcademico}',"
                        f"0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )")
                    miConexion.commit()

                else:
                    pass


                cursor.execute(f"select id from alumno where nombre_y_apellidos = '{nombreApellido}'")
                idAlum = cursor.fetchall()


                fichaAlumno.write("(NOMBRE DE LA INSTITUCION)\nSECRETARÍA\n\n                                 COMPROBANTE DE INSCRIPCIÓN")
                fichaAlumno.write(f"\n\nALUMNO/A: {nombreApellido}")
                fichaAlumno.write(f"\nID: {idAlum[0][0]}")
                fichaAlumno.write(f"\nCURSO MATRICULADO: {curso}")
                fichaAlumno.close()


    
                miConexion.close()  # cerrar la conexion con la base de datos



                #messagebox.showinfo('DULA', 'REGISTRADO CON ÉXITO')
                comboDia.current(0)
                comboMes.current(0)
                comboYear.current(10)

                textoNombre.set("")
                textoApellido.set("")
                textoCurso.set("")

                textoTutor.set("")
                textoTelTutor.set("")
                textoSalud.set("")
                textoResidencia.set("")
                cuadroFoto.config(font=("calibri", 14), state="normal")
                textoFoto.set("logoTsei.png")
                cuadroFoto.config(font=("calibri", 14), state="readonly")
                #textoAcademico.set("")
           else:

               messagebox.showerror("DULA", "INTRODUZCA PRIMERO LOS DATOS")
               textoNombre.set("")
               textoApellido.set("")
               textoCurso.set("")

               textoTutor.set("")
               textoTelTutor.set("")
               textoSalud.set("")
               textoResidencia.set("")
               cuadroFoto.config(font=("calibri", 14), state="normal")
               textoFoto.set("logoTsei.png")
               cuadroFoto.config(font=("calibri", 14), state="readonly")
               comboDia.current(0)
               comboMes.current(0)
               comboYear.current(10)
               #textoAcademico.set("")


               #messagebox.askyesnocancel("DULA", "ensayo")

        except PermissionError:
            attencion.set("Atención!!! procure cerrar el archivo word inscripcion.doc")



    def genero():
        if opcionRadiobutton.get() == 1:
            return "M"
        else:
            return "F"
    def estado():
        if textoEstado.get() == 1:
            return "matriculado/a"
        else:
            return "trasladado/a"




    #-----------Entry--------------------------

    cuadroNombre = Entry(frameRoot, textvariable = textoNombre, width = 30)
    cuadroNombre.config(font = ("calibri",14))
    cuadroNombre.grid(row = 2, column = 1, padx = 5, pady = 5, sticky = "w")

    cuadroApellido = Entry(frameRoot, textvariable = textoApellido, state = "normal", width = 30)
    cuadroApellido.config(font = ("calibri",14))
    cuadroApellido.grid(row = 3, column = 1, padx = 5, pady = 5, sticky = "w")

    cuadroDateN= Entry(frameRoot, textvariable = textoDateN, width = 10)
    cuadroDateN.config(font = ("calibri",14), fg ="red", )
    #cuadroDateN.grid(row = 4, column = 1, padx = 5, pady = 5, sticky = "wn")

    """
    cuadroCurso = Entry(frameRoot, textvariable = textoCurso,width = 30)
    cuadroCurso.config(font = ("calibri",14))
    cuadroCurso.grid(row = 7, column = 1, padx = 5, pady = 5, sticky = "w")
    """
    cuadroTutor = Entry(frameRoot, textvariable = textoTutor, width = 25)
    cuadroTutor.config(font = ("calibri",14))
    cuadroTutor.grid(row = 2, column = 3, padx = 5, pady = 5, sticky = "w")

    cuadroTelTutor = Entry(frameRoot, textvariable = textoTelTutor,width = 25)
    cuadroTelTutor.config(font = ("calibri",14))
    cuadroTelTutor.grid(row = 3, column = 3, padx = 5, pady = 5, sticky = "w")

    cuadroResidencia = Entry(frameRoot, textvariable=textoResidencia, width = 25)
    cuadroResidencia.config(font=("calibri", 14))
    cuadroResidencia.grid(row=4, column=3, padx=5, pady=5, sticky="wn")

    cuadroSalud = Entry(frameRoot, textvariable=textoSalud, width = 25)
    cuadroSalud.config(font=("calibri", 14))
    cuadroSalud.grid(row=5, column=3, padx=5, pady=5, sticky="wn")
    """

    cuadroFecha = Entry(frameRoot, textvariable=textoAcademico, width=30)
    cuadroFecha.config(font=("calibri", 14))
    cuadroFecha.grid(row=6, column=3, padx=5, pady=5, sticky="wn")
    """

    cuadroFoto = Entry(frameRoot, textvariable=textoFoto, width = 25)
    cuadroFoto.config(font=("calibri", 14), state = "readonly")
    cuadroFoto.grid(row=7, column=3, padx=5, pady=5, sticky="wn")

    # -------COMBOBOX----------------------------------------------

    comboFecha = Combobox(frameRoot, width = 25,state = "readonly")
    comboFecha['values'] = ('2010/2011', '2011/2012', '2012/2013',
                            '2013/2014', '2014/2015', '2015/2016',
                            '2016/2017', '2017/2018', '2018/2019',
                            '2019/2020','2020/2021', '2021/2022', '2022/2023',
                            '2023/2024', '2024/2025', '2025/2026',
                            '2026/2027', '2027/2028', '2028/2029',
                            '2029/2030', '2030/2031', '2031/2032',
                            '2032/2033', '2033/2034', '2034/2035', '2035/2036', '2036/2037',
                            '2037/2038', '2038/2039', '2039/2040', '2040/2041', '2041/2042',
                            '2042/2043', '2043/2044', '2044/2045', '2045/2046', '2046/2047',
                            '2047/2048', '2048/2049', '2049/2050', '2050/2051', '2051/2052', '2052/2053',
                            '2053/2054', '2054/2055', '2055/2056', '2056/2057', '2057/2058', '2058/2059',
                            '2059/2060', '2060/2061', '2061/2062', '2062/2063', '2063/2064', '2064/2065',
                            '2065/2066', '2066/2067', '2067/2068', '2068/2069', '2069/2070', '2070/2071',
                            '2071/2072', '2072/2073', '2073/2074', '2074/2075', '2075/2076', '2076/2077',
                            '2077/2078', '2078/2079', '2079/2080', '2080/2081', '2081/2082', '2082/2083',
                            '2083/2084', '2084/2085', '2085/2086', '2086/2087', '2087/2088', '2088/2089',
                            '2089/2090', '2090/2091', '2091/2092', '2092/2093', '2093/2094', '2094/2095',
                            '2095/2096', '2096/2097', '2097/2098', '2098/2099', '2099/2100', '2100/2101',
                            '2101/2102', '2102/2103', '2103/2104', '2104/2105', '2105/2106', '2106/2107',
                            '2107/2108', '2108/2109', '2109/2110', '2110/2111', '2111/2112', '2112/2113',
                            '2113/2114', '2114/2115', '2115/2116', '2116/2117', '2117/2118', '2118/2119', '2119/2120')
    comboFecha.grid(row=6, column=3, padx=5, pady=5, sticky="w" )
    comboFecha.current(0)


    #-----------RADIOBUTTON------------------------------------------
    Radiobutton(frameRoot, text = "MASCULINO", variable = opcionRadiobutton, value = 1, width = 15,
                font = ("calibry", 11), cursor = "hand2").grid(row = 5, column = 1, padx = 5, pady = 5, sticky = "wn")
    Radiobutton(frameRoot, text = "FEMENINO", variable = opcionRadiobutton, value = 2, width = 15,
                font = ("calibry", 11), cursor = "hand2",).grid(row = 5, column = 1, padx = 5, pady = 5, sticky = "ne")
    #----------check button---------------------
    """
    Checkbutton(frameRoot, text = "ESTADO DEL ALUMNO M/T", variable = textoEstado, onvalue = 1, offvalue = 0,
                command = estado(),
                cursor = "hand2", font = ("calibry", 11), relief = "groove").grid(row = 6, column = 2, columnspan = 2)
    """




    """"
    combo = Combobox(frameRoot)
    combo['values'] = ("1°ESBA", "2°ESBA", "3°ESBA", "4°ESBA", "1°BACH", "2°BACH")
    #combo.config(font = ("calibri", 14))
    combo.grid(row = 4, column = 1, padx = 5, pady = 5, sticky = "w")
    """
    #----------------------------------

    #------------label-----------------

    #----------el parametro sticky es para linear el texto del label (e, w, n, s)-------------
    espacioLabel = Label(frameRoot, text ="DATOS DEL ALUMNO/A")
    espacioLabel.config(font = ("monotype corsiva",14), relief="sunken", bd = 3, bg = "white")
    espacioLabel.grid(row = 1, column = 1, sticky = "w", padx = 5, pady = 5)

    espacioLabel1 = Label(frameRoot, text ="DATOS COMPLEMENTARIOS")
    espacioLabel1.config(font = ("monotype corsiva",14), relief="sunken", bd = 3, bg = "white")
    espacioLabel1.grid(row = 1, column = 3, sticky = "w", padx = 5, pady = 5)

    NombreLabel1 = Label(frameRoot, text = "NOMBRE:")
    NombreLabel1.config(font=("comic sans ms", 11), relief="sunken", bd = 3)
    NombreLabel1.grid(row = 2, column = 0, sticky = "ne", padx = 5, pady = 5)

    ApellidoLabel2 = Label(frameRoot, text = "APELLIDOS:")
    ApellidoLabel2.config(font=("comic sans ms", 11), relief="sunken", bd = 3)
    ApellidoLabel2.grid(row = 3, column = 0, sticky = "e", padx = 5, pady = 5)

    dateNLabel = Label(frameRoot, text = "FECHA DE NACIMIENTO:")
    dateNLabel.config(font=("comic sans ms", 11), relief="sunken", bd = 3)
    dateNLabel.grid(row = 4, column = 0, sticky = "ne", padx = 5, pady = 5 )
    Label(frameRoot, text = "/", font=("comic sans ms", 14), bg = "grey85").place(x = 270, y = 120)
    Label(frameRoot, text="/", font=("comic sans ms", 14), bg="grey85").place(x=350, y=120)


    generoLabel = Label(frameRoot, text = "GENERO:")
    generoLabel.config(font=("comic sans ms", 11), relief="sunken", bd = 3)
    generoLabel.grid(row = 5, column = 0, sticky = "ne", padx = 5, pady = 5, rowspan = 5)

    cursoLabel = Label(frameRoot, text = "CURSO:")
    cursoLabel.config(font=("comic sans ms", 11), relief="sunken", bd = 3)
    cursoLabel.grid(row = 7, column = 0, sticky = "e", padx = 5, pady = 5, rowspan = 5)

    tutorLabel = Label(frameRoot, text = "TUTOR/A:")
    tutorLabel.config(font=("comic sans ms", 11), relief="sunken", bd = 3)
    tutorLabel.grid(row = 2, column = 2, sticky = "ne", padx = 5, pady = 5,)

    TeltutorLabel = Label(frameRoot, text = "TUTOR/A N°TEL:")
    TeltutorLabel.config(font=("comic sans ms", 11), relief="sunken", bd = 3)
    TeltutorLabel.grid(row = 3, column = 2, sticky = "ne", padx = 5, pady = 5,)

    residenciaLabel = Label(frameRoot, text="RESIDENCIA:")
    residenciaLabel.config(font=("comic sans ms", 11), relief="sunken", bd=3)
    residenciaLabel.grid(row=4, column=2, sticky="ne", padx=5, pady=5, )

    patologiaLabel = Label(frameRoot, text="PATOLOGÍA GRAVE DE SALUD:")
    patologiaLabel.config(font=("comic sans ms", 11), relief="sunken", bd=3)
    patologiaLabel.grid(row=5, column=2, sticky="en", padx=5, pady=5, )

    fechaLabel = Label(frameRoot, text="AÑO ACADÉMICO:")
    fechaLabel.config(font=("comic sans ms", 11), relief="sunken", bd=3)
    fechaLabel.grid(row=6, column=2, sticky="en", padx=5, pady=5, )
    #tituloLabel.grid(row = 0, column = 2, sticky = "n")


    #---------------------------------------------------

    #--------------WIDGETS TEXT-------------------------

    """
    cuadroSalud = Text(frameRoot, width = "50", height = "5",)
    cuadroSalud.config(font = ("calibri", 12), fg = "black",)
    cuadroSalud.grid(row = 5, column = 3, padx = 5, pady = 5, sticky = "e")
    
    #----------scrollbar---------------
    scrollVerticalComen = Scrollbar(frameRoot, command = cuadroSalud.yview)
    scrollVerticalComen.grid(row = 5, column = 4, sticky = "wns",)
    cuadroSalud.config(yscrollcommand = scrollVerticalComen.set)
    """
    #-------------BOTONES---------------------------

    registrarBotton = Button(raiz, text = "Registrar",  activebackground="#F50743",command = lambda:MostrarText())
    registrarBotton.config(curso = "hand2", padx = 5, pady = 10, bd = 3, bg = "grey75",
                           font = ("comic sans ms", 9),)
    registrarBotton.place(x = 400, y = 450)

    UltimoregistroBotton = Button(raiz, text="Último registro",
                                  activebackground="#F50743",command=lambda: interface.UltimoRegistro())
    UltimoregistroBotton.config(curso="hand2", padx=5, pady=10, bd=3, bg="grey75",
                           font=("comic sans ms", 9), )
    UltimoregistroBotton.place(x=500, y=450)

    ActualizarDatosAlumBotton = Button(raiz, text="Actualizar datos",
                                  activebackground="#F50743", command = lambda:ventanas_actualizacion.actualizarDatosAum())
    ActualizarDatosAlumBotton.config(curso="hand2", padx=5, pady=10, bd=3, bg="grey75",
                                font=("comic sans ms", 9), )
    ActualizarDatosAlumBotton.place(x=635, y=450)

    buscarInfoBotton = Button(raiz, text="Buscar Alumno/a",
                                       activebackground="#F50743",
                                       command=lambda: consultasAca())
    buscarInfoBotton.config(curso="hand2", padx=5, pady=10, bd=3, bg="grey75",
                                     font=("comic sans ms", 9), )
    buscarInfoBotton.place(x=775, y=450)

    carnet = PhotoImage(file = "images/foto.png")
    IntroFotoBoton = Button(frameRoot, compound = "left" ,image = carnet,text = "foto".upper(), command = lambda:abrir())
    IntroFotoBoton.config(curso="hand2", bd=3, font=("comic sans ms", 9), bg = "white")
    IntroFotoBoton.grid(row = 7, column = 2,padx = 5, pady = 5,  sticky="en")

    botonCerrarV = Button(raiz, text="cerrar la ventana",
                          command=raiz.destroy, activebackground="#F50743")
    botonCerrarV.config(font=("comic sans ms", 10), bg="salmon3", cursor="hand2")
    botonCerrarV.pack(side = "left", anchor = "s")

    # ----------funcion para buscar imagen---------------------
    def abrir():

        archivo = filedialog.askopenfilename(title="SELECCIONAR FOTO")
        if archivo:
            cuadroFoto.config(font=("calibri", 14), state="normal")
            textoFoto.set(archivo)
            cuadroFoto.config(font=("calibri", 14), state="readonly")

        else:
            cuadroFoto.config(font=("calibri", 14), state="normal")
            textoFoto.set("images/logoTsei.png")
            cuadroFoto.config(font=("calibri", 14), state="readonly")




    raiz.mainloop()


#---------------SEGUNADA VENTANA FUNCION CONSULTAS ACADEMICAS-----------------------------------------------

def consultasAca():
    ventanaConsultas = Toplevel()
    #------INFORMACION DE LA RAIZ-------------------------------------------
    ventanaConsultas.title("DULA-INFO DEL ALUMNO")
    ventanaConsultas.geometry("1060x590")
    ventanaConsultas.resizable(1,0)
    ventanaConsultas.config(bg="grey85")
    #-------------imagenes de la raiz---------------------------------------------

    ventanaConsultas.iconbitmap("images/dula.ico")

    logo = PhotoImage(file="images/logoTsei.png")
    labeLogo = Label(ventanaConsultas, image=logo)
    labeLogo.pack(side="right", anchor="n")
    #--------------------variables de cuadros de busqueda---------------------
    textoBusqueda = StringVar()
    buscar = StringVar()
    valorRadioboton = IntVar()

    #---------label raiz ------------------------------------
    tituloLabel = Label(ventanaConsultas, text="DATOS DEL ALUMNO/A")
    tituloLabel.config(font=("jokerman", 14), bd=5, relief="groov", fg="black", bg="lemonchiffon2")
    tituloLabel.pack()
    #--------------botones de la raiz----------------------------------------------
    botonCerrarV = Button(ventanaConsultas, text = "cerrar la ventana",
                          command = ventanaConsultas.destroy, activebackground="#F50743")
    botonCerrarV.config(font=("comic sans ms", 10), bg = "salmon3", cursor = "hand2" )
    botonCerrarV.pack(side = "left", anchor = "s")

    #------------------------frames de la raiz-------------------------------------------

    frame1 = Frame(ventanaConsultas, width = "100", height = "100")
    frame1.config(bg = "grey85")
    frame1.place(x = 0, y = 80 )

    frame2 = Frame(ventanaConsultas, width="100", height="100")
    frame2.config(bg="grey85")
    frame2.place(x=500, y=80)

    frame3 = Frame(ventanaConsultas, width="100", height="100")
    frame3.config(bg="grey85")
    frame3.place(x=385, y=270)

    #-------------imagenes importados funciones--------------------
    """
    fotoCarnet = PhotoImage(file = "holl.png")
    label1F3 = Label(frame3, image= fotoCarnet)
    label1F3.pack()
    """
    #------------------label frame1--------------------------------------------------
    label1F1 = Label(frame1, text = "SELECIONA LA OPCIÓN DE BÚSQUEDA")
    label1F1.config(bd=5 , font=("comic sans ms", 12), relief="sunken")
    label1F1.grid(row = 0, column = 0, padx = 5, pady = 5, columnspan = 2)

    """
    label2F1 = Label(frame1, text="nombre completo\n del alumno/a")
    label2F1.config(bd=5 , font=("comic sans ms", 12), relief="sunken",)
    label2F1.grid(row=1, column=0, padx=5, pady=5)
    """
    label3F1 = Label(frame1, text="Introdúzca aqui:")
    label3F1.config(bd=5, font=("comic sans ms", 11), relief="sunken", )
    label3F1.grid(row=3, column=0, padx=5, pady=5)
    #------------------label frame2-------------------------------------------------------
    label1F2 = Label(frame2, text = "cuadro de información")
    label1F2.config(font=("comic sans ms", 12), relief="sunken", bd=5)
    label1F2.grid(row=0, column=0, padx=5, pady=5, sticky = "wn")
    #---------------label frame3--------------------------------------------


    #------------entry frame1----------------------
    """
    entry1 = Entry(frame1, textvariable = textoBusqueda)
    entry1.config(font = ("comic sans ms",11), width = 30)
    entry1.grid(row=1, column=1, padx=5, pady=5, sticky = "e")
    """
    entry2 = Entry(frame1, textvariable= buscar)
    entry2.config(font=("comic sans ms", 11), width=30)
    entry2.grid(row=3, column=1, padx=5, pady=5, sticky="e")
    #------------- cuadro de texto frame---------------------------
    textoInfo = Text(frame2, width = 60, height=24)
    textoInfo.config(bg = "grey85", font=("comic sans ms", 10))
    textoInfo.grid(row=1, column=0, padx=5, pady=5)

    # ----------scrollbar---------------
    scrollVertical = Scrollbar(frame2, command=textoInfo.yview)
    scrollVertical.grid(row=1, column=1, sticky="wns", )
    textoInfo.config(yscrollcommand=scrollVertical.set)

    # -----------RADIOBUTTON------------------------------------------
    Radiobutton(frame1, text="nombre completo", variable=valorRadioboton, value=1, bg = "lightgreen",
                font=("comic sans ms", 11), cursor="hand2").grid(row=1, column=1, padx=5, pady=5, sticky="w")
    Radiobutton(frame1, text="ID", variable=valorRadioboton, value=2, bg = "lightblue",
                font=("comic sans ms", 11), cursor="hand2", ).grid(row=1, column=1, padx=5, pady=5, sticky="e")


    #---------------botones frame1--------------
    """
    botonBusar1 = Button(frame1, text = "Buscar con el nombre", activebackground="#F50743", command = lambda:escritura())
    botonBusar1.grid(row=2, column=0, padx=5, pady=5, columnspan = 2 )
    botonBusar1.config(font=("comic sans ms", 10), bg = "grey75", cursor = "hand2")
    """
    botonBusar2 = Button(frame1, text="Buscar", activebackground="#F50743", command=lambda: buscarNomId())
    botonBusar2.grid(row=4, column=0, padx=5, pady=5, columnspan=2)
    botonBusar2.config(font=("comic sans ms", 10), bg="grey75", cursor="hand2")

    Button(frame3, text = "Ver Cumpleaños", activebackground="#F50743", command = lambda:aniversa(),
           font =("comic sans ms", 10), bg="grey75", cursor="hand2").grid(row=0, column=0, padx=5, pady=5, )

    Button(frame3, text="Borrar", activebackground="#F50743", command = lambda:borrarCaja(),
           font=("comic sans ms", 10), bg="grey75", cursor="hand2").grid(row=1, column=0, padx=5, pady=5, )
#-----------FUNCIONES DE BUSCAR---------------------------


    #funcion de busqueda con el nombre completo y escriture en la caja de texto
    def buscarNomId():
        """
        esta funcion permite buscar la informacion de un alumno con el nombre completo, o con el ID
        :return:
        """

        def imagen(s):
            """
            esta funcion es la que permite mostrar un imagen dentro de la caja de texto
            :param s: el parametro es la informacion de la base de datos que contiene la direccion de la imagen
            :return:
            """
            global foto
            foto = PhotoImage(file=f"{s}")
            textoInfo.image_create(1.0, image=foto)
            textoInfo.insert(END, "\n\n")


        if valorRadioboton.get() == 1:

                miConexion = sqlite3.connect(nameBD.nomBD())
                cursor = miConexion.cursor()
                cursor.execute("select * from alumno ")
                cajaRecepcion = cursor.fetchall()
                textoInfo.config(state='normal')
                textoInfo.delete(1.0, "end")


                i = 0
                while i < len(cajaRecepcion):

                    if i == len(cajaRecepcion) + 1:
                        pass
                        break

                    inforegistro = cajaRecepcion[i]
                    j = i + 1
                    i += 1


                    if buscar.get() =="":
                        textoInfo.delete(1.0, "end")
                        textoInfo.config(fg = "red")
                        textoInfo.insert(1.0, "Error!!!! el campo de búsqueda esta vacío,\nIntroduzca un nombre completo")
                        break

                    if buscar.get().strip().upper() == inforegistro[1].upper():
                        """
                        textoInfo.delete(1.0, "end")
                        fotoCarnet = PhotoImage(file="logo2.png")
                        textoInfo.image_create(2, image=fotoCarnet)
                        textoInfo.config(fg = "black")
                        """
                        imagen(inforegistro[10])

                        if inforegistro[3].upper() == "M":

                            textoInfo.config(fg="black")
                            textoInfo.insert(END, "ALUMNO: " + inforegistro[1].upper()
                                             + "\nFECHA DE NACIMIENTO: "
                                             + inforegistro[2] + "\nSEXO: " + inforegistro[3].upper()
                                             + "\nCURSO: " + inforegistro[4].upper() + "\nTUTOR/A: "
                                             + inforegistro[5].upper()
                                             + "\nN°TEL TUTOR/A: " + inforegistro[6].upper() +
                                             "\nDIRECCIÓN: " + inforegistro[7].upper() +
                                             "\nPATOLOGÍA GRAVE DE SALUD: "+ inforegistro[8].upper() +
                                             "\nESTADO DEL ALUMNO/A: " + inforegistro[9].upper() +
                                             "\nID: "+ str(inforegistro[0]) +
                                             "\nN° DE REGISTRO: " +str(j) + "/"+ str(len(cajaRecepcion))+"\n\n")


                            break

                        else:
                            textoInfo.config(fg="black")
                            textoInfo.insert(END, "ALUMNA: " + inforegistro[1].upper()
                                             + "\nFECHA DE NACIMIENTO: "
                                             + inforegistro[2] + "\nSEXO: " + inforegistro[3].upper()
                                             + "\nCURSO: " + inforegistro[4].upper() + "\nTUTOR/A: "
                                             + inforegistro[5].upper()
                                             + "\nN°TEL TUTOR/A: " + inforegistro[6].upper() +
                                             "\nDIRECCIÓN: " + inforegistro[7].upper() +
                                             "\nPATOLOGÍA GRAVE DE SALUD: " + inforegistro[8].upper() +
                                             "\nESTADO DEL ALUMNO/A: " + inforegistro[9].upper() +
                                             "\nID: " + str(inforegistro[0]) +
                                             "\nN° DE REGISTRO: " + str(j) + "/" + str(len(cajaRecepcion)) + "\n\n")

                            break

                    if i == len(cajaRecepcion) :
                        textoInfo.delete(1.0, "end")
                        textoInfo.config(fg="red")
                        textoInfo.insert(1.0, "El nombre no exite en la base de datos\nrevíselo porfavor!")
                        break

                miConexion.close()
                textoInfo.config(state='disabled')

        if valorRadioboton.get() == 2:
            #------------funcion de escritura id--------------------------------

            miConexion = sqlite3.connect(nameBD.nomBD())
            cursor = miConexion.cursor()
            cursor.execute("select * from alumno ")
            cajaRecepcion = cursor.fetchall()
            textoInfo.config(state='normal')
            textoInfo.delete(1.0, "end")


            i = 0
            while i < len(cajaRecepcion):

                if i == len(cajaRecepcion) + 1:
                    pass
                    break

                inforegistro = cajaRecepcion[i]
                j = i +1
                i += 1



                if  buscar.get() =="":
                    textoInfo.delete(1.0, "end")
                    textoInfo.config(fg = "red")
                    textoInfo.insert(1.0, "Error!!!! el campo de búsqueda esta vacío,\nIntroduzca un ID válido")
                    break

                try:
                    if int(buscar.get()) == inforegistro[0]:
                        imagen(inforegistro[10])
                        if inforegistro[3].upper() == "M":

                            textoInfo.config(fg="black")
                            textoInfo.insert(END, "ALUMNO: " + inforegistro[1].upper()
                                             + "\nFECHA DE NACIMIENTO: "
                                             + inforegistro[2] + "\nSEXO: " + inforegistro[3].upper()
                                             + "\nCURSO: " + inforegistro[4].upper() + "\nTUTOR/A: "
                                             + inforegistro[5].upper()
                                             + "\nN°TEL TUTOR/A: " + inforegistro[6].upper() +
                                             "\nDIRECCIÓN: " + inforegistro[7].upper() +
                                             "\nPATOLOGÍA GRAVE DE SALUD: "+ inforegistro[8].upper() +
                                             "\nESTADO DEL ALUMNO/A: " + inforegistro[9].upper() +
                                             "\nID: "+ str(inforegistro[0]) +
                                             "\nN° DE REGISTRO: " +str(j) + "/"+ str(len(cajaRecepcion))+"\n\n")


                            break

                        else:
                            textoInfo.config(fg="black")
                            textoInfo.insert(END, "ALUMNA: " + inforegistro[1].upper()
                                             + "\nFECHA DE NACIMIENTO: "
                                             + inforegistro[2] + "\nSEXO: " + inforegistro[3].upper()
                                             + "\nCURSO: " + inforegistro[4].upper() + "\nTUTOR/A: "
                                             + inforegistro[5].upper()
                                             + "\nN°TEL TUTOR/A: " + inforegistro[6].upper() +
                                             "\nDIRECCIÓN: " + inforegistro[7].upper() +
                                             "\nPATOLOGÍA GRAVE DE SALUD: " + inforegistro[8].upper() +
                                             "\nESTADO DEL ALUMNO/A: " + inforegistro[9].upper() +
                                             "\nID: " + str(inforegistro[0]) +
                                             "\nN° DE REGISTRO: " + str(j) + "/" + str(len(cajaRecepcion)) + "\n\n")

                            break



                    if i == len(cajaRecepcion) :
                        textoInfo.delete(1.0, "end")
                        textoInfo.config(fg="red")
                        textoInfo.insert(1.0, "El ID no exite en la base de datos\nrevíselo porfavor!")
                        break
                except ValueError:
                    textoInfo.config(fg="red")
                    textoInfo.insert(1.0, "\nError!!!! ID INCORRECTO ")



            miConexion.close()

            textoInfo.config(state='disabled')
        else:
            pass


    #-------------funciones de aniversarios y de borrar el Text-------------------------

    def borrarCaja():
        textoInfo.config(state='normal')
        textoInfo.delete(1.0, "end")
        textoInfo.config(state='disabled')


    def aniversa():
        """
        esta funcion permite ver los cumpleanos de los alumnos
        :return:
        """

        textoInfo.config(state='normal', fg = "black")
        textoInfo.delete(1.0, "end")
        textoInfo.insert(1.0,"                EN NOMBRE DEL DIRECTOR \n\n       "
                             "      (NOMBRE DE LA INSTICIÓN EDUCATIVA)")
        textoInfo.insert(END,"\n              LE DESEA FELIZ CUMPLEAÑOS A :\n")

        connexion = sqlite3.connect(nameBD.nomBD())
        cursor = connexion.cursor()
        cursor.execute("select * from alumno ")
        box = cursor.fetchall()



        i = 0


        while i < len(box):
                box1 = box[i][2]

                if i == len(box) + 1:
                    pass
                    break

                fechaHora = datetime.datetime.now()
                stock1 = fechaHora.strftime('%d/%m/%Y ')
                if stock1[0:5] == box1[0:5]:

                    #print(lista)

                    textoInfo.insert(END,"\n\n" + "- " + box[i][1]+"\n  DEL CURSO: "+box[i][4])
                    #textoInfo.config(fg="green")
                i += 1

        textoInfo.insert(END,"\n\n                      FELIZ JORNADA")

        connexion.close()
        textoInfo.config(state='disabled')





    ventanaConsultas.mainloop()

    """
               else:

                   textoInfo.delete(1.0, "end")
                   textoInfo.config(fg="red")
                   textoInfo.insert(1.0, "error!!!! el nombre exite en la base de datos\nreviselo")
               """


#-------------TERECERA VENTA FUNCION DE DISCIPLINA-------------------------------------------------------
def diciplina():

    root = Toplevel()

    root.title("DULA 1.0-CONSULTA DE DISCIPLINA")
    root.geometry("800x580")
    root.config(bg = "grey85")
    root.resizable(0,0)
    #-------------imagenes de la raiz---------------------------------------------

    root.iconbitmap("images/dula.ico")



    #-------------label de la raiz------------------------------------------------------------------

    tituloLabel = Label(root, text="CONSULTAS DISCIPLINARIAS")
    tituloLabel.config(font=("jokerman", 14), bd=5, relief="groov", fg="black", bg="lemonchiffon2")
    tituloLabel.pack()
    """
    labelCuleur = Label(root, width = 11, height = 26)
    labelCuleur.config(bg = "papaya whip", )
    labelCuleur.place(x = 420, y = 80)
    
    """
    #----------------frames root--------------------------------------------------
    frame = Frame(root, width=10000, height = 400)
    frame.pack(pady = 20)

    # -------------Notbook----------------------------------------------------------

    notebook = Notebook(frame, width=700, height=450)
    notebook.config()
    notebook.grid(row=0, column=0)

    #---------------------frame2  busqueda-------------------------------------------------------
    frame2Busc = Frame(root, width=100, height=100)
    frame2Busc.config(bg="grey85")

    notebook.add(frame2Busc, text="CONSULTA DISCIPLINARIA")

    # ----------frame1 registrar aqui--------------------------------------------------------------
    frame1Regis = Frame(notebook, width=100, height=100)
    frame1Regis.config(bg="grey85")

    notebook.add(frame1Regis, text="REGISTRO")
    #--------------------------VARIABLES--------------------------------------------
    textoNombre = StringVar()
    textoCurso = StringVar()
    textoFaltas = StringVar()


    #---------------logo tesi----------------------------------------
    logo = PhotoImage(file="images/logoTsei.png")
    labeLogo = Label(root, image=logo)
    labeLogo.place(x=640, y=0)
    #-------------labes frame1----------------------------------------------------------------

    label1F1 = Label(frame1Regis, text = "Registrar aqui:")
    label1F1.config(font=("comic sans ms", 10), bd = 5, relief = "groove", bg = "antique white")
    label1F1.grid(row = 0, column = 0, padx = 5, pady = 5, columnspan = 3 )

    label2F1 = Label(frame1Regis, text = "Nombre completo\ndel alumno/a:")
    label2F1.config(bg = "white", font=("comic sans ms", 10), relief = "groove")
    label2F1.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "w")

    """
    label3F1 = Label(frame1Regis, text = "N° de la falta de diciplina:")
    label3F1.config( bg = "white", font=("comic sans ms", 10), relief = "groove")
    label3F1.grid(row = 5, column = 0, padx = 5, pady = 5,  sticky = "w")
    """
    label3F1 = Label(frame1Regis, text = "Descripción de la falta:")
    label3F1.config(bg = "white", font=("comic sans ms", 10), relief = "groove")
    label3F1.grid(row = 7, column = 0, padx = 5, pady = 5,  sticky = "w")

    #------------Entry frame1------------------------------------------------
    entryNombreApell = Entry(frame1Regis, width = 35, textvariable = textoNombre)
    entryNombreApell.config(font=("comic sans ms", 10), justify = "center")
    entryNombreApell.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "e")

    #--------------frame1----------------------------------------------------------
    textDescrip = Text(frame1Regis, width = 50, height = 15)
    textDescrip.config(font=("comic sans ms", 10))
    textDescrip.grid(row = 8, column = 0, padx = 5, pady = 5)



    #---------------boton frame1 registrar------------------------------------------
    botonRegistro = Button(frame1Regis, text = "Registrar", activebackground="#F50743",
                           command = lambda: registroDis())
    botonRegistro.grid(row=9, column=0, padx=5, pady=5,  sticky = "w")
    botonRegistro.config(font=("comic sans ms", 10), bg = "grey75", cursor = "hand2")

    botonVerRegistro = Button(frame1Regis, text = "último registro", activebackground="#F50743",
                              command = lambda:interface.UltimoRegistro1())
    botonVerRegistro.grid(row=9, column=0, padx=5, pady=5,)
    botonVerRegistro.config(font=("comic sans ms", 10), bg = "grey75", cursor = "hand2")


    #-------------label frame2---------------------------------------------------------
    label1F2 = Label(frame2Busc, text = "Buscar aqui:" )
    label1F2.config(font = ("comic sans ms", 10), bd = 5, relief = "groove", bg = "antique white")
    label1F2.grid(row = 0, column = 0, padx=5, pady=5)

    label2F2 = Label(frame2Busc, text="Nombre y Apellidos del alumno/a:")
    label2F2.config( bg="white", font=("comic sans ms", 10), relief = "groove")
    label2F2.grid(row=1, column=0, padx=5, pady=5, sticky = "w")
    #----------------Entry frame2-----------------------------------------------
    entryNombreApellFrame2 = Entry(frame2Busc, width = 40)
    entryNombreApellFrame2.config(font=("comic sans ms", 10))
    entryNombreApellFrame2.grid(row=1, column=0, padx=5, pady=5, sticky = "e")
    #-------Text frame2---------------------------------------------------------
    textInfo = Text(frame2Busc, width = 59, height = 16)
    textInfo.config(font = ("comic sans ms", 11), bg = "grey75")
    textInfo.grid(row=3, column=0, padx=5, pady=5)

    scrollVertical = Scrollbar(frame2Busc, command=textInfo.yview)
    scrollVertical.grid(row=3, column=1, sticky="wns", )
    textInfo.config(yscrollcommand=scrollVertical.set)


    #----------------botones frame2----------------------------------------------
    botonBuscar = Button(frame2Busc, text = "Buscar", activebackground="#F50743",
                         command = lambda:buscarDisc())
    botonBuscar.grid(row=5, column=0, padx=5, pady=5,sticky = "w")
    botonBuscar.config(font=("comic sans ms", 10), bg="grey75", cursor="hand2")

    botonTodoRegistro = Button(frame2Busc, text="ver todos los registros", activebackground="#F50743",
                               command = lambda:buscarTodoDisc())
    botonTodoRegistro.grid(row=5, column=0, padx=5, pady=5, sticky = "e")
    botonTodoRegistro.config(font=("comic sans ms", 10), bg="grey75", cursor="hand2")

    botonDell = Button(frame2Busc, text="Borrar", activebackground="#F50743",
                               command=lambda: borrar())
    botonDell.grid(row=5, column=0, padx=5, pady=5,)
    botonDell.config(font=("comic sans ms", 10), bg="grey75", cursor="hand2")

    botonVerRegistro = Button(frame2Busc, text="Actualizar info", activebackground="#F50743",
                              command=lambda: ventana_actualizacioDisc.actulDisci())
    botonVerRegistro.grid(row=5, column=2, padx=5, pady=5, sticky="e")
    botonVerRegistro.config(font=("comic sans ms", 10), bg="grey75", cursor="hand2")

    #--------boton de ciere de la ventana------------------------------------------------
    botonCerrarV = Button(root, text="cerrar la ventana",
                          command = root.destroy, activebackground="#F50743")
    botonCerrarV.config(font=("comic sans ms", 10), bg="salmon3", cursor="hand2")
    botonCerrarV.pack(side="left", anchor="s")
    #----------------funciones de registro en la tabal disciplina--------------------------
    def registroDis(): # funcion para registrar informaciones en la tabla de disciplina

        try:
            if textoNombre.get():
                miConexion = sqlite3.connect(nameBD.nomBD())  # crear o abrir la conexion con al base de datos
                cursor = miConexion.cursor()

                cursor.execute("select * from alumno")
                stock = cursor.fetchall()
                i = 0
                while i < len(stock):

                    if i == len(stock) + 1:
                        pass
                        break

                    inforegistro1 = stock[i]
                    i += 1
                    if textoNombre.get().strip().upper() == inforegistro1[1].upper():
                        global recup
                        global recup1
                        cursor.execute(f"select id, curso from alumno where nombre_y_apellidos = '{textoNombre.get().strip().upper()}'")
                        stock1 = cursor.fetchall()
                        recup = stock1[0][0]
                        recup1 = stock1[0][1]

                nombre = textoNombre.get().strip().upper()
                curso = recup1
                faltas = 1
                id = recup
                fechaHora = datetime.datetime.now()

                textoDescripcion = fechaHora.strftime('%d/%m/%Y ')+"\n" +textDescrip.get(1.0, "end")
                avion = [
                    (nombre, curso, faltas, textoDescripcion, id)
                ]

                # insercion de datos en la tabla
                cursor.executemany("insert into disciplina values (?,?,?,?,?)", avion)

                miConexion.commit()  # validation de la insertion de datos

                miConexion.close()  # cerrar la conexion con la base de datos
                messagebox.showinfo('DULA', 'REGISTRADO CON ÉXITO')

                textoNombre.set("")
                textoCurso.set("")

                textDescrip.delete(1.0, "end")

            else:
                textoNombre.set("")
                textoCurso.set("")
                textDescrip.delete(1.0, "end")
        except NameError:
            textInfo.config(fg="red", state = 'normal')
            textInfo.delete(1.0, "end")
            textInfo.insert(1.0, "El nombre introducido para registrar\nNo corresponde a ningún alumno del centro")
            textInfo.config(state = 'disabled')

        #-------------------funciones de busqueda disciplinaria-----------------------------------------


    def buscarDisc(): # funcion para mostrar un solo registro de discplina y su foto del registro en la tabla alumno

        miConexion = sqlite3.connect(nameBD.nomBD())
        cursor = miConexion.cursor()
        cursor.execute("select * from disciplina")
        cajaRecepcion = cursor.fetchall()
        textInfo.config(state='normal')
        textInfo.delete(1.0, "end")

        i = 0
        while i < len(cajaRecepcion):

            if i == len(cajaRecepcion) + 1:
                pass
                break

            inforegistro2 = cajaRecepcion[i]
            j = i + 1
            i += 1

            if entryNombreApellFrame2.get() == "":
                textInfo.delete(1.0, "end")
                textInfo.config(fg="red")
                textInfo.insert(1.0, "Error!!!! el campo de búsqueda esta vacío,\nIntroduzca un nombre completo")
                break
            try:
                if entryNombreApellFrame2.get().strip().upper() == inforegistro2[0].upper():
                    """
                    textoInfo.delete(1.0, "end")
                    fotoCarnet = PhotoImage(file="logo2.png")
                    textoInfo.image_create(2, image=fotoCarnet)
                    textoInfo.config(fg = "black")
                    
                    """
                    global stock1
                    stock1 = inforegistro2[0].upper()
                    global foto
                    foto = PhotoImage(file=f"{funciones.rescateImagen(stock1)}")
                    textInfo.image_create(1.0, image=foto)  # parametro m
                    textInfo.insert(END, "\n\n")

                    textInfo.config(fg="black")
                    if inforegistro2[2] >=5:
                        textInfo.insert(END, "           DÍSCOLO\n")

                    textInfo.insert(END, "\nALUMNO/A: " + inforegistro2[0].upper()
                                     + "\nCURSO: "+ inforegistro2[1].upper() +
                                     "\nNUMERO DE FALTAS: " + str(inforegistro2[2]) +
                                    "\nÚLTIMAS FALTAS:\n"+inforegistro2[3]+"\n")


                    break
                if i == len(cajaRecepcion):
                    textInfo.delete(1.0, "end")
                    textInfo.config(fg="red")
                    textInfo.insert(1.0, "El nombre introducido para buscar,\nNo existe, revíselo porfavor!")
                    break
            except TclError:
                textInfo.config(fg="red")
                textInfo.insert(END, "El alumno/a no tiene datos registrados")

        miConexion.close()
        textInfo.config(state='disabled')



    def buscarTodoDisc(): # funcion para buscar y mostrar todos los registros de disciplina en la caja de texto
                          #con la imagen de cada de registro

            miConexion = sqlite3.connect(nameBD.nomBD())
            cursor = miConexion.cursor()
            cursor.execute("select * from disciplina")
            cajaRecepcion = cursor.fetchall()
            textInfo.config(state='normal')
            textInfo.delete(1.0, "end")
            j = 0.0
            i = 0
            while i < len(cajaRecepcion):

                if i == len(cajaRecepcion) + 1:
                    pass
                    break

                inforegistro2 = cajaRecepcion[i]

                i += 1

                textInfo.config(fg="black")
                textInfo.insert(1.0, "ALUMNO/A: " + inforegistro2[0].upper()
                                    + "\nCURSO: " + inforegistro2[1].upper() +
                                    "\nNUMERO DE FALTAS: " + str(inforegistro2[2]) +
                                    "\nÚLTIMAS FALTAS:\n" + inforegistro2[3] + "\n")




            miConexion.close()
            textInfo.config(state='disabled')




    def borrar():
        textInfo.config(state='normal')
        textInfo.delete(1.0, "end")



    root.mainloop()