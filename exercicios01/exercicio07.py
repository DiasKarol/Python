""" Exercício 001-7: Faça um programa que leia um valor inteiro representando um valor em reais e calcule o menor número de cédulas possíveis no qual o valor pode ser decomposto. As cédulas consideradas são as de R$200.00, R$100.00, R$50.00, R$20.00, R$10.00, R$5.00, R$2.00 e R$1.00. Seu programa deve imprimir a quantidade de cada cédula. Dica: divisão inteira usa // e resto da divisão usa %
Assim valor total R$ 1317,00 quantas notas de R$ 200,00
qtdNotas200 = valorTotal // 200
resulta 6 notas de 200 e agora o resto seria
restoValor = valorTotal % 200
resulta 117 """

reais_value = int(input("Informe um valor: "))

notes_200 = reais_value // 200 
remain = reais_value % 200

notes_100 = remain // 100 
remain = remain % 100

notes_50 = remain // 50 
remain = remain % 50

notes_20 = remain // 20 
remain = remain % 20

notes_10 = remain // 10 
remain = remain % 10

notes_5 = remain // 5 
remain = remain % 5

notes_2 = remain // 2 
remain = remain % 2

notes_1 = remain // 1 
remain = remain % 1

print(f"Serão necessários {notes_200} de R$200,00")
print(f"Serão necessários {notes_100} de R$100,00")
print(f"Serão necessários {notes_50} de R$50,00")
print(f"Serão necessários {notes_20} de R$20,00")
print(f"Serão necessários {notes_10} de R$10,00")
print(f"Serão necessários {notes_5} de R$5,00")
print(f"Serão necessários {notes_2} de R$2,00")
print(f"Serão necessários {notes_1} de R$1,00")