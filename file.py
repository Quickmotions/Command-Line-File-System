# file.py -- Fergus Haak -- 05/09/2023
from datetime import datetime


class File:

    def __init__(self, name: str, file_format: str, priv_req: int = 2):
        self.name = name
        self.fmt = file_format
        self.content = ""
        self.size = 0
        self.date = datetime.now()
        self.priv = priv_req
        self.hidden = False

        self.check_hidden()

    def __str__(self):
        return self.name

    def read(self) -> str:
        return self.content

    def write(self, content) -> None:
        self.content = content
        self.size += len(str(content))

    def sizeof(self) -> int:
        return self.size

    def check_hidden(self):
        if self.name[0] == ".":
            self.hidden = True
