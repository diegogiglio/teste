altura = float(input('informe sua altura '))
sexo = str(input('informe o sexo '))
if sexo == 'masculino':
    print(f'seu peso ideal é {(72.7 * altura) - 58}')
elif sexo == 'feminino':
    print(f'seu peso ideal é {62.1 * altura} - 44.7')

