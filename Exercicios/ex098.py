'''Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''
from random import randint
from time import sleep
def maior(x):
    m = 0
    if x > m:
        m = x


def gerador():
    for cont in range(0, 6):
        while cont < 6:
            num = randint(0, 9)
            maior(num)
            print(num, end=' ', flush= True)
            cont = cont + 1
            sleep(1)

        print()
gerador()
