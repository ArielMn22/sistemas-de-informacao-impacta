# Programação Orientada a Objetos
# AC01 POO-EaD - Números especiais
#
# Email Impacta: ariel.paixao@aluno.faculdadeimpacta.com.br

def eh_primo(n):
  for i in range(2, n):
    if (n % i == 0):
      return False
    
  return n > 1

def lista_primos(n):
	primos = []

	for i in range(1, n):
		if eh_primo(i):
			primos.append(i)

	print(str(primos))

	return primos

def conta_primos(s):
	obj = {}

	for n in s:
		if eh_primo(n):
			if n in obj:
				obj[n] = obj[n] + 1
			else:
				obj[n] = 1

	print(str(obj))
	return obj

def eh_armstrong(n):
	ehArmstrong = False

	strN = str(n)
	nLen = len(strN)

	sum = 0
	for algarism in strN:
		algarism = int(algarism)
		sum += algarism ** nLen

	if (sum == n):
		ehArmstrong = True
	else:
		ehArmstrong = False

	print(str(ehArmstrong))

	return ehArmstrong
	
def eh_quase_armstrong(n):
	ehArmstrong = False
	
	if eh_armstrong(n):
		ehArmstrong = False
		print(ehArmstrong)
		return ehArmstrong

	strN = str(n)
	nLen = len(strN)

	sum = 0
	for algarism in strN:
		algarism = int(algarism)
		sum += algarism ** nLen

	if sum + 1 == n:
		ehArmstrong = True
	elif sum - 1 == n:
		ehArmstrong = True
	else:
		ehArmstrong = False

	print(str(ehArmstrong))

	return ehArmstrong

def lista_armstrong(n):
	armstrongs = []

	for i in range(n):
		if eh_armstrong(i):
			armstrongs.append(i)

	print(str(armstrongs))
	return armstrongs

def eh_perfeito(n):
	ehPerfeito = False

	divisores = []

	for i in range(n):
		if (i > 0):
			if (n % i == 0):
				divisores.append(i)

	soma = 0
	for j in divisores:
		soma += j

	if soma == n:
		ehPerfeito = True
	else:
		ehPerfeito = False

	return ehPerfeito

def lista_perfeitos(n):
	perfeitos = []

	for i in range(n):
		if eh_perfeito(i):
			perfeitos.append(i)

	print(str(perfeitos))
	return perfeitos