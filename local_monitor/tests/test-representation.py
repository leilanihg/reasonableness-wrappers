import unittest
from ..primitives.representation import *


# A set of tests
# The angry bear chased the frightened little squirrel
# I sot an elephant in my pajamas
# He saw the fine fat trout in the brook
# My name is Leilani
# Mary has seen Bob
# Mary saw a dog
# A penguin crossing the street
# A penguin did cross the street
# The squirrel really was frightened
# The squirrel was really frightened
# The dog barked
# Joe put the fish on the log
# The prince and I read together
class TestVerbPrimitive(unittest.TestCase):
    def runTest(self):
        tester = """                                                                                       |
  S -> NP VP                                                                                         |
  VP -> V NP | V NP PP                                                                               |
  PP -> P NP""" 
        self.assertEqual(make_string_grammar([]), tester)

class TestPar

class TestStringBuilder(unittest.TestCase):
    def runTest(self):
        self.assertEqual(stringBuilder(['']), '')
        self.assertEqual(stringBuilder(['harry', 'met', 'sally']), 'harry met sally')
        self.assertEqual(stringBuilder(['when we', 'were', 'young']),
                         'when we were young')

if __name__ == '__main__':
    unittest.main()
