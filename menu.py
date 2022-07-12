import converter
from rich.console import Console
import dao
from rich import box
from rich.table import Table


class Menu:

    def __init__(self):
        Console().print('\n\n\n===================================\n'
                        'BEM-VINDO AO CONVERSOR DE ARQUIVOS!\n'
                        '===================================\n\n', style='bold yellow')
        pass

    @staticmethod
    def opcoes():
        opcao = -1

        try:
            while opcao != 0:
                opcao = int(input('Deseja converter links únicos ou uma playlist?\n\n'
                                  '1. Links únicos\n'
                                  '2. Playlist\n'
                                  '3. Excluir vídeo no banco de dados\n0. Sair\n'))
                if opcao == 1:
                    Menu.opcaoLinkUnico()
                elif opcao == 2:
                    Menu.opcaoPlaylist()
                elif opcao == 3:
                    Menu.consultar()
                    Menu.excluir()
                elif opcao == 0:
                    break
                else:
                    Console().print('Comando não encontrado.', style='bold red')

            Console().print("Aproveite seus arquivos!", style="bold underline green")

        except Exception as error:
            print(f'Erro na função {Menu.opcoes().__name__}:\n{error}')

    @staticmethod
    def opcaoLinkUnico():
        url = ''
        qualidade = -1

        while qualidade != 0:
            qualidade = int(input(
                'Gostaria de baixar o vídeo em alta ou baixa qualidade?\n'
                '1. Baixa qualidade\n'
                '2. Alta qualidade\n'
                '0. Voltar\n'))

            if qualidade == 1:
                while url != '0':
                    print(
                        'Digite abaixo a URL do video do youtube que você deseja converter.\n'
                        'Ou digite 0 para VOLTAR:')
                    url = input()  # URL do video que você quer converter

                    if url != '0':
                        print(converter.Converter().converterArquivoUnico(url, qualidade))

            elif qualidade == 2:
                while url != '0':
                    print('Digite abaixo a URL do video do youtube que você deseja converter.\n'
                          'Ou digite 0 para VOLTAR:')
                    url = input()  # URL do video que você quer converter

                    if url != '0':
                        print(converter.Converter().converterArquivoUnico(url, qualidade))

            elif qualidade == 0:
                break

            else:
                Console().print('Comando não encontrado.', style='bold red')

    @staticmethod
    def opcaoPlaylist():
        url = ''
        qualidade = -1

        while qualidade != 0:
            qualidade = int(input('Gostaria de baixar a playlist em alta ou baixa qualidade?\n'
                                  '1. Baixa qualidade\n'
                                  '2. Alta qualidade\n'
                                  '0. Voltar\n'))
            if qualidade == 1:
                while url != '0':
                    print('Digite abaixo a URL da playlist do youtube que você deseja baixar e converter.\n'
                          'Ou digite 0 para VOLTAR:')
                    url = input()  # URL do video que você quer converter
                    if url != '0':
                        print(converter.Converter().converterArquivosPlaylist(url, qualidade))
            elif qualidade == 2:
                while url != '0':
                    print('Digite abaixo a URL da playlist do youtube que você deseja baixar e converter.\n'
                          'Ou digite 0 para VOLTAR:')
                    url = input()  # URL do video que você quer converter
                    if url != '0':
                        print(converter.Converter().converterArquivosPlaylist(url, qualidade))

            elif qualidade == 0:
                break
            else:
                Console().print('Comando não encontrado.', style='bold red')

    @staticmethod
    def consultar():
        try:

            console = Console()
            tabela = dao.Dao.consultar()
            console.print(tabela)

        except Exception as error:
            print(error)

    @staticmethod
    def excluir():
        dao.Dao.consultar()
        print('Digite o código do arquivo que você gostaria de excluir:')
        codigo = int(input())
        converter.Converter().excluirVideo(codigo)

