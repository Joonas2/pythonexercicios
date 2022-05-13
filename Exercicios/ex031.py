'''Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.'''

distancia = float(input('Digite a distancia da viagem: '))

'''if distancia <= 200:
    preço = distancia * 0.5
else:
    preço = distancia * 0.45

print('Você ira pagar R${:.2f}'.format(preço))
'''
#forma dois de resolver

preçoDois = distancia * 0.5 if distancia <= 200 else distancia * 0.45
print('R${:.2f}'.format(preçoDois))