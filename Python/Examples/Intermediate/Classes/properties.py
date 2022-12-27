"""Properties"""

__all__ = ["main"]
__version__ = "0.1"
__author__ = "Overzealous Lotus"


def main():
    """Function used to run our program"""
    class SoftwareEngineer():
        """Our SoftwareEngineer() class"""

        def __init__(self):
            self._salary: int = 0

        @property  # Allows us to get salary
        def salary(self):
            "Calls one of our Protected attributes"
            return self._salary

        @salary.setter  # Allows salary to be its own setter
        def salary(self, value: int):
            "Sets one of our Protected attributes' value"
            self._salary = value

        @salary.deleter  # Allows us to delete salary
        def salary(self):
            "Sets one of our Protected attributes' value"
            del self._salary

    worker = SoftwareEngineer()

    worker.salary = 6000
    print(worker.salary)
    del worker.salary
    print(worker.salary)  # Pylance does not like this.


if __name__ == "__main__":
    main()