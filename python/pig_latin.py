import re

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
  
  for word in split:
    whole_word_or_phrase = word
    first_letter_of_word = word[0]
    #final = list_holding.join(list_holding)
    #Still looking for regex to check for vowel/would compare upper/lower seperately/[a-zA-Z]?
    #Y is not a real vowel
    if first_letter_of_word in ('a','e','i','o','u'):
      whole_word_or_phrase = f'{whole_word_or_phrase}ay' 
      list_holding.append(whole_word_or_phrase)
    elif first_letter_of_word in ('A','E','I','O','U'):
      whole_word_or_phrase = f'{whole_word_or_phrase}ay'
      list_holding.append(whole_word_or_phrase)
    #If letter is constant
    elif first_letter_of_word not in ('a','e','i','o','u','A','E','I','O','U'):
      constant_hold = whole_word_or_phrase[1:] + whole_word_or_phrase[0]
      whole_word_or_phrase = f'{constant_hold}ay'
      list_holding.append(whole_word_or_phrase)
      
  #Join and return seperated by space
  final = ' '.join(list_holding)
  return print(final)

