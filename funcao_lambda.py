# Função lambda em Python
# A função lambda é uma função como qualquer
# Outra em Python. Porém são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única expressão

lista = [
    {'nome': 'Josnei', 'sobrenome': 'Pereira'},
    {'nome': 'Chad', 'sobrenome': 'Chungus'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Pedro', 'sobrenome': 'Roberto'},
    {'nome': 'Bob', 'sobrenome': 'Shell'},

]

sorted(lista, key=lambda item: item['nome'])
print(lista)


###########

def executa(funcao, *args):
    return funcao(*args)

def soma(x, y):
    return x + y

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica