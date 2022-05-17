# Números Primos
# By: Ariel Paixão
# GitHub: ArielMn22

def ehPrimo (n) :
  for i in range(2, n):
    if (n % i == 0):
      return False
    
  return n > 1

inicio = int(input())
fim = int(input())

i = inicio
primosCount = 0

while (i <= fim):
  if(ehPrimo(i)):
    print(i)
    primosCount += 1
  i += 1

print('primos: ' + str(primosCount))
