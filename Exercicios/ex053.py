'''Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. '''
frase = str(input('Digite uma frase: ')).strip().lower()
separa = frase.split()
junto = ''.join(separa)
inverso = ''

for i in range(len(junto)-1, -1, -1): #for inverso
    inverso += junto[i] # inverso = inverso + junto[i]

if junto == inverso:
    print('A frase "{}" é um palindromo'.format(frase))
else:
    print('A frase "{}" não é um palindromo'.format(frase))



