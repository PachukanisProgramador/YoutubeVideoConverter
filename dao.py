import db_connection
from rich.console import Console
from rich import box
from rich.table import Table
import time


class Dao:
    # Método construtor
    def __init__(self):
        self.__db = db_connection.DbConnection().conectar()
        self.__con = self.__db.cursor()

    # Função para inserir linha no banco de dados
    def inserir(self, nome, arquivo):
        try:
            # Executando comando no MySql
            texto_codigo = f"INSERT INTO midia(idMidia, nome, arquivo) VALUES('','{nome}','{arquivo}')"
            self.__con.execute(texto_codigo)
            self.__db.commit()

            return print(f'{self.__con.rowcount} linha(s) afetada(s).')

        except Exception as error:
            return print(f'Erro no comando inserir.\n{error}')

    # Função para excluir alguma linha no banco de dados
    def excluir(self, codigo):
        try:
            # Executando comando no MySql
            texto_codigo = f"DELETE FROM midia WHERE idMidia = '{codigo}'"
            self.__con.execute(texto_codigo)
            self.__db.commit()

            # Verificando se alguma linha do código foi afetada

            # Caso não tenha sido afetada é por que o código não existe.
            if int(self.__con.rowcount) == 0:
                Console().print("\nCódigo não encontrado. Digite um código existente.", style="red")
                time.sleep(1)
            else:
                print(f'{self.__con.rowcount} linha(s) afetada(s)')
                time.sleep(1)

        except Exception as error:
            print(error)

    # Função para consultar dados no banco de dados e criar tabela como resultado para disponibilizar as informações
    def consultar(self):

        # Criando tabela
        tabela = Table(title="Arquivos MP3",
                       style='bold red',
                       box=box.HEAVY_HEAD,
                       show_lines=True,
                       safe_box=True,
                       expand=True)

        # Adicionando colunas conforme banco de dados e o que eu preciso que seja mostrado (código e nome)
        tabela.add_column("Código", justify="left", style="cyan", no_wrap=True)
        tabela.add_column("Nome", justify="left", style="cyan", no_wrap=True)

        try:
            # Executando comando no mySql
            texto_codigo = 'SELECT * FROM midia'
            self.__con.execute(texto_codigo)

            # Preenchendo tabela com os dados lidos
            for (idMidia, nome, arquivo) in self.__con:
                tabela.add_row(str(idMidia), str(nome))

            # Retornando tabela com as informações para futura manipulação
            return tabela

        except Exception as error:
            print(error.args)

    def buscar(self, codigo):
        try:
            # Executando comando para buscar o nome pelo código
            texto_codigo = f"SELECT * FROM midia WHERE idmidia = '{codigo}'"
            self.__con.execute(texto_codigo)

            # Retornando apenas o nome
            for (idMidia, nome, arquivo) in self.__con:
                return str(nome)

        except Exception as error:
            print(error)
