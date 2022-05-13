'''Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular
 e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.'''

def factorial(num, opcional = 0):
    total = 1
    for c in range(num, 0, -1):
        total = total * c
    return f'Valor é do fatorial de {num} é: {total} '

teste = int(input('Digite o valor do fatorial: '))
print(factorial(teste))
