# dir, hasattr e getattr em Python
string = 'Josnei'
metodo = 'upper'

if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo))
    print(string)
else:
    print('Não existe o método', metodo)