from math import sqrt


def square_or_square_root(arr):
    res = []

    for i in arr:
        if sqrt(i).is_integer():
            res.append(int(sqrt(i)))
        else:
            res.append(i ** 2)

    print(res)
    return res


if __name__ == '__main__':
    assert square_or_square_root([4, 3, 9, 7, 2, 1]) == [2, 9, 3, 49, 4, 1]
