# directory.py -- Fergus Haak -- 05/09/2023
from datetime import datetime
from program.file import File
from program.errorhandler import ErrorHandler


class Directory:

    def __init__(self, name, parent):
        self.name: str = name
        self.files: list[File] = []
        self.subdir: list[Directory] = []
        self.date: datetime = datetime.now()
        self.parent_dir: Directory = parent
        self.error_handler = ErrorHandler()

    def __str__(self):
        return self.name

    def cr_subdir(self, name):
        if name in list(self.ls()):
            self.error("007")
            return None

        self.subdir.append(Directory(name, parent=self))

    def dl_subdir(self, name) -> None:
        for subdir in self.subdir:
            if subdir.name == name:
                self.subdir.remove(subdir)
                return None
        self.error("004")

    def cr_file(self, name, file_format, content) -> None:
        if name in list(self.ls()):
            self.error("006")
            return None
        new_file = File(name, file_format)
        if content: new_file.write(content)
        self.files.append(new_file)

    def dl_file(self, name) -> None:
        for file in self.files:
            if file.name == name:
                self.files.remove(file)
                return None
        self.error("005")

    def ls(self):
        for subdir in self.subdir:
            yield subdir.name
        for file in self.files:
            if not file.hidden:
                yield file.name

    def get_subdir(self, name) -> object:
        for subdir in self.subdir:
            if subdir.name == name:
                return subdir
        self.error("004")
        return self

    def rd(self, name) -> str:
        for file in self.files:
            if str(file) == name:
                return file.read()
        self.error("005")

    def sizeof(self) -> int:
        size = 0
        for file in self.files:
            size += file.sizeof()
        for directory in self.subdir:
            size += directory.sizeof()
        return size

    def error(self, code: str) -> None:
        """calls a directory error"""
        self.error_handler.handle_error(code)
