"""
    Escreva uma função que desenhe uma grade
    * Adaptei a função para que a grade possa ser desenhada em qualquer tamanho.
"""


def grade(linha, coluna):
    for linhas in range(linha):
        montar_linha(coluna)
        montar_coluna(coluna)
    montar_linha(coluna)


def montar_linha(coluna):
    print('+', '-', '-', '-', '-', '+', end=' ')
    for i in range(coluna - 1):
        print('-', '-', '-', '-', '+', end=' ')
    print()


def montar_coluna(coluna):
    for j in range(4):
        print('|         |', end='')
        for i in range(coluna - 1):
            print('         |', end='')

        print()


print('Tabela Digital')
quant_linhas = int(input('Digite a quantidade de linhas: '))
quant_colunas = int(input('Digite a quantidade de colunas: '))

grade(quant_linhas, quant_colunas)
