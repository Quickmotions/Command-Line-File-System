# file.py -- Fergus Haak -- 05/09/2023
from datetime import datetime


class File:

    def __init__(self, name: str, file_format: str):
        self.name = name
        self.fmt = file_format
        self.content = ""
        self.size = 0
        self.date = datetime.now()

    def __str__(self):
        return self.name

    def read(self) -> str:
        return self.content

    def write(self, content) -> None:
        self.content = content

    def __sizeof__(self) -> int:
        return self.size
