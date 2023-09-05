# user.py -- Fergus Haak -- 05/09/2023
from datetime import datetime


class User:
    def __init__(self, name: str, priv: int = 2):
        self.name: str = name
        self.date: datetime = datetime.now()
        self.priv: int = priv
