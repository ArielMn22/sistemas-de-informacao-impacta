# Corra Forrest!
# By: Ariel Paixão
# GitHub: ArielMn22

# Declarações
corridas = []

km = 0

while km >= 0:
  km = int(input())
  if (km >= 0):
    corridas.append(km)

soma = 0

for num in corridas:
  soma += num

media = soma / len(corridas)

print("MEDIA: " + "{:.2f}".format(media))

for num in corridas:
  if num < media:
    print(num)