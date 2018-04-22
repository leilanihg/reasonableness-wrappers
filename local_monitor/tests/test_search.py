import unittest
#from .test import *
from ..conceptnet.search import *

#class TestGeShortestIsAtHops(unittest.TestCase):
#    print("Trying to test hops")
#    def runTest(self):
#        print("HAI THERE")
#        self.assertEqual(get_shortest_IsA_hops('penguin', 'animal'), 1)
#        self.assertEqual(get_shortest_IsA_hops('cactus', 'animal'), 0)

class TestShortestHops(unittest.TestCase):
    def runTest(self):
        self.assertEqual(get_shortest_hops('penguin'), 
                         ('animal', ['penguin', 'animal']))
        self.assertEqual(get_shortest_hops('cactus'), 
                         ('plant', ['cactus', 'plant']))
        self.assertEqual(get_shortest_hops('san francisco'),
                         ('place', ['san francisco', 'city', 'place']))
        self.assertEqual(get_shortest_hops('atlanta'),
                         ('place', ['atlanta', 'city', 'place']) )
        self.assertEqual(get_shortest_hops('antartica'),
                         (None, None))
        self.assertEqual(get_shortest_hops('brazil'),
                         ('place', ['brazil', 'country', 'place']))
        self.assertEqual(get_shortest_hops('toucan'),
                         ('animal', ['toucan', 'bird', 'animal']))
        self.assertEqual(get_shortest_hops('mailbox'),
                         ('object', ['mailbox', 'box', 'object']))

class TestShortest(unittest.TestCase):
    def runTest(self):
        self.assertEqual(find_shortest_path('penguin', 'animal'), 
                         ['penguin', 'animal'])
        self.assertEqual(find_shortest_path('cactus', 'animal'), 
                         ['cactus', 'plant', 'animal'])
        self.assertEqual(find_shortest_path('cactus', 'plant'), 
                         ['cactus', 'plant'])
        self.assertEqual(find_shortest_path('san francisco', 'place'),
                         ['san francisco', 'city', 'place'])
        self.assertEqual(find_shortest_path('atlanta', 'place'),
                         ['atlanta', 'city', 'place']) 
        self.assertEqual(find_shortest_path('antartica', 'place'),
                         None)
        self.assertEqual(find_shortest_path('brazil', 'place'),
                         ['brazil', 'country', 'place'])
        self.assertEqual(find_shortest_path('toucan', 'animal'),
                         ['toucan', 'bird', 'animal'])
        self.assertEqual(find_shortest_path('toucan', 'place'),
                         None)
        self.assertEqual(find_shortest_path('run', 'move'),
                         ['run', 'move'])
        self.assertEqual(find_shortest_path('mailbox', 'object'),
                         ['mailbox', 'box', 'object'])
        self.assertEqual(find_shortest_path('mailbox', 'plant'),
                         ['mailbox', 'box', 'plant'])

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

if __name__ == '__main__':
    unittest.main()
