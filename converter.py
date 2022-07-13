from moviepy.editor import *
from pytube import Playlist
from pytube import YouTube
import dao
import os


class Converter:

    # Método construtor
    def __init__(self):
        # Nome da pasta destino dos arquivos que serão baixados e convertidos.
        self.__nome_pasta = 'arquivos_convertidos'

        # Pega o caminho da pasta em que o programa está em uso e adiciona a pasta arquivos_mp3.
        self.__caminho = os.path.join(os.getcwd(),
                                      self.__nome_pasta)

        # Instanciando classe Dao
        self.__dao = dao.Dao()

    # Verificar se a pasta de caminho para o arquivo convertido existe.
    def verificarPasta(self):
        # Se o diretório definido no construtor não existe então será criado.
        if not os.path.exists(self.__caminho):
            os.mkdir(self.__nome_pasta)  # Criando pasta destino.

    # Função principal para baixar, converter e salvar os arquivos
    def baixarArquivo(self, video, qualidade):
        try:

            # Definindo a qualidade do arquivo
            if qualidade == 1:
                # Pegando o nome do arquivo MP4 que será baixado.
                nome_arquivo_mp4 = video.streams.get_lowest_resolution().default_filename

                # Baixando playlist em MP4 na pior qualidade possível.
                video.streams.get_lowest_resolution().download(
                    output_path=rf'{self.__caminho}')
            else:
                # Pegando o nome do arquivo MP4 que será baixado.
                nome_arquivo_mp4 = video.streams.get_highest_resolution().default_filename

                # Baixando playlist em MP4 na pior qualidade possível.
                video.streams.get_highest_resolution().download(
                    output_path=rf'{self.__caminho}')

            # Guardando o caminho onde o arquivo foi baixado. - PASTA "arquivos_convertidos".
            arquivo_mp4 = os.path.join(self.__caminho, nome_arquivo_mp4)

            # Definindo o nome do arquivo MP3 e juntando formatando para poder ser reproduzido
            nome = nome_arquivo_mp4.replace('.mp4', '')
            nome = nome.replace(' ', '_')
            nome = nome.replace('(', '')
            nome = nome.replace(')', '')
            nome = nome.replace('-', '')
            nome = nome.replace('&', 'and')

            # Especificando o caminho em que o arquivo MP3 será salvo. - PASTA "arquivos_convertidos".
            caminho_arquivo_convertido = os.path.join(self.__caminho, f'{nome}.mp3')

            # Convertendo o arquivo simples MP4 em leitura para a biblioteca do moviepy.
            video_file = VideoFileClip(arquivo_mp4)

            # Salvando o arquivo de audio do arquivo de vídeo de MP4 (videofile).
            audio = video_file.audio

            # Baixando o arquivo de áudio MP3 no caminho especificado anteriormente
            audio.write_audiofile(caminho_arquivo_convertido)

            # Salvando no banco de dados nome e arquivo
            self.__dao.inserir(nome, audio)  # Inserindo no banco de dados

            # Fechando streams de video e áudio
            video_file.close()
            audio.close()

            # Excluindo o arquivo MP4 que foi baixado
            os.remove(arquivo_mp4)  # Removendo arquivo mp4 anteriormente baixado

        except Exception as error:
            print(error)

    # Função de arquivo único para chamar na classe menu
    def converterArquivoUnico(self, video_url, qualidade):  # Função principal onde o arquivo é convertido.
        try:
            # Verificando se pasta destino existe
            Converter().verificarPasta()

            # Instanciando classe Youtube para manipulação através da URL
            video = YouTube(video_url)

            # Executando função de baixar, converter e salvar
            Converter().baixarArquivo(video, qualidade)

            # os.system('cls' if os.name == 'nt' else 'clear')
            return f'Arquivo convertido com sucesso. Ele pode ser encontrado em:\n' \
                   f'{self.__caminho}'

        except Exception as error:
            return f'Erro na função {Converter().converterArquivoUnico.__name__}:\n{error}'

    # Função de playlist para chamar na classe menu
    def converterPlaylist(self, playlist_url, qualidade):
        try:
            # Verificando se pasta destino existe
            Converter().verificarPasta()

            # Instanciando playlist para manipulação através da URL
            playlist = Playlist(playlist_url)

            # Pegando cada video da playlist e jogando em um looping para baixar todos
            for video in playlist.videos:
                # Executando função de baixar, converter e salvar
                Converter().baixarArquivo(video, qualidade)

            # os.system('cls' if os.name == 'nt' else 'clear')
            return f'Playlist convertida com sucesso. Os arquivos podem ser encontrados em:\n' \
                   f'{self.__caminho}'

        except Exception as error:
            return f'Erro na função {Converter().converterPlaylist.__name__}:\n{error}'

    # Função para consultar banco de dados
    def consultar(self):
        try:
            return self.__dao.consultar()
        except Exception as error:
            print(error)

    # Função para excluir dados no banco de dados
    def excluirVideo(self, codigo):
        try:
            self.__dao.excluir(codigo)
        except Exception as error:
            print(error)

    # Função para deletar arquivo da pasta
    def deletarArquivoPasta(self, codigo):
        try:
            arquivo = self.__dao.buscar(codigo)
            arquivo = arquivo + ".mp3"
            caminho_arquivo = os.path.join(self.__caminho, arquivo)

            if os.path.exists(caminho_arquivo):
                os.remove(caminho_arquivo)
                return True
            else:
                return False

        except Exception as error:
            # Tratando os error da classe

            # Se o erro da função estiver associado à classe de error de tipo (que acontece quando digitado um código que não existe no banco de dados)
            # eu apenas omito o erro para não ficar feio no console, uma vez que o tratamento dele é feito em outra função.
            if error.__class__ == TypeError:
                pass
            else:
                print(error)

    def reproduzir(self, codigo):
        try:
            arquivo = self.__dao.buscar(codigo)
            arquivo = arquivo + ".mp3"
            caminho_arquivo = os.path.join(self.__caminho, arquivo)

            if os.path.exists(caminho_arquivo):
                os.system(caminho_arquivo)
                return True
            else:
                return False

        except Exception as error:
            print(error)
