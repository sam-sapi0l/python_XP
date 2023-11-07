nota1 = float(input('Digite sua nota M1: '))
nota2 = float(input('Digite sua nota M2: '))
nota3 = float(input('Digite sua nota M3: '))

media = (nota1 + nota2 + nota3) / 3

if media >= 0 and media <= 4:
    print(f'Nota: {media:.2f},aluno reprovado')
elif media >= 4.1 and media <= 5.9:
    print(f'Nota: {media:.2f}, aluno pegou exame')
elif media >= 6.0 and media <= 10.0:
    print(f'Nota: {media:.2f}, aluno aprovado')
else:
    print('insira notas validas')
    