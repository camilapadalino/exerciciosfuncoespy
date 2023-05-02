"""
Escreva um programa que solicita um valor inteiro ao usuário e exibe a tabuada desse número. 
Você deverá escrever as seguintes funções:
-ler_numero(): Solicita um número inteiro e retorna esse número para o programa principal
-tabuada(n): Recebe como parâmetro um número inteiro e exibe na tela a tabuada desse número.
"""
def ler_numero(numero):
    print(f'O número inserido foi: {numero}')

def tabuada(numero):
    for i in range (numero, 100, numero):
        print(f' Tabuada do {numero}: {i}')


numero = int(input('Insira um número: '))
ler_numero(numero)
tabuada(numero)
