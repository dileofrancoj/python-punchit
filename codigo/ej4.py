# -*- coding: utf-8 -*-

#2) Ingresar números hasta que el último sea cero. Calcular la cantidad de positivos.
numero = 1
cantPositivos = 1

while numero != 0:
    numero = int(input("Ingresá un número"))
    if(numero > 0):
        cantPositivos = cantPositivos + 1

print("Escribiste: {} numeros positivos".format(cantPositivos - 1))

    