"""

Listas de listas e seus indices

"""

salas = [

    ['Zero', 'Um',],
    ['Dois', ],
    ['Tres', 'Quatro', 'Cinco', (0, 10, 20, 30, 40)]
]

for sala in salas:
    for aluno in sala:
        print(aluno)
