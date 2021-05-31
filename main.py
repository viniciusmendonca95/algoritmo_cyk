from time import sleep
from cyk import Gramatica
from lib.interface import menu, cabecalho


cabecalho(f'{"="*18} Algoritmo CYK {"="*18}')

while True:
    gramatica = Gramatica()

    resposta = menu(['Imprimir gramática',
                     'Testar palavra',
                     'Testar palavra mostrando passo a passo',
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
        gramatica.cyk(palavra)
        sleep(1)
        print()

    elif resposta == 3:
        print()
        cabecalho('Opção 4 - Testar palavra mostrando passo a passo')
        palavra = input(
            'Informe a palavra que deseja testar: ')
        gramatica.cyk_passo_a_passo(palavra)
        sleep(1)
        print()

    elif resposta == 4:
        print()
        cabecalho('Saindo do sistema... Até logo!')
        sleep(1)
        break