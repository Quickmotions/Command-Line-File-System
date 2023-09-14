# tests/test_user.py -- Fergus Haak -- 14/09/2023
import unittest
from user import User


class TestFileSystem(unittest.TestCase):

    def set_up(self):
        # Set up any necessary resources or create a new instance of your FileSystem class
        self.user = User()


if __name__ == '__main__':
    unittest.main()
