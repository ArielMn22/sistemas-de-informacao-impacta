# Calcula Preço com Desconto
# By: Ariel Paixão
# GitHub: ArielMn22

preco = float(input())
qnt = int(input())

# Preço total (Sem Desconto)
precoTotal = preco * qnt
print('{:.2f}'.format(precoTotal))

# Preço com desconto (10% fixo mais 1% a cada unidade)
precoComDesconto = precoTotal - ((precoTotal * 0.1) + (precoTotal * (qnt / 100)))

print('{:.2f}'.format(precoComDesconto))
