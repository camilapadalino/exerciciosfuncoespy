"""
Implementar uma função que recebe como parâmetro a altura em metros (exemplo: 1.70) 
e o sexo ('M' para masculino e 'F' para feminino) de uma pessoa e retorne o seu peso ideal, 
sendo que:
Peso Ideal (para homens) = (72.7 * altura) -58
Peso Ideal (para mulheres) = (62.1 * altura) -44.7
"""
# Definindo o Gênero
feminino = "F"
masculino = "M"
print('Insira F se você for mulher, e M se você for homem.')

# Atribuindo a Função
def peso_ideal(altura):
    if genero == "M":
        peso = (72.7 * altura) - 58
        print(f'Seu peso ideal seria {peso} kilos ')
    elif genero == "F":
        peso = (62.1 * altura) - 44.7
        print(f'Seu peso ideal seria {peso} kilos')

# Inputs
genero = input('insira seu gênero: ')
altura = float(input('Insira sua altura em metros: '))
peso_ideal(altura)