
#help(str.join)

tupla_str = ('Hola','alumnos','Tecnicatura','Universitaria')

mensaje = ' '.join(tupla_str)
print(f'Mensaje: {mensaje}')


lista_curso = ['Java','Py','Angular','Spring']
mensaje = ','.join(lista_curso)
print(f'Mensaje: {mensaje}')

cadena = 'HolaMundo'
mensaje = '.'.join(cadena)
print(f'Mensaje: {mensaje}')

diccionario = {'nombre': 'Juan', 'apellido': 'Perez','edad':'20'}
#el numero 20 de valor de edad tiene estar tipo string, no numerico
llaves = '-'.join(diccionario.keys())
valores = '-'.join(diccionario.values())
print(f'Llaves: {llaves}, Type: {type(llaves)}')
print(f'Valores: {valores}, Type: {type(valores)}')


