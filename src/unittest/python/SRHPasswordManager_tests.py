import unittest
from unittest.mock import patch
from SRHPasswordManager import Notebook

class TestNotebook(unittest.TestCase):
    def setUp(self):
        self.notebook = Notebook({})

    def test_check_for_file_existing(self):
        # Mock the os.path.exists function to simulate an existing file
        with patch('os.path.exists', return_value=True):
            result = self.notebook.check_for_file()

        self.assertEqual(result, 1)  # Expecting 1 as the file exists

    def test_check_for_file_not_existing(self):
        # Mock the os.path.exists function to simulate a non-existing file
        with patch('os.path.exists', return_value=False):
            result = self.notebook.check_for_file()

        self.assertEqual(result, 0)  # Expecting 0 as the file does not exist


if __name__ == "__main__":
    unittest.main()