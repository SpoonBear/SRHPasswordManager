import unittest
from unittest.mock import patch, mock_open
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

    def test_load_and_decrypt(self):
        # Create a mock notebook
        with patch('builtins.input', return_value='password'):
            self.notebook.mock_notebook()
            key = self.notebook.generate_key()
            notebook = Notebook()
        
        # Create a mock open function to simulate reading from a file
        with patch('builtins.open', mock_open(read_data='encrypted_data')) as m:
            # Call the load_and_decrypt method
            notebook.load_and_decrypt(key)
        
        # Verify that the file was opened and read from
        m.assert_called_once_with('Notebook.txt', 'rb')

    def test_add_entry(self):
        # Create a mock notebook
        with patch('builtins.input', side_effect=['password','password']):
            self.notebook.mock_notebook()  
            key = self.notebook.generate_key()  
            notebook = Notebook(self.notebook.load_and_decrypt(key))

        # Simulate user input to test the add_entry method
        with patch('builtins.input', side_effect=['Websites', 'example', 'john_doe', 'password123']):
            # Print contents of notebook before add_entry
            print("Notebook content before add_entry:", notebook.book)
            notebook.add_entry()

        # Check if the entry has been added to the notebook
        expected_entry = {'Username': 'john_doe', 'Password': 'password123'}
        self.assertEqual(notebook.book['Websites']['example'], expected_entry)


if __name__ == "__main__":
    unittest.main()