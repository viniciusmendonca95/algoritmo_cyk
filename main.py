from time import sleep
from cyk import Gramatica
from lib.interface import menu, cabecalho


cabecalho(f'{"="*18} Algoritmo CYK {"="*18}')

while True:
    gramatica = Gramatica()

    resposta = menu(['Imprimir gramática',
                     'Testar palavra',
                     'Sair do sistema'])

    if resposta == 1:
        print()
        cabecalho('Opção 1 - Imprimir gramática')
        print(gramatica)
        sleep(1)

    elif resposta == 2:
        print()
        cabecalho('Opção 2 - Testar palavra')
        palavra = input(
            'Informe a palavra que deseja testar: ')
        sleep(1)
        print()

    elif resposta == 3:
        print()
        cabecalho('Saindo do sistema... Até logo!')
        sleep(1)
        break