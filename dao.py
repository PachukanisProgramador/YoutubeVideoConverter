import db_connection
from rich.console import Console
from rich import box
from rich.table import Table


class Dao:

    def __init__(self):
        self.__db = db_connection.DbConnection.conectar()
        self.__con = self.__db.cursor()

    def inserir(self, nome, arquivo):
        try:
            texto_codigo = f"INSERT INTO midia(idMidia, nome, arquivo) VALUES('','{nome}','{arquivo}')"
            self.__con.execute(texto_codigo)
            self.__db.commit()

            return print(f'{self.__con.rowcount} linha(s) afetada(s).')

        except Exception as error:
            return print(f'Erro no comando inserir.\n{error}')

    def excluir(self, codigo):
        try:
            texto_codigo = f"DELETE FROM midia WHERE idMidia = '{codigo}'"
            self.__con.execute(texto_codigo)
            self.__db.commit()
            if self.__con.rowcount == 0:
                Console().print("Código não encontrado. Digite um código existente.", style="red")
            else:
                print(f'{self.__con.rowcount} linha(s) afetada(s)')

        except Exception as error:
            print(error)

    @staticmethod
    def consultar():
        db = db_connection.DbConnection.conectar()
        con = db.cursor()
        tabela = Table(title="Arquivos MP3",
                       style='bold red',
                       box=box.HEAVY_HEAD,
                       show_lines=True,
                       safe_box=True,
                       expand=True)

        tabela.add_column("Código", justify="left", style="cyan", no_wrap=True)
        tabela.add_column("Nome", justify="left", style="cyan", no_wrap=True)

        try:
            texto_codigo = 'SELECT * FROM midia'
            con.execute(texto_codigo)

            for (idMidia, nome, arquivo) in con:
                tabela.add_row(str(idMidia), str(nome))

            return tabela

        except Exception as error:
            print(error.args)
