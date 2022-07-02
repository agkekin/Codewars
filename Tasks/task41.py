# def recurs(a, b):
#     my_str = ''
#     tt = []
#
#     for i in a:
#         for j in i:
#             if j != b:
#                 my_str += j
#             else:
#                 break
#
#         if len(my_str) > 1:
#             if my_str[-1] == ' ':
#                 tt.append(my_str[0:len(my_str)-1])
#             else:
#                 tt.append(my_str)
#
#         else:
#             tt.append(my_str)
#
#         my_str = ''
#
#     return tt

def strip_comments(string, markers):

    lines = string.splitlines()
    print('lines =', lines)

    tt = []
    tt1 = []
    my_str1 = ''

    if not markers:
        return string

    if not string:
        return string

    for x in markers:
        print('\n')

        print('x = ', x)

        for i in lines:
            print('*************************************')
            print('i = ', i)

            if i.find(x) > 0:
                print('1')
                i = i[:i.find(x)]
            print('my_str = ', i)

            if i[-1] == ' ':
                i = i[0:len(i) - 1]

            tt.append(i)
            print('tt =', tt)

    pass


if __name__ == '__main__':
    assert strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']) == \
           'apples, pears\ngrapes\nbananas'
    # assert strip_comments('apples, pears # and bananas\ngrapes\navocado @apples',['@', '!']) == \
    #        'apples, pears # and bananas\ngrapes\navocado'

    # assert strip_comments('#', ['#', '!']) == ' '
    # assert strip_comments('§', ['#', '§']) == '\n'
    # assert strip_comments('apples, pears  # and bananas\ngrapes\nbananas !apples', []) == \
    #        'apples, pears  # and bananas\ngrapes\nbananas !apples'
