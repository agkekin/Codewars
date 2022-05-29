def prescribe(d, a, b):
    res_a = 0
    res_b = 0
    res_ab = 0
    res_aba = 0
    res_bab = 0
    res = []

    while res_a + a <= d:
        res_a += a
    print('res_a', res_a)
    res.append(res_a)

    while res_b + b <= d:
        res_b += b
    print('res_b', res_b)
    res.append(res_b)

    while res_ab + a + b <= d:
        res_ab += a + b
    print('res_ab', res_ab)
    res.append(res_ab)

    while res_aba + res_a + b <= d:
        res_aba += res_a + b
    print('res_aba', res_aba)
    res.append(res_aba)

    while res_bab + res_b + a <= d:
        res_bab += res_b + a
    print('res_bab', res_bab)
    res.append(res_bab)

    print('res', res)

    print(max(res))
    return max(res)


if __name__ == '__main__':
    # assert prescribe(99, 25, 60) == 85
    # assert prescribe(180, 25, 60) == 180
    # assert prescribe(2575, 400, 150) == 2550
    # assert prescribe(4540, 9, 15) == 4539
    assert prescribe(5424, 83, 98) == 5424
