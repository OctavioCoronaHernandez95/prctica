#Un bucle for es un bucle que repite el bloque de instrucciones un número
#predeterminado de veces. El boque de instrucciones,
print("Comienzo")
for i in [3, 4, 5]:
    print("Hola. Ahora i vale", i, "y su cuadrado", i ** 2)
print("Final")
#Los valores de la variable no son importantes. Lo que importa es que
#tiene tres elementos, por tanto el bucle se ejecutara tres veces.

#La variable de control i puede ser una valiable empleada antes del bicle.
#El valos que tenga no afecta la ejecucion del bucle, pero al terminar el
#bucle, i conserva el último valor asignado.
i = 10
print("El bucle no ha comenzado. Ahora i vale", i)

for i in [0, 1, 2, 3, 4]:
    print(i, "*", i,"=", i ** 2)

print("El bucle ha terminado. Ahora i vale", i)

#Se puede usar una cadena y la variable tomará el valor de cada uno de Los
#carácteres
for i in "AMIGO":
    print("Dame una ", i)
print("¡AMIGO!")

#imprime tres veces Hola
print("Comienzo")
for i in range(3):
    print("Hola ", end="")
print()
print("Final")

#el num de iteraciones lo elige el usuario
veces = int(input("¿Cuántas veces quiere que le salude? "))
for i in range(veces):
    print("Hola ", end="")
print()
print("Adios")
