"""
    Напишите функцию, которая принимает строку из одного или нескольких слов и возвращает ту же строку,
    но с перевернутыми словами из пяти или более букв (например, имя этого ката).

    Переданные строки будут состоять только из букв и пробелов.
    Пробелы будут добавлены только в том случае, если присутствует более одного слова.

"""


def spin_words(sentence):

    sentence_new = sentence.rsplit()
    my_list = []
    my_str = ""

    for i in sentence_new:
        if len(i) >= 5:
            my_list.append(i[::-1])
        else:
            my_list.append(i)

        if len(my_list) > 1:
            my_str = (" ".join(my_list))
        else:
            my_str = ("".join(my_list))
    # print(my_str)
    return my_str


if __name__ == '__main__':
    assert spin_words("Welcome") == "emocleW"
    assert spin_words("Hey fellow warriors") == "Hey wollef sroirraw"
    assert spin_words("This is a test") == "This is a test"
    assert spin_words("This is another") == "This is rehtona test"

