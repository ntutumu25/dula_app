import random
"""

print("\n========= ESTA ES TU APLICACION DE ENTRETENIMIENTO===============")
while True:
    adivina = random.randint(1, 7)
    print("\nINGRESA (1) PARA CONTINUAR\nINGRESA (2) PARA SALIR DE LA APLICACION")
    opcion = input(">>")

    #condicion de selecion
    if opcion == "1":
        print("\n**********BIENVENIDO AL JUEGO ADIVINA UN NUMERO**************\n")
        nom_user = input("INTRODUZCA SU NOMBRE: ")
        print("\nMUY BIEN " + nom_user + " ESTOY PENSANDO EN UN NUMERO ENTRE  1 y 7, INTENTA ADIVINARLO")
        print("**********ATENCION!!! SOLO TIENES DERECHO A TRES INTENTOS*************")

        numero = int(input("INTRODUZCA EL NUMERO: "))

        # AHORA EMPIEZA EL CODIGO DEL FUENTE del juego

        if numero == adivina:
            print("\nBRAVOOOOOO ADIVINASTE EN EL PRIMER INTENTO!!!!ERES UN GENIO DEL JUEGO")
        else:
            if numero > adivina:
                print("\nINTENTA CON UN NUMERO MAS PEQUENO AL NUMERO INTRODUCIDO")
            else:
                print("INTENTA CON UN NUMERO MAS GRADE AL NUMERO INTRODUCIDO")
                print("TE FALTAN DOS INTENTOS")
            numero = int(input("INTENTA OTRA VEZ:"))
            if numero == adivina:
                print("BRAVOOOOOO!!!! ADIVINASTE EL NUMERO ERES UN GENIO DEL JUEGO")
            else:
                if numero > adivina:
                    print("\nINTENTA CON UN NUMERO MAS PEQUENO AL NUMERO INTRODUCIDO")
                else:
                    print("\nINTENTA CON UN NUMERO MAS GRADE AL NUMERO INTRODUCIDO")
                    print("TE FALTA UN INTENTO")
                numero = int(input("INTENTA OTRA VEZ:"))
                if numero == adivina:
                    print("BRAVOOOOOO ADIVINASTE EN EL ULTIMO INTENTO!!!! ERES UN GENIO DEL JUEGO")
                else:
                    print("PERDISTE, LO SIENTO MUCHO Y HA SIDO UN PLACER TENERTE AQUI!!")
    if opcion == "2":
        print("\nEL JUEGO SERA DETENIDO EN BREVE, GRACIAS POR LA PARTICIPACION")
        break


"""
"""
adivina = random.randint(1, 4)

print("\n**********BIENVENIDO AL JUEGO ADIVINA UN NUMERO**************\n")
nom_user = input("INTRODUZCA SU NOMBRE: ")
print("\nMUY BIEN " + nom_user + " ESTOY PENSANDO EN UN NUMERO ENTRE  1 y 4, INTENTA ADIVINARLO")
print("**********ATENCION!!! SOLO TIENES DERECHO A TRES INTENTOS*************")

numero = int(input("INTRODUZCA EL NUMERO: "))
i = 3 # inicializacion del contador de los intentos

while i > 1:
    if numero == adivina:
        print("\nBRAVOOOOO HAS ADIVINADO EL NUMERO MAGICO!!!!! ERES UN GENIO DEL JUEGO")
        break
    else:
        print(f"HAS FALLADO EL INTENTO")
    i -= 1
    print(f"\nTE FALTAN {i} INTENTOS")
    numero = int(input("INTENTA OTRA VEZ:"))
if numero == adivina:
    print("")
else:
    print("PERDISTE, LO SIENTO MUCHO Y HA SIDO UN PLACER TENERTE AQUI!!")
print("\n FIN DEL JUEGO MUCHAS GRACIAS POR PARTICIPAR")
"""

##for letra in "hola mundo":
  #  print(letra)

# LISTAS ANIDADAS O LISTA DE DOS DIMENSIONES
""""
mat = [
    [1, 4, 5, 7],
    [0, 1, 8, 10],
    [-1, 8, 9, 7]
]
for matriz in mat:
    print(matriz)
"""

#ARCHIVOS ABRIR Y CERRAR1




