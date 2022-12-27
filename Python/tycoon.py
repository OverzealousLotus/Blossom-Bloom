"""Simple Tycoon"""

import time
import random as rd


def main():
    """Primary function of our program."""

    money: int = 0
    view_time: int = 3
    shop: dict[str, str] = {
        "Apartment": "Apartments: 50C",
        "Poolhouse": "Track, 150C",
        "Condo": "Field 250C"
    }
    properties: list[str] = []
    print("test")

    def market():
        nonlocal money

        user_choice: str = str(input("Which property suits your fancy?")).upper()
        match user_choice:
            case "APARTMENT" if money >= 50:
                properties.append("Apartment")
                shop.pop("Apartment")
                money -= 50
                print("Thank you for purchasing your shiny new house!")
                print("Owned properties:", properties)
            case "POOLHOUSE" if money >= 150:
                properties.append("Poolhouse")
                shop.pop("Poolhouse")
                money -= 150
                print("Thank you for purchasing your new home.")
                print("Owned properties:", properties)
            case "Condo" if money >= 250:
                properties.append("Condo")
                shop.pop("Condo")
                money -= 250
                print("Thank you for purchasing your new Dorm Room.")
                print("Owned properties:", properties)
            case _:
                pass

    while shop:
        if shop is False:
            print("Congratulations, you own a monopoly of properties!")
            break
        time.sleep(1)

        money += rd.randint(1, 5)
        view_time -= 1

        if view_time:
            print("")
        else:
            print("You now have", money, "patience money.")
            view_time = 3

        if money > 50:
            user_choice = str(input("\"y\" to buy, otherwise \"n\" to decline: "))
            if user_choice == "y":
                print(shop)
                market()
            else:
                continue


if __name__ == "__main__":
    main()
