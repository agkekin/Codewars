def bin_to_decimal(inp):
    return int(inp, 2)




if __name__ == '__main__':
    assert bin_to_decimal ("0") == 0
    assert bin_to_decimal ("1") == 1
    assert bin_to_decimal ("10") == 2
    assert bin_to_decimal ("11") == 3
    assert bin_to_decimal ("101010") == 42
    assert bin_to_decimal ("1001001") == 73


