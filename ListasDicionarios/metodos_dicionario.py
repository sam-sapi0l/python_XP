pessoa = {
    'nome': 'Josnei',
    'Sobrenome': 'Pereira',
    'Idade': 900,
}

pessoa.setdefault('idade', 0)

print(pessoa['Idade'])
print(len(pessoa))
print(list(pessoa.keys()))
print(list(pessoa.values()))
print(list(pessoa.items()))