"""Threading allows us to run several processes at once."""
from random import choice
from threading import Thread
from time import sleep

__all__ = ["main"]
__version__ = "0.1"
__author__ = "Overzealous Lotus"
__license__ = "GPL-3.0"


def main() -> None:
    """Main function of our program."""
    def fruit_gen() -> None:
        """Fruit generation."""
        while True:
            our_fruit = choice([
                "Apple",
                "Orange",
                "Pear",
                "Melon",
                "Kiwi",
                "Banana",
                "Pineapple",
                "Tomato",
                "Dragonfruit",
                "Starfruit",
                "Grape bundle",
                "Blackberry bundle",
                "Strawberry bundle",
                "Raspberry bundle"
                ])
            sleep(2)
            print(f"One of our {our_fruit}s has been sold!")


    def income() -> None:
        """Our income gain."""
        increase: int = 1
        while True:
            increase += increase
            sleep(10)
            print(f"You have gained ₼{increase} from selling fruits.")


    def time() -> None:
        """Our time passing."""
        days: int = 0
        while True:
            days += 1
            sleep(90)
            print(f"\n{days} has passed since first opening.")


    fruit_thread = Thread(target=fruit_gen)
    income_thread = Thread(target=income)
    time_thread = Thread(target=time)


    fruit_thread.start()
    income_thread.start()
    time_thread.start()


if __name__ == "__main__":
    main()
