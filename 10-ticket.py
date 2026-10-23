import os
os.system('cls')

salarios = []
filhos = []

while True:
    print("\n--- MENU ---")
    print("1 – Adicionar família")
    print("2 – Sair e exibir resultados")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        salario = float(input("Digite o salário da família: R$ "))
        num_filhos = int(input("Digite o número de filhos: "))
        
        salarios.append(salario)
        filhos.append(num_filhos)
        print("Família cadastrada com sucesso!")
        
    elif opcao == "2":
        if len(salarios) > 0:
            total_familias = len(salarios)
            media_salario = sum(salarios) / total_familias
            media_filhos = sum(filhos) / total_familias
            maior_salario = max(salarios)
            menor_salario = min(salarios)
            
            print("\n=== RESULTADOS DA PESQUISA ===")
            print(f"Total de famílias pesquisadas: {total_familias}")
            print(f"Média de salário: R$ {media_salario:.2f}")
            print(f"Média de filhos: {media_filhos:.1f}")
            print(f"Maior salário: R$ {maior_salario:.2f}")
            print(f"Menor salário: R$ {menor_salario:.2f}")
        else:
            print("\nNenhuma família foi cadastrada.")
            
        print("Encerrando o sistema...")
        break
        
    else:
        print("Opção inválida! Digite 1 ou 2.")