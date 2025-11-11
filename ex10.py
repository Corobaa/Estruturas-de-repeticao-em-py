# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor
#e a soma dos valores.
soma_valores=0
n=int(input("n?  "))
if n > 0:
    x=int(input("introduza o numero:"))
    menor_valor = x
    maior_valor = x
    soma_valores += x
    for i in range(2,n+1):
        x=int(input("introduza o numero:"))
        soma_valores+=x
        if x < menor_valor:
            menor_valor = x
        if x > maior_valor:
            maior_valor = x
    print("a soma dos valores",soma_valores)
    print("o menor valor",menor_valor)
    print("o maior valor",maior_valor)
else:
    print("N deve ser maior que 0")
