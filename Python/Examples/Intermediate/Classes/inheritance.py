"""Inheritance in Python."""
from typing import Any, Self

__all__ = ["main"]
__version__ = "0.1"
__author__ = "Overzealous Lotus"


def main() -> None:
    """Function to run our program."""
    class Employee():
        """Our main class."""

        def __init__(self: Self, name: str, age: int, salary: int) -> None:
            """Defines our class attributes."""
            self.name = name
            self.age = age
            self.salary = salary

        def work(self: Self) -> None:  # All Subclasses of Employee() can use this method
            """Tells our user an Employee is working, but is overridden."""
            print(f"{self.name} is working...")

    class SoftwareEngineer(Employee):
        """One of our subclasses, inheriting Employee."""

        def __init__(self: Self, name: str, age: int, salary: int, level: str) -> None:
            """Inherits attributes from Employee using super()."""
            # "super()"" lets us inherit all attributes from our Subclass"s parent
            super().__init__(name, age, salary)
            self.level = level  # This attribute is exclusive to our SE Subclass

        def work(self: Self) -> None:
            """Tells our user an Employee is working."""
            print(f"{self.name} is coding...")

        def debug(self: Self) -> None:  # Exclusive method to only our SE Subclass.
            """Tells us if our Software Engineer is debugging."""
            print(f"{self.name} is debugging...")

    class Designer(Employee):
        """Another subclass, inheriting Employee attributes."""

        def work(self: Self) -> None:
            """Tells our user an Employee is working."""
            print(f"{self.name} is designing...")

        def draw(self: Self) -> None:  # Exclusive method to only our Designer Subclass
            """Notifies us of our Designer drawing."""
            print(f"{self.name} is drawing...")

    # While DE and SE do both inherit Employee"s attributes, they have differences

    worker_one = SoftwareEngineer("Faraday", 20, 6000, "Junior")
    worker_one.work()
    worker_one.debug()

    worker_two = Designer("Newton", 20, 7000)
    worker_two.work()
    worker_two.draw()

    # Polymorphism

    workforce = [
        SoftwareEngineer("Max", 25, 6000, "Junior"),
        SoftwareEngineer("Lisa", 30, 9000, "Senior"),
        Designer("Frank", 27, 7000)]

    def mote_workforce(workforce: list[Any]) -> None:
        """Grabs our listed instances, and orders them to work."""
        for employee in workforce:
            employee.work()

    mote_workforce(workforce)


if __name__ == "__main__":
    main()
