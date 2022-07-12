import db_connection
import this
from rich.console import Console
from rich import box
from rich.table import Table


class Dao:

    def __init__(self):
        this.__db = db_connection.DbConnection.conectar()
        this.__con = this.__db.cursor()

    @staticmethod
    def inserir(nome, arquivo):
        try:
            texto_codigo = f"INSERT INTO midia(idMidia, nome, arquivo) VALUES('','{nome}','{arquivo}')"
            this.__con.execute(texto_codigo)
            this.__db.commit()

            return print(f'{this.__con.rowcount} linha(s) afetada(s).')

        except Exception as error:
            return print(f'Erro no comando inserir.\n{error}')

    @staticmethod
    def excluir(codigo):
        try:
            texto_codigo = f"DELETE FROM midia WHERE idMidia = '{codigo}'"
            this.__con.execute(texto_codigo)
            this.__db.commit()
            if this.__con.rowcount == 0:
                Console().print("Código não encontrado. Digite um código existente.", style="red")
            else:
                print(f'{this.__con.rowcount} linha(s) afetada(s)')

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
