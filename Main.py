class File:
    def __init__(self, name: str, content: str = None) -> None:
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
        ...


    def create(self, name: str, content: str = None) -> None:
        self.files.append(File(name, content))

    def write(self, name: str, content: str) -> None:
        self.find(name).write(content)

    def read(self, name: str):
        file_content = self.find(name).read()
        print(file_content)

    def list(self) -> None:
        for file in self.files:
            print(f"- {file.name}")

    def delete(self, name: str) -> None:
        for file in self.files:
            if file.name == name:
                self.files.pop(file)
                print(f"File deleted: {file.name}")
                return

        print("File not found")

    def run(self):
        ...

if __name__ == "__main__":
    program = FileSystem()
    program.run()
