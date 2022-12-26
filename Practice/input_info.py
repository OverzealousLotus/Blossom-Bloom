"""A program that asks a user their name, & age, then returns the year they will turn 100."""

from datetime import date

def main():
    """Primary function of our program"""

    user_name: str = str(input("Hello, what is your name?: "))
    countdown: int = 0

    while True:
        if user_name is False:
            print("Invalid name, please try again.")
            continue
        else:
            break
    
    user_age: int = int(input(f"How old are you, {user_name}?: "))
    
    while True:
        if int(user_age) >= 100:
            break
        else:
            pass

        user_age += 1
        countdown += 1
        
    
    birthdate: date = date.today()
    birthdate.replace(year=lambda key: key = 2022 + countdown)
    message_count: int = int(input("How many times would you like to be reminded?: "))

    for index in range(message_count):
        print(f"\nYou are {birthdate} years away from turning 100!")


if __name__ == "__main__":
    main()