import re
import string


def is_pangram(s):
    my_set = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
    my_list = []
    my_str = ''

    for i in my_set:
        ss = s.lower().count(i)
        print(i,my_str)
        if ss > 0:
            my_list.append(ss)

    print(s)
    print(my_set)
    print(len(my_set))
    print(my_list)
    print(len(my_list))

    if len(my_list) < 26:
        return False
    else:
        return True


if __name__ == '__main__':
    # assert is_pangram("The quick, brown fox jumps over the lazy dog!") == True
    assert is_pangram("This isn't a pangram!") == False