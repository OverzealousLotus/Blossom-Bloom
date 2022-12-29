"""Usable implementation of Python encryption."""
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
    """Main function of the program."""
    admin_pwd_provided = 'password'  # This is input in the form of a string
    admin_pwd = admin_pwd_provided.encode()  # Convert password to bytes

    user_pwd_provided = 'birthday'
    user_pwd = user_pwd_provided.encode()

    salt = urandom(32)
    admin_kdf = PBKDF2HMAC(
        algorithm=hashes.SHA512(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )

    adminlogin_kdf = PBKDF2HMAC(
        algorithm=hashes.SHA512(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )

    user_kdf = PBKDF2HMAC(
        algorithm=hashes.SHA512(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )

    userlogin_kdf = PBKDF2HMAC(
        algorithm=hashes.SHA512(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )

    # Can only use kdfs once
    admin_pw = base64.urlsafe_b64encode(admin_kdf.derive(admin_pwd))
    user_pw = base64.urlsafe_b64encode(user_kdf.derive(user_pwd))

    inputted_pwd = ''
    username = ''

    try:
        while True:
            username = str(input('What is your username? ')).upper()

            if username == 'ADMIN':
                inputted_pwd = str(input('What is your password? ')).encode()
                hashed_pw = base64.urlsafe_b64encode(adminlogin_kdf.derive(inputted_pwd))
                if hashed_pw == admin_pw:
                    print('Welcome, Johnson.')
                    break
                else:
                    print('Incorrect password.')
            elif username == username:
                inputted_pwd = str(input('What is your password? ')).encode()
                public_pw = base64.urlsafe_b64encode(userlogin_kdf.derive(inputted_pwd))
                if public_pw == user_pw:
                    print(f'Welcome, {username}.')
                    break
                else:
                    print('Incorrect password.')
            else:
                raise RuntimeError('Unknown error, or possible exploit attempt.')
    except KeyboardInterrupt:
        print('Login aborted by user.')


if __name__ == "__main__":
    main()
