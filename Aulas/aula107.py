# Exercicio - Unir Listas
# Crie uma função zipper
# O trabalho dessa função será unir duas listas na ordem
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]


def zipper(lista1, lista2):
        intervalo = min(len(lista1), len(lista2))
        return [(lista1[i], lista2[i]) for i in range(intervalo)]

lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista2 = ['BA', 'SP', 'MG', 'RJ']
print(zipper(lista1, lista2))



