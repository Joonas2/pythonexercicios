'''Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.'''

a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão: '))
c = 1
an = a1

while c != 11:
   print('a{} = {}'.format(c, an))
   c += + 1
   an = a1 + ((c - 1) * r)

