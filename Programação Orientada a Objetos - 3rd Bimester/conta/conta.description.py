# Programação Orientada a Objetos
# AC02 POO-EaD - Implementação de classes
#
# Email Impacta: ______________@aluno.faculdadeimpacta.com.br

"""
Nesta atividade você deve implementar uma classe que modela uma conta em um banco.
Um "esqueleto" da classe encontra-se montado abaixo, e você deve utilizá-lo
para completar o que falta.
Siga as instruções nos comentários detalhadamente.

OBS: não altere as assinaturas dos métodos, caso contrário sua atividade não será
aprovada pelo corretor automático.
"""


class Conta:

	def __init__(self, titular, agencia, numero, saldo_inicial):
		"""
		Método construtor da classe.
		Crie os seguintes atributos privados no construtor da classe e inicie 
		seus respectivos valores de acordo com as especificações:

		- titular: inicializado através do parâmetro de mesmo nome;
		- agencia: inicializado através do parâmetro de mesmo nome;
		- numero: inicializado através do parâmetro de mesmo nome;
		- saldo: inicializado através do parâmetro saldo_inicial;
		- ativa: inicializado com o valor booleano False;
		- operacoes: lista inicializada com o valor inicial: [('saldo inicial', saldo_inicial)]

		* OBS: note que o(s) valor(es) contido(s) na lista de operações (que é um
		atributo privado) sempre serão tuplas, cada uma com 2 valores.
		*OBS: Note também que os atributos devem ter exatamente o nome especificado, e alguns
		deles são iniciados com valores fixos (não são passados por parâmetro no construtor).
		"""
		pass


	@property
	def titular(self):
		"""
		Implemente a property titular: retorna o valor do atributo privado titular;
		"""
		pass


	@property
	def agencia(self):
		"""
		Implemente a property agencia: retorna o valor do atributo privado agencia;
		"""
		pass
	

	@property
	def numero(self):
		"""
		Implemente a property numero: retorna o valor do atributo privado numero;
		"""
		pass
	

	@property
	def saldo(self):
		"""
		Implemente a property saldo: retorna o valor do atributo privado saldo;
		"""
		pass
	

	@property
	def ativa(self):
		"""
		Implemente a property ativa: retorna o valor do atributo privado ativa;
		"""
		pass
	

	@ativa.setter
	def ativa(self, situacao):
		"""
		Implemente o setter ativa: recebe um valor booleano (situacao), e atribui
		esse valor ao atributo privado ativa.

		*OBS: antes de atribuir o valor recebido no setter ao atributo privado ativa,
		você deve verificar se o tipo de dado do parâmetro situacao é booleano;

		*DICA: Para verificar o tipo de dado de uma variável, você pode utilizar
		a função isinstance(NOME_VARIAVEL, bool) em conjunto com uma estrutura condicional,
		onde NOME_VARIAVEL representa o nome de uma variável ou parâmetro, e bool representa 
		o tipo booleano.
		"""
		pass
	

	def depositar(self, valor):
		"""
		Implemente o método depositar: recebe um valor para depósito na conta,
		adiciona esse valor ao saldo atual (atributo privado saldo), e adiciona a seguinte
		operação ao final da lista de operações (atributo privado operacoes): ('deposito', valor)

		*OBS: Um depósito só pode ser feito se as seguintes condições forem atendidas:
		a conta está ativa e o valor do depósito deve ser maior que zero. Você deve
		implementar essas verificações com uma estrutura condicional.
		"""
		pass


	def sacar(self, valor):
		"""
		Implemente o método sacar: recebe um valor para saque na conta, subtrai esse valor 
		do saldo atual (atributo privado saldo), e adiciona a seguinte operação ao
		final da lista de operações (atributo privado operacoes): ('saque', valor)

		*OBS: Um saque só pode ser feito se as seguintes condições forem atendidas:
		a conta está ativa, o valor do saque deve ser maior que zero, e o valor do
		saque não pode ser maior que o saldo atual da conta. Você deve implementar
		essas verificações com uma estrutura condicional.
		"""
		pass


	def transferir(self, conta_destino, valor):
		"""
		Implemente o método transferir: recebe dois parâmetros: a conta de destino, que é
		um outro objeto já instanciado da classe Conta (isto é, ele possui os métodos 
		depositar e sacar e a property ativa, por exemplo), e o valor da transferência.
		Esse valor será subtraído do saldo atual (atributo privado saldo) da conta 
		de origem (o objeto referenciado pelo parâmetro self) e, em seguida, deve
		ser depositado na conta de destino. Ao final, adiciona a seguinte operação
		no fim da lista de operações (atributo privado operacoes): ('transferencia', valor)

		*OBS: Uma transferencia só pode ser realizada se as seguintes condições
		forem atendidas: a conta de origem e a conta de destino estão ativas (ao mesmo
		tempo), o valor transferido deve ser maior que zero, e o valor transferido
		não pode ser maior que o saldo atual da conta de origem. Você deve implementar
		essas verificações.
		"""
		pass
	

	def tirar_extrato(self):
		"""
		Implemente o método tirar_extrato: retorna a lista de operações (o atributo privado
		operacoes). Essa lista contém todas as operações feitas na conta (abertura da conta,
		deposito, saque, transferencia, etc). Essas informações devem ser armazenadas
		na lista de operações como tuplas, conforme as descrições nos métodos anteriores.
		
		*OBS: note que a descrição das operações contidas nas tuplas não possui acentos.
		Você deve seguir exatamente esse padrão, utilizando letras minúsculas e sem
		acentos.
		"""
		pass


