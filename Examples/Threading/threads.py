"""Threading allows us to run several processes at once."""
from random import choice
from threading import Thread
from time import sleep


def fruit_gen():
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


def income():
    """Our income gain."""
    increase: int = 1
    while True:
        increase += increase
        sleep(10)
        print(f"You have gained ₼{increase} from selling fruits.")


def time():
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
