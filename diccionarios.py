#no tienen indice
d ={'clave1':[1,2,3],
    4:True
}

print d[4]
print d['clave1']

#se puede cambiar el valor de la clave pero no la clave en si
d[4] = False



# Primera manera de declarar un diccionario
primer_diccionario =  dict()

# Segunda manera de declarar un diccionario
segundo_diccionario = {'key_1': 'valor_1','key_2': 'valor_2','key_3': 'valor_3','key_4': 'valor_4'}

# Tercera manera de declarar un diccionario
tercer_diccionario = {}

# Agregar nuevo valor al diccionario
primer_diccionario['otro_key'] = 'otro_valor'
print primer_diccionario
# {'otro_diccionario': 'otro_valor'}

# Mostrar el valor del diccionario
print primer_diccionario['otro_key']
# 'otro valor'

# Eliminar un valor del diccionario
del primer_diccionario['otro_key']
print primer_diccionario
# {}
