def slice(start, end, array):
    def _slice(start, end, array):
        end -= 1
        if end < start:
            return []
        res = _slice(start, end, array)
        res.append(array[end])
        return res

    if end < 0:
        end += len(array)
    elif start < 0:
        end = len(array)
        start += end
    elif start >= 0 and end == 0:
        end = len(array)
    return _slice(start, end, array)


if __name__ == '__main__':
    array = ['a', 'b', 'c', 'd', 'e', 'f']
    print(slice(0, 2, array))
    print(slice(2, 4, array))
    print(slice(-2, 0, array))
