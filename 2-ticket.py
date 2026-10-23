import os

quantidade = 0
preco = 0

produto = input("qual produto foi adquirido ")
quantidade = int(input("quantidade de produtos "))
preco = float(input("preço unitario dos produtos "))


#2% de desconto
if quantidade == 5:
    desconto = preco * 0.02

#desconto 3%
elif quantidade >= 6 and 10:
    desconto = preco  * 0.03
else:
    desconto = preco * 0.05




total = quantidade * preco
desconto_total = total - desconto
print(f"total = {total}")
print(f"total com desconto = {desconto_total}")