"""Encapsulation"""

__all__ = ["main"]
__version__ = "0.1"
__author__ = "Overzealous Lotus"


def main():
    """Function to run our program."""
    class SoftwareEngineer():
        """Our SoftwareEngineer() class"""

        def __init__(self, name: str, age: int):
            self.name = name  # Public attributes
            self.age = age
            self._salary: int = 0  # Protected attribute, still callable
            self.__bugs_solved: int = 0  # Private attribute, not callable

        def code(self):
            "Increases the number of bugs solved"
            self.__bugs_solved += 1

        # Getter function
        def get_salary(self):
            "Calls one of our Protected attributes"
            return self._salary

        # Setter function
        def set_salary(self, base_value: int):
            "Sets one of our Protected attributes' value"
            self._salary = self._calc_salary(base_value)

        def _calc_salary(self, base_value: int):  # Protected function
            "Modifies our engineer's salary based on their bugs solved"
            if self.__bugs_solved < 10:
                return base_value
            if self.__bugs_solved < 100:
                return base_value*2
            return base_value*3

    worker = SoftwareEngineer("Max", 25)
    print(worker.name, worker.age)

    for _ in range(70):
        worker.code()

    worker.set_salary(6000)
    print(worker.get_salary())


if __name__ == "__main__":
    main()
