'''Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e
peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.'''
from random import randint
from time import sleep

computador = randint(0, 5)
usuario = int(input('Digite o numero de 0 a 5 que o computador pensou: '))
print('-=-'*20)
print('Processando...')
print('-=-'*20)

sleep(3)

if usuario == computador:
    print('Venceu')
else:
    print('Perdeu')

print('O computador pensou no numero {} e você digitou {}'.format(computador, usuario))
