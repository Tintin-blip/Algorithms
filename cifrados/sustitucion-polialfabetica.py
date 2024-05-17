import numpy as np

palabra = 'LA-CASA'
clave = 'CASA'

lp = len(palabra)
lc = len(clave)

if(lp % 2 != 0):
    lp = lp + 1
lp = int(lp)
filas = lp // lc
mitad = lp // 2

matriz = np.zeros([filas, mitad])
palabrasindex = []
for i in range(len(palabra)):
    palabrasindex.append(i)

for i in range(filas):
    for j in range(mitad):
        if j < len(palabrasindex):
            matriz[i][j] = palabrasindex[j]

for j in range(mitad):
    if j + mitad < len(palabrasindex):
        matriz[filas - 1][j] = palabrasindex[j + mitad]


texto_cifrado ='HSQPECAYIWACZPQOAEIVRWOUCSQGECCE'
clave_invertida = ''.join(sorted(clave))

# Encontrar los índices originales
indices_originales = np.argsort(list(clave_invertida))

# Descifrar el texto
texto_descifrado = ''
for row in matriz:
    for index in row:
        if int(index) < len(texto_cifrado):
            texto_descifrado += texto_cifrado[int(index)]
        else:
            break

print("Texto descifrado:", texto_descifrado)