def translate(word_or_phrase):
  return_word = ''
  vowel_list = ['a', 'e', 'i', 'o', 'u']
  for letter in word_or_phrase:
    if letter in vowel_list:
      return_word += word_or_phrase[(word_or_phrase.index(letter))::]
      return_word += word_or_phrase[:(word_or_phrase.index(letter))]
      return_word += 'ay'
      print(return_word)



translate('zach')



