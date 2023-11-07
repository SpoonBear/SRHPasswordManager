#Notebook as class
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

    def remove_entry(self):
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

    def encrypt(self):
        # Convert dictionary to string, insert "Success" flag at the beginning and encrypt with user's key
        pass

    def decrypt(self):
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
nb1.add_entry()
nb1.print_book()