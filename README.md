# Simple Command-Line File System

This is a basic command-line file system implementation that allows users to create, write, read, and delete files.

## Table of Contents
- [Description](#description)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Commands](#commands)
- [Example](#example)
- [Known Issues](#known-issues)
- [Contributing](#contributing)
- [License](#license)

## Description

This project implements a simple command-line file system with the following features:
- `create <filename>`: Create an empty file.
- `write <filename> <content>`: Write content to a file.
- `read <filename>`: Read and display the content of a file.
- `delete <filename>`: Delete a file.
- `list`: List all files in the file system.

## Getting Started

To use the file system, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run the main program file, e.g., `python file_system.py` or `java FileSystemMain`.

## Usage

1. Open a command-line terminal.
2. Navigate to the project directory.
3. Run the program and follow the on-screen instructions to interact with the file system.

## Commands

- `create <filename>`: Creates an empty file with the specified name.
- `write <filename> <content>`: Writes the provided content to the specified file.
- `read <filename>`: Displays the content of the specified file.
- `delete <filename>`: Deletes the specified file.
- `list`: Lists all files in the file system.

## Example

Here's an example of how you can interact with the file system:

```sh
$ create example.txt
File created: example.txt

$ write example.txt Hello, world!
Content written to example.txt

$ read example.txt
Content of example.txt:
Hello, world!

$ list
Files in the file system:
- example.txt

$ delete example.txt
File deleted: example.txt
```

## Known Issues
- No input validation, program will work with correct commands with full arguments.

## Contributing

Contributions are welcome! If you find a bug or have an idea for an enhancement, feel free to open an issue or submit a pull request.
License

This project is licensed under the [MIT License](LICENSE).
