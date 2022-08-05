import mysql.connector

import requests, json

url = requests.get("")
text = url.text
print(type(text))

conexao = mysql.connector.connect(
    host ='localhost',
    user = 'root',
    password = 'senha',
    database ='sucos'
)


nome = "Fernanda carolina"
data_nascimento = '1998-02-22'

cursor = conexao.cursor()

comando_insert = f'INSERT INTO INSCRITOS (NOME,DATA_NASCIMENTO) VALUES ("{nome}",{data_nascimento})'

cursor.execute(comando_insert)

conexao.commit() # quando edita o banco de dados

#resultado = cursor.fetchall() # ler banco de dados

cursor.close()
conexao.close()
