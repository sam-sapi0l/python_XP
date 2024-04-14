'''
Funções Recursivas

'''

def recursiva(inicio=0, fim=4):
    print(inicio, fim)

    #Caso base
    if inicio >= 4:
        return fim

    # Caso recursivo
    inicio += 1
    return recursiva(inicio, fim)
print(recursiva())


#######


# Fatorial de 5

def fatorial(n):
    if n <= 0:
        return 1
    
    return n * fatorial(n -1)
print(fatorial(5))