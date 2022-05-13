'''Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.'''

primeiro = int(input('Digite o primeiro valor da PA: '))
r = int(input('Informe a razão da PA: '))
cont = 1

for i in range(primeiro, 20, r):
  print('a{} = {}'.format(cont, i))
  cont = cont + 1
