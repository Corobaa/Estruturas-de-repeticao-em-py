# Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido 
#pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para 
#encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes 
#(divisões) executados. 
cont=0
n=int(input("Introduza um numero:"))
for i in range(1,n+1):
    if n%i==0:
        cont+=1
            

if cont==2:
    print("o nr",n," primo")
else:
    print("Nao e primo")
    
    
print("Foram feitas",cont,"divisoes")