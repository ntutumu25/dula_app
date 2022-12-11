import sqlite3
#import mysql.connector
from tkinter import *



connexion = sqlite3.connect("database1.db")  #crear o abrir la conexion con al base de datos
cursor = connexion.cursor()
#cursor.execute("create table sesion (usuario text unique, nombre_usuario text, password text)")
"""
nombreApellido = "pedro joaquin ondo nututmu obono"
dateN = "10/07/187"
genero = "M"
tutor = "dula obono obama"
telTutor = "222-122-832"
curso ="1°BACH"
avion = [
    (nombreApellido, dateN, genero, curso, tutor, telTutor)
]
"""
#insercion de datos en la tabla
#cursor.executemany("insert into alumno values (null,?,?,?,?,?,?)", avion)

#cursor.execute("update alumno set tutor = 'dula obono obama nfono' where id = 1")
#cursor.execute("select * from alumno ")
#cursor.execute("delete from alumno where id = 3")

#cajaRecepcion = cursor.fetchall()
#for letra in cajaRecepcion:
   #print(letra)
#miConexion.commit() #validation de la insertion de datos
"""
def doc():
    i = 0
    while i < len(cajaRecepcion):

        if i == len(cajaRecepcion) + 1:
            pass
            break
        j = i + 1
        inforegistro = cajaRecepcion[i]
        print(j,"NOMBRE Y APELLIDOS: ",inforegistro[1],"\n  FECHA DE NACIMIENTO: ",  inforegistro[2],"\n  SEXO: ", inforegistro[3],"\n  CURSO: ", inforegistro[4], "\n  TUTOR: ", inforegistro[5], "\n  N°TEL TUTOR: ",inforegistro[6], "\n")
        i += 1
"""
"""
cursor.execute("create table segundo_bach_septiembre (id integer, nombre text, año_academico text, lengua real, historia real,"
               " filosofia real, cns real, economia real, religion real ,frances real,"
               " ingles real, matematicasII real, quimica real, gelogia real, electrotecnia real, mates_aplicadas real, historia_arte real, latin real,"
               "griego real, tecnologia real, dibujo_tecnico real, ef real, informatica real) ")
"""


#cursor.execute(f"delete from segundo_esba_septiembre where nombre = 'FORTUNATO CLEMENTE NTUTUMU OBONO'")
#connexion.commit()


#connexion.close()  #cerrar la conexion con la base de datos

doc = open("images/prueba.rtf", "w")
doc.write("hola mundo")
doc.close()