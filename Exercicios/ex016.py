#Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
'''from math import trunc
num = float(input("Digite um numero: "))
print('Valor digitado foi {} e sua parte inteira é {}'.format(num, trunc(num)))'''

num = float(input('Digite um numero: '))
print('Valor digitado é {} e sua parte inteira é {}'.format(num, int(num)))
