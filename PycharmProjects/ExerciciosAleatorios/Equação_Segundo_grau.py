import math

print("Vamos fazer uma equação do 2°Grau")

print("1)x²+bx+c=0")
#a= 1 b =-1 c = -12

valor_a = int(input("Digite o valor de a: "))
valor_b = int(input("Digite o valor de b: "))
valor_c = int(input("Digite o valor de c: "))

print("1) {}x²+{}x+{}=0".format(valor_a, valor_b, valor_c))

delta = (valor_b * valor_b) + ((- 4) * valor_a) * valor_c

print(delta)

raiz = math.sqrt(delta)

print(raiz)

x1 = -((valor_b) - raiz )/ (2 * valor_a)
x2 = -((valor_b) + raiz )/ (2 * valor_a)

print("Valor do x1 {} \nValor do x2 {}".format(x1,x2))
