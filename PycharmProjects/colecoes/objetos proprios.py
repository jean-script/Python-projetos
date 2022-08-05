

# Objetos proprios

class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo= 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return "[>> Codigo: {} Saldo {} <<]".format(self.codigo, self.saldo)

conta_gui = ContaCorrente(15)
conta_gui.deposita(500)
#print(conta_gui)

conta_dani = ContaCorrente(14)
conta_dani.deposita(1000)
#print(conta_dani)

contas = [conta_gui, conta_dani]
#print(contas)

def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)


print(contas[0], contas[1])
deposita_para_todas(contas)
print(contas[0], contas[1])

guilherme = ('Guilherme', 37, 1981)
daniela = ('Daniela', 31, 1987)

usuarios = [guilherme, daniela]

usuarios.append(('Paulo', 39, 1979))

print(usuarios)