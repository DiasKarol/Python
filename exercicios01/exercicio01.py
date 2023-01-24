""" Exercício 001-1: A fórmula para calcular a área de uma circunferência é: área = pi . raio². Crie um programa para ler o valor do raio e efetuar o cálculo da área. Entrada: A entrada contém um número real, positivo, representando o raio. Saída: Seu programa deve imprimir na tela a área do círculo com 4 casas após o ponto decimal. """

import math

ray = float(input("Informe o raio do circulo a ser calculado: "))
area = math.pi * (ray**2)

print("A área do circulo é %.4f" % area) 