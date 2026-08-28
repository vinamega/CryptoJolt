# test_cryptojolt.py
"""
Tests for CryptoJolt module.
"""

import unittest
from cryptojolt import CryptoJolt

class TestCryptoJolt(unittest.TestCase):
    """Test cases for CryptoJolt class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoJolt()
        self.assertIsInstance(instance, CryptoJolt)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoJolt()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
