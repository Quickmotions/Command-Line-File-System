# commands/command.py -- Fergus Haak -- 11/09/23
from abc import ABC


class FactoryCommand(ABC):

    def __init__(self):
        self.name: str = "command"
        self.priv_req = 2

    def __str__(self) -> str:
        return self.name

    def get(self) -> str:
        return self.name

    def has_priv(self, user_priv: int) -> bool:
        if user_priv <= self.priv_req:
            return True
        return False

    def execute(self, *args):
        raise NotImplementedError("Subclasses must implement the execute method.")

