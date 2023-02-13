""" Crie uma função chamada teste_args que tenha a estrutura para receber 2 argumentos fixos e outros variáveis e ao final imprima todos os argumentos passados para essa função:
Exemplo de passagem de argumentos que a função receberá sem precisar ter nenhuma mudança: 
Chamada da função: teste_args(Carro, 100, 50, Pedra) 
Saída: 
    arg1: 'brasil' 
    arg2: 'País' 
    arg3: 'PEDRA' 
Outros exemplos de chamadas de função que deverão funcionar sem alterar a função: 
teste_args('brasil', 'País', 'Mundo', Carro', 100, 50, Pedra) 
teste_args('brasil', 'País', 'Gol', Carro', 10)  """

def teste_args(arg1='Brasil', arg2='País', *arg3):
    print(arg1)
    print(arg2)
    for arg in arg3:
        print(arg)

teste_args('Carro', 100, 50, 'Pedra') 
print('----------------')
teste_args('brasil', 'País', 'Mundo', 'Carro', 100, 50, 'Pedra')
print('----------------')
teste_args('brasil', 'País', 'Gol', 'Carro', 10)