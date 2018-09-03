import unittest

class TestTokenMethods(unittest.TestCase):
    def test_set(self):
        self.assertEqual('foo'.upper(), 'FOp')

if __name__ == "__main__":
    unittest.main()