# url = "https://bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real"

url = ""

#sanitização da url
url = url.strip()

#validação url
if url == "":
    raise ValueError("A url esta vazia")

#separa a base e parâmetros
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao + 1:]
print(url_parametros)

#busca o valor de um parâmetro
parametro_busca = 'quantidade'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)

if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]

print(valor)
