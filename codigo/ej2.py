# -*- coding: utf-8 -*-

# Un usuario ingresa 3 números: Encontrar el mayor

num1 = int(input("ingresá el primer número"))
num2 = int(input("ingresá el segundo número"))
num3 = int(input("ingresá el tercer número"))

# <, >, <=, >= -> operadores relacionales
# operadores lógicos (and , or)
if(num1 > num2 and num1 > num3):
    print("El numero 1 {} es el mayor".format(num1))
else:
    if num2 > num3:
        print("El numero 2 {} es el mayor".format(num2))
    else:
        print("El numero 3 " + str(num3) + " es el mayor")
        if(num3 % 2 == 0):
            print("Y además es par")
        else:
            print(" ohhh es impar :( ")

