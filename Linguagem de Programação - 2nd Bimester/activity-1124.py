# Jogo do par ou ímpar
# By: Ariel Paixão
# GitHub: ArielMn22

numero = int(input())

def checaSeEhPar(n):
  if (n % 2 == 0):
    return True
  else: 
    return False

# Se for maior que 
if (numero >= 2):
  if (checaSeEhPar(numero)):
    print(str(numero - 1) + " " + str(numero + 2))
  else:
    print(str(numero - 2) + " " + str(numero + 1))