'''Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''
numeros = list()
continuar = 's'

while continuar not in 'n':
    n = (int(input('Digite um valor: ')))

    if n not in numeros:# se o valor de n, não estiver em numeros, ele entra no if.
        numeros.append(n)
    else:
        print('Valor repetido')

    continuar = str(input('Desejar continuar ? [S/N]: ')).lower().strip()

    if continuar != 's' and continuar != 'n':
        continuar = str(input('Opção invalida. Deseja continuar [S/N]: ')).lower().strip()

numeros.sort()
print(numeros)








