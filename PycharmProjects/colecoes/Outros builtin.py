

idades = [15, 87, 32, 65, 56, 32, 49, 37]

#for idade in range(0,len(idades), 1):
  #  print("index: {} Value: {}".format(idade, idades[idade]))

#print(list(enumerate(idades))) #forçar a geração dos valores

#for indice, idade in enumerate(idades): # unpacking da nossa tupla
    #print("indice:",indice, "idade:",idade)

usuarios = [
    ("Guilherme", 37, 1981),
    ("Daniela", 31, 1987),
    ("Paulo", 39, 1979)
]

#for nome, idade, nascimento in usuarios: #ja desempacotando
    #print(nome)

#for nome, _, _ in usuarios: #ja desempacotando, ignorando o resto
   # print(nome)

print(sorted(idades, reverse=True))
print(list(reversed(idades))) #lazy