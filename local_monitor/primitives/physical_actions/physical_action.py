from ..primitives import *
# There are five primitives for physical actions
# INGEST - to take something inside an animate object
# EXPEL - to take something from inside an animate object and force it out
# GRASP - to physically grasp an object
# MOVE - to move a body part
# PROPEL - to apply a force to
#
# TODO - Maybe we can move some of the "physical action constraints" here. 
class PhysicalAction(ACT):
    def constaints_violated(self):
        if violated:
            return self.constraints