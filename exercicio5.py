"""
Escreva um programa que leia o raio de um círculo e faça duas funções: 
uma função chamada area que  calcula  e  retorna  a  área  do  círculo  
e  outra  função  chamada perimetro que  calcula  e  retorna  o perímetro do círculo.
Utilize as fórmulas abaixo.
Área = π * r2
Perímetro = π * 2 * r
"""
def area_do_circulo(numero):
    area = 3.14 * (numero**2)
    print(f'A área do círculo é de: {area}')

def perimetro_do_circulo(numero):
    perimetro = 3.14 * 2 * numero
    print(f'O perímetro do círculo é de: {perimetro}')

numero = int(input('Insira o raio do círculo: '))
area_do_circulo(numero)
perimetro_do_circulo(numero)