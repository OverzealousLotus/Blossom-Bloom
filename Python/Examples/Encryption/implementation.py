"""Usable implementation of Python encryption."""
import base64

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

admin_pwd_provided = 'password'  # This is input in the form of a string
admin_pwd = admin_pwd_provided.encode()  # Convert password to bytes

user_pwd_provided = 'birthday'
user_pwd = user_pwd_provided.encode()

SALT = b'\xb1?\xed\xac\xd9\xe1\x91\x1e!\xb3\xe79\xf2\x03{Wr\x83\x06\xe5\x8cm\xf3@\xdd6\xb8vw+M\x91'
admin_kdf = PBKDF2HMAC(
    algorithm=hashes.SHA512(),
    length=32,
    salt=SALT,
    iterations=100000,
    backend=default_backend()
)

adminlogin_kdf = PBKDF2HMAC(
    algorithm=hashes.SHA512(),
    length=32,
    salt=SALT,
    iterations=100000,
    backend=default_backend()
)

user_kdf = PBKDF2HMAC(
    algorithm=hashes.SHA512(),
    length=32,
    salt=SALT,
    iterations=100000,
    backend=default_backend()
)

userlogin_kdf = PBKDF2HMAC(
    algorithm=hashes.SHA512(),
    length=32,
    salt=SALT,
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
