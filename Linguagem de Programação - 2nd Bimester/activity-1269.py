# Carrinho de compras
# By: Ariel Paixão
# GitHub: ArielMn22

# Declarações
entradasAnteriores = input().split()

lista = []
if (len(entradasAnteriores) > 0):
  for entrada in entradasAnteriores:
    lista.append(int(entrada))

continuarNoLoop = True

# Bubble Sort
def troca(v, i, j):
  temp = v[i]
  v[i] = v[j]
  v[j] = temp
  return

def empurra (v, n):
  i = 0
  while i < n - 1:
    if (v[i] > v[i + 1]):
      troca(v, i, i + 1)
    i += 1

  return

def bubbleSort(v):
  tam = len(v)

  while tam > 1:
    empurra(v, tam)
    tam -= 1
  
  return v

# Métodos
def adicionar (codigo):
  lista.append(codigo)

def remover (codigo):
  if codigo in lista:
    lista.remove(codigo)
  else:
    print('código ' + str(codigo) + ' não encontrado')

def exibir ():
  listaOrdenada = bubbleSort(lista)

  for codigo in listaOrdenada:
    print(codigo, end=' ')

  print('')

while (continuarNoLoop):
  entradas = input().split()

  if len(entradas) > 1:
    entradas[1] = int(entradas[1])

  if (entradas[0] == 'adicionar'):
    adicionar(entradas[1])
  elif (entradas[0] == 'remover'):
    remover(entradas[1])
  elif(entradas[0] == 'exibir'):
    exibir()
  elif(entradas[0] == 'encerrar'):
    exibir()
    continuarNoLoop = False