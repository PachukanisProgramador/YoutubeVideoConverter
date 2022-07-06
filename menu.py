import converter
from pytube import YouTube
import moviepy.editor as arquivo
import os
import this


class Menu:

    def __init__(self):
        print('\n\n\n=============================\n'
              'BEM-VINDO AO CONVERSOR DE ARQUIVOS!\n'
              '=============================\n\n')
        pass

    @staticmethod
    def opcoes():
        try:
            opcao = -1
            while opcao != 0:
                opcao = int(input('Deseja converter links únicos ou uma playlist?\n\n1. Links únicos\n2. Playlist\n0. Sair\n'))
                if opcao == 1:
                    Menu.opcaoLinkUnico()
                elif opcao == 2:
                    Menu.opcaoPlaylist()
                elif opcao == 0:
                    break
                else:
                    print('Comando não encontrado.')

            print('Aproveite seus arquivos!')
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
                print('Comando não encontrado.')

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
                print('Comando não encontrado.')


