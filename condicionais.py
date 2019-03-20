idade = input("Qual sua idade?")

def calcula_idade(idade):
    if idade < 18:
        print("Menor de idade")
    elif idade >= 18 and idade <= 60:
        print("Maior de idade")
    elif idade > 60:
        print("Você é um idoso!")


calcula_idade(int(idade))
