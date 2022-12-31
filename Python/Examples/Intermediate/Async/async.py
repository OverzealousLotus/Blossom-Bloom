"""Asynchronous code example."""
from asyncio import create_task, run, sleep
from typing import Any

__all__ = ["main", "secondary", "teritary"]
__version__ = "0.1"
__author__ = "Overzealous Lotus"
__license__ = "GPL-3.0"


# Syncronous Programming is the concept of moving from line-to-line in order.
# Asyncronous Programming is jumping to different lines during certain tasks.
# This can be useful during web development. We can do other tasks while waiting-
# -for another process to complete. 
async def main() -> None:
    """Primary function of program."""
    first_task: Any = create_task(secondary())  # Create first task
    second_task: Any = create_task(teritary())  # Create second task
    print("Hello friends")
    await sleep(2)  # During sleep, we jump to secondary()
    print("My friends please.")
    print("I can talk while we are waiting.")
    await first_task  # We Await our first task
    await second_task  # Then we Await our second task.


async def secondary() -> None:
    """Secondary function of program."""
    print("My name is Karl.")
    await sleep(4)  # During sleep, we jump to teritary()
    print("Can you help me with my homework?")


async def teritary() -> None:
    """Auxillary function of the program."""
    print("How are you doing today?")
    await sleep(6)  # During sleep, we jump back to main()
    print("I have trouble keeping up with it.")


if __name__ == "__main__":
    run(main())
