from moviepy.editor import *


class Converter:

    mp4_file = 'video.mp4'
    mp3_file = 'audio.mp3'

    videoClip = VideoFileClip(mp4_file)
    audioClip = videoClip.audio
    audioClip.write_audiofile(mp3_file)
    audioClip.close()
    videoClip.close()