#Desafio 013
#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

sal_fun = float(input('introduza o salario do funcionario'))

aument = sal_fun + (0.15 * sal_fun)

print('Salário base do funcionário: {:.2f} mts\n'
      'Salário com 15% de aumento: {:.2f} mts'.format(sal_fun, aument))