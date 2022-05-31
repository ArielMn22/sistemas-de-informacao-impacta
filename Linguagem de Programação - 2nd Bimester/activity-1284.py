# Segunda Chance
# By: Ariel Paixão
# GitHub: ArielMn22

# Declarações
alunosQnt = int(input())

def formataNumero (numero):
  formatado = "{:05.2f}".format(numero)
  return formatado

# Recebe notas anteriores
notasAnteriores = []
i = 1
while i <= alunosQnt:
  notaAnterior = float(input())
  notasAnteriores.append(notaAnterior)
  i += 1

# Recebe notas novas
notasNovas = []
j = 1
while j <= alunosQnt:
  notaNova = float(input())
  notasNovas.append(notaNova)
  j += 1

notasAlteradas = 0

k = 0

# Processamento das notas
while k < len(notasAnteriores):
  if notasAnteriores[k] == 10:
    notasNovas[k] = 10

  if notasNovas[k] == 10:
    notasNovas[k] = notasAnteriores[k] + 2
  else:
    notasNovas[k] = notasAnteriores[k]

  if notasAnteriores[k] == 0:
    notasNovas[k] = 0

  # Limitador de nota máxima
  if notasNovas[k] > 10:
    notasNovas[k] = 10

  if notasAnteriores[k] != notasNovas[k]:
    notasAlteradas += 1
  k += 1

k = 0

print("NOTAS ALTERADAS: " + str(notasAlteradas))

while k < len(notasAnteriores):
  if notasAnteriores[k] != notasNovas[k]:
    print('* (' + "{:03}".format(k+1) + ') original: ' + formataNumero(notasAnteriores[k]) + ' | final: ' + formataNumero(notasNovas[k]))
  else:
    print('- (' + "{:03}".format(k+1) + ') original: ' + formataNumero(notasAnteriores[k]) + ' | final: ' + formataNumero(notasNovas[k]))
  k += 1