#Escribir un programa que pida al usuario un número entero y muestre por
#pantalla un triángulo rectángulo que tenga tantas líneas como el número
#introducido, como el triángulo de más abajo.
#1
#3 1
#5 3 1
#7 5 3 1
#9 7 5 3 1
num = int(input('Escribe un numero: '))
for i in range(1, num +1, 2):
    for h in range(i, 0, -2):
        print(h, end='\n')
