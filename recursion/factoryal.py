def factoryal(number):
    if number < 2:
        return 1
    return number * factoryal(number - 1)


if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(1001)
    print(factoryal(10))
