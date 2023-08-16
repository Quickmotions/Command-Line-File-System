class File:
    def __init__(self, name: str, content: str = "") -> None:
        self.name = name
        self.content = content

    def write(self, content: str) -> None:
        self.content = content

    def read(self) -> str:
        return self.content


class FileSystem:
    def __init__(self) -> None:
        self.files: list[File] = []

    def find(self, name: str) -> File:
        for file in self.files:
            if file.name == name:
                return file
        raise ValueError("ERROR: File could not be found.")

    def create(self, name: str) -> None:
        self.files.append(File(name))
        print(f"File created: {name}")

    def write(self, name: str, content: str) -> None:
        self.find(name).write(content)
        print(f"Content written to {name}")

    def read(self, name: str):
        file_content = self.find(name).read()
        print(f"Content of {name}:\n{file_content}")

    def list(self) -> None:
        for file in self.files:
            print(f"- {file.name}")

    def delete(self, name: str) -> None:
        index = 0
        for file in self.files:
            if file.name == name:
                self.files.pop(index)
                print(f"File deleted: {file.name}")
                return
            index += 1
        print("File not found")

    def run(self):
        user_input: str = input("$ ")
        while user_input != "exit":
            user_command: list = user_input.split(" ", 2)

            if user_command[0] == "create":
                self.create(user_command[1])
            elif user_command[0] == "write":
                self.write(user_command[1], user_command[2])
            elif user_command[0] == "read":
                self.read(user_command[1])
            elif user_command[0] == "delete":
                self.delete(user_command[1])
            elif user_command[0] == "list":
                self.list()
            else:
                raise ValueError("ERROR: Unknown command or aguments.")
            user_input: str = input("$ ")


if __name__ == "__main__":
    program = FileSystem()
    program.run()
