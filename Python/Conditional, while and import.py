#LearningPython
#Author: Pedro
#Function: Learn
#Language: Portuguese
#Date: 29/08/2014

#Primeiro importar de 'random' um inteiro 'randomico'
from random import randint
print("Bem vindo!")
#Criar variável e atribui-la ao inteiro randomico determinando números de 1 a 100
sorteado = randint(1, 100)
#Atribuindo 0 para que a função while prossiga
chute = 0
#Enquanto o 'chute' for diferente do número sorteado, o programa repetirá
while chute != sorteado:
#Introduzir valor a variável 'g' / Entrada de dados.
#Igualar variável 'g' com 'chute' e defini-la como número inteiro
    g = input("Chute um número: ")
    chute = int(g)
#Possibilidades
    if chute == sorteado:
        print("Voce ganhou!")
    else:
        if chute > sorteado:
            print("Alto")
        else:
            print("Baixo")
print("Fim de jogo")
