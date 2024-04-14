# Try, except, else, finally
from os import error

try:
    a = 18
    b = 2
    c = a / b

except ZeroDivisionError as e:
    print('Dvidiu por zero')
except NameError:
    print('Nome não definido')
except TypeError as error:
    print('TypeError')
except IndexError:
    print('IndexError')
except Exception:
    print('Erro desconhecido')

# Try Finally
    
try:
    print(1)
finally:
    print(2)