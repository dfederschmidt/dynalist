import unittest

class TestTokenMethods(unittest.TestCase):
    def test_set(self):
        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == "__main__":
    unittest.main()