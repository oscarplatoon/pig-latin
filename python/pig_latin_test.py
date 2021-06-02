import unittest
from pig_latin import translate

class PigLatinTestCase(unittest.TestCase):
  
  def test_single_words(self):
    self.assertEqual({translate('apple'), 'appleay'})
    self.assertEqual({translate('banana'), 'ananabay'})
    self.assertEqual({translate('cherry'), 'errychay'})

  def test_mulitlpe_words(self):
    self.assertEqual({translate('fast car'), 'astfay arcay'})
    self.assertEqual({translate('eat pie'), 'eatay iepay'})


if __name__ == '__main__':
  unittest.main()

#print(f"translates a word beginning with three consonants: {translate('three') == 'eethray'}")
#print(f"counts 'sch' as a single phoneme: {translate('school') == 'oolschay'}")
#print(f"counts 'qu' as a single phoneme: {translate('quiet') == 'ietquay'}")
#print(f"counts 'qu' as a consonant even when it's preceded by a consonant: {translate('square') == 'aresquay'}")
#print(f"translates many words: {translate('the quick brown fox') == 'ethay ickquay ownbray oxfay'}")

# write a test asserting that capitalized words are still capitalized
# (but with a different initial capital letter, of course) retain the
# punctuation from the original phrase
