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
    # print('lines =', lines)

    tt = []
    tt1 = []
    my_str1 = ''

    if not markers:
        return string

    if not string:
        return string

    for x in markers:

        print('x = ', x)

        if not x:
            return string

        for i in range(len(lines)):
            print('lines', lines)

            if lines[i].find(x) != -1:
                lines[i] = lines[i][:lines[i].find(x)]

                print('lines.find = ', lines)



            if len(lines[i]) > 1:


                if lines[i][-1] == ' ' :
                    lines[i] = lines[i][0:len(lines[i]) - 1]
                    print('lines[i]cut = ', lines[i])

                if lines[i].isspace():
                    lines[i] = ''


        print('lines.end', lines)
    return '\n'.join(lines)


if __name__ == '__main__':
    # assert strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']) == \
    #        'apples, pears\ngrapes\nbananas'
    # assert strip_comments('apples, pears # and bananas\ngrapes\navocado @apples',['@', '!']) == \
    #        'apples, pears # and bananas\ngrapes\navocado'

    assert strip_comments('a #b\nc\nd $e f g', ['#', '$']) == 'a\nc\nd'
    assert strip_comments(' a #b\nc\nd $e f g', ['#', '$']) == ' a\nc\nd'

    # assert strip_comments('#', ['#', '!']) == ''
    # assert strip_comments('§', ['#', '§']) == '\n'
    # assert strip_comments('apples, pears  # and bananas\ngrapes\nbananas !apples', []) == \
    #        'apples, pears  # and bananas\ngrapes\nbananas !apples'
    # assert strip_comments('\t,\ncherries pears apples strawberries apples\n? cherries ! bananas', [',', '=', '#', '@', '?', '-', '.']) == '\ncherries pears apples strawberries apples\n'
    assert strip_comments("  ^ oranges\n, # ^ ^\npears strawberries '", ['@', '?', '-', '.', "'", '#', '!', '^']) == \
           '\n,\npears strawberries'