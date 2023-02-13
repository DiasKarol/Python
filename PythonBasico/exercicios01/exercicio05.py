""" Exercício 001-5: Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 5% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais."""

vender = input("Informe o vendedor: ")
salary = float(input("Informe o salário deste vendedor: "))
sales = float(input("Informe o total de vedas do vendedor: "))

commission = sales * 0.05

total = salary + commission

print(f"{vender} irá receber um total de R$ {total:.2f} no final do mês.")