"""Math functions"""

__all__ = ["main"]
__version__ = "0.1"
__author__ = "Overzealous Lotus"

import math  # Importing math


def main():
    """Function used to run entire program."""

    pie: float = 3.13
    xanther: int = 1
    yankee: int = 2
    zulu: int = 3

    # Rounds to the nearest integer
    print(round(pie))

    # Rounds upwards
    print(math.ceil(pie))

    # Rounds downwards
    print(math.floor(pie))

    # Notifies Python how far a value is from zero
    print(abs(pie))

    # Raises a value to a given power
    print(pow(pie, 2))

    # Square roots a given value
    print(math.sqrt(pie))

    # Cube roots a given valsue
    print(math.cbrt(pie))

    # Searches for the highest value
    print(max(xanther, yankee, zulu))

    # Searches for the lowest value
    print(min(xanther, yankee, zulu))


if __name__ == "__main__":
    main()
