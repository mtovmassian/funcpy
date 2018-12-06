def replicate(rep, element):
    if rep <= 0:
        return []
    res = replicate(rep - 1, element)
    res.append(element)
    return res


if __name__ == '__main__':
    print(replicate(3, "toto"))
