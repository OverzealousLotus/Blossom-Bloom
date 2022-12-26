"""Basic Encryption in Python."""
import base64

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

PASSWORD_PROVIDED = 'password'  # This is input in the form of a string
PASSWORD = PASSWORD_PROVIDED.encode()  # Convert password to bytes

SALT = b'A\x94@<\xdb\x88=f\x10\x00\xe3\xd4\x92\xd6\xf0>\xf8\x0fa\n\x80$W\xbf\x9cQ;c\xaa\xab\xfa\x00'
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA512(),
    length=32,
    salt=SALT,
    iterations=100000,
    backend=default_backend()
)

key = base64.urlsafe_b64encode(kdf.derive(PASSWORD))  # Can only use kdf once
print(key)
