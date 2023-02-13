""" Crie um programa em python que receba via input n números e faça a multiplicação entre eles e imprima na tela. 
Pode receber a quantidade ilimitada de números mas deve-se usar o *args em uma função onde vai receber esses valores e irá realizar a multiplicação. 
Exemplo: 
Se rodar o programa e receber : 5, 4, 5 o resultado será 100. 
Se rodar o programa e receber : 10, 2, 4, 3 o resultado será 240. """

numbers = input('insiras os números que deseja multiplicar, separando-os por espaços: ')
list_numbers = [int(num) for num in numbers.split()]

def calculate_n(*n):
    result = 1
    for num in n:
        result *= num
    return result

print(calculate_n(*list_numbers))