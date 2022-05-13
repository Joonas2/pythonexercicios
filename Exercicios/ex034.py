'''Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''

salario = float(input('Digite segu salario: '))

if salario > 1250:
    aumento = salario * (1 + 0.1)
    print('Seu aumento será de 10% ficando com salario de R${:.2f}'.format(aumento))
else:
    aumento = salario * (1 + 0.15)
    print('Seu aumento será de 15% ficando com salario de R${:.2f}'.format(aumento))