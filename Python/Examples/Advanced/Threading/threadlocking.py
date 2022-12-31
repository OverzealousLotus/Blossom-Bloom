"""Example about threadlocking in Python."""
from random import choice, randint
from threading import Lock, Thread
from time import sleep
from typing import Any

__all__ = ["main"]
__version__ = "0.1"
__author__ = "Overzealous Lotus"
__license__ = "GPL-3.0"


def main() -> None:
    """Main function of our program."""
    money: int = 0
    threadlock = Lock()
    enter: str = "No"
    inventory: list[str] = []
    merch: dict[str, str] = {
        "Umbrella": "$10",

        "Candy": "$30",

        "Wheels": "$50"
    }


    def fruit_sell() -> None:
        """Where our fruit is sold."""
        nonlocal money, threadlock, enter
        if enter == "YES":
            threadlock.release()
        else:
            threadlock.acquire()

        while True:
            sleep(1)
            fruit: Any = choice([
                "Pineapple",
                "Grape",
                "Kiwi",
                "Strawberry",
                "Dragonfruit",
                "Durian"
            ])
            money += randint(3, 10)
            print(f"{fruit} sold at our market! money:{money}\r", end="", flush=True)
            print("")


    def shop() -> None:
        """Where user can purchase items."""
        nonlocal money, threadlock, enter, inventory, merch
        while True:
            if enter == "YES":
                threadlock.acquire()

                user_choice = str(input(" \nPlease choose from these items:")).upper()
                print("Otherwise, type anything to cancel.")

                if user_choice == "UMBRELLA":
                    inventory.append("Umbrella")
                    merch.pop("Umbrella")
                    money -= 10
                elif user_choice == "CANDY":
                    inventory.append("Candy")
                    merch.pop("Candy")
                elif user_choice == "WHEELS":
                    inventory.append("Wheels")
                    merch.pop("Wheels")
            else:
                threadlock.release()
            enter = str(input("Type 'Yes' at anytime to enter the shop.")).upper()


    thread_one = Thread(target=fruit_sell)
    thread_two = Thread(target=shop)

    thread_one.start()
    thread_two.start()

if __name__ == "__main__":
    main()
