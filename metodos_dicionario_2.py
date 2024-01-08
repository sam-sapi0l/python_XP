# Mais métodos com dicionários.
import copy


d1 = {
    'C1': 1,
    'C2': 2,
    'lista 1': [0, 1, 2],
}
d2 = copy.deepcopy(d1)


d2 = d1
d2['C1'] = 9999
d2['lista 1'][1] = 2000

print(d1)
print(d2)