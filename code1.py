"""""
def  suma (s1, s2, s3):
    resul=s1+s2+s3
    print(f"SUMA: {resul}")

suma(19,7,8)
print("********TABLA DE MULTIPLICACION********\n  INTRODUZCA EL NUMERO QUE DESEA")
numero=int(input())
print(f"1 x {numero} = {1*numero}\n2 x {numero} = {2*numero}\n3 x {numero} = {3*numero}\n4 x {numero} = {4*numero}\n5 x {numero} = {5*numero}\n6 x {numero} = {6*numero}\n7 x {numero} = {7*numero}\n8 x {numero} = {8*numero}\n9 x {numero} = {9*numero}\n10 x {numero} = {10*numero}\n")
"""
""""
numero = 10
numero1 = 23
numero3 = numero > numero1
print(numero3)
"""

""
#  a, b, r = 87, 9, 0
# print(b, r, a)
"""""
alumnos = 98
cadena = "Tenemos " + str(alumnos) + " alumnos en el CENTRO PRIVADO ENEM"
print(cadena)

cadena1 = "tenemos {}  alumnos en el CENTRO PRIVADO ENEM".format(alumnos)
print(cadena1)
"""
# INTRODUCIR texto
# mi_nombre = input("IGRESE TU NOMBRE: ")

#LISTAS : una lista es una collecion de elemento
"""
frutas = ["mango", "appel", "aguacate","naranja", "platano", 78]
type(frutas)
print(type(frutas))
print(frutas[3])
print(f"{frutas, frutas[0:4]} lo tengo" )
"""
#funcione de las listas
"""
1. list : es para crear una lista exp: list = frutas(())
2 len : la longitud de una lista exp : len(frutas)
3. append : nos permite anadir un elemento de la lista, exp: frutas.append("algo")
4 extend : unir dos listas en una sola exp : lista.extend
"""
# FUNCIONE
#def saludar():
 #   print("quien esta ahi")
 # el mayor de tres numero
 """
def mayor_num(num1, num2, num3):
     if num1 >= num2 and num1 >= num3:
       return num1
     if num2 >= num1 and num2 >= num3:
         return num2
     else:
         return num3


a = float(input("INTRODUZCA EL PRIMER NUMERO: "))
b = float(input("INTRODUZCA EL PRIMER NUMERO: "))
c = float(input("INTRODUZCA EL PRIMER NUMERO: "))
print(f"EL MAYOR NUMERO DE ESTOS TRES NUMEROS {a, b, c}  ES: {mayor_num(a, b, c)}")
"""

# JUEGO DE ADIVINA UN NUMERO

# import random
# random.randint(a, b), es la funcion para generar numero aleatorios
