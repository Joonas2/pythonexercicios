'''Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

dados = list()
pessoas = list()
gordo = magro = 0

while True:
    dados.append(str(input('Digite seu nome: ').strip()))
    dados.append(float(input('Seu peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    continuar = str(input('Deseja continuar [S/N] ? ')).lower()

    if continuar in 'n':
        break

for pos, kg in enumerate(pessoas):
    if pos == 0:
        gordo = gordo + kg[1]
        magro = magro + kg[1]
    else:
        if kg[1] >= gordo:
            gordo = kg[1]
        elif kg[1] < magro:
            magro = kg[1]


print(f'Foram cadastras {len(pessoas)}')
print(f'O maior peso foi {gordo} kg da pessoa', end=' ')
for p in pessoas:
    if p[1] == gordo:
        print(f'{p[0]}')
print(f'O menor peso foi {magro}kg da pessoa', end=' ')
for p in pessoas:
    if p[1] == magro:
        print(f'{p[0]}')


