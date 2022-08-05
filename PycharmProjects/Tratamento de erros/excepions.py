

class OperacaoFinanceiraError(Exception):
    pass

class SaldoinsuficienteError(OperacaoFinanceiraError):
    def __init__(self, messagen ="", saldo=None, valor=None, *args):
        self.saldo = saldo
        self.valor = valor
        msg = 'Saldo insulfisiente para efetuar a transação\n'\
            f'Saldo atual: {self.saldo} valor a ser sacado: {self.valor}'
        self.msg = messagen or msg
        super(SaldoinsuficienteError, self).__init__(self.msg, self.saldo,self.valor, *args)

