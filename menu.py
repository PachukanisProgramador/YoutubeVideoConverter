import converter
from rich.console import Console
from rich.panel import Panel
import os


class Menu:

    # Método construtor
    def __init__(self):
        self.__console = Console()
        pass

    def opcoes(self):
        opcao = -1
        loop = 0
        try:
            while opcao != 0:

                os.system('cls' if os.name == 'nt' else 'clear')

                if loop == 0:
                    self.__console.print(Panel.fit('BEM-VINDO AO CONVERSOR DE ARQUIVOS!'), justify='center', style='yellow')
                    print()

                Menu.consultar()
                print()
                loop = loop + 1

                opcao = int(input('Deseja converter links únicos ou uma playlist?\n\n'
                                  '1. Links únicos.\n'
                                  '2. Playlist.\n'
                                  '3. Excluir arquivo.\n'
                                  '4. Reproduzir.\n'
                                  '0. Sair.\n'))

                if opcao == 1:
                    Menu.opcaoLinkUnico()
                elif opcao == 2:
                    Menu.opcaoPlaylist()
                elif opcao == 3:
                    Menu.excluir()
                elif opcao == 4:
                    Menu.reproduzirAudio()
                elif opcao == 0:
                    break
                else:
                    Console().print('Comando não encontrado.', style='bold red')

            Console().print("\nAproveite seus arquivos!", style="bold underline green")

        except Exception as error:
            print(f'Erro na função {Menu().opcoes().__name__}:\n{error}')

    # Método para escolha de número 1 no menu anterior (links únicos)
    @staticmethod
    def opcaoLinkUnico():
        url = ''
        qualidade = -1

        while qualidade != 0:
            qualidade = int(input(
                '\nGostaria de baixar o vídeo em alta ou baixa qualidade?\n'
                '1. Baixa qualidade\n'
                '2. Alta qualidade\n'
                '0. Voltar\n'))

            if qualidade == 1 or qualidade == 2:
                while url != '0':
                    # Pegar a URL do vídeo que você quer converter
                    url = input(
                        '\nDigite abaixo a URL do video do youtube que você deseja converter.\n'
                        'Ou digite 0 para VOLTAR:\n')

                    if url != '0':
                        Console().print(converter.Converter().converterArquivoUnico(url, qualidade), style='bold green')

                    else:
                        qualidade = 0

            else:
                Console().print('\nComando não encontrado.', style='bold red')

    # Método para escolha de número 2 no menu anterior (playlist)
    @staticmethod
    def opcaoPlaylist():
        url = ''
        qualidade = -1

        while qualidade != 0:
            qualidade = int(input('\nGostaria de baixar a playlist em alta ou baixa qualidade?\n'
                                  '1. Baixa qualidade\n'
                                  '2. Alta qualidade\n'
                                  '0. Voltar\n'))

            if qualidade == 1 or qualidade == 2:
                while url != '0':
                    # Pegar a URL do vídeo que você quer converter
                    url = input('\nDigite abaixo a URL da playlist do youtube que você deseja baixar e converter.\n'
                                'Ou digite 0 para VOLTAR:\n')

                    if url != '0':
                        Console().print(converter.Converter().converterPlaylist(url, qualidade), style='bold green')

                    else:
                        qualidade = 0

            else:
                Console().print('\nComando não encontrado.', style='bold red')

    # Método para consultar no banco de dados
    @staticmethod
    def consultar():
        try:
            # Instanciando variável da biblioteca Rich
            console = Console()

            # Pegando a tabela de consulta
            tabela = converter.Converter().consultar()

            # Mostrando em tela tabela
            console.print(tabela)

        except Exception as error:
            print(error)

    # Método para excluir no banco de dados e na pasta
    @staticmethod
    def excluir():
        try:
            print('\nDigite o código do arquivo que você gostaria de excluir:')
            codigo = int(input())

            if not converter.Converter().deletarArquivoPasta(codigo):
                resposta = -1
                while resposta != 1 or resposta != 2:
                    resposta = int(input("\nArquivo não encontrado na pasta local. Deseja excluir apenas do banco de dados?\n1. Sim.\n2. Não.\n"))
                    if resposta == 1:
                        converter.Converter().excluirVideo(codigo)
                        break
                    elif resposta == 2:
                        break
                    else:
                        print("\nDigite um comando válido!")

            else:
                converter.Converter().excluirVideo(codigo)

        except Exception as error:
            print(error)

    @staticmethod
    def reproduzirAudio():
        try:
            codigo = int(input('Digite o código do arquivo que deseja reproduzir.\n'))

            if converter.Converter().reproduzir(codigo):
                pass
            else:
                print("Arquivo não encontrado.")
        except Exception as error:
            print(error)

