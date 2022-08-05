
#Variavel type str
nome = "Jean Carlos"
print(type(nome))

#variavel type int
numero = 20
print(type(numero))

#variavel type float
ndecimal = 3.1415
print(type(ndecimal))

#variavel type list
lista = [nome, numero, ndecimal, "Jean Carlos"]
print(type(lista))

#variavel type dic 
dic = {"Nome": nome, "numero":numero, "float":ndecimal, "lista":lista}
print(type(dic))

#variavel type tupla
tupla = ("Jean", "Maria", 12, 3.55, dic, lista)
print(type(tupla))

print(tupla)

lista.append("Murilo")

print(tupla)

print(set(lista))
