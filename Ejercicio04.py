#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener
#unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa
#que pregunte al usuario su edad y sus ingresos mensuales y muestre por
#pantalla si el usuario tiene que tributar o no.
Edad = int(input('Cuantos años tienes: '))
ingresos = int(input('Cantidad de ingresos mensuales: '))
if Edad > 16:
    print('Mayor de 16 años')
elif ingresos >= 1000:
    print('Usted tiene que tributar')
else:
    print('Usted no tiene que tributar')