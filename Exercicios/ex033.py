'''Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''
p = int(input('Digite o primeiro valor: '))
s = int(input('Digite o segundo valor '))
t = int(input('Digite o terceiro valor: '))

if p > s and p > t :
    maior = p
if s > p and s > t:
    maior = s
if t > p and t > s:
    maior = t
print(maior)

if p < s and p < t:
    menor = p
if s < p and s < t:
    menor = s
if t < p  and t < s:
    menor = t

print(menor)
