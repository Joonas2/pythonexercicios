'''Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8'''

prox = 0
ant = 0

while prox < 50:
    print(prox)
    prox = prox + ant
    ant = prox - ant

    if prox < 1:
        prox = prox + 1