import unittest
from ..main import *

# TODO most of these will not pass
class TestExpelVehiclePass(unittest.TestCase):
    def runTest(self):
        print("Testing things that vehicle can Expel")
        object_sentence = test_main("car", "spill",  "gas")
        self.assertTrue(object_sentence, "Car can spill gas")

class TestExpelVehicleFail(unittest.TestCase):
    def runTest(self):
        print("Testing things that vehicle should not Expel")
        # No Object sentence 
        object_sentence = test_main("car", "spill",  "man")
        self.assertFalse(object_sentence, "Car cannot spill a man")

class TestExpelPersonPass(unittest.TestCase):
    def runTest(self):
        print("Testing things that man can Expel")
        # No Object sentence 
        no_object = test_main("man", "expel", None)
        self.assertTrue(no_object, "Man can expel")
        object_sentence = test_main("man", "expel",  "air")
        self.assertTrue(object_sentence, "Man can expel air")

class TestExpelPersonFail(unittest.TestCase):
    def runTest(self):
        print("Testing things that man can not Expel")
        # No Object sentence 
        object_sentence = test_main("man", "Expel",  "rain", context="hurricane")
        self.assertFalse(object_sentence, "Man cannot Expel rain in a hurricane")


class TestExpelAnimalPass(unittest.TestCase):
    def runTest(self):
        print("Testing things that animal can Expel")
        # No Object sentence 
        no_object = test_main("monkey", "throw up", None)
        self.assertTrue(no_object, "monkey can throw up")
        object_sentence = test_main("monkey", "leak",  "blood")
        self.assertTrue(object_sentence, "monkey can leak blood")

class TestExpelAnimalFail(unittest.TestCase):
    def runTest(self):
        print("Testing things that animal should not Expel")
        # No Object sentence 
        object_sentence = test_main("turtle", "expel",  "orange")
        self.assertFalse(object_sentence, "turtle cannot expel an orange")

class TestExpelPlantPass(unittest.TestCase):
    def runTest(self):
        print("Testing things that plant can Expel")
        # No Object sentence 
        object_sentence = test_main("tree", "expel", "leaves", ["hurricane"])
        self.assertTrue(object_sentence, "tree can expel leaves in a hurricane")
        object_sentence_2 = test_main("flower", "spill", "pollen", ["hurricane"])
        self.assertTrue(no_object, "flower can spill pollen")

class TestExpelPlantFail(unittest.TestCase):
    def runTest(self):
        print("Testing things that plant should not Expel")
        # No Object sentence 
        object_sentence = test_main("flower", "expel", "water")
        self.assertFalse(object_sentence, "flower cannot expel water")
        # TODO thinks flower is a person

class TestExpelObjectPass(unittest.TestCase):
    def runTest(self):
        print("Testing things that object can Expel")
        # No Object sentence 
        object_sentence = test_main("faucet", "leaks", "water")
        self.assertTrue(object_sentence, "faucet can leak water")

class TestExpelObjectFail(unittest.TestCase):
    def runTest(self):
        print("Testing things that object should not Expel")
        # No Object sentence 
        no_object = test_main("laptop", "expels", None)
        self.assertFalse(no_object, "Laptop cannot expel without context")

# TODO can hurricanes move?
class TestExpelWeatherPass(unittest.TestCase):
    def runTest(self):
        print("Testing things that weather can Expel")
        # No Object sentence 
        no_object = test_main("hurricane", "expel", "water")
        self.assertTrue(no_object, "Hurricanes can expel water")
        # TODO They Expel other objects
        # object_sentence = test_main("car", "move",  "man")
        # self.assertTrue(object_sentence, "Car can move man")

class TestExpelWeatherFail(unittest.TestCase):
    def runTest(self):
        print("Testing things that vehicle should not Expel")
        # No Object sentence 
        no_object = test_main("earthquake", "leaks", "water")
        self.assertFalse(no_object, "an earthquake cannot leak water")
        # object_sentence = test_main("car", "move",  "weather")
        # self.assertFalse(object_sentence, "Car cannot move weather")

if __name__ == '__main__':
    unittest.main()

# TODO: is fall a Expel?
