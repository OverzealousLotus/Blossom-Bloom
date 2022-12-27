"""Data Methodology"""

__all__ = ["main"]
__version__ = "0.1"
__author__ = "Overzealous Lotus"


def main():
    """Function used to run our program."""

    xanther, yankee, zulu = 1, 2.0, "3"

    # Modifies a variable to become an integer
    yankee = int(yankee)
    # Modifies a variable to become a float
    zulu = float(zulu)
    # Modifies a variable to become a string
    xanther = str(xanther)

    print(xanther)

    print(yankee)

    print(zulu * 3)

    # Lists

    food: list = ["Pizza", "Ramen", "Hamburger", "Hotdog", "Pudding"]

    # To access an item in our list, we use square brackets.
    print(food[3])

    # Pizza is now Mochi
    food[0] = "Mochi"

    print(food[0])

    for i in food:
        print(i)

    # Adds an item
    food.append("Ice Cream")

    # Removes an item
    food.remove("Hotdog")

    # Removes the last listed item in the list
    food.pop()

    # Inserts an item at a given point in the list
    food.insert(0, "Cake")

    # Sort lists alphabetically
    food.sort()

    # List is cleared of all ltems
    food.clear()


if __name__ == "__main__":
    main()
