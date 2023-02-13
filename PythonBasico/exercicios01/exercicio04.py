""" Exercício 001-4: Leia dois números inteiros a, b, e dois números em ponto flutuante x, y. Então calcule a expressão:
a + bx – sqrt(b) + ( (a+b) / (x-y) )
atribuindo o resultado à variável expressao. A seguir, mostre a variável expressao com a mensagem correspondente, conforme exemplos abaixo. A saída deve imprimir duas casas decimais. """
import math

a = int(input("Informe o 1º número inteiro: "))
b = int(input("Informe o 2º número inteiro: "))
x = float(input("Informe o 1º número decimal: "))
y = float(input("Informe o 2º número decimal: "))

expressao = a + b * x - math.sqrt(b) + ( (a+b) / (x-y) )

print("O resultado da expressão a + bx – sqrt(b) + ( (a+b) / (x-y) ) com os numeros retornados são: %.2f" % expressao)