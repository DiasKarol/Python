''' Escreva um programa que recebe uma lista de palavras e calcula a média de ocorrências da letra X. Segmente a solução em 3 funções: 
    get_user_words() -> List[str]
    count_x_occurrences(word: str) -> int
    inform_average(average: float) -> None
Não se esqueça de fazer tudo com o MyPy ligado e usando as type hints! '''


from typing import List

def get_user_words() -> List[str]:
    # Recebe a lista de palavras
    #função pura
    words = input('Informe as palavras separando-as por espaços: ').split()
    return words

def count_x_occurrences(word: str) -> int:
    # Conta as letra X em cada palavra
    #função pura
    return word.count('x') + word.count('X')

def inform_average(average: float) -> None:
    # Mostra as ocorrencias da lista informada
    #função pura
    return print(f'O número de ocorrencias desta lista é: {average} ')

def main():
    # Função chama as funções get_user_words, count_x_occurrences e inform_average para realizar os calculos que possibilitam o resultado de ocorrencias da letra X
    #Esta função não é pura
    words = get_user_words()
    x_occurrences = [count_x_occurrences(word.lower()) for word in words] #tranforma 
    average = sum(x_occurrences) / len(x_occurrences)
    inform_average(average)

if __name__ == '__main__':
    #garante que o main seja a função principal e executa a mesma
    main()