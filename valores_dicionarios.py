# manipulando chaves e valores em dicionários 

pessoa = {}

chave = 'nome'

pessoa[chave] = 'Josnei Pereira'
lista = []

print(pessoa[chave])
print(pessoa)

if pessoa.get('Sobrenome') is None:
    print('Não existe')
else:
    print(pessoa['Sobrenome'])