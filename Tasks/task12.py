def to_freud(sentence):
    res = sentence.split(' ')
    print('res =', res)
    res1 = []

    sentence1 = sentence.count('sex')
    if sentence == '':
        ss = ''
        return ss

    elif sentence1 > 0:
        for i in range(0, sentence1):
            res1.append('sex')
        print(' '.join(res1))
        return ' '.join(res1)

    else:
        for i in res:
            res1.append('sex')
        print(' '.join(res1))
        return ' '.join(res1)


if __name__ == '__main__':

    assert to_freud('test') == 'sex'
    assert to_freud('sexy sex') == 'sex sex'
    assert to_freud('This is a test') == 'sex sex sex sex'
    assert to_freud('This is a longer test') == 'sex sex sex sex sex'
    assert to_freud('Youre becoming a true freudian expert') == 'sex sex sex sex sex sex'
    assert to_freud('sexsexsexsex') == 'sex sex sex sex'
    assert to_freud('sexsexsexsexsex') == 'sex sex sex sex sex'
    assert to_freud('sexsexsexsexsexsex') == 'sex sex sex sex sex sex'

