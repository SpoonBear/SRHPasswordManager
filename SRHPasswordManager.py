import json
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import os

class User:
    # Hypothetical user class to expand the domains of the project
    def __init__(self, ID, username, password,sub_status) -> None:
        self.ID = ID
        self.username = username
        self.passowrd = password
        self.sub_status = sub_status

    def login(self):
        # Hypothetical method to expand the domains of the project
        # Logs into user account
        pass

    def subscribe(self):
        # Hypothetical method to expand the domains of the project
        # Enables subscription so the user can access premium features, like
        # SSO and Check for Leaks
        pass
    
class Services:
    # Hypothetical user class to expand the domains of the project
    def __init__(self,sso_status,backup_recovery_status,subscription_status) -> None:
        self.sso_status = sso_status
        self.backup_recovery_status = backup_recovery_status
        self.subscription_status = subscription_status

    def sso_service(self):
        # Hypothetical method to expand the domains of the project
        # Service providing Single Sign On to users.
        pass

    def subscription_service(self):
        # Hypothetical method to expand the domains of the project
        # Service that manages the subscription of status of the users so they can access premium features, like
        # SSO and Check for Leaks
        pass
    
    def backup_recovery_service(self):
        # Hypothetical method to expand the domains of the project
        # Service that manages cloud saves and backups of the credentials
        pass

class Notebook:
    def __init__(self, book) -> None:
        self.book = book
        
    def __str__(self) -> str:
        return f'{self.book}'

    def print_book(self):
        # Iterate through the dictionary to print it
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
        # Check if the 'Notebook.txt' file exists in the current directory
        file_path = 'Notebook.txt'
        if os.path.exists(file_path):
            print(f'The file {file_path} exists.')
            return 1
        else:
            print(f'The file {file_path} does not exist.') 
            return 0           

    @staticmethod
    def generate_key():
        # Ask the user to enter a secure password for the Notebook
        password = input('Please enter the master password\n')
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

    def encrypt_and_write(self, key):
        # Convert dictionary to JSON string and encrypt with user's key
        # Convert dictionary to JSON
        json_string = json.dumps(self.book)
        # Encrypt the JSON
        cipher_suite = Fernet(key)
        encrypted_data = cipher_suite.encrypt(json_string.encode())
        # Write encrypted data to file
        with open('Notebook.txt', 'wb') as file:
            file.write(encrypted_data)
        # Clear the data in the encrypted_data variable, for security reasons
        encrypted_data = b''

    def load_and_decrypt(self,key):
        # Decrypt with user's key, check for "Success" flag and convert JSON string to dictionary
        # Read the encrypted data from the file
        with open('Notebook.txt', 'rb') as file:
            encrypted_data = file.read()
        # The encryption key provided by the user
        cipher_suite = Fernet(key)
        try:
            # Decrypt the data
            decrypted_data = cipher_suite.decrypt(encrypted_data)
            # Convert the decrypted data to a string
            json_string = decrypted_data.decode()
            # Convert the JSON string to a dictionary
            result_dict = json.loads(json_string)
            return result_dict
        except InvalidToken:
            print('Incorrect password, please try again')
            return None
        
    def check_for_leaks(self):
        # Hypothetical method to expand the domains of the project
        # Sends storaged usernames/emails to the HaveIBeenPwned API and a security operations team,
        # where they will be checked for leaks in the clear and dark web. A report will be emailed to the user
        pass
    
    def generate_passphrase(self):
        # Hypothetical method to expand the domains of the project
        # Generates a secure and easy to remeber passphrase, e.g. 'PhoneSnowNickelPolish'
        pass

    def password_strength_analysis(self):
        # Hypothetical method to expand the domains of the project
        # Analyses the stored passwords and reports the strength,
        # such as usage of lowercase, uppercase, numbers, special characters and length
        pass

    def cloud_backup_and_recovery(self):
        # Hypothetical method to expand the domains of the project
        # Manages cloud saves and backups of the credentials
        pass

    def ui_ux(self):
        # Hypothetical method to expand the domains of the project
        # Should display a functioning and intuitive GUI
        pass


nb1 = Notebook({})

print('Welcome to the Passwords Notebook\nChecking for an existing Notebook')
# Check for existing Notebook.txt file containing the passwords
notebook_exists = nb1.check_for_file()
if notebook_exists == 1:
    # Ask user for the master password password, key will be used for decryption and encryption
    key = nb1.generate_key()
    # Load file, decrypt using key and load contents into the object
    if nb1.load_and_decrypt(key) is not None:
        nb1 = Notebook(nb1.load_and_decrypt(key))
        # Continously print the dictionary and show the menu
        while True:
            # Print the dictionary
            nb1.print_book()
            # Show the menu
            print('Menu: \n1. Add New Entry \n2. Remove Entry \n3. Add New Category \n4. Remove Category \n5. Save Notebook \n6. Change master password \n0. Exit')
            choice = input('Enter your choice: ')
            if choice == '1':
                nb1.add_entry()
            elif choice == '2':
                nb1.remote_entry()
            elif choice == '3':
                nb1.add_category()
            elif choice == '4':
                nb1.remove_category()
            elif choice == '5':
                nb1.encrypt_and_write(key)
            elif choice == '6':
                print('Changes will be saved\n')
                key = nb1.generate_key()
                nb1.encrypt_and_write(key)
            elif choice == '0':
                # Exit the program
                # Wipe the key for security reasons
                key = b''
                print('Exiting program...')
                break
            else:
                print("Invalid choice. Please try again.")
else:
    # File was not found, create one or exit
    print('Notebook.txt was not found\n Please choose:\n 1. Create a new Notebook\n 2. Exit')
    choice = input('Enter your choice: ')
    if choice == '1':
        # Create new Notebook.txt file with mock data
        print('Creating new Notebook')
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
        # Ask for the password for the new Notebook
        nb1.encrypt_and_write(nb1.generate_key())
        print('New Notebook has been created')
    elif choice == '2':
        #Exit program
        print('Exiting program...')
    else:
        print("Invalid choice. Please try again.")

