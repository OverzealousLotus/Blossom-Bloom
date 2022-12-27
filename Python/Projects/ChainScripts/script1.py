'''Our first script in the chain'''

from time import sleep
from os import system
from random import randint

NUMERAL = 0

print('Script one started.')
try:
    while NUMERAL <= 5:
        sleep(randint(1, 3))
        NUMERAL += 1
        print(f'{NUMERAL} incremented by one.')
        print(NUMERAL)
    system('python ~/Coding/Python/Projects/ChainScripts/script2.py')
except RuntimeError:
    print("An error has occurred.")
