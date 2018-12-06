def quicksort(array):

    def _sub_quicksort(sublists, array, pivot):
        if array == []:
            return sublists
        head, *tail = array
        if head < pivot:
            sublists[0].append(head)
        elif head == pivot:
            sublists[1].append(head)
        else:
            sublists[2].append(head)
        return _sub_quicksort(sublists, tail, pivot)

    if len(array) > 1:
        sublists = [[], [], []]
        pivot = array[len(array) - 1]
        left, center, right = _sub_quicksort(sublists, array, pivot)
        return quicksort(left) + center + quicksort(right)
    return array


if __name__ == '__main__':
    print(quicksort([10, -1, -5, 158, 12, 3]))
