# directory.py -- Fergus Haak -- 05/09/2023
from datetime import datetime


class Directory:

    def __init__(self, name):
        self.name = name
        self.files = []
        self.subdr = []
        self.date = datetime.now()

    def cr_subdr(self):
        ...

    def dl_subdr(self):
        ...

    def cr_file(self, file):
        ...

    def dl_file(self, file):
        ...

    def ls(self):
        ...
