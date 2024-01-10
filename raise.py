# raise - lançando exceções(erros)
def excecao(d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero')

def tipo_do_dado(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'{n} deve ser int ou float'
            f'"{tipo_n.__name__}" enviado.'
        )
    return True


def divide(n, d):
    tipo_do_dado(n)
    tipo_do_dado(d)
    excecao(d)
    return n / d


print(divide(2, 0))