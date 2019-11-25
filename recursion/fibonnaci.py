def fibonnaci(number):
    if number <= 1:
        return 1
    return fibonnaci(number - 2) + fibonnaci(number - 1)


if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(1001)
    print(fibonnaci(999))
