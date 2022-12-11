from tkinter import *
import interface1
#import  ventana_cursos
from tkinter import messagebox
import funciones_notas
import datetime
import avanzado

from tkinter import filedialog
import loguin


#from tkinter import messagebox
#from tkinter.ttk import *

root = Tk()

root.title("DULA 1.0")


root.resizable(1,1)
root.iconbitmap("images/dula.ico")
root.config(bg = "black")
root.geometry("1020x600")
#-------------------labe de la raiz-----------------------






#---------imagen-----------------------------------------------------
"""
logoFondo1 = ""
fondo = PhotoImage(file=logoFondo1)
fondo = fondo.subsample(1, 1)
fondoLabel = Label(root, image=fondo)
fondoLabel.place(x=0, y=0, relwidth=1.0, relheight=1.0)
"""

logo = "images/moi1.gif"

fondo = PhotoImage(file=logo)
fondo = fondo.subsample(1, 1)
fondoLabel = Label(root, image=fondo, bg = "white")
fondoLabel.place(x=0, y=0, relwidth=1.0, relheight=1.0)



logo1 = PhotoImage(file="images/afromedia.png")
labeLogo1 = Label(root, image=logo1)
labeLogo1.place(x = 0, y = 0)

logo = PhotoImage(file = "images/logoTsei.png")
labeLogo = Label(root, image = logo)
labeLogo.pack(side="right", anchor="n")



#----------------botones de root--------------------------------------------------
"""
botonCerrarV = Button(root, text = "cerrar la ventana",
                          command = lambda:cierreV(), activebackground="#F50743")
botonCerrarV.config(font=("comic sans ms", 10), bg = "salmon3", cursor = "hand2" )
botonCerrarV.pack(side = "left", anchor = "s")
"""

#---------label root-----------------------------------------------------
horaLabel = Label(root,text = "")
horaLabel.pack(side = "left", anchor = "s", padx = 10, pady = 50,)
horaLabel.config( font = ("comic sans ms", 14), relief = "sunken", bg = "lightyellow", )

#------ ----------frameFondo------------------------------------------------
frameFondo = Frame(root, width = "300", height = "100")
frameFondo.config(bg = "white")
frameFondo.place(x = 160, y = 0)
#----------------labels frameFondo-------------------------------------------------
#------------------------variable entry--------------------------------------------

#----------label frames fondo------------------------------------------------------



#-----------BOTONES frameFondo--------------------------------------------------
botonRegistro = Button(frameFondo, text = "REGISTRO\nDE\nALUMNOS", width = "11", activebackground="#F50743",
                       command = lambda:interface1.registro(), height = "0")
botonRegistro.config(bg = "white smoke", font = ("comic sans ms", 9), cursor = "hand2", bd = 2)
botonRegistro.grid(row = 0, column = 0, padx = 5, pady = 1, sticky = "w")


botonRegistro = Button(frameFondo, text = "REGISTRO\nDE\nNOTAS", width = "11", activebackground="#F50743",
                        height = "0", command = lambda : loguin.loguin())
botonRegistro.config(bg = "peachpuff", font = ("comic sans ms", 9), cursor = "hand2", bd = 2)
botonRegistro.grid(row = 0, column = 1, padx = 5, pady = 1, sticky = "w")


botonConsultasDisci = Button(frameFondo, text = "CONSULTAS\nDISCIPLINARIAS",height = "3", activebackground="#F50743",
                             command = lambda:interface1.diciplina())
botonConsultasDisci.config(bg = "lightgrey", font = ("comic sans ms", 9), cursor = "hand2", bd = 2)
botonConsultasDisci.grid(row = 0, column = 3, padx = 5, pady = 1, sticky = "w")


botonConsultasNotas = Button(frameFondo, text = "CONSULTAS\nACADÉMICAS", height = "3", activebackground="#F50743",
                             command = lambda:funciones_notas.notas())
botonConsultasNotas.config(bg = "lightblue1", font = ("comic sans ms", 9), width = 13, cursor = "hand2", bd = 2)
botonConsultasNotas.grid(row = 0, column = 2, padx = 5, pady = 5, sticky = "w")

#

#----------------------MENU DE CONFIGURACION-----------------------------------------------------------




menu = Menu(root)
root.config(menu = menu)

#edicion = Menu(menu, tearoff = 0)
#edicion.add_command(label = "configuración avanzada", command = lambda:avanzado.selecDataBase())

avanzadoS = Menu(menu, tearoff = 0)
avanzadoS.add_command(label = "Ver sesiones", command = lambda:avanzado.avanzadoSion())
avanzadoS.add_command(label = "Búsquedas avanzadas", command = lambda:avanzado.buscarAvancada())


ayuda = Menu(menu, tearoff = 0)
ayuda.add_command(label = "Acerca de DULA 1.0", command =lambda :acerca())

#---------opciones de submenus------------------------


#menu.add_cascade(label = "Configuración", menu = edicion)
menu.add_cascade(label = "Avanzado", menu = avanzadoS)
menu.add_cascade(label = "Ayuda", menu = ayuda)


#----------funcion de Acerca de -----------------------------------------------
def acerca():

    root = Toplevel()

    root.title("DULA 1.0 INFO")

    root.resizable(0, 0)
    root.iconbitmap("images/dula.ico")
    root.config(bg="white")
    root.geometry("430x390")

    #---------------lambel imagen----------------
    imagen = PhotoImage(file = "images/aceca.png")
    Label(root, image = imagen, text = "DULA 1.0").pack(pady = 3)

    Label(root, text = "DULA 1.0", font = ("chiller", 24), bg = "yellow" ).place(x = 255, y = 120)

    #----------------FRAMES-------------
    frame = Frame(root)
    frame.config(bg = "white")
    frame.pack(expand = 1, fill = "both", pady = 5, padx = 10)
    #-------label frames -------------------------------


    Label(frame, text="© 2021.NTUTUMU OBONO Fc, todos los derechos reservados\nE-mail: hollprody.j@outlook.com",
          font=("CALIBRI", 8), bg = "white").place(x = 30, y = 170)




    Label(frame, text="Apoyado por:",
          font=("comic sans ms", 10), bg = "white").grid(row=2, column=0, padx=5, pady=5, sticky="e")
    Label(frame, text="AFROMEDIA GE",
          font=("comic sans ms", 10), bg = "white").grid(row=2, column=1, padx=5, pady=2, sticky="W")
    Label(frame, text="Genoveva Ntongono MBO MAYIE",
          font=("comic sans ms", 10), bg = "white").grid(row=3, column=1, padx=5, pady=2, sticky="W")
    Label(frame, text="Gregorio Nsue ASEKO NCHAMA",
          font=("comic sans ms", 10), bg="white").grid(row=4, column=1, padx=5, pady=2, sticky="W")

    Label(frame, text="COLEGAS EAMACINOS",
          font=("comic sans ms", 10), bg = "white").grid(row=5, column=1, padx=5, pady=2, sticky="nW")


    root.mainloop()

#-----------funcion de busquedas avanzadas------------------------------------------





def cierreV():
    """
    funcion de cierre de la ventan con con opcion de messagebox
    :return:
    """
    resultado = messagebox.askyesno("DULA 1.0", "¿SEGURO QUE QUIERES CERRAR LA APLICACIÓN?")
    if resultado:
        root.destroy()

    else:
        pass



def update():
    """
    funcion de alcrualizacion de la hora
    :return:
    """
    fechaHora = datetime.datetime.now()

    horaLabel.config(text = fechaHora.strftime('%H:%M:%S')+ "\n"+fechaHora.strftime('%d/%m/%Y '))

    horaLabel.after(1000, update)



update()


# -----------------funcion pa buscar imagen de fonfo--------------


def abrir():
    """
    archivo = filedialog.askopenfilename(title="SELECCIONAR FOTO")
    if archivo:
        logoFondo = archivo
    else:
        logoFondo = "moi1.gif"
    """
    #logoFondo = "moi1.gif"
    #fondo = PhotoImage(file=logoFondo)
    #fondo = fondo.subsample(1, 1)
    #fondoLabel.config(root, image= "moi1.gif", bg="white")
    #fondoLabel.place(x=0, y=0, relwidth=1.0, relheight=1.0)
    #fondoLabel.after(5000, abrir)


abrir()






root.protocol("WM_DELETE_WINDOW", cierreV) # metodo de asociar la aplicacion con el administrador de ventanas
                                           # es mecanismo de controladores de ventanas
root.mainloop()


