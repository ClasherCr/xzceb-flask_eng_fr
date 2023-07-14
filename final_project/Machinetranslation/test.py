import unittest
from translator import frenchToEnglish, englishToFrench

class TestE2F(unittest.TestCase):
    """English to French tests"""
    def test1(self):
        # Test Hello returns Bonjour
        self.assertEqual(englishToFrench('hello'), 'bonjour')
        # Test Hello does not return Hello
        self.assertNotEqual(englishToFrench('hello'), 'hello')

class TestF2E(unittest.TestCase):
    def test1(self):
        # Test Bonjour returns Hello
        self.assertEqual(frenchToEnglish('bonjour'), 'hello')
        # Test Bonjour does not return Bonjour
        self.assertNotEqual(frenchToEnglish('bonjour'), 'bonjour')

if __name__ == '__main__':
    unittest.main()
