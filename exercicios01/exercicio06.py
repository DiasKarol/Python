""" Exercício 001-6: Faça um programa que leia três números inteiros e apresente o maior dos três valores. Nesta questão está proibido usar if (isto é, não deve se usar nenhuma estrutura condicional) ou a função max, mas vai precisar usar a função abs(z) que retorna com o valor do módulo, sem sinal do parâmetro. Dica: A seguinte fórmula permite calcular o maior valor dados os números x e y:
Max(x,y) = (x+y)/2 + abs(y-x)/2 """

a = int(input("informe o 1º número: "))
b = int(input("informe o 2º número: "))
c = int(input("informe o 3º número: "))

larger = (a+b)/2 + abs(b-a)/2 #verifica qual dos dois primeiros é o maior
larger = (larger+c)/2 + abs(c-larger)/2 #pega o maior e verica se é maior que o ultimo numero

print(f"o maior número informado é o {larger}")