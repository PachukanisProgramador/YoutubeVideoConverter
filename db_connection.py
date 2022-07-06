import mysql.connector  # Importa o MySql
from mysql.connector import errorcode  # Trata as execções que irão surgir


class DbConnection:

    @staticmethod
    def conectar():
        try:
            db_connection = mysql.connector.connect(host='localhost', user='root', password='', database='BancoDeDados')

            print('Conectado com sucesso!')
            return db_connection

        except mysql.connector.Error as error:  # Guardando as possíveis exceções de mysql.connector na variável 'error'

            if error.errno == errorcode.ER_NO_DB_ERROR:  # Caso o bando de dados não exista
                print(f'Banco de dados não existe.\n{error.msg}')
            elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print(f'Usuário ou senha de acesso ao Banco de Dados estão incorretos.\n{error.msg}')
            elif error.errno == errorcode.ER_BAD_DB_ERROR:
                print(f'Erro de conexão com o Banco de dados.\n {error}')
            else:
                print(error.msg)

        else:
            db_connection.close()