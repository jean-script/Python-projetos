

class Funcionario:
    def __init__(self, nome):
        self.nome = nome
    def registra_horas(self, horas):
        print('Horas registradas...')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')

class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')

class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')

#MIXINS
class Hipster:
    def __str__(self):
        return f'hipster, {self.nome}'

class Junior(Alura):
    pass

class Pleno(Alura, Caelum):
    pass

class Senior(Alura, Caelum, Hipster):
    pass



jose = Junior('Jose')
jose.busca_perguntas_sem_resposta()
jose.mostrar_tarefas()

Luan = Pleno('Luan')
Luan.busca_perguntas_sem_resposta()
Luan.busca_cursos_do_mes()

Luan.mostrar_tarefas()

joao = Senior('joao')
print(joao)

#MRO
# pleno > alura ->funvionarios -> Caelum -> funcionarios