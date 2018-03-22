from .physical_action import *

# A person, object or thing is taken from or comes from inside
# another person,  object, or thing and is forced out
class Expel(PhysicalAction):
    def check_constraints(self):
        return None

    def summary(self):
        print(self.subject, "is taken from inside", self.object, "and is forced out")
