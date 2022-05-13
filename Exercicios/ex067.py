'''Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo. '''

while True:
    n = int(input('Digite o numero que deseja saber a tabuada: '))
    print('-=-'*20)
    if n < 0:
        break

    for i in range(0, 10):
        print(f'{n} x {i + 1} = {n * (i +1)}')

    print('-=-' * 20)

print('FIM !!!')