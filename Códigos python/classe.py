

class Cliente:
    
    #construtor da classe
    def __init__(self, nome, data, endereco):
        self.__nome = nome      #o andercor indica que o elemento é privado
        self.__data = data
        self.__endereco = endereco
        
    @property  #property indica que a função é um get todo get retorna algo
    def nome (self):
        return self.__nome.upper()
    
    @property
    def data(self):
        return self.__data
    
    @property
    def endereco (self):
        return self.__endereco
    
    @property
    def mensagem (self):
        return print("O cliente {} nasceu no {} e mora no endereço {} ".format(self.__nome, self.__data, self.__endereco))
    
    @endereco.setter
    def enderecoSet(self, endereco):
        self.__endereco = endereco


jean = Cliente("jean", '03/03/2001','jardim paulistano')

print(f'{jean.endereco}')

jean.enderecoSet = 'Piqueri'

print(f'{jean.endereco}')
