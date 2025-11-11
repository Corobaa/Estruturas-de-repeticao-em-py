#Escreva um programa que imprima na tela a soma dos números ímpares entre 0 e 30 e a 
#multiplicação dos números pares entre 0 e 30.

soma_impares = 0
multiplicacao_pares = 1
for i in range(1,5):
 if i%2!=0 :
  soma_impares+=i
 else:
     multiplicacao_pares*=i
print("Soma dos impares",soma_impares)
print("Multiplicacao dos pares",multiplicacao_pares)
    