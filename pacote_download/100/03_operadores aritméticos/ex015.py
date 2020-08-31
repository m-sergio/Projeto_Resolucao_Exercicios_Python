#Desafio
#Escreva um programa que pergunte a quantidade de Km percorridos
# por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.


km = float(input('Qual é a quantidade de Km percorridos'))
Qdias = int(input('Quantos dias o carro foi alugado'))

ppag = (60 * Qdias) + (0.15 * km)

print('O preco a pagar por {} dias alugados é de {:.2}'.format(Qdias, ppag))