'''
   * Digite o exemplo e teste-o
   * Altere do_twice para que receba dois argumentos, um objeto de função e um valor, e chame a função duas vezes,
     passando o valor como argumento
   * Copie a definição de print_twice que aparece anteriormente...
   * Use a versão alterada de do_twice para chamar print_twice duas vezes, passando 'spam' como um argumento
   * Defina uma função nova chamada do_four que receba um objeto de função e um valor e chame a função quatro vezes,
     passando o valor como um parâmetro. Deve haver só duas afirmações no corpo desta função, não quatro.
'''


def do_twice(objeto_funcao, valor):
    objeto_funcao(valor)
    objeto_funcao(valor)


def print_spam():
    print('Spam')


def print_twice(bruce):
    print(bruce)
    print(bruce)


def do_four(objeto_funcao, valor): # usar 'func' e 'arg'
    objeto_funcao(print_twice, valor)
    objeto_funcao(print_twice, valor)


do_twice(print_twice, 'spam')
do_four(do_twice, 'spam')
