'''Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo'''
num = int(input('Digite um numero: '))
primo = 0
cont = 0

for i in range(1, num + 1):
        if num % i == 0:
            print('\033[32m {}\033[m'.format(i), end='')
            primo = primo + 1
        else:
            print('\033[31m {}\033[m'.format(i), end='')


print('\n')

if primo == 2:
    print('{} foi dividido {}, então é um numero primo'.format(num, primo))
else:
    print('O {} foi divido {} vezes, então ele não é um numero primo'.format(num, primo))
