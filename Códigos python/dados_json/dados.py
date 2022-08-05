
class Funcionario:
    def __init__(self, nome, data_nascimento, profissao, salario):
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__profissao = profissao
        self.__salario = salario
             
    @property
    def nome(self):
        return self.__nome
    
    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @property
    def profissao(self):
        return self.__profissao
    
    @profissao.setter
    def muda_profissao(self, nova_profissao):
        self.__profissao = nova_profissao
        
    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def aumento_salario(self, novo_salario):
        self.__salario += novo_salario
        
        
        
        
        
jean = Funcionario("Jean Carlos", "03/03/2001", "Estagiario", 1800.00)

print(f'\
    \nNome do funcionario: {jean.nome}\n\
    Data de nascimento: {jean.data_nascimento}\n\
    Cargo: {jean.profissao}\n\
    Salario inicial: %.2f' % (jean.salario))


jean.aumento_salario = 400
jean.muda_profissao = "desenvolvedor junior"


print(f'\
    \nNome do funcionario: {jean.nome}\n\
    Data de nascimento: {jean.data_nascimento}\n\
    Cargo: {jean.profissao}\n\
    Salario inicial: %.2f' % (jean.salario))
