# Carrinho Exibindo Tabuadas
# By: Ariel Paixão
# GitHub: ArielMn22

# Declarações
n1 = int(input())
n2 = int(input())

if (n1 > n2):
  print('Nenhuma tabuada no intervalo!')
else:
  i = n1

  while (i <= n2):
    j = 1
    while (j <= 10):
      print(str(i) + ' x ' + str(j) + ' = ' + str(i*j))
      j += 1
    print('----------')
    i += 1