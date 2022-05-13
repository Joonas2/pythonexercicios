valor = float(input('Digite o valor que possui na carteira em R$: '))
dolar = float(3.27)
di = valor / dolar

print('Você tem {} reais e pode comprar U$$ {:.2f} dolares'.format(valor, di))
#troco será {:.2f} siginifica que quero apenas duas casas decimais apos a virgula.