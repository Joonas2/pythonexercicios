'''Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'''


num = int(input('Digite um numero: '))
conv = int(input('Deseja converter para qual base: 1) Binario, 2) Octal, 3) hexa: '))


if conv == 1:
    print('o numero {} em binario fica: {}'.format(num, bin(num)[2:]))
elif conv == 2:
    print('O numero {} em octadecimal fica : {}'.format(num, oct(num)[2:]))
else:
    print('O Numero {} em hexadecimal fica {}'.format(num, hex(num)[2:]))
