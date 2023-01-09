"""Dataclasses in Python."""

from dataclasses import dataclass

__all__ = ["main"]
__version__ = "0.1"
__author__ = "Overzealous Lotus"
__license__ = "GPL-3.0"


# Sometimes, defining Magic Methods can become jarring.
# However, in Python, Dataclasses make this simple.
# Dataclasses allow us to add a decorator to our Class.
# This Class is now automatically configured for us.
# If we want to customize Magic Methods manually,
# we can add (init=false) to @dataclass to initalize the class ourself.
@dataclass
class Terminator:
    """Terminator dataclass."""

    # No __init__ method necessary.
    model: str
    weapon: str
    special: str = "None"  # Default is "None"


def main() -> None:
    """Main function of our program."""
    alfa: Terminator = Terminator("T-888", "V96", "Reinforced Frame")
    bravo: Terminator = Terminator("T-600", "Arm-Mounted M134")  # Default is "None" for special.
    charile: Terminator = Terminator("T-1000", "None", "Memetic Shifting")

    print(alfa.model)
    print(bravo.weapon)
    print(charile) # The __repr__ Method is created by default for us.


if __name__ == "__main__":
    main()
