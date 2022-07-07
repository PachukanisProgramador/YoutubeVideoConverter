import converter
from rich.console import Console


class Menu:

    def __init__(self):
        Console().print('\n\n\n===================================\n'
              'BEM-VINDO AO CONVERSOR DE ARQUIVOS!\n'
              '===================================\n\n', style='bold yellow')
        pass

    @staticmethod
    def opcoes():
        try:
            opcao = -1
            while opcao != 0:
                opcao = int(input('Deseja converter links únicos ou uma playlist?\n\n1. Links únicos\n2. Playlist\n3. Excluir vídeo no banco de dados\n0. Sair\n'))
                if opcao == 1:
                    Menu.opcaoLinkUnico()
                elif opcao == 2:
                    Menu.opcaoPlaylist()
                elif opcao == 3:
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
                'Gostaria de baixar o vídeo em alta ou baixa qualidade?\n1. Baixa qualidade\n2. Alta qualidade\n0. Voltar\n'))
            if qualidade == 1:
                while url != '0':
                    print(
                        'Digite abaixo a URL do video do youtube que você deseja converter.\nOu digite 0 para VOLTAR:')
                    url = input()  # URL do video que você quer converter

                    if url != '0':
                        print(converter.Converter().converterArquivoUnico(url, qualidade))
            elif qualidade == 2:
                while url != '0':
                    print('Digite abaixo a URL do video do youtube que você deseja converter.\nOu digite 0 para VOLTAR:')
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
            qualidade = int(input('Gostaria de baixar a playlist em alta ou baixa qualidade?\n1. Baixa qualidade\n2. Alta qualidade\n0. Voltar\n'))
            if qualidade == 1:
                while url != '0':
                    print( 'Digite abaixo a URL da playlist do youtube que você deseja baixar e converter.\nOu digite 0 para VOLTAR:')
                    url = input()  # URL do video que você quer converter
                    if url != '0':
                        print(converter.Converter().converterArquivosPlaylist(url, qualidade))
            elif qualidade == 2:
                while url != '0':
                    print( 'Digite abaixo a URL da playlist do youtube que você deseja baixar e converter.\nOu digite 0 para VOLTAR:')
                    url = input()  # URL do video que você quer converter
                    if url != '0':
                        print(converter.Converter().converterArquivosPlaylist(url, qualidade))

            elif qualidade == 0:
                break
            else:
                Console().print('Comando não encontrado.', style='bold red')

    @staticmethod
    def excluir():
        print('Digite o código do arquivo no banco de dados que você gostaria de excluir:')
        codigo = int(input())
        converter.Converter().excluirVideo(codigo)