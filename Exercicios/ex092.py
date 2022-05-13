'''Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''
from datetime import datetime
pessoa = dict()

pessoa['nome'] = str(input('Digite seu nome: '))
anoNascimento = int(input('Ano de nascimento: '))
pessoa['idade'] = datetime.now().year - anoNascimento
pessoa['ct'] = int(input('Carteira de Trabalho (0 se não tiver): '))

if pessoa['ct'] == 0:
    pessoa['ct'] = str('Não tem cateira de trabalho')
    for k, v in pessoa.items():
        print(f'O {k} tem o valor {v}')
else:
    pessoa['contrato'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salario: '))
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['contrato'] + 35) - datetime.now().year)

for k, v in pessoa.items():
    print(f'O {k} tem o valor {v}')
