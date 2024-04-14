import sys

# Generator expression, Iterables e Iterators em Python

#iterable = ['Jos', 'Nei', '__iter__']
#iterator = iterable.__iter__() # tem __iter__ e __next__
#lista = [1000]
#generator = {n for n in range(1000)}
#print(sys.getsizeof(lista))
#print(sys.getsizeof(generator))
#
#for n in generator:
#    print(n)
#
#print(generator)


# Introdução às Generator Functions em Python
# Generator = (n for n in range(1000))

def generator(n=0, maximum=10):
    while True:
        yield n # Pausar
        n += 1
        if n > maximum:
            return
        
gen = generator()
for n in gen:
    print(n)