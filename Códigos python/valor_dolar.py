import requests

url = 'https://economia.awesomeapi.com.br/all/USD-BRL'

resposta = requests.get(url)

if resposta.status_code == 200:
    dolar_value = resposta.json()['USD']['low']
    print(f'O valor do dolar é R${dolar_value}')
else:
    print('Erro na busca do valor do dolar')