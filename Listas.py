# Primera manera de declarar una lista
primera_lista = list()

# Otra manera de declarar una lista
segunda_lista = ['x', 'y', 'z']

# Tercera manera de declarar una lista
tercera_lista = []

# Agregar valores a la lista
primera_lista.append('a')
primera_lista.append('b')
primera_lista.append('c')
primera_lista.append('d')
primera_lista.append('e')
print primera_lista
# ['a', 'b', 'c', 'd', 'e']

# Seleccionar un elemento de la lista
print primera_lista[0]
# 'a'

# Seleccionar varios elementos de una lista
print primera_lista[2:]
# ['c', 'd', 'e']

# Seleccionar un rango de elementos de una lista
print primera_lista[1:3]
# ['b', 'c']

#Seleccionar ciertos elementos de la lista
print primera_lista[0::2]
# ['a','c']

# Eliminar un elemento de la lista
del primera_lista[4]
print primera_lista
# print ['a', 'b', 'c', 'd']

#Otra manera de eliminar un elemento
primera_lista.remove('d')
print primera_lista
# print ['a', 'b', 'c']

#Cambiar elementos de una lista
 primera_lista[0:2]=[2,5]
 print primera_lista
# print ['2', 'b', '5']

# Obtener el indice de un elemento
primera_lista.index('b')
