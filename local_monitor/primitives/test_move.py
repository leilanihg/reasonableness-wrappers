import unittest
from .main import *

class TestMoveVehiclePass(unittest.TestCase):
    def runTest(self):
        print("Testing things that vehicle can move")
		# No Object sentence 
        no_object = test_main("car", "cross", None)
        self.assertTrue(no_object, "Car can cross")
        object_sentence = test_main("car", "drive",  "man")
        self.assertTrue(object_sentence, "Car can move man")

class TestMoveVehicleFail(unittest.TestCase):
    def runTest(self):
        print("Testing things that vehicle should not move")
        # No Object sentence 
        no_object = test_main("car", "swim", None)
        self.assertFalse(no_object, "Car cannot swim")
        object_sentence = test_main("car", "move",  "weather")
        self.assertFalse(object_sentence, "Car cannot move weather")

class TestMovePersonPass(unittest.TestCase):
    def runTest(self):
        print("Testing things that man can move")
        # No Object sentence 
        no_object = test_main("man", "run", None)
        self.assertTrue(no_object, "Man can run")
        object_sentence = test_main("man", "move",  "leg")
        self.assertTrue(object_sentence, "Man can move flower")

class TestMoveAnimalPass(unittest.TestCase):
    def runTest(self):
        print("Testing things that animal can move")
        # No Object sentence 
        no_object = test_main("penguin", "run", None)
        self.assertTrue(no_object, "penguin can run")
        object_sentence = test_main("giraffe", "move",  "neck")
        self.assertTrue(object_sentence, "giraffe can move neck")

class TestMovePlantPass(unittest.TestCase):
    def runTest(self):
        print("Testing things that plant can move")
        # No Object sentence 
        no_object = test_main("flower", "move", None, ["wind"])
        self.assertTrue(no_object, "Flower can move in the wind")

class TestMovePlantFail(unittest.TestCase):
    def runTest(self):
        print("Testing things that plant should not move")
        # No Object sentence 
        no_object = test_main("flower", "move", None)
        self.assertFalse(no_object, "Flower cannot move without context")

class TestMoveObjectPass(unittest.TestCase):
    def runTest(self):
        print("Testing things that object can move")
        # No Object sentence 
        no_object = test_main("mailbox", "cross", None, context=["hurricane"])
        self.assertTrue(no_object, "mailbox can move in a hurricane")

class TestMoveObjectFail(unittest.TestCase):
    def runTest(self):
        print("Testing things that object should not move")
        # No Object sentence 
        no_object = test_main("laptop", "move", None)
        self.assertFalse(no_object, "Laptop cannot move without context")

# TODO can hurricanes move?
class TestMoveWeatherPass(unittest.TestCase):
    def runTest(self):
        print("Testing things that weather can move")
        # No Object sentence 
        no_object = test_main("hurricane", "move", None)
        self.assertTrue(no_object, "Hurricanes can move")
        # TODO They propel other objects
        # object_sentence = test_main("car", "move",  "man")
        # self.assertTrue(object_sentence, "Car can move man")

class TestMoveWeatherFail(unittest.TestCase):
    def runTest(self):
        print("Testing things that vehicle should not move")
        # No Object sentence 
        no_object = test_main("hurricane", "swim", None)
        self.assertFalse(no_object, "Hurricane cannot swim")
        # object_sentence = test_main("car", "move",  "weather")
        # self.assertFalse(object_sentence, "Car cannot move weather")

if __name__ == '__main__':
    unittest.main()
