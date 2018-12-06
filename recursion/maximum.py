def maximum(array):
    head, *tail = array
    max_tail = head if tail == [] else maximum(tail)
    return head if head > max_tail else max_tail


if __name__ == '__main__':
    print(maximum([63, 5, 1, 9, 28, 4, 58, 9]))
