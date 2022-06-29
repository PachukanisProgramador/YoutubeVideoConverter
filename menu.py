import videoFile
from pytube import YouTube
import moviepy.editor as arquivo
import os
import this


class Menu:

    def __init__(self):
        this.user = os.getenv('USERNAME')  # Pegar o nome de usuário do computador
        this.url = input('URL: ')  # URL do video que você quer converter
        pass

    @staticmethod
    def pegarArquivo():
        video = YouTube(this.url).streams.get_audio_only()
        video.download(rf'C:\Users\{this.user}\Desktop\mp3')
        title = str(video.title)
        clip = arquivo.AudioFileClip(rf'C:\Users\{this.user}\Desktop\mp3\{title}.mp4')
        clip.write_audiofile(rf'C:\Users\{this.user}\Desktop\mp3\{title}.mp3')
        os.remove(rf'C:\Users\{this.user}\Desktop\mp3\{title}.mp4')