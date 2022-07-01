import subprocess
from pytube import YouTube
import os
import this

class Converter:

    def __init__(self, video_url):
        this.__video_url = video_url
        this.__caminho = os.getcwd() + '\\arquivos_mp3'  # Pegar o caminho da pasta em uso e adicionar a pasta arquivos_mp3

    @staticmethod
    def converterArquivo():
        try:
            this.__video_url = YouTube(this.__video_url).streams.get_audio_only()  #

            this.__video_url.download(rf'{this.__caminho}')

            title = this.__video_url.default_filename

            print(f'Caminho: {this.__caminho}')
            print(title)

            titulo = this.__video_url.title
            print(rf'ffmpeg -i {os.path.join(this.__caminho, title)} {os.path.join(this.__caminho, f"{titulo}.mp3")}')

            subprocess.run([
                rf'ffmpeg', '-i', os.path.join(this.__caminho, title),
                os.path.join(this.__caminho, f'{titulo}.mp3')
            ])

            os.remove(rf'{this.__caminho}\{title}.mp4')

            return f'Video convertido com sucesso. Ele pode ser encontrado em:\n' \
                   f'{this.__caminho}'

        except Exception as error:
            print(f'Erro na função {Converter.converterArquivo.__name__}.\n{error}')

