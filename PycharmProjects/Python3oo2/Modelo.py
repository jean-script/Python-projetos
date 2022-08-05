from abc import ABCMeta, abstractmethod

class Programa(metaclass = ABCMeta):
    def __init__(self, nome, ano):
        self._nome = nome.title() #_Programa__nome
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def dar_like(self):
        self._likes += 1

    @abstractmethod
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} likes'


class Filmes(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome,ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.ano}- {self.duracao} min - {self._likes} likes'


class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome,ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas- {self._likes} likes'

class Playlist:

    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas


    #metodo para fazer um interavel
    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)






vingadores = Filmes('Vingadores - guerra infinita',2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filmes('Todo mundo em pânico', 1999,100)
demolidor = Serie('Demolidor', 2016, 2)

vingadores.dar_like()
tmep.dar_like()
demolidor.dar_like()
atlanta.dar_like()
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta,demolidor,tmep]
plalist_fim_de_semana = Playlist('Fim de semana', filmes_e_series)

print(f'Tamanho da playlist: {len(plalist_fim_de_semana)}')

# comentar mais de uma linha ctrl + /


print(f'Ta ou não esta? {demolidor in plalist_fim_de_semana}')

for programa in plalist_fim_de_semana:
    print(programa)


