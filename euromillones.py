#!/usr/bin/env python

from random import randint as aleatorio

def combinacion(num_comb, num_eleg):
    elementos = []
    aux = num_comb
    while aux > 0:
        numero = aleatorio(1,num_eleg)
        if not numero in elementos:
            elementos.append(numero)
            elementos.sort()
            aux = aux - 1
    return elementos

#Imprime los 5 numeros
print "Los 5 numeros son:"
print combinacion(5,50)

#Imprime las 2 estrellas
print "Las estrellas son:"
print combinacion(2,12)
