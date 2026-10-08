temperaturas = [20, 22, 19, 21]

def diferencias_de_temperatura(temperaturas):
    diferencias = []
    for i in range(len(temperaturas) - 1):
        diferencia = temperaturas[i + 1] - temperaturas[i]
        diferencias.append(diferencia)
    return diferencias

print(diferencias_de_temperatura(temperaturas))