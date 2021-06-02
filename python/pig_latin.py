# Input is a regular english word or phrase
# Separate input into an list of individual words
# the individual words include punctuation
# pass individual words to function pig latin to
# convert
# output is a combined string of pig latin words
def translate(word_or_phrase):
  word_list = word_or_phrase.split(" ")
  output_list = []

  for elem in word_list:
    output_list.append(pig_latin(elem))
    
  return " ".join(output_list)



# Input is a regular english word
# create a variable converted_word to store result
# if the word starts with vowel, add -ay to word
# and save to converted_word
# if the word starts with a consonant, move all consonants
# up to the first vowel to end end and save to converted_word
# add -ay to the end of converted_word
# return converted_word


def pig_latin(word):

  vowel = ['a', 'e', 'i', 'o', 'u']
  converted_word = ""

  if (word[0].lower() in vowel):
      converted_word = word + "ay"
  
  else:
    word_array = list(word)
    first_letter_cap = False

    if (not word_array[0].islower()):
      first_letter_cap = True
      word_array[0] = word_array[0].lower()

    while (not word_array[0].lower() in vowel):
      new_end_ch = word_array.pop(0)
      word_array.append(new_end_ch)
    
    
    converted_word = "".join(word_array) + "ay"
    
    if (first_letter_cap):
      converted_word = converted_word.capitalize()

  return converted_word


print(translate("School"))