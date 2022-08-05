
numeros = []
soma = 0
media = 0
maior_numero = 0
menos_numero = 10000

for numero in range(0, 5, 1):
    
    numeros.append(int(input("Digite um numero: ")))
    
    soma += numeros[numero]

    if (numeros[numero] > maior_numero):
        maior_numero = numeros[numero]    
    
    if(numeros[numero] < menos_numero):
        menos_numero = numeros[numero]    
        

media = soma / len(numeros)  
numeros_ordenados = sorted(numeros)

    
print("Soma de todos os numeros {}".format(soma), end="\n")    
print("A media da soma das idades {}".format(media), end="\n")
print("Este é o maior numero do vetor {}".format(maior_numero), end="\n")
print("Este é o menor numero do vetor {}".format(menos_numero), end="\n")
print("Os numeros ordenados do menor do maior ","{}".format(numeros_ordenados), sep="--", end="")
