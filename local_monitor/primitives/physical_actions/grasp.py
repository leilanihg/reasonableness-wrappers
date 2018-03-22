from .physical_action import *

# A person, object or thing grabs hold of another person,
# object or thing, or becomes attatched to another person
# object or thing
class Grasp(PhysicalAction):
    def __init__(self):
        self.grabs = False
    
    def check_constraints(self):
        return self.check_subject_constraints() and self.check_object_constraints()

    # Add support here
    def check_subject_constraints(self):
        anchor_point = get_animate(self.subject)
        if anchor_point != None:
            self.add_subject_support(self.subject, anchor_point, GRASP)
            return True
        else:
            self.add_subject_violation(self.subject, GRASP)
            return False

    # very naive check
    # beginning of adding in object constraints
    def check_object_constraints(self):
        if self.object == None:
            return True
        print("called object constraint")
        anchor_point = get_graspable(self.object, self.verbose)
        if anchor_point != None:
            self.add_object_support(self.object, anchor_point, GRASP) 
            return True
        else:
            violation = "A %s is not graspable." %(self.object)
            self.violations.append(violation)
            return False

