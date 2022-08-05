from operator import attrgetter
from functools import total_ordering

# fazer que todas as operações de <,>, <=,>= , == funcione apartir de duas funções colocadas
@total_ordering
class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, other):
        if type(other) != ContaSalario:
            return False
        return self._codigo == other._codigo

    def __lt__(self, other):
        if self._saldo != other._saldo:
            return self._saldo < other._saldo
        return self._codigo < other._codigo

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)


conta_do_guilherme = ContaSalario(1700)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(500)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]

#for conta in sorted(contas, key=attrgetter("_saldo", "_codigo")): # ordenação por varios atributos
    #print(conta)

for conta in sorted(contas):
    print(conta)

print(conta_do_guilherme <= conta_da_daniela)

print(conta_do_guilherme <= conta_do_paulo)