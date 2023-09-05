# file.py -- Fergus Haak -- 05/09/2023
from datetime import datetime


class File:

    def __init__(self, name, format):
        self.name = name
        self.fmt = format
        self.content = []
        self.size = 0
        self.date = datetime.now()

    def read(self):
        ...

    def write(self, content):
        ...

    def __sizeof__(self) -> int:
        return self.size
