# reduce - faz um iterável em um valor

from functools import reduce

produtos = [
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 4', 'preco': 60.90},
    {'nome': 'Produto 5', 'preco': 10.00}
]

def funcao_do_reduce(contador, produto):
    print('Contador : ', contador)
    print('Produto : ', produto)
    print()
    return contador + produto['preco']

total = reduce(
    funcao_do_reduce,
    produtos,
    0
)

#total = 0
#for p in produtos:
#    total += p['preco']
#print(total)