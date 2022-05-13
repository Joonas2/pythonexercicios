'''Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.'''
n = int(input('Digite o numero: '))
t = int(input('Digite ate qual numero quer multiplicar: '))
for m in range (1, t + 1):
    print('{} x {} = {}'.format(n, m, n * m))
