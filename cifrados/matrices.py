import numpy as np

def cifrado(cadena):
    longitud = len(cadena)
    matriz = [[0 for _  in range(2)] for _ in range(int(longitud/2))]
    t = []

    if longitud % 2 != 0:
        longitud = longitud + 1
        cadena = cadena + '.'

    contador = 0
    for i in range(len(matriz)):
        for j in range(2):
            matriz[i][j] = cadena[contador]
            contador = contador + 1
    for j in range(2):
        for i in range(len(matriz)):
            t.append(matriz[i][j])
    return t


def descifrado(cadena):
    longitud = len(cadena)

    contador = 0
    t = [0 for _ in range(int(longitud/2))]

    for i in range(int(longitud/2)):
        t[i] = cadena[i] + cadena[int(longitud/2) + i]

    

    return ''.join(t)



print(descifrado('DB-RCIA-A-YHNPR-NEDRRBTCEOPATCRMSPTO-AAETRE-OOIA'))


print(cifrado('LEONAS'))