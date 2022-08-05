lista = [1,2,3,4,5,6,7,8,9]

tuple(lista)
print(type(tuple(lista)))

tamanho = len(lista)
tipo = type(tuple(lista))

try:
    for itens in range(0,len(lista)):
        print("Indice {} do valor {}".format(itens,lista[itens]))
except:
    print("Houve erro")
finally:
    print(tamanho)
    print(tipo)
    print("Fim do programa")
      