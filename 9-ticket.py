import os
os.system('cls')

print("RESTAURANTE SABOR DA TERRA - CARDÁPIO ")
print("1 - Feijoada Completa: R$ 35.00")
print("2 - Bife a Cavalo: R$ 28.00")
print("3 - Frango Grelhado: R$ 22.00")
print("4 - Moqueca de Peixe: R$ 40.00")
print("5 - Salada da Casa: R$ 18.00")

total = 0.0
quantidade = 0
continuar = "S"

while continuar == "S" or continuar == "s":
    codigo = input("\nDigite o codigo do prato (1 a 5): ")

    match codigo:
        case "1":
            total = total + 35.00
            quantidade = quantidade + 1
            print("Feijoada adicionada!")
        case "2":
            total = total + 28.00
            quantidade = quantidade + 1
            print("Bife a Cavalo adicionado!")
        case "3":
            total = total + 22.00
            quantidade = quantidade + 1
            print("Frango Grelhado adicionado!")
        case "4":
            total = total + 40.00
            quantidade = quantidade + 1
            print("Moqueca de Peixe adicionada!")
        case "5":
            total = total + 18.00
            quantidade = quantidade + 1
            print("Salada da Casa adicionada!")
        case _:
            print("Codigo invalido, tente novamente.")

    continuar = input("Deseja outro prato? (S/N): ")

print("\n--- RESUMO DO PEDIDO ---")
print("Quantidade de pratos:", quantidade)
print("Total a pagar: R$", total)