# filesystem.py -- Fergus Haak -- 05/09/2023
from datetime import datetime
from pprint import pprint

from directory import Directory

class FileSystem:
    def __init__(self):
        self.wrk_dir = Directory()
        self.root = self.wrk_dir
        self.date = datetime.now()

    def cr_dir(self, name):
        """creates a directory in working directory"""
        self.wrk_dir.cr_subdir(name)

    def del_dir(self, name):
        """deletes a directory in working directory"""
        self.wrk_dir.dl_subdir(name)

    def cr_file(self, name, content: str = None):
        """creates a file"""
        self.wrk_dir.cr_file(name, content)

    def del_file(self, name):
        """deletes a file"""
        self.wrk_dir.dl_file(name)

    def dir(self) -> list:
        """list working directory"""
        return list(self.wrk_dir.dir())

    def ch_dir(self, name):
        """change working directory"""
        self.wrk_dir = self.wrk_dir.get_subdir(name)

    def mv_bk(self):
        """move back to previous directory"""
        self.wrk_dir = self.wrk_dir.parent_dir

    def sv_fs(self):
        """saves the file system to disc"""
        ...

    def ld_fs(self):
        """loads the file system from disc"""
        ...

