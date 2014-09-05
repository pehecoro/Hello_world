#LearningPython
#Author: Pedro
#Function: Confer list
#Date: 2014/09/05
#Language: Portuguese

#Importar a função de "dormir" para não deixar o programa tão acelerado.
from time import sleep
print("Bem vindo aluno!")
sleep(1)
print("Vamos listar suas notas!")
sleep(1)
#Atribuindo valores às variáveis e à lista.
x = 0
soma = 0
L=[0,0,0,0,0]
#Substituição de elementos por notas.
#Acumulação de valores a 'soma'
while x < 5:
	L[x] = float(input("Nota %d: " %(x+1)))
	soma += L[x]
	x += 1
print("Listado!")
print("Sua média é: %d" %(soma/x))
#Exibir notas conforme digitado
while True:
	x = int(input("Para verificar sua nota, digite o número dela(0 para sair): "))
	if x == 0:
		print("Até logo!")
		break
	print(L[x-1])
