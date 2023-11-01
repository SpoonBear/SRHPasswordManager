# Initialize passwords dictionary with placeholder info
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
    # Continously print the dictionary
    print('\nCurrent credentials in notebook:\n')
    for cat, name in notebook.items():
        print(f'---Category: {cat}---')
        for key, value in name.items():
            print(f' --{key}--')
            for user, passw in value.items():
                print(f'   -{user}: {passw}')

    # Print the menu and ask for input
    print('Menu: \n1. Add New Entry \n2. Remove Entry \n3. Add New Category \n4. Remove Category \n5. Exit')
    
    choice = input('Enter your choice: ')
    
    if choice == '1':
        # Add new entry
        category = input('Enter the category (e.g., Websites, Emails): ')
        # Check if category exists
        if category in notebook:
             site = input('Enter the name of the website or service: ')
             username = input('Enter the username: ')
             password = input('Enter the password: ')
             # Add the new entry to the dictionary
             notebook[category][site] = {'Username': username, 'Password': password}
             print('New entry added successfully.')
        else:
             print(f'Category {category} not found')
             
    elif choice == '2':
        # Remove entry
        category = input('Enter the category of the entry you want to remove: ')
        # Check if category exists
        if category in notebook:
            site = input('Enter the name of the entry you want to remove: ')
            if site in notebook[category]:
                del notebook[category][site]
                print(f'Entry in category {category} removed successfully.')
        else:
            print(f'Category {category} not found.')
            
    elif choice == '3':
        # Add Category
        category = input('Enter the new category (e.g., Websites, Emails): ')
        # Check if category exists
        if category in notebook:
            print(f'Category {category} exists already')

        else:
            # Add the new category to the dictionary, with blank keys and values
            notebook[category] = {}
            notebook[category]['empty'] = {'empty':'empty'} 
            print('New category added successfully.')

    elif choice == '4':
        # Remove Category
        category = input('Enter the category you want to remove: ')
        # Check if category exists
        if category in notebook:
                del notebook[category]
                print(f'Entry in category {category} removed successfully.')
        else:
            print(f'Category {category} not found.')

    elif choice == '5':
        # Exit the program
        print('Exiting program...')
        break
    
    else:
        print("Invalid choice. Please try again.")