a, b = 1, 2
a, b = b, a
print(a, b)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.70,
}

pessoa_completa = {**pessoa}
print(pessoa_completa)

(a1, a2), (b1, b2) = pessoa.items()
print(a1, a2)
print(b1, b2)

for chave, valor in pessoa.items():
    print(chave, valor)


# args e kwargs

def argumentos_nomeados(*args, **kwargs):
    print(kwargs)