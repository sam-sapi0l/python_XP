idade = int(input("Digite sua idade: "))
if idade >= 0 and idade <= 12:
    print('Crianca')
elif idade > 12 and idade <= 17:
    print('adolescente')
elif idade > 17:
    print('maior de idade')
else:
    print("Numero invalido")