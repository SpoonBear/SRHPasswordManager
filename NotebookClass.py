import json
from cryptography.fernet import Fernet

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

    def ADD_ENTRY(self):
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

    def ADD_CATEGORY(self):
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

    def REMOVE_ENTRY(self):
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

    def REMOVE_CATEGORY(self):
        # Remove Category
        category = input('Enter the category you want to remove: ')
        # Check if category exists
        if category in self.book:
                del self.book[category]
                print(f'Entry in category {category} removed successfully.')
        else:
            print(f'Category {category} not found.')

    def GENERATE_KEY(self,input)
        #Ask the user to generate a secure password for the Password Notebook
        pass

    def ENCRYPT_AND_WRITE(self,dict,key):
        # Convert dictionary to string, insert "Success" flag at the beginning and encrypt with user's key
        # Convert dictionary to JSON
        json_string = json.dumps(dict)
        # Encrypt the JSON
        cipher_suite = Fernet(key)
        encrypted_data = cipher_suite.encrypt(json_string.encode())
        # Write encrypted data to file
        with open('Notebook.srh', 'wb') as file:
            file.write(encrypted_data)
        # Clear the data in the encrypted_data variable
        encrypted_data = b''

        pass

    def DECRYPT_AND_LOAD(self):
        # Decrypt with user's key, check for "Success" flag and convert string to dictionary
        pass


    
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