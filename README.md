# Algoritmo CYK

Implementação de um reconhecedor de palavras utilizando o algoritmo CYK em python.  
Desenvolvido para a matéria de Automatos Finitos e Deterministicos, ministrada pelo professor Adolfo Guimarães na Universidade Tiradentes.

## Carregando a Gramática

Para carregar o gramática, devemos configurar o arquivo `gramatica.txt`, presente na raíz do projeto.
A gramática no arquivo de texto deve seguir a seguinte notação `gramatica.txt`:

```txt
S => XB | AB
X => AS
A => a
B => b
```

O conjunto de regras são compostas por:
 
* Uma variável que está sendo definida pela regra `S, X, A, B`;
* Um símbolo da regra `=>`;
* Strings de zero ou mais terminais e variáveis `XB, AB, AS, a, b`.


## Executando o Programa

Para iniciar a o programa, basta executar o arquivo `main.py` e seguir as instruções do Menu!

## Desenvolvedores

- Natália Braga da Fonseca
- Vinícius José Santana de Mendonça
