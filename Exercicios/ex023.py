'''Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.'''
num = int(input('Digite um numero de 0 a 9999: '))
n = str(num)
print('{} unidades'.format(n[3]))
print('Dezenas {}'. format(n[2]))
print('Centenas'.format(n[1]))
print('Milhar'.format(n[0]))