"""Basic Encryption in Python."""
import base64
from os import urandom

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

__all__ = ["main"]
__version__ = "0.1"
__author__ = "Overzealous Lotus"
__license__ = "GPL-3"


def main() -> None:
    """Main function of our program."""
    pwd_provided = 'password'  # This is input in the form of a string
    pwd = pwd_provided.encode()  # Convert password to bytes

    salt = urandom(32)  # Always use Salt during Encryption.
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA512(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )

    key = base64.urlsafe_b64encode(kdf.derive(pwd))  # Can only use kdf once
    print(key)


if __name__ == "__main__":
    main()
