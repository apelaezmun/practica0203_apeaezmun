#Escribir un programa que pida al usuario dos números y muestre por pantalla
#su división. Si el divisor es cero el programa debe mostrar un error.
dividendo = float(input('Escribe el numerador: '))
divisor = float(input('Escribe el divisor: '))
if divisor != 0:
    print('El resultado es =', dividendo / divisor)
else:
    print('syntax Error')
