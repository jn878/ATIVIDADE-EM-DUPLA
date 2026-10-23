import os



renda = float(input("digite sua renda mensal "))
emprestimo = float(input("digite o valor do emprestimo "))
prestacao_valor = int(input("digite o valor das prestações  "))




if emprestimo <= 0.10 * renda or  prestacao_valor <= 0.3 * renda :
    print(" emprestimo aprovado com sucesso !")
else:
    print("emprestimo foi negado")

