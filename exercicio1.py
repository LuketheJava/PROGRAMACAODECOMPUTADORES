#Calcular total do salário

salariohora = float(input("Digite quanto você recebe por hora:"))
numerodehoras = float(input("Digite o número de horas que trabalhas:"))

#Executa o calculo
salariototal = round(float((salariohora*numerodehoras)),2)

#Visualizar
print("\nSeu salário por hora é:",salariohora,"\nSeu número de horas trabalhadas é:",numerodehoras,"\nSeu salário total é:",salariototal)