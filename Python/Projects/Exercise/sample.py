"""A program to practice my Python syntax recollection."""
# In W3Schools, they have their own, but it's not enough for me.

from typing import Any

user_choice: Any = None
completion: bool = False

try:
    while completion is False:

        print('|class MyClass():')
        print('|    def __init__(self, template)')
        print('|        self.template = template \n|')
        print('|@{Which decorator?}')
        print('|def my_function(template):')
        print('|    template += 1\n')

        user_choice: Any = input('When the "self" attribute is not present in a class function, what decorator is used?: ')

        if user_choice != "@staticmethod":
            print(f"{user_choice} is incorrect. Please try again.")

        user_choice: Any = None

        print('|class MyClass():')
        print('|    def __init__(self, template):')
        print('|        self.{character here}template = template \n|')

        user_choice: Any = input('What character is used to define an attribute as Protected?')

        if user_choice != "_":
            print(f"{user_choice} is incorrect. Please try again.")

        user_choice: Any = None
except KeyboardInterrupt:
    print('\nExercise interrupted by user.')
except RuntimeError:
    print('An unknown error has occurred.')
