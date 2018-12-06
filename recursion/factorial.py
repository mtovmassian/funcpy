def factorial(number):
    if number < 2:
        return 1
    return number * factorial(number - 1)


if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(1001)
    print(factorial(10))
