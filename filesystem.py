# filesystem.py -- Fergus Haak -- 05/09/2023
from datetime import datetime
from directory import Directory
from file import File


class FileSystem:
    def __init__(self):
        self.working_directory = Directory()
        self.root_directory = self.working_directory
        self.date = datetime.now()

    def cr_dir(self):
        """creates a directory in working directory"""
        ...

    def del_dir(self):
        """deletes a directory in working directory"""
        ...

    def cr_file(self):
        """creates a file"""
        ...

    def del_file(self):
        """deletes a file"""
        ...

    def dir(self):
        """list working directory"""
        ...

    def ch_dir(self):
        """change working directory"""
        ...

    def save_fs(self):
        """saves the file system to disc"""
        ...

    def load_fs(self):
        """loads the file system from disc"""
        ...

