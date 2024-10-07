# tests/test_scanner.py

import unittest
from core.scanner import scan_networks

class TestScanner(unittest.TestCase):
    def test_scan_networks(self):
        networks = scan_networks()
        self.assertIsInstance(networks, list)
        for network in networks:
            self.assertIn('ssid', network)
            self.assertIn('bssid', network)
            self.assertIn('signal', network)
            self.assertIn('akm', network)

if __name__ == '__main__':
    unittest.main()
