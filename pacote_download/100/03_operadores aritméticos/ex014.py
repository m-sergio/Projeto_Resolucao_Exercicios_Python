#Desafio 014
# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

tempC = float(input('Digte a temperatura em graus celsos: '))
tempfF = ((9 * tempC) /5 )+ 32

print('Temperatura em Graus celsos: {:.2f} ºC \n'
      'Temperatura em Fahrenheit: {:.2f} ºF'.format(tempC,tempfF))