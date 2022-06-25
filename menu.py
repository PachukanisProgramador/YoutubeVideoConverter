import videoFile

class Menu:

    def __init__(self):
        pass

    def pegar(self):
        self.file = videoFile.VideoFile('lerolero', 'xumbrega');

        print(f'Nome da string: {self.file.get_file_string()}\nBytes: {self.file.get_file_bytes()}')