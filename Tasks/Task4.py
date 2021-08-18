"""
Vasya - Clerk

Только что вышел новый фильм «Мстители»! В кассах кинотеатра много людей, стоящих в огромную очередь.
У каждого из них есть единственная банкнота в 100, 50 или 25 долларов. Билет на «Мстителей» стоит 25 долларов.

Вася сейчас работает клерком. Он хочет продать билет каждому человеку в этой очереди.

Может ли Вася продать билет каждому и отдать сдачу, если у него изначально нет денег и он продает билеты
 строго в порядке очереди?

Верните ДА, если Вася может продать билет каждому человеку и отдать сдачу с имеющимися у него в данный
момент счетами. В противном случае верните NO.
"""


def tickets(people):
    money_Vasya = 0

    rub_25 = 0
    rub_50 = 0
    rub_100 = 0

    for i in people:
        if i == 25:
            rub_25 = rub_25 + i
            money_Vasya = money_Vasya + i
            continue
        if i == 50:
            rub_50 = rub_50 + i
            if money_Vasya >= i:
                money_Vasya = money_Vasya - (i - 25)
                money_Vasya = money_Vasya + i
                rub_25 = rub_25 - 25
                if rub_25 < 0:
                    return "NO"
        if i == 100:
            rub_100 = rub_100 + i
            if money_Vasya >= i:
                money_Vasya = money_Vasya - (i - 25)
                money_Vasya = money_Vasya + i
                rub_25 = rub_25 - 25
                if rub_25 < 0:
                    return "NO"
        else:
                return "NO"
    return "YES"

if __name__ == '__main__':
    assert tickets ( [25, 25, 50] ) == "YES"
    # assert tickets ( [25, 100] ) == "NO"
    # assert tickets ( [25, 25, 50, 50, 100] ) == "NO"
    # assert tickets ( [25, 25, 25, 25, 50, 100, 50] ) == "YES"
    # assert tickets ( [25, 25, 25, 25, 25, 25, 25, 50, 50, 50, 100, 100, 100, 100] ) == "NO"


