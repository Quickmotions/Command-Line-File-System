# errorhandler.py -- Fergus Haak -- 06/09/2023

class ErrorHandler:
    def __init__(self):
        # Define error codes and their corresponding error messages
        self.error_codes = {
            "001": "Invalid command. Type 'help' for a list of commands.",
            "002": "Invalid file or directory name.",
            "003": "Permission denied.",
            "004": "Directory not found.",
            "005": "File not found.",
            "006": "File already exists.",
            "007": "Directory already exists.",
            "008": "Already at root",

        }

    def handle_error(self, error_code, details=None) -> Exception:
        """
        Handles and displays errors with the given error code.

        :param error_code: The error code.
        :param details: Additional details or context about the error.
        """
        error_message = self.error_codes.get(error_code, "An unknown error occurred.")

        if details:
            error_message += f" Details: {details}"

        print(f"Error ({error_code}): {error_message}")
        return Exception(f"Error ({error_code}): {error_message}")

    @staticmethod
    def handle_exception(self, exception, details=None) -> Exception:
        """
        Handles and displays exceptions along with optional details.

        :param exception: The exception object.
        :param details: Additional details or context about the exception.
        """
        error_message = str(exception)

        if details:
            error_message += f" Details: {details}"

        print(f"Exception: {error_message}")
