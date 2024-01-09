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