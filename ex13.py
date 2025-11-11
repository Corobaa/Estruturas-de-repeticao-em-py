# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
#Peça para cada eleitor votar em um dos candidatos e ao final mostrar o número de votos de cada 
#candidato.

candidatoA=0  
candidatoB=0 
candidatoC=0
n=int(input("introduza o numero de eleitores"))
for i in range (1,n+1):
 escolha=int(input("Escolha o seu candidato 1,2,3"))
 if escolha==1 :
     candidatoA+=1
     print("Voce votou em A")
 elif escolha==2:
     candidatoB+=1
     print("Voce votou em B")
 elif escolha==3:
     candidatoC+=1
     print("Voce votou em C")


print(f"O candidato a teve{candidatoA}  votos")
print(f"O candidato a teve{candidatoB}  votos")
print(f"O candidato a teve{candidatoC}  votos")


