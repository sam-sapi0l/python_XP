p1 = {
    'nome': 'Josnei',
    'sobrenome': 'Pereira',    
}

print(p1.get('nome', 'Não Existe'))

# .pop elimina chave do dicionario

nome = p1.pop('nome')
print(nome)
print(p1)

# .popitem exclui a ultima chave do dicionario

ultima_chave = p1.popitem()
print(ultima_chave)
print(p1)

#update atualiza valor da chave atual e cria uma nova chave
p1.update({
    'nome': 'Josnei',
    'idade': 24,
})
print(p1)

# update alternativo
tupla = ('nome', 'Josnei'), ('idade', 24)
p1.update(tupla)
print(p1)