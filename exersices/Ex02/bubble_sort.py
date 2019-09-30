def bubble_sort(data):
    data = list(data)
    length = len(data)
    while length >= 1:
        loop(data)
        length -= 1
    return tuple(data)


def loop(data):
    for k in range(len(data) - 1):
        if data[k] > data[k+1]:
            data[k], data[k + 1] = data[k+1], data[k]
    return data


if __name__ == "__main__":

    for data in ((),
                 (1,),
                 (1, 3, 8, 12),
                 (12, 8, 3, 1),
                 (8, 3, 12, 1)):
        print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))
