#!/usr/bin/env python
from random import randint as aleatorio
#Programa para rellenar boleto Euromillones
#Elegir 5 numeros y 2 estrellas

#Variables
a = 1
e = 1
#5 numeros aleatorios
print ("Los 5 numeros son:")
while (a < 6):
    b = aleatorio(1,50)
    a += 1
    print (b)

# 2 estrellas
print ("Las estrellas son:")
while (e < 3):
    h = aleatorio(1,11)
    e += 1
    print (h)
