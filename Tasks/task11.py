'''
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

    It must start with a hashtag (#).
    All words must have their first letter capitalized.
    If the final result is longer than 140 chars it must return false.
    If the input or the result is an empty string it must return false.

'''


def generate_hashtag(s):
    # your code here
    new = s.split(' ')

    print('s =', s)
    print('new =', new)
    print('len(new) = ', len(new))
    print('len(s) = ', len(s))

    if len(s) > 139 or not s:
        return False
    else:
        s1 = '#' + s.title()
        s1 = s1.replace(' ','')
        print('s.title =', s1)
        return s1



print(generate_hashtag)

if __name__ == '__main__':
    #assert generate_hashtag('Basic tests') == '#BasicTest'
    #assert generate_hashtag('') == False
    assert generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat') == False

