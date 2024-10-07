# tests/test_dictionary_attack.py

import unittest
from core.dictionary_attack import dictionary_attack

class TestDictionaryAttack(unittest.TestCase):
    def test_dictionary_attack(self):
        result = dictionary_attack('test_ssid', 'resources/dictionary.txt')
        self.assertIn('Password', result)

if __name__ == '__main__':
    unittest.main()
