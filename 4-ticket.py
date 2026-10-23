import os


desconto = 0
valor = 0



valor_produto = float(input("Digite o valor do produto: R$ "))
forma_pagamento = int(input("Escolha a forma de pagamento (1 para à vista, 2 para a prazo): "))

match forma_pagamento:
    case 1:
        
        desconto = valor_produto * 0.10
        valor_final = valor_produto - desconto
        
        print(f"\nValor do produto: R$ {valor_produto:.2f}")
        print("Forma de pagamento: À vista")
        print(f"Desconto: R$ {desconto:.2f}")
        print(f"Valor total a pagar: R$ {valor_final:.2f}")

    case 2:
        
        parcelas = int(input("Digite a quantidade de parcelas (máximo 6): "))
        
        if parcelas > 6 or parcelas < 1:
            print("Número de parcelas inválido. O máximo permitido é 6.")
        else:
            valor_parcela = valor_produto / parcelas
            
            print(f"\nValor do produto: R$ {valor_produto:.2f}")
            print("Forma de pagamento: A prazo")
            print(f"Quantidade de parcelas: {parcelas}x")
            print(f"Valor da parcela: R$ {valor_parcela:.2f}")
            print(f"Valor total a pagar: R$ {valor_produto:.2f}")

    case _:
        print("Forma de pagamento inválida.")




