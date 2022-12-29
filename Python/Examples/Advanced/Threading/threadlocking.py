"""Example about threadlocking in Python."""
from random import choice, randint
from threading import Lock, Thread
from time import sleep
from typing import Any

credits: int = 0
threadlock = Lock()
open: str = "No"
user_items: list[str] = []
shop_items: dict[str, str] = {
    "Umbrella": "10 credits",

    "Candy": "30 credits",

    "Wheels": "50 credits"
}


def fruit_sell() -> None:
    """Where our fruit is sold."""
    global credits, threadlock, open
    if open == "YES":
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
        credits += randint(3, 10)
        print(f"{fruit} sold at our market! credits:{credits}\r", end="", flush=True)
        print("")


def shop() -> None:
    """Where user can purchase items."""
    global credits, threadlock, open, user_choice, user_items, shop_items
    while True:
        if open == "YES":
            threadlock.acquire()

            user_choice = str(input(" \nPlease choose from these items:")).upper()
            print("Otherwise, type anything to cancel.")

            if user_choice == "UMBRELLA":
                user_items.append("Umbrella")
                shop_items.pop("Umbrella")
                credits -= 10
            elif user_choice == "CANDY":
                user_items.append("Candy")
                shop_items.pop("Candy")
            elif user_choice == "WHEELS":
                user_items.append("Wheels")
                shop_items.pop("Wheels")
        else:
            threadlock.release()
        open = str(input("Type \"Yes\" at anytime to open the shop.")).upper()


thread_one = Thread(target=fruit_sell)
thread_two = Thread(target=shop)

thread_one.start()
thread_two.start()
