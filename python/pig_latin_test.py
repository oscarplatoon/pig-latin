# Rewrite this in Unit Test
import unittest
from pig_latin import translate

class PigTest(unittest.TestCase):

    def test_returns_a_string(self):
        self.assertTrue(type(translate("a")) == type("str"))

    def test_translates_leading_vowel(self):
        self.assertEqual(translate('apple'), 'appleay')

    def test_translates_beginning_consonant(self):
        self.assertTrue(translate('banana') == 'ananabay')
    
    def test_translates_beginning_two_consonants(self): 
        self.assertTrue(translate('cherry') == 'errychay')
    
    def test_translates_two_words(self):
        self.assertTrue(translate('eat pie') == 'eatay iepay')
# print(f"translates a word beginning with three consonants: {translate('three') == 'eethray'}")
# print(f"counts 'sch' as a single phoneme: {translate('school') == 'oolschay'}")
# print(f"counts 'qu' as a single phoneme: {translate('quiet') == 'ietquay'}")
# print(f"counts 'qu' as a consonant even when it's preceded by a consonant: {translate('square') == 'aresquay'}")
# print(f"translates many words: {translate('the quick brown fox') == 'ethay ickquay ownbray oxfay'}")

# # write a test asserting that capitalized words are still capitalized
# # (but with a different initial capital letter, of course) retain the
# # punctuation from the original phrase

if __name__ == '__main__':
    unittest.main()
