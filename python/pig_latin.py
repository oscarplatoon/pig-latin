def translate(word_or_phrase):

    if len(word_or_phrase.split()) == 1:
        return translate_word(word_or_phrase)
    elif len(word_or_phrase.split()) > 1:
        answer = []
        for x in word_or_phrase:
            answer.append(translate_word(x))
        return " ".join(str(answer))


def translate_word(word_or_phrase):
    key = ['a','e','i','o','u','y']
    hold = [char for char in word_or_phrase]
    for x in range(len(word_or_phrase)):
        if hold[0] in key:
            return(''.join(hold) + 'ay')
        else:
            hold.append((hold.pop(0)))
    print('no vowels found')