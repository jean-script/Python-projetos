
from abc import ABCMeta, abstractmethod

class Conta(metaclass= ABCMeta):
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo= 0

    # forçar todas as class filhar terem esse metodo
    @abstractmethod
    def passa_mes(self):
        pass

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return "[>> Codigo: {} Saldo {} <<]".format(self._codigo, self._saldo)

class ContaCorrente(Conta):
    def passa_mes(self):
        self._saldo -= 2

class ContaPoupaca(Conta):
    def passa_mes(self):
        self._saldo *=1.01
        self._saldo -=3

class ContaInvestimento(Conta):
    pass

#print(ContaInvestimento(764))

conta16 = ContaCorrente(16)
#print(conta16)
conta16.deposita(1000)
#conta16.passa_mes()
#print(conta16)

conta17 = ContaPoupaca(17)
#print(conta17)
conta17.deposita(1000)
#conta17.passa_mes()
#print(conta17)

contas = [conta16, conta17]

#for conta in contas:
    #conta.passa_mes()
    #print(conta)

class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, other):
        if type(other) != ContaSalario:
            return False
        return self._codigo == other._codigo

    def __lt__(self, other):
        return self._saldo < other._saldo

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)

class ContaMultiploSalario(ContaSalario):
    pass

#conta1 = ContaSalario(37)
#conta2 = ContaCorrente(37)

#print(conta1 == conta2)


#print(isinstance(ContaCorrente(34), Conta))

conta_do_guilherme = ContaSalario(17)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(510)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]

from operator import attrgetter

#def extrai_saldo(conta):
    #return conta._saldo

#for conta in sorted(contas, key=attrgetter("_saldo")):
    #print(conta)
print(conta_do_guilherme < conta_da_daniela)
print(conta_do_guilherme > conta_da_daniela)

for conta in sorted(contas, reverse=True):
    print(conta)

