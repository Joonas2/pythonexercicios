'''Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''

sair = False
soma = 0
cont = 0

while not sair:
    n = int(input('Digite o valor ou 999 para sair:'))

    if n == 999:
        sair = True
    else:
        soma = soma + n
        cont = cont + 1

print('Foi somados {} numeros e a sua soma foi {}'.format(cont, soma))

