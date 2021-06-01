def translate(str):

# Rule 1: If a word begins with a vowel sound, add an "ay" sound to the end of the word.

# Rule 2: If a word begins with a consonant sound, move it to the end of the word, and then add an "ay" sound to the end of the word.
  piglatin_output = ""
  str_array = str.split(" ")
  for word in str_array:
    vowels = ["a", "e", "i", "o", "u", "y"]
    rule_1 = False
    for i in vowels:
      if word[0] == i:
        rule_1 = True

    if rule_1==True:
      word += "ay"

    if rule_1 == False:
        word += word[0]
        word = word[1 : : ]
        word += "ay"
   
    piglatin_output += word + " "
    piglatin_output = piglatin_output[:-1]
    return piglatin_output


    # vowels = ["a", "e", "i", "o", "u", "y"]
    # rule_1 = False
    # for i in vowels:
    #   if word[0] == i:
    #     rule_1 = True

    # if rule_1==True:
    #   word = word + "ay"

    # if rule_1 == False:
    #     word = word + word[0]
    #     word = word[1 : : ]
    #     word = word + "ay"
    
    # return word