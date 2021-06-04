class Gramatica:
    def __init__(self):
        self.regras = self.ler_gramatica()
        self.terminais = self.get_terminais()
        self.nao_terminais = self.get_nao_terminais()
        self.simbolo_inicial = self.get_simbolo_inicial()

    def __repr__(self):
        string = ''
        string += f'Regras Gerais: {self.regras}\n'
        string += f'Regras Terminais: {self.terminais}\n'
        string += f'Regras Não terminais: {self.nao_terminais}\n'
        string += f'Símbolo Inicial: {self.simbolo_inicial}\n'
        return string

    @staticmethod
    def ler_gramatica():
        with open('gramatica.txt', 'r') as gramatica:
            gramatica = gramatica.read().splitlines()

            return gramatica

    def get_terminais(self):
        terminais = []

        for linha in self.regras:
            lado_esquerdo, lado_direito = linha.split(" => ")
            lado_direito = lado_direito.split(" | ")

            for letra in lado_direito:
                if str.islower(letra):
                    terminais.append([lado_esquerdo, letra])

        return terminais

    def get_nao_terminais(self):
        nao_terminais = []

        for linha in self.regras:
            lado_esquerdo, lado_direito = linha.split(" => ")
            lado_direito = lado_direito.split(" | ")

            for simbolo in lado_direito:
                if not str.islower(simbolo):
                    nao_terminais.append([lado_esquerdo, simbolo])

        return nao_terminais

    def get_simbolo_inicial(self):
        simbolo_inicial = self.regras[0][0]

        return simbolo_inicial

    def cyk(self, palavra):
        # Lista de chaves e valores de Não terminais
        nt_chaves = [nao_terminal[0] for nao_terminal in self.nao_terminais]
        nt_valores = [nao_terminal[1] for nao_terminal in self.nao_terminais]

        # Criação da tabela usada no CYK com estruturas de conjunto de valores set()
        tabela = [[set() for j in range(len(palavra) - i)] for i in range(len(palavra))]

        # Verificação se a letra da palavra estiver em um dos terminais. Se sim, adiciona o terminal na tabela (base da tabela)
        for i in range(len(palavra)):
            for terminal in self.terminais:
                if terminal[1] == palavra[i]:
                    tabela[0][i].add(terminal[0])

        # Criação de um conjunto de valores set() que vão agrupar os conjuntos de dados que entrarão na tabela
        for i in range(1, len(palavra)):
            for j in range(len(palavra) - i):
                for k in range(i):
                    conjunto_valores = set()

                    # Combinação dos valores na tabela, adicionando os resultados em um conjunto de valores set()
                    for primeira_letra in tabela[k][j]:
                        for segunda_letra in tabela[i - k - 1][j + k + 1]:
                            conjunto_valores.add(primeira_letra + segunda_letra)
                    combinacoes = conjunto_valores

                    # Verificação se esse conjunto de valores set() está dentro da lista de não terminais (valores), se sim adicionaremos sua chave na tabela. (preenchimento da tabela)
                    for combinacao in combinacoes:
                        if combinacao in nt_valores:
                            tabela[i][j].add(
                                nt_chaves[nt_valores.index(combinacao)])

        # Verificação do topo da tabela. Se no topo for encontrado o símbolo inicial, a palavra pertence a gramática. Caso contrário, a palavra não pertence a gramática.
        if self.simbolo_inicial in tabela[len(palavra) - 1][0]:
            print(f"{palavra} pertence a gramática")
            return True
        else:
            print(f"{palavra} não pertence a gramática")
            return False

    def cyk_passo_a_passo(self, palavra):
        print(f"Palavra: {palavra}")

        nt_chaves = [nao_terminal[0] for nao_terminal in self.nao_terminais]
        nt_valores = [nao_terminal[1] for nao_terminal in self.nao_terminais]

        tabela = [[set() for j in range(len(palavra) - i)] for i in range(len(palavra))]

        self.imprimir_tabela(tabela, palavra)

        for i in range(len(palavra)):
            for terminal in self.terminais:
                if terminal[1] == palavra[i]:
                    tabela[0][i].add(terminal[0])

        for i in range(1, len(palavra)):
            self.imprimir_tabela(tabela, palavra)
            for j in range(len(palavra) - i):
                for k in range(i):
                    conjunto_valores = set()

                    for primeira_letra in tabela[k][j]:
                        for segunda_letra in tabela[i - k - 1][j + k + 1]:
                            conjunto_valores.add(primeira_letra + segunda_letra)
                    combinacoes = conjunto_valores

                    for combinacao in combinacoes:
                        if combinacao in nt_valores:
                            tabela[i][j].add(
                                nt_chaves[nt_valores.index(combinacao)])
        self.imprimir_tabela(tabela, palavra)

        if self.simbolo_inicial in tabela[len(palavra) - 1][0]:
            print(f"{palavra} pertence a gramática")
            return True
        else:
            print(f"{palavra} não pertence a gramática")
            return False

    @staticmethod
    def imprimir_tabela(tabela, palavra):
        print()
        for i in range((len(tabela) - 1), -1, -1):
            print(', '.join(map(str, tabela[i])))
        print(', '.join(palavra))
        print()
