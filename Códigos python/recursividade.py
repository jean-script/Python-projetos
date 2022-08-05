

# def conta(n):
#     n = n + 1
#     if n <= 10:
#         print(n)
#         conta(n)
#     else:
#         print("Numero é igual a 10")

# conta(0)

nomes = []
contador = 0
while (contador < 2):
    nome = input("Digite seu nome: ").strip().title() 
    nomes.append(nome)
    contador += 1
    
    
for nome in nomes:    
    print("Hello {}".format(nome))