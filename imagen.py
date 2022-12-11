from tkinter import *


root = Tk()
root.resizable(0,0)
root.title("DULA 1.0-ULTIMO REGISTRO")
root.geometry("500x450")
root.iconbitmap("dula.ico")

#---------la cja de TEXTO-----------------------------
textExample = Text(root, width = 60, height=20,)
textExample.config(bg = "grey85", font=("comic sans ms", 10))
textExample.pack()
#-------------boton de videos---------------------------------

botonImagen = Button(root, text = "ver imagen", command = lambda:imagen(logo2.png))
botonImagen.pack()

botonElim = Button(root, text = "borrar", command = lambda:clear())
botonElim.pack()

#-----BOTON DE CIERRE DE VENTANA----------------------
botonCerrarV = Button(root, text = "cerrar la ventana",
                              command = root.destroy, activebackground="#F50743")
botonCerrarV.config(font=("comic sans ms", 10), bg = "salmon3", cursor = "hand2" )
botonCerrarV.pack(side = "left", anchor = "s")
#---------------funciones---------------------------------

def imagen(s):
    global foto
    foto = PhotoImage(file = f"C:/Users/user/Desktop/untitled/photo/{s}")
    textExample.image_create(1.0, image = foto)
def clear():
    textExample.delete(1.0, "end")



root.mainloop()
