import os
os.system('cls')

pares = 0
impares = 0
soma = 0

for i in range(5):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
    soma += numero
    
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print("\n--- RESUMO DOS DADOS ---")
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
print(f"Soma de todos os números: {soma}")