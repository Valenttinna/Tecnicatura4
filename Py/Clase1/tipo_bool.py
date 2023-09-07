#Bool contiene los valores de True y False
#Los tipos numericos, es false para el 0(cero), true
#para los demas valores
valor = 0
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')

valor = 3
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')

valor = 0.5
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')

#Tipo String -> False ''. True para demas valores

valor = ''
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')

valor = 'Valentina'
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')

#Tipo Colecciones -> False para colecc. vacias, True para demas colecc.

#Lista --> []
valor = []
resultado = bool(valor)
print(f'valor: {valor}, Resultado vacio: {resultado}')

valor = [2, 3, 4]
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')

#Tuplas --> ()
valor = ()
resultado = bool(valor)
print(f'valor: {valor}, Resultado vacio: {resultado}')

valor = ('Juan','Pedro')
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')

#Diccionario --> {}
valor = {}
resultado = bool(valor)
print(f'valor: {valor}, Resultado vacio: {resultado}')

valor = {'Nombre': 'Juan', 'Apellido': 'Perez'}
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')

#Sentencias de control con bool
#mismo resultado que el tipo String -- vacio = falso
#podemos usar, diccionario, tupla, String
if '':
    print('Regresa verdadero')
else:
    print('Regresa falso')

if 'if relleno':
    print('Regresa verdadero')
else:
    print('Regresa falso')


#CICLOS
variable = 17
while variable:
    print('Regresa verdadero')
    break
else:
    print('Regresa falso')