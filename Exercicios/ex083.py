'''Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''

expre = input('Digite uma expressão: ')

direita = expre.count('(')
esquerda = expre.count(')')

if direita != esquerda:
    print('Expressão invalida')
else:
    print('Expressão valida!')