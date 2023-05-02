"""
Faça uma função que receba como parâmetro o número de lados de um polígono e:
-Se o número de lados for igual a 3, escrever TRIÂNGULO.
-Se o número de lados for igual a 4, escrever QUADRILÁTERO.
-Se o número de lados for igual a 5, escrever PENTÁGONO.
-Se o número de lados for diferente de 3, 4 ou 5, escrever VALOR INVÁLIDO.
"""

def defina_o_poligono(numero):
    if numero == 3:
        print('É um Triângulo')
    elif numero == 4:
        print('É um Quadrilátero')
    elif numero == 5:
        print('É um Pentágono')
    else:
        print('Valor Inválido')





numero = int(input('Insira o número de lados do polígono: '))
defina_o_poligono(numero)
