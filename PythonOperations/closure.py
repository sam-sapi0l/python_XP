"""
Closure

"""
def criar_saudacao(saudacao, nome):
        def saudar():
            return f'{saudacao}, {nome}!'
        return saudar

s1 = criar_saudacao('Bom dia', 'Josnei')
s2 = criar_saudacao('Boa Noite', 'Josnei')

print(s1())
print(s2())
