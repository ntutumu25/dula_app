from tkinter import *
import sqlite3
import funciones
import nameBD

def UltimoRegistro():
    try:

        root = Toplevel()
        root.resizable(0,0)
        root.title("DULA 1.0-ULTIMO REGISTRO")
        root.geometry("509x400")
        root.iconbitmap("images/dula.ico")
        #-----------frames root------------------------*
        frameText = Frame(root)
        frameText.pack()

        #---------la cja de TEXTO-----------------------------
        textExample = Text(frameText, width = 60, height=20,)
        textExample.config(bg = "grey85", font=("comic sans ms", 10))
        textExample.grid(row = 0, column = 0, padx = 5, pady = 5)

        # ----------scrollbar---------------
        scrollVertical = Scrollbar(frameText, command=textExample.yview)
        scrollVertical.grid(row=0, column=1, sticky="wns", )
        textExample.config(yscrollcommand=scrollVertical.set)

        #-----BOTON DE CIERRE DE VENTANA----------------------
        botonCerrarV = Button(root, text = "cerrar la ventana",
                                  command = root.destroy, activebackground="#F50743")
        botonCerrarV.config(font=("comic sans ms", 10), bg = "salmon3", cursor = "hand2" )
        botonCerrarV.pack(side = "left", anchor = "s")

        def imagen(s):
            global foto
            foto = PhotoImage(file=f"{s}")
            textExample.image_create(1.0, image=foto)
            textExample.insert(END, "\n")

        #-----operacion de lectura de la base de datos y escritura en el widgets Text----------
        miConexion = sqlite3.connect(nameBD.nomBD())
        cursor = miConexion.cursor()
        cursor.execute("select * from alumno ")
        cajaRecepcion = cursor.fetchall()
        textExample.delete(1.0, "end")
        i = 0
        while i < len(cajaRecepcion):

                if i == len(cajaRecepcion) + 1:
                    pass
                    break
                j = i + 1
                inforegistro = cajaRecepcion[i]
                i += 1

        imagen(inforegistro[10])
        if inforegistro[3].upper() == "M":
            textExample.insert(END, "\nALUMNO: "
                                 + inforegistro[1].upper() + "\nFECHA DE NACIMIENTO: "
                                 + inforegistro[2].upper() + "\nSEXO: "
                                 + inforegistro[3].upper() + "\nCURSO: "
                                 + inforegistro[4].upper() + "\nTUTOR/A: "
                                 + inforegistro[5].upper() + "\nN°TEL TUTOR: "
                                 + inforegistro[6].upper() + "\nDIRECCIÓN: "
                                 + inforegistro[7].upper() + "\nPATOLOGÍA GRAVE DE SALUD: "
                                 + inforegistro[8].upper() + "\nESTADO DEL ALUMNO/A: "
                                 + inforegistro[9].upper()+
                               "\nID: "+ str(inforegistro[0]) +
                               "\nN° DE REGISTRO: " +str(j) + "/"+ str(len(cajaRecepcion))+ "\n\n")

        else:
            textExample.insert(END, "\nALUMNA: "
                               + inforegistro[1].upper() + "\nFECHA DE NACIMIENTO: "
                               + inforegistro[2].upper() + "\nSEXO: "
                               + inforegistro[3].upper() + "\nCURSO: "
                               + inforegistro[4].upper() + "\nTUTOR/A: "
                               + inforegistro[5].upper() + "\nN°TEL TUTOR: "
                               + inforegistro[6].upper() + "\nDIRECCIÓN: "
                               + inforegistro[7].upper() + "\nPATOLOGÍA GRAVE DE SALUD: "
                               + inforegistro[8].upper() + "\nESTADO DEL ALUMNO/A: "
                               + inforegistro[9].upper() +
                               "\nID: " + str(inforegistro[0]) +
                               "\nN° DE REGISTRO: " + str(j) + "/" + str(len(cajaRecepcion)) + "\n\n")



        miConexion.close()
        textExample.config( state = 'disabled',)
        #-----------------------------------------------------------------------
        root.mainloop()
    except UnboundLocalError:
        pass


def UltimoRegistro1(): # VENTANA DE ULTIMO REGIDTRO DE LA VENTA REGIDTRO DE DISCIPLINA
    try:

        root = Toplevel()
        root.resizable(0,0)
        root.title("DULA 1.0-ULTIMO REGISTRO")
        root.geometry("509x400")
        root.iconbitmap("images/dula.ico")
        #------------frames---------------------------
        frameText = Frame(root)
        frameText.pack()

        #---------la cja de TEXTO-----------------------------
        textExample = Text(frameText, width = 60, height=20,)
        textExample.config(bg = "grey85", font=("comic sans ms", 10))
        textExample.grid(row = 0, column = 0, padx = 5, pady = 5)
        # ----------scrollbar caja de TEXTO---------------
        scrollVertical = Scrollbar(frameText, command=textExample.yview)
        scrollVertical.grid(row=0, column=1, sticky="wns", )
        textExample.config(yscrollcommand=scrollVertical.set)

        #-----BOTON DE CIERRE DE VENTANA----------------------
        botonCerrarV = Button(root, text = "cerrar la ventana",
                                  command = root.destroy, activebackground="#F50743")
        botonCerrarV.config(font=("comic sans ms", 10), bg = "salmon3", cursor = "hand2" )
        botonCerrarV.pack(side = "left", anchor = "s")



        #-----operacion de lectura de la base de datos y escritura en el widgets Text TABLA DISCIPLINA----------
        miConexion = sqlite3.connect(nameBD.nomBD())
        cursor = miConexion.cursor()
        cursor.execute("select * from disciplina")
        cajaRecepcion = cursor.fetchall()
        textExample.delete(1.0, "end")
        i = 0
        while i < len(cajaRecepcion):

                if i == len(cajaRecepcion) + 1:
                    pass
                    break

                inforegistro = cajaRecepcion[i]
                i += 1
        global stock
        stock = inforegistro[1]
        textExample.insert(END, "\n\nNOMBRE Y APELLIDOS: "
                             + inforegistro[0].upper() + "\nCURSO: "
                             + inforegistro[1].upper() + "\n\nNUMERO DE FALTAS: "
                             + str(inforegistro[2]) + "\nDESCRIPCIÓN DE LA ÚLTIMA FALTA:\n "
                             + inforegistro[3]+"\n")
        stock = inforegistro[0].upper()

        miConexion.close()



        #-------------funcion de imagen------------------------------------------------------------

        def imagen1(s): # FUNCION DE RESCATE DE LA FOTO Y ESCRITURA DE EN LA CAJA DE TEXTO textExample
            global foto
            foto = PhotoImage(file=f"{s}")
            textExample.image_create(1.0, image=foto)
            textExample.insert(END, "\n\n")

        # -----operacion de lectura de la base de datos y escritura en el widgets Text TABLA ALUMNO----------
        miConexion = sqlite3.connect("database1.db")
        cursor = miConexion.cursor()
        cursor.execute("select * from alumno")
        cajaRecepcion = cursor.fetchall() # metodo para meter la informacion de la base de datos a la variable cajaRecepcion


        i = 0
        while i < len(cajaRecepcion):

            if i == len(cajaRecepcion) + 1:
                pass
                break

            inforegistro1 = cajaRecepcion[i]
            i += 1
            if stock.upper() == inforegistro1[1].upper():
                imagen1(inforegistro1[10])

        #-----------------------------------------------------------------------
        textExample.config(state='disabled', )
        miConexion.close()

        root.mainloop()
    except UnboundLocalError:
        pass



