def recurs(a, b):
    my_str = ''
    tt = []

    for i in a:
        for j in i:
            if j != b:
                my_str += j
            else:
                break

        if len(my_str) > 1:
            if my_str[-1] == ' ':
                tt.append(my_str[0:len(my_str)-1])
            else:
                tt.append(my_str)

        else:
            tt.append(my_str)

        my_str = ''

    return tt

def strip_comments(string, markers):

    lines = string.splitlines()
    print('lines =', lines)

    tt = []
    tt1 = []
    my_str = ''

    if not markers:
        return string

    for x in markers:
        print(x)
        print(recurs(recurs(lines, x),x))

        ss = '\n'.join(recurs(lines, x))
    print('ss =', ss)

    return ss


if __name__ == '__main__':
    assert strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']) == \
           'apples, pears\ngrapes\nbananas'
    # assert strip_comments('apples, pears # and bananas\ngrapes\navocado @apples',['@', '!']) == \
    #        'apples, pears # and bananas\ngrapes\navocado'

    # assert strip_comments('#', ['#', '!']) == ' '
    # assert strip_comments('§', ['#', '§']) == '\n'
    # assert strip_comments('apples, pears  # and bananas\ngrapes\nbananas !apples', []) == \
    #        'apples, pears  # and bananas\ngrapes\nbananas !apples'
