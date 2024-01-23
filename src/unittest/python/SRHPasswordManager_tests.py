import unittest
import json
from unittest.mock import patch, mock_open
from SRHPasswordManager import Notebook
from cryptography.fernet import Fernet

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

    def test_encrypt_and_write(self):
        # Create a mock notebook
        with patch('builtins.input', side_effect=['password','password']):
            self.notebook.mock_notebook()  
            key = self.notebook.generate_key()  
            notebook = Notebook(self.notebook.load_and_decrypt(key))

        # Use a mock open function to capture the written data
        with patch('builtins.open', mock_open()) as m:
            # Call the encrypt_and_write method
            notebook.encrypt_and_write(key)

        # Verify that the file was opened in binary write mode
        m.assert_called_once_with('Notebook.txt', 'wb')

        # Verify that the encrypted data was written to the file
        written_data = m().write.call_args[0][0]
        self.assertIsInstance(written_data, bytes)

        # Verify that the encryption key was used to create a Fernet instance
        m().write.assert_called_once()

        # Verify that the encrypted data was written to the file
        written_data = m().write.call_args[0][0]
        self.assertIsInstance(written_data, bytes)

        # Decrypt the data to ensure it matches the original notebook
        cipher_suite = Fernet(key)
        decrypted_data = cipher_suite.decrypt(written_data)
        decrypted_notebook = json.loads(decrypted_data.decode())

        # Check if the decrypted notebook matches the original notebook data
        self.assertEqual(decrypted_notebook, notebook.book)



    def test_add_entry(self):
        # Create a mock notebook
        with patch('builtins.input', side_effect=['password','password']):
            self.notebook.mock_notebook()  
            key = self.notebook.generate_key()  
            notebook = Notebook(self.notebook.load_and_decrypt(key))

        # Simulate user input to test the add_entry method
        with patch('builtins.input', side_effect=['Websites', 'example', 'john_doe', 'password123']):
            notebook.add_entry()

        # Check if the entry has been added to the notebook
        expected_entry = {'Username': 'john_doe', 'Password': 'password123'}
        self.assertEqual(notebook.book['Websites']['example'], expected_entry)


if __name__ == "__main__":
    unittest.main()