lista = [10, 2, 1, 30, 4, 1]
objetivo = 1

def obtener_posiciones(lista, objetivo):
    posiciones = []
    for i in range(len(lista)):
        if lista[i] == objetivo:
            posiciones.append(i)
    return posiciones
print(obtener_posiciones(lista, objetivo))