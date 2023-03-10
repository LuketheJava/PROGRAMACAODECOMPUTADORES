#Exemplo 2 - Utilizando Input

#Definindo e puxando variável
nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))

#Visualizar
if idade <= 0:
    print("Sua idade precisa ser maior que 0")
    if idade >= 120:
        print("Sua idade precisa ser menor que 120")
else:
    print(nome,"você tem",idade,"anos")
