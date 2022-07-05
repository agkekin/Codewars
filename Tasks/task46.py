def warn_the_sheep(queue):

    num = 0

    for i, j in reversed(list(enumerate(queue))):
        if j == 'wolf':
            num = (len(queue) - i - 1)
    a = ''
    if num == 0:
        a = 'Pls go away and stop eating my sheep'

    else:
        a = f'Oi! Sheep number {num}! You are about to be eaten by a wolf!'

    return a


if __name__ == '__main__':
    # assert warn_the_sheep(['sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'wolf', 'sheep', 'sheep']) ==\
    #        'Oi! Sheep number 2! You are about to be eaten by a wolf!'
    # assert warn_the_sheep(['sheep', 'wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep']) == \
    #        'Oi! Sheep number 5! You are about to be eaten by a wolf!'
    # assert warn_the_sheep(['wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep']) == \
    #            'Oi! Sheep number 6! You are about to be eaten by a wolf!'
    # assert warn_the_sheep(['sheep', 'wolf', 'sheep']) == 'Oi! Sheep number 1! You are about to be eaten by a wolf!'
    assert warn_the_sheep(['sheep', 'sheep', 'wolf']) == 'Pls go away and stop eating my sheep'
