#Faça um programa que imprima os factoriais de 1 a 10.
for n in range(1, 11):
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    print(f"O fatorial de {n} é {fatorial}")
