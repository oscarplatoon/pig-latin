# Rewrite this in Unit Test
import unittest
from pig_latin import translate

class PigLatinTestCases(unittest.TestCase):

    def test_case_1(self):
        output = translate('apple')
        self.assertEqual(output, 'appleay')

    def test_case_2(self):
        output = translate('banana')
        self.assertEqual(output, 'ananabay')

    def test_case_3(self):
        output = translate('cherry')
        self.assertEqual(output, 'errychay') 
    
    def test_case_4(self):
        output = translate('eat pie')
        self.assertEqual(output, 'eatay iepay')
    
    def test_case_5(self):
        output = translate('school')
        self.assertEqual(output, 'oolschay')
    
    def test_case_6(self):
        output = translate('quiet')
        self.assertEqual(output, 'ietquay')
    
    def test_case_7(self):
        output = translate('the quick brown fox')
        self.assertEqual(output, 'ethay ickquay ownbray oxfay')
    
    def test_case_8(self):
        output = translate('square')
        self.assertEqual(output, 'aresquay')
   
# print(f"translates a word beginning with a vowel: {translate('apple') == 'appleay'}")
# print(f"translates a word beginning with a consonant: {translate('banana') == 'ananabay'}")
# print(f"translates a word beginning with two consonants: {translate('cherry') == 'errychay'}")
# print(f"translates two words: {translate('eat pie') == 'eatay iepay'}")
# print(f"translates a word beginning with three consonants: {translate('three') == 'eethray'}")
# print(f"counts 'sch' as a single phoneme: {translate('school') == 'oolschay'}")
# print(f"counts 'qu' as a single phoneme: {translate('quiet') == 'ietquay'}")
# print(f"counts 'qu' as a consonant even when it's preceded by a consonant: {translate('square') == 'aresquay'}")
# print(f"translates many words: {translate('the quick brown fox') == 'ethay ickquay ownbray oxfay'}")

# write a test asserting that capitalized words are still capitalized
# (but with a different initial capital letter, of course) retain the
# punctuation from the original phrase

if __name__ == '__main__':
    unittest.main()

