"""
Faça  um  programa  para  uma  calculadora  simples  com  as  seguintes  operações:  
adição,  subtração, multiplicação e divisão. 
O programa começa apresentando ao usuário um menu de opções semelhante ao mostrado abaixo:
Calculadora: 1-Adição 2-Subtração 3-Multiplicação 4-Divisão 5-Sair do programa.
Selecione sua opção: Crie  uma  função  chamada Menu,  que  exiba  o  menu  acima  
e  retorna  a  opção  do  usuário  para  o programa  principal. 
Se  a  opção  for  inválida,  informe  ao  usuário  
e  peça  a  ele  para  entrar  com  uma opção válida.
De   acordo   com  a   opção   do   usuário,   chame   uma   das   seguintes   funções: 
adicao,   subtracao, multiplicacao, divisao, passando como parâmetros 
dois números também informados pelo usuário.
Após a execução da operação o programa volta a apresentar 
o menu inicial até que o usuário encerre o programa com a opção 5.
"""
# Definindo Funções
def adicao(numero, numero2):
    adicao = numero + numero2
    print(f'{numero} + {numero2} é igul a {adicao}')

def subtracao(numero, numero2):
    sub = numero - numero2
    print(f'{numero} - {numero2} é igual a {sub}')

def multiplicacao(numero, numero2):
    mult = numero * numero2
    print(f'{numero} multiplicado por {numero2} é igual a {mult}')

def divisao (numero, numero2):
    div = numero / numero2
    print(f'{numero} dividido por {numero2} é igual a {div}')


while True:
# Menu
    print('Menu')
    print('1-Adição')
    print('2-Subtração')
    print('3-Multiplicação')
    print('4-Divisão')
    print('5-Sair do programa')
# Inputs ao usuário
    menu = int(input('Selecione a operação desejada: '))
    if menu == 5:
        print('Obrigada!')
        break
    if menu > 5:
        print('Opção Inválida, por favor Insira uma opção válida.')
    else:
        numero = float(input('Insira um número: '))
        numero2 = float(input('Insira um outro número: '))
# ifs
        if menu == 1:
            adicao(numero,numero2)
        elif menu == 2:
            subtracao(numero,numero2)
        elif menu == 3:
            multiplicacao(numero,numero2)
        elif menu == 4:
            divisao(numero,numero2)
   






