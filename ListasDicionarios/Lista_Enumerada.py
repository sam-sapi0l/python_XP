"""
Tipo Tuplas = Lista Imutável

"""

numeros = [1, 2, 3, 4]
_,_, numero, *resto = numeros
print(numeros)


"""
Listas Enumeradas - Enumerate = enumera iteráveis(índices)

"""


lista = [1, 2, 3]
lista.append(4)

for indice, numero in enumerate(lista):
    print(indice, numero, lista[indice])
