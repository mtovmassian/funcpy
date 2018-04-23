def replycate(rep, element):
    if rep <= 0:
        return []
    res = replycate(rep - 1, element)
    res.append(element)
    return res


if __name__ == '__main__':
    print(replycate(3, "toto"))
