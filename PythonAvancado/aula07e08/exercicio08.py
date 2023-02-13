""" Crie uma função chamada “count_up” recebe x (int) e retorna um Generator que retorna os números menores que x da sequência: 

1, 2, 4, 7, 11, 16, 22, 29, 37, 46, 56, 67, … 

onde a diferença de um termo da sequência para o anterior aumenta em uma unidade. """

from typing import Generator

def count_up(x: int) -> Generator[int, None, None]:
    "Gera números inteiros de 1 a x de forma crescente, onde a diferença entre um termo da sequência e o anterior aumenta em uma unidade. Retorna -> Generator[int, None, None]: Um gerador de números inteiros."

    n = 1 #Inicializa a sequência
    diff = 1 #Diferença (iniciado em 1)
    count = n #Contador
    while count < x:
        yield n
        n += diff
        count = n
        diff += 1

for i in count_up(100):
    print(i)