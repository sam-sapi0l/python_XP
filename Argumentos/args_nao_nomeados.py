"""
args - argumentos nao nomeados
*  - *args (empacotamento e desempacotamento)
"""
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

def soma(*args):
    total = 0
    for numero in args:
        total += numero
        print(numero)


soma(1, 2, 3, 4, 5, 6)