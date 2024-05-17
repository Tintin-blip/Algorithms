# Datos ajustados para alcanzar un estado seguro
DEMANDA = [
    [1, 2, 5, 3],
    [2, 5, 5, 3],
    [5, 5, 4, 3],
    [4, 3, 3, 1],
    [1, 4, 5, 1]
]

ASIGNADOS = [
   [1, 0, 3, 3],
    [0, 1, 0, 3],
    [0, 0, 1, 3],
    [2, 3, 0, 0],
    [0, 1, 3, 0]
]

PARCIAL = [[DEMANDA[i][j] - ASIGNADOS[i][j] for j in range(len(DEMANDA[i]))] for i in range(len(DEMANDA))]
print(DEMANDA),print(ASIGNADOS)
print('RESTA DE DEMANDA Y ASIGNADOS:',PARCIAL)
RECURSOS = [17, 5, 20, 10]

# Calcular los recursos disponibles
DISPONIBLES = [RECURSOS[i] - sum(x[i] for x in ASIGNADOS) for i in range(len(RECURSOS))]
print("Recursos disponibles inicialmente:", DISPONIBLES)

# Número de procesos y recursos
p, r = len(PARCIAL), len(RECURSOS)
print("Número de procesos y recursos:", p, r)

def verificar(indice_proceso, demanda, recursos_disponibles):
    for j in range(len(demanda)):
        print(f"Comparando DEMANDA[{indice_proceso}][{j}]: {demanda[j]} con RECURSOS_DISPONIBLES[{j}]: {recursos_disponibles[j]}")
        if demanda[j] > recursos_disponibles[j]:
            print("¡Se ha detectado que la demanda excede los recursos disponibles!")
            return False  # Si la demanda excede los recursos disponibles, la verificación falla
    return True ## Sino, se envia un True demostrando que si se puede continuar



# inicializo estado seguro
estado_seguro = []
while p > 0: # p >0 para verificar que solo se ejecute mientras hayan procesos disponibles, es decir, la longitud del arreglo de parcial
    seguro = False
    print(f'Procesos restantes: {p}')
    print(f'Estado seguro actual: {estado_seguro}')
    print(f'Recursos disponibles actuales: {DISPONIBLES}')
    
    # Iterando a traves de cada proceso para verificar la seguridad comparando la matriz de demanda(o la parcial en este caso) con la disponible
    for i in range(len(PARCIAL)):
        if PARCIAL[i] != [float('inf')] * r: 
                print(f'\nDEMANDA {PARCIAL[i]}')
                if verificar( i,PARCIAL[i], DISPONIBLES):
               
                    print('PROCESO ACEPTADO, TODAS LAS DEMANDAS SON VALIDAS RECURSOS ACTUALES: ',DISPONIBLES)
                    # Actualizar los recursos disponibles
                    print(f'DEVOLVIENDO AL SISTEMA LOS RECURSOS UTILIZADOS POR {DEMANDA[i]}', 'SERIA:', DISPONIBLES ,'+', ASIGNADOS[i]) ## si la verificacion es correcta se arresignan los valores.
                    DISPONIBLES = [x + y for x, y in zip(DISPONIBLES, ASIGNADOS[i])] ## Sumatoria al sistema, es decir, devolver los valores
                    print(f'Actualizando recursos disponibles: {DISPONIBLES}') 
                    # Marcar el proceso como ejecutado
                    estado_seguro.append(i)
                    PARCIAL[i] = [float('inf')] * r  # Marca como infinito para no volver a ser considerado
                    
                    p -= 1 ## Le asignamos -1 a un p para llevar la cuenta de cuantos procesos se han resuelto con exito
                    seguro = True
                    break  # Romper el ciclo después de ejecutar un proceso
            
    # Si ningun proceso puede ejecutarse, entonces es un estado inseguro
    if not seguro: 
        print("¡El sistema está en un estado inseguro!")
        break

if seguro:
    print("¡El sistema está en un estado seguro!")
    print("Orden de ejecución segura:", estado_seguro)
else:
    print("No se pudo encontrar un estado seguro.")
