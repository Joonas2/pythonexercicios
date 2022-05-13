''' Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor da matriz{l}x{c}: '))#dessa forma ele ira substituir os valores que estão na lista


for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end=' ')
    print()




'''
matriz = [[[], [], []], [[], [], []], [[], [], []]]
pos = 0
for c in range(0, 9):
    var = int(input('Digite do valor da matriz: '))

    if c < 3:
        matriz[0][pos].append(var)
        pos = pos + 1
        print(matriz[0])
        if pos > 2:
            pos = 0
            print(pos)

    elif c > 2 and c < 6:
        matriz[1][pos].append(var)
        pos = pos + 1
        print(matriz[1])
        if pos > 2:
            pos = 0

    else:
        matriz[2][pos].append(var)
        pos = pos + 1


print(matriz[0])
print(matriz[1])
print(matriz[2])
'''


#_________________________________________

'''linha = list()
matriz = list()
for c in range(0, 9):
    var = int(input('Digite do valor da matriz: '))
    linha.append(var)
    matriz.append(linha[:])
    linha.clear()
    
print(matriz[0:3])
print(matriz[3:6])
print(matriz[6:10])
'''