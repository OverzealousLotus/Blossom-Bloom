"""Caching tips on improving performance in Python."""
from functools import cache, lru_cache
from timeit import timeit

__all__ = ["fibonacci_cache", "fibonacci_lru", "main"]
__version__ = "0.1"
__author__ = "Overzealous Lotus"


# Caching allows us to remember previous operations, which are stored in a datatable-
# -later fetched by our program again to be reused to solve another problem. Here, we use it-
# -to ease the load on calculating Fibonnaci numbers. However, default caching can take a lot-
# -of memory.
@cache
def fibonacci_cache(november: int) -> int:
    """Cached Fibonnaci Sequence."""
    if november <= 1:
        return november
    return fibonacci_cache(november - 1) + fibonacci_cache(november - 2)


# To solve this problem, we can instead use lru_caching. Here, we can limit the amount-
# -of solutions stored in memory, thus easing our memory load, while still profiting from-
# -caching."""
@lru_cache(maxsize=5)
def fibonacci_lru(november: int) -> int:
    """Basic Fibonacci Sequence."""
    if november <= 1:
        return november
    return fibonacci_lru(november - 1) + fibonacci_lru(november - 2)


def main() -> None:
    """Primary executor of our program."""
    for index in range(100):
        print("Non-LRU: ", index, fibonacci_lru(index))

    for index in range(100):
        print("With-LRU: ", index, fibonacci_cache(index))
    print("Done.")


if __name__ == "__main__":
    timeit("main()")
