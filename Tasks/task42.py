def snail(column, day, night):
    count = 0
    res = 0

    while res < column:

        res = res + day

        if res >= column:
            print(count+1)
            return count+1

        else:
            res = res - night
        count += 1

    return count


if __name__ == '__main__':
    # assert snail(3, 2, 1) == 2
    # assert snail(10, 3, 1) == 5
    # assert snail(10, 3, 2) == 8
    # assert snail(100, 20, 5) == 7
    assert snail(5, 10, 3) == 1
