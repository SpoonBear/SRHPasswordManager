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
        category = input('Enter the category (e.g., Websites, Emails): ')#Take out of class?
        # Check if category exists
        #Take check out of class?
        if category in self.book:
             site = input('Enter the name of the website or service: ')
             username = input('Enter the username: ')
             password = input('Enter the password: ')
             # Add the new entry to the dictionary
             self.book[category][site] = {'Username': username, 'Password': password}
             print('New entry added successfully.')
        else:
             print(f'Category {category} not found')
    
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