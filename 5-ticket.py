import os
import time

multiplicacao = 0

numero = int(input("digite um numero para exibir a tabuada "))

for i in range(1,11):
    resultado = numero + i
    print(f"{numero} * {i} = {resultado}")

time.sleep(1)