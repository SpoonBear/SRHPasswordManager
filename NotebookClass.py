import json
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64

class Notebook:
    def __init__(self, book) -> None:
        self.book = book
        
    def __str__(self) -> str:
        return f'{self.book}'

    def print_book(self):
        print('\nCurrent credentials in notebook:\n')
        for categ, name in self.book.items():
            print(f'---Category: {categ}---')
            for key, value in name.items():
                print(f' --{key}--')
                for user, passw in value.items():
                    print(f'   -{user}: {passw}')

    def add_entry(self):
        # Add new entry
        category = input('Enter the category of the new entry (e.g., Websites, Emails): ')
        # Check if category exists
        if category in self.book:
             site = input('Enter the name of the website or service: ')
             # Check if entry exists
             if site not in self.book[category]:
                 username = input('Enter the username: ')
                 password = input('Enter the password: ')
                 # Add the new entry to the dictionary
                 self.book[category][site] = {'Username': username, 'Password': password}
                 print(f'Entry {site} added successfully.')
             else:
                 print(f'Entry {site} exists already')
        else:
             print(f'Category {category} not found')

    def add_category(self):
        # Add Category
        category = input('Enter the new category (e.g., Websites, Emails): ')
        # Check if category exists
        if category in self.book:
            print(f'Category {category} exists already')
        else:
            # Add the new category to the dictionary, with blank keys and values
            self.book[category] = {}
            self.book[category]['empty'] = {'empty':'empty'} 
            print(f'Category {category} added successfully.')

    def remote_entry(self):
        # Remove entry
        category = input('Enter the category of the entry you want to remove: ')
        # Check if category exists
        if category in self.book:
            site = input('Enter the name of the entry you want to remove: ')
            if site in self.book[category]:
                del self.book[category][site]
                print(f'Entry in category {category} removed successfully.')
            else:
                print(f'Entry {site} not found')
        else:
            print(f'Category {category} not found.')

    def remove_category(self):
        # Remove Category
        category = input('Enter the category you want to remove: ')
        # Check if category exists
        if category in self.book:
                del self.book[category]
                print(f'Entry in category {category} removed successfully.')
        else:
            print(f'Category {category} not found.')

    def check_for_file(self):
        pass

    @staticmethod
    def GENERATE_KEY():
        #Ask the user to enter a secure password for the Notebook
        password = input('Please enter the password')
        # Salt the password to avoid rainbow tables, ideally it should be different each time
        salt = b'salt_123' 
        # Derive cryptographic key from the user password
        kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        iterations=100000,
        salt=salt,
        length=32
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        return key

    def ENCRYPT_AND_WRITE(self,dict):
        # Convert dictionary to JSON string, insert "Success" flag at the beginning and encrypt with user's key
        # Convert dictionary to JSON
        json_string = json.dumps(dict)
        # We need a flag to know when we have inputed the correct password for the Notebook
        # To achieve this, concatenate 'success' to the beginning of the JSON string
        json_string = 'success' + json_string
        # Encrypt the JSON
        key = Notebook.GENERATE_KEY()
        cipher_suite = Fernet(key)
        encrypted_data = cipher_suite.encrypt(json_string.encode())
        # Write encrypted data to file
        with open('Notebook.txt', 'wb') as file:
            file.write(encrypted_data)
        # Clear the data in the encrypted_data variable, for security reasons
        encrypted_data = b''

    def LOAD_AND_DECRYPT(self,key):
        # Decrypt with user's key, check for "Success" flag and convert JSON string to dictionary
        # Read the encrypted data from the file
        with open('Notebook.txt', 'rb') as file:
            encrypted_data = file.read()
        # The encryption key provided by the user
        cipher_suite = Fernet(key)
        # Decrypt the data
        decrypted_data = cipher_suite.decrypt(encrypted_data)
        # Convert the decrypted data to a string
        json_string = decrypted_data.decode()
        # Check if the 'success' string is present
        if json_string.startswith('success'):
            # Remove the 'success' string
            json_string = json_string[len('success'):]
            # Convert the JSON string to a dictionary
            result_dict = json.loads(json_string)
            # Return the dictionary
            return result_dict
        # Else exit
        else:
            print('Incorrect password, please try again')
        
nb1 = Notebook({ 
    'Websites': {
        'amazon.com':{ 
        'Username': 'johndoe',
        'Password':'pass123'
        }
        },
        'Emails': {
            'gmail': { 
            'Username': 'johndoe@gmail.com',
            'Password':'pass321'
            }
            }
        }
)

nb1.print_book()
nb1.ADD_ENTRY()
nb1.print_book()