'''Exercício Python 29: Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.'''

velocidade = int(input('Digite a velocida que o veiculo passou: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Voce ira pagar uma multa de {}'.format(multa))
else:
    print('Velocidade permitida, boa viagem !')
