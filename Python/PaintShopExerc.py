#LearningPython
#Author: Pedro
#Function: Learn
#Date: 2014/09/01
#Language: Portuguese

'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados 
e que a tinta é vendida em latas de 18 litros, que custam R$ 80, 00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
Obs.: Somente são vendidos um número inteiro de latas.
'''

#Apresentação
print("Bem vindo à Loja de tintas!")
tam = int(input("Diga a área, em metros quadrados, a ser pintada: "))
#Verificar resto, no caso de uma divisão não exata, adicionar uma lata de tinta.
if tam % 54 != 0:
    tinta = int((tam/54)+1)
else:
    tinta = tam/54
print("Voce vai precisar de %d latas de tinta!" % tinta)
print("Isso dara um custo total de R$%5.2f" % (tinta*80))
