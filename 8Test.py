import unittest
import Lab8 as L

# Fråga om vad bugen ska göra

class TestTime(unittest.TestCase):

    def testReg(self):
        A, B = L.Sieve(120)
        print(B)
        self.assertEqual(len(A), 30)
        self.assertEqual(len(B), 89)


    def testThread(self):
        A, B = L.ThreadSieve(120)
        print(B)
        self.assertEqual(len(A), 30)
        self.assertEqual(len(B), 89)

if __name__ == "__main__":
    unittest.main()
