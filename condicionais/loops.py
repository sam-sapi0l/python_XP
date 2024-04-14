<<<<<<< HEAD
nota1 = int(input('Nota 1: '))
nota2 = int(input('Nota 2: '))
nota3 = int(input('Nota 3: '))
nota4 = int(input('Nota 4: '))
nota5 = int(input('Nota 5: '))

media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

for nota in media:
    if media >= 0 and media <= 4.0:
        print('reprovado')
    elif media > 4.1 and media <= 6.0:
        print('pegou exame')
        exame = int(input('Nota Exame: '))
        while media > 4.1 and media <= 6.0:
            print('aluno reprovado no exame')
    elif media > 6.0 and media <= 10.0:
        print('aluno aprovado')
=======
nota = media = soma = 0

for _ in range(1,6):
    nota = float(input('Digite a nota: '))
    soma += nota

print(soma)
>>>>>>> 0139af2e3f1114380ece7e4b37508b7417609c00
