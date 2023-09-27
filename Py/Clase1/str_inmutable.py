
#help(str.capitalize)
mensaje1 = 'hola mundo'
mensaje2 = mensaje1.capitalize()

print(f'Mesanje 1: {mensaje1}, id: {id(mensaje1)}')
print(f'Mensaje 2: {mensaje2}, id: {id(mensaje2)}')

mensaje1 += ' Adios'
print(f'Mesanje 1: {mensaje1}, id: {id(mensaje1)}')
#Cada que queremos modificar una cadena se genra
#un nuevo objeto, una nueva cadena