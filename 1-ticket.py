import os
os.system("cls")
QUANTIDADE_DE_NUMEROS = 2


while True:
    for i in range(QUANTIDADE_DE_NUMEROS):
        numeros = float(input(f"digite o {i+1} numero "))

    operação = input("digite um simbolo de operação ")


    match operação:
        case "+":
            soma = numeros + numeros
            print(f"soma = {soma} ")
        case"*":
            multiplicacao = numeros * numeros
            print(f"multiplicação = {multiplicacao}")
        case"-":
            subtracao = numeros - numeros
            print(f"subtração = {subtracao}")
        case"/":
            if numeros > 0:
                divisao = numeros / numeros
                print(f"divisão {divisao}")
            else:
                print("o numero precisa ser maior que 0")
        case _:
            print(" algo deu errado, tente novamente ")

