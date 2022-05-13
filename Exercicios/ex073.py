'''Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''

brasileiro = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians',
'Bragantino', 'Fluminense', 'América-MG', 'Atletico-GO', 'Santos', 'Ceará', 'Internacional',
'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')


#a) Os 5 primeiros times.
print('Os primeiros 5 colocados são:')
for c in range(1, 6):
    print(f'{c}) {brasileiro[c]}')

#b) Os últimos 4 colocados.
print('\nOs ultimos 4 colocados')

for c in range(16, 20):
    print(f'{c + 1}) {brasileiro[c]}')

#c) Times em ordem alfabética.
print('\nOrdem alfabetica')
print(sorted(brasileiro))


#d) Em que posição está o time da Chapecoense.'''
print('\nPosição da Chapecoense')
print(brasileiro.index('Chapecoense'))