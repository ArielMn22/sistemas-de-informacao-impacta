# Anos bissextos
# By: Ariel Paixão
# GitHub: ArielMn22

anoInicio = int(input())
anoFim = int(input())

i = anoInicio
bissextosCount = 0

while (i <= anoFim):
  if ((i % 4 == 0 and i % 100 != 0) == True or (i % 400 == 0) == True):
    print(i)
    bissextosCount += 1
  i += 1

print('bissextos: ' + str(bissextosCount))