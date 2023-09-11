# commands/help.py -- Fergus Haak -- 11/09/2023

from commands.command import FactoryCommand


class HelpCommand(FactoryCommand):
    def __init__(self):
        super().__init__()

        self.name = "help"
        self.priv_req = 2

    def update_priv_req(self, priv: int):
        self.priv_req = priv

    def execute(self, args):
        if len(args) == 0:
            self.display_general_help()
        elif len(args) == 1:
            self.display_command_help(args[0])
        else:
            print("Usage: help [command]")
