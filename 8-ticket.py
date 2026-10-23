import os
os.system('cls')

print("=== CADASTRO ===")
login_cadastrado = input("Cadastre seu login: ")
senha_cadastrada = input("Cadastre sua senha: ")

print("\n" * 30)

print("=== Acesso ao Sistema ===")

tentativas = 0
limite_tentativas = 3
acesso_concedido = False

while tentativas < limite_tentativas:
    login_input = input("Digite seu login: ")
    senha_input = input("Digite sua senha: ")

    if login_input == login_cadastrado and senha_input == senha_cadastrada:
        acesso_concedido = True
        break
    else:
        tentativas += 1
        tentativas_restantes = limite_tentativas - tentativas

        if tentativas_restantes > 0:
            print(f"Login ou senha incorretos! Você ainda tem {tentativas_restantes} tentativa(s).\n")

if acesso_concedido:
    print(f"\nSeja bem-vindo(a) ao portal!")
else:
    print("\nNúmero máximo de tentativas excedido. Acesso bloqueado!")