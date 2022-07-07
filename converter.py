from moviepy.editor import *
from pytube import YouTube
from pytube import Playlist
import os
import this
import dao


class Converter:

    def __init__(self):
        this.__nome_pasta = 'arquivos_convertidos'  # Nome da pasta destino dos arquivos convertidos.
        this.__caminho = os.path.join(os.getcwd(), this.__nome_pasta)  # Pega o caminho da pasta em que o programa está em uso e adiciona a pasta arquivos_mp3.
        this.__dao = dao.Dao()

    @staticmethod
    def verificarPasta():  # Verificar se a pasta de caminho para o arquivo convertido existe.
        if not os.path.exists(this.__caminho):  # Se não existe então o diretório é criado.
            os.mkdir(this.__nome_pasta)  # Criando pasta destino

    @staticmethod
    def baixarArquivoUrl(video_url, qualidade):  # Função para baixar o arquivo MP4 por meio apenas da URL do vídeo.
        Converter.verificarPasta()

        if qualidade == 1:
            video_stream = YouTube(video_url).streams.get_lowest_resolution()  # Baixando arquivo MP4 na pior qualidade.
        else:
            video_stream = YouTube(video_url).streams.get_highest_resolution()  # Baixando arquivo MP4 na melhor qualidade possível.

        return video_stream

    @staticmethod
    def baixarPlaylist(playlist_url, qualidade):
        Converter.verificarPasta()

        playlist = Playlist(playlist_url)  # Baixando arquivo MP4 na pior qualidade.

        if qualidade == 1:
            for video in playlist.videos:
                return video.streams.get_lowest_resolution()   # Baixando playlist em MP4 através de list comprehension  na pior qualidade possível.
        else:
            for video in playlist.videos:
                return video.streams.get_highest_resolution()  # Baixando playlist em MP4 através de list comprehension  na melhor qualidade possível.

    @staticmethod
    def converterArquivoUnico(video_url, qualidade):  # Função principal onde o arquivo é convertido.
        try:

            # Tratar arquivo e definir caminhos
            arquivo = Converter.baixarArquivoUrl(video_url, qualidade)
            arquivo.download(output_path=rf'{this.__caminho}')  # Informando o caminho em que o arquivo será baixado.
            arquivo_mp4 = os.path.join(this.__caminho, arquivo.default_filename)
            nome = arquivo.default_filename.replace('.mp4', '')

            # Especificando o caminho do arquivo que será convertido para mp3
            caminho_arquivo_convertido = os.path.join(this.__caminho, f'{nome}.mp3')

            # Convertendo o arquivo para mp3 e salvando no caminho anteriormente instanciado
            video = VideoFileClip(arquivo_mp4)
            audio = video.audio
            audio.write_audiofile(caminho_arquivo_convertido)

            this.__dao.inserir(arquivo.default_filename, nome)  # Inserindo no banco de dados

            video.close()
            audio.close()

            os.remove(arquivo_mp4)  # Removendo arquivo mp4 anteriormente baixado

            return f'Arquivo convertido com sucesso. Ele pode ser encontrado em:\n{caminho_arquivo_convertido}'

        except Exception as error:
            return f'Erro na função {Converter.converterArquivoUnico.__name__}:\n{error}'

    @staticmethod
    def converterArquivosPlaylist(video_url, qualidade):
        try:

            # Tratar arquivo e definir caminhos
            arquivo = Converter.baixarPlaylist(video_url, qualidade)
            arquivo.download(output_path=rf'{this.__caminho}')  # Informando o caminho em que o arquivo será baixado.
            arquivo_mp4 = os.path.join(this.__caminho, arquivo.default_filename)
            nome = arquivo.default_filename.replace('.mp4', '')

            # Especificando o caminho do arquivo que será convertido para mp3
            caminho_arquivo_convertido = os.path.join(this.__caminho, f'{nome}.mp3')

            # Convertendo o arquivo para mp3 e salvando no caminho anteriormente instanciado
            video = VideoFileClip(arquivo_mp4)
            audio = video.audio
            audio.write_audiofile(caminho_arquivo_convertido)
            video.close()
            audio.close()

            this.__dao.inserir(arquivo.default_filename, nome)  # Inserindo no banco de dados

            os.remove(arquivo_mp4)  # Removendo arquivo mp4 anteriormente baixado

            return f'Playlist convertida com sucesso. Os arquivos podem ser encontrados em:\n{caminho_arquivo_convertido}'

        except Exception as error:
            return f'Erro na função {Converter.converterArquivosPlaylist.__name__}:\n{error}'

    @staticmethod
    def excluirVideo(codigo):
        this.__dao.excluir(codigo)
