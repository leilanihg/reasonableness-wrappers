import unittest
from .main import *

# TODO most of these will not pass
class TestIngestVehiclePass(unittest.TestCase):
    def runTest(self):
        print("Testing things that vehicle can Ingest")
        object_sentence = test_main("car", "eat",  "gas")
        self.assertTrue(object_sentence, "Car can eat gas")

# TODO this is weird, a car can be full of people but it does not ingest them?
class TestIngestVehicleFail(unittest.TestCase):
    def runTest(self):
        print("Testing things that vehicle should not Ingest")
        # No Object sentence 
        object_sentence = test_main("car", "ingest",  "man")
        self.assertFalse(object_sentence, "Car cannot ingest a man")

class TestIngestPersonPass(unittest.TestCase):
    def runTest(self):
        print("Testing things that man can Ingest")
        # No Object sentence 
        no_object = test_main("man", "eat", None)
        self.assertTrue(no_object, "Man can eat")
        object_sentence = test_main("man", "eats",  "food")
        self.assertTrue(object_sentence, "Man can eat food")

class TestIngestPersonFail(unittest.TestCase):
    def runTest(self):
        print("Testing things that man can not Ingest")
        # No Object sentence 
        object_sentence = test_main("man", "eat",  "earthquake")
        self.assertFalse(object_sentence, "Man cannot eat an earthquake")


class TestIngestAnimalPass(unittest.TestCase):
    def runTest(self):
        print("Testing things that animal can Ingest")
        # No Object sentence 
        no_object = test_main("monkey", "eats", None)
        self.assertTrue(no_object, "monkey can eat")
        object_sentence = test_main("monkey", "eat",  "milk")
        self.assertTrue(object_sentence, "monkey can eat milk")

class TestIngestAnimalFail(unittest.TestCase):
    def runTest(self):
        print("Testing things that animal should not Ingest")
        # No Object sentence 
        object_sentence = test_main("turtle", "eat",  "air")
        self.assertFalse(object_sentence, "turtle cannot eat air")

class TestIngestPlantPass(unittest.TestCase):
    def runTest(self):
        print("Testing things that plant can Ingest")
        # No Object sentence 
        object_sentence = test_main("tree", "ingest", "water", ["hurricane"])
        self.assertTrue(object_sentence, "tree can ingest water in a hurricane")
        object_sentence_2 = test_main("flower", "ingests", "plant food", ["hurricane"])
        self.assertTrue(no_object, "flower can ingest plant food")

class TestIngestPlantFail(unittest.TestCase):
    def runTest(self):
        print("Testing things that plant should not Ingest")
        # No Object sentence 
        object_sentence = test_main("flower", "eats", "person")
        self.assertFalse(object_sentence, "flower cannot eat a person")
        # TODO thinks flower is a person

# TODO mailbox is filled with mail
# class TestIngestObjectPass(unittest.TestCase):
#     def runTest(self):
#         print("Testing things that object can Ingest")
#         # No Object sentence 
#         object_sentence = test_main("faucet", "eats", "water")
#         self.assertTrue(object_sentence, "faucet can leak water")

class TestIngestObjectFail(unittest.TestCase):
    def runTest(self):
        print("Testing things that object should not Ingest")
        # No Object sentence 
        no_object = test_main("laptop", "eats", None)
        self.assertFalse(no_object, "Laptop cannot Ingest without context")

# TODO can hurricanes move?
class TestIngestWeatherPass(unittest.TestCase):
    def runTest(self):
        print("Testing things that weather can Ingest")
        # No Object sentence 
        no_object = test_main("hurricane", "eat", "car")
        self.assertTrue(no_object, "Hurricanes can eat a car")
        # TODO They Ingest other objects
        # object_sentence = test_main("car", "move",  "man")
        # self.assertTrue(object_sentence, "Car can move man")

class TestIngestWeatherFail(unittest.TestCase):
    def runTest(self):
        print("Testing things that vehicle should not Ingest")
        # No Object sentence 
        no_object = test_main("earthquake", "eat", "water")
        self.assertFalse(no_object, "an earthquake cannot eat water")
        # object_sentence = test_main("car", "move",  "weather")
        # self.assertFalse(object_sentence, "Car cannot move weather")

if __name__ == '__main__':
    unittest.main()

# TODO: is fall a Ingest?
