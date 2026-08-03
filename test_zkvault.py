# test_zkvault.py
"""
Tests for ZKVault module.
"""

import unittest
from zkvault import ZKVault

class TestZKVault(unittest.TestCase):
    """Test cases for ZKVault class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ZKVault()
        self.assertIsInstance(instance, ZKVault)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ZKVault()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
