'''Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
 em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.'''

frase = str(input('Digite uma frase: ')).strip()
print('Letra "A" aparece {} vezes'.format(frase.lower().count('a')))
print('Primeira vez na posição {}'.format(frase.lower().find('a')))
print('Ultima vez na posição {}'.format(frase.lower().rfind('a')))