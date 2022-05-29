def make_negative(number):
    if number == 0:
        return 0
    elif number > 0:
        return number * (-1)
    else:
        return number


if __name__ == '__main__':
    assert make_negative(42) == -42
