from typing import Callable

def suite(head: int, repetition: int, increment: Callable, sink = []):
    if head > repetition: return sink
    sink.append(increment(head))
    return suite(head + 1, repetition, increment, sink)

if __name__ == "__main__":
    print(suite(0, 3, lambda x: x * 90))