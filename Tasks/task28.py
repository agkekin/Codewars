def distance_between_points(a, b):
    x = (b[0] - a[0]) ** 2
    print(x)
    y = (b[1] - a[1]) ** 2
    print(y)
    res = sqrt(x + y)
    print('res', res)
    s = str(res).split('.')
    print(s)

    if s[1] == '0':
        res1 = int(s[0])
        print(res1)
        return res1
    else:

        res = round(res, 6)
        print(res)
        return res


if __name__ == '__main__':
    # assert distance_between_points((3, 3), (3, 3)) == 0
    assert distance_between_points((1, 6), (4, 2)) == 5
    # assert distance_between_points((-10.2, 12.5), (0.3, 14.7)) == 10.728001
