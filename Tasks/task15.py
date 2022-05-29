def how_much_water(water, load, clothes):
    result = 0

    if clothes > load * 2:
        return 'Too much clothes'
    elif clothes < load:
        return 'Not enough clothes'
    else:
        result = round(water * 1.1 ** (clothes - load), 2)
        return result


if __name__ == '__main__':
    assert how_much_water(10, 10, 21) == 'Too much clothes'
    assert how_much_water(10, 10, 2) == 'Not enough clothes'
    assert how_much_water(10, 11, 20) == 23.58
    assert how_much_water(50, 15, 29) == 189.87

    '''
    test.assert_equals(how_much_water(10,10,21), 'Too much clothes', '')
test.assert_equals(how_much_water(10,10,2), 'Not enough clothes','')
test.assert_equals(how_much_water(10,11,20), 23.58, '')
test.assert_equals(how_much_water(50,15,29), 189.87, '')
'''
