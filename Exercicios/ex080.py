'''Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
 já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''

valores = list()
laco = 0

for i in range(0, 5):
    n = int(input('Digite um valor: '))

    if i == 0 or n > valores[-1]:
        valores.append(n)

    else:
        for cont in range(0, len(valores)+1):

            if n <= valores[cont]:
                valores.insert(cont, n)
                print(cont, len(valores), valores)
                break

            elif n > valores[cont] and n < valores[-1] :
                valores.index(cont, n)

    print(laco, len(valores), valores)
'''




print(valores)


