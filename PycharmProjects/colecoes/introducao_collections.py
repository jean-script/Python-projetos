
#
# idades = [39, 30, 27, 18]
#
# print(type(idades))
#
# print(len(idades))
#
# idades.append(15)
#
# print(idades)
#
# for idade in idades:
#     print(idade)
#
# idades.remove(30)
# print(idades)
#
# idades.insert(0,12)
#
# print(idades)
#
# # idades.clear()
#
# print(28 in idades)
#
# print(15 in idades)
#
# if 15 in idades:
#     idades.remove(15)
#
# idades.insert(0,20)
#
# print(idades)
#
# idades.extend([27,19])
#
# print(idades)
#
#
#
# idades_no_ano_que_vem = []
#
# for idade in idades:
#     idades_no_ano_que_vem.append(idade + 1)
#
# print(idades_no_ano_que_vem)
#
#
# #list comprehension
# idades_no_ano_que_vem = [(idade+1) for idade in idades]
# print(idades_no_ano_que_vem)
#
# idade_maior_21 = [(idade) for idade in idades if idade > 21]
# print(idade_maior_21)
#
# def faz_processamento_visualizacao(lista):
#     print(len(lista))
#
# faz_processamento_visualizacao(idades)

def faz_processamento_visualizacao(lista = None):
    if lista == None:
        lista = list()
    print(len(lista))
    print(lista)
    lista.append(13)

faz_processamento_visualizacao()
faz_processamento_visualizacao()





