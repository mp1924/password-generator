import hashlib
import base64
import os
from cryptography.fernet import Fernet

# ---------------- KEY DERIVATION ----------------
def derive_key(password, salt):
    try:
        key = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode(),
            salt.encode(),
            100000
        )
        return base64.urlsafe_b64encode(key)
    except Exception as e:
        print(f"Error in key derivation: {e}")
        raise

# ---------------- ENCRYPT / DECRYPT ----------------
def create_cipher(key):
    return Fernet(key)

def encrypt_password(cipher, password):
    try:
        return cipher.encrypt(password.encode()).decode()
    except Exception as e:
        print(f"Error during encryption: {e}")
        raise

def decrypt_password(cipher, encrypted_password):
    try:
        return cipher.decrypt(encrypted_password.encode()).decode()
    except Exception as e:
        print(f"Error during decryption: {e}")
        raise
