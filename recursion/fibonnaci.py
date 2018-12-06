def fibonnaci(number):
    if number < 2:
        return number
    return number + fibonnaci(number - 1)


if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(1001)
    print(fibonnaci(999))
