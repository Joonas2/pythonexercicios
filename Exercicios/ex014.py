#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dias = int(input('Quantos dias ficou com carro? '))
km = float(input('Quantos Km você rodou com carro? '))
custo = (dias * 60) + (km * 0.15)
print('Você ficou {} dias com carro e rodou {} km com ele, o custo final ficou R$ {:.2f}'.format(dias, km, custo))
