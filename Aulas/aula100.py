import copy
from dados import produtos


novos_produtos = [
    
    p for p in copy.deepcopy(produtos)
        
]

#print(*produtos, sep='\n')
#print()
#print(*novos_produtos, sep='\n')

ordem_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['preco']
)

ordem_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome']
)

print(*produtos, sep='\n')
print()
print(*novos_produtos, sep='\n')
print()
print(*ordem_nome, sep='\n')
print()
print(*ordem_preco, sep='\n')
