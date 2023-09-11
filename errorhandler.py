# errorhandler.py -- Fergus Haak -- 06/09/2023

import logging


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

        # Configure logging
        logging.basicConfig(
            level=logging.ERROR,  # Set the log level to ERROR or higher
            format="%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        self.logger = logging.getLogger("error_handler")

    def handle_error(self, error_code, details=None) -> Exception:
        """
        Handles and logs errors with the given error code.

        :param error_code: The error code.
        :param details: Additional details or context about the error.
        """
        error_message = self.error_codes.get(error_code, "An unknown error occurred.")

        if details:
            error_message += f" Details: {details}"

        error_message = f"Error ({error_code}): {error_message}"

        # Log the error
        self.logger.error(error_message)

        return Exception(error_message)

    @staticmethod
    def handle_exception(exception, details=None) -> Exception:
        """
        Handles and logs exceptions along with optional details.

        :param exception: The exception object.
        :param details: Additional details or context about the exception.
        """
        error_message = str(exception)

        if details:
            error_message += f" Details: {details}"

        error_message = f"Exception: {error_message}"

        # Log the exception
        logging.error(error_message)

        return Exception(error_message)
