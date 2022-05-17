# Cálculo de notas
# By: Ariel Paixão
# GitHub: ArielMn22

divida = int(input())
valorDaParcela = int(input())

i = 1
while (divida > 0):
  
  antes = divida

  if ((divida - valorDaParcela) > 0):
    depois = divida - valorDaParcela
  else:
    depois = 0
    
  print('pagamento: ' + str(i))
  print('antes = ' + str(antes))
  print('depois = ' + str(depois))
  print('-----')

  divida = depois

  i += 1