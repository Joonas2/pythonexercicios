'''Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

produtos = ('Lapis', 1.50, 'caneta', 2.00, 'Apontador', 0.50, 'Borracha', 0.70, 'Caderno', 15.00)

for c in range(0, len(produtos)):
    if c % 2 == 0:
     print(f'{produtos[c]:.<30}', end='R$: ')
    else:
        print(f'{produtos[c]}')
