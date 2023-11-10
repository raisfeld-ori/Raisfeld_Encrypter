import appdirs
import os
from typing import TextIO
from typing import Optional


class SavedData:
    def __init__(self, location: str):
        self.location = appdirs.AppDirs(location)
        if os.path.exists(self.location.user_data_dir):
            return
        else:
            os.makedirs(self.location.user_data_dir)

    def create_dir(self, dir_name: str):
        path = os.path.join(self.location.user_data_dir, dir_name)
        os.makedirs(path)

    def create_file(self, file_name: str) -> TextIO:
        path = os.path.join(self.location.user_data_dir, file_name)
        return open(path, "w+")


class File:
    def __init__(self, location: str):
        self.location = location

        if os.path.isdir(location):
            raise IsADirectoryError("expected a file, got a directory")
        self.file: Optional[TextIO] = None

    def exists(self) -> bool: return os.path.exists(self.location)
    def create(self): self.file = open(self.location, 'w+')
    def read(self) -> str: return self.file.read() if self.file else open(self.location, 'r').read()
