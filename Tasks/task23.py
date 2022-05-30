def how_much_i_love_you(nb_petals):
    my_str = ['I love you', 'a little', 'a lot', 'passionately', 'madly', 'not at all']
    res = nb_petals % len ( my_str )
    res1 = nb_petals // len ( my_str )
    print (res)
    print (res1)
    print ('\n')
    return my_str [ res -1 ]


if __name__ == '__main__':
    assert how_much_i_love_you ( 1 ) == "I love you"
    assert how_much_i_love_you ( 2 ) == "a little"
    assert how_much_i_love_you ( 3 ) == "a lot"
    assert how_much_i_love_you ( 4 ) == "passionately"
    assert how_much_i_love_you ( 5 ) == "madly"
    assert how_much_i_love_you ( 6 ) == "not at all"
    assert how_much_i_love_you ( 7 ) == "I love you"
    assert how_much_i_love_you ( 8 ) == "a little"
    assert how_much_i_love_you ( 9 ) == "a lot"
