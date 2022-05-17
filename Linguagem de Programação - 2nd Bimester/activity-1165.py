# Cálculo de notas
# By: Ariel Paixão
# GitHub: ArielMn22

i = 0
numero = 0
somaVCoins = 0

while (numero >= 0):
  numero = float(input())

  if (numero >= 0): 
    somaVCoins += numero

print('VC$ ' + '{0:.2f}'.format(somaVCoins))
print('R$ ' + '{0:.2f}'.format(somaVCoins * 2.50))