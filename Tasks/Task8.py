"""

5 kyu
Greed is Good

Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it, is to score a throw according to these rules. You will always be given an array with five six-sided dice values.

 Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point

A single die can only be counted once in each roll. For example, a given "5" can only count as part of a triplet (contributing to the 500 points) or as a single 50 points, but not both in the same roll.

Example scoring

 Throw       Score
 ---------   ------------------
 5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
 1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
 2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)

In some languages, it is possible to mutate the input to the function. This is something that you should never do. If you mutate the input, you will not be able to pass all the tests.


Жадность - это игра в кости, в которую играют пятью шестигранными кубиками. Ваша миссия, если вы решите ее принять, состоит в том, чтобы выполнить бросок в соответствии с этими правилами. Вам всегда будет предоставлен массив с пятью значениями шестигранных игральных костей.

 Три единицы => 1000 баллов
 Три шестерки => 600 баллов
 Три пятерки => 500 баллов
 Три четверки => 400 баллов
 Три тройки => 300 очков
 Три двойки => 200 баллов
 Один 1 => 100 баллов
 Один 5 => 50 баллов

Один кубик может быть засчитан только один раз за каждый бросок. Например, данная цифра «5» может считаться только частью тройки (составляющей 500 очков) или отдельными 50 очками, но не обеими в одном броске.

Пример подсчета очков

 Бросок
 ---------   ------------------
 5 1 3 4     1250: 50 (для 5) + 2 * 100 (для 1)
 1 1 1 3 1   1100: 1000 (для трех единиц) + 100 (для другой 1)
 2 4 4 5     4450: 400 (для трех четверок) + 50 (для пятерки)

В некоторых языках можно изменить ввод функции. Этого никогда не следует делать. Если вы измените ввод, вы не сможете пройти все тесты.

"""


def score(dice):
    result = 0

    if len(dice) > 5:
        # print("error len > 6")
        return result

    for i in dice:
        if i < 1 or i > 6:
            # print("error value")
            return result

    print("dice first= ", dice)
    new_dice = dice.copy()

    list_dup = [x for x in dice if dice.count(x) >= 3]
    print("list_dup =", list_dup)

    if list_dup:
        if list_dup[0] == 1:
            result = 1000
        if list_dup[0] == 6:
            result = 600
        if list_dup[0] == 5:
            result = 500
        if list_dup[0] == 4:
            result = 400
        if list_dup[0] == 3:
            result = 300
        if list_dup[0] == 2:
            result = 200

        count = 0

        for i in dice:
            if count < 3:
                if i == list_dup[0]:
                    new_dice.remove(i)
                    count += 1
    else:
        result = 0

    print("new_dice = ", new_dice)

    for i in new_dice:
        if i == 1:
            result = result + 100
        if i == 5:
            result = result + 50

    print(result)

    return result


if __name__ == '__main__':
    # assert score([2, 3, 4, 6, 2]) == 0
    # assert score([4, 4, 4, 3, 3]) == 400
    # assert score([2, 4, 4, 5, 4]) == 450
    # assert score([5, 1, 3, 4, 1]) == 250
    assert score([1, 1, 1, 3, 1]) == 1100
    # assert score([2, 4, 4, 5, 4]) == 450
    # assert score([5, 5, 2, 5, 2]) == 500
