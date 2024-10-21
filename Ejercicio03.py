#Escribir un programa que pida al usuario un número entero y muestre por
#pantalla si es par o impar.
num = int(input('Escribe un numero: '))
if num % 2 != 0:
    print('Numero impar')
else:
    print('Numero par')