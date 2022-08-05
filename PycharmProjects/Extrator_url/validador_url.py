'''
Exemplos de URLs válidas:
    bytebank.com/cambio
    bytebank.com.br/cambio
    www.bytebank.com/cambio
    www.bytebank.com.br/cambio
    http://www.bytebank.com/cambio
    http://www.bytebank.com.br/cambio
    https://www.bytebank.com/cambio
    https://www.bytebank.com.br/cambio

Exemplos de URLs inválidas:
    https://bytebank/cambio
    https://bytebank.naoexiste/cambio
    ht://bytebank.naoexiste/cambio
'''
# https://www.bytebank.com.br/cambio
import re
#(verificar tudo) [um dos valores]

url = "www.bytebank.com.br/cambio"
padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
match = padrao_url.match(url)

if not match:
    raise ValueError("A url não é valida")
else:
    print("A url é valida")
