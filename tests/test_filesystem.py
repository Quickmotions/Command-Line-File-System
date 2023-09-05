# tests/test_filesystem.py -- Fergus Haak -- 05/09/2023

import unittest
from filesystem import FileSystem  # Import your FileSystem class


class TestFileSystem(unittest.TestCase):

    def setUp(self):
        # Set up any necessary resources or create a new instance of your FileSystem class
        self.fs = FileSystem()

    def tearDown(self):
        # Clean up any resources if needed
        pass

    def test_initial_directory_structure(self):
        # Test that the file system starts with a root directory
        self.assertEqual(self.fs.current_directory, "/")

    def test_create_directory(self):
        # Test creating a new directory
        directory_name = "new_directory"
        self.fs.create_directory(directory_name)
        self.assertIn(directory_name, self.fs.list_directory())

    def test_create_file(self):
        # Test creating a new file
        file_name = "new_file.txt"
        content = "This is a test file."
        self.fs.create_file(file_name, content)
        self.assertIn(file_name, self.fs.list_directory())
        self.assertEqual(self.fs.read_file(file_name), content)

    def test_delete_directory(self):
        # Test deleting a directory
        directory_name = "to_be_deleted"
        self.fs.create_directory(directory_name)
        self.fs.delete_directory(directory_name)
        self.assertNotIn(directory_name, self.fs.list_directory())

    def test_delete_file(self):
        # Test deleting a file
        file_name = "to_be_deleted.txt"
        self.fs.create_file(file_name, "Delete me!")
        self.fs.delete_file(file_name)
        self.assertNotIn(file_name, self.fs.list_directory())

    # Add more test cases as needed


if __name__ == '__main__':
    unittest.main()
