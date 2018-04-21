import unittest
from .main import *

class TestPropelVehiclePass(unittest.TestCase):
    def runTest(self):
        print("Testing things that vehicle can propel")
        object_sentence = test_main("car", "propel",  "man")
        self.assertTrue(object_sentence, "Car can propel man")

class TestPropelVehicleFail(unittest.TestCase):
    def runTest(self):
        print("Testing things that vehicle should not propel")
        # No Object sentence 
        object_sentence = test_main("car", "push",  "weather")
        self.assertFalse(object_sentence, "Car cannot move weather")

class TestPropelPersonPass(unittest.TestCase):
    def runTest(self):
        print("Testing things that man can propel")
        # No Object sentence 
        no_object = test_main("man", "push", None)
        self.assertTrue(no_object, "Man can push")
        object_sentence = test_main("man", "throw",  "chair")
        self.assertTrue(object_sentence, "Man can throw a chair")

class TestPropelPersonFail(unittest.TestCase):
    def runTest(self):
        print("Testing things that man can not propel")
        # No Object sentence 
        object_sentence = test_main("man", "propel",  "rain", context="hurricane")
        self.assertFalse(object_sentence, "Man cannot propel rain in a hurricane")


class TestPropelAnimalPass(unittest.TestCase):
    def runTest(self):
        print("Testing things that animal can propel")
        # No Object sentence 
        no_object = test_main("monkey", "throw", None)
        self.assertTrue(no_object, "monkey can throw")
        object_sentence = test_main("monkey", "push",  "orange")
        self.assertTrue(object_sentence, "monkey can push an orange")

class TestPropelAnimalFail(unittest.TestCase):
    def runTest(self):
        print("Testing things that animal should not propel")
        # No Object sentence 
        object_sentence = test_main("turtle", "propel",  "weather")
        self.assertFalse(object_sentence, "turtle cannot propel weather")

class TestPropelPlantPass(unittest.TestCase):
    def runTest(self):
        print("Testing things that plant can propel")
        # No Object sentence 
        no_object = test_main("tree", "hit", "car", ["hurricane"])
        self.assertTrue(no_object, "tree can hit a car in a hurricane")

class TestPropelPlantFail(unittest.TestCase):
    def runTest(self):
        print("Testing things that plant should not propel")
        # No Object sentence 
        no_object = test_main("flower", "hit", None)
        self.assertFalse(no_object, "flower cannot hit without context")
        # TODO thinks flower is a person

class TestPropelObjectPass(unittest.TestCase):
    def runTest(self):
        print("Testing things that object can propel")
        # No Object sentence 
        no_object = test_main("mailbox", "hit", "man", context=["hurricane"])
        self.assertTrue(no_object, "mailbox can hit a man in a hurricane")

class TestPropelObjectFail(unittest.TestCase):
    def runTest(self):
        print("Testing things that object should not propel")
        # No Object sentence 
        no_object = test_main("laptop", "fall", None)
        self.assertFalse(no_object, "Laptop cannot fall without context")

# TODO can hurricanes move?
class TestPropelWeatherPass(unittest.TestCase):
    def runTest(self):
        print("Testing things that weather can propel")
        # No Object sentence 
        no_object = test_main("hurricane", "propel", "man")
        self.assertTrue(no_object, "Hurricanes can propel a man")
        # TODO They propel other objects
        # object_sentence = test_main("car", "move",  "man")
        # self.assertTrue(object_sentence, "Car can move man")

class TestPropelWeatherFail(unittest.TestCase):
    def runTest(self):
        print("Testing things that vehicle should not propel")
        # No Object sentence 
        no_object = test_main("earthquake", "move", "rain")
        self.assertFalse(no_object, "an earthquake cannot move the rain")
        # object_sentence = test_main("car", "move",  "weather")
        # self.assertFalse(object_sentence, "Car cannot move weather")

if __name__ == '__main__':
    unittest.main()

# TODO: is fall a propel?
