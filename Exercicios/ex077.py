'''Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''

palavras = ('Casa', 'Cachorro', 'Maquina', 'Comida', 'Agua', 'esquina')

for p in palavras:#Aqui p ta recebendo a variavel que tem em palavras em cada loop
    print(f'A palavra {p} tem as vogais: ', end='')

    for contador in p: #contador ta dentro da posição do for, então ele vai recer o que P recebeu de palavras
           if contador.lower() in 'aeiou': #Na posição contar tem as vogais
               print(contador, end=' ')

    print('\n')
