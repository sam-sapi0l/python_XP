# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover / Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Usar as funções decoradoras em outras funções.

def criar_funcao(func):
    def interna(*args, **kwargs):
        for arg in args:
            is_string(arg)
        resultado = func(*args, *kwargs)
        return resultado
    
    return interna


def inverte_string(string):
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')

check_inverte_string = criar_funcao(inverte_string)
invertida = check_inverte_string(123)
print(invertida)