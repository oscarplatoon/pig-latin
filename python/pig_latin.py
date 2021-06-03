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
# up to the first vowel to end and save to converted_word
# add -ay to the end of converted_word
# return converted_word


def pig_latin(word):

  vowel = ['a', 'e', 'i', 'o', 'u']
  punctuation = [".", "!", ",", "?"]
  converted_word = ""
  word_array = list(word)
  first_letter_cap = False
  last_letter_punc = False
  punc = ""

  # case where word starts with a vowel
  if (word[0].lower() in vowel):
      converted_word = word + "ay"
  
  #case where word starts with a consonant sound
  else:

    # check if first letter is capitalized
    if (not word_array[0].islower()):
      first_letter_cap = True
      word_array[0] = word_array[0].lower()

    # check if last letter is punctuation
    if (word_array[-1] in punctuation):
      last_letter_punc = True
      punc = word_array.pop()

    # move all consonants at the beginning of the
    # word to the end, stop when a vowel is found
    while (not word_array[0].lower() in vowel):
      #edge case where to treat qu as a single consonant sound
      #moves 1 additional character to end of word array
      if word_array[0].lower() == 'q':
        new_end_ch = word_array.pop(0)
        word_array.append(new_end_ch)
    
      new_end_ch = word_array.pop(0)
      word_array.append(new_end_ch)
      
    # store word array as a string with ay at the end
    converted_word = "".join(word_array) + "ay"
    
    # if the original word's first letter was capitalized,
    # capitalize the first letter of the output string
    if (first_letter_cap):
      converted_word = converted_word.capitalize()
    
    # if the original word ended in punctuation
    # add the punctuation to the end of the string
    if (last_letter_punc):
      converted_word = converted_word + punc

  return converted_word
