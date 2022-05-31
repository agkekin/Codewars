def hex_string_to_RGB(hex_string):
    my_string = hex_string.replace('#', '')
    r = int(my_string[0:2], 16)
    g = int(my_string[2:4], 16)
    b = int(my_string[4:6], 16)
    res = {'r': r, 'g': g, 'b': b}
    return res


if __name__ == '__main__':
    assert hex_string_to_RGB("#FF9933") == {'r': 255, 'g': 153, 'b': 51}
    assert hex_string_to_RGB("#beaded") == {'r': 190, 'g': 173, 'b': 237}
    assert hex_string_to_RGB("#000000") == {'r': 0, 'g': 0, 'b': 0}
    assert hex_string_to_RGB("#111111") == {'r': 17, 'g': 17, 'b': 17}
    assert hex_string_to_RGB("#Fa3456") == {'r': 250, 'g': 52, 'b': 86}
