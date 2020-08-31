#Desafio 11
#Faça um programa que leia a largura e a
# altura de uma parede em metros, calcule a sua área e a quantidade
# de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.


larg = float(input('Digite a largura da parede'))
alt =float(input('Digite a altura da parede'))
a = larg * alt
tint = a  / 2


print('A area por se pintar é de {} m2 e quantidade de tinta necessaria é de {} litros'.format(a,tint))

