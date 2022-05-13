'''Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''
from statistics import median as md

sair = 'S'
maior = menor = soma = cont = 0

while sair in 'S':
    n = int(input('Digite um valor: '))

    soma = soma + n
    cont = cont + 1

    if maior and menor == 0:
        maior = menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n

    sair = str(input('Deseja continuar S/N:')).upper()


print('\nVoce digitou {} numeros, a media deles foi {:.2f}'.format(cont, media))
print('O numero {} foi o maior'.format(maior))
print('O numero {} foi o menor'.format(menor))