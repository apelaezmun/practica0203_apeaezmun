
frase = input('Escribe una frase: ')
letra = input('Escribe una letra: ')
cantletras = 0
for numletras in frase:
    if numletras == letra:
        cantletras = cantletras +1
print('La frase', frase, 'tiene la letra', letra, 'repetida', cantletras)