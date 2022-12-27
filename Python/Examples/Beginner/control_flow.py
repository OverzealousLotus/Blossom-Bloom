"""Statement examples"""
from time import sleep

__all__ = ["main_if", "main_looping", "main_control"]
__version__ = "0.2"
__author__ = "Overzealous Lotus"


def main_if():
    """ Function to run entire program."""

    # if statement

    age: int = int(input("How old are you?:"))

    if age >= 100:
        print("You are an elderly.")
    elif age >= 18:   # An if statement, asking a question. Only runs if true.
        print("Wow! You are an adult!")
    elif age < 0:  # If its parent statement(s) are false, then this will run.
        print("You have not been born yet. Weirdo.")
    else:  # Asks if its parent statements are all false. Only runs if true.
        print("You are an adolescent.")

    temp: int = int(input("What is the temperature outside?: "))

    # This will not run if both are not true
    if not (temp >= 0 and temp <= 30):
        print("The temperature is terrible today.", "\nStay inside.")
    elif not (temp < 0 or temp > 30):  # This will run if either is true
        print("The temperature is good today.", "\nGo outside fatty.")
    elif temp is False:
        print("Wow! The temperature is exactly zero!")

    # "is" simply asks if something is something

    # Matching

    # Alternatively to elif, we can use match cause statements

    match age:
        case 100 if age >= 100:
            print("Stop being old.")
        case 18 if age >= 18:
            print("You are LEGALLY an adult.")
        case 0 if age < 0:
            print("Okay, time-traveler.")
        case _:  # _ is a placeholder
            print("I don't know what that means.")


def main_looping():
    """Second function to run program. ( Loops )"""

    name: str = ""

    while not name:  # Freezes program until input is given
        name = str(input("What is your name?: "))

    print(f"Hello, {name}")

    # for loop

    for i in range(10):  # Here, we tell Python to count up to 10.
        print(i + 1)

    for i in range(50, 100 + 1, 2):  # Python will count from 50, to 100.
        print(i)

    for i in "Joshua Salas":  # Prints every char in our name
        print(i)

    for seconds in range(10, 0, -1):  # How about we count backwards now?
        print(seconds)
        sleep(1)
    print("Happy new year.")


def main_control():
    """Tertiary function to run program. ( Loop Control )"""

    # Nesting Loops/Statements

    rows: int = int(input("How many rows?: "))
    columns: int = int(input("How many columns?: "))
    symbol: str = str(input("Enter a symbol: "))

    for index in range(rows):  # This is our outer loop
        for _ in range(columns):  # This is our inner lop
            print(symbol, end="")  # Stops from printing to new line
        print()

    # Controlling Loops

    while True:
        name = str(input("Enter your name: "))
        if name != "":
            break   # Stops the loop

    phone_number: str = "123-456-7890"

    for index in phone_number:

        if index == "-":
            continue  # Skips to the next iteration
        print(index, end="")

    for index in range(1, 21):

        if index == 13:
            pass  # Passes current iteration
        else:
            print(index)


if __name__ == "__main__":
    main_if()
    main_looping()
    main_control()
