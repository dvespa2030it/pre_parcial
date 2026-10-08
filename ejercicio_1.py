lista = [4, 7, 4, 2, 4]
objetivo = 4


def obtener_posiciones(lista, objetivo):
    posiciones = []
    for i in range(len(lista)):
        if lista[i] == objetivo:
            posiciones.append(i)
    return posiciones
print(obtener_posiciones(lista, objetivo))