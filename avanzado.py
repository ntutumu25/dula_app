from tkinter.ttk import *
from tkinter import *
import sqlite3
from tkinter import filedialog
from tkinter import filedialog
import nameBD



def avanzadoSion():

    root = Toplevel()
    root.title("DULA 1.0 CONSULTAS DE ACCESO")
    root.geometry("900x520")
    root.iconbitmap("images/dula.ico")
    root.config(bg = "grey85")
    root.resizable(0,0)
    #-----------LABEL ROOT-------------------------------------------------------------
    tituloLabel = Label(root, text="CONSULTAS DE ACCESO")
    tituloLabel.config(font=("jokerman", 14), bd=5, relief="groov", fg="black", bg="lemonchiffon2")
    tituloLabel.pack()

    logo = PhotoImage(file="images/logoTsei.png")
    labeLogo = Label(root, image=logo)
    labeLogo.place(x = 733, y = 0)


    # -----------frames root------------------------*
    frameText = Frame(root)
    frameText.config(bg = "grey85")
    frameText.pack(pady = 25)

    frame2 = Frame(root, width = 100, height = 50)
    frame2.config(bg = "grey85")

    frame2.pack()

    # ---------la cja de TEXTO-----------------------------
    textExample = Text(frameText, width=100, height=20, )
    textExample.config(bg="grey85", font=("comic sans ms", 10))
    textExample.grid(row=0, column=0,)

    # ----------scrollbar---------------
    scrollVertical = Scrollbar(frameText, command=textExample.yview)
    scrollVertical.grid(row=0, column=1, sticky="wns", )
    textExample.config(yscrollcommand=scrollVertical.set, )


    #-----------------------botones del frame2-------------------------------------------
    Button(frame2, text = "Sesiones", font=("comic sans ms", 11), command = lambda:abrir(),
           activebackground="#F50743").grid(row = 0, column = 0, padx = 5)

    Button(frame2, text="Usuarios", font=("comic sans ms", 11), command=lambda: usuarios(),
          activebackground="#F50743").grid(row=0, column=1, padx=5)
    #-------------------boton de cierre de ventana----------------------------------------

    botonCerrarV = Button(root, text="cerrar la ventana",
                          command=root.destroy, activebackground="#F50743")
    botonCerrarV.config(font=("comic sans ms", 10), bg="salmon3", cursor="hand2")
    botonCerrarV.pack(side="left", anchor="s")




    #---------------------funciones----------------------------------------------------
    def abrir():
        """
        esta funcion lee el archivo infoS y escribe la infoermacion en la caja de texto TextExample
        :return:
        """
        textExample.config(state="normal")
        textExample.delete(1.0, "end")
        archivo = open("system/infoS.txt", "r")

        textExample.insert(1.0,archivo.read())
        archivo.close()
        textExample.config(state = "disabled")


    def usuarios():
        """
                esta funcion lee el archivo registroUsuarios.txt y escribe la infoermacion en la caja de texto TextExample
                :return:
        """
        textExample.config(state="normal")
        textExample.delete(1.0, "end")
        archivo = open("system/registroUsuarios.txt", "r")

        textExample.insert(1.0, archivo.read())
        archivo.close()
        textExample.config(state="disabled")


    root.mainloop()



def buscarAvancada():

    root = Toplevel()
    root.title("DULA 1.0 BÚSQUEDAS AVANZADAS")
    root.geometry("1055x520")
    root.iconbitmap("images/dula.ico")
    root.config(bg="grey85")
    root.resizable(0, 0)

    #------------------label root-----------------------------

    logo = PhotoImage(file="images/logoTsei.png")
    labeLogo = Label(root, image=logo)
    labeLogo.pack(side="right", anchor="n")

    tituloLabel = Label(root, text="CONSULTAS PARAMETRADAS")
    tituloLabel.config(font=("jokerman", 14), bd=5, relief="groov", fg="black", bg="lemonchiffon2")
    tituloLabel.pack()

    # -----BOTON DE CIERRE DE VENTANA----------------------
    botonCerrarV = Button(root, text="cerrar la ventana",
                          command=root.destroy, activebackground="#F50743")
    botonCerrarV.config(font=("comic sans ms", 10), bg="salmon3", cursor="hand2")
    botonCerrarV.pack(side="left", anchor="s")

    #-------------------FRAME root------------------------------------------------------------------

    frame1 = Frame(root, width = 100, height = 50)
    frame1.config(bg = "grey85")
    frame1.place(x = 5, y = 70)

    frame2 = Frame(root, width=100, height=50)
    frame2.config(bg="grey85")
    frame2.place(x=540, y=70)

    frame3 = Frame(root, width=100, height=50)
    frame3.config(bg="grey85")
    frame3.place(x=540, y=230)

    Frame(root, width = 30, height = 163, bg = "grey75", relief = "sunken", bd = 5).place(x=510, y=70)
    #--------------------------label frame1---------------------------------------------------
    Label(frame1, text = "Información general", relief = "sunken", bd = 5, bg = "lightyellow",
          font = ("comic sans ms", 12), ).grid(row = 0, column = 0, padx = 5, pady = 5, columnspan = 3)

    Label(frame1, text = "Año Académico", bg = "white", bd = 3, relief = "groove",
          font = ("comic sans ms", 10), ).grid(row = 1, column = 0, padx = 5, pady = 8, sticky = "e")

    Label(frame1, text="Curso", bg="white", bd=3, relief="groove",
          font=("comic sans ms", 10), ).grid(row=1, column=1, padx=5, pady=8, sticky="e")

    #----------------entry frame1---------------------------------------------------------
    #--------------variable entry------------------------------------------------
    entry1 = StringVar()

    Entry(frame1, width = 30, textvariable = entry1, justify = "center",
          font = ("comic sans ms", 14)).grid(row = 4, column = 0, padx = 5, pady = 5, columnspan = 3)
    #------------botones frame1------------------------------------------------------------------------
    Button(frame1, text = "Ver", activebackground = "red", cursor = "hand2", width = 6, command = lambda:buscarGeneral(),
          font=("comic sans ms", 12)).grid(row=3, column=0, padx=5, pady=5, columnspan=3)
    #--------------------------radiobutons frame1--------------------------------------------------------

    #-------------variables radioButon-----------------------------------------------------------------
    radio1 = IntVar()

    Radiobutton(frame1, text = "Total de alumnos matriculados", variable = radio1, value = 1, bg = "grey85",cursor = "hand2",
                font = ("comic sans ms", 10)).grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "w")

    Radiobutton(frame1, text="Total de varones", variable=radio1, value=2, bg = "grey85", cursor = "hand2",
                font=("comic sans ms", 10)).grid(row=2, column=1, padx=5, pady=5, sticky = "w")

    Radiobutton(frame1, text="Total de hembras", variable=radio1, value=3, bg = "grey85", cursor = "hand2",
                font=("comic sans ms", 10)).grid(row=2, column=2, padx=5, pady=5, sticky = "w")
    #---------------------combobox frmae1---------------------------------------------------

    comboYear = Combobox(frame1, width = 10, state = "readonly")
    comboYear.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = "w")
    comboYear['values'] = ('2010/2011', '2011/2012', '2012/2013',
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
    comboYear.current(0)

    comboCurso = Combobox(frame1, width = 10, state = "readonly")
    comboCurso.grid(row = 1, column = 2, padx = 5, pady = 5, sticky = "w")
    comboCurso['values'] = ("TODOS", "1°ESBA", "2°ESBA", "3°ESBA", "4°ESBA", "1°BACH", "2°BACH")
    comboCurso.current(0)

    #--------------frame2 ----------------------------------------------------------------------------------
    #--------------label frame2----------------------------------------------------------------------------
    Label(frame2, text="Información específica", relief="sunken", bd=5, bg="white",
          font=("comic sans ms", 12), ).grid(row=0, column=0, padx=5, pady=5, columnspan=6)

    Label(frame2, text = "Curso", bg = "white",
          font = ("comic sans ms", 10), relief = "groove", bd = 3).grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "e")

    Label(frame2, text="Año Académico", bg="white",
          font=("comic sans ms", 10), relief="groove", bd=3).grid(row=1, column=2, padx=5, pady=5, sticky="e")

    Label(frame2, text="Sesión", bg="white",
          font=("comic sans ms", 10), relief="groove", bd=3).grid(row=1, column=4, padx=5, pady=5, sticky="e")
    #-----------------boton frame3----------------------------------------------------------
    Button(frame2, text = "Buscar",activebackground = "red", command = lambda:buscarEspecifica(), cursor = "hand2",
           width = 6, font=("comic sans ms", 10)).grid(row=2, column=0, padx=5, pady=5, columnspan = 6)
    #-------------------combobox frame2-------------------------------------------------------------------

    comboYearEspe = Combobox(frame2, width = 10, state = "readonly")
    comboYearEspe.grid(row=1, column=3, padx=5, pady=5, sticky="w")
    comboYearEspe['values'] = ('2010/2011', '2011/2012', '2012/2013',
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
    comboYearEspe.current(0)

    comboCursoEspe = Combobox(frame2, width=10, state = "readonly")
    comboCursoEspe.grid(row=1, column=1, padx=5, pady=5, sticky="w")
    comboCursoEspe['values'] = ("1°ESBA", "2°ESBA", "3°ESBA", "4°ESBA",
                                "1°BACH-CC", "1°BACH-TEC", "1°BACH-HUM", "2°BACH-CC", "2°BACH-TEC", "2°BACH-HUM")
    comboCursoEspe.current(0)

    comboSesionEspe = Combobox(frame2, width=10, state="readonly")
    comboSesionEspe.grid(row=1, column=5, padx=5, pady=5, sticky="w")
    comboSesionEspe['values'] = ("1°Trimestre", "2°Trimestre", "3°Trimestre", "JUNIO")
    comboSesionEspe.current(0)

    # ---------la cja de TEXTO frame3-----------------------------
    textExample = Text(frame3, width=60, height=15, )
    textExample.config(bg="white", font=("comic sans ms", 10))
    textExample.grid(row=0, column=0, padx=5, pady=5)

    # ----------scrollbar---------------
    scrollVertical = Scrollbar(frame3, command=textExample.yview)
    scrollVertical.grid(row=0, column=1, sticky="wns", )
    textExample.config(yscrollcommand=scrollVertical.set)


    #----------------------funciones de la parte general---------------------------------------------
    def buscarGeneral():
        """
        esta funcion permite obtener el numero de alumnos matriculados de un ano academico, en todo los cursos y en particulares
        igualmente reflejar el numero de varones y de hembras

        :return:
        """

        connexion = sqlite3.connect(nameBD.nomBD())  # crear o abrir la conexion con al base de datos
        cursor = connexion.cursor()


        try:
            archivo = open("informe/listaAlumnos.doc", "w")
            nomInsti = "HOLLPRODY.S.L"

            if radio1.get() == 1:
                if comboCurso.get() == "TODOS":
                    cursor.execute(f"select nombre  from primero_esba_uno where año_academico =  '{comboYear.get()}'")
                    stock = cursor.fetchall()

                    cursor.execute(f"select nombre  from segundo_esba_uno where año_academico = '{comboYear.get()}'")
                    stock1 = cursor.fetchall()

                    cursor.execute(f"select nombre  from tercero_esba_uno where año_academico =  '{comboYear.get()}'")
                    stock2 = cursor.fetchall()

                    cursor.execute(f"select nombre  from cuarto_esba_uno where año_academico =  '{comboYear.get()}'")
                    stock3 = cursor.fetchall()

                    cursor.execute(f"select nombre  from primero_bach_uno where año_academico =  '{comboYear.get()}'")
                    stock4 = cursor.fetchall()

                    cursor.execute(f"select nombre  from segundo_bach_uno where año_academico =  '{comboYear.get()}'")
                    stock5 = cursor.fetchall()

                    lista = stock + stock1 + stock2 + stock3 + stock4 + stock5

                    entry1.set(str(len(lista))+ " alumnos")






                elif comboCurso.get() == "1°ESBA":
                    cursor.execute(f"select nombre  from primero_esba_uno where año_academico =  '{comboYear.get()}' ORDER BY nombre")
                    stock = cursor.fetchall()
                    entry1.set(str(len(stock))+ " alumnos")

                    archivo.write(f"{nomInsti}\nSECRETARÍA\n\nCURSO: 1°ESBA\nAÑO ACADÉMICO: {comboYear.get()}")
                    archivo.write("\n\n                         LISTA DE ALUMNOS MATRICULADOS\n")
                    i = 0
                    while i < len(stock):
                        m = i + 1
                        archivo.write(f"\n{m}._{stock[i][0]}")
                        i += 1

                elif comboCurso.get() == "2°ESBA":
                    cursor.execute(f"select nombre  from segundo_esba_uno where año_academico =  '{comboYear.get()}' ORDER BY nombre")
                    stock = cursor.fetchall()
                    entry1.set(str(len(stock))+ " alumnos")

                    archivo.write(
                        f"{nomInsti}\nSECRETARÍA\n\nCURSO: 2°ESBA\nAÑO ACADÉMICO: {comboYear.get()}")
                    archivo.write("\n\n                         LISTA DE ALUMNOS MATRICULADOS\n")
                    i = 0
                    while i < len(stock):
                        m = i + 1
                        archivo.write(f"\n{m}._{stock[i][0]}")
                        i += 1


                elif comboCurso.get() == "3°ESBA":
                    cursor.execute(f"select nombre  from tercero_esba_uno where año_academico =  '{comboYear.get()}' ORDER BY nombre")
                    stock = cursor.fetchall()
                    entry1.set(str(len(stock))+ " alumnos")

                    archivo.write(
                        f"{nomInsti}\nSECRETARÍA\n\nCURSO: 3°ESBA\nAÑO ACADÉMICO: {comboYear.get()}")
                    archivo.write("\n\n                         LISTA DE ALUMNOS MATRICULADOS\n")
                    i = 0
                    while i < len(stock):
                        m = i + 1
                        archivo.write(f"\n{m}._{stock[i][0]}")
                        i += 1


                elif comboCurso.get() == "4°ESBA":
                    cursor.execute(f"select nombre  from cuarto_esba_uno where año_academico =  '{comboYear.get()}' ORDER BY nombre")
                    stock = cursor.fetchall()
                    entry1.set(str(len(stock))+ " alumnos")

                    archivo.write(
                        f"{nomInsti}\nSECRETARÍA\n\nCURSO: 4°ESBA\nAÑO ACADÉMICO: {comboYear.get()}")
                    archivo.write("\n\n                         LISTA DE ALUMNOS MATRICULADOS\n")
                    i = 0
                    while i < len(stock):
                        m = i + 1
                        archivo.write(f"\n{m}._{stock[i][0]}")
                        i += 1

                elif comboCurso.get() == "1°BACH":
                    cursor.execute(f"select nombre  from primero_bach_uno where año_academico =  '{comboYear.get()}' ORDER BY nombre")
                    stock = cursor.fetchall()
                    entry1.set(str(len(stock))+ " alumnos")

                    archivo.write(
                        f"{nomInsti}\nSECRETARÍA\n\nCURSO: 1°BACH\nAÑO ACADÉMICO: {comboYear.get()}")
                    archivo.write("\n\n                         LISTA DE ALUMNOS MATRICULADOS\n")
                    i = 0
                    while i < len(stock):
                        m = i + 1
                        archivo.write(f"\n{m}._{stock[i][0]}")
                        i += 1


                elif comboCurso.get() == "2°BACH":
                    cursor.execute(f"select nombre  from segundo_bach_uno where año_academico =  '{comboYear.get()}' ORDER BY nombre")
                    stock = cursor.fetchall()
                    entry1.set(str(len(stock))+ " alumnos")

                    archivo.write(
                        f"{nomInsti}\nSECRETARÍA\n\nCURSO: 2°BACH\nAÑO ACADÉMICO: {comboYear.get()}")
                    archivo.write("\n\n                         LISTA DE ALUMNOS MATRICULADOS\n")
                    i = 0
                    while i < len(stock):
                        m = i + 1
                        archivo.write(f"\n{m}._{stock[i][0]}")
                        i += 1
                else:
                    pass


            elif radio1.get() == 2:


                if comboCurso.get() == "TODOS":
                    cursor.execute(f"select nombre  from primero_esba_uno where año_academico =  '{comboYear.get()}'")
                    stock = cursor.fetchall()

                    cursor.execute(f"select nombre  from segundo_esba_uno where año_academico = '{comboYear.get()}'")
                    stock1 = cursor.fetchall()

                    cursor.execute(f"select nombre  from tercero_esba_uno where año_academico =  '{comboYear.get()}'")
                    stock2 = cursor.fetchall()

                    cursor.execute(f"select nombre  from cuarto_esba_uno where año_academico =  '{comboYear.get()}'")
                    stock3 = cursor.fetchall()

                    cursor.execute(f"select nombre  from primero_bach_uno where año_academico =  '{comboYear.get()}'")
                    stock4 = cursor.fetchall()

                    cursor.execute(f"select nombre  from segundo_bach_uno where año_academico =  '{comboYear.get()}'")
                    stock5 = cursor.fetchall()

                    lista = stock + stock1 + stock2 + stock3 + stock4 + stock5

                    i = 0
                    global j
                    j = 0
                    while i < len(lista):
                        cursor.execute(f"select genero  from alumno where nombre_y_apellidos =  '{lista[i][0]}'")
                        box = cursor.fetchall()
                        if box[0][0] == "M":
                            j += 1
                        i += 1
                    entry1.set(str(j)+ " v")

                elif comboCurso.get() == "1°ESBA":
                    cursor.execute(f"select nombre  from primero_esba_uno where año_academico =  '{comboYear.get()}'")
                    stock = cursor.fetchall()

                    i = 0

                    j = 0
                    while i < len(stock):
                        cursor.execute(f"select genero  from alumno where nombre_y_apellidos =  '{stock[i][0]}'")
                        box = cursor.fetchall()
                        if box[0][0] == "M":
                            j += 1
                        i += 1
                    entry1.set(str(j)+ " v")

                elif comboCurso.get() == "2°ESBA":
                    cursor.execute(f"select nombre  from segundo_esba_uno where año_academico =  '{comboYear.get()}'")
                    stock = cursor.fetchall()

                    i = 0

                    j = 0
                    while i < len(stock):
                        cursor.execute(f"select genero  from alumno where nombre_y_apellidos =  '{stock[i][0]}'")
                        box = cursor.fetchall()
                        if box[0][0] == "M":
                            j += 1
                        i += 1
                    entry1.set(str(j)+ " v")

                elif comboCurso.get() == "3°ESBA":
                    cursor.execute(f"select nombre  from tercero_esba_uno where año_academico =  '{comboYear.get()}'")
                    stock = cursor.fetchall()

                    i = 0

                    j = 0
                    while i < len(stock):
                        cursor.execute(f"select genero  from alumno where nombre_y_apellidos =  '{stock[i][0]}'")
                        box = cursor.fetchall()
                        if box[0][0] == "M":
                            j += 1
                        i += 1
                    entry1.set(str(j)+ " v")

                elif comboCurso.get() == "4°ESBA":
                    cursor.execute(f"select nombre  from cuarto_esba_uno where año_academico =  '{comboYear.get()}'")
                    stock = cursor.fetchall()

                    i = 0

                    j = 0
                    while i < len(stock):
                        cursor.execute(f"select genero  from alumno where nombre_y_apellidos =  '{stock[i][0]}'")
                        box = cursor.fetchall()
                        if box[0][0] == "M":
                            j += 1
                        i += 1
                    entry1.set(str(j)+ " v")

                elif comboCurso.get() == "1°BACH":
                    cursor.execute(f"select nombre  from primero_bach_uno where año_academico =  '{comboYear.get()}'")
                    stock = cursor.fetchall()

                    i = 0

                    j = 0
                    while i < len(stock):
                        cursor.execute(f"select genero  from alumno where nombre_y_apellidos =  '{stock[i][0]}'")
                        box = cursor.fetchall()
                        if box[0][0] == "M":
                            j += 1
                        i += 1
                    entry1.set(str(j)+ " v")

                elif comboCurso.get() == "2°BACH":
                    cursor.execute(f"select nombre  from segundo_bach_uno where año_academico =  '{comboYear.get()}'")
                    stock = cursor.fetchall()

                    i = 0

                    j = 0
                    while i < len(stock):
                        cursor.execute(f"select genero  from alumno where nombre_y_apellidos =  '{stock[i][0]}'")
                        box = cursor.fetchall()
                        if box[0][0] == "M":
                            j += 1
                        i += 1
                    entry1.set(str(j) + " v")

            elif radio1.get() == 3:
                if comboCurso.get() == "TODOS":
                    cursor.execute(f"select nombre  from primero_esba_uno where año_academico =  '{comboYear.get()}'")
                    stock = cursor.fetchall()

                    cursor.execute(f"select nombre  from segundo_esba_uno where año_academico = '{comboYear.get()}'")
                    stock1 = cursor.fetchall()

                    cursor.execute(f"select nombre  from tercero_esba_uno where año_academico =  '{comboYear.get()}'")
                    stock2 = cursor.fetchall()

                    cursor.execute(f"select nombre  from cuarto_esba_uno where año_academico =  '{comboYear.get()}'")
                    stock3 = cursor.fetchall()

                    cursor.execute(f"select nombre  from primero_bach_uno where año_academico =  '{comboYear.get()}'")
                    stock4 = cursor.fetchall()

                    cursor.execute(f"select nombre  from segundo_bach_uno where año_academico =  '{comboYear.get()}'")
                    stock5 = cursor.fetchall()

                    lista = stock + stock1 + stock2 + stock3 + stock4 + stock5

                    i = 0

                    j = 0
                    while i < len(lista):
                        cursor.execute(f"select genero  from alumno where nombre_y_apellidos =  '{lista[i][0]}'")
                        box = cursor.fetchall()
                        if box[0][0] == "F":
                            j += 1
                        i += 1
                    entry1.set(str(j)+ " h")

                elif comboCurso.get() == "1°ESBA":
                    cursor.execute(f"select nombre  from primero_esba_uno where año_academico =  '{comboYear.get()}'")
                    stock = cursor.fetchall()

                    i = 0

                    j = 0
                    while i < len(stock):
                        cursor.execute(f"select genero  from alumno where nombre_y_apellidos =  '{stock[i][0]}'")
                        box = cursor.fetchall()
                        if box[0][0] == "F":
                            j += 1
                        i += 1
                    entry1.set(str(j)+ " h")

                elif comboCurso.get() == "2°ESBA":
                    cursor.execute(f"select nombre  from segundo_esba_uno where año_academico =  '{comboYear.get()}'")
                    stock = cursor.fetchall()

                    i = 0

                    j = 0
                    while i < len(stock):
                        cursor.execute(f"select genero  from alumno where nombre_y_apellidos =  '{stock[i][0]}'")
                        box = cursor.fetchall()
                        if box[0][0] == "F":
                            j += 1
                        i += 1
                    entry1.set(str(j)+ " h")

                elif comboCurso.get() == "3°ESBA":
                    cursor.execute(f"select nombre  from tercero_esba_uno where año_academico =  '{comboYear.get()}'")
                    stock = cursor.fetchall()

                    i = 0

                    j = 0
                    while i < len(stock):
                        cursor.execute(f"select genero  from alumno where nombre_y_apellidos =  '{stock[i][0]}'")
                        box = cursor.fetchall()
                        if box[0][0] == "F":
                            j += 1
                        i += 1
                    entry1.set(str(j)+ " h")

                elif comboCurso.get() == "4°ESBA":
                    cursor.execute(f"select nombre  from cuarto_esba_uno where año_academico =  '{comboYear.get()}'")
                    stock = cursor.fetchall()

                    i = 0

                    j = 0
                    while i < len(stock):
                        cursor.execute(f"select genero  from alumno where nombre_y_apellidos =  '{stock[i][0]}'")
                        box = cursor.fetchall()
                        if box[0][0] == "F":
                            j += 1
                        i += 1
                    entry1.set(str(j)+ " h")

                elif comboCurso.get() == "1°BACH":
                    cursor.execute(f"select nombre  from primero_bach_uno where año_academico =  '{comboYear.get()}'")
                    stock = cursor.fetchall()

                    i = 0

                    j = 0
                    while i < len(stock):
                        cursor.execute(f"select genero  from alumno where nombre_y_apellidos =  '{stock[i][0]}'")
                        box = cursor.fetchall()
                        if box[0][0] == "F":
                            j += 1
                        i += 1
                    entry1.set(str(j)+ " h")

                elif comboCurso.get() == "2°BACH":
                    cursor.execute(f"select nombre  from segundo_bach_uno where año_academico =  '{comboYear.get()}'")
                    stock = cursor.fetchall()

                    i = 0

                    j = 0
                    while i < len(stock):
                        cursor.execute(f"select genero  from alumno where nombre_y_apellidos =  '{stock[i][0]}'")
                        box = cursor.fetchall()
                        if box[0][0] == "F":
                            j += 1
                        i += 1
                    entry1.set(str(j) + " h")
                else:
                    pass

            archivo.close()

        except PermissionError:
            entry1.set("cierre el documento listaAlumnos.doc")



        connexion.close()













        connexion.close()


    #-----------------------funciones de la parte especifica-------------------------------------------

    def buscarEspecifica():

        connexion = sqlite3.connect(nameBD.nomBD())  # crear o abrir la conexion con al base de datos
        cursor = connexion.cursor()

        if comboCursoEspe.get() == "1°ESBA":
            if comboSesionEspe.get() == "1°Trimestre":
                cursor.execute(f"select *  from primero_esba_uno where año_academico =  '{comboYearEspe.get()}'")
                stock = cursor.fetchall()

                i = 0

                m = 0
                textExample.delete(1.0, END)
                textExample.insert(1.0,f"ALUMNOS APROBADOS EN TODAS "
                                       f"LAS MATERIAS\nCURSO: 1°ESBA\nAño académico: {comboYearEspe.get()}\nSesión: 1°Trimestre\n\n")

                while i < len(stock):
                    if (stock[i][3] >= 5.0) and (stock[i][4] >= 5.0) and (stock[i][5] >= 5.0) and (
                            stock[i][6] >= 5.0) and (stock[i][7] >= 5.0) and (stock[i][8] >= 5.0) and (
                            stock[i][9] >= 5.0) and (stock[i][10] >= 5.0) and (stock[i][11] >= 5.0) and (
                            stock[i][12] >= 5.0):
                        m += 1
                        textExample.insert(END, f"{str(m)}._{stock[i][1]}\n")

                    i += 1
                textExample.insert(END, f"\nTOTAL: {str(m)}")

            elif comboSesionEspe.get() == "2°Trimestre":
                cursor.execute(f"select *  from primero_esba_dos where año_academico =  '{comboYearEspe.get()}'")
                stock = cursor.fetchall()

                i = 0

                m = 0
                textExample.delete(1.0, END)
                textExample.insert(1.0,f"ALUMNOS APROBADOS EN TODAS "
                                       f"LAS MATERIAS\nCURSO: 1°ESBA\nAño académico: {comboYearEspe.get()}\nSesión: 2°Trimestre\n\n")

                while i < len(stock):
                    if (stock[i][3] >= 5.0 )and (stock[i][4]>= 5.0) and (stock[i][5]>= 5.0) and (stock[i][6]>= 5.0) and (stock[i][7]>= 5.0 ) and (stock[i][8]>= 5.0 )and (stock[i][9]>= 5.0 ) and (stock[i][10]>= 5.0 ) and (stock[i][11]>= 5.0 ) and (stock[i][12] >= 5.0 ):
                        m += 1
                        textExample.insert(END, f"{str(m)}._{stock[i][1]}\n")

                    i += 1
                textExample.insert(END, f"\nTOTAL: {str(m)}")

            elif comboSesionEspe.get() == "3°Trimestre":
                cursor.execute(f"select *  from primero_esba_tres where año_academico =  '{comboYearEspe.get()}'")
                stock = cursor.fetchall()

                i = 0

                m = 0
                textExample.delete(1.0, END)
                textExample.insert(1.0,f"ALUMNOS APROBADOS EN TODAS "
                                       f"LAS MATERIAS\nCURSO: 1°ESBA\nAño académico: {comboYearEspe.get()}\nSesión: 3°Trimestre\n\n")

                while i < len(stock):
                    if (stock[i][3] >= 5.0) and (stock[i][4] >= 5.0) and (stock[i][5] >= 5.0) and (
                            stock[i][6] >= 5.0) and (stock[i][7] >= 5.0) and (stock[i][8] >= 5.0) and (
                            stock[i][9] >= 5.0) and (stock[i][10] >= 5.0) and (stock[i][11] >= 5.0) and (
                            stock[i][12] >= 5.0):
                        m += 1
                        textExample.insert(END, f"{str(m)}._{stock[i][1]}\n")

                    i += 1
                textExample.insert(END, f"\nTOTAL: {str(m)}")

            elif comboSesionEspe.get() == "JUNIO":
                cursor.execute(f"select *  from primero_esba_junio where año_academico =  '{comboYearEspe.get()}'")
                stock = cursor.fetchall()

                i = 0

                m = 0
                textExample.delete(1.0, END)
                textExample.insert(1.0,f"ALUMNOS APROBADOS EN TODAS "
                                       f"LAS MATERIAS\nCURSO: 1°ESBA\nAño académico: {comboYearEspe.get()}\n JUNIO\n\n")

                while i < len(stock):
                    if (stock[i][3] >= 5.0) and (stock[i][4] >= 5.0) and (stock[i][5] >= 5.0) and (
                            stock[i][6] >= 5.0) and (stock[i][7] >= 5.0) and (stock[i][8] >= 5.0) and (
                            stock[i][9] >= 5.0) and (stock[i][10] >= 5.0) and (stock[i][11] >= 5.0) and (
                            stock[i][12] >= 5.0):
                        m += 1
                        textExample.insert(END, f"{str(m)}._{stock[i][1]}\n")

                    i += 1
                textExample.insert(END, f"\nTOTAL: {str(m)}")

        elif comboCursoEspe.get() == "2°ESBA":

            if comboSesionEspe.get() == "1°Trimestre":
                cursor.execute(f"select *  from segundo_esba_uno where año_academico =  '{comboYearEspe.get()}'")
                stock = cursor.fetchall()

                i = 0

                m = 0
                textExample.delete(1.0, END)
                textExample.insert(1.0,f"ALUMNOS APROBADOS EN TODAS "
                                       f"LAS MATERIAS\nCURSO: 2°ESBA\nAño académico: {comboYearEspe.get()}\nSesión: 1°Trimestre\n\n")

                while i < len(stock):
                    if (stock[i][3] >= 5.0) and (stock[i][4] >= 5.0) and (stock[i][5] >= 5.0) and (
                            stock[i][6] >= 5.0) and (stock[i][7] >= 5.0) and (stock[i][8] >= 5.0) and (
                            stock[i][9] >= 5.0) and (stock[i][10] >= 5.0) and (stock[i][11] >= 5.0) and (
                            stock[i][12] >= 5.0):
                        m += 1
                        textExample.insert(END, f"{str(m)}._{stock[i][1]}\n")

                    i += 1
                textExample.insert(END, f"\nTOTAL: {str(m)}")

            elif comboSesionEspe.get() == "2°Trimestre":
                cursor.execute(f"select *  from segundo_esba_dos where año_academico =  '{comboYearEspe.get()}'")
                stock = cursor.fetchall()

                i = 0

                m = 0
                textExample.delete(1.0, END)
                textExample.insert(1.0,f"ALUMNOS APROBADOS EN TODAS "
                                       f"LAS MATERIAS\nCURSO: 2°ESBA\nAño académico: {comboYearEspe.get()}\nSesión: 2°Trimestre\n\n")

                while i < len(stock):
                    if (stock[i][3] >= 5.0) and (stock[i][4] >= 5.0) and (stock[i][5] >= 5.0) and (
                            stock[i][6] >= 5.0) and (stock[i][7] >= 5.0) and (stock[i][8] >= 5.0) and (
                            stock[i][9] >= 5.0) and (stock[i][10] >= 5.0) and (stock[i][11] >= 5.0) and (
                            stock[i][12] >= 5.0):
                        m += 1
                        textExample.insert(END, f"{str(m)}._{stock[i][1]}\n")

                    i += 1
                textExample.insert(END, f"\nTOTAL: {str(m)}")

            elif comboSesionEspe.get() == "3°Trimestre":
                cursor.execute(f"select *  from segundo_esba_tres where año_academico =  '{comboYearEspe.get()}'")
                stock = cursor.fetchall()

                i = 0

                m = 0
                textExample.delete(1.0, END)
                textExample.insert(1.0,f"ALUMNOS APROBADOS EN TODAS "
                                       f"LAS MATERIAS\nCURSO: 2°ESBA\nAño académico: {comboYearEspe.get()}\nSesión: 3°Trimestre\n\n")

                while i < len(stock):
                    if (stock[i][3] >= 5.0) and (stock[i][4] >= 5.0) and (stock[i][5] >= 5.0) and (
                            stock[i][6] >= 5.0) and (stock[i][7] >= 5.0) and (stock[i][8] >= 5.0) and (
                            stock[i][9] >= 5.0) and (stock[i][10] >= 5.0) and (stock[i][11] >= 5.0) and (
                            stock[i][12] >= 5.0):
                        m += 1
                        textExample.insert(END, f"{str(m)}._{stock[i][1]}\n")

                    i += 1
                textExample.insert(END, f"\nTOTAL: {str(m)}")

            elif comboSesionEspe.get() == "JUNIO":
                cursor.execute(f"select *  from segundo_esba_junio where año_academico =  '{comboYearEspe.get()}'")
                stock = cursor.fetchall()

                i = 0

                m = 0
                textExample.delete(1.0, END)
                textExample.insert(1.0,f"ALUMNOS APROBADOS EN TODAS "
                                       f"LAS MATERIAS\nCURSO: 2°ESBA\nAño académico: {comboYearEspe.get()}\nJUNIO\n\n")

                while i < len(stock):
                    if (stock[i][3] >= 5.0) and (stock[i][4] >= 5.0) and (stock[i][5] >= 5.0) and (
                            stock[i][6] >= 5.0) and (stock[i][7] >= 5.0) and (stock[i][8] >= 5.0) and (
                            stock[i][9] >= 5.0) and (stock[i][10] >= 5.0) and (stock[i][11] >= 5.0) and (
                            stock[i][12] >= 5.0):
                        m += 1
                        textExample.insert(END, f"{str(m)}._{stock[i][1]}\n")

                    i += 1
                textExample.insert(END, f"\nTOTAL: {str(m)}")

        elif comboCursoEspe.get() == "3°ESBA":

            if comboSesionEspe.get() == "1°Trimestre":
                cursor.execute(f"select *  from tercero_esba_uno where año_academico =  '{comboYearEspe.get()}'")
                stock = cursor.fetchall()

                i = 0

                m = 0
                textExample.delete(1.0, END)
                textExample.insert(1.0,f"ALUMNOS APROBADOS EN TODAS "
                                       f"LAS MATERIAS\nCURSO: 3°ESBA\nAño académico: {comboYearEspe.get()}\nSesión: 1°Trimestre\n\n")

                while i < len(stock):
                    if ((stock[i][3]>= 5.0) and (stock[i][4]>= 5.0) and (stock[i][5]>= 5.0) and (stock[i][6]>= 5.0) and (stock[i][7]>= 5.0) and (stock[i][8]>= 5.0) and
                            (stock[i][9]>= 5.0) and (stock[i][10]>= 5.0) and (stock[i][11]>= 5.0) and (stock[i][12]>= 5.0) and (stock[i][13]>= 5.0) and (stock[i][14]>= 5.0)):


                        m += 1
                        textExample.insert(END, f"{str(m)}._{stock[i][1]}\n")

                    i += 1
                textExample.insert(END, f"\nTOTAL: {str(m)}")

            elif comboSesionEspe.get() == "2°Trimestre":
                cursor.execute(f"select *  from tercero_esba_dos where año_academico =  '{comboYearEspe.get()}'")
                stock = cursor.fetchall()

                i = 0

                m = 0
                textExample.delete(1.0, END)
                textExample.insert(1.0,f"ALUMNOS APROBADOS EN TODAS "
                                       f"LAS MATERIAS\nCURSO: 3°ESBA\nAño académico: {comboYearEspe.get()}\nSesión: 2°Trimestre\n\n")

                while i < len(stock):
                    if ((stock[i][3]>= 5.0) and (stock[i][4]>= 5.0) and (stock[i][5]>= 5.0) and (stock[i][6]>= 5.0) and (stock[i][7]>= 5.0) and (stock[i][8]>= 5.0) and
                            (stock[i][9]>= 5.0) and (stock[i][10]>= 5.0) and (stock[i][11]>= 5.0) and (stock[i][12]>= 5.0) and (stock[i][13]>= 5.0) and (stock[i][14]>= 5.0)):

                        m += 1
                        textExample.insert(END, f"{str(m)}._{stock[i][1]}\n")

                    i += 1
                textExample.insert(END, f"\nTOTAL: {str(m)}")

            elif comboSesionEspe.get() == "3°Trimestre":
                cursor.execute(f"select *  from tercero_esba_tres where año_academico =  '{comboYearEspe.get()}'")
                stock = cursor.fetchall()

                i = 0

                m = 0
                textExample.delete(1.0, END)
                textExample.insert(1.0,f"ALUMNOS APROBADOS EN TODAS "
                                       f"LAS MATERIAS\nCURSO: 3°ESBA\nAño académico: {comboYearEspe.get()}\nSesión: 3°Trimestre\n\n")

                while i < len(stock):
                    if ((stock[i][3]>= 5.0) and (stock[i][4]>= 5.0) and (stock[i][5]>= 5.0) and (stock[i][6]>= 5.0) and (stock[i][7]>= 5.0) and (stock[i][8]>= 5.0) and
                            (stock[i][9]>= 5.0) and (stock[i][10]>= 5.0) and (stock[i][11]>= 5.0) and (stock[i][12]>= 5.0) and (stock[i][13]>= 5.0) and (stock[i][14]>= 5.0)):

                        m += 1
                        textExample.insert(END, f"{str(m)}._{stock[i][1]}\n")

                    i += 1
                textExample.insert(END, f"\nTOTAL: {str(m)}")

            elif comboSesionEspe.get() == "JUNIO":
                cursor.execute(f"select *  from tercero_esba_junio where año_academico =  '{comboYearEspe.get()}'")
                stock = cursor.fetchall()

                i = 0

                m = 0
                textExample.delete(1.0, END)
                textExample.insert(1.0, f"ALUMNOS APROBADOS EN TODAS "
                                        f"LAS MATERIAS\nCURSO: 3°ESBA\nAño académico: {comboYearEspe.get()}\nJUNIO\n\n")

                while i < len(stock):
                    if ((stock[i][3]>= 5.0) and (stock[i][4]>= 5.0) and (stock[i][5]>= 5.0) and (stock[i][6]>= 5.0) and (stock[i][7]>= 5.0) and (stock[i][8]>= 5.0) and
                            (stock[i][9]>= 5.0) and (stock[i][10]>= 5.0) and (stock[i][11]>= 5.0) and (stock[i][12]>= 5.0) and (stock[i][13]>= 5.0) and (stock[i][14]>= 5.0)):

                        m += 1
                        textExample.insert(END, f"{str(m)}._{stock[i][1]}\n")

                    i += 1
                textExample.insert(END, f"\nTOTAL: {str(m)}")

        elif comboCursoEspe.get() == "4°ESBA":

            if comboSesionEspe.get() == "1°Trimestre":
                cursor.execute(f"select *  from cuarto_esba_uno where año_academico =  '{comboYearEspe.get()}'")
                stock = cursor.fetchall()

                i = 0

                m = 0
                textExample.delete(1.0, END)
                textExample.insert(1.0,f"ALUMNOS APROBADOS EN TODAS "
                                       f"LAS MATERIAS\nCURSO: 4°ESBA\nAño académico: {comboYearEspe.get()}\nSesión: 1°Trimestre\n\n")

                while i < len(stock):
                    if ((stock[i][3]>= 5.0) and (stock[i][4]>= 5.0) and (stock[i][5]>= 5.0) and (stock[i][6]>= 5.0) and (stock[i][7]>= 5.0) and (stock[i][8]>= 5.0) and
                            (stock[i][9]>= 5.0) and (stock[i][10]>= 5.0) and (stock[i][11]>= 5.0) and (stock[i][12]>= 5.0) and (stock[i][13]>= 5.0) and (stock[i][14]>= 5.0)):

                        m += 1
                        textExample.insert(END, f"{str(m)}._{stock[i][1]}\n")

                    i += 1
                textExample.insert(END, f"\nTOTAL: {str(m)}")

            elif comboSesionEspe.get() == "2°Trimestre":
                cursor.execute(f"select *  from cuarto_esba_dos where año_academico =  '{comboYearEspe.get()}'")
                stock = cursor.fetchall()

                i = 0

                m = 0
                textExample.delete(1.0, END)
                textExample.insert(1.0,f"ALUMNOS APROBADOS EN TODAS "
                                       f"LAS MATERIAS\nCURSO: 4°ESBA\nAño académico: {comboYearEspe.get()}\nSesión: 2°Trimestre\n\n")

                while i < len(stock):
                    if ((stock[i][3]>= 5.0) and (stock[i][4]>= 5.0) and (stock[i][5]>= 5.0) and (stock[i][6]>= 5.0) and (stock[i][7]>= 5.0) and (stock[i][8]>= 5.0) and
                            (stock[i][9]>= 5.0) and (stock[i][10]>= 5.0) and (stock[i][11]>= 5.0) and (stock[i][12]>= 5.0) and (stock[i][13]>= 5.0) and (stock[i][14]>= 5.0)):

                        m += 1
                        textExample.insert(END, f"{str(m)}._{stock[i][1]}\n")

                    i += 1
                textExample.insert(END, f"\nTOTAL: {str(m)}")

            elif comboSesionEspe.get() == "3°Trimestre":
                cursor.execute(f"select *  from cuarto_esba_tres where año_academico =  '{comboYearEspe.get()}'")
                stock = cursor.fetchall()

                i = 0

                m = 0
                textExample.delete(1.0, END)
                textExample.insert(1.0,f"ALUMNOS APROBADOS EN TODAS "
                                       f"LAS MATERIAS\nCURSO: 4°ESBA\nAño académico: {comboYearEspe.get()}\nSesión: 3°Trimestre\n\n")

                while i < len(stock):
                    if ((stock[i][3]>= 5.0) and (stock[i][4]>= 5.0) and (stock[i][5]>= 5.0) and (stock[i][6]>= 5.0) and (stock[i][7]>= 5.0) and (stock[i][8]>= 5.0) and
                            (stock[i][9]>= 5.0) and (stock[i][10]>= 5.0) and (stock[i][11]>= 5.0) and (stock[i][12]>= 5.0) and (stock[i][13]>= 5.0) and (stock[i][14]>= 5.0)):

                        m += 1
                        textExample.insert(END, f"{str(m)}._{stock[i][1]}\n")

                    i += 1
                textExample.insert(END, f"\nTOTAL: {str(m)}")

            elif comboSesionEspe.get() == "JUNIO":
                cursor.execute(f"select *  from cuarto_esba_junio where año_academico =  '{comboYearEspe.get()}'")
                stock = cursor.fetchall()

                i = 0

                m = 0
                textExample.delete(1.0, END)
                textExample.insert(1.0, f"ALUMNOS APROBADOS EN TODAS "
                                        f"LAS MATERIAS\nCURSO: 4°ESBA\nAño académico: {comboYearEspe.get()}\nJUNIO\n\n")

                while i < len(stock):
                    if ((stock[i][3]>= 5.0) and (stock[i][4]>= 5.0) and (stock[i][5]>= 5.0) and (stock[i][6]>= 5.0) and (stock[i][7]>= 5.0) and (stock[i][8]>= 5.0) and
                            (stock[i][9]>= 5.0) and (stock[i][10]>= 5.0) and (stock[i][11]>= 5.0) and (stock[i][12]>= 5.0) and (stock[i][13]>= 5.0) and (stock[i][14]>= 5.0)):
                        
                        m += 1
                        textExample.insert(END, f"{str(m)}._{stock[i][1]}\n")

                    i += 1
                textExample.insert(END, f"\nTOTAL: {str(m)}")


        elif comboCursoEspe.get() == "1°BACH-CC":

            if comboSesionEspe.get() == "1°Trimestre":
                cursor.execute(f"select *  from primero_bach_uno where año_academico =  '{comboYearEspe.get()}'")
                stock = cursor.fetchall()

                i = 0

                m = 0
                textExample.delete(1.0, END)
                textExample.insert(1.0,f"ALUMNOS APROBADOS EN TODAS "
                                       f"LAS MATERIAS\nCURSO: 1°BACH-CIENCIAS\nAño académico: {comboYearEspe.get()}\nSesión: 1°Trimestre\n\n")

                while i < len(stock):
                    if ((stock[i][3]>= 5.0) and (stock[i][4]>= 5.0) and (stock[i][5]>= 5.0) and
                            (stock[i][6]>= 5.0) and (stock[i][7]>= 5.0) and (stock[i][8]>= 5.0) and
                            (stock[i][9]>= 5.0) and (stock[i][10]>= 5.0) and (stock[i][11]>= 5.0)
                        and (stock[i][12]>= 5.0) and (stock[i][13]>= 5.0) and (stock[i][19]>= 5.0)
                            and (stock[i][20]>= 5.0) and (stock[i][21]>= 5.0)):
                        m += 1
                        textExample.insert(END, f"{str(m)}._{stock[i][1]}\n")

                    i += 1
                textExample.insert(END, f"\nTOTAL: {str(m)}")

            elif comboSesionEspe.get() == "2°Trimestre":
                cursor.execute(f"select *  from primero_bach_dos where año_academico =  '{comboYearEspe.get()}'")
                stock = cursor.fetchall()

                i = 0

                m = 0
                textExample.delete(1.0, END)
                textExample.insert(1.0,f"ALUMNOS APROBADOS EN TODAS "
                                       f"LAS MATERIAS\nCURSO: 1°BACH-CIENCIAS\nAño académico: {comboYearEspe.get()}\nSesión: 2°Trimestre\n\n")

                while i < len(stock):
                    if ((stock[i][3]>= 5.0) and (stock[i][4]>= 5.0) and (stock[i][5]>= 5.0) and
                            (stock[i][6]>= 5.0) and (stock[i][7]>= 5.0) and (stock[i][8]>= 5.0) and
                            (stock[i][9]>= 5.0) and (stock[i][10]>= 5.0) and (stock[i][11]>= 5.0)
                        and (stock[i][12]>= 5.0) and (stock[i][13]>= 5.0) and (stock[i][19]>= 5.0)
                            and (stock[i][20]>= 5.0) and (stock[i][21]>= 5.0)):
                        m += 1
                        textExample.insert(END, f"{str(m)}._{stock[i][1]}\n")

                    i += 1
                textExample.insert(END, f"\nTOTAL: {str(m)}")

            elif comboSesionEspe.get() == "3°Trimestre":
                cursor.execute(f"select *  from primero_bach_tres where año_academico =  '{comboYearEspe.get()}'")
                stock = cursor.fetchall()

                i = 0

                m = 0
                textExample.delete(1.0, END)
                textExample.insert(1.0,f"ALUMNOS APROBADOS EN TODAS "
                                       f"LAS MATERIAS\nCURSO: 1°BACH-CIENCIAS\nAño académico: {comboYearEspe.get()}\nSesión: 3°Trimestre\n\n")

                while i < len(stock):
                    if ((stock[i][3]>= 5.0) and (stock[i][4]>= 5.0) and (stock[i][5]>= 5.0) and
                            (stock[i][6]>= 5.0) and (stock[i][7]>= 5.0) and (stock[i][8]>= 5.0) and
                            (stock[i][9]>= 5.0) and (stock[i][10]>= 5.0) and (stock[i][11]>= 5.0)
                        and (stock[i][12]>= 5.0) and (stock[i][13]>= 5.0) and (stock[i][19]>= 5.0)
                            and (stock[i][20]>= 5.0) and (stock[i][21]>= 5.0)):
                        m += 1
                        textExample.insert(END, f"{str(m)}._{stock[i][1]}\n")

                    i += 1
                textExample.insert(END, f"\nTOTAL: {str(m)}")

            elif comboSesionEspe.get() == "JUNIO":
                cursor.execute(f"select *  from primero_bach_junio where año_academico =  '{comboYearEspe.get()}'")
                stock = cursor.fetchall()

                i = 0

                m = 0
                textExample.delete(1.0, END)
                textExample.insert(1.0, f"ALUMNOS APROBADOS EN TODAS "
                                        f"LAS MATERIAS\nCURSO: 1°BACH-CIENCIAS\nAño académico: {comboYearEspe.get()}\nJUNIO\n\n")

                while i < len(stock):
                    if ((stock[i][3]>= 5.0) and (stock[i][4]>= 5.0) and (stock[i][5]>= 5.0) and
                            (stock[i][6]>= 5.0) and (stock[i][7]>= 5.0) and (stock[i][8]>= 5.0) and
                            (stock[i][9]>= 5.0) and (stock[i][10]>= 5.0) and (stock[i][11]>= 5.0)
                        and (stock[i][12]>= 5.0) and (stock[i][13]>= 5.0) and (stock[i][19]>= 5.0)
                            and (stock[i][20]>= 5.0) and (stock[i][21]>= 5.0)):
                        m += 1
                        textExample.insert(END, f"{str(m)}._{stock[i][1]}\n")

                    i += 1
                textExample.insert(END, f"\nTOTAL: {str(m)}")


        elif comboCursoEspe.get() == "1°BACH-TEC":

            if comboSesionEspe.get() == "1°Trimestre":
                cursor.execute(f"select *  from primero_bach_uno where año_academico =  '{comboYearEspe.get()}'")
                stock = cursor.fetchall()

                i = 0

                m = 0
                textExample.delete(1.0, END)
                textExample.insert(1.0,f"ALUMNOS APROBADOS EN TODAS "
                                       f"LAS MATERIAS\nCURSO: 1°BACH-TECNOLOGIA\nAño académico: {comboYearEspe.get()}\nSesión: 1°Trimestre\n\n")

                while i < len(stock):
                    if ((stock[i][3]>= 5.0) and (stock[i][4]>= 5.0) and (stock[i][5]>= 5.0) and (stock[i][6]>= 5.0) and (stock[i][7]>= 5.0) and
                            (stock[i][8]>= 5.0) and (stock[i][9]>= 5.0) and (stock[i][10]>= 5.0) and (stock[i][11]>= 5.0) and (stock[i][13]>= 5.0) and
                            (stock[i][18]>= 5.0) and (stock[i][19]>= 5.0) and (stock[i][20]>= 5.0) and (stock[i][21]>= 5.0)):
                        m += 1
                        textExample.insert(END, f"{str(m)}._{stock[i][1]}\n")

                    i += 1
                textExample.insert(END, f"\nTOTAL: {str(m)}")

            elif comboSesionEspe.get() == "2°Trimestre":
                cursor.execute(f"select *  from primero_bach_dos where año_academico =  '{comboYearEspe.get()}'")
                stock = cursor.fetchall()

                i = 0

                m = 0
                textExample.delete(1.0, END)
                textExample.insert(1.0,f"ALUMNOS APROBADOS EN TODAS "
                                       f"LAS MATERIAS\nCURSO: 1°BACH-TECNOLOGIA\nAño académico: {comboYearEspe.get()}\nSesión: 2°Trimestre\n\n")

                while i < len(stock):
                    if((stock[i][3]>= 5.0) and (stock[i][4]>= 5.0) and (stock[i][5]>= 5.0) and (stock[i][6]>= 5.0) and (stock[i][7]>= 5.0) and
                            (stock[i][8]>= 5.0) and (stock[i][9]>= 5.0) and (stock[i][10]>= 5.0) and (stock[i][11]>= 5.0) and (stock[i][13]>= 5.0) and
                            (stock[i][18]>= 5.0) and (stock[i][19]>= 5.0) and (stock[i][20]>= 5.0) and (stock[i][21]>= 5.0)):
                        m += 1
                        textExample.insert(END, f"{str(m)}._{stock[i][1]}\n")

                    i += 1
                textExample.insert(END, f"\nTOTAL: {str(m)}")

            elif comboSesionEspe.get() == "3°Trimestre":
                cursor.execute(f"select *  from primero_bach_tres where año_academico =  '{comboYearEspe.get()}'")
                stock = cursor.fetchall()

                i = 0

                m = 0
                textExample.delete(1.0, END)
                textExample.insert(1.0,f"ALUMNOS APROBADOS EN TODAS "
                                       f"LAS MATERIAS\nCURSO: 1°BACH-TECNOLOGIA\nAño académico: {comboYearEspe.get()}\nSesión: 3°Trimestre\n\n")

                while i < len(stock):
                    if ((stock[i][3]>= 5.0) and (stock[i][4]>= 5.0) and (stock[i][5]>= 5.0) and (stock[i][6]>= 5.0) and (stock[i][7]>= 5.0) and
                            (stock[i][8]>= 5.0) and (stock[i][9]>= 5.0) and (stock[i][10]>= 5.0) and (stock[i][11]>= 5.0) and (stock[i][13]>= 5.0) and
                            (stock[i][18]>= 5.0) and (stock[i][19]>= 5.0) and (stock[i][20]>= 5.0) and (stock[i][21]>= 5.0)):
                        m += 1
                        textExample.insert(END, f"{str(m)}._{stock[i][1]}\n")

                    i += 1
                textExample.insert(END, f"\nTOTAL: {str(m)}")

            elif comboSesionEspe.get() == "JUNIO":
                cursor.execute(f"select *  from primero_bach_junio where año_academico =  '{comboYearEspe.get()}'")
                stock = cursor.fetchall()

                i = 0

                m = 0
                textExample.delete(1.0, END)
                textExample.insert(1.0, f"ALUMNOS APROBADOS EN TODAS "
                                        f"LAS MATERIAS\nCURSO: 1°BACH-TECNOLOGIA\nAño académico: {comboYearEspe.get()}\nJUNIO\n\n")

                while i < len(stock):
                    if ((stock[i][3]>= 5.0) and (stock[i][4]>= 5.0) and (stock[i][5]>= 5.0) and (stock[i][6]>= 5.0) and (stock[i][7]>= 5.0) and
                            (stock[i][8]>= 5.0) and (stock[i][9]>= 5.0) and (stock[i][10]>= 5.0) and (stock[i][11]>= 5.0) and (stock[i][13]>= 5.0) and
                            (stock[i][18]>= 5.0) and (stock[i][19]>= 5.0) and (stock[i][20]>= 5.0) and (stock[i][21]>= 5.0)):

                        m += 1
                        textExample.insert(END, f"{str(m)}._{stock[i][1]}\n")

                    i += 1
                textExample.insert(END, f"\nTOTAL: {str(m)}")


        elif comboCursoEspe.get() == "1°BACH-HUM":

            if comboSesionEspe.get() == "1°Trimestre":
                cursor.execute(f"select *  from primero_bach_uno where año_academico =  '{comboYearEspe.get()}'")
                stock = cursor.fetchall()

                i = 0

                m = 0
                textExample.delete(1.0, END)
                textExample.insert(1.0,f"ALUMNOS APROBADOS EN TODAS "
                                       f"LAS MATERIAS\nCURSO: 1°BACH-HUMANIDADES\nAño académico: {comboYearEspe.get()}\nSesión: 1°Trimestre\n\n")

                while i < len(stock):
                    if ((stock[i][3]>= 5.0) and (stock[i][4]>= 5.0) and (stock[i][5]>= 5.0) and (stock[i][6]>= 5.0) and
                            (stock[i][7]>= 5.0) and (stock[i][8]>= 5.0) and
                            (stock[i][9]>= 5.0) and (stock[i][10]>= 5.0) and (stock[i][14]>= 5.0) and
                            (stock[i][15]>= 5.0) and (stock[i][16]>= 5.0) and (stock[i][17]>= 5.0) and
                            (stock[i][20]>= 5.0) and (stock[i][21]>= 5.0)):
                        m += 1
                        textExample.insert(END, f"{str(m)}._{stock[i][1]}\n")

                    i += 1
                textExample.insert(END, f"\nTOTAL: {str(m)}")

            elif comboSesionEspe.get() == "2°Trimestre":
                cursor.execute(f"select *  from primero_bach_dos where año_academico =  '{comboYearEspe.get()}'")
                stock = cursor.fetchall()

                i = 0

                m = 0
                textExample.delete(1.0, END)
                textExample.insert(1.0,f"ALUMNOS APROBADOS EN TODAS "
                                       f"LAS MATERIAS\nCURSO: 1°BACH-HUMANIDADES\nAño académico: {comboYearEspe.get()}\nSesión: 2°Trimestre\n\n")

                while i < len(stock):
                    if ((stock[i][3]>= 5.0) and (stock[i][4]>= 5.0) and (stock[i][5]>= 5.0) and (stock[i][6]>= 5.0) and
                            (stock[i][7]>= 5.0) and (stock[i][8]>= 5.0) and
                            (stock[i][9]>= 5.0) and (stock[i][10]>= 5.0) and (stock[i][14]>= 5.0) and
                            (stock[i][15]>= 5.0) and (stock[i][16]>= 5.0) and (stock[i][17]>= 5.0) and
                            (stock[i][20]>= 5.0) and (stock[i][21]>= 5.0)):
                        m += 1
                        textExample.insert(END, f"{str(m)}._{stock[i][1]}\n")

                    i += 1
                textExample.insert(END, f"\nTOTAL: {str(m)}")

            elif comboSesionEspe.get() == "3°Trimestre":
                cursor.execute(f"select *  from primero_bach_tres where año_academico =  '{comboYearEspe.get()}'")
                stock = cursor.fetchall()

                i = 0

                m = 0
                textExample.delete(1.0, END)
                textExample.insert(1.0,f"ALUMNOS APROBADOS EN TODAS "
                                       f"LAS MATERIAS\nCURSO: 1°BACH-HUMANIDADES\nAño académico: {comboYearEspe.get()}\nSesión: 3°Trimestre\n\n")

                while i < len(stock):
                    if ((stock[i][3]>= 5.0) and (stock[i][4]>= 5.0) and (stock[i][5]>= 5.0) and (stock[i][6]>= 5.0) and
                            (stock[i][7]>= 5.0) and (stock[i][8]>= 5.0) and
                            (stock[i][9]>= 5.0) and (stock[i][10]>= 5.0) and (stock[i][14]>= 5.0) and
                            (stock[i][15]>= 5.0) and (stock[i][16]>= 5.0) and (stock[i][17]>= 5.0) and
                            (stock[i][20]>= 5.0) and (stock[i][21]>= 5.0)):
                        m += 1
                        textExample.insert(END, f"{str(m)}._{stock[i][1]}\n")

                    i += 1
                textExample.insert(END, f"\nTOTAL: {str(m)}")

            elif comboSesionEspe.get() == "JUNIO":
                cursor.execute(f"select *  from primero_bach_junio where año_academico =  '{comboYearEspe.get()}'")
                stock = cursor.fetchall()

                i = 0

                m = 0
                textExample.delete(1.0, END)
                textExample.insert(1.0, f"ALUMNOS APROBADOS EN TODAS "
                                        f"LAS MATERIAS\nCURSO: 1°BACH-HUMANIDADES\nAño académico: {comboYearEspe.get()}\nJUNIO\n\n")

                while i < len(stock):
                    if ((stock[i][3]>= 5.0) and (stock[i][4]>= 5.0) and (stock[i][5]>= 5.0) and (stock[i][6]>= 5.0) and
                            (stock[i][7]>= 5.0) and (stock[i][8]>= 5.0) and
                            (stock[i][9]>= 5.0) and (stock[i][10]>= 5.0) and (stock[i][14]>= 5.0) and
                            (stock[i][15]>= 5.0) and (stock[i][16]>= 5.0) and (stock[i][17]>= 5.0) and
                            (stock[i][20]>= 5.0) and (stock[i][21]>= 5.0)):
                        m += 1
                        textExample.insert(END, f"{str(m)}._{stock[i][1]}\n")

                    i += 1
                textExample.insert(END, f"\nTOTAL: {str(m)}")


        elif comboCursoEspe.get() == "2°BACH-CC":

            if comboSesionEspe.get() == "1°Trimestre":
                cursor.execute(f"select *  from segundo_bach_uno where año_academico =  '{comboYearEspe.get()}'")
                stock = cursor.fetchall()

                i = 0

                m = 0
                textExample.delete(1.0, END)
                textExample.insert(1.0, f"ALUMNOS APROBADOS EN TODAS "
                                        f"LAS MATERIAS\nCURSO: 2°BACH-CIENCIAS\nAño académico: {comboYearEspe.get()}\nSesión: 1°Trimestre\n\n")

                while i < len(stock):
                    if ((stock[i][3]>= 5.0) and (stock[i][4]>= 5.0) and (stock[i][5]>= 5.0) and
                            (stock[i][6]>= 5.0) and (stock[i][7]>= 5.0) and (stock[i][8]>= 5.0) and
                            (stock[i][9]>= 5.0) and (stock[i][10]>= 5.0) and (stock[i][11]>= 5.0)
                        and (stock[i][12]>= 5.0) and (stock[i][13]>= 5.0) and (stock[i][14]>= 5.0)  and (stock[i][22]>= 5.0)):
                        m += 1
                        textExample.insert(END, f"{str(m)}._{stock[i][1]}\n")

                    i += 1
                textExample.insert(END, f"\nTOTAL: {str(m)}")

            elif comboSesionEspe.get() == "2°Trimestre":
                cursor.execute(f"select *  from segundo_bach_dos where año_academico =  '{comboYearEspe.get()}'")
                stock = cursor.fetchall()

                i = 0

                m = 0
                textExample.delete(1.0, END)
                textExample.insert(1.0, f"ALUMNOS APROBADOS EN TODAS "
                                        f"LAS MATERIAS\nCURSO: 2°BACH-CIENCIAS\nAño académico: {comboYearEspe.get()}\nSesión: 2°Trimestre\n\n")

                while i < len(stock):
                    if ((stock[i][3]>= 5.0) and (stock[i][4]>= 5.0) and (stock[i][5]>= 5.0) and
                            (stock[i][6]>= 5.0) and (stock[i][7]>= 5.0) and (stock[i][8]>= 5.0) and
                            (stock[i][9]>= 5.0) and (stock[i][10]>= 5.0) and (stock[i][11]>= 5.0)
                        and (stock[i][12]>= 5.0) and (stock[i][13]>= 5.0) and (stock[i][14]>= 5.0)  and (stock[i][22]>= 5.0)):
                        m += 1
                        textExample.insert(END, f"{str(m)}._{stock[i][1]}\n")

                    i += 1
                textExample.insert(END, f"\nTOTAL: {str(m)}")

            elif comboSesionEspe.get() == "3°Trimestre":
                cursor.execute(f"select *  from segundo_bach_tres where año_academico =  '{comboYearEspe.get()}'")
                stock = cursor.fetchall()

                i = 0

                m = 0
                textExample.delete(1.0, END)
                textExample.insert(1.0, f"ALUMNOS APROBADOS EN TODAS "
                                        f"LAS MATERIAS\nCURSO: 2°BACH-CIENCIAS\nAño académico: {comboYearEspe.get()}\nSesión: 3°Trimestre\n\n")

                while i < len(stock):
                    if ((stock[i][3]>= 5.0) and (stock[i][4]>= 5.0) and (stock[i][5]>= 5.0) and
                            (stock[i][6]>= 5.0) and (stock[i][7]>= 5.0) and (stock[i][8]>= 5.0) and
                            (stock[i][9]>= 5.0) and (stock[i][10]>= 5.0) and (stock[i][11]>= 5.0)
                        and (stock[i][12]>= 5.0) and (stock[i][13]>= 5.0) and (stock[i][14]>= 5.0)  and (stock[i][22]>= 5.0)):
                        m += 1
                        textExample.insert(END, f"{str(m)}._{stock[i][1]}\n")

                    i += 1
                textExample.insert(END, f"\nTOTAL: {str(m)}")

            elif comboSesionEspe.get() == "JUNIO":
                cursor.execute(f"select *  from segundo_bach_junio where año_academico =  '{comboYearEspe.get()}'")
                stock = cursor.fetchall()

                i = 0

                m = 0
                textExample.delete(1.0, END)
                textExample.insert(1.0, f"ALUMNOS APROBADOS EN TODAS "
                                        f"LAS MATERIAS\nCURSO: 2°BACH-CIENCIAS\nAño académico: {comboYearEspe.get()}\nJUNIO\n\n")

                while i < len(stock):
                    if ((stock[i][3]>= 5.0) and (stock[i][4]>= 5.0) and (stock[i][5]>= 5.0) and
                            (stock[i][6]>= 5.0) and (stock[i][7]>= 5.0) and (stock[i][8]>= 5.0) and
                            (stock[i][9]>= 5.0) and (stock[i][10]>= 5.0) and (stock[i][11]>= 5.0)
                        and (stock[i][12]>= 5.0) and (stock[i][13]>= 5.0) and (stock[i][14]>= 5.0)  and (stock[i][22]>= 5.0)):
                        m += 1
                        textExample.insert(END, f"{str(m)}._{stock[i][1]}\n")

                    i += 1
                textExample.insert(END, f"\nTOTAL: {str(m)}")


        elif comboCursoEspe.get() == "2°BACH-TEC":

            if comboSesionEspe.get() == "1°Trimestre":
                cursor.execute(f"select *  from segundo_bach_uno where año_academico =  '{comboYearEspe.get()}'")
                stock = cursor.fetchall()

                i = 0

                m = 0
                textExample.delete(1.0, END)
                textExample.insert(1.0, f"ALUMNOS APROBADOS EN TODAS "
                                        f"LAS MATERIAS\nCURSO: 2°BACH-TECNOLOGIA\nAño académico: {comboYearEspe.get()}\nSesión: 1°Trimestre\n\n")

                while i < len(stock):
                    if ((stock[i][3]>= 5.0) and (stock[i][4]>= 5.0) and (stock[i][5]>= 5.0) and (stock[i][6]>= 5.0) and
                            (stock[i][7]>= 5.0) and (stock[i][8]>= 5.0) and
                            (stock[i][9]>= 5.0) and (stock[i][10]>= 5.0) and (stock[i][11]>= 5.0) and (stock[i][12]>= 5.0)
                        and (stock[i][13]>= 5.0) and (stock[i][14]>= 5.0) and (stock[i][22]>= 5.0)):
                        m += 1
                        textExample.insert(END, f"{str(m)}._{stock[i][1]}\n")

                    i += 1
                textExample.insert(END, f"\nTOTAL: {str(m)}")

            elif comboSesionEspe.get() == "2°Trimestre":
                cursor.execute(f"select *  from segundo_bach_dos where año_academico =  '{comboYearEspe.get()}'")
                stock = cursor.fetchall()

                i = 0

                m = 0
                textExample.delete(1.0, END)
                textExample.insert(1.0, f"ALUMNOS APROBADOS EN TODAS "
                                        f"LAS MATERIAS\nCURSO: 2°BACH-TECNOLOGIA\nAño académico: {comboYearEspe.get()}\nSesión: 2°Trimestre\n\n")

                while i < len(stock):
                    if ((stock[i][3]>= 5.0) and (stock[i][4]>= 5.0) and (stock[i][5]>= 5.0) and (stock[i][6]>= 5.0) and
                            (stock[i][7]>= 5.0) and (stock[i][8]>= 5.0) and
                            (stock[i][9]>= 5.0) and (stock[i][10]>= 5.0) and (stock[i][11]>= 5.0) and (stock[i][12]>= 5.0)
                        and (stock[i][13]>= 5.0) and (stock[i][14]>= 5.0) and (stock[i][22]>= 5.0)):
                        m += 1
                        textExample.insert(END, f"{str(m)}._{stock[i][1]}\n")

                    i += 1
                textExample.insert(END, f"\nTOTAL: {str(m)}")

            elif comboSesionEspe.get() == "3°Trimestre":
                cursor.execute(f"select *  from segundo_bach_tres where año_academico =  '{comboYearEspe.get()}'")
                stock = cursor.fetchall()

                i = 0

                m = 0
                textExample.delete(1.0, END)
                textExample.insert(1.0, f"ALUMNOS APROBADOS EN TODAS "
                                        f"LAS MATERIAS\nCURSO: 2°BACH-TECNOLOGIA\nAño académico: {comboYearEspe.get()}\nSesión: 3°Trimestre\n\n")

                while i < len(stock):
                    if ((stock[i][3]>= 5.0) and (stock[i][4]>= 5.0) and (stock[i][5]>= 5.0) and (stock[i][6]>= 5.0) and
                            (stock[i][7]>= 5.0) and (stock[i][8]>= 5.0) and
                            (stock[i][9]>= 5.0) and (stock[i][10]>= 5.0) and (stock[i][11]>= 5.0) and (stock[i][12]>= 5.0)
                        and (stock[i][13]>= 5.0) and (stock[i][14]>= 5.0) and (stock[i][22]>= 5.0)):
                        m += 1
                        textExample.insert(END, f"{str(m)}._{stock[i][1]}\n")

                    i += 1
                textExample.insert(END, f"\nTOTAL: {str(m)}")

            elif comboSesionEspe.get() == "JUNIO":
                cursor.execute(f"select *  from segundo_bach_junio where año_academico =  '{comboYearEspe.get()}'")
                stock = cursor.fetchall()

                i = 0

                m = 0
                textExample.delete(1.0, END)
                textExample.insert(1.0, f"ALUMNOS APROBADOS EN TODAS "
                                        f"LAS MATERIAS\nCURSO: 2°BACH-TECNOLOGIA\nAño académico: {comboYearEspe.get()}\nJUNIO\n\n")

                while i < len(stock):
                    if ((stock[i][3]>= 5.0) and (stock[i][4]>= 5.0) and (stock[i][5]>= 5.0) and (stock[i][6]>= 5.0) and
                            (stock[i][7]>= 5.0) and (stock[i][8]>= 5.0) and
                            (stock[i][9]>= 5.0) and (stock[i][10]>= 5.0) and (stock[i][11]>= 5.0) and (stock[i][12]>= 5.0)
                        and (stock[i][13]>= 5.0) and (stock[i][14]>= 5.0) and (stock[i][22]>= 5.0)):
                        m += 1
                        textExample.insert(END, f"{str(m)}._{stock[i][1]}\n")

                    i += 1
                textExample.insert(END, f"\nTOTAL: {str(m)}")


        elif comboCursoEspe.get() == "2°BACH-HUM":

            if comboSesionEspe.get() == "1°Trimestre":
                cursor.execute(f"select *  from segundo_bach_uno where año_academico =  '{comboYearEspe.get()}'")
                stock = cursor.fetchall()

                i = 0

                m = 0
                textExample.delete(1.0, END)
                textExample.insert(1.0, f"ALUMNOS APROBADOS EN TODAS "
                                        f"LAS MATERIAS\nCURSO: 2°BACH-HUMANIDADES\nAño académico: {comboYearEspe.get()}\nSesión: 1°Trimestre\n\n")

                while i < len(stock):
                    if ((stock[i][3]>= 5.0) and (stock[i][4]>= 5.0) and (stock[i][5]>= 5.0) and
                            (stock[i][6]>= 5.0) and (stock[i][7]>= 5.0) and (stock[i][8]>= 5.0) and
                            (stock[i][9]>= 5.0) and (stock[i][10]>= 5.0) and (stock[i][15]>= 5.0)
                        and (stock[i][16]>= 5.0) and (stock[i][17]>= 5.0) and (stock[i][18]>= 5.0) and (stock[i][22]>= 5.0)):
                        m += 1
                        textExample.insert(END, f"{str(m)}._{stock[i][1]}\n")

                    i += 1
                textExample.insert(END, f"\nTOTAL: {str(m)}")

            elif comboSesionEspe.get() == "2°Trimestre":
                cursor.execute(f"select *  from segundo_bach_dos where año_academico =  '{comboYearEspe.get()}'")
                stock = cursor.fetchall()

                i = 0

                m = 0
                textExample.delete(1.0, END)
                textExample.insert(1.0, f"ALUMNOS APROBADOS EN TODAS "
                                        f"LAS MATERIAS\nCURSO: 2°BACH-HUMANIDADES\nAño académico: {comboYearEspe.get()}\nSesión: 2°Trimestre\n\n")

                while i < len(stock):
                    if ((stock[i][3]>= 5.0) and (stock[i][4]>= 5.0) and (stock[i][5]>= 5.0) and
                            (stock[i][6]>= 5.0) and (stock[i][7]>= 5.0) and (stock[i][8]>= 5.0) and
                            (stock[i][9]>= 5.0) and (stock[i][10]>= 5.0) and (stock[i][15]>= 5.0)
                        and (stock[i][16]>= 5.0) and (stock[i][17]>= 5.0) and (stock[i][18]>= 5.0) and (stock[i][22]>= 5.0)):
                        m += 1
                        textExample.insert(END, f"{str(m)}._{stock[i][1]}\n")

                    i += 1
                textExample.insert(END, f"\nTOTAL: {str(m)}")

            elif comboSesionEspe.get() == "3°Trimestre":
                cursor.execute(f"select *  from segundo_bach_tres where año_academico =  '{comboYearEspe.get()}'")
                stock = cursor.fetchall()

                i = 0

                m = 0
                textExample.delete(1.0, END)
                textExample.insert(1.0, f"ALUMNOS APROBADOS EN TODAS "
                                        f"LAS MATERIAS\nCURSO: 2°BACH-HUMANIDADES\nAño académico: {comboYearEspe.get()}\nSesión: 3°Trimestre\n\n")

                while i < len(stock):
                    if ((stock[i][3]>= 5.0) and (stock[i][4]>= 5.0) and (stock[i][5]>= 5.0) and
                            (stock[i][6]>= 5.0) and (stock[i][7]>= 5.0) and (stock[i][8]>= 5.0) and
                            (stock[i][9]>= 5.0) and (stock[i][10]>= 5.0) and (stock[i][15]>= 5.0)
                        and (stock[i][16]>= 5.0) and (stock[i][17]>= 5.0) and (stock[i][18]>= 5.0) and (stock[i][22]>= 5.0)):

                        m += 1
                        textExample.insert(END, f"{str(m)}._{stock[i][1]}\n")

                    i += 1
                textExample.insert(END, f"\nTOTAL: {str(m)}")

            elif comboSesionEspe.get() == "JUNIO":
                cursor.execute(f"select *  from segundo_bach_junio where año_academico =  '{comboYearEspe.get()}'")
                stock = cursor.fetchall()

                i = 0

                m = 0
                textExample.delete(1.0, END)
                textExample.insert(1.0, f"ALUMNOS APROBADOS EN TODAS "
                                        f"LAS MATERIAS\nCURSO: 2°BACH-HUMANIDADES\nAño académico: {comboYearEspe.get()}\nJUNIO\n\n")

                while i < len(stock):
                    if ((stock[i][3]>= 5.0) and (stock[i][4]>= 5.0) and (stock[i][5]>= 5.0) and
                            (stock[i][6]>= 5.0) and (stock[i][7]>= 5.0) and (stock[i][8]>= 5.0) and
                            (stock[i][9]>= 5.0) and (stock[i][10]>= 5.0) and (stock[i][15]>= 5.0)
                        and (stock[i][16]>= 5.0) and (stock[i][17]>= 5.0) and (stock[i][18]>= 5.0) and (stock[i][22]>= 5.0)):

                        m += 1
                        textExample.insert(END, f"{str(m)}._{stock[i][1]}\n")

                    i += 1
                textExample.insert(END, f"\nTOTAL: {str(m)}")


        else:
            pass
        connexion.close()

    root.mainloop()


def selecDataBase():
        """
        esta funcion es utliado para seleccionar la direccion de la base de datos
        :return:
        """

        l = ""
        archivo = filedialog.askopenfilename(title="DULA 1.0", initialdir = "c:/")
        if archivo:
            l = archivo

        else:
            l = nameBD.nomBD()


        return l









#avanzado()