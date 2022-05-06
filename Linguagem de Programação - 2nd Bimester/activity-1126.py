# Cálculo de notas
# By: Ariel Paixão
# GitHub: ArielMn2

diasDaSemana = [ 'domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado' ]

qntDias = len(diasDaSemana)

diaEscolhido = input()
diasDeEspera = int(input())

if (diasDeEspera == 0):
  print('chega hoje!')
else:
  i = 0
  while (i < len(diasDaSemana)):
    if (diasDaSemana[i] == diaEscolhido):
      if ((i + diasDeEspera) > (qntDias - 1)): # Irá estourar o array
        print('sera entregue ' + diasDaSemana[i + diasDeEspera - qntDias])
      else:
        print('sera entregue ' + diasDaSemana[i + diasDeEspera])
    i += 1