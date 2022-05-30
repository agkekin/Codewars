def how_much_i_love_you(7):
    my_str = ['I love you', 'a little', 'a lot', 'passionately', 'madly', 'not at all']
    num = nb_petals / 6

    while num > 6:
        num = nb_petals / 6

    print(my_str[num-1])
    return my_str[num-1]


if __name__ == '__main__':
    assert how_much_i_love_you(7) == "I love you"
    assert how_much_i_love_you(3) == "a lot"
    assert how_much_i_love_you(6) == "not at all"
    #assert how_much_i_love_you(200) == "I love you"

