# Dictionary comprehension e Set Comprehension
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'Categoria': 'Escritório',
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
    if chave != 'categoria'
}

lista = [
    ('a', 'valor a'),
    ('a', 'valor a'),
    ('a', 'valor a'),
]

dc = {
   chave: valor
   for chave, valor in lista 
}
print(dict(dc))


s = {2 ** i for i in range(10)}

print(s)