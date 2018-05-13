import unittest
import warnings
from ...premise.premise import *
 
#from util.normalization import remove_repeating_chars
 
def ignore_warnings(test_func):
    def do_test(self, *args, **kwargs):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            test_func(self, *args, **kwargs)
    return do_test

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


class TestEnum(unittest.TestCase):
    def runTest(self):
        self.assertEqual(Relation.RelatedTo.name, "RelatedTo")


class TestSetRelationEnum(unittest.TestCase):
    def runTest(self):
        self.assertEqual(Premise("penguin", "RelatedTo", "Don't Care").relation, Relation.RelatedTo)
        self.assertEqual(Premise("penguin", "ExternalURL", "Don't Care").relation, Relation.ExternalURL)
        self.assertEqual(Premise("penguin", "IsA", "Don't Care").relation, Relation.IsA)
        self.assertEqual(Premise("penguin", "isA", "Don't Care").relation, Relation.IsA)
if __name__ == '__main__':
    unittest.main()
