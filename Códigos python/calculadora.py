


class Calculadora:
    """
        classe para simular as funções de uma calculadora.
    """
    def __init__(self, numero1, numero2):
        self.__num1 = numero1
        self.__num2 = numero2
        
    @property
    def adicao(self):
        soma = f'A adição do {self.__num1} + {self.__num2} = {self.__num1 + self.__num2}'
        return soma
    
    @property
    def subtracao(self):
        soma = f'A subtração de {self.__num1} - {self.__num2} = {self.__num1 - self.__num2}'
        return soma
    
    @property
    def multiplicacao(self):
        soma = f'A Multiplicação de {self.__num1} * {self.__num2} = {self.__num1 * self.__num2}'
        return soma
    
    @property
    def exponeciacao(self):
        soma = f'O numero {self.__num1} elevado a {self.__num2} é igual a  = {self.__num1 ** self.__num2}'
        return soma
    
    @property
    def num1(self):
        return f'Este é o numero 1: {self.__num1}'
    
    @property
    def num2(self):
        return f'Este é o numero 2: {self.__num2}'
    
    @num1.setter
    def define_num1(self, novo_num):
        self.__num1 = novo_num
        
    @num2.setter
    def define_num2(self, novo_num):
        self.__num2 = novo_num
    
    def __str__(self):
        return f'Calculadora é um dispositivo para a realização de cálculos numéricos.'





calculadora = Calculadora(2,3)

print(calculadora.adicao)
print(calculadora.subtracao)
print(calculadora.multiplicacao)
print(calculadora.exponeciacao)
print(calculadora.num1)
print(calculadora.num2)
calculadora.define_num1 = 10
calculadora.define_num2 = 14
print(calculadora.num1)
print(calculadora.num2)


print(calculadora)
