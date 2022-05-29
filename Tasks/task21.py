def prescribe(d, a, b):
    res = 0

    for a_pills in range(d // a + 1):
        print('a_pills = ', a_pills)

        for b_pills in range(d // b + 1):
            print('b_pills = ', b_pills)

            dose = a_pills * a + b_pills * b
            print('dose =', dose)

            if dose <= d:
                res = max(res, dose)
                print('res =', res)

        print("\n")

    return res


if __name__ == '__main__':
    assert prescribe(99, 25, 60) == 85
    # assert prescribe(180, 25, 60) == 180
    # assert prescribe(2575, 400, 150) == 2550
    # assert prescribe(4540, 9, 15) == 4539
    #assert prescribe(5424, 83, 98) == 5424
