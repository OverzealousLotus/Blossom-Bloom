'''Short games made to practice Python. To test, comment out all but one'''

from random import randint

USER_CHOICE = None
MY_CHOICE = 79

while USER_CHOICE != MY_CHOICE:
    if USER_CHOICE == MY_CHOICE:
        print('Congratulations, you won... For now.')
        break
    myChoice = randint(1, 3)

    print(MY_CHOICE)
