# # Premise
# Pig Latin is a made-up children's language that's intended to be confusing. It obeys a few simple rules (below) but when it's spoken quickly it's really difficult for non-children (and non-native speakers) to understand.

# Rule 1: If a word begins with a vowel sound, add an "ay" sound to the end of the word.

# Rule 2: If a word begins with a consonant sound, move it to the end of the word, and then add an "ay" sound to the end of the word.

# (There are a few more rules for edge cases, and there are regional variants too, but that should be enough to understand the tests.)

# See <http://en.wikipedia.org/wiki/Pig_latin> for more details.


def translate(word_or_phrase):

  #  if phrase split up into multiple words
  split_words = word_or_phrase.split(' ')
  # print(split_words)
  # make vowel array, if string starts with vowel then return str with 'ay' appended
  vowels = ['a','e','i','o','u']
  result = ''
  for word in split_words:
    if word[0] in vowels:
      result+= (word + 'ay' + ' ')
    else:
      for index, l in enumerate(word):
        if l in vowels:
          to_be_moved_letters = word[:index]
          result += (word[index:] + to_be_moved_letters + 'ay')
          break
          
  return result.strip()


print(translate('eat pie'))