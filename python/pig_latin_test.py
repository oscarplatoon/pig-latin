import unittest
from pig_latin import translate

class PigTest(unittest.TestCase):

    def test_1(self):
        self.assertEqual(translate('apple'),  'appleay')
    
    def test_2(self):
        self.assertEqual(translate('banana'), 'ananabay')
    
    def test_3(self):
        self.assertEqual(translate('cherry'), 'errychay')
    
    def test_4(self):
        self.assertEqual(translate('eat pie'), 'eatay iepay')

    def test_5(self):
        self.assertEqual(translate('three'), 'eethray')
    
    def test_6(self):
        self.assertEqual(translate('school'), 'oolschay')
    
    def test_7(self):
        self.assertEqual(translate('quiet'), 'ietquay')
    
    def test_8(self):
        self.assertEqual(translate('square'), 'aresquay')
    
    def test_9(self):
        self.assertEqual(translate('the quick brown fox'), 'ethay ickquay ownbray oxfay')

    

if __name__ == '__main__':
    unittest.main()
