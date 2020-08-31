#Desafio
#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

mts = float(input('Quantos meticais possuis na carteira?'))
dol = mts/71.04
print('Com {:.2f} mts, podes comprar $ {:.2f} '.format(mts, dol))