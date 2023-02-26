import hashlib

password = input("Enter your password: ")

# Encode the password string to bytes using UTF-8 encoding
password_bytes = password.encode('utf-8')

# Create a SHA-256 hash object
hash_object = hashlib.sha256()

# Update the hash object with the password bytes
hash_object.update(password_bytes)

# Get the encrypted password as a hexadecimal string
encrypted_password = hash_object.hexdigest()

print(f"Encrypted password: {encrypted_password}")