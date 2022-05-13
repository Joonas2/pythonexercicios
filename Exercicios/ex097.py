'''Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada
a) de 1 até 10, de 1 em 1  b) de 10 até 0, de 2 em 2  c) uma contagem personalizada'''
from time import sleep

def linha():
    print('~' * 20)

def primeiro():
    for i in range(1, 11):
        print(i, end=' ')
        sleep(1)
    print()
    linha()

def segundo():
    for i in range(10, 0, -2):
        print(i, end=' ')
        sleep(1)
    print()
    linha()

def personalizada():
    i = int(input('Inicio: '))
    f = int(input('Fim: '))
    p =int(input('Passo: '))

    for contador in range(i, f, p):
        print(contador, end=' ')
        sleep(1)
    print()

primeiro()
segundo()
personalizada()

