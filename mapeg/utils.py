from cryptography.fernet import Fernet
import base64
import os 


# Generate a key and save it in a secure place
# You can generate a key once and reuse it

key = base64.urlsafe_b64encode(os.urandom(32))
fernet  = Fernet(key)

def encrypt_id(plain_text_id):
    """Encrypt the plain text id."""
    # Ensure plain_text_id is converted to string and encoded
    return fernet.encrypt(str(plain_text_id).encode()).decode()

def decrypt_id(encrypted_id):
    """Decrypt the encrypted id."""
    # Ensure encrypted_id is decoded from string back to bytes
    return fernet.decrypt(encrypted_id.encode()).decode()
