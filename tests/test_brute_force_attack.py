# tests/test_brute_force_attack.py

import unittest
from core.brute_force_attack import brute_force_attack

class TestBruteForceAttack(unittest.TestCase):
    def test_brute_force_attack(self):
        result = brute_force_attack('test_ssid', max_length=3)
        self.assertIn('Password', result)

if __name__ == '__main__':
    unittest.main()
