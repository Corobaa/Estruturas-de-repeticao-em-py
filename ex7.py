#7. Faça um programa que calcule e exiba o valor do desconto e o valor a ser pago pelo cliente de
#vários carros. O desconto deverá ser calculado de acordo com o ano do veículo. Até 2000
#desconto de 12% e acima de 2000 desconto de 7%. O sistema deverá perguntar se deseja
#continuar calculando novos descontos até que a resposta seja: "( N ) Não )". Informar o total de
#carros com ano até 2000 e o total de carros no geral.

total_carros_ate_2000 = 0
total_carros_geral = 0

resposta = input("Deseja cadastrar carros? (S para Sim, N para Não): ")

while resposta == 'S':
    qt = int(input("Digite quantos carros você quer cadastrar: "))
    for i in range(1, qt + 1):
        ano = int(input(f"Introduza o ano do carro {i}: "))
        valor = float(input(f"Introduza o valor a pagar pelo carro {i}: "))
        total_carros_geral += 1
        if ano <= 2000:
            desconto = 0.12
            total_carros_ate_2000 += 1
        else:
            desconto = 0.07
        valor_desconto = valor * desconto
        valor_a_pagar = valor - valor_desconto
        print(f"Carro {i}, ano {ano}, desconto {desconto*100:.0f}%, valor a pagar {valor_a_pagar:.2f}")

    resposta = input("Deseja continuar calculando novos descontos? (S para Sim, N para Não): ")

print(f"Total de carros com ano até 2000: {total_carros_ate_2000}")
print(f"Total de carros no geral: {total_carros_geral}")
print("Encerrado")
    
    
    
    
        
    
