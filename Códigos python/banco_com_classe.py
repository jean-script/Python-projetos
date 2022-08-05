import mysql.connector
from classe import Cliente

def inicia_cadastro(nome, data, endereco):

    conexao = mysql.connector.connect(
        host ='localhost',
        user = 'root',
        password = 'senha*',
        database ='sucos'
    )

    cliente = Cliente(f'{nome}', f'{data}',f'{endereco}')

    cursor = conexao.cursor()

    comando_insert = f'INSERT INTO INSCRITOS (NOME, DATA_NASCIMENTO, ENDERECO) VALUES("{cliente.nome}","{cliente.data}","{cliente.endereco}")'

    cursor.execute(comando_insert)

    conexao.commit()

    cursor.close()
    conexao.close()
