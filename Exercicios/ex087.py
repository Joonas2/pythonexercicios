'''Exercício Python 087: Aprimore o desafio anterior, mostrando no final
A) A soma de todos os valores pares digitados
B) A soma dos valores da terceira coluna
C) O maior valor da segunda linha.'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = list()
soma = somaPar = maior = 0



for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor da matriz{l}x{c}: '))

        if matriz[l][c] % 2 == 0:
            somaPar = somaPar + matriz[l][c]

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end=' ')
    print()
print('-=-' * 20)

print(f'Pares: e sua soma é {somaPar}')

print(f'Soma dos valores da terceira coluna é:', end=' ')
for linha in range(0, 3):
    soma = soma + matriz[linha][2]
print(soma)


print('Maior da segunda linha é:', end=' ')
for coluna in range(0, 3):
   if maior == 0:
       maior = matriz[1][0]
   elif maior < matriz[1][coluna]:
       maior  = matriz[1][coluna]

print(maior)
