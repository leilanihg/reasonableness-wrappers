import unittest
from explain import *
from local_monitor import *
import warnings
 
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


        
# Need to work on this one
#class TestIsAPath(unittest.TestCase):
#    def runTest(self):
#        self.assertEqual(find_IsA_path("penguin", "animal"))

# Still want explain non-relation?!! 

#class TestExplainNonRelation(unittest.TestCase):
#    def runTest(self):
#        return


if __name__ == '__main__':
    unittest.main()
