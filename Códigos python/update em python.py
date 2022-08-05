import mysql.connector

conexao = mysql.connector.connect(
    host ='localhost',
    user = 'root',
    password = '980922Ged*',
    database ='sucos'
)

cursor = conexao.cursor()

comando_update =f'ALTER TABLE youtube ADD PRIMARY KEY(MATRICULA)'

cursor.execute(comando_update)

conexao.commit()

cursor.close()
conexao.close()
