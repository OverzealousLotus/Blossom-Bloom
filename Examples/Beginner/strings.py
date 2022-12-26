"Python String Concatination Examples"

__all__ = ["main"]
__version__ = "0.2"
__author__ = "Overzealous Lotus"


def main():
    """Function to run our program."""

    # The three values we can modify:
    # [start:finish:step]

    # [start] is where we start in a String.

    # [finish] is where we end in a String.

    # [step] is the number of steps we take in a String."""

    name: str = "Josh Brewer"

    # <===| String Manipulation |===>

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

    # Asks if the provided variable is a digit or not
    print(name.isdigit())

    # Asks if the provided variable is numerical or not
    print(name.isnumeric())

    # Asks if var only contains alphabetical characters
    print(name.isalpha())

    # Prints the amount of a given character
    print(name.count("a"))

    # Multiplies variable print to console
    print(name * 5)

    # Removes Brewer from NAME
    print(name[slice(5, 11)])

    # <===| Concatenated Variables |===>

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
