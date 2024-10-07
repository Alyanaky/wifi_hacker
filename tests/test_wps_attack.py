# tests/test_wps_attack.py

import unittest
from core.wps_attack import wps_attack

class TestWPSAttack(unittest.TestCase):
    def test_wps_attack(self):
        result = wps_attack('test_bssid', '12345670')
        self.assertIsInstance(result, str)

if __name__ == '__main__':
    unittest.main()
