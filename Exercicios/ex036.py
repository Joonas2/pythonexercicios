'''Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

casa = float(input('Digite valor da casa: R$'))
salario = float(input('Qual seu salario R$'))
anos = int(input('Quantos anos desejar pagar a casa: '))

prestação = casa / (anos * 12)
minimo = (salario / 100) * 30
if prestação > minimo:
    print('Seu emprestimo foi negado')
else:
    print('Emprestimo aprovado')

print('Para pagar uma casa no valor de R$ {:.2f} em {} anos, a prestção ficou R${:.2f}'.format(casa, anos, prestação))

