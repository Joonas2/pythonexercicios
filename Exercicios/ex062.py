'''Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.'''

a = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
a1 = a
c = 1
t = 0
mais = 10

while mais != 0:
    t = t + mais
    while c != t + 1:
        print('{}'.format(a1), end=' ')
        print('-> ' if c < t else '\n', end='')
        a1 += + r
        c += +1
    mais = int(input('Deseja ver quantos mais termo: '))

print('\nFIM !')
