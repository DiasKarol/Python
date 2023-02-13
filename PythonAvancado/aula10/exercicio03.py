""" Crie uma função chamada que tenha a estrutura para receber 2 argumentos fixos e N argumentos nomeados e no final imprima todos os argumentos passados para essa função: 
Exemplo de passagem de argumentos que a função receberá sem precisar ter nenhuma mudança: 
Chamada da função: teste_Kargs('Carro', 100, nome='jose', chave='teste') 
Saída: 
    arg1=carro 
    arg2=100 
    nome=jose 
    chave=teste 
Outros exemplos de chamadas de função que deverão funcionar sem alterar a função: 
teste_Kargs('Carro', 100, nome='jose', chave='teste',outrachave='brasil', oo='python') 
Saída: 
    arg1=carro 
    arg2=100 
    nome=jose 
    chave=teste 
    outrachave = brasil 
    oo = python  """
    
def teste_Kargs(arg1='Brasil', arg2='País', **arg3):
    print(arg1)
    print(arg2)
    for key, value in arg3.items():
        print(f'{key}: {value}')

teste_Kargs('Carro', 100, nome='jose', chave='teste')
print('----------------')
teste_Kargs('Carro', 100, nome='jose', chave='teste',outrachave='brasil', oo='python')
print('----------------')
teste_Kargs('Amora', 100, nome='Maria', chave='Aquino',pais='Argentina', casa='10', rua='alphaEdPedra')