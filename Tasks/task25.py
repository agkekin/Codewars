def hotpo(n):
    res =0

    if n == 1:
        return 0

    while n != 1:
        res += 1

        if n % 2 == 0:
            n = n / 2
        else:
            n = 3*n + 1

    print(res)
    return res


if __name__ == '__main__':
    assert hotpo(1) == 0
    assert hotpo(5) == 5
    assert hotpo(6) == 8
    assert hotpo(23) == 15
