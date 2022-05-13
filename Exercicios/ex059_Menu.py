'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

valorUm = float(input('Digite o primeiro valor: '))
valorDois = float(input('Digite o valor dois: '))

sair = False
while not sair:
    print('-=-'*20)
    print('Menu')
    print('[ 1 ] somar\n' 
          '[ 2 ] multiplicar\n'
          '[ 3 ] maior\n'
          '[ 4 ] novos números\n'
          '[ 5 ] sair do programa')
    opçao = int(input('Escolha um opção: '))
    print('-=-'*20)

    if opçao == 1:
        print('Soma: {} + {} = {}'.format(valorUm, valorDois, valorUm + valorDois))
    elif opçao == 2:
        print('Multiplicação: {} x {} = {}'.format(valorUm, valorDois, valorUm * valorDois))
    elif opçao == 3:
        if valorUm > valorDois:
            maior = valorUm
        else:
            maior = valorDois
        print('Maior: {} e {} é {}'.format(valorUm, valorDois, maior))
    elif opçao == 4:
        valorUm = float(input('Digite o novo de N1 valor: '))
        valorDois = float(input('Digite o novo valor de N2: '))

        print('Os novos valores são {} e {}'.format(valorUm, valorDois))
    elif opçao == 5:
        sair = True

print('FIM!!')
