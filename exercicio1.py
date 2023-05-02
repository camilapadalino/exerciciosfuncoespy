"""
Escreva  um  programa  para solicitaras  notas  de  duas provas.  Faça  uma função que  receba  
as  duas notas por parâmetro e exibe a mensagem “Você foi Aprovado!” ou “Você foi Reprovado!”. 
Considere 6.0 a média mínima para aprovação.
"""
def mediadanota(nota1,nota2):
    media = (nota1 + nota2) / 2
    if media >= 6:
        print(f'Você foi aprovado! Sua média foi de {media}')
    else: 
        print(f'Você foi reprovado! Sua média foi de {media}')



nota1 = float(input('Insira uma nota: '))
nota2 = float(input('Insira a outra nota: '))
mediadanota(nota1,nota2)
