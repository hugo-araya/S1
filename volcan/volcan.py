#!/usr/bin/python3
# -*- coding: utf-8 -*-
# import

def lee_dimension(ar):
    dimension = ar.readline().rstrip('\n').split(' ')
    dimension[0] = int(dimension[0])
    dimension[1] = int(dimension[1])   
    return dimension

def lee_centro(ar):
    centro = ar.readline().rstrip('\n').split(' ')
    centro[0] = int(centro[0])
    centro[1] = int(centro[1])   
    return centro

def str_a_int(linea):
    i = 0
    while i < len(linea):
        linea[i] = int(linea[i])
        i = i + 1
    return linea

def lee_tablero(ar, filas):
    tablero = []
    i = 0
    while i < filas:
        linea = ar.readline().rstrip('\n').split(' ')
        linea = str_a_int(linea)
        tablero.append(linea)
        i = i + 1
    return tablero

def lee_altura(tablero, centro):
    altura = tablero[centro[0]-1][centro[1]-1]
    return altura

def genera_ladera(tablero, altura, dimension):
    fila0 = []
    i = 0
    while i < dimension[0] + 2:
        fila0.append(altura)
        i = i + 1
    ladera =[]
    ladera.append(fila0)
    i = 0
    while i < dimension[0]:
        ladera.append([altura]+tablero[i]+[altura])
        i = i + 1
    ladera.append(fila0)
    return ladera

def leer_datos(nombre):
    ar = open(nombre)
    dimension = lee_dimension(ar)
    centro = lee_centro(ar)
    tablero = lee_tablero(ar, dimension[0])
    altura = lee_altura(tablero, centro)
    ladera = genera_ladera(tablero, altura, dimension) 
    return ladera, centro, altura

def que_paso_vecino(ladera, i, j, altura):
    print (i, j)
    for elem in ladera:
        print(elem)
    
    status = []

    if ladera[i-1][j-1] < altura:
        status.append('X')
    else:
        status.append(ladera[i-1][j-1])

    if ladera[i-1][j] < altura:
        status.append('X')
    else:
        status.append(ladera[i-1][j])

    if ladera[i-1][j+1] < altura:
        status.append('X')
    else:
        status.append(ladera[i-1][j+1])

    if ladera[i][j-1] < altura:
        status.append('X')
    else:
        status.append(ladera[i][j-1])

    if ladera[i][j+1] < altura:
        status.append('X')
    else:
        status.append(ladera[i][j+1])

    if ladera[i+1][j-1] < altura:
        status.append('X')
    else:
        status.append(ladera[i+1][j-1])

    if ladera[i+1][j] < altura:
        status.append('X')
    else:
        status.append(ladera[i+1][j])

    if ladera[i+1][j+1] < altura:
        status.append('X')
    else:
        status.append(ladera[i+1][j+1])

    return status

def estallo_crater(ladera, centro, altura):
    i = centro[0]
    j = centro[1]
    vecinos = que_paso_vecino(ladera, i, j, altura)
    print(vecinos)

def genera_mapa(lava):
    pass

if __name__ == "__main__":
    ladera, centro, altura = leer_datos('VOLCAN.DAT')
    lava = estallo_crater(ladera, centro, altura)
    genera_mapa(lava)


