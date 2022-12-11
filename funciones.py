from tkinter import *
import interface1
import sqlite3
import nameBD

#-------------------------funcion de escritura de imagen

#----------------funcion de rescate de informacion en la base de datos Busacar un solo registro------------------

def rescateImagen(l):  # funcion de rescate de la imagen en la tabla alumno
    miConexion = sqlite3.connect(nameBD.nomBD())
    cursor = miConexion.cursor()
    cursor.execute("select * from alumno")
    cajaRecepcion = cursor.fetchall()

    i = 0
    while i < len(cajaRecepcion):

        if i == len(cajaRecepcion) + 1:
            pass
            break

        inforegistro1 = cajaRecepcion[i]
        i += 1
        if l.upper() == inforegistro1[1].upper(): # parametro l del metodo upper()
            avion = inforegistro1[10]
            return avion

# ------------------ gunciones de las notas--------------------------------

def primeroEsba(a):
    """
    esta funcion permite mostrar las notas de primero esba de  un alumno en la tabla treeview
    :param a: nombre del alumno
    :return:
    """
    try:

        connexion = sqlite3.connect(nameBD.nomBD())
        cursor = connexion.cursor()
        cursor.execute(f"select * from primero_esba_uno where nombre = '{a}'")
        stock1 = cursor.fetchall()

        cursor.execute(f"select * from primero_esba_dos where nombre = '{a}'")
        stock2 = cursor.fetchall()

        cursor.execute(f"select * from primero_esba_tres where nombre = '{a}'")
        stock3 = cursor.fetchall()

        cursor.execute(f"select * from primero_esba_junio where nombre = '{a}'")
        stock4 = cursor.fetchall()

        cursor.execute(f"select * from primero_esba_septiembre where nombre = '{a}'")
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

        connexion.close()

        return lista

    except IndexError:
        pass




def segundoEsba(a):
    """
    esta funcion permite mostrar las notas de segundo esba de  un alumno en la tabla treeview
    :param a: nombre del alumno
    :return: lista
    """
    try:

        connexion = sqlite3.connect(nameBD.nomBD())
        cursor = connexion.cursor()
        cursor.execute(f"select * from segundo_esba_uno where nombre = '{a}'")
        stock1 = cursor.fetchall()

        cursor.execute(f"select * from segundo_esba_dos where nombre = '{a}'")
        stock2 = cursor.fetchall()

        cursor.execute(f"select * from segundo_esba_tres where nombre = '{a}'")
        stock3 = cursor.fetchall()

        cursor.execute(f"select * from segundo_esba_junio where nombre = '{a}'")
        stock4 = cursor.fetchall()

        cursor.execute(f"select * from segundo_esba_septiembre where nombre = '{a}'")
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

        connexion.close()

        return lista

    except IndexError:
        pass

