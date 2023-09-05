# directory.py -- Fergus Haak -- 05/09/2023
from datetime import datetime
from file import File

class Directory:

    def __init__(self, name, parent: None):
        self.name: str = name
        self.files: list[File] = []
        self.subdir: list[Directory] = []
        self.date: datetime = datetime.now()
        self.parent_dir: Directory = parent

    def cr_subdir(self, name):
        self.subdir.append(Directory(name))

    def dl_subdir(self):
        ...

    def cr_file(self, name, content):
        new_file = File(name)
        if content: new_file.write(content)
        self.files.append(new_file)

    def dl_file(self, file):
        ...

    def ls(self):
        ...

    def dir(self):
        for file in self.files:
            yield file.name

    def get_subdir(self, name):
        for subdir in self.subdir:
            if subdir.name == name:
                return subdir

