#Exemplo 3 calcular - Utilizando Input

#Definindo e puxando variável
n1 = float(input("Digite o primeiro número:"))
n2 = float(input("Digite o segundo número:"))

soma = n1+n2
subtrair = n1-n2
divisao = n1/n2
multiplicar = n1*n2
restodivisao = n1%n2

#Visualizar e funções

if n1 < 0:
    print("Digite o primeiro número maior ou igual a zero")
if n2 < 0:
    print("Digite o segundo número maior ou igual a zero")
else:
    print("\nO Primeiro número é:",n1,"\nO Segundo número é:",n2,"\nA soma dos dois números é:",soma,"\nA subtração dos dois números é:",subtrair,"\nA divisão dos dois números é:",divisao,"\nA multiplicação dos dois números é:",multiplicar,"\nO resto da divisão é:",restodivisao)
#Visualizar e funções
