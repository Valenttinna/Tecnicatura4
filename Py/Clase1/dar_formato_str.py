
#dar formato a un string
nombre = 'Alvaro'
edad = 30
mensaje_con_formato = 'Mi nombre es %s'%nombre
#%s apunta a tipo string#si hay mas variables tengo que
#poner ()
print(mensaje_con_formato)

mensaje_con_formato = 'Mi nombre es %s y tengo %s años'%(nombre,edad)
print(mensaje_con_formato)

persona = ('Carla','Gomez', 5000.00)
mensaje_con_formato = 'Hola %s %s .Tu Saldo es de: %.2f' %persona
print(mensaje_con_formato)

persona = ('Carla','Gomez', 5000.00)
mensaje_con_formato = 'Hola %s %s .Tu Saldo es de: %.2f'
#en vez del objeto aqui lo ponemos abajo en el print
print(mensaje_con_formato %persona)

sueldo = 30000
mensaje_con_formato = 'Nombre {} Edad {} Sueldo {:.2f}'.format(nombre,edad,sueldo)
#con las llaves marcamos una posicion
#y luego lo sustutuye por el valor de la variable
print(mensaje_con_formato)

mensaje = 'Nombre {0} Edad {1} Sueldo {2:.2f}'.format(nombre,edad,sueldo)
#ahora le pongo el indice
print(mensaje)

mensaje = 'Sueldo {2:.2f} Nombre {0} Edad {1} '.format(nombre,edad,sueldo)
#cambio el orden  simrpe que le de un indice
print(mensaje)

mensaje = 'Nombre {n} Edad {e} Sueldo {s}'.format(n=nombre,e=edad,s=sueldo)
print(mensaje)

diccionario = {'nombre': 'Ivan', 'edad': 35,'sueldo':7000.00}
mensaje = 'Nombre {dic[nombre]} Edad {dic[edad]} Sueldo {dic[sueldo]:.2f}'.format(dic=diccionario)
print(mensaje)