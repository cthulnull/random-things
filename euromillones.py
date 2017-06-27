#!/usr/bin/env python

from random import randint as aleatorio

#Funcion combinacion, obtiene los numeros aleatorios y los ordena.
def combinacion(num_comb, num_eleg, repetir = False, ordenar = True):
    elementos = []
    aux = num_comb
    while aux > 0:
        numero = aleatorio(1,num_eleg)
        if repetir:
            elementos.append(numero)
            aux = aux - 1
        else:
            if elementos.count(numero) == 0:
                elementos.append(numero)
                aux = aux - 1
    if ordenar:
        elementos.sort()
    return elementos



#Imprime los 5 numeros
print "Los 5 numeros son:"
print combinacion(5,50)

#Imprime las 2 estrellas
print "Las estrellas son:"
print combinacion(2,11)
