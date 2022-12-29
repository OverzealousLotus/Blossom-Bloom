"""Built-in functions for Python."""

__all__ = ["main"]
__version__ = "0.1"
__author__ = "Overzealous Lotus"
__license__ = "GPL-3"


def main() -> None:
    """Function to run our program."""
    # Input()

    # We ask the user their name.
    name: str = input("What is your name?: ")

    # Converts user input to an integer
    age: int = int(input("How old are you?: "))

    # Converts user input to a float
    height: float = float(input("How tall are you?: "))

    age += 1

    print("Hello, " + name)
    print("You are " + str(age) + " years old.")
    print("You are " + str(height) + "CM tall.")


if __name__ == "__main__":
    main()
