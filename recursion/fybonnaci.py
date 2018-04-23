def fybonnaci(number):
    if number < 2:
        return number
    return number + fybonnaci(number - 1)


if __name__ == '__main__':
    print(fybonnaci(9))
