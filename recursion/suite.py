from typing import Callable

def suite(head: int, repetition: int, increment: Callable):
    if head > repetition: return []
    return [
        increment(head),
        *suite(head + 1, repetition, increment)
    ]

if __name__ == "__main__":
    print(suite(0, 3, lambda x: x * 90))
