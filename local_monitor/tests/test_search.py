import unittest
from .test import *
from ..conceptnet.search import *
#from ..primitives.search import *

class TestGetHops(unittest.TestCase):
    def runTest(self):
        print("trying to get hops")
        self.assertEqual(get_hops('penguin', 'animal'), 1)
        #self.assertEqual(get_hops('cactus', 'animal'), 0)
        
        #self.assertEqual(get_hops('cactus', 'plant'), 0)
        #self.assertEqual(get_hops('dinosaur', 'plant'), 0)

        #self.assertEqual(get_hops('chair', 'object'), 0)
        #self.assertEqual(get_hops('snow', 'object'), 0)

        #self.assertEqual(get_hops('san francisco', 'city'), 0)

        #self.assertEqual(get_hops('Maine', 'place'), 0)
        #self.assertEqual(get_hops('house', 'place'), 0)
        #self.assertEqual(get_hops('boy', 'place'), 0)

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


if __name__ == '__main__':
    print("Is this main being called?")
    unittest.main()
