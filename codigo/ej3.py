# -*- coding: utf-8 -*-

semana = 1
GastoTotal = 0
while semana<=4:
    gasto = int(input("cuanto gastaste esta semana?"))
    GastoTotal = GastoTotal + gasto
    semana += 1 #es lo mismo que decir "semana=semana+1"
print("El promedio de gasto semanal es: {}".format(GastoTotal/(semana-1)))