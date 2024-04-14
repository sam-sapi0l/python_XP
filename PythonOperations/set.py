s = set('Josnei') 
s = set() # vazio
s = {'Josnei', 1, 2, 3}  #com dados

print(s)

# Métodos úteis:
# add, update, clear, discard

s1 = set()
s1.add('Josnei')
s1.add(1)
s1.update('Pereira')
#s1.clear()
s1.discard('Pereira')
print(s1)


# Operações úteis
# união | união (union) - Une
# intersecção % (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em amboas

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
s3 = s1 & s2
s3 = s2 - s1
s3 = s1 ^ s2
print(s3)