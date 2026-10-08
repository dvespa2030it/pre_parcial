entrada = [4, 2, 4, 7, 2, 9]
salida = [4, 2, 7, 9]

def eliminar_repetidos(entrada):
    lista_sin_repetidos = []
    for elemento in entrada:
        if elemento not in lista_sin_repetidos:
            lista_sin_repetidos.append(elemento)
    return lista_sin_repetidos

print(eliminar_repetidos(entrada))