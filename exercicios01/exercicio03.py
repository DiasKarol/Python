""" Exercício 001-3: A conversão de graus Fahrenheit para Celsius é dada pela expressão:
C . 1.8 = F - 32
e a conversão de Kelvin para graus Celsius é dada por
C = k - 273.15
Faça um programa que recebe como entrada a temperatura em graus Celsius e realize duas conversões: uma para Fahrenheit e outra para Kelvin. """

celsius = int(input("Informe a temperatura (em  Celsius) que deseja converter: "))

fahrenheit = celsius * 1.8 + 32
kelvin = celsius + 273.15

print("Em Fahrenheit a temperatu é de: %.2f" % fahrenheit) 
print("Em Kelvin a temperatu é de: %.2f" % kelvin) 