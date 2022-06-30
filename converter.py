from pytube import YouTube
import moviepy.editor as editor
import os
import this
import math


class Converter:

    def __init__(self, video_url):
        this.video_url = video_url
        this.__caminho = os.getcwd() + '\\arquivos_mp3'  # Pegar o caminho da pasta em uso e adicionar a pasta arquivos_mp3

    @staticmethod
    def converterArquivo():
        try:
            this.video_url = YouTube(this.video_url).streams.get_audio_only()  #

            this.video_url.download(rf'{this.__caminho}')

            title = str(this.video_url.title)

            audio = editor.AudioFileClip(rf'{this.__caminho}\{title}.mp4', buffersize=math.inf)

            print(audio.duration)

            audio.write_audiofile(rf'{this.__caminho}\{title}.mp3')

            os.remove(rf'{this.__caminho}\{title}.mp4')

            return f'Video convertido com sucesso. Ele pode ser encontrado em:\n' \
                   f'{this.__caminho}'

        except Exception as error:
            print(f'Erro na função {Converter.converterArquivo.__name__}.\n{error}')

