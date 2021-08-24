"""
Simple Pig Latin

Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples

pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !

Переместите первую букву каждого слова в его конец, затем добавьте «ау» в конец слова. Не трогайте знаки препинания.

"""


def pig_it(text):
    text_new = text[::]
    text_new = text_new.rsplit()
    list_letter = []
    new_word = []
    my_str = ""

    for word in text_new:
        list_letter.clear()

        for letter in word:
            list_letter.append(letter)

        e1 = list_letter[0]
        list_letter.pop(0)
        list_letter.append(e1)
        if letter.isalpha():
            list_letter.append("ay")

        my_str = ''.join(list_letter)
        new_word.append(my_str)

        my_str = ' '.join(new_word)
    return my_str


if __name__ == '__main__':
    assert pig_it("Pig latin is cool") == "igPay atinlay siay oolcay"
    assert pig_it("This is my string") == "hisTay siay ymay tringsay"
    assert pig_it("Hello world !") == "elloHay orldway !"
