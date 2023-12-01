import json
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64

# Your dictionary
nb1 = {
    'Websites': {
        'amazon.com': {
            'Username': 'johndoe',
            'Password': 'pass123'
        }
    },
    'Emails': {
        'gmail': {
            'Username': 'johndoe@gmail.com',
            'Password': 'pass321'
        }
    }
}

# Step 1: Convert the dictionary to a JSON string
json_string = json.dumps(nb1)

# Step 2: Derive a key from the password
password = 'password'
salt = b'salt_123'  # You should use a different salt for each encryption
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    iterations=100000,  # You can adjust the number of iterations for security
    salt=salt,
    length=32  # The length of the derived key, which must match the key length for Fernet
)
key = base64.urlsafe_b64encode(kdf.derive(password.encode()))

# Step 3: Encrypt the JSON string
cipher_suite = Fernet(key)
encrypted_data = cipher_suite.encrypt(json_string.encode())

# Write the encrypted data to a file
with open('encrypted_data.txt', 'wb') as file:
    file.write(encrypted_data)

print("Encrypted Data has been written to 'encrypted_data.txt'")
