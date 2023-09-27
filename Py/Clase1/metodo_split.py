

#help(str.split)
#regrsa una lista de palabras, y utilisa un delimitador
'''
split(self, /, sep=None, maxsplit=-1)
    Return a list of the substrings in the string, using sep as the separator string.

      sep
        The separator used to split the string.

        When set to None (the default value), will split on any whitespace
        character (including \\n \\r \\t \\f and spaces) and will discard
        empty strings from the result.
      maxsplit
        Maximum number of splits (starting from the left).
        -1 (the default value) means no limit.

    Note, str.split() is mainly useful for data that has been intentionally
    delimited.  With natural text that includes punctuation, consider using
    the regular expression module.


Process finished with exit code 0

'''

cursos = 'Java JavaScript Node Py Diseno'
lista_cursos = cursos.split()
print(f'Lista de cursos: {lista_cursos}')
print(type(lista_cursos))

cursos_separados_coma = 'Java,Py,Node,JavaScript,Spring'
lista_cursos = cursos_separados_coma.split(',')
#en este caso le digo cual es el separados
print(f'Lista de cursos: {lista_cursos}')
print(len(lista_cursos))#veo que hay 5 elementos
print(type(lista_cursos))

cursos_separados_coma = 'Java,Py,Node,JavaScript,Spring'
lista_cursos = cursos_separados_coma.split(',',2)
#en este caso le digo cual es el separados y cuantos elementos muestra
print(f'Lista de cursos: {lista_cursos}')
print(len(lista_cursos))#veo que hay 5 elementos
print(type(lista_cursos))