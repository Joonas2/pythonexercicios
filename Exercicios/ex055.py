'''Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.'''
gordo = 0
magro = 0

for i in range(0, 3):
    peso = float(input('{}) Digite seu peso: '.format(i + 1)))

    if i == 0: #to adicionando o primeiro peso ao gordo e magro
        magro = peso
        gordo = peso
    else:
       if peso > gordo:
           gordo = peso
       if peso < magro:
           magro = peso

print('Maior peso é {}'.format(gordo))
print('Menor peso é {}'.format(magro))



