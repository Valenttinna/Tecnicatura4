import math
from decimal import Decimal

#NaN( NOT A NUMBER)
a = float ('nan') #ejecuta numeros, letras, decimales
print(f'a: {a}')

#modulo math
a = float('nan')
print(f'Es de tipo NaN(not a number)?:  {math.isnan(a)}')

#modulo decimal
a = Decimal('nan')
print(f'Es de tipo NaN(not a number)?:  {math.isnan(a)}')