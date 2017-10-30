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


class TestHasIsAEdge(unittest.TestCase):
    def runTest(self):
        self.assertEqual(has_IsA_edge('penguin', 'animal'), True)
        self.assertEqual(has_IsA_edge('cactus', 'animal'), False)
        
        self.assertEqual(has_IsA_edge('cactus', 'plant'), True)
        self.assertEqual(has_IsA_edge('dinosaur', 'plant'), False)

        self.assertEqual(has_IsA_edge('chair', 'object'), True)
        self.assertEqual(has_IsA_edge('snow', 'object'), False)

        self.assertEqual(has_IsA_edge('san francisco', 'city'), True)

        self.assertEqual(has_IsA_edge('Maine', 'place'), True)
        self.assertEqual(has_IsA_edge('house', 'place'), True)
        self.assertEqual(has_IsA_edge('boy', 'place'), False)

class TestHasEdge(unittest.TestCase):
    def runTest(self):
        self.assertEqual(has_any_edge('penguin', 'animal'), True)
        self.assertEqual(has_any_edge('cactus', 'animal'), False)
        
        #self.assertEqual(has_any_edge('cactus', 'plant'), True)
        self.assertEqual(has_any_edge('dinosaur', 'plant'), False)

        self.assertEqual(has_any_edge('chair', 'object'), True)
        self.assertEqual(has_any_edge('snow', 'object'), False)

        self.assertEqual(has_any_edge('san francisco', 'city'), True)

        self.assertEqual(has_any_edge('Maine', 'place'), True)
        self.assertEqual(has_any_edge('house', 'place'), True)
        self.assertEqual(has_any_edge('boy', 'place'), False)

        self.assertEqual(has_any_edge('cross', 'action'), True)

class TestSearchRelation(unittest.TestCase):
    def runTest(self):
        self.assertEqual(search_relation('penguin', 'AtLocation'),['antarctica', 'a zoo'])
        self.assertEqual(search_relation('gorilla', 'AtLocation'),[])

class TestCleanSearch(unittest.TestCase):
    def runTest(self):
        self.assertEqual(clean_search("a city"), "city")
        self.assertEqual(clean_search("A CITY"), "city")

class TestFindIsAPath(unittest.TestCase):
    def runTest(self):
        self.assertEqual(find_IsA_path('san francisco', 'place'),
                         ['san_francisco', 'city', 'place'])
        self.assertEqual(find_IsA_path('atlanta', 'place'),
                         ['atlanta', 'city', 'place']) 
        # This test may need to be changed
        self.assertEqual(find_IsA_path('antartica', 'place'),
                         None)
        self.assertEqual(find_IsA_path('brazil', 'place'),
                         ['brazil', 'country', 'place'])
        self.assertEqual(find_IsA_path('toucan', 'animal'),
                         ['toucan', 'bird', 'animal'])
        self.assertEqual(find_IsA_path('toucan', 'place'),
                         None)
        self.assertEqual(find_IsA_path('cactus', 'plant'),
                         ['cactus', 'plant'])
        self.assertEqual(find_IsA_path('run', 'move'),
                         ['run', 'move'])
        self.assertEqual(find_IsA_path('mailbox', 'object'),
                         ['mailbox', 'container_product', 'object'])
        self.assertEqual(find_IsA_path('mailbox', 'plant'),
                         None)

class TestFindAnchorPoint(unittest.TestCase):
    def runTest(self):
        self.assertEqual(find_anchor_point('san francisco'), 'place')
        self.assertEqual(find_anchor_point('atlanta'), 'place')
        self.assertEqual(find_anchor_point('brazil'),'place')
        self.assertEqual(find_anchor_point('toucan'), 'animal')
        self.assertEqual(find_anchor_point('cactus'), 'plant')
        self.assertEqual(find_anchor_point('mailbox'), 'object')
        #self.assertEqual(find_anchor_point('wind'), 'confusion')

class TestIsActionVerb(unittest.TestCase):
    def runTest(self):
        self.assertEqual(is_action_verb('run'), True)
        #self.assertEqual(is_action_verb('talk'), False)
        self.assertEqual(is_action_verb('cross'), True)
        self.assertEqual(is_action_verb('is'), False)
        self.assertEqual(is_action_verb('raise'), True)
        self.assertEqual(is_action_verb('give'), True)

        self.assertEqual(is_action_verb('has'), False)
        self.assertEqual(is_action_verb('thinking'), False)
        # Add talk and stuff

# TODO - Next step
class TestFindLinkingVerb(unittest.TestCase):
    def runTest(self):
        self.assertEqual(is_linking_verb('is'), True)
        self.assertEqual(is_linking_verb('appearing'), True)
        self.assertEqual(is_linking_verb('smelled'), True)

        self.assertEqual(is_linking_verb('move'), False)
        self.assertEqual(is_linking_verb(''), False)
        self.assertEqual(is_linking_verb('dance'), False)

class TestFindHelpingVerb(unittest.TestCase):
    def runTest(self):
        self.assertEqual(is_helping_verb('is'), True)
        self.assertEqual(is_helping_verb('should'), True)
        self.assertEqual(is_helping_verb('have'), True)

        self.assertEqual(is_helping_verb('move'), False)
        self.assertEqual(is_helping_verb(''), False)
        self.assertEqual(is_helping_verb('smell'), False)

class TestIsPossessionVerb(unittest.TestCase):
    def runTest(self):
        self.assertEqual(is_possession_verb('is'), False)
        self.assertEqual(is_possession_verb('should'), False)
        self.assertEqual(is_possession_verb('have'), True)

        self.assertEqual(is_possession_verb('move'), False)
        self.assertEqual(is_possession_verb(''), False)
        self.assertEqual(is_possession_verb('smell'), False)

        self.assertEqual(is_possession_verb('have'), True)
        self.assertEqual(is_possession_verb('bought'), True)
        self.assertEqual(is_possession_verb('possess'), True)
        self.assertEqual(is_possession_verb('providing'), True)

class TestIsCommunicationVerb(unittest.TestCase):
    @ignore_warnings
    def runTest(self):
        self.assertEqual(is_communication_verb('is'), False)
        self.assertEqual(is_communication_verb('should'), False)
        self.assertEqual(is_communication_verb('have'), False)

        self.assertEqual(is_communication_verb('move'), False)
        self.assertEqual(is_communication_verb(''), False)
        self.assertEqual(is_communication_verb('smell'), False)

        self.assertEqual(is_communication_verb('talk'), True)
        self.assertEqual(is_communication_verb('told'), True)
        self.assertEqual(is_communication_verb('tell'), True)
        self.assertEqual(is_communication_verb('said'), True)
        self.assertEqual(is_communication_verb('talked'), True)


class TestVerbType(unittest.TestCase):
    @ignore_warnings
    def runTest(self):
        self.assertEqual(find_verb_type('is'), 'linking')
        self.assertEqual(find_verb_type('should'), 'helping')
        self.assertEqual(find_verb_type('have'), 'helping')

        self.assertEqual(find_verb_type('move'), 'action')
        self.assertEqual(find_verb_type(''), 'preposition')
        self.assertEqual(find_verb_type('smell'), 'linking')

        self.assertEqual(find_verb_type('talk'), 'communication')
        self.assertEqual(find_verb_type('told'), 'communication')
        self.assertEqual(find_verb_type('tell'), 'communication')
        self.assertEqual(find_verb_type('said'), 'communication')
        self.assertEqual(find_verb_type('talked'), 'communication')
        
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
