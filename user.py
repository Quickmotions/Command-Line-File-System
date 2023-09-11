# user.py -- Fergus Haak -- 05/09/2023
from datetime import datetime
from commands import HelpCommand
from errorhandler import ErrorHandler

class User:
    def __init__(self, name: str, priv: int = 2):
        self.name: str = name
        self.date: datetime = datetime.now()
        self.priv: int = priv
        self.error_handler = ErrorHandler()

    def user_interface_input(self):
        ...

    def process_command(self, user_input):
        # TODO document why this method is empty
        pass

    def error(self, code: str) -> None:
        """calls a directory error"""
        self.error_handler.handle_error(code)
