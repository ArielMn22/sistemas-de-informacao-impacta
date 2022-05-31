# ImpacTube
# By: Ariel Paixão
# GitHub: ArielMn22

# Declarações
informacoesDosCanais = []
canaisQnt = int(input())

i = 0
while (i < canaisQnt):
  informacoes = input()
  informacoesDosCanais.append(informacoes)
  i += 1

valorPremium = float(input())
valorNonPremium = float(input())

print('-----')
print('BÔNUS')
print('-----')

for canal in informacoesDosCanais:
  infos = canal.split(';')

  nomeCanal = infos[0]
  inscritosQnt = int(infos[1])
  faturamentoMesAnterior = float(infos[2])
  ehPremium = infos[3]

  novoFaturamento = 0

  multiplicador = inscritosQnt // 1000

  if (ehPremium == 'sim'):
    novoFaturamento = faturamentoMesAnterior + (multiplicador * valorPremium)
  else:
    novoFaturamento = faturamentoMesAnterior + (multiplicador * valorNonPremium)

  print(nomeCanal + ":" + " R$ " + "{:.2f}".format(novoFaturamento))