def translate(word_or_phrase):
  #split by word into array
  #iterate through word/phrase
  #check if first word is constant
  #ignore space
  #place constant at end, then add ay to end
  #vowel just add ay at end
  #return string

  split = list(word_or_phrase.split(' '))
  #pushing list items in array
  list_holding = []
  #from list_holding convert back to string
  final = ''
  for word in split:
    word = word[0]

    #Still looking for regex to check for vowel/would compare upper/lower seperately
    #Y is not a real vowel
    if word in ('a','e','i','o','u'):
      word = f'{word}ay' 
      list_holding += word 
    elif word in ('A','E','I','O','U'):
      word = f'{word}ay'
      list_holding += word 
  return print(list_holding)

translate('test a test O A')