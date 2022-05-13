'''Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista'''

numeros = list()
for pos in range(0, 5):
    numeros.append(int(input(f'Digite o {pos + 1}º valor: ')))

print(f'O maior valor é {max(numeros)} e está na posição', end=' ')
for pos, valor in enumerate(numeros):
    if valor == max(numeros):
        print(pos, end=' ')

print(f'\nO menor valor é {min(numeros)} e está na posição', end=' ')
for pos, valor in enumerate(numeros):
    if valor == min(numeros):
        print(pos, end=' ')