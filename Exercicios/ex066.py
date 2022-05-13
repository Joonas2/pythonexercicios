'''Exercício Python 66: Crie um programa que leia números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).'''

soma = cont = 0

while True:
    n = int(input('Digite um valor ou [999] para sair: '))
    if n == 999:
        break

    soma = soma + n
    cont = cont + 1


print(f'Voce digitou {cont} e a soma deles foi {soma}')
