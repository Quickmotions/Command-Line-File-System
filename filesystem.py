# filesystem.py -- Fergus Haak -- 05/09/2023
from datetime import datetime
from directory import Directory
from errorhandler import ErrorHandler

class FileSystem:
    def __init__(self):
        self.wrk_dir = Directory(name="/", parent=None)
        self.root = self.wrk_dir
        self.date = datetime.now()
        self.error_handler = ErrorHandler()

    def cr_dir(self, name) -> None:
        """creates a directory in working directory"""
        self.wrk_dir.cr_subdir(name)

    def del_dir(self, name) -> None:
        """deletes a directory in working directory"""
        self.wrk_dir.dl_subdir(name)

    def cr_file(self, name, format: str, content: str = None) -> None:
        """creates a file"""
        self.wrk_dir.cr_file(name, format, content)

    def del_file(self, name) -> None:
        """deletes a file"""
        self.wrk_dir.dl_file(name)

    def rd_file(self, name) -> str:
        """reads a file in working directory"""
        return self.wrk_dir.rd(name)

    def dir(self) -> list:
        """list working directory"""
        return list(self.wrk_dir.ls())

    def mv_dir(self, name) -> None:
        """change working directory"""
        self.wrk_dir = self.wrk_dir.get_subdir(name)

    def mv_bk(self) -> None:
        """move back to previous directory"""
        if self.wrk_dir.parent_dir is None:
            self.error("008")
            return
        self.wrk_dir = self.wrk_dir.parent_dir

    def sizeof(self) -> int:
        """returns the size in characters of all files and sub-dirs in working directory"""
        return self.wrk_dir.sizeof()

    def sv_fs(self):
        """saves the file system to disc"""
        ...

    def ld_fs(self):
        """loads the file system from disc"""
        ...

    def error(self, code: str) -> None:
        """calls a file system error"""
        self.error_handler.handle_error(code)
