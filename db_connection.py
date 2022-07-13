import mysql.connector  # Importa o MySql
from mysql.connector import errorcode  # Trata as execções que irão surgir


class DbConnection:

    def __init__(self):
        self.__connection = mysql.connector.connect(host='localhost',
                                                    user='root',
                                                    password='',
                                                    database='YoutubeVideoConverter')

    # Função para conectar com o banco de dados
    def conectar(self):
        try:
            return self.__connection

        # Guardando as possíveis exceções de mysql.connector na variável 'error'
        except mysql.connector.Error as error:

            # Caso o banco de dados não exista
            if error.errno == errorcode.ER_NO_DB_ERROR:
                print(f'Banco de dados não existe.\n{error.msg}')

            # Caso o banco de dados esteja com o usuário ou senha incorretos.
            elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print(f'Usuário ou senha de acesso ao Banco de Dados estão incorretos.\n{error.msg}')

            # Caso o banco de dados tenha algum outro erro de código
            elif error.errno == errorcode.ER_BAD_DB_ERROR:
                print(f'Erro de conexão com o Banco de dados.\n {error}')

            # Quaisquer outros erros com o banco de dados
            else:
                print(error.msg)

        else:
            self.__connection.close()
