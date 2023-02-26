import hashlib

# Define a dictionary to store user information
users = {}

# Function to hash the password using SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

# Function to register a new user
def register():
    username = input('Enter a username: ')
    password = input('Enter a password: ')
    hashed_password = hash_password(password)
    users[username] = hashed_password
    print('Registration successful')

# Function to authenticate a user
def authenticate():
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    if username in users:
        hashed_password = hash_password(password)
        if hashed_password == users[username]:
            return True
    return False

# Example usage
register()
if authenticate():
    print('Authentication successful')
else:
    print('Authentication failed')