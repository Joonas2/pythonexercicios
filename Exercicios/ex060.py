'''Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.'''
from math import factorial
num = int(input('Digite um valor: '))
fat = factorial(num)

print('{}! ='.format(num), end=' ')

while num != 0:
    print('{}'.format(num), end=' ')
    print(' x ' if num > 1 else ' = ', end='')
    num = num - 1

print(fat)
