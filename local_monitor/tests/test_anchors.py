import unittest
from ..anchor.anchors import *

class TestFindAnchorPoint(unittest.TestCase):
    def runTest(self):
        self.assertEqual(find_anchor_point('san francisco'), 'place')
        self.assertEqual(find_anchor_point('atlanta'), 'place')
        self.assertEqual(find_anchor_point('brazil'),'place')
        self.assertEqual(find_anchor_point('toucan'), 'animal')
        self.assertEqual(find_anchor_point('cactus'), 'plant')
        self.assertEqual(find_anchor_point('mailbox'), 'object')
        #self.assertEqual(find_anchor_point('wind'), 'confusion')

if __name__ == '__main__':
    unittest.main()
