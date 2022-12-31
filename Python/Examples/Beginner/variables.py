"""Data Methodology."""

__all__ = ["main"]
__version__ = "0.1"
__author__ = "Overzealous Lotus"
__license__ = "GPL-3.0"


def main() -> None:
    """Function used to run our program."""
    # <===| Defining Variables |===>
    # Defining variables can be done in a single, or multiple lines.
    # For simplicity sake, we'll first use multiple lines.

    # Integer
    xanther = 1

    # Float
    yankee = 2.0

    # String
    zulu = "3"

    # Boolean
    wunder = False

    # <| Modification |>
    # "int()" converts variables to an Integer, if possible.
    yankee = int(yankee)
    # "float()" converts variables to a Float, if possible.
    zulu = float(zulu)
    # "str()" converts variables to a String, if possible.
    xanther = str(xanther)

    # Printing our defined values:
    print(f"{xanther} nut, {yankee} honey jars, {zulu} beans, and a {wunder} God.")

    # <===| Lists |===>
    # Lists can contain multiple pieces of data. Below, "food" is filled with Strings.
    # Each item must be separated by commas.
    food: list[str] = ["Pizza", "Ramen", "Hamburger", "Hotdog", "Pudding"]

    # To access an item in our List, we use square brackets.
    # Remember, computers always start at zero. So, 0 is item one, etc.
    print(food[3])

    # <| Modification |>

    # Similar to defining variables, we can re-define items in a List.
    food[0] = "Mochi"
    print(food[0])

    # Or... Display every single item.
    for i in food:
        print(i)

    # "append()" adds an item to a List.
    food.append("Ice Cream")

    # "remove()" removes items in a List.
    food.remove("Hotdog")

    # "pop()" removes the last item in a List.
    food.pop()

    # "insert()" adds items to a given point in a List.
    food.insert(0, "Cake")

    # "sort()"  organizes a List alphabetically.
    food.sort()

    # "clear()" completely wipes the List empty.
    food.clear()

    # <===| String Manipulation |===>
    # Strings are one of the most basic data types in Python.
    # Thus, the various methods used to modify them are necessary-
    # -when working with variables. There are three options for Strings:
    # [start:finish:step]

    # [start] is where we start in a String.

    # [finish] is where we end in a String.

    # [step] is the number of steps we take in a String.

    name: str = "Josh Brewer"

    # "len()" returns the length of a given String.
    print(len(name))

    # "find()" searches for a character in a String, then returns it.
    print(name.find("e"))

    # "capitalize()" will capitalize the start of a String.
    print(name.capitalize())

    # "upper()" converts our whole String to Uppercase.
    print(name.upper())

    # "lower()" is the opposite of "upper()"
    print(name.lower())

    # Asks if the provided variable is a digit or not.
    print(name.isdigit())

    # Asks if the provided variable is numerical or not.
    print(name.isnumeric())

    # Asks if a variable only contains alphabetical characters.
    print(name.isalpha())

    # Prints the amount of a given character.
    print(name.count("a"))

    # Multiplies the amount of times a variable is printed to the console.
    print(name * 5)

    # Removes Brewer from our "name" variable.
    print(name[slice(5, 11)])

    # <| Concatenated String Variables |>

    # Defines Forename as Josh
    forename: str = name[0:4]

    # Defines Surname as Brewer
    surname: str = name[5:11]

    # Defines Byname as Js rwr
    byname: str = name[0:11:2]

    # Defines Sillyname as Josh Brewer, but backwards
    silly_name: str = name[0:11:-1]

    # Prints all the above in newlines
    print("I am " + forename + "\n" + surname)
    print("Your name is " + byname + "\n" + silly_name)

    # Alternatively, we can use F-Strings to simplify the process.

    print(f"I am {forename} \n {surname}")
    print(f"Your name is {byname} \n {silly_name}")


if __name__ == "__main__":
    main()
