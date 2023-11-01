#Initialize passwords notebook with placeholder info
notebook = { 
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

while True:
    #Continously print the notebook
    print('\nCurrent credentials in notebook:')
    for cat, name in notebook.items():
        print(f'---Category: {cat}---')
        for key, value in name.items():
            print(f' --{key}--')
            for user, passw in value.items():
                print(f'   -{user}: {passw}')

    #Print the menu and ask for input
    print('Menu: \n1. Add New Entry \n2. Remove Entry \n3. Add New Category \n4. Remove Category \n5. Exit')
    
    choice = input('Enter your choice: ')
    
    if choice == '1':
        # Add new entry
        category = input('Enter the category (e.g., Websites, Emails): ')
        #Check if category is already present
        if category in notebook:
             site = input('Enter the name of the website or service: ')
             username = input('Enter the username: ')
             password = input('Enter the password: ')
             # Add the new entry to the dictionary
             notebook[category][site] = {'Username': username, 'Password': password}
             print('New entry added successfully.')
        else:
             print(f'Category {category} not found')