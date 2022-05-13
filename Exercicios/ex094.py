'''Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média'''

dados = dict()
pessoas = list()
continuar = 's'
media = soma = 0

while continuar not in 'n':
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo M/F: ')).lower()
    dados['idade'] = int(input('Idade: '))
    pessoas.append(dados.copy())
    continuar = str(input('Deseja continuar [S/N]: ')).lower()
print()

'''A) Quantas pessoas foram cadastradas'''
print(f'Foram cadastradas: {len(pessoas)} pessoas')

'''B) A média de idade'''
for p in range(0, len(pessoas)):
    soma = soma + pessoas[p]['idade']
media = soma/len(pessoas)
print(f'A media de idade é {media:.2f}')

'''C) Uma lista com as mulheres'''
