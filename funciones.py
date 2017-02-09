#Tener presente que los parámetros de nuestra función 'multiplica_numeros' son a b y c
#Creamos nuestra lista en orden

def multilpica_numeros(a, b, c):
    return a*b*c

parametros = list()
parametros.append(2) # Sera el parametro de a
parametros.append(3) # Sera el parametro de b
parametros.append(6) # Sera el parametro de c

# Para asignarle la lista a la funcion se debe agregar un asterisco
multiplica_numeros(*parametros)
# La respuesta es 36
