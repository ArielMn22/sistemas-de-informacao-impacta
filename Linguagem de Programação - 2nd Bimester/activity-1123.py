# Conversor de centímetros em polegadas
# By: Ariel Paixão
# GitHub: ArielMn22

CENTIMETROS_POR_POLEGADA = 2.54

centimetros = float(input())

polegadas = centimetros * CENTIMETROS_POR_POLEGADA

print('{:.3f}'.format(polegadas))