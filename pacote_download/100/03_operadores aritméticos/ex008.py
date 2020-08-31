#Desafio 08
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

val = float(input('Insira um valor em metros'))
cent = val * 100
mil = val * 1000

print('Valor em metros: {}'
      '\nValor em centímetros: {} \n'
      'Valor em milímentros: {}'.format(val, cent, mil))