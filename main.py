# main.py -- Fergus Haak -- 05/09/2023
from program.filesystem import FileSystem  # Import your FileSystem class
from program.user import User

def main():
    # Create an instance of the FileSystem class
    file_system = FileSystem()

    # Create an instance of the User class for user interactions
    user_interface = User("root")

    print("Welcome to My Command-Line File System!")

    while True:
        # Display the current directory
        print(f"Current Directory: {file_system.wrk_dir}")

        # Get user input
        user_input = input("Enter a command (type 'help' for a list of commands): ").strip()

        if user_input.lower() == 'quit':
            print("Exiting the file system.")
            break

        # Pass the user input to the User class for processing
        user_interface.process_command(user_input)

if __name__ == "__main__":
    main()
