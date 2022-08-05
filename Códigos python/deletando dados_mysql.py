import mysql.connector

conexao = mysql.connector.connect(
    host ='localhost',
    user = 'root',
    password = '980922Ged*',
    database ='sucos'
)

cursor = conexao.cursor()

comando_update =f'DELETE FROM youtube WHERE MATRICULA = "123"'

cursor.execute(comando_update)

conexao.commit()


cursor.close()
conexao.close()