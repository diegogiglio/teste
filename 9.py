salario = int(input('insira o salario '))
emprestimo = int(input('insira emprestimo '))
if emprestimo >= salario * 0.20:
    print('emprestimo não concedido')
else:
    print('emprestimo concedido')
