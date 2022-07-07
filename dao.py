import db_connection
import this
from rich.console import Console

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
            return print(f'Erro no comando inserir.\n{error.msg}')

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
