import unittest
from ..conceptnet.explain import *

#class SimpleWidgetTestCase(unittest.TestCase):
#    def setUp(self):
#        self.widget = Widget('The widget')

#class DefaultWidgetSizeTestCase(SimpleWidgetTestCase):
#    def runTest(self):
#        self.assertEqual(self.widget.size(), (50,50),
#                         'incorrect default size')

#class WidgetResizeTestCase(SimpleWidgetTestCase):
#    def runTest(self):
#        self.widget.resize(100,150)
#        self.assertEqual(self.widget.size(), (100,150),
#                         'wrong size after resize')


class TestISA(unittest.TestCase):
    def runTest(self):
        self.assertEqual(50,50)

class TestNotRelated(unittest.TestCase):
    def runTest(self):
        self.assertEqual(not_related("gorilla", "bamboo"), True)
        self.assertEqual(not_related("penguin", "bamboo"), True)
        self.assertEqual(not_related("penguin", "kosher"), True)
        self.assertEqual(not_related("cheese", "kosher"), True)
        self.assertEqual(not_related("corn", "kosher"), True)
        self.assertEqual(not_related("penguin", "bird"), False)
        self.assertEqual(not_related("bird", "penguin"), False)

class TestIsA(unittest.TestCase):
    def runTest(self):
        self.assertEqual(isA("bamboo", "plant"), 
                         ("bamboo", 'IsA', "plant"))

# Need to work on this one
#class TestHierarchyPath(unittest.TestCase):
#    def runTest(self):
#        self.assertEqual(find_hierarchy_path("penguin", "animal"))

# Still want explain non-relation?!! 

class TestTag(unittest.TestCase):
    def runTest(self):
        self.assertEqual(tag("A mailbox crossing the street"),
                         [('A', 'DT'), ('mailbox', 'NN'), 
                          ('crossing', 'VBG'), ('the', 'DT'), 
                          ('street', 'NN')])

class TestFindConcepts(unittest.TestCase):
    def runTest(self):
        tags = tag("A mailbox crossing the street")
        self.assertEqual(findConcepts(tags), ['mailbox', 'crossing', 'street'])

#class TestExplainNonRelation(unittest.TestCase):
#    def runTest(self):
#        return


if __name__ == '__main__':
    unittest.main()
