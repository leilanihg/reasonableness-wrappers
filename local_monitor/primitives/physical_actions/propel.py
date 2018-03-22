from .physical_action import *

# A person, object or thing applies a force to another person,
# object or thing, or a moving person, object or thing
# strikes or impacts another person object or thing
# JM - more constraints
#    - The object must be a physical object, thing, substance or person
#    - The actor must be an "animate" object or thing capabale of applying
#      a force or momentum to another object
# TODO why is phys_object necessary for propel? 
class Propel(PhysicalAction):
    # TODO change name to be check_subject_constraints    
    def check_constraints(self):
        return self.check_subject_constraints() and self.check_object_constraints()

    def check_subject_constraints(self):
        anchor_point = get_propel(self.subject, self.verbose)
        if anchor_point != None:
            self.add_subject_support(self.subject, anchor_point, PROPEL)
            return True
        else:
            violation = "A %s is an object or thing that cannot move on its own." %(self.subject)
            self.violations.append(violation)
            return False

    def check_object_constraints(self):
        if self.object == None:
            return True
        if not is_confusion(self.object): 
            self.add_object_support(self.object, 'item', PROPEL)
            return True
        else:
            violation = "A %s cannot be propeled" %(self.object)
            self.violations.append(violation)
            return False