

def dividir(dividendo, divisor):
    if not (isinstance(dividendo, int) and isinstance(divisor, int)):
        raise ValueError("Dividir deve receber argumentos inteiros")
    try:
        aux = dividendo / divisor
    except:
        print(f"Não foi possível dividir {dividendo} por {divisor}")
        raise

    return aux

def teste_divisao(divisor):
    resultado = dividir(10, divisor)
    print(f'O resultado da divisor de 10 por {divisor} é {resultado})')


# try:
#     teste_divisao(1.5)
# except ZeroDivisionError as E:
#     print("Erro de divisão por zero")
#
#
# print("programa encerrado")


try:
    print("O fluxo esta aqui")
    raise ValueError("teste")
except Exception:
     print(f"Agora ele foi para cá")
print("E enfim ele continua...")