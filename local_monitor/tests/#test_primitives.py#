import unittest
from ..primitives.primitives import *

class TestVerbPrimitive(unittest.TestCase):
    def runTest(self):
        testObject = Move("Ben", "Sally")
        self.assertEqual(True, True)
        self.assertEqual(testObject.summary(), "Ben moves Sally")

class TestStringBuilder(unittest.TestCase):
    def runTest(self):
        self.assertEqual(stringBuilder(['']), '')
        self.assertEqual(stringBuilder(['harry', 'met', 'sally']), 'harry met sally')
        self.assertEqual(stringBuilder(['when we', 'were', 'young']),
                         'when we were young')

if __name__ == '__main__':
    unittest.main()
