def translate(word_or_phrase):
  return_phrase = ''
  vowel_list = ['a', 'e', 'i', 'o', 'u']
  word_list = word_or_phrase.split(' ')
  for word in word_list:
    for letter in word:
      return_phrase += ' '
      if letter in vowel_list:
        if word.index(letter) == 0:
          return_phrase += word
          return_phrase += 'ay'
          break
        else:
          return_phrase += word[(word.index(letter))::]
          return_phrase += word[:(word.index(letter))]
          return_phrase += 'ay'
          break
  print(return_phrase.strip())



translate('Zach Attack')



