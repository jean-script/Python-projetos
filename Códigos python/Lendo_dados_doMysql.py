import mysql.connector

conexao = mysql.connector.connect(
    host ='localhost',
    user = 'root',
    password = 'senha',
    database ='sucos'
)

cursor = conexao.cursor()

comando_insert = f'SELECT * FROM INSCRITOS'

cursor.execute(comando_insert)

resultado = cursor.fetchall() # ler banco de dados
print(resultado)

cursor.close()
conexao.close()
