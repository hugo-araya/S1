#!/usr/bin/python3
# -*- coding: utf-8 -*-

#import <biblioteca>

def datos(linea):
    lista = linea.split(' ')
    x = int(lista[0])
    y = int(lista[1])  
    return [x, y]

def invertir(palabra, dimension):
    pal = ''
    i = -1
    while i >= dimension[1]:
        pal = pal + palabra[i]
        i = i - 1
    return pal

def lectura_datos(nombre):
    ar = open(nombre)
    tablero = []
    palabras = []
    dimension = datos(ar.readline().rstrip('\n'))
    i = 0
    while i< dimension[0]:
        linea = ar.readline().rstrip('\n')
        tablero.append(linea)
        i = i + 1
    cantidad = int(ar.readline().rstrip('\n'))
    i = 0
    while i < cantidad:
        linea = ar.readline().rstrip('\n')
        palabras.append(linea)
        i = i + 1
    ar.close()
    return tablero, palabras, dimension 

def izq_der(tablero, palabra):
    for linea in tablero:
        if palabra in linea:
            return('Esta')
    return('No esta')

def der_izq(tablero, palabra, dimension):
    palabra = invertir(palabra, dimension)
    for linea in tablero:
        if palabra in linea:
            return ('Esta')
    return ('No esta')

def proceso(tablero, palabras, dimension):
    for palabra in palabras:
        resultado = izq_der(tablero, palabra)
        print(palabra, resultado)
        resultado = der_izq(tablero, palabra, dimension)
        print(invertir(palabra, dimension), resultado)
        print("---------------------------")

def genera_solucion(solucion):
    pass

if __name__ == '__main__':
    tablero, palabras, dimension = lectura_datos('SOP.DAT')
    solucion = proceso(tablero, palabras, dimension)
    genera_solucion(solucion)
