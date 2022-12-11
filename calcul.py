from tkinter import *

root = Tk() # creacion del objeto de venta
root.title("TSEI/2018 1.0")

#-----------------------hollprody 1.0
#--------------frame principal--------------
principFrame = Frame(root)
principFrame.config(bg = "black")
principFrame.pack(fill = "both", expand = True)



#---------------label------------------------
marcaCalculadora = Label(principFrame, text = "TSEI/2018 1.0")
marcaCalculadora.config(bg = "YELLOW", relief = "groov")
#marcaCalculadora.grid(row = 0, column = 2, padx = 2, pady = 2, columnspan = 4, sticky = "n")
marcaCalculadora.place(x = 10, y = 195)



#--------------- fin label--------------------


#----------------entry---------------------


#pantalla de la calculadora
numeroPatalla = StringVar()

pantalla = Entry(principFrame, textvariable = numeroPatalla)
pantalla.config(justify = "right", width = "30", bg = "black", fg ="green", relief = "groov", bd = 3)
pantalla.grid(row = 1, column = 1, padx = 15, pady = 15, columnspan = 4)
#fin de la panralla
#------------ funcion de pulasar la tecla -----------------------------------
def teclaPulsado(valor):

    numeroPatalla.set(numeroPatalla.get() + valor) # el metodo set pone el valor den pantalla
#-------------------botones-----------------------

# botones de la fila 1---------
boton7 = Button(principFrame, text = "7",  width = "3", height = "0", command = lambda:teclaPulsado("7"))
boton7.config(cursor = "hand2", bg = "tan1")
boton7.grid(row = 2, column = 1,padx = 5, pady = 5, sticky = "ne")

boton8 = Button(principFrame, text = "8",  width = "3", height = "0", command = lambda:teclaPulsado("8"))
boton8.config(cursor = "hand2", bg = "tan1")
boton8.grid(row = 2, column = 2,padx = 5, pady = 5, sticky = "n")

boton9 = Button(principFrame, text = "9",  width = "3", height = "0", command = lambda:teclaPulsado("9"))
boton9.config(cursor = "hand2", bg = "tan1")
boton9.grid(row = 2, column = 3,padx = 5, pady = 5, sticky = "nw")

botonDiv = Button(principFrame, text = "/",  width = "10", height = "2")
botonDiv.config(cursor = "hand2")
botonDiv.grid(row = 2, column = 4,padx = 5, pady = 5, sticky = "nw")

# botones de la fila 2 ----------------------

boton4 = Button(principFrame, text = "4",  width = "3", height = "0", command = lambda:teclaPulsado("4"))
boton4.config(cursor = "hand2", bg = "tan1")
boton4.grid(row = 3, column = 1,padx = 5, pady = 5, sticky = "ne" )

boton5 = Button(principFrame, text = "5",  width = "3", height = "0", command = lambda:teclaPulsado("5"))
boton5.config(cursor = "hand2", bg = "tan1")
boton5.grid(row = 3, column = 2,padx = 5, pady = 5, sticky = "n")

boton6 = Button(principFrame, text = "6",  width = "3", height = "0", command = lambda:teclaPulsado("6"))
boton6.config(cursor = "hand2", bg = "tan1")
boton6.grid(row = 3, column = 3,padx = 5, pady = 5, sticky = "nw")

botonMult = Button(principFrame, text = "x",  width = "10", height = "2")
botonMult.config(cursor = "hand2")
botonMult.grid(row = 3, column = 4,padx = 5, pady = 5, sticky = "nw")
# botones de la 3 fila-------------------------

boton1 = Button(principFrame, text = "1",  width = "3", height = "0", command = lambda:teclaPulsado("1"))
boton1.config(cursor = "hand2", bg = "tan1")
boton1.grid(row = 4, column = 1,padx = 5, pady = 5, sticky = "ne" )

boton2 = Button(principFrame, text = "2",  width = "3", height = "0", command = lambda:teclaPulsado("2"))
boton2.config(cursor = "hand2", bg = "tan1")
boton2.grid(row = 4, column = 2,padx = 5, pady = 5, sticky = "n" )

boton3 = Button(principFrame, text = "3",  width = "3", height = "0", command = lambda:teclaPulsado("3"))
boton3.config(cursor = "hand2", bg = "tan1")
boton3.grid(row = 4, column = 3,padx = 5, pady = 5, sticky = "nw")

botonSum = Button(principFrame, text = "+",  width = "10", height = "2")
botonSum.config(cursor = "hand2")
botonSum.grid(row = 4, column = 4,padx = 5, pady = 5, sticky = "nw")

# botones de la 4 fila -----------------------------
botonIgual = Button(principFrame, text = "=",  width = "3", height = "0", activebackground="#F50743")
botonIgual.config(cursor = "hand2", )
botonIgual.grid(row = 5, column = 1,padx = 5, pady = 5, sticky = "se" )

boton0 = Button(principFrame, text = "0",  width = "3", height = "0", command = lambda:teclaPulsado("0"))
boton0.config(cursor = "hand2", bg = "tan1")
boton0.grid(row = 5, column = 2,padx = 5, pady = 5, sticky = "s" )

botonComa = Button(principFrame, text = ",",  width = "3", height = "0", command = lambda:teclaPulsado(","))
botonComa.config(cursor = "hand2")
botonComa.grid(row = 5, column = 3,padx = 5, pady = 5, sticky = "sw")

botonRes = Button(principFrame, text = "-",  width = "10", height = "2")
botonRes.config(cursor = "hand2")
botonRes.grid(row = 5, column = 4,padx = 5, pady = 5, sticky = "nw")













root.mainloop() # bucle infinito
