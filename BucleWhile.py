#permiten ejecutar un codigo depiendo una condición
i = 1
while i <= 50:
    print(i)
    i = 3*i + 1
print "programa terminado"
#1. Se ejecuta la primera instrucción: i=1 que se usa como variable de control
#2. Se ejecuta el bucle bajo la condición i<=50.
#3. La primer instrucción imprime el valor de i.
#4. A contnuación se modifica la variable de control.
#5. Se repite el bucle, ahora con i=4

#ejemplo 2
numero = int(input("Escriba un número positivo: "))
while numero < 0:
    print("¡Ha escrito un número negativo! Inténtelo de nuevo")
    numero = int(input("Escriba un número positivo: "))
print("Gracias por su colaboración")
