# Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# Abaixo dele 
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path
try:
    import sys
    sys.path.append('/Users/gabriel.soares/Desktop/')
except ModuleNotFoundError:
    ...

print('Este módulo se chama ', __name__)
print(*sys.path, sep='\n')


# Mais sobre módulos
from sys import path
import packages.modulo


print(*path, sep='\n')