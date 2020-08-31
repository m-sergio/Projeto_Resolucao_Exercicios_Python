# Desafio 006:
#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um numero qualquer'))

dob = n * 2
trip = n * 3
razq = n**(1/2)

print('Resultado do numero digitado: \n'
      'Dobro: {} \n'
      'Triplo: {} \n'
      'Raiz Quadrada: {}'.format(dob,trip,razq))