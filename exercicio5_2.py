"""
    Escreva uma função chamada check_fermat que receba quatro parâmetros -a, b, c, n - e verifique se o teorema de
    Fermat se mantém.
    Escreva uma função que peça ao usuário para digitar valores para a, b, c e n, e os conveta em números inteiros e
    use check_fermat para verificar se violam o teorema de Fermat.
"""


def check_fermat(a, b, c, n):
    fermat = a**n + b**n

    if n > 2 and fermat == c**n:
        print('Holy smokes, Fermat was wrong!')
    else:
        print("No, that doesn't work")


a, b, c, n = input('Digite os valores de - a, b, c e n - nesta ordem e com espaço: ').split(' ')
check_fermat(int(a), int(b), int(c), int(n))
