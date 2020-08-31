#Desafio 012
#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

prec = float(input('Digite o preco do produto'))
prec_desc = prec - (prec * 0.05)

print('Preço do produto: {:.2f} mts\n'
      'Preço do produto com 5% de desconto: {:.2f} mts'.format(prec,prec_desc))