import re


class ExtratorUrl:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str: # __eq__
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError("A url não é valida")

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base


    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)

        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return f'A URL: {self.url} \n os parametros: {self.get_url_parametros()}\n ' \
               f'URL base: { self.get_url_base()}'

    def __eq__(self, other):
        return self.url == other.url


# print('__len__' in dir(str))

url = "https://bytebank.com/cambio?moedaDestino=4.75&quantidade=100&moedaOrigem=10.0"
extrator_url = ExtratorUrl(url)

Valor_dolar = extrator_url.get_valor_parametro('moedaDestino')
valor_real = extrator_url.get_valor_parametro('moedaOrigem')


valor_real_int = float(valor_real)
valor_dolar_int = float(Valor_dolar)

conversao = valor_real_int * valor_dolar_int
print("Conversão do dolar para real. valor dolar: {}, valor real {} = {} ".format(valor_dolar_int, valor_real_int, conversao))













# url = "https://bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real"
# extrator_url = ExtratorUrl(url)
# extrator_url2 = ExtratorUrl(url)
# print(id(extrator_url))
# print(id(extrator_url2))
# print("são iguais? ",extrator_url == extrator_url2)
# # extrator_url = ExtratorUrl(None)
#
# print(extrator_url)
# # valor_quantidade = extrator_url.get_valor_parametro('quantidade')
# # print(valor_quantidade)
#
# print("O tamanho da URL: ", len(extrator_url))

