class Gramatica:
    def __init__(self):
        self.regras = self.ler_gramatica()
        self.terminais = self.get_terminais(self.regras)
        self.nao_terminais = self.get_nao_terminais(self.regras)
        self.simbolo_inicial = self.get_simbolo_inicial(self.regras)

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


    def get_terminais(self, regras):
        terminais = []

        for linha in regras:
            lado_esquerdo, lado_direito = linha.split(" => ")
            lado_direito = lado_direito.split(" | ")

            for letra in lado_direito:
                if(str.islower(letra)):
                    terminais.append([lado_esquerdo, letra])

        return terminais


    def get_nao_terminais(self, regras):
        nao_terminais = []

        for linha in regras:
            lado_esquerdo, lado_direito = linha.split(" => ")
            lado_direito = lado_direito.split(" | ")

            for simbolo in lado_direito:
                if (str.islower(simbolo) == False):
                    nao_terminais.append([lado_esquerdo, simbolo])

        return nao_terminais


    def get_simbolo_inicial(self, regras):
        simbolo_inicial = regras[0][0]

        return simbolo_inicial


    def cyk(self, terminais, nao_terminais, palavra):
        return ""



