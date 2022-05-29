def define_suit(card):
    if len(card) == 2:
        # print('len(i) = ', len(card))

        if card[1:] == 'C':
            # print('clubs')
            return 'clubs'

        elif card[1:] == 'S':
            # print('spades')
            return 'spades'

        elif card[1:] == 'D':
            # print('diamonds')
            return 'diamonds'

        elif card[1:] == 'H':
            # print('hearts')
            return 'hearts'

    elif len(card) == 3:
        # print('len(i) = ', len(card))

        if card[2:] == 'C':
            return 'clubs'

        elif card[2:] == 'S':
            return 'spades'

        elif card[2:] == 'D':
            return 'diamonds'

        elif card[2:] == 'H':
            return 'hearts'


if __name__ == '__main__':
    assert define_suit('3C') == 'clubs'
    assert define_suit('QS') == 'spades'
    assert define_suit('9D') == 'diamonds'
    assert define_suit('JH') == 'hearts'
