import converter
from pytube import YouTube
import moviepy.editor as arquivo
import os
import this


class Menu:

    def __init__(self):
        print('====================================\n'
              'BEM-VINDO AO CONVERSOR DE ARQUIVOS!\n'
              '====================================')
        pass

    @staticmethod
    def opcoes():
        url = ''

        while url != '0':
            print('Digite abaixo a URL do video do youtube que você deseja converter.\nOu digite 0 para SAIR:')
            url = input()  # URL do video que você quer converter

            if url != '0':
                converter.Converter(url).converterArquivo()

        print('Obrigado!')
