#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1
#al 10.
N = 1
while N <= 10:
    for i in range(1, 11):
        print(i * N, end=' \n')
    N = N + 1