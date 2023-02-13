""" Faça um programa em python que faça a divisão de 1 por um valor passado por uma
variável e realize o tratamento para as entradas abaixo:
entrada = 0
divisao = 1/entrada # vai dar error
#nesse caso tem que ser tratado o erro de divisão por zero, criar um tratamento de
exceção para esse tipo de erro e imprimir uma mensagem amigável com o tipo de
erro.
entrada = ‘teste’
divisao = 1/entrada # vai dar error
#nesse caso tem que ser tratado o erro de tipo, criar um tratamento # exceção para
esse tipo de erro e imprimir uma mensagem amigável com o tipo de erro.
E deixar o código para tratar erros genéricos diferentes dos mencionados acima.
Caso a entrada seja um valor que não provoque erro, imprimir o valor da divisão.
Por fim, independente de ter erro ou não imprimir ao final da execução do programa,
dentro da estrutura de tratamento de exceções uma mensagem informando seu nome
.
Crie esse código, suba para o github e envie na plataforma somente o link do
repositório com o exercício resolvido. """

try:
    num = input('Informe um número: ')
    entrada=int(num)
    
    divisao = 1/entrada
except ZeroDivisionError:
    print('Olá, você está tentando dividir por zero. Isso não é possível, tente outro número.')
except ValueError:
    print('Olá, você inseriu uma entrada inválida. Por favor, insira um número inteiro.')
except Exception as error:
    print(f'Ocorreu um erro: {error}')
else:
    print(f'O resultado da divisão de 1/{entrada} é: {divisao:.2f}')
finally:
    print('Ana Dias')