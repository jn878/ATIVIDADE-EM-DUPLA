import os
os.system('cls')

i = 1
soma = 0

while i <= 3:
    nota = float(input(f"Digite a {i}ª nota (0 a 10): "))
    
    while nota < 0 or nota > 10:
        print("Nota inválida! Digite apenas valores entre 0 e 10.")
        nota = float(input(f"Digite a {i}ª nota novamente: "))
    
    soma = soma + nota
    i = i + 1

media = soma / 3

print(f"\nMédia do aluno: {media:.1f}")

if media >= 7:
    print("Situação: APROVADO")
elif media >= 5:
    print("Situação: RECUPERAÇÃO")
else:
    print("Situação: REPROVADO")