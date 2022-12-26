'Second Script'

from time import sleep
from random import choice

COLOR = 'Placeholder'

print('Script two started.')

try:
    while COLOR != 'Green':
        sleep(2)
        COLOR = choice(['Blue', 'Red', 'Orange', 'Yellow', 'Green'])
        print(f'My favorite color is now {COLOR}')
except RuntimeError:
    raise Warning('An unknown error has occurred.')
