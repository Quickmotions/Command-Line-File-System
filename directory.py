# directory.py -- Fergus Haak -- 05/09/2023
from datetime import datetime
from file import File


class Directory:

    def __init__(self, name, parent):
        self.name: str = name
        self.files: list[File] = []
        self.subdir: list[Directory] = []
        self.date: datetime = datetime.now()
        self.parent_dir: Directory = parent

    def __str__(self):
        return self.name

    def cr_subdir(self, name):
        self.subdir.append(Directory(name, parent=self))

    def dl_subdir(self, name):
        for subdir in self.subdir:
            if subdir.name == name:
                self.subdir.remove(subdir)

    def cr_file(self, name, format, content):
        new_file = File(name, format)
        if content: new_file.write(content)
        self.files.append(new_file)

    def dl_file(self, name):
        for file in self.files:
            if file.name == name:
                self.files.remove(file)

    def ls(self):
        for subdir in self.subdir:
            yield subdir.name
        for file in self.files:
            yield file.name

    def get_subdir(self, name):
        for subdir in self.subdir:
            if subdir.name == name:
                return subdir

    def rd(self, name) -> str:
        for file in self.files:
            if str(file) == name:
                return file.read()
