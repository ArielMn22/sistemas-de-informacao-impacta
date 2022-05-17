# Cálculo de notas
# By: Ariel Paixão
# GitHub: ArielMn22

numero = int(input())

alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def mostraTabuada (n):
  i = 0

  while (i < n):
    j = 0
    while (j <= i):
      print(alfabeto[i], end='')
      j += 1
    print('')
    i += 1

if (numero >= 1 and numero <= 26):
  mostraTabuada(numero)