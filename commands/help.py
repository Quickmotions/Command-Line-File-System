# help.py -- Fergus Haak -- 11/09/2023

class HelpCommand:
    def __init__(self, available_commands):
        self.available_commands = available_commands

    def execute(self, args):
        if len(args) == 0:
            self.display_general_help()
        elif len(args) == 1:
            self.display_command_help(args[0])
        else:
            print("Usage: help [command]")

    def display_general_help(self):
        print("Welcome to My Command-Line File System!")
        print("Available commands:")
        for command in self.available_commands:
            print(f"- {command}")

    def display_command_help(self, command):
        if command in self.available_commands:
            # Provide help information for the specific command
            if command == "create":
                print("Usage: create <file/directory name>")
                print("Description: Create a new file or directory.")
                # Add more details about the create command
            elif command == "delete":
                print("Usage: delete <file/directory name>")
                print("Description: Delete a file or directory.")
                # Add more details about the delete command
            # Add help information for other commands as needed
            else:
                print(f"No help information available for '{command}'.")
        else:
            print(f"Command '{command}' not found.")

