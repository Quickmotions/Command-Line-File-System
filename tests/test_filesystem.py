# tests/test_filesystem.py -- Fergus Haak -- 05/09/2023
import unittest
from filesystem import FileSystem


class TestFileSystem(unittest.TestCase):

    def setUp(self):
        # Set up any necessary resources or create a new instance of your FileSystem class
        self.fs = FileSystem()

    def tear_down(self):
        # Clean up any resources if needed
        pass

    def test_initial_directory_structure(self):
        # Test that the file system starts with a root directory
        self.assertEqual(str(self.fs.wrk_dir), "/")

    def test_create_directory(self):
        # Test creating a new directory
        directory_name = "new_directory"
        self.fs.cr_dir(directory_name)
        self.assertIn(directory_name, self.fs.dir())

    def test_create_file(self):
        # Test creating a new file
        file_name = "new_file.txt"
        content = "This is a test file."
        fmt = "txt"
        self.fs.cr_file(file_name, fmt, content)
        self.assertIn(file_name, self.fs.dir())
        self.assertEqual(self.fs.rd_file(file_name), content)

    def test_delete_directory(self):
        # Test deleting a directory
        directory_name = "to_be_deleted"
        self.fs.cr_dir(directory_name)
        self.fs.del_dir(directory_name)
        self.assertNotIn(directory_name, self.fs.dir())

    def test_delete_file(self):
        # Test deleting a file
        file_name = "to_be_deleted.txt"
        content = "Delete me!"
        fmt = "txt"
        self.fs.cr_file(file_name, fmt, content)
        self.fs.del_file(file_name)
        self.assertNotIn(file_name, self.fs.dir())

    def test_changing_directories(self):
        # Test changing in and out of directories and subdirectories
        directory = "main"
        sub_directory = "sub"
        self.assertEqual(str(self.fs.wrk_dir), "/")
        self.fs.cr_dir(directory)
        self.fs.mv_dir("main")
        self.assertEqual(str(self.fs.wrk_dir), "main")
        self.fs.cr_dir(sub_directory)
        self.assertEqual(str(self.fs.wrk_dir), "main")
        self.fs.mv_bk()
        self.assertEqual(str(self.fs.wrk_dir), "/")
        self.assertEqual(self.fs.dir(), ["main"])
        self.fs.mv_dir("main")
        self.assertEqual(self.fs.dir(), ["sub"])
        self.fs.mv_dir("sub")
        self.assertEqual(self.fs.dir(), [])

    def test_fs_sizeof(self):
        file_name = "file1.txt"
        content = "Hi this is content of length 33"
        file_name_2 = "file2.txt"
        content_2 = "hi"
        file_name_3 = "file3.txt"
        self.fs.cr_file(file_name, "txt", content)
        self.fs.cr_file(file_name_2, "txt", content_2)
        self.fs.cr_file(file_name_3, "txt")
        self.assertEqual(self.fs.sizeof(), 33)

    # Add more test cases as needed


if __name__ == '__main__':
    unittest.main()
