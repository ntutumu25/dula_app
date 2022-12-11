from tkinter import *

def encriptar(texto):
    cod = ""
    for letra in texto:
        if letra in " ":
            cod += ""
        else:
            cod += letra
    return cod
#print(encriptar("hola mundo estoy vivo"))

def elimspace(a):
    """
    esta funciion permite corregir los errores de espacios a la derecha como la izquierda de una cadena de exto
    :param a: el texto
    :return:
    """
    i = 0
    code = ""
    while i < len(a):

        if i == len(a) - 1 and a[len(a) - 1] == " ":
            code += ""
        elif i == 0 and a[0] == " ":
            code += ""
        else:
            code += a[i]

        i += 1
    return code

