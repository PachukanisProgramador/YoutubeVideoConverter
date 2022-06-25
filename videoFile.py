class VideoFile:

    def __init__(self, file_string, file_bytes):
        self._file_string = file_string
        self._file_bytes = file_bytes

    def get_file_string(self):
        return self._file_string

    def set_file_string(self, value):
        self._file_string = value
        
    def get_file_bytes(self):
        return self._file_bytes
    
    def set_file_bytes(self, value):
        self._file_bytes = value
