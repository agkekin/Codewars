def strip_comments(strng, markers):
    # print(strng)
    ll = ''
    mlist = []
    mstr = ''
    # mstr = strng[strng.find(markers[0]):strng.find(markers[1])]
    # strng = strng.replace(mstr,'')
    # print(strng)
    k = 0

    for i in strng:
        k += 1
        if i != markers[0]:
            mstr += i
        else:
            break
    # print(mstr)
    print(strng[k::])

    for i in strng[k::]:
        if i == "\\":
            mstr += i

    print(mstr)

    return strng

if __name__ == '__main__':
    assert strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']) == \
           'apples, pears\ngrapes\nbananas'

