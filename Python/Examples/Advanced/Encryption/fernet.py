"""Key generation for encryption."""

from time import sleep
from typing import Any

from cryptography.fernet import Fernet

__all__ = ["main"]
__version__ = "0.1"
__author__ = "Overzealous Lotus"
__license__ = "GPL-3.0"


def main() -> None:
    """Main function of our program."""
    iteration: int = 5
    key_array: list[Any] = []

    try:
        print("Procuring keys... \n")

        while iteration > 0:
            sleep(1)
            iteration -= 1
            key: bytes = Fernet.generate_key()
            key_array.append(key)

        print("The following keys have been produced: ")

        for index in key_array:
            sleep(0.5)
            print(index)
    except KeyboardInterrupt:
        print("\nKey generation stopped by user.")
    except RuntimeError:
        print("What did you do?")


if __name__ == "__main__":
    main()
