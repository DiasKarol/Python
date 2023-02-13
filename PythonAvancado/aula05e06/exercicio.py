""" Defina uma função chamada weird_prod que recebe como argumento uma lista de números inteiros e devolve o produto do primeiro elemento, pelo quadrado do segundo, pelo cubo do terceiro, e assim sucessivamente. """

from typing import List
from functools import reduce
from operator import mul

p = 0

def user_list() -> int:
    #Solicita ao usuario uma lista de numeros
    numbers_list = input('insira uma lista de numeros inteiros separados por um espaço: ')
    numbers = list(map(int, numbers_list.split()))
    return numbers

def potentied(x: int) -> int:
  global p #tenho que declarar dentro da função que a variável a ser utilizada aqui dentro é a variavel global
  p = p + 1
  return x ** p

def weird_prod(numbers: List[int]) -> int:
    #recebe a lista de numero do usuario e retorna como produto final, a potencia dos elementos de acordo com o exercicio proposto.
    
    result = list(map(potentied, numbers)) 

    return reduce(mul, result)

print( weird_prod(user_list()))