'''Asynchronous code example'''
from asyncio import sleep, run, create_task


async def main():
    '''Primary function of program'''
    secondary_task = create_task(secondary())
    teritary_task = create_task(teritary())
    print('Hello friends')
    await sleep(2)
    print('My friends please.')
    print('I can talk while we are waiting.')
    await secondary_task
    await teritary_task


async def secondary():
    '''Secondary function of program'''
    print('My name is Karl.')
    await sleep(4)
    print('Can you help me with my homework?')


async def teritary():
    '''Auxillary function of the program'''
    print('How are you doing today?')
    await sleep(6)
    print('I have trouble keeping up with it.')


if __name__ == "__main__":
    run(main())
