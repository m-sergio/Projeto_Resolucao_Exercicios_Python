#Desafio 05
# Faça um progrma que leia um numero interiro mostre na tela o seu sucessor e o seu antecessor


n = int(input('Digite um numero inteiro'))

ant = n-1
suc = n + 1
print('Numero digitado: {} \n'
      'Antecessor: {} \n'
      'Sucessor: {}'.format(n, ant, suc))

