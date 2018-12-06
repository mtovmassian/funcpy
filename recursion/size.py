def size(array):
    def _size(counter):
        try:
            array[counter]
            return _size(counter + 1)
        except IndexError:
            return counter
    return _size(0)


if __name__ == '__main__':
    print(size("martin"))
