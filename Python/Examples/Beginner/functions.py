"""All about Functions in Python."""

__all__ = ["main"]
__version__ = "0.1"
__author__ = "Overzealous Lotus"
__license__ = "GPL-3.0"


def main() -> None:
    """Primary function of our program."""
    # To define functions in Python, we use the "def" keyword, then our function name.
    # Below, we can see a few things going on in our function. In parenthesis, they list-
    # -expected values to be inputed when this function is called. Without them, our func-
    # -tion cannot run. This function simply adds two values together.
    def addition(
            xanther: int | float,
            yankee: int | float) -> int | float:
        """Always add Docstrings to your functions."""
        return xanther + yankee  # The "return" keyword returns our value.

    print(addition(24.5, 24.5))

    # "lambda", or "anonymous" functions, allow us to write single-line logic, without def-
    # -ining a new function.

    foxtrot: list[str] = ["0", "8", "-1", "3", "-2", "-3", "2"]

    # This lambda function sorts our list from least to greatest.
    print(sorted(foxtrot, key=lambda zulu: int(zulu)))


if __name__ == "__main__":
    main()
