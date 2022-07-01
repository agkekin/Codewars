def strip_comments(strng, markers):
    print(strng)
    for i in strng:
        if i == "#":
            if i == "\"
                mlist.append(i)
    pass

if __name__ == '__main__':
    assert strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']) == \
           'apples, pears\ngrapes\nbananas'

