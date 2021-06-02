def translate(word_or_phrase):
  vowels = ['a', 'e', 'i', 'o', 'u', 'y']
  phrase = word_or_phrase
  if word_or_phrase[0] in vowels:
    phrase = word_or_phrase + 'ay'

    return phrase
  else:
    phrase_list = []
    phrase_list[:] = phrase
    phrase_list.append(phrase[0])
    phrase_list.pop(0)
    phrase_list.append('ay')

    return ''.join(phrase_list)

