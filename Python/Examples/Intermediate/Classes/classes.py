"""Object Oriented Programming"""
from typing import Any

__all__ = ["main_classing"]
__version__ = "0.2"
__author__ = "Overzealous Lotus"


def main_classing():
    """First function to run our program."""
    class SoftwareEngineer():
        """instance attributes"""

        # class attribute
        alias = "Keyboard Mage"  # This is a class-wide attribute

        def __init__(self, name: str, age: int, level: str, salary: int):  # Define our attributes
            self.name = name
            self.age = age
            self.level = level
            self.salary = salary

        # instance method

        def coding(self):  # These are basic methods we define ourself in classes
            "Lets our user know who is coding right now"

            print(f"{self.name} is writing code...")

        def c_language(self, language: str):  # Without self, does not work
            "Lets our user know what language who is writing in"

            print(f"{self.name} is writing code in {language}...")

        # Dunder method
        def __str__(self):  # When called, info is shown
            "Information about our objects"

            info = f"Name = {self.name}, age = {self.age}, level = {self.level}"
            return info

        # Equalizer Method
        def __eq__(self, other: Any):  # By default, compares memory
            "Comparison between two objects."

            return self.name == other.name and self.age == other.age

        @staticmethod  # Fixes a problem when the self attribute is not present
        def entry_salary(age: int):
            "Checks what a worker's salary should be"
            if age < 25:
                return 5000
            if age < 30:
                return 7000
            return 9000

    # instance

    worker_one = SoftwareEngineer("Jason", 20, "Junior", 5000)
    worker_two = SoftwareEngineer("Garret", 25, "Senior", 7000)
    worker_tres = SoftwareEngineer("Garret", 25, "Senior", 7000)

    worker_one.coding()
    worker_two.coding()

    worker_one.c_language("Python")
    worker_two.c_language("Bash")

    print(f"{worker_one} and {worker_two}")

    print(worker_tres == worker_two)


if __name__ == "__main__":
    main_classing()
