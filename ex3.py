#Faça um programa que para um número inteiro positivo imprima seus divisores (Ex: Divisores de 
#12 são os números 1, 2, 3, 4, 6 e 12)

nr=int(input("Introduza um numero:"))
print("Os divisores de",{nr},"sao:")
for i in range(1,nr+1):
    if nr%i==0:
        print(i)