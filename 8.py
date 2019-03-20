nota1 = int(input('insira nota 1'))
nota2 = int(input('insira nota 2'))
if (nota1 and nota2 >= 0) and (nota1 and nota2 <= 10):
#if (nota1 >= 0 and nota1 <= 10) and (nota2 >= 0 and nota2 <= 10):
    print((nota1 + nota2) / 2)
else:
    print('insira nota com valor entre 0 e 10')
